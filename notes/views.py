from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


# 1. READ: Displays all sticky notes
def note_list(request):
    """
    Retrieves all sticky notes from the database and renders the list page.
    """
    notes = Note.objects.all()
    context = {"notes": notes, "page_title": "My Sticky Notes"}
    return render(request, "notes/note_list.html", context)


# 2. READ: Displays a single sticky note's details.
def note_detail(request, pk):
    """
    View to displayy the details of a specific sticky note.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


# 3. CREATE: Make a new sticky note
def note_create(request):
    """
    View to create a new sticky note.
    Handles both GET requests (displays empty form) and POST requests
    (validating and saving the new note).
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")

    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form})


# 4. UPDATE: Edit an existing sticky note
def note_update(request, pk):
    """
    View to update an existing sticky note.
    Handles both GET requests (displays the form pre-filled with existing date)
    and POST requests (validating and saving the updated note).
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form})


# 5. DELETE: Remove a sticky note
def note_delete(request, pk):
    """
    View to delete an existing sticky note.
    """
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("note_list")
