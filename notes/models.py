from django.db import models


class Note(models.Model):
    """
    Represents a single sticky note in the database
    Attributes:
    title (str): A short title for each note.
    content (str): The main text body of the sticky note.
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
