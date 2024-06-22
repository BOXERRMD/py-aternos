# Import
from python_aternos import Client
import time

# Create object
atclient = Client()

# Log in
# with username and password
atclient.login('test7747', '147258369')

# Get AternosAccount object
aternos = atclient.account



# Get servers list
servs = aternos.servers

# Get the first server
myserv = servs[0]

# Start

# You can also find server by IP
testserv = myserv


#print(testserv)

if testserv is not None:
    # Prints the server software and its version
    # (for example, "Vanilla 1.12.2")
    #print(testserv.software, testserv.version)
    # Starts server
    print(testserv.set_subdomain(value="test7747"))


