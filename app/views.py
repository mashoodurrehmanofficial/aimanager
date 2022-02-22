import enum
from django.shortcuts import render,redirect,HttpResponse ,HttpResponseRedirect
from .models import *
from django.views.decorators.csrf import csrf_exempt 
import os,shutil 
from datetime import datetime 
from wsgiref.util import FileWrapper
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .data_file import *
from .pdfReportGenerator import generatePdfReport
from django.forms.models import model_to_dict
from datetime import datetime
# Create your views here.

@login_required(login_url="login_router")
def index(request):
    return render(request, 'app/index.html' ) 


 



@login_required(login_url="login_router")
def manage_customers(request):
    context = {}
    all_customers = CustomerProfile.objects.all().values()
    all_customers = [x for x in all_customers]
    for customer_index,customer in enumerate(all_customers):
        all_customers[customer_index]['enrolled_program'] = None
        
        enrolled_programs = CustomerProfile.ai_program.through.objects.filter(customerprofile_id=int(customer['id'])).values() 
        enrolled_programs = [int(x['ai_program_id']) for x  in enrolled_programs]
        enrolled_programs = AI_Program.objects.filter(id__in=enrolled_programs).order_by('-start_date','finished')
        if enrolled_programs:
            all_customers[customer_index]['enrolled_program'] = enrolled_programs[0] 
        # all_customers[customer_index]['ai_program'] = AI_Program.objects.get(id=int(customer['ai_program_id']))
        try:
            all_customers[customer_index]['property'] = Property.objects.get(id=int(customer['property_id']))
        except:
            all_customers[customer_index]['property'] = None
            
        pass
        
    context['title'] = "Manage Customers"
    
    total_customers_with_enrolled_programs = len([x for x in all_customers if x['enrolled_program'] is not None])
    print("total_customers_with_enrolled_programs = ",total_customers_with_enrolled_programs)
    
    context['all_customers'] = all_customers 
    context['total_customers_with_enrolled_programs'] = total_customers_with_enrolled_programs  
    return render(request, 'app/manage_customers.html' ,context) 





@login_required(login_url="login_router")
def manage_cows(request,property_id=None):
    context = {}
    required_property = Property.objects.filter(id=property_id)
    if required_property:
        required_property = required_property.first()
    
    if property_id:
        all_cows = CowTable.objects.filter(property__id=int(property_id))
    else:
        all_cows = CowTable.objects.all()
    all_cows = all_cows.values()
    # for cow_index, cow in enumerate(all_cows):
    #     required_property = Property.objects.filter(cows__id = cow['id'])
    #     if required_property:
    #         all_cows[cow_index]['property'] = required_property.first()
    #     else:
    #         all_cows[cow_index]['property'] = None
            
        
    context['title'] = "Manage Cows"
    context['all_cows'] = all_cows  
    context['required_property'] = required_property  
    return render(request, 'app/manage_cows.html' ,context) 




@login_required(login_url="login_router")
def edit_cow(request,cow_id=None,property_id=None):
    print("id = ",cow_id)
    print("id = ",request.method)
    
    if request.method=='POST':
        cow_nlsid = request.POST['cow_nlsid']
        cow_vid = request.POST['cow_vid']
        condition_score = request.POST['condition_score']
        cow_weight = request.POST['cow_weight']
        cow_imf = request.POST['cow_imf']
        cow_ema = request.POST['cow_ema']
        cow_breed = request.POST['cow_breed']
        cow_interaction = request.POST['cow_interaction']
        cow_note = request.POST['cow_note']
        
        if cow_id:
            required_cow = CowTable.objects.get(id=cow_id)
        else:
            required_cow = CowTable()
        
        required_cow.nlsid = cow_nlsid
        required_cow.vid = cow_vid
        required_cow.condition_score = condition_score
        required_cow.weight = cow_weight
        required_cow.imf = cow_imf
        required_cow.ema = cow_ema
        required_cow.breed = cow_breed
        required_cow.interaction = cow_interaction
        required_cow.note = cow_note
        required_cow.save()
        required_property = Property.objects.get(id=property_id)
        print(required_property)
        required_property.cows.add(required_cow)
        print("required cow = ", required_cow.id)
        
        return redirect(f'/manage_properties/edit_property/{required_property.id}/manage_cows')
            
    
    
    required_cow = None
    required_property = None
    avaliable_properties = []
    context = {} 
    if cow_id:
        required_cow = CowTable.objects.filter(id=cow_id)
        if required_cow:
            required_cow = required_cow.first()
            required_property = Property.objects.filter(cows__id=int(cow_id)) 
            if required_property:
                required_property = required_property.first()
        context['title'] = "Edit Cow"
    else: 
        context['title'] = "Add Cow" 
    
    avaliable_properties = Property.objects.all()
    context['required_cow'] = required_cow
    context['required_property'] = required_property
     
    
    context['avaliable_properties'] = avaliable_properties 
    context['available_breed_types']    = list(AVAILABLE_BREED_TYPES) , 
     
    
    return render(request, 'app/edit_cow.html' ,context) 




def generateAIProgramDateListing(record):
    
    data = [
        {'display_name':"CIDRS In", 'id': 'seeder','day':0, 'date': record.cidrs_in_date,'status':record.cidrs_in_status },
        {'display_name':"PG Injection", 'id': 'pg_injection','day':2, 'date': record.pg_injection_date,'status':record.pg_injection_status },
        {'display_name':"Bomerol", 'id': 'bomerol', 'day':6, 'date': record.bomerol_date,'status':record.bomerol_status },
        {'display_name':"CIDRS Out", 'id': 'cidrs_out','day':8, 'date': record.cidrs_out_date,'status':record.cidrs_out_status },
        {'display_name':"Insemination", 'id': 'insemination','day':10, 'date': record.insemination_date,'status':record.insemination_status }, 
        {'display_name':"Pregnancy Test", 'id': 'pregnancy_test','day':46, 'date': record.pregnancy_test_date,'status':record.pregnancy_test_status }, 
    ]
    for index,entry in enumerate(data):
        data[index]['date'] = datetime.strptime(str(entry['date']), "%Y-%m-%d").strftime("%d/%m/%Y") 
    
    return data




@login_required(login_url="login_router")
def edit_ai_program(request,ai_program_id=None,customer_id=None):
    
    if request.method == 'POST':
        required_customer = CustomerProfile.objects.get(id=customer_id)
        if ai_program_id:
            required_ai_program = AI_Program.objects.get(id=int(ai_program_id))
        else:
            required_ai_program = AI_Program()
        
        
        proposed_start      = request.POST['proposed_start'] 
        program_finished    = request.POST['program_finished'] 
        proposed_start      = datetime.strptime(proposed_start, '%Y-%m-%d').date() 
        
        program_finished        = True if request.POST['program_finished']         == 'on' else False
        seeder_status           = True if request.POST['seeder_status']         == 'on' else False
        bomerol_status           = True if request.POST['bomerol_status']         == 'on' else False
        pg_injection_status             = True if request.POST['pg_injection_status']           == 'on' else False
        cidrs_out_status      = True if request.POST['cidrs_out_status']    == 'on' else False
        insemination_status     = True if request.POST['insemination_status']   == 'on' else False
        insemination_status     = True if request.POST['insemination_status']   == 'on' else False
        pregnancy_test_status   = True if request.POST['pregnancy_test_status']   == 'on' else False
         
        decisions = [
            proposed_start!=required_ai_program.start_date,
            required_ai_program.cidrs_in_status != seeder_status,
            required_ai_program.pg_injection_status != pg_injection_status,
            required_ai_program.bomerol_status != bomerol_status,
            required_ai_program.cidrs_out_status != cidrs_out_status,
            required_ai_program.insemination_status != insemination_status, 
            required_ai_program.finished != program_finished, 
        ] 
        print(pg_injection_status)
        if any(decisions):
            predicted_dates_data = generateAIProgramDateListing(AI_Program.objects.get(id=int(required_ai_program.id))) 
            generatePdfReport( 
                customer_name=required_customer.name,
                customer_email=required_customer.email,
                customer_property_name=required_customer.property.name,
                customer_billing_address=required_customer.billing_address,
                dates=predicted_dates_data
            )
            print("-> Send Email")
        else:
            print("-> Don't send email") 
            
        required_ai_program.start_date                  = proposed_start
        required_ai_program.cidrs_in_status             = seeder_status
        required_ai_program.pg_injection_status         = pg_injection_status
        required_ai_program.bomerol_status              = bomerol_status
        required_ai_program.cidrs_out_status            = cidrs_out_status
        required_ai_program.insemination_status         = insemination_status
        required_ai_program.pregnancy_test_status       = pregnancy_test_status
        required_ai_program.finished                    = program_finished
        
        required_ai_program.save() 
        required_customer.ai_program.add(required_ai_program) 
        
        
        
        
        return redirect(f'/manage_customers/edit_customer/{customer_id}')
        
    
    
    
    context = {}  
    required_ai_program = None
    required_customer = None
    required_property = None
    predicted_dates_data = None
    available_customers = []
    if ai_program_id: 
        required_ai_program = AI_Program.objects.filter(id=ai_program_id)
        if required_ai_program:
            required_ai_program = required_ai_program.first() 
            required_customer = CustomerProfile.objects.filter(ai_program__id=int(ai_program_id)) 
            if required_customer:
                required_customer = required_customer.first()
                required_property = required_customer.property
            else: 
                required_customer = CustomerProfile.objects.get(id=customer_id)
                required_property = required_customer.property
                
        context['title'] = "Edit AI Program"
    else: 
        required_customer = CustomerProfile.objects.get(id=customer_id)
        required_property = required_customer.property
        temp_ai_program = AI_Program(start_date= datetime.now().date())
        temp_ai_program.save()
        required_ai_program = temp_ai_program
        context['title'] = "Add AI Program" 
    
    
    
    if required_ai_program: 
        predicted_dates_data = generateAIProgramDateListing(required_ai_program)
        print("Dates")
        print(predicted_dates_data)
  
        
        required_ai_program = model_to_dict(required_ai_program)
        for key,val in required_ai_program.items():
            if 'date' in key and 'status' not in key: 
                required_ai_program[key] = str(val)
                # required_ai_program[key] = datetime.strptime(str(val), "%Y-%m-%d").strftime("%d/%m/%Y") 
    

    
    
    
    available_customers = CustomerProfile.objects.filter(Q(ai_program=None))  
    context['required_ai_program']  = required_ai_program
    context['required_customer']    = required_customer
    context['required_property']    = required_property 
    context['available_customers']    = available_customers 
    context['predicted_dates_data']    = predicted_dates_data , 
    
     
    
    
    
    try:
        temp_ai_program.delete()
    except:
        pass
     
    return render(request, 'app/edit_ai_program.html' ,context) 











@login_required(login_url="login_router")
def edit_customer(request,id=None):
    print("id = ",id)
    print("id = ",request.method)
    
    if request.method == "POST":
        customer_name = request.POST['customer_name']
        customer_email = request.POST['email']
        customer_mobile_number = request.POST['mobile_number']
        customer_abn = request.POST['customer_abn']
        property_pic = request.POST['property_pic']
        property_address = request.POST['property_address']
        property_state = request.POST['property_state']
        property_postcode = request.POST['property_postcode']
        billing_address = request.POST['billing_address']
        billing_state = request.POST['billing_state']
        billing_postcode = request.POST['billing_postcode']
        property_name = request.POST['property_name']
        
        if id:
            required_customer = CustomerProfile.objects.get(id=int(id))
        else:
            required_customer = CustomerProfile()
        
        required_customer.name                  = customer_name 
        required_customer.email                 = customer_email 
        required_customer.mobile_number         = customer_mobile_number 
        required_customer.abn                   = customer_abn 
        required_customer.property_address      = property_address 
        required_customer.property_state        = property_state 
        required_customer.property_postcode     = property_postcode 
        required_customer.billing_address       = billing_address 
        required_customer.billing_state         = billing_state 
        required_customer.billing_postcode      = billing_postcode 
        required_customer.save()
        
        
        
        if required_customer.property:
            required_property = required_customer.property
        else:
            required_property = Property()
        
        required_property.name = property_name
        required_property.pic = property_pic
        required_property.save()
        
        required_customer.property = required_property
        required_customer.save() 
    
        return redirect(f'/manage_customers')
    
    
    
    context = {}
    context['available_states'] = AVAILABLE_STATES 
    avaliable_properties = list(Property.objects.filter(customerprofile__name=None).values()) 
    required_customer = None 
    enrolled_programs = []
    if id:
        required_customer = CustomerProfile.objects.filter(id=int(id))
        if required_customer:
            required_customer = required_customer.first() 
            enrolled_programs = CustomerProfile.ai_program.through.objects.filter(customerprofile_id=int(required_customer.id)).values() 
            enrolled_programs = [int(x['ai_program_id']) for x  in enrolled_programs]
            enrolled_programs = AI_Program.objects.filter(id__in=enrolled_programs).order_by('-start_date','finished') 
            print(enrolled_programs) 
        context['title'] = "Edit Customer"
    else:
        context['title'] = "Add Customer"
         
    context['enrolled_programs'] = enrolled_programs
    context['avaliable_properties'] = avaliable_properties
    context['required_customer'] = required_customer
     
    
    return render(request, 'app/edit_customer.html',context ) 











# Router for Adding/Editing a Property
@login_required(login_url="login_router")
def edit_property(request,id=None): 
    context = {}
    if request.method=="POST":
        property_name = request.POST['property_name']
        property_pic = request.POST['property_pic']
        required_property = Property.objects.get(id=id)
        required_property.pic = property_pic
        required_property.name = property_name
        required_property.save()
        return redirect(f'/manage_properties')
    
    
    context['available_states'] = AVAILABLE_STATES  
    required_property = None 
    required_customer = None
    avaliable_customers = []
    if id:
        required_property = Property.objects.filter(id=int(id)) 
        if required_property:
            required_property = required_property.first()
            required_customer = CustomerProfile.objects.filter(id=int(required_property.id)) 
            if required_customer:
                required_customer = required_customer.first()
        avaliable_customers = list(CustomerProfile.objects.filter(Q(property__id=None) | Q(property__id=None)).values()) + list(CustomerProfile.objects.filter(id=int(required_property.id)).values()) 
        context['title'] = "Edit Customer"
    else:
        avaliable_customers = list(CustomerProfile.objects.filter(property__id=None).values())
        context['title'] = "Add Customer"
        
         
     
    
    print("Availabale Cusotmer = ",avaliable_customers)
    print("Required Cusotmer = ", required_customer)      
    context['required_property'] = required_property 
    context['required_customer'] = required_customer 
    context['avaliable_customers'] = [required_customer]
    # context['avaliable_customers'] = avaliable_customers[::-1]
    
    print(avaliable_customers)
     
     
     
    return render(request, 'app/edit_property.html',context ) 










def manage_properties(request):
    context = {}
    avaialable_properties = Property.objects.all().values() 
    context['title'] = "Property Listing"
    for property_index,property in enumerate(avaialable_properties): 
        try:
            avaialable_properties[property_index]['customer'] = CustomerProfile.objects.get(property__id=property['id'])
        except:
            avaialable_properties[property_index]['customer'] = None

        try:
            avaialable_properties[property_index]['cows'] = Property.cows.through.objects.filter(property_id=property['id'])
        except:
            avaialable_properties[property_index]['cows'] = None
            
     
     
    print(avaialable_properties) 
    context['avaialable_properties'] = avaialable_properties
    return render(request, 'app/manage_properties.html',context ) 
    





















def login_router(request):  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print("-->", user)
        if user is not None:
            login(request, user) 
            return redirect('/')
        else: 
            return redirect('login_router')
 
    return render(request, 'accounts/login.html' ) 

def logout_router(request):    
    logout(request)
    return redirect('login_router')

