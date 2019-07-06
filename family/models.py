# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

def individual_directory_path(instance, filename):
    return 'individual_{0}/{1}'.format(instance.date_of_birth, filename)

class Individual(models.Model):
    GENDER = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=50)
    other_individual_details = models.TextField(null=True, blank=True)
    image_path = models.FileField(upload_to=individual_directory_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_of_birth']

    def natural_key(self):
        return { 'last_name': self.last_name , 'image_path': u'%s' %(self.image_path) }

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

def family_directory_path(instance, filename):
    return 'family_{0}/{1}'.format(instance.user.id, filename)

class Family(models.Model):
    head_of_family_individual_id = models.ForeignKey(Individual, on_delete=models.CASCADE)
    family_name = models.CharField(max_length=50)
    family_description = models.CharField(max_length=100, null=True, blank=True)
    family_date_from = models.DateField(null=True, blank=True)
    family_date_to = models.DateField(null=True, blank=True)
    other_family_details = models.TextField(null=True, blank=True)
    image_path = models.FileField(upload_to=family_directory_path, null=True, blank=True)

    def __unicode__(self):
        return self.family_name

class Relationship_Type(models.Model):
    TYPE = [
        ('C', 'Consanguinity'),
        ('M', 'Marriage'),
    ]
    relationship_type_code = models.IntegerField(primary_key=True)
    relationship_type_description = models.CharField(max_length=10, choices=TYPE)

    def __str__(self):
        return self.relationship_type_description

class Role(models.Model):
    ROLES = [
        ('F', 'Father'),
        ('M', 'Mother'),
        ('S', 'Son'),
        ('D', 'Daughter'),
        ('H', 'Husband'),
        ('W', 'Wife'),
    ]
    role_code = models.IntegerField(primary_key=True)
    role_description = models.CharField(max_length=10, choices=ROLES)

    def __str__(self):
        return self.role_description

class Relationship(models.Model):
    family_id = models.ForeignKey(Family, on_delete=models.CASCADE)
    individual_1_id = models.ForeignKey(Individual, related_name='individual_1', on_delete=models.CASCADE)
    individual_2_id = models.ForeignKey(Individual, related_name='individual_2', on_delete=models.CASCADE)
    relationship_type_code = models.ForeignKey(Relationship_Type, on_delete=models.CASCADE)
    individual_1_role_code = models.ForeignKey(Role, related_name='individual_1_role', on_delete=models.CASCADE)
    individual_2_role_code = models.ForeignKey(Role, related_name='individual_2_role', on_delete=models.CASCADE)
    date_relationship_started = models.DateField()
    date_relationship_ended = models.DateField(null=True, blank=True)
    relationship_place = models.CharField(max_length=50, null=True, blank=True)
    other_relationship_details = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['date_relationship_started']
