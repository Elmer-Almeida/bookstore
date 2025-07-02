from django.db import models
from django.contrib.auth.models import User

BOOK_FORMAT_CHOICES = (
('HC', 'Hardcover'),
('PB', 'Paperback'),
('EB', 'E-Book'),
)


class Genre(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    name = models.CharField(max_length=120, help_text="What's the author's name?")
    bio = models.TextField(blank=True, help_text="Some information on the author...")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    seller = models.ForeignKey(User, on_delete=models.PROTECT, related_name="books")
    isbn = models.CharField(max_length=14, db_index=True, verbose_name="ISBN")
    title = models.CharField(max_length=120, db_index=True)
    description = models.TextField(blank=False)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    format_choices = models.CharField(choices=BOOK_FORMAT_CHOICES, max_length=2)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    publication_date = models.DateField()
    language = models.CharField(max_length=120, default="English")
    isAvailable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
