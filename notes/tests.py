from django.test import TestCase
from django.urls import reverse
from .models import Note


# Create your tests here.
class NoteModelTest(TestCase):
    def setUp(self):
        Note.objects.create(title="Test Database", content="Task 16 Part 2")

    def test_note_content(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, "Test Database")
        self.assertEqual(note.content, "Task 16 Part 2")


class NoteViewTest(TestCase):
    def setUp(self):
        Note.objects.create(title="Test Note", content="Testing View")

    def test_note_list_view(self):
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_detail_view(self):
        note = Note.objects.get(id=1)
        response = self.client.get(reverse("note_detail", args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Testing View")
