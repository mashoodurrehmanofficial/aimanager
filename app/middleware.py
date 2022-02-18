 
from app.views import edit_customer, edit_property
from .models import *
from django.contrib.auth.models import User
from django.conf import settings

from django.contrib.auth import authenticate, login,logout 
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404,HttpResponseRedirect
  

from django.urls import reverse

def context_processor(request):   
    current_absolute_url = str(request.build_absolute_uri())
    current_child_url = request.META.get('PATH_INFO', None)
    
    
    current_child_url = current_child_url[1:] if str(current_child_url).startswith('/') else current_child_url
    
    context = {}
    breadcrump_paths = []
    
    breadcrump_paths.append({'display_name':'Dashboard', 'url': ''})
    
    
    
    
    if [x for x in  ['manage_customers','edit_customer','add_customer'] if x in current_child_url] :  
        context['base_navigation_panel'] = "customer"  
        context['breadcrump_main_display_name'] = "Customers"  
        if 'manage_customer' in current_child_url:
            breadcrump_paths.append({'display_name':'Manage Customers', 'url': 'manage_customers'}) 
            
            if 'edit_customer' in current_child_url and [x for x in ['ai_program'] if x not in current_child_url]:
                breadcrump_paths.append({'display_name':'Edit Customer'})
            elif 'add_customer' not in current_child_url:
                edit_customer_path = str(current_child_url).split('edit_ai_program') if 'edit_ai_program' in current_child_url else  str(current_child_url).split('add_ai_program')
                edit_customer_path = edit_customer_path[0]
                breadcrump_paths.append({'display_name':'Edit Customer','url':edit_customer_path})
                
                if 'add_ai_program' in current_child_url:
                    breadcrump_paths.append({'display_name':'Add AI Program', 'url':current_child_url})
                
                if 'edit_ai_program' in current_child_url:
                    breadcrump_paths.append({'display_name':'Edit AI Program', 'url':current_child_url})
                     
                 
            if 'add_customer' in current_child_url:
                breadcrump_paths.append({'display_name':'Add Customer'})
                
                
            
        
         
    
    if [x for x in  ['manage_properties','edit_property','add_property'] if x in current_child_url] : 
        context['breadcrump_main_display_name'] =  "Property" 
        context['base_navigation_panel'] = "property"  
        
        if 'manage_properties' in current_child_url:
            breadcrump_paths.append({'display_name':'Manage Properties', 'url': 'manage_properties'}) 
        
            if 'edit_property' in current_child_url and 'manage_cows' not in current_child_url:
                breadcrump_paths.append({'display_name':'Edit Property', 'url': current_child_url })
            
            if 'manage_cows' in current_child_url:
                edit_property_path  = current_child_url.split('manage_cows')[0]
                breadcrump_paths.append({'display_name':'Edit Property', 'url': edit_property_path })
                breadcrump_paths.append({'display_name':'Manage Cows', 'url':  edit_property_path+ 'manage_cows'})
                
                if 'edit_cow' in current_child_url:
                    breadcrump_paths.append({'display_name':'Edit Cow', 'url':  current_child_url})
                elif 'add_cow' in current_child_url:
                    breadcrump_paths.append({'display_name':'Add Cow', 'url':  current_child_url})
                    
       
    
    
    
    
    
    
    
    
    print(current_child_url)
    print(breadcrump_paths)
    print('context') 
        
        
         
    for path_index,path in enumerate(breadcrump_paths):
        if 'url' in list(path.keys()): 
            breadcrump_paths[path_index]['url'] = path['url'][:-1] if str(path['url']).endswith('/') else path['url'] 
       
    
    
    context['breadcrump_paths'] = breadcrump_paths
    return context









 
from django.http import HttpResponse,HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin

class CustomMiddleware(MiddlewareMixin):
    
    def _init_(self, get_response):
        self.get_response = get_response

    # Code that is executed in each request before the view is called
    # def _call_(self, request):
    #     response = self.get_response(request)
    #     # Code that is executed in each request after the view is called
    #     return response
 
 
 
    # This code is executed if an exception is raised
    def process_request(self, request):
        pass
        # print("incoming url = ",incoming_url)
        # incoming_url = request.build_absolute_uri()
        # if  'dashboard' in incoming_url  or 'login' in incoming_url or  'bussiness_admin' in incoming_url: 
        #     if manageOtp(request): 
        #         print("---> ACCOUNT LOCKED !") 
        #         return HttpResponsePermanentRedirect(f"{settings.DOMAIN}accounts/authotp")

        #     required_user = request.user 
        #     if 'bussiness_admin' in incoming_url and not  required_user.is_superuser and required_user.is_authenticated:
        #         logout(request)
        #         return redirect("bussiness_admin/pwzg")
        #     elif 'login' in incoming_url and required_user.is_superuser and required_user.is_authenticated:
        #         print(incoming_url, "-->",required_user.is_superuser)
        #         logout(request)
        #         return redirect("login_register")
        
 

 