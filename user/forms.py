from django import forms

from user.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def clean_max_distance(self):
        cleaned_data = super().clean()
        min_distance = cleaned_data['min_distance']

        max_distance = cleaned_data['max_distance']
        if min_distance > max_distance:
            raise forms.ValidationError('min_distance 大于 max_distance')
        return max_distance

    def clean_max_dating_age(self):
        cleaned_data = super().clean()
        min_dating_age = cleaned_data['min_dating_age']

        max_dating_age = cleaned_data['max_dating_age']
        if min_dating_age > max_dating_age:
            raise forms.ValidationError('min_dating_age 大于 max_dating_age')
        return max_dating_age
