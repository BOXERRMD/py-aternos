# Import
from python_aternos import Client

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
testserv = None
for serv in servs:
    if (serv.ip == 'test7747.aternos.me'):
        testserv = serv

print(testserv)

if testserv is not None:
    # Prints the server software and its version
    # (for example, "Vanilla 1.12.2")
    print(testserv.software, testserv.version)
    # Starts server
    testserv.start()