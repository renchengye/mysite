from django.conf.urls import url
from . import views

app_name = 'family'
urlpatterns = [
    url(r'^$', views.Index),
    url(r'^familyList/$', views.FamilyList, name='family_list'),
    url(r'^(?P<family_id>[0-9]+)/$', views.FamilyDetails, name='family_details'),
    url(r'^(?P<family_id>[0-9]+)/memberList/$', views.FamilyMemberList, name='member_list'),
    url(r'^(?P<family_id>[0-9]+)/relation/$', views.FamilyRelationship),

    url(r'^createMember/$', views.CreateMember, name='create_member'),
    url(r'^member/(?P<member_id>[0-9]+)/$', views.MemberDetails, name='member'),
    url(r'^member/(?P<member_id>[0-9]+)/modify$', views.ModifyMember, name='modify_member'),
    
]