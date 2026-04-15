from django.test import TestCase
from django.urls import reverse
from .models import Note


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


def test_note_create_view(self):
    response = self.client.post(
        reverse("note_create"),
        {
            "title": "New User Note",
            "content": "Testing creation via the view form.",
        },
    )

    self.assertEqual(response.status_code, 302)

    self.assertEqual(Note.objects.count(), 2)

    new_note = Note.objects.last()
    self.assertEqual(new_note.title, "New User Note")


def test_note_update_view(self):
    response = self.client.post(
        reverse("note_update", args=[str(self.note.id)]),
        {"title": "Updated Title", "content": "Updated Content"},
    )

    self.assertEqual(response.status_code, 302)
    self.note.refresh_from_db()
    self.assertEqual(self.note.title, "Updated Title")
    self.assertEqual(self.note.content, "Updated Content")


def test_note_delete_view(self):
    response = self.client.post(
        reverse("note_delete", args=[str(self.note.id)])
    )
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Note.objects.count(), 0)
