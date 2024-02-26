# "pip install whois" to install the whois library

import whois
w = whois.query('google.com')
print(w.name)
print(w.registrar)
print(w.creation_date)
print(w.expiration_date)
print(w.last_updated)
print(w.name_servers)
print(w.status)
print(w.emails)
