#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from django.shortcuts import render, redirect
from forms import NewUserForm
from django.contrib.auth import login 
from django.contrib import messages

def login_request(request):
    if request.mthod == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"You are now logged in as{username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
                else:
                    messages.error(request,"Invalid username or password.")
                    form = AuthenticationForm()
                    return render(request = requestr, template_name = "main/register.html",context={"form":form})

