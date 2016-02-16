import requests
from BeautifulSoup import BeautifulSoup

url = "http://192.168.1.154/dvwa/login.php"

r= requests.get(url)
soup = BeautifulSoup(r.text)

#print [(element['value']) for element in soup.find_all('input')]
#print soup

texts = soup.body.findAll('input', {'type':'text'})
passwords = soup.body.findAll('input', {'type':'password'})
action = soup.find('form').get('action')

U =[]
P=[]

# These loops finds all text and password input fields from the body
for elem in texts:
   U.append(elem['name'])
for elem in passwords:
   P.append(elem['name'])


# lets do some error checking....
if len(U) > 1:
   raise ValueError('to many user name values')
if len(U) < 1:
   raise ValueError('no user name value')
if len(P) > 1:
   raise ValueError('to many passwords')
if len(P) < 1:
   raise valueError('no password value')

print "USERNAME VARIABLE =" + U[0]
print "PASSWORD VARIABLE =" + P[0]
print "ACTION VARIABLE =" + action




