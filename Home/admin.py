from django.contrib import admin
from Home.models import AddStudent
# Register your models here.
class Admin_view(admin.ModelAdmin):
    list_display = ('Name','Father_Name','Mobile','Class','Status') # here we define the list diplay which show the entire data into a list in the admin panel
admin.site.register(AddStudent,Admin_view) # here we are register the model which we create first we define the model which we want to register and then the admin class