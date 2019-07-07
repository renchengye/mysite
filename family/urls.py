from django.conf.urls import url
from . import views

app_name = 'family'
urlpatterns = [
    url(r'^$', views.Index, name='index'),

    url(r'^familyList/$', views.FamilyList, name='family_list'),
    url(r'^(?P<family_id>[0-9]+)/$', views.FamilyDetails, name='family_details'),
    url(r'^(?P<family_id>[0-9]+)/memberList/$', views.FamilyMemberList, name='member_list'),
    url(r'^(?P<family_id>[0-9]+)/relationship/$', views.FamilyRelationship, name='relationship'),    

    url(r'^createMember/$', views.CreateMember, name='create_member'),

    url(r'^member/(?P<member_id>[0-9]+)/modify$', views.ModifyMember, name='modify_member'),
    url(r'^member/(?P<member_id>[0-9]+)/createFamily/$', views.CreateFamily, name='create_family'),
    url(r'^member/(?P<member_id>[0-9]+)/joinFamily/$', views.JoinInFamily, name='join_family'),

    url(r'^myMemberList/$', views.MyMemberList, name='my_member'),

    
]