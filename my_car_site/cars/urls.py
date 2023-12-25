from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('list/',views.list_view,name='list'),
    path('add/',views.add,name='add'),
    path('delete',views.delete,name='delete')
]
