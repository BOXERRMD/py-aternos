# Import
from python_aternos import Client, Lists
import time
import asyncio


atclient = Client()

atclient.login('test7747', '147258369', restore_session=True)

a = atclient.account.list_servers()

server = a[0]

if server.status == 'offline':
    server.start(accepteula=True)

print(server.config().set_java(21.3))

