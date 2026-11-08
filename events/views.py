from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from events.models import Event
from events.form import EventModelForm #CategoryModelForm
from django.db.models import Q, Count
from django.utils import timezone

from django.contrib import messages

# Create your views here.
def home(request):
    
    type = request.GET.get('type', 'all')
    searchValue = request.GET.get('search', '')
    
    # event = Event.objects.all()
    
    # baseQuery = Event.objects.select_related('category').prefetch_related('participants')
    
    baseQuery = Event.objects.select_related('category').annotate(
        total_participants=Count('participants')
    )
    
    # event = baseQuery.all()
    
    
    if type == 'ai-ml':
    
        event = baseQuery.filter(name__isnull=False,category__name='AI & ML')

    elif type == 'web-dev':
    
        event = baseQuery.filter(name__isnull=False,category__name='Web Dev')

    elif type == 'cybersecurity':
    
        event = baseQuery.filter(name__isnull=False,category__name='Cybersecurity')

    elif type == 'cloud':
    
        event = baseQuery.filter(name__isnull=False,category__name='Cloud Computing')
    
    elif type == 'all':
    
        event = baseQuery.filter(name__isnull=False)
    
    
    if searchValue:
        event = event.filter(Q(name__icontains=searchValue) | Q(location__icontains=searchValue))   
    
    
    # Paginate by 6 items per page
    paginator = Paginator(event, 6)
    
    # Get the current page number from request parameters (?page=2)
    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)
    
    return render(request, 'index.html', {'events': events})



def event_details(request, event_id):
    # event = Event.objects.get(id=event_id)
    event = Event.objects.prefetch_related('participants').filter(id=event_id).first()
    return render(request, 'event_details.html', {'event': event})


def contact(request):
    return HttpResponse("Contact us at  contact@example.com")



def admin_dashboard(request):
    
    type = request.GET.get('type', 'all')
    
    dateFrom = request.GET.get('date', 'all')
    dateTo = request.GET.get('date_to', 'all')
    
    
    baseQuery = Event.objects.select_related('category').prefetch_related('participants')

        
    if type == 'previous':
    
        event = baseQuery.filter(name__isnull=False,date__lt=timezone.now().date())

    elif type == 'present':
    
        event = baseQuery.filter(name__isnull=False,date=timezone.now().date())

    elif type == 'upcoming':
    
        event = baseQuery.filter(name__isnull=False,date__gt=timezone.now().date())
    
    elif dateFrom != 'all' and dateTo != 'all':
        
        event = baseQuery.filter(name__isnull=False,date__range=[dateFrom, dateTo])
        
    elif type == 'all':
    
        event = baseQuery.all()
        
    
    count = Event.objects.aggregate(
        
        totalParticipants = Count('participants', distinct=True),
        previousParticipants = Count('participants', filter=Q(date__lt=timezone.now().date()), distinct=True),
        presentParticipants = Count('participants', filter=Q(date=timezone.now().date()), distinct=True),
        upcomingParticipants = Count('participants', filter=Q(date__gt=timezone.now().date()), distinct=True),
        
        totalEvents = Count('id', distinct=True),
        previousEvents = Count('id', filter=Q(date__lt=timezone.now().date()), distinct=True),
        presentEvents = Count('id', filter=Q(date=timezone.now().date()), distinct=True),
        upcomingEvents = Count('id', filter=Q(date__gt=timezone.now().date()), distinct=True)
    )
    
    context = {
        
        'events': event,
        'count': count
    }
    
    return render(request, 'dashboard/AdminDashboard.html', context )




def create_event(request):
    
    eventForm = EventModelForm()
    # categoryForm = CategoryModelForm()
    
    if request.method == 'POST':
        
        eventForm = EventModelForm(request.POST)
        # categoryForm = CategoryModelForm(request.POST)
        
        if eventForm.is_valid() : #and categoryForm.is_valid()
            
            event = eventForm.save()
            # category = categoryForm.save(commit=False)
            # event.category = category
            event.save()
            
            messages.success(request, 'Event and Category created successfully!')
            return redirect('create-event')
        
    context = {
        'eventForm': eventForm, 
        # 'categoryForm': categoryForm
    }
    return render(request, 'Dashboard/CreateEvent.html', context)


def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    messages.success(request, 'Event deleted successfully!')
    return redirect('admin-dashboard')

def update_event(request, event_id):
    event = Event.objects.get(id=event_id)
    eventForm = EventModelForm(instance=event)

    if request.method == 'POST':
        eventForm = EventModelForm(request.POST, instance=event)
        if eventForm.is_valid():
            eventForm.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('admin-dashboard')

    context = {
        'eventForm': eventForm,
        'event': event
    }
    return render(request, 'Dashboard/CreateEvent.html', context)

# def create_event(request):
#     if request.method == 'POST':
#         eventForm = EventModelForm(request.POST)
#         if eventForm.is_valid():
#             eventForm.save()
#             messages.success(request, 'Event created successfully!')
#             return redirect('create-event')
#         else:
#             # Add this to inspect the exact errors in your terminal console!
#             print("Form Errors:", eventForm.errors)
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         eventForm = EventModelForm()

#     context = {
#         'eventForm': eventForm,
#     }
#     return render(request, 'Dashboard/CreateEvent.html', context)