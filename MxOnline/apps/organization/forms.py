__date__ = '2018/8/23 0023 上午 10:40'
from django import forms
from operation.models import UserAsk
import re


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        验证手机号码是否合法
        :return:
        """
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^[1][3,4,5,7,8][0-9]{9}$"
        p = re.compile(REGEX_MOBILE)

        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('手机号码非法', code="mobile_invalid")
