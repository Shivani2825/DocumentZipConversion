from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=120)
    contact=models.PositiveIntegerField()
    password=models.CharField(max_length=150)


    def __str__(self):
        return self.name
    
class Files(models.Model):
    user=models.ForeignKey(Person,on_delete=models.CASCADE)
    profile=models.FileField(upload_to='profile')
    aadharcard=models.FileField(upload_to='aadharcard')
    pancard=models.FileField(upload_to='pancard')
    marksheet=models.FileField(upload_to='marksheet')

    def __str__(self):
        return str(self.user)