from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
		# use a slug for tags in URL?

    def __str__(self):
        return self.name
