from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Your Full Name"
                }
            )
        )
    email    = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder":"Your Email"
                }
            )
        )
    content  = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Message'
                }
            )
        )

    def clean_email(self):
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail")
        return email

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()