# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Individual, Family, Relationship
from .forms import MemberForm

def Index(request):
    return render(request, 'family/index.html')

def FamilyList(request):
    families = Family.objects.all()
    return render(request, 'family/family_list.html', {'families': families})

def FamilyDetails(request, family_id):
    family = Family.objects.get(pk=family_id)
    return render(request, 'family/family_details.html', {'family': family})

# def CreateFamily(request):

def FamilyMemberList(request, family_id):
    family = Family.objects.get(pk=family_id)
    individual_1 = Individual.objects.filter(individual_1__family_id=family_id)
    individual_2 = Individual.objects.filter(individual_2__family_id=family_id)
    individuals = (individual_1 | individual_2).distinct()
    return render(request, 'family/member_list.html', {'members': individuals, 'family': family})

def FamilyRelationship(request, family_id):
    relations = Relationship.objects.filter(family_id=family_id)
    return render(request, 'family/relation.html', {'relations': relations})

def MemberDetails(request, member_id):
    member = Individual.objects.get(pk=member_id)
    return render(request, 'family/member_details.html', {'member': member})

def CreateMember(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            new_member = form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = MemberForm()
    return render(request, 'family/create_member.html', {'form': form})

# def JoinInFamily(request):

