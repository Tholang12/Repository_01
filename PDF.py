#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install PyPDF2')


# *****PDF DATA EXTRACTER*****

# In[4]:


import PyPDF2 as p2


# In[7]:


PDFfile = open("C:/Users/milad/OneDrive/Desktop/Intern/PDF/Invoice-Invoice.pdf","rb")


# In[9]:


pdfread = p2.PdfFileReader(PDFfile)


# ***Ectract Single Page***

# In[13]:


x = pdfread.getPage(0)


# In[14]:


print(x.extractText())


# In[15]:


print(pdfread.getIsEncrypted())


# In[16]:


print(pdfread.getDocumentInfo())


# In[18]:


print(pdfread.getNumPages())


# *** Ectract Entire PDF ***

# In[19]:


i = 0
while i<pdfread.getNumPages():
    pageinfo = pdfread.getPage(i)
    print(pageinfo.extractText())
    i = i+1

