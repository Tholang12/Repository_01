#!/usr/bin/env python
# coding: utf-8

# ***Using pdfplumber library for extracting the text***

# In[ ]:


import pdfplumber


# In[10]:


invoice = open("C:/Users/milad/OneDrive/Desktop/Intern/PDF/Invoice001..pdf","rb")


# In[12]:


with pdfplumber.open(invoice) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()


# In[13]:


print(text)


# *** find each detail that we need ***

# ***extraction account number***

# In[31]:


for row in text.split('\n'):
    if row.startswith('Account Number:'):
        accountnumber = row.split()[-2]


# In[32]:


accountnumber


# *** Invoice numbers ***

# In[41]:


for row in text.split('\n'):
    if row.startswith('#'):
        Invoice = row.split()[-1]


# In[42]:


Invoice


# In[ ]:




