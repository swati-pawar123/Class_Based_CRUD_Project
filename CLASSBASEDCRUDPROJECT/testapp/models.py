from django.db import models


from django.urls import reverse

# Create your models here.
#modelname->singular
#table name-->pluarl
class Employee(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    salary=models.IntegerField()
    city=models.CharField(max_length=30)


    def get_absolute_url(self):
        return reverse('hello')


    #register in admin interface

#django code--->corresponding sql query

#-->py manage.py makemigrations


#just by writing a sql query can a table be created?
#execute that sql query

#-->py manage.py migrate

