from django import forms 


class UserSendEmailForm(forms.Form):
	parent_email = Forms.EmailField(max_length=245)
	


