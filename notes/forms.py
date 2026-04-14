from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    """ A form for creating and updating sticky notes.
    Binds to the Note model and exposes the 'title' and 'content' fields.
    """
    class Meta:
        model = Note
        fields = ['title', 'content']