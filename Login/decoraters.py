from django.http import HttpResponse
from django.shortcuts import redirect
#Decoraters are generally a fuction which conatin the another function
def unauthenticated_user(view_func): # here we create a fuction in which we passed the view func ,view func is nothing but this is the another fuction
    def wrapper_func(request,*args,**kwargs):#this is the another Wrapper fuction
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func


def allowed_user(allowed_roles=[]):#here we create a another fuction and passed a list of roles,These is not Work for know I am still working on that part
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("User not allowed to access to this page only Admin has Authority to acess this page Please Contact admin ")
        return wrapper_func
    return decorator

def admin_only(view_func): # here we create the function amd Give the authority to the admin Only
    def wrapper_function(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group= request.user.groups.all()[0].name
        if group == 'customer':
            return redirect('userpage')
        if group == 'admin':
            return view_func(request,*args,**kwargs)
    return wrapper_function