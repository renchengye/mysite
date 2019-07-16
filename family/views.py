# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.db.models import Q
from .models import Individual, Family, Relationship, Role, Relationship_Type
from .forms import MemberForm, FamilyForm, RelationshipForm


def Index(request):
    return render(request, 'family/index.html')

# Member
@login_required
def CreateMember(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            new_member = form.save(commit=False)
            new_member.created_by = request.user
            new_member.save()
            return redirect('family:my_member')
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
            return redirect('family:my_member')
    else:
        form = MemberForm(instance=instance)
    return render(request, 'family/member_form.html', {'form': form, 'member': instance})

@login_required
def MyMemberList(request):
    members = Individual.objects.filter(created_by=request.user).exclude(family__isnull=False).exclude(individual_1__isnull=False)
    return render(request, 'family/member_list.html', {'members': members})

def FamilyMemberList(request, family_id):
    family = Family.objects.get(pk=family_id)
    head_member = Individual.objects.filter(family__id=family_id)
    other_members = Individual.objects.filter(individual_1__family_id=family_id)
    members = head_member | other_members
    return render(request, 'family/member_list.html', {'members': members, 'family': family})

# Family
@login_required
def CreateFamily(request, member_id):
    try:
        family = Family.objects.get(head_of_family_individual_id=member_id)
    except (KeyError, Family.DoesNotExist):
        member = Individual.objects.get(pk=member_id)
        if request.method == 'POST':
            form = FamilyForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.head_of_family_individual_id = member
                instance.save()
                return redirect('family:family_list')
        else:
            form = FamilyForm()
        return render(request, 'family/family_form.html', {'form': form, 'member': member})
    else:
        return redirect('family:family_details', family_id=family.id)

def FamilyDetails(request, family_id):
    instance = Family.objects.get(pk=family_id)
    member = instance.head_of_family_individual_id
    if request.method == 'POST':
        form = FamilyForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('family:family_list')
    else:
        form = FamilyForm(instance=instance)
    return render(request, 'family/family_form.html', {'form': form, 'member': member, 'family': instance})

@login_required
def FamilyList(request):
    families = Family.objects.filter(head_of_family_individual_id__created_by=request.user)
    return render(request, 'family/family_list.html', {'families': families})

# Relationship
@login_required
def ChooseFamily(request, member_id):
    member = Individual.objects.get(pk=member_id)
    families = Family.objects.exclude(relationship__individual_1_id=member_id).exclude(head_of_family_individual_id=member_id)
    return render(request, 'family/relationship_choose_family.html', {'member': member, 'families': families})

@login_required
def JoinInFamily(request, member_id, family_id):
    member = Individual.objects.get(pk=member_id)
    family = Family.objects.get(pk=family_id)
    
    head_member = Individual.objects.filter(family__id=family_id)
    other_members = Individual.objects.filter(individual_1__family_id=family_id, individual_1__relationship_type_code='C')
    members = head_member | other_members

    roles2 = Role.objects.filter(Q(role_code='F') | Q(role_code='M') | Q(role_code='H') | Q(role_code='W'))

    if request.method == 'POST':
        form = RelationshipForm(request.POST)
        if form.is_valid():
            relation = form.save(commit=False)
            relation.family_id = family
            relation.individual_1_id = member

            role2 = relation.individual_2_role_code.role_code

            if role2 == 'F' or role2 == 'M':
                type_code = 'C'
            else:
                type_code = 'M'
            if type_code == 'C':
                if member.gender == 'M':
                    role_code = 'S'
                else: 
                    role_code = 'D'
            else:
                if member.gender == 'M':
                    role_code = 'H'
                else: 
                    role_code = 'W'

            relation.relationship_type_code = Relationship_Type.objects.get(relationship_type_code=type_code)
            relation.individual_1_role_code = Role.objects.get(role_code=role_code)
            relation.save()
            return redirect('family:my_member')
    else:
        form = RelationshipForm()
    return render(request, 'family/relationship_form.html', {'form': form, 'member': member, 'family': family, 'members': members, 'roles': roles2})

def FamilyRelationship(request, family_id):
    head_member = family = Family.objects.get(pk=family_id).head_of_family_individual_id
    relations = Relationship.objects.filter(family_id=family_id)
    return render(request, 'family/relationship_genealogy.html', {'head_member': head_member, 'relations': relations})
