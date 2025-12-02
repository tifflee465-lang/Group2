from django.urls import path
from . import views
from .form import studentForm
urlpatterns = [
    path('',views.home, name = 'home'),
    path('student/',views.student, name = 'student'),
    path('addStudent',views.addStudent,name='addStudent'),
    path('about',views.about,name='about'),
    path('contactus',views.contactUs,name='contactus'),
    path('listviews',views.listView,name='listviews'),
    path('addhtmlform',views.addhtml,name='addform2'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name= "delete")
]