


from django.urls import path
from . views import Delete_student, Home, student_view,Editstudent

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('add_student/',student_view.as_view(),name='add_student'),
    path('delete_student/',Delete_student.as_view(),name='delete_student'),
 
    path('edit_student/<int:id>/',Editstudent.as_view(),name='edit_student'),

]
