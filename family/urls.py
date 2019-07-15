from django.conf.urls import url
from . import views

app_name = 'family'
urlpatterns = [
    url(r'^$', views.Index, name='index'),

    url(r'^member/myMemberList/$', views.MyMemberList, name='my_member'),
    url(r'^member/memberListOfFamily/(?P<family_id>[0-9]+)/$', views.FamilyMemberList, name='member_list'),
    url(r'^member/createMember/$', views.CreateMember, name='create_member'),
    url(r'^member/(?P<member_id>[0-9]+)/$', views.ModifyMember, name='modify_member'),

    url(r'^family/myFamilyList/$', views.FamilyList, name='family_list'),
    url(r'^family/(?P<family_id>[0-9]+)/$', views.FamilyDetails, name='family_details'),
    url(r'^family/createFamilyByMember/(?P<member_id>[0-9]+)/$', views.CreateFamily, name='create_family'),

    url(r'^relationship/member/(?P<member_id>[0-9]+)/chooseFamily/$', views.ChooseFamily, name='choose_family'),
    url(r'^relationship/member/(?P<member_id>[0-9]+)/joinFamily/(?P<family_id>[0-9]+)/$', views.JoinInFamily, name='join_family'),
    url(r'^relationship/genealogyOfFamily/(?P<family_id>[0-9]+)/$', views.FamilyRelationship, name='relationship'),

]