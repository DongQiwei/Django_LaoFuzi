from django import forms
from captcha.fields import CaptchaField
from django.forms import widgets


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误!"})


class OrderForms(forms.Form):
    address = forms.CharField(
        label="配送地址",
        required=True,
        widget=widgets.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "请输入配送地址",
            }),
        error_messages={
            "required": "对不起，配送地址不能为空！",
        }
    )
    pay_type = forms.ChoiceField(
        label="支付方式",
        required=True,
        choices=((0, '货到付款'), (1, '微信支付'), (2, '支付宝支付')),
        widget=forms.RadioSelect()
    )
    phone = forms.CharField(
        label="手机",
        required=True,
        widget=widgets.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "请输入手机",
            }),
        error_messages={
            "required": "对不起，手机不能为空！",
        }
    )
