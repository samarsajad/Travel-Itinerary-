from django import forms

class TravelPlanForm(forms.Form):
    days = forms.IntegerField(label="Days", min_value=1)
    location = forms.CharField(label="Location", max_length=255)
    budget = forms.FloatField(label="Budget", min_value=0)
