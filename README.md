Skype-iplookup
======================

Perform obscure ip lookup for online skype account.

Can find local and remote ip address.

Based on deobfuscated Skypekit runtime that write clear debug log.

How to use?
-----------

First of all you need cracked Skypekit. 

magnet:?xt=urn:btih:3da068082f6ec70be379d4046e4c77bc4578f751&dn=SkypeKit_sdk%2Bruntimes_370_412.zip&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.ccc.de%3A80

This Skypekit also don't need request certificate from Skype Inc to use it. You can made your own skype client/plugin and share sources without proprietary Skypekit. 

To run skypekit you need compile and run video loopback:  skypekit-sdk_runtime-3.7.0/reference/videortphost-loopback (require premake4 and g++-multilibs for compile)

Skypekit listen 127.0.0.1:8963 for wrapper connection. It make local SSL tunnel.  Archive contain keypair.pem, this key used to encrypt local connection.

You must setup this key in examples/python/tutorial/keypair.py

    keyFileName = '../../../keypair.pem';
    distroRoot      = '../../../';

	
1. Run Skypekit and video loopback

    ./skypekit-sdk_runtime-3.7.0/reference/videortphost-loopback/build/videortphost-loopback
    
	./skypekit-sdk_runtime-3.7.0/bin/linux-x86/RUNTIME_linux-x86-skypekit-voicertp-videortp_3.7.0 -x -m -d logname

2. Put server.py in ./skypekit-sdk_runtime-3.7.0/examples/python/tutorial/ and run it

    python2.6.5 ./server.py username password

  Be aware to login with your main account!


3. Edit path to log file in client.py and try it.




-------------
Read more about Skypekit python api http://developer.skype.com/skypekit/reference/python/html/help.html

For additional help go to xmpp:skypeopensource@conference.jabber.ru

