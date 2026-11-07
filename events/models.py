from django.db import models

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