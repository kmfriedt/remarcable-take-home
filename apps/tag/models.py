from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
		# use a slug for tags in URL?


    def clean(self):
        self.name = self.name.strip().lower()

    def save(self, *args, **kwargs):
        self.name = self.name.strip().lower()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
