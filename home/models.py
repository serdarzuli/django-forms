from django.db import models

# Build the contact form using the inheritance and ORM
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    
# coktan secmeli bir kismimiz var departmant diye, ona buraya bir karsilik ENUMORATIN yazicaz. ayrica bunu ingilziceye cevir

    DEPARTMENTS = [
        ('MF', 'Manufacturing'),
        ('SH', 'Shipping'),
        ('AD', 'Administration'),
        ('HR', 'Human Resources')
    ]
    
    dept = models.CharField(max_length=2, choices=DEPARTMENTS, default=DEPARTMENTS[3][0])
    