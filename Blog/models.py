from django.db import models

# Create your models here.
class bloginfo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()



#so this will create a table in DB with ID,TITLE,CONTENT,CREATED AT
def __str__(self):
    return self.title