#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#  keyring-test.py(c) RYX 2007 <ryx [at] ryxperience [dot] com>

import gtk


try: 
	import gnomekeyring 
except ImportError: 
	HAVE_GNOMEKEYRING = False 
else: 
	HAVE_GNOMEKEYRING = True 

# TEST:
#import gobject
#gtk.set_application_name("keyring-test")
if HAVE_GNOMEKEYRING:
	# check availability
	if not gnomekeyring.is_available():
		print "Keyring not available."
	# list names of keyrings and use the first one we can find
	keyring_list = gnomekeyring.list_keyring_names_sync()
	if len(keyring_list) == 0:
		print "No keyrings available."
		import sys
		sys.exit(1)
	else:
		print "We have %i keyrings" % len(keyring_list)
		print "KEYRING: %s" % keyring_list[0]
	# name/password to store
	name		= 'myname'
	password	= 'mysecret'
	# get default keyring
	keyring = gnomekeyring.get_default_keyring_sync() 	# crashes if no default exists
	# create attributes
	attribs = dict(name=name, magic='something')
	
	# create keyring item with password
	auth_token = gnomekeyring.item_create_sync(keyring, 
		gnomekeyring.ITEM_GENERIC_SECRET, name, attribs, password, True) 
	print auth_token
	print "save: token for account %s: %i" % (name, auth_token) 
	token = "gnomekeyring:%i" % (auth_token,) 
	print token
	
	# now read it back from the keyring
	print "Password read from keyring is:"
	print gnomekeyring.item_get_info_sync(keyring, auth_token).get_secret()

