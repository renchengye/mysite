# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core import serializers
from django.http import HttpResponse
# Create your views here.
from .models import Individual, Family, Relationship
from .forms import MemberForm, FamilyForm

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
            return redirect('family:index')
    else:
        form = MemberForm()
    return render(request, 'family/member_form.html', {'form': form})

@login_required
def ModifyMember(request, member_id):
    instance = Individual.objects.get(pk=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('family:index')
    else:
        form = MemberForm(instance=instance)
    return render(request, 'family/member_form.html', {'form': form, 'member': instance})

@login_required
def MyMemberList(request):
    members = Individual.objects.filter(created_by=request.user)
    return render(request, 'family/member_list.html', {'members': members})

def FamilyMemberList(request, family_id):
    family = Family.objects.get(pk=family_id)
    head_member = Individual.objects.filter(family__id=family_id)
    other_members = Individual.objects.filter(individual_1__family_id=family_id)
    members = head_member | other_members
    return render(request, 'family/member_list.html', {'members': members, 'family': family})

def FamilyRelationship(request, family_id):
    head_member = family = Family.objects.get(pk=family_id).head_of_family_individual_id
    relations = Relationship.objects.filter(family_id=family_id)
    return render(request, 'family/genealogy.html', {'head_member': head_member, 'relations': relations})

@login_required
def CreateFamily(request, member_id):
    try:
        family = Family.objects.get(head_of_family_individual_id=member_id)
    except (KeyError, Family.DoesNotExist):
        member = Individual.objects.get(pk=member_id)
        if request.method == 'POST':
            form = FamilyForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('family:index')
        else:
            form = FamilyForm()
        return render(request, 'family/family_form.html', {'form': form, 'member': member})
    else:
        return redirect('family:family_details', family_id=family.id)

@login_required
def JoinInFamily(request, member_id):
    if request.method == 'POST':
        form = RelationshipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('family:index')
    else:
        form = RelationshipForm()
    return render(request, 'family/relationship_form.html', {'form': form})

def FamilyList(request):
    families = Family.objects.all()[:5]
    return render(request, 'family/family_list.html', {'families': families})

def FamilyDetails(request, family_id):
    family = Family.objects.get(pk=family_id)
    return render(request, 'family/family_details.html', {'family': family})
