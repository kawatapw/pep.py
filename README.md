# pep.py
The Kawata realtime server!

![image](https://user-images.githubusercontent.com/36131887/118535385-4fd4c200-b742-11eb-8886-7ba8463b8d57.png)

## What does it do?
This portion of the Kawata manages all of the real-time, packet related portions of the Bancho protocol. This includes but is not limited to:
- Logging in
- Chat
- Multiplayer
- Spectator
- Server Bot (RealistikBot)

## Why is our fork better?
This fork of pep.py has been developed specifically to suit the need of Kawata. With the rapid growth of the server, more and more demand has been placed on us in regards of features alongside performance. The original repo features a large quantity of fatal flaws alongside performance hogs, and through our usage of the software, we have solved a majority of those issues.

- Fixed multiplayer
- MASSIVE OPTIMISATIONS (your database will thank you)
- Relax and Autopilot support
- Extended Redis API
- Extended 3rd party API support
- Customised HWID system
- Extended in-game bot commands
- Python 3.9 support!

## Requirements
To run pep.py, there is an list of requirements to ensure the server runs at all.
- Python >=3.6
- Kawata MySQL Database
- Cython + GCC
- Linux (preferably Ubuntu 18.04)

## Notes for potential users
If you are planning on using our fork of pep.py, there is a multitude of things to consider that are unique to our variant
- Low reliance on `userutils` for performance reasons.

The entire `userutils` module promotes inefficient use of the database. This is especially bad on established servers with large
databases, where the cost of each query becomes more and more expensive with every user. This appends unnecessary stress on the
database and as a consequence, the server as a whole.
- Private database

Due to the old nature of the origin code, the age of the modules is **quite large**. This means that we do not benefit from any improvements,
bugfixes or any other quality of life improvements of any new module updates. This is an issue with the whole Python based Ripple stack, and is
not an exclusive to Kawata pep.py. **This issue is however planned on being addressed soon.**
