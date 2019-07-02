# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Individual, Family, Relationship_Type, Role, Relationship

class IndividualAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'place_of_birth','other_individual_details')
    ordering = ('date_of_birth',)
    search_fields = ['last_name']

class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'individual_1_id', 'individual_2_id', 'individual_1_role_code', 'individual_2_role_code', 'date_relationship_started',)
    ordering = ('date_relationship_started',)
    search_fields = ['individual_1_id', 'individual_2_id']

admin.site.register(Individual, IndividualAdmin)
admin.site.register(Family)
admin.site.register(Relationship_Type)
admin.site.register(Role)
admin.site.register(Relationship, RelationshipAdmin)
