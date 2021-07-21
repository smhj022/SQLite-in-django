from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=60)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
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
