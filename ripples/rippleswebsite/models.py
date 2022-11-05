from django.db import models


# Create your models here.

# class EventRegistration(models.Model):


class Te1(models.Model):
    username = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)

    def __str__(self):#MAIN USAGE IS THAT WHEN WE ADD THE VALUE IN ADMIN PAGE IT WILL RETURN THIS 'USERNAME' ADDED
        return self.username


class Te2(models.Model):
    username = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)

    def __str__(self):#MAIN USAGE IS THAT WHEN WE ADD THE VALUE IN ADMIN PAGE IT WILL RETURN THIS 'USERNAME' ADDED
        return self.username


class Te3(models.Model):
    username = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)

    def __str__(self):#MAIN USAGE IS THAT WHEN WE ADD THE VALUE IN ADMIN PAGE IT WILL RETURN THIS 'USERNAME' ADDED
        return self.username


class Nte1(models.Model):
    username = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)

    def __str__(self):#MAIN USAGE IS THAT WHEN WE ADD THE VALUE IN ADMIN PAGE IT WILL RETURN THIS 'USERNAME' ADDED
        return self.username


class Nte2(models.Model):
    username = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)

    def __str__(self):#MAIN USAGE IS THAT WHEN WE ADD THE VALUE IN ADMIN PAGE IT WILL RETURN THIS 'USERNAME' ADDED
        return self.username


class Nte3(models.Model):
    username = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)

    def __str__(self):#MAIN USAGE IS THAT WHEN WE ADD THE VALUE IN ADMIN PAGE IT WILL RETURN THIS 'USERNAME' ADDED
        return self.username
