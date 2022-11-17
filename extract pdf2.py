#!/usr/bin/env python
# coding: utf-8

# *****PDF DATA EXTRACTER*****

# In[1]:


import PyPDF2 as p2


# In[3]:


PDFfile = open("C:/Users/milad/OneDrive/Desktop/Intern/PDF/Invoice001..pdf","rb")


# In[4]:


pdfread = p2.PdfFileReader(PDFfile)


# ***Extract Single Page***

# In[6]:


x = pdfread.getPage(0)


# In[9]:


M = print(x.extractText().splitlines())


# In[17]:


print(pdfread.getDocumentInfo())


# In[18]:


print(pdfread.getNumPages())


# In[19]:


M = ['INVOICE', '# 001', 'RPA NUGGETS', '44 Melrose Boulevard, Melrose Arch', 'Johannesburg', '2196', 'www.rpanuggets.com', 'info@rpanuggets.com', 'FNB', 'Account Number: 62884518675 RPA', 'NUGGETS PTY (LTD)', 'Bill To:', 'Dr Motsamai A', 'Date:', 'Due Date:', 'Balance Due:', 'Feb 11, 2021', 'Feb 19, 2021', 'ZAR 11,500.00', 'Item Quantity Rate Amount', 'Intelligent Automation Training', '1 ZAR 8,000.00 ZAR 8,000.00', 'Subtotal:', 'Tax (15%):', 'Total:', 'Notes:', 'This admission fee is exclusive of exam fees ', 'ZAR 10,000.00 ZAR 1,500.00 ZAR 11,500.00']


# In[21]:


print (M[1]) # invoice number


# In[22]:


print (M[2]) # company name


# In[23]:


print (M[7]) # email


# In[24]:


print (M[16]) # due date


# In[28]:


print (M[27].split(' ')[5].strip()) # amount


# In[31]:


print (M[9].split(' ')[2].strip()) # account number

