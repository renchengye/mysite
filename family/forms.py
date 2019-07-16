from django.forms import ModelForm
from .models import Individual, Family, Relationship

class MemberForm(ModelForm):
    class Meta:
        model = Individual
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'place_of_birth', 'other_individual_details', 'image_path']
        localized_fields = ('date_of_birth',)

class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = ['family_name', 'family_description', 'family_date_from', 'family_date_to','other_family_details', 'image_path']
        localized_fields = ('family_date_from', 'family_date_to')

class RelationshipForm(ModelForm):
    class Meta:
        model = Relationship
        fields = ['individual_2_id', 'individual_2_role_code', 'date_relationship_started', 'date_relationship_ended', 'relationship_place', 'other_relationship_details']
        localized_fields = ('date_relationship_started', 'date_relationship_ended')
