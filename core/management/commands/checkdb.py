from django.core.management.base import BaseCommand
from django.db import connections

class Command(BaseCommand):
    help = "Check database connections"

    def handle(self, *args, **kwargs):

        print("\nChecking for PostgreSQL (default)")
        try:
            connections["default"].cursor()
            print("Connection is successful")
        except Exception as e:
            print("Connection failed ❌")
            print(e)

        print("\nChecking for MySQL")
        try:
            connections["mysql_db"].cursor()
            print("Connection is successful")
        except Exception as e:
            print("Connection failed ❌")
            print(e)

        print("\nChecking for SQLite")
        try:
            connections["sqlite_db"].cursor()
            print("Connection is successful")
        except Exception as e:
            print("Connection failed ❌")
            print(e)