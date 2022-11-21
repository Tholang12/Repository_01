# scratching data from PDF and JPG with 500 trial scan frees with 98% accuracy, use ***hub.veryfi.com*** website

import pprint
import veryfi
pip install veryfi

# First we need enrolment on the website and put our informations below

client_id = ''      #put your id from website
client_secret = ''  #put your client secret
username=''         #put your username
api_key=''          #put your key

# hub.veryfi.con/singup/veryfidemo/ - 1 month free and 500 scans

client = veryfi.Client(client_id,  client_secret, username, api_key)

#you can set your category that you want to scratch  

categories = [""]   #set your categories 

json_result = client.process_document("files/invoice.pdf", categories) #address your files 

pprint.pprint(json_result)
