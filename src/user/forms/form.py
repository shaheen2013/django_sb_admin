from django import forms


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs.update({'id': 'inputEmail'})
            self.fields['password'].widget.attrs.update({'id': 'inputPassword'})
            self.fields['username'].widget.attrs.update({'placeholder': 'Email address'})
            self.fields['password'].widget.attrs.update({'placeholder': 'Password'})
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
