import time

from django.core.management import BaseCommand
from django.db import OperationalError, connection
from django.db.backends.mysql.base import DatabaseWrapper

connection: DatabaseWrapper = connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for DB...')
        db_conn = False

        while not db_conn:
            try:
                connection.ensure_connection()
                db_conn = True
            except OperationalError:
                self.stdout.write('DB is not unavailable, wait 3 seconds....')
                time.sleep(3)

        self.stdout.write('DB is available!')