
from datetime import datetime,timedelta 
from statistics import mode
from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_save,pre_save 
from django.dispatch import receiver
from .data_file import *


AVAILABLE_INTERACTIONS =  tuple([(x,x) for x in AVAILABLE_INTERACTIONS])


class CowTable(models.Model):
    nlsid           = models.CharField(max_length=20,default='',blank=True,null=True,verbose_name="NLSID") 
    vid             = models.CharField(max_length=20,default='',blank=True,null=True,verbose_name="VID") 
    weight          = models.FloatField(default=0,blank=True,null=True,verbose_name="Weight") 
    condition_score = models.FloatField(default=0,blank=True,null=True,verbose_name="Condition Score") 
    imf             = models.CharField(max_length=20,default='',blank=True,null=True,verbose_name="IMF") 
    ema             = models.CharField(max_length=20,default='',blank=True,null=True,verbose_name="EMA") 
    note            = models.TextField(default='',blank=True,null=True,verbose_name="Note") 
    breed           = models.CharField(max_length=2000,default='',blank=True,null=True,verbose_name="Breed") 
    interaction     = models.CharField(max_length=2000,default='',blank=True,null=True,verbose_name="Interaction" ) 
    
    def __str__(self):
        return  f"{self.nlsid}"
    





class Property(models.Model):
    name    = models.CharField(max_length=20,default='',blank=True,null=True,verbose_name="Property Name") 
    pic     = models.CharField(max_length=20,default='',blank=True,null=True,verbose_name="PIC (Property Identofication Code)") 
    cows    = models.ManyToManyField(CowTable,blank=True)
    def __str__(self):
        return  f"{self.name} - {self.pic}"
    
    
class AI_Program(models.Model):
    start_date                  = models.DateField(default=now) 
    seeder_injection_date       = models.DateField(default=now) 
    prosto_injection_date        = models.DateField(default=now) 
    gnrh_date                   = models.DateField(default=now) 
    remove_seed_date        = models.DateField(default=now) 
    insemination_date           = models.DateField(default=now) 
    pregnancy_test_date         = models.DateField(default=now) 
    
    
    seeder_injection_status       = models.BooleanField(default=False) 
    prosto_injection_status        = models.BooleanField(default=False) 
    gnrh_status                   = models.BooleanField(default=False) 
    remove_seed_status          = models.BooleanField(default=False) 
    insemination_status           = models.BooleanField(default=False) 
    pregnancy_test_status         = models.BooleanField(default=False) 
    
    
    
    
    finished                    = models.BooleanField(default=False)
    def __str__(self):
        return  f"{self.start_date}"
    


@receiver(pre_save , sender=AI_Program, dispatch_uid="save_update_ai_program_dates")
def save_update_ai_program_dates(sender, instance, **kwargs): 
    instance.seeder_injection_date  = instance.start_date  + timedelta(days=0)
    instance.prosto_injection_date   = instance.start_date  + timedelta(days=2)
    instance.gnrh_date              = instance.start_date  + timedelta(days=3)
    instance.remove_seed_date     = instance.start_date  + timedelta(days=8)
    instance.insemination_date      = instance.start_date  + timedelta(days=10)
    instance.pregnancy_test_date    = instance.start_date  + timedelta(days=46) 
    


 

AVAILABLE_STATES =  tuple([(x,x) for x in AVAILABLE_STATES])



class CustomerProfile(models.Model):
    name                = models.CharField(max_length=500,default='',blank=True,null=True)
    email               = models.CharField(max_length=500,default='',blank=True,null=True)
    mobile_number       = models.CharField(max_length=50,default='',blank=True,null=True)
    property_address    = models.CharField(max_length=500,default='',blank=True,null=True)
    property_state      = models.CharField(max_length=100,default='',blank=True,null=True,choices=AVAILABLE_STATES)
    property_postcode   = models.CharField(max_length=20,default='',blank=True,null=True) 
    billing_address     = models.CharField(max_length=500,default='',blank=True,null=True)
    billing_state       = models.CharField(max_length=100,default='',blank=True,null=True,choices=AVAILABLE_STATES)
    billing_postcode    = models.CharField(max_length=20,default='',blank=True,null=True) 
    abn                 = models.CharField(max_length=100,default='',blank=True,null=True)
    property            = models.OneToOneField(Property,on_delete=models.CASCADE,blank=True,null=True)
    ai_program          = models.ManyToManyField(AI_Program,blank=True, related_name='enrolled_programs', )
    
    
    def __str__(self):
        return f"{self.name} - {self.email}"
        
    
    
    
    
