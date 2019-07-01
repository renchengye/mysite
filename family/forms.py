from django.forms import ModelForm
from .models import Individual

class MemberForm(ModelForm):
    class Meta:
        model = Individual
        fields = '__all__'
        # localized_fields = ('date_of_birth',)
