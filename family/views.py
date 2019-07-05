# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core import serializers
from django.http import HttpResponse
# Create your views here.
from .models import Individual, Family, Relationship
from .forms import MemberForm

def Index(request):
    return render(request, 'family/index.html')

@login_required
def CreateMember(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            new_member = form.save(commit=False)
            new_member.created_by = request.user
            new_member.save()
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

def MemberDetails(request, member_id):
    member = Individual.objects.get(pk=member_id)
    return render(request, 'family/member_details.html', {'member': member})

@login_required
def MyMemberList(request):
    members = Individual.objects.filter(created_by=request.user)
    return render(request, 'family/member_list.html', {'members': members})

def FamilyMemberList(request, family_id):
    head_member = Individual.objects.filter(family__id=family_id)
    other_members = Individual.objects.filter(individual_1__family_id=family_id)
    members = head_member | other_members
    return render(request, 'family/member_list.html', {'members': members})

# @login_required
# def CreateFamily(request):

# def JoinInFamily(request):

def FamilyList(request):
    families = Family.objects.all()[:5]
    return render(request, 'family/family_list.html', {'families': families})

def FamilyDetails(request, family_id):
    family = Family.objects.get(pk=family_id)
    return render(request, 'family/family_details.html', {'family': family})

def FamilyRelationship(request, family_id):
    relations = Relationship.objects.filter(family_id=family_id)
    return render(request, 'family/relation.html', {'relations': relations})

def Genealogy(request, family_id):
    relations = Relationship.objects.filter(family_id=family_id)
    json = serializers.serialize("json", relations, use_natural_foreign_keys=True)
    return HttpResponse(json, content_type='application/json')
