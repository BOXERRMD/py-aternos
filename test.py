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

a.stop()

exit()

if not a.confirm():
    a.start()


while True:

    if a.countdown < 60 and a.confirm():
        a.add_countdown()

    time.sleep(10)





# Get AternosAccount object











