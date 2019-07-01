# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
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

@login_required
def CreateMember(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            new_member = form.save()
            return redirect('family:member', member_id=new_member.id)
    else:
        form = MemberForm()
    return render(request, 'family/edit_member.html', {'form': form})

@login_required
def ModifyMember(request, member_id):
    instance = Individual.objects.get(pk=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('family:member', member_id=member_id)
    else:
        form = MemberForm(instance=instance)
    return render(request, 'family/edit_member.html', {'form': form})

# def JoinInFamily(request):

