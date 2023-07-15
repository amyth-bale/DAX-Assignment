from django.urls import path
from .views import home,new_note,edit_note,status_change,delete

urlpatterns = [
    path('', home, name="home"),
    path('new_note/',new_note, name='new_note'),
    path('note/<int:id>/edit/', edit_note, name='edit_note'),
    path('note/<int:id>/status/', status_change, name='status_change'),
    path('note/<int:id>/delete/', delete, name='delete'),
]
