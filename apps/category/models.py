from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def clean(self):
        self.name = self.name.strip().lower()

    def save(self, *args, **kwargs):
        self.name = self.name.strip().lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
