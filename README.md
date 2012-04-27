Skype-iplookup
======================

Perform obscure ip lookup for online skype account.

Can find local and remote ip address.

Based on deobfuscated Skypekit runtime that write clear debug log.

How to use?
-----------

First of all you need cracked Skypekit. 

magnet:?xt=urn:btih:3da068082f6ec70be379d4046e4c77bc4578f751&dn=SkypeKit_sdk%2Bruntimes_370_412.zip&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.ccc.de%3A80

This runtime also don't need certificate from Skype LTD to use it. You can made your own skype client/plugin and share sources without proprietary Skypekit. 

1. Run Skypekit

    ./skypekit-sdk_runtime-3.7.0/bin/linux-x86/RUNTIME_linux-x86-skypekit-voicertp-videortp_3.7.0 -x -m -d logname
	
2. Put server.py in ./skypekit-sdk_runtime-3.7.0/examples/python/tutorial/ and run it

    python2.6.5 ./server.py username password

Be aware to login with your main account!


3. Edit path to log file in client.py and try it.


### For additional help go to skypeopensource@conference.jabber.ru

