from django.forms import ModelForm
from Home.models import AddStudent
class StudentAdd(ModelForm):# here we are create a model based form
    class Meta:
        model = AddStudent
        fields = ['Name','Father_Name','Mobile','Class' ,'Status'] # this is the feild which we want to display