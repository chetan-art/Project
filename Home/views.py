from django.shortcuts import render,redirect,HttpResponseRedirect
from Home.models import AddStudent  # We import the models From Home.Models
from Home.forms import StudentAdd # We import the Forms from Home.forms
from Login.decoraters import allowed_user,admin_only,unauthenticated_user
from django.contrib.auth.decorators import login_required
# Create your views here.
def Home(request): # We create a Function

    return render(request,'home.html')  # we return A html file

# In this function we fetch all the data from the Database or Table and show it on Student.html
@login_required(login_url='http://127.0.0.1:8000/Loginup/')
def Detail(request):
    x = AddStudent.objects.all()
    return render(request,'Student.html',{'x':x})

#In this function we write logic to add a new student using the form
@login_required(login_url='http://127.0.0.1:8000/Loginup/')
def Add(request):
    form = StudentAdd()
    if request.method == 'POST': # we used the POST request
        form = StudentAdd(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'Add.html',{'form':form})

# In this function we write The code To edit the present detail in the table or database We also use the form to edit the data
@login_required(login_url='http://127.0.0.1:8000/Loginup/')
def Edit(request,id): # we pass the id , id represent the unique number or serial or which item you are gonna be edit
    form = StudentAdd()
    if request.method == 'POST':
        pi = AddStudent.objects.get(pk = id)
        form = StudentAdd(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/Details/')
    else:
        pi = AddStudent.objects.get(pk=id)
        form = StudentAdd(instance=pi)
    return render(request, 'ShowStudent.html', {'form': form})

# we write the code for Delete the data , Here also we use the id to identify the data which data we want to delete
@login_required(login_url='http://127.0.0.1:8000/Loginup/')
def DeleteStudent(request,id):
    if request.method == 'POST':
        pi = AddStudent.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('http://127.0.0.1:8000/Details/')


