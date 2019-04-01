from django import forms

from user.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def clearn_min_distance(self):
        cleaned_data = super().clean()
        min_distance = cleaned_data['min_distance']
        print('************')
        print(cleaned_data)

        max_distance = cleaned_data['max_distance']
        if min_distance > max_distance:
            raise forms.ValidationError('min_distance 大于 max_distance')
        return min_distance

    def clearn_min_dating_age(self):
        cleaned_data = super().clean()
        min_dating_age = cleaned_data['min_dating_age']

        max_dating_age = cleaned_data['max_dating_age']
        if min_dating_age > max_dating_age:
            raise forms.ValidationError('min_dating_age 大于 max_dating_age')
        return min_dating_age
