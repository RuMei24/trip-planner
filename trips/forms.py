from django import forms
from .models import Trip
from .models import Preference

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['title', 'destination', 'num_days']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'num_days': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        exclude = ['trip', 'submitted_at']

        widgets = {
            'user_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'food' : forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
            'shopping' : forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
            'attraction' : forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
            'beauty' : forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
            'additional_notes' : forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
            'budget' : forms.TextInput(attrs={'class': 'form-control'}),
        }