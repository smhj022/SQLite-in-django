from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=60)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    # One to many relationship between author and book / on_delete is used to clarify what happen when author is deleted
    # CASCADE delete book also
    # PROTECT avoide delete book data
    # SET_NULL set to null
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)
    # bd_index is used because slug is used in url so to increase the performance db_index is se to True

    # show queryset in the form defined

    def __str__(self) -> str:
        return f"{self.title}({self.rating})"

    # overwrite method, here we overwriting save method to slugify over title(Harry Potter 1-->harry-potter-1)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
