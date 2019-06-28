from django import forms

class MemberForm(forms.Form):
    GENDER = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    first_name = forms.CharField()
    last_name = forms.CharField()
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER)
    date_of_birth = forms.DateField()
    place_of_birth = forms.CharField()
    other_individual_details = forms.CharField(widget=forms.Textarea)
    image_path = forms.FileField()
