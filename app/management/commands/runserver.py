import sys

from django.contrib.staticfiles.management.commands.runserver import (
    Command as RunserverCommand,
)
from django.db import connections
from django.db.utils import OperationalError


class Command(RunserverCommand):
    """Custom runserver command that tests database connections before starting the server."""
    help = "Starts the development server after testing the database connection."

    def execute(self, *args, **options):
        # Read the verbosity level passed to manage.py (defaults to 1)
        verbosity = options.get('verbosity', 1)
        
        if verbosity > 0:
            self.stdout.write(self.style.WARNING("Testing database connections..."))
            
        # Loop through and verify all configured databases in settings.py
        for db_alias in connections:
            try:
                connection = connections[db_alias]
                # Forces Django to physically connect and run a low-level check
                connection.ensure_connection()
                
                if verbosity > 0:
                    self.stdout.write(
                        self.style.SUCCESS(f"Successfully connected to database alias: '{db_alias}'")
                    )
            except OperationalError as e:
                self.stderr.write(
                    self.style.ERROR(f"Database connection failed for alias '{db_alias}'!")
                )
                self.stderr.write(self.style.ERROR(f"Error details: {e}"))
                self.stderr.write(self.style.ERROR("Exiting server startup."))
                sys.exit(1)

        # If all databases pass, hand execution back to the standard runserver logic
        return super().execute(*args, **options)
