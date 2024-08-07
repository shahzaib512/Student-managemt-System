from django.urls import path
from .views import StudentView

urlpatterns = [
    path('students/', StudentView.as_view(), name='students'),  # list all students
    path('students/<int:pk>/', StudentView.as_view()),  # get a single student by id
    # path('students/create/', StudentView.as_view(), name='student-create'),  # create a new student
    # path('students/<int:pk>/update/', StudentView.as_view(), name='student-update'),  # update a student by id
    # path('students/<int:pk>/delete/', StudentView.as_view(), name='student-delete'),  # delete a student by id
]