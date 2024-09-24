from django.contrib import admin
# Register your models here.

from .models import Contact  # Import the model



class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')  # Use 'phone' if that's the correct field name

admin.site.register(Contact, ContactAdmin)  # Display these fields in the admin panel

    
# Register your models here.
from django.contrib import admin
from .models import LoginHistory

class LoginHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'login_time', 'success']
    list_filter = ['success', 'login_time']
    search_fields = ['user__username']

admin.site.register(LoginHistory, LoginHistoryAdmin)

# myapp/admin.py

from django.contrib import admin
from .models import InternshipApplication

class InternshipApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'sex', 'whatsapp_number', 'college_name', 'qualification', 'last_qualification_year', 'resume', 'random_number']
    search_fields = ['full_name', 'email', 'college_name', 'random_number']  # You can search using the random number too

admin.site.register(InternshipApplication, InternshipApplicationAdmin)
