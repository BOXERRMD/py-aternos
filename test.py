# Import
from python_aternos import Client, Lists
import time



# Create object
atclient = Client()



# Log in
# with username and password
atclient.login('test7747', '147258369')


u = atclient.account.list_servers(cache=False)
print(u)

a = u[0]





# Get AternosAccount object











