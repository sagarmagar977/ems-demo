from django.db import models

# Create your models here.


class role(models.Model):
    name=models.CharField(max_length=20,null=False,unique=True)
    def  __str__(self):
        return self.name

class department(models.Model):
    name=models.CharField(max_length=20,unique=True)
    def  __str__(self):
        return self.name

class employee(models.Model):
    name=models.CharField(max_length=100)
    role=models.ForeignKey(role,on_delete=models.CASCADE)
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    hire_date=models.DateField()
    def  __str__(self):
        return  '%s %s %s' %(self.name, ",",self.role)
    