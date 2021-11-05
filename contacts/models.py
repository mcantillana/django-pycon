from django.db import models

class Contact(models.Model):

    subject = models.CharField(max_length=100)
    message = models.TextField()
    sender = models.EmailField()
    
    def __str__(self):
        return self.sender

