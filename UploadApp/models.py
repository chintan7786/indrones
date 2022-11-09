from django.db import models

# Create your models here.
class Files(models.Model):
    File = models.FileField(upload_to='files')

    def __str__(self):
        return str(self.File)

