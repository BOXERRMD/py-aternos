<div align="center">
    <img src="https://i.ibb.co/3RXcXJ1/aternos-400.png" alt="Python Aternos Logo">
    <h1>
        Python Aternos
        <div>
            <a href="https://pypi.org/project/python-aternos/">
                <img src="https://img.shields.io/pypi/v/python-aternos">
            </a>
            <a href="https://www.apache.org/licenses/LICENSE-2.0.html">
                <img src="https://img.shields.io/pypi/l/python-aternos">
            </a>
            <a href="https://github.com/DarkCat09/python-aternos/commits">
                <img src="https://img.shields.io/github/last-commit/DarkCat09/python-aternos">
            </a>
            <a href="https://github.com/DarkCat09/python-aternos/issues">
                <img src="https://img.shields.io/github/issues/DarkCat09/python-aternos">
            </a>
        </div>
    </h1>
</div>

An unofficial Aternos API written in Python.  
It uses [aternos](https://aternos.org/)' private API and html parsing.

> # WARNING !
> Development has been resumed, but it's possible that the module **contains functions/classes that don't work at the moment**. 
> However, you can still manage your server with peace of mind *(start, too much, restart...)*.

Python Aternos supports:

 - Logging in to account with password (plain or hashed) or `ATERNOS_SESSION` cookie value
 - Saving session to the file and restoring
 - Changing username, email and password
 - Parsing Minecraft servers list
 - Parsing server info by its ID
 - Starting/stoping server, restarting, confirming/cancelling launch
 - Updating server info in real-time (see [WebSocket API](https://python-aternos.codeberg.page/howto/websocket)) `NOT IMPLEMENTED`
 - Changing server subdomain and MOTD (message-of-the-day)
 - Managing files, settings, players (whitelist, operators, etc.)

## Install

### Common
```bash
$ pip install python-aternos
```
> **Note** for Windows users
>
> Install `lxml` package from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml)
> if you have problems with it, and then execute:  
> `pip install --no-deps python-aternos`

### Development
```bash
$ git clone https://github.com/BOXERRMD/python-aternos.git
$ cd python-aternos
$ pip install -e .[dev]
```

## Usage
To use Aternos API in your Python script, import it
and login with your username and password or its MD5 hash.

Then request the servers list using `list_servers()`.  
You can start/stop your Aternos server, calling `start()` or `stop()`.

Here is an example how to use the API:
```python
# Import
from python_aternos import Client

# Create object
atclient = Client()

# Log in
# with username and password
atclient.login('example', 'test123')
# ----OR----
# with username and MD5 hashed password
atclient.login_hashed('example', 'cc03e747a6afbbcbf8be7668acfebee5')
# ----OR----
# with session cookie
atclient.login_with_session('ATERNOS_SESSION cookie value')

# Get AternosAccount object
aternos = atclient.account

# Get servers list
servs = aternos.list_servers()

# Get the first server
myserv = servs[0]

# Start
myserv.start()
# Stop
myserv.stop()

# You can also find server by IP
testserv = None
for serv in servs:
    if serv.address == 'test.aternos.org':
        testserv = serv

if testserv is not None:
    # Prints the server software and its version
    # (for example, "Vanilla 1.12.2")
    print(testserv.software, testserv.version)
    # Starts server
    testserv.start()
```

## [More examples](https://github.com/DarkCat09/python-aternos/tree/main/examples)

## [Documentation](https://python-aternos.codeberg.page)

## [How-To Guide](https://python-aternos.codeberg.page/howto/auth)

## Changelog
|      Version      | Description                                                                                                                                                                     |
|:-----------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       v0.3        | Implemented files API, added typization.                                                                                                                                        |
|       v0.4        | Implemented configuration API, some bugfixes.                                                                                                                                   |
|       v0.5        | The API was updated corresponding to new Aternos security methods. Huge thanks to [lusm554](https://github.com/lusm554).                                                        |
|  **v0.6/v1.0.0**  | Code refactoring, websockets API and session saving to prevent detecting automation access.                                                                                     |
|      v1.0.x       | Lots of bugfixes, changed versioning (SemVer).                                                                                                                                  |
|      v1.1.x       | Documentation, unit tests, pylint, bugfixes, changes in atwss.                                                                                                                  |
| **v1.1.2/v2.0.0** | Solution for [#25](https://github.com/DarkCat09/python-aternos/issues/25) (Cloudflare bypassing), bugfixes in JS parser.                                                        |
|      v2.0.x       | Documentation, automatically saving/restoring session, improvements in Files API.                                                                                               |
|      v2.1.x       | Fixes in websockets API, atconnect (including cookie refreshing fix). Support for captcha solving services (view [#52](https://github.com/DarkCat09/python-aternos/issues/52)). |
|      v2.2.x       | Node.JS interpreter support.                                                                                                                                                    |
|      v3.0.0       | Partially rewritten, API updates.                                                                                                                                               |
|      v3.0.5       | Unmaintained.                                                                                                                                                                   |
|      v3.1.x       | TODO: Full implementation of config API.                                                                                                                                        |
|      v3.2.x       | TODO: Shared access API and maybe Google Drive backups.                                                                                                                         |
|      v3.0.7       | Maintained                                                                                                                                                                      |

## Reversed API Specification
Private Aternos API requests were captured into
[this HAR file](https://github.com/DarkCat09/python-aternos/blob/main/aternos.har)
and were imported to
[a Postman Workspace](https://www.postman.com/darkcat09/workspace/aternos-api).  
You can use both resources to explore the API.  
Any help with improving this library is welcome.

## License
[License Notice:](https://github.com/DarkCat09/python-aternos/blob/main/NOTICE)
```
Copyright 2021-2022 All contributors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

#### *Thank to **Darkcat09** for allowing me to continue maintaining this API*

