#!/usr/bin/env python
# coding: utf-8

# In[ ]:


{% extends "main/header.html"%}

{% block content %}

{% load crispy_forms_tags %}

<!--Register-->
<div class="container py-50"
    <h1>Register</h1>
    <form method="POST">
    {% csrf_token %}
    {{ register_form|crispy}}
    <button class="btn btn-primary" type="submit">Register</button>
    </form>
    <p class="text-center">If you already have an account, <a href="/login">login</a> instead.</p>
    </div>
