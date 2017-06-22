#!/usr/bin/python3
import os;
from sys import exit;

class Site:
	def ensite( self, site ):
		site = str( site );

		# Append .conf automatically to the end if not specified
		site += '.conf' if not site.endswith( '.conf' ) else '';
		abs_site = site;
		abs_enabled = os.path.join( self.sites_enabled, site );
		abs_site = os.path.join( self.sites_available, abs_site.strip() );

		# Check if site to be enabled exists
		if not os.path.exists( abs_site ):
			print( 'Unable to enable site: {0} does not exist'.format( abs_site ) );
			exit( 1 );
		elif( os.path.exists( abs_enabled ) ):
			print( '{0} already enabled\nSkipping...Run\n\tsystemctl reload httpd'.format( site ) );
			exit();
		else:
			# Seems to exist, proceed with enabling
			print( 'Enabling \'{0}\' '.format( site ) );
			try:
				# Create a link from sites-available to sites-enabled. That's the whole trick
				os.symlink( abs_site, abs_enabled );
				print( "{0} enabled successfully\nReload httpd \n \t systemctl reload httpd".format( abs_site ) );
				exit();
			except IOError as e:
				# Oops! We have a problem.
				print( 'Unable to enable site:\n{0}'.format( e ) );
				exit( 1 );

	def dissite( self, site ):
		site = str( site );

		# Append .conf automatically to the end if not specified
		site += '.conf' if not site.endswith( '.conf' ) else '';

		# Create absolute path
		abs_enabled = os.path.join( self.sites_enabled, site );
		abs_available = os.path.join( self.sites_available, site );

		# Check if its enabled so to be disabled
		if not os.path.exists( abs_enabled ):
			print( '{0} is not enabled\nSkipping...Run:\n\tsystemctl reload httpd'.format( site ) );
			exit();
		else:
			print( 'Disabling \'{0}\''.format( site ) );
			try:
				# Unlink to disable
				os.unlink( abs_enabled );
				print( '{0} disabled successfully\nReload httpd\n\tsystemctl reload httpd'.format( site ) );
				exit( 1 );
			except IOError as e:
				print( 'Unable to disable site:\n{0}'.format( e ) );
				exit( 1 );

	def enabled_sites( self ):
		try:
			# Get list of files, iterate and print
			sites = os.listdir( self.sites_enabled );
			if len( sites ) > 0:
				for site in sites:
					print( site.strip( '.conf' ) );
				exit();
			else:
				print( 'No enabled sites' );
				exit();
		except IOError as e:
			print( e );
			exit( 1 );

	def available_sites( self ):
		try:
			# Get list of files, iterate and print
			available = os.listdir( self.sites_available );
			enabled = os.listdir( self.sites_enabled );
			disabled = list( set( available ).difference( enabled ) );
			
			for site in disabled:
				print( site.strip( '.conf' ) );

		except IOError as e:
			print( e );
			exit( 1 );