from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


# 1. READ: Displays all sticky notes
def note_list(request):
    notes = Note.objects.all()
    # Grabs everything from the database
    context = {"notes": notes, "page_title": "My Sticky Notes"}
    # Renders the HTML template and passes the data (context) to it
    return render(request, "notes/note_list.html", context)


# 2. READ: Displays a single sticky note's details.
def note_detail(request, pk):
    # Grabs the specific note using its Primary Key (pk),
    # or shows 404 error if it doesn't exist
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


# 3. CREATE: Make a new sticky note
def note_create(request):
    # If user clicked "Submit" on form.
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
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("note_list")
