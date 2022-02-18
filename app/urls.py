
from django.urls import path
from .views import * 
from .ajaxAPI import * 
from django.conf import settings
from django.conf.urls.static import static
from . import views
 
urlpatterns = [ 
    path('', index, name='index'),     
    # path('datatable/', datatable, name='datatable'),     
    path('manage_customers/', manage_customers, name='manage_customers'), 
    path('manage_properties/', manage_properties, name='manage_properties'), 
    
    
    path('edit_customer/<str:id>', edit_customer, name='edit_customer'), 
    path('manage_customers/edit_customer/<str:id>', edit_customer, name='edit_customer'), 
    
    
    path('manage_customers/edit_customer/<str:customer_id>/edit_ai_program/<str:ai_program_id>', edit_ai_program, name='edit_customer'), 
    path('manage_customers/edit_customer/<str:customer_id>/add_ai_program/', edit_ai_program, name='edit_customer'), 
    
    path('manage_customers/add_customer/', edit_customer, name='edit_customer'), 
    
    
    path('manage_properties/edit_property/<str:id>', edit_property, name='edit_customer'), 
    path('manage_properties/edit_property/<str:property_id>/manage_cows', manage_cows, name='edit_customer'),   
    path('manage_properties/add_property/', edit_property, name='add_property'), 
    
    
    
    
    
    
    path('edit_ai_program/<str:ai_program_id>', edit_ai_program, name='edit_ai_program'), 
    path('add_ai_program/', edit_ai_program, name='add_ai_program'), 
    
    
    
    
    path('manage_cows/', manage_cows, name='manage_cows'), 
    
    
    
    
    
    path('manage_cows/<str:property_id>', manage_cows, name='manage_cows'), 
    
     
    
    path('manage_properties/edit_property/<str:property_id>/manage_cows/edit_cow/<str:cow_id>', edit_cow, name='edit_cow'), 
    path('manage_properties/edit_property/<str:property_id>/manage_cows/add_cow/', edit_cow, name='add_cow'), 
    
    
    
    path('edit_cow/<str:cow_id>', edit_cow, name='edit_cow'), 
    
    
    
    
    path('add_cow/', edit_cow, name='add_cow'), 
    
    
        
    path('login/', login_router, name='login_router'),     
    path('logout/', logout_router, name='logout_router'),     
      
    
    path('ajaxgenerateAIProgramDateListing/', ajaxgenerateAIProgramDateListing, name='ajaxgenerateAIProgramDateListing'),     
    
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

