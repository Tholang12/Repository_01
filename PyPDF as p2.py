#!/usr/bin/env python
# coding: utf-8

# In[1]:



import PyPDF2 as p2

PDFfile = open("C:/Users/milad/OneDrive/Desktop/Intern/PDF/Invoice-Invoice.pdf","rb")


# In[2]:


pdfread = p2.PdfFileReader(PDFfile)


# In[3]:


x = pdfread.getPage(0)


# In[4]:


print(x.extractText().splitlines())


# In[5]:


print(pdfread.getIsEncrypted())


# In[6]:


print(pdfread.getDocumentInfo())


# In[7]:


print(pdfread.getNumPages())


# In[8]:


i = 0
while i<pdfread.getNumPages():
    pageinfo = pdfread.getPage(i)
    print(pageinfo.extractText())
    i = i+1


# In[9]:


l = ['Your Company', '123 Your Street', 'Your City, ST 12345', '(123) 456-7890', 'Invoice', 'Submitted on 01/01/2000', 'Invoice for Payable to Invoice #', 
     'Name Name 123456', 'Company name', 'Street address Project Due date', 'City, State, Zip Project name 1/3/2000', 'Description Qty Unit price Total price',
     'Item #1 1 $200.00 $200.00', 'Item #2 2 $200.00 $400.00', '$0.00', '$0.00', 'Notes: Subtotal $600.00', 'Adjustments -$100.00', '$500.00']


# In[10]:


l[3].replace('(','').replace(')','').replace('-','').replace(' ','').strip()
l[5].split('Submitted on ')[1]
print (l[2].split(',')[0])


# In[11]:


print (l[2].split(',')[1].strip())


# In[12]:


l = ['Your Company', '123 Your Street', 'Your City, ST 12345', '(123) 456-7890', 'Invoice', 'Submitted on 01/01/2000', 'Invoice for Payable to Invoice #', 
     'Name Name 123456', 'Company name', 'Street address Project Due date', 'City, State, Zip Project name 1/3/2000', 'Description Qty Unit price Total price',
     'Item #1 1 $200.00 $200.00', 'Item #2 2 $200.00 $400.00', '$0.00', '$0.00', 'Notes: Subtotal $600.00', 'Adjustments -$100.00', '$500.00']


# In[13]:


print (l[7].split(' ')[2].strip())


# In[14]:


print (l[8])


# In[15]:


print (l[10].split(' ')[5].strip())


# In[16]:


print (l[18].split(' ')[0].strip())


# In[17]:


print (l[10].split(' ')[5].strip())


# In[18]:


print (l[2].split(',')[1].strip())


# In[ ]:




