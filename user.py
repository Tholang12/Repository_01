#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

 # Create	your forms here.

class NewUserForm(UserCreat1onForm):
email = forms.EmailField (required=True) 
class Meta:
model = User
fields  =  ("username",	"emall",	"password1",	" password2")
def	save(self,	comm1t=True):	
user = super (NewUserForm,	self) . save(commit= False)
user.email = self.cleaned_data['email']
if commit:
user.save()
return user 

