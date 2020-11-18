from django.db import models

# Create your models here.
class QNA(models.Model):
    name= models.TextField()
    relation= models.TextField()
    question= models.TextField()
    option1= models.TextField()
    option2= models.TextField()
    option3= models.TextField()
    option4= models.TextField()

class sanQNA(models.Model):
    name= models.TextField()
    relation= models.TextField()
    question= models.TextField()
    option1= models.TextField()
    option2= models.TextField()
    option3= models.TextField()
    option4= models.TextField()

    
   