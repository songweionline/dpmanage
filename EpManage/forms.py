from django.forms import Form
from django.forms import fields


class LoginForm(Form):
    user_id = fields.CharField(
        required=True,
        min_length=3,
        max_length=18,
        error_messages={
            "required":"用户名不可以为空！",
            "min_length":"用户名不能低于3位！",
            "max_length":"用户名不能超过18位！"
        }
    )
    password = fields.CharField(
        required=True,
        error_messages={
            "required": "密码不可以空",
        }
    )
