"""School URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from Home.views import Add,Detail,Home #url of every page it must be defined here
from Home import views
from Teacher.views import TeacherDetail
from Login.views import Loginup,Signup,LogoutPage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('gettoken/',TokenObtainPairView.as_view(),name = 'token obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name = 'token refresh_pair'),
    path('Verifytoken/',TokenVerifyView.as_view(),name = 'token verify_pair'),
    path('Home/',Home),
    path('Add/',Add),
    path('Loginup/',Loginup),
    path('LogoutPage/',LogoutPage),
    path('Teacher/',TeacherDetail),
    path('Signup/',Signup),
    path('Details/',Detail),
    path('<int:id>/',views.Edit,name = 'editdata'),
    path('delete/<int:id>/',views.DeleteStudent,name = 'deletedata'),

]
