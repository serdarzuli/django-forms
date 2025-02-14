from django.db import models

# Build the contact form using the inheritance and ORM
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    
    