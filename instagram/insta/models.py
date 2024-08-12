from django.db import models

# Create your models here.
class Feed(models.Model):
    person=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    pic=models.ImageField(upload_to='media')
    cap=models.CharField(max_length=200)


    def __str__(self):
        return self.cap
    
    