#!/usr/bin/env python
# coding: utf-8

# In[22]:


import re

import requests
import pdfplumber
import pandas as pd
from collections import namedtuple


# In[23]:


Inv = namedtuple('Inv', 'vend_num vend_name inv_dt due_dt inv_amt net_amt description')


# In[24]:


def download_file(url):
    local_filename = url.split('/')[-1]
    
    with requests.get(url) as r:
        with open(local_filename, 'wb') as f:
            f.write(r.content)
        
    return local_filename


# In[32]:


ap_url = 'https://www.tabs3.com/support/sample/apreports.pdf'


# In[35]:


ap = download_file(ap_url)


# In[36]:


with pdfplumber.open(ap) as pdf:
    page = pdf.pages[15]
    text = page.extract_text()


# In[37]:


print(text)


# In[38]:


new_vend_re = re.compile(r'^\d{3} [A-Z].*')


# In[39]:


for line in text.split('\n'):
    if new_vend_re.match(line):
        print(line)


# In[ ]:


for line in text.split('\n'):
    if new_vend_re.match(line):
        vend_num, *vend_name = line.split()
        vend_name = ' '.join(vend_name)
print(vend_num)
print(vend_name)


# In[ ]:


inv_line_re = re.compile(r'(\d{6}) (\d{6}) ([\d,]+\.\d{2}) [\sP]*([\d,]+\.\d{2}) [YN ]*\d (.*?) [*\s\d]')


# In[ ]:


line_items = []
for line in text.split('\n'):
    if new_vend_re.match(line):
        vend_num, *vend_name = line.split()
        vend_name = ' '.join(vend_name)    
    
    line = inv_line_re.search(line)
    if line:
        inv_dt = line.group(1)
        due_dt = line.group(2)
        inv_amt = line.group(3)
        net_amt = line.group(4)
        desc = line.group(5)
        line_items.append(Inv(vend_num, vend_name, inv_dt, due_dt, inv_amt, net_amt, desc))


# In[ ]:


df = pd.DataFrame(line_items)


# In[ ]:


df.head()


# In[ ]:


df['inv_dt'] = pd.to_datetime(df['inv_dt'])
df['due_dt'] = pd.to_datetime(df['due_dt'])


# In[ ]:


df.head()


# In[ ]:


df['inv_amt'] = df['inv_amt'].map(lambda x: float(x.replace(',', '')))


# In[ ]:


df['net_amt'] = df['net_amt'].map(lambda x: float(x.replace(',', '')))


# In[ ]:


df.sum()


# In[ ]:


df.to_csv('inv_lines.csv')

