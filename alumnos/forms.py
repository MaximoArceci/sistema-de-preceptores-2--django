from models import Alumnos
from db_file_storage.form_widgets import DBClearableFileInput
from django import forms

class ConsoleForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        exclude = []
        widgets = {
            'picture': DBClearableFileInput
        }