from django.db import models
import string, random

def generate_trip_code (length =6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

class Trip(models.Model):
    title = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    num_days = models.PositiveIntegerField()
    trip_code = models.CharField(max_length=10, unique=True, default=generate_trip_code)
    created_at = models.DateTimeField(auto_now_add=True)
    num_people = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} - {self.destination}"
    
class Preference(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='preferences')
    user_name = models.CharField(max_length=50)
    food = models.TextField(blank=True, help_text="List food or resturants you want to try")
    shopping = models.TextField(blank=True, help_text="List shops or brands you want to go")
    attractions = models.TextField(blank=True, help_text="List tourist spots or activities you want to visit and do")
    beauty = models.TextField(blank=True, help_text="List beauty-related places you want to go or do")
    additional_notes = models.TextField(blank=True, help_text="Any special request or things you would like to state")
    budget = models.PositiveIntegerField(help_text="Enter your estimated budget (e.g. 500 for SGD500)")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name}'s preference for {self.trip.trip_code}"


