#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pdfplumber
import pandas as pd
invoice = open("C:\\Users\\milad\\OneDrive\\Desktop\\Intern\\PDF\\PDF Editor1.PDF","rb")
with pdfplumber.open(invoice) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()
print(text)


# In[14]:


for row in text.split('/n'):
    if row.startswith(''):
        accountnumber = row.split()[19+20]
accountnumber


# In[41]:


for row in text.split('\n'):
    if row.startswith('PR'):
        Invoice = row.split()[0]
Invoice


# In[42]:


for row in text.split('/n'):
    if row.startswith(''):
        companyname = row.split()[4+6]
companyname


# In[45]:


for row in text.split('/n'):
    if row.startswith(''):
        Date = row.split()[28:29]
Date


# In[79]:


for row in text.split('/n'):
    if row.startswith(''):
        Amount = row.split()[29+30]
Amount


# In[80]:


data = pd.DataFrame({'mail':mail,'Invoice':Invoice,'Date':Date, 'companyname':companyname,'Amount':Amount,'Accountnumber':accountnumber})
datatoexcel = pd.ExcelWriter("Template data export sheet.xlsx",engine='xlsxwriter')
data.to_excel(datatoexcel, sheet_name = 'Sheet2')
datatoexcel.save()


# In[ ]:





# In[ ]:




