#!/usr/bin/python3
import os;
import sys;
from core import Site;
import argparse;

class CentOSHttpdTools( Site ):
	"""The base class"""
	def __init__( self ):
		super( CentOSHttpdTools, self ).__init__();
		self.sites_available = '/etc/httpd/sites-available';
		self.sites_enabled = '/etc/httpd/sites-enabled';

		try:
			if( not os.path.exists( self.sites_available ) ):
				os.mkdir( self.sites_available );

			if( not os.path.exists( self.sites_enabled ) ):
				os.mkdir( self.sites_enabled );
		except IOError as e:
			print( e );
			sys.exit( 1 );

parser = argparse.ArgumentParser( description = 'CentOS Httpd tools' );
parser.add_argument( 'action', help="Action to perform: ensite, dissite" );
parser.add_argument( 'object' );
args = parser.parse_args();

Tools = CentOSHttpdTools();
if args.action == 'ensite':
	Tools.ensite( args.object );
elif args.action == 'dissite':
	Tools.dissite( args.object );
elif args.action == 'show' and args.object == 'enabled':
	Tools.enabled_sites();
elif args.action == 'show' and args.object == 'available':
	Tools.available_sites();