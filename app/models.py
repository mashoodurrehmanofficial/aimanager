
from datetime import datetime,timedelta 
from statistics import mode
from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_save,pre_save 
from django.dispatch import receiver
from .data_file import * 
from django.core.validators import MaxValueValidator,RegexValidator

AVAILABLE_INTERACTIONS =  tuple([(x,x) for x in AVAILABLE_INTERACTIONS])
AVAILABLE_BREED_TYPES =  tuple([(x,x) for x in AVAILABLE_BREED_TYPES])


class CowTable(models.Model):
    nlsid           = models.CharField(max_length=16,default='',verbose_name="NLSID",validators=[RegexValidator(r'^\w+[A-Za-z0-9]{15}')],) 
    vid             = models.CharField(max_length=20,default='',blank=True,null=True,verbose_name="VID") 
    weight          = models.FloatField(default=0,blank=True,null=True,verbose_name="Weight") 
    condition_score = models.CharField(max_length=1,default='',blank=True,null=True, validators=[RegexValidator(r'^\d{0,9}$')],verbose_name="Condition Score")
    imf             = models.CharField(max_length=20,default='',blank=True,null=True,verbose_name="IMF") 
    ema             = models.CharField(max_length=20,default='',blank=True,null=True,verbose_name="EMA") 
    note            = models.TextField(default='',blank=True,null=True,verbose_name="Note") 
    breed           = models.CharField(max_length=2000,default='',blank=True,null=True,choices=AVAILABLE_BREED_TYPES,verbose_name="Breed") 
    interaction     = models.CharField(max_length=2000,default='',blank=True,null=True,verbose_name="Interaction" ) 
    
    def __str__(self):
        return  f"{self.nlsid}"
    





class Property(models.Model):
    name    = models.CharField(max_length=20,default='',blank=True,null=True,verbose_name="Property Name") 
    pic     = models.CharField(max_length=8,default='',blank=True,null=True,verbose_name="PIC (Property Identofication Code)") 
    cows    = models.ManyToManyField(CowTable,blank=True)
    def __str__(self):
        return  f"{self.name} - {self.pic}"
    class Meta:
        verbose_name = "Properties"
    
    
class AI_Program(models.Model):
    start_date                  = models.DateField(default=now,verbose_name='') 
    cidrs_in_date       = models.DateField(default=now,verbose_name='CIDRS In') 
    pg_injection_date        = models.DateField(default=now,verbose_name='PG Injection') 
    bomerol_date                   = models.DateField(default=now,verbose_name='Bomerol') 
    cidrs_out_date        = models.DateField(default=now,verbose_name='CIDRS Out') 
    insemination_date           = models.DateField(default=now,verbose_name='Insemination') 
    pregnancy_test_date         = models.DateField(default=now,verbose_name='Pregnancy Test') 
    
    
    cidrs_in_status       = models.BooleanField(default=False) 
    pg_injection_status        = models.BooleanField(default=False) 
    bomerol_status                   = models.BooleanField(default=False) 
    cidrs_out_status          = models.BooleanField(default=False) 
    insemination_status           = models.BooleanField(default=False) 
    pregnancy_test_status         = models.BooleanField(default=False)  
    last_completed_action  = models.CharField(max_length=8,default='N/A',blank=True,null=True,verbose_name="Last completed action")  
    finished                    = models.BooleanField(default=False)
    def __str__(self):
        return  f"{self.start_date}"
    
    
    
    
    


@receiver(pre_save , sender=AI_Program, dispatch_uid="save_update_ai_program_dates")
def save_update_ai_program_dates(sender, instance, **kwargs): 
    instance.cidrs_in_date  = instance.start_date  + timedelta(days=0)
    instance.pg_injection_date   = instance.start_date  + timedelta(days=2)
    instance.bomerol_date              = instance.start_date  + timedelta(days=3)
    instance.cidrs_out_date     = instance.start_date  + timedelta(days=8)
    instance.insemination_date      = instance.start_date  + timedelta(days=10)
    instance.pregnancy_test_date    = instance.start_date  + timedelta(days=46) 
    try:
        instance._pre_save_instance = AI_Program.objects.get(pk=instance.pk)
    except AI_Program.DoesNotExist: 
        instance._pre_save_instance = instance
    
    last_completed_action = instance._pre_save_instance.last_completed_action
    
    if instance._pre_save_instance.start_date!= instance.start_date:
        last_completed_action = 'Start Date'
    
    if instance._pre_save_instance.cidrs_in_status!= instance.cidrs_in_status:
        last_completed_action = 'CIDRS In'
    
    if instance._pre_save_instance.pg_injection_status!= instance.pg_injection_status:
        last_completed_action = 'PG Injection'
    
    if instance._pre_save_instance.bomerol_status!= instance.bomerol_status:
        last_completed_action = 'Bomerol'
    
    if instance._pre_save_instance.cidrs_out_status!= instance.cidrs_out_status:
        last_completed_action = 'CIDRS Out'
     
    if instance._pre_save_instance.insemination_status!= instance.insemination_status:
        last_completed_action = 'Insemination'
    if instance._pre_save_instance.pregnancy_test_status!= instance.pregnancy_test_status:
        last_completed_action = 'Pregnancy Test'
    
        
        
    
    instance.last_completed_action = last_completed_action
    


 

AVAILABLE_STATES =  tuple([(x,x) for x in AVAILABLE_STATES])


class CustomerProfile(models.Model):
    name                = models.CharField(max_length=500,default='',blank=True,null=True)
    email               = models.CharField(max_length=500,default='',blank=True,null=True)
    mobile_number       = models.CharField(max_length=15,default='',blank=True,null=True, validators=[RegexValidator(r'^\d[0-9]..\s\d[0-9].\s\d[0-9].')])
    property_address    = models.CharField(max_length=20,default='',blank=True,null=True)
    property_suburb     = models.CharField(max_length=20,default='',blank=True,null=True)
    property_state      = models.CharField(max_length=20,default='',blank=True,null=True,choices=AVAILABLE_STATES)
    property_postcode   = models.CharField(max_length=4,default='', validators=[RegexValidator(r'^\d{0,9}$')])
    billing_address     = models.CharField(max_length=20,default='',blank=True,null=True)
    billing_suburb      = models.CharField(max_length=20,default='',blank=True,null=True)
    billing_state       = models.CharField(max_length=20,default='',blank=True,null=True,choices=AVAILABLE_STATES)
    billing_postcode    = models.CharField(max_length=4,default='',blank=True,null=True ,validators=[RegexValidator(r'^\d{0,9}$')])
    abn                 = models.CharField(max_length=20,default='', validators=[RegexValidator(r'^\d[0-9]\s\d[0-9].\s\d[0-9].\s\d[0-9].')])
    property            = models.OneToOneField(Property,on_delete=models.CASCADE,blank=True,null=True)
    ai_program          = models.ManyToManyField(AI_Program,blank=True, related_name='enrolled_programs')
    
 
    def __str__(self):
        return f"{self.name} - {self.email}"
        
    
    
    
    
