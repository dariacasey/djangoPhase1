from django.urls import path
from . import views

# Should these be changed to forms.as_view()
urlpatterns = [
    path('create_class/', views.create_class, name='create_class'),
    path('classes/<int:class_id>/', views.class_detail, name='class_detail'),
    path('join-class/', views.join_class, name='join_class')
]
