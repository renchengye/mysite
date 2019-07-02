from django.forms import ModelForm
from .models import Individual

class MemberForm(ModelForm):
    class Meta:
        model = Individual
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'place_of_birth','other_individual_details', 'image_path']
        localized_fields = ('date_of_birth',)
