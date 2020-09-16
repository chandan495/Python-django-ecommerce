from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class GuestForm(forms.Form):
	email = forms.EmailField()

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
		attrs={
		"class":"form-control",
		"placeholder":"Enter your name"
		 	}
		 )
	)
	password = forms.CharField(widget=forms.PasswordInput(
		attrs={
		"class":"form-control",
		"placeholder":"*************"
		 	}
		 )
	)

class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
		attrs={
		"class":"form-control",
		"placeholder":"Enter your name"
		 	}
		 )
	)
	email = forms.EmailField(widget=forms.EmailInput(
		attrs={
		"class":"form-control",
		"placeholder":"Enter your Email Address"
			}
		)
	)
	password = forms.CharField(widget=forms.PasswordInput(
		attrs={
		"class":"form-control",
		"placeholder":"*************"
		 	}
		 )
	)
	password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
		attrs={
		"class":"form-control",
		"placeholder":"*************"
		 	}
		 )
	)

	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("user has aleardy exists")
		return username
	
	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email has aleardy exists")
		return email

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("Must match the confirm passwor")
		return data