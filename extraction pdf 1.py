#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pdfplumber
import pandas as pd


# In[2]:


invoice = open("C:\\Users\\milad\\OneDrive\\Desktop\\Intern\\PDF\\PDF Editor.PDF","rb")
with pdfplumber.open(invoice) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()
print(text)


# In[29]:


# *** find each detail that we need ***
# ***extraction account number***
for row in text.split('\n'):
    if row.startswith('#'):
        accountnumber = row.split()[1]


# In[30]:


accountnumber


# In[34]:


for row in text.split('\n'):
    if row.startswith('Invoice #'):
        Invoice = row.split()[-1]


# In[35]:


Invoice


# In[61]:


for row in text.split('/n'):
    if row.startswith(''):
        companyname1 = row.split()[4+6]


# In[62]:


companyname1


# In[63]:


for row in text.split('/n'):
    if row.startswith(''):
        companyname2 = row.split()[5+6]


# In[64]:


companyname2


# In[65]:


companyname = companyname1 + companyname2


# In[66]:


companyname


# In[70]:


for row in text.split('/n'):
    if row.startswith(''):
        mail = row.split()[34:35]
mail


# In[80]:


for row in text.split('/n'):
    if row.startswith(''):
        Date = row.split()[0+2]
Date


# In[93]:


for row in text.split('\n'):
    if row.startswith('$'):
        Amount = row.split()[0]
Amount


# In[95]:


data = pd.DataFrame({'mail':mail,'Invoice':Invoice,'Date':Date, 'companyname':companyname,'Amount':Amount,'Accountnumber':accountnumber})
datatoexcel = pd.ExcelWriter("Template data export sheet.xlsx",engine='xlsxwriter')
data.to_excel(datatoexcel, sheet_name = 'Sheet2')
datatoexcel.save()


# In[ ]:




