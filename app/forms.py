from .models import City
from django.forms import ModelForm
from django.forms import TextInput
class userinput(ModelForm):
    class Meta:
        model=City
        fields=['cityname']
        widgets= {'cityname':TextInput(attrs={'class':'input','placeholder':'Banglore'})} 