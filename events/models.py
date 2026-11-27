from django.db import models
from django.db.models.signals import post_save, pre_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail




# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category"
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    
    time = models.TimeField()
    location = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return self.name


class Participant(models.Model):
    
    events = models.ManyToManyField(Event, related_name="participants")

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
    
    
    #Signals 
    
    # @receiver(post_save, sender=Event)
    # def send_email_notification(sender, instance, created, **kwargs):
    #     if created:
    #         print(f"New event created: {instance.name}. Sending email notifications to participants...")
    #         print(f"Sender: {sender}, Instance: {instance}, Created: {created}")
            
    #         instance.save()
            
            
    # @receiver(pre_save, sender=Event)
    # def send_email_notification(sender, instance, **kwargs):
        
    #     print(f"New event created: {instance.name}. Sending email notifications to participants...")
    #     print(f"Sender: {sender}, Instance: {instance}")
    
    
    
# @receiver(m2m_changed, sender=Event.participants.through)
# def send_email_notification(sender, instance, action, **kwargs):
#     if action == "post_add":
#         assigned_email = [participant.email for participant in instance.participants.all()]
#         send_mail(
#             "New Event Created: {instance.name}",
#             f"A new event has been created: {instance.name}.",
#             "redankabir.cse@gmail.com",
#             assigned_email,
#             fail_silently=False, 
#         )


@receiver(post_save, sender=Event)
def send_email_notification(sender, instance, created, **kwargs):
    if created:
        # Fetch all participants from the database
        assigned_email = list(Participant.objects.values_list("email", flat=True))
        
        if assigned_email:  # Only send if there is at least 1 participant
            send_mail(
                f"New Event Created: {instance.name}",
                f"A new event has been created: {instance.name}.",
                "redankabir.cse@gmail.com",
                assigned_email,
                fail_silently=False,
            )