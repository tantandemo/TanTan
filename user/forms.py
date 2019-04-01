from django import forms

from user.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    # def clean_min_distance(self):
    #     cleaned_data = super().clean()
    #     min_distance = cleaned_data['min_distance']
    #     print('************')
    #     print('距离')
    #
    #     max_distance = cleaned_data['max_distance']
    #     if min_distance > max_distance:
    #         raise forms.ValidationError('min_distance 大于 max_distance')
    #     return min_distance

    # 获取最大距离，并比较验证
    def clean_max_distance(self):
        cleaned_data = super().clean()
        print('max_dis')
        max_distance = cleaned_data['max_distance']
        print(max_distance)

        if self.min_distance > max_distance:
            raise forms.ValidationError('min_distance 大于 max_distance')
        return max_distance

    # 获取最短距离
    def clean_min_distance(self):
        cleaned_data = super().clean()
        print('min_dis')
        self.min_distance = cleaned_data['min_distance']
        print(self.min_distance)
        return self.min_distance





    # def clean_min_dating_age(self):
    #     cleaned_data = super().clean()
    #     min_dating_age = cleaned_data['min_dating_age']
    #
    #     print('************')
    #     print('年龄')
    #     max_dating_age = cleaned_data['max_dating_age']
    #     if min_dating_age > max_dating_age:
    #         raise forms.ValidationError('min_dating_age 大于 max_dating_age')
    #     return min_dating_age

    # 获取最小年龄
    def clean_min_dating_age(self):
        cleaned_data = super().clean()
        print('min_dating_age')
        self.min_dating_age = cleaned_data['min_dating_age']
        print(self.min_dating_age)
        return self.min_dating_age

    # 获取最大年龄，并比较
    def clean_max_dating_age(self):
        cleaned_data = super().clean()
        print('max_dating_age')
        max_dating_age = cleaned_data['max_dating_age']
        print(max_dating_age)
        if self.min_dating_age > max_dating_age:
            raise forms.ValidationError('min_dating_age 大于 max_dating_age')
        return max_dating_age