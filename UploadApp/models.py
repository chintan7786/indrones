from django.db import models

# Create your models here.
class Files(models.Model):
    File_name = models.CharField(max_length=50)
    File = models.FileField(upload_to='files')

    def __str__(self):
        return self.File_name

