from django.urls import path
from events.views import contact, delete_event, home, event_details, admin_dashboard, create_event,update_event


urlpatterns = [
    
    path('', home, name='home'),
    path('event-details/<int:event_id>/', event_details, name='event-details'),
    path('contact/', contact, name='contact'),
    path('admin-dashboard/', admin_dashboard, name='admin-dashboard'),
    path('create-event/', create_event, name='create-event'),
    path('update_event/<int:event_id>/', update_event, name='update_event'),
    path('delete_event/<int:event_id>/', delete_event, name='delete_event'),
    
    
    
]
    