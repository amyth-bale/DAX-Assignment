from django import forms
from .models import Notes

class NewNote(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ('title', 'description','start_date','end_date','is_completed')