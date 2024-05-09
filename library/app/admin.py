from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import Groups, Company, Departments,Divisions,Sections,
from .models import book,Author,Genre

#Adding Product_Data table to be accessed in Admin portal
admin.site.register(book)
admin.site.register(Author)
admin.site.register(Genre)


