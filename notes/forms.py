from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        # These are the fields the user will actually fill out.
        fields = ['title', 'content']