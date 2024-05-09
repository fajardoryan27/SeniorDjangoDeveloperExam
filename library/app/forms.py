from django.forms import ModelForm
from .models import book

class AddBook(ModelForm):
    class Meta:
        model = book
        fields = '__all__'