from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StaticContent(BaseModel):
    slug = models.SlugField(unique=True, blank=True)
    content = RichTextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.name)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
