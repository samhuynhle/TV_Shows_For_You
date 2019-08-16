from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()

    def __repr__(self):
        return f"<Show object: {self.title} ({self.id}), release date: {self.release_date}>"