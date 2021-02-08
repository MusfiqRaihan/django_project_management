from django.db import models


class Development_Tool(models.Model):
    development_method = models.CharField(max_length=100)
    development_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.development_method


class development_methodology(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class Development_Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.position


class Payment_type(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
