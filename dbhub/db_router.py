# db_router.py

class MultiDBRouter:
    """
    Routes database operations:
    - Tenant apps and shared apps → PostgreSQL ("default")
    - MySQL apps → mysql_db
    - SQLite apps → sqlite_db
    """

    POSTGRES_APPS = ['core', 'client_app']
    MYSQL_APPS = []
    SQLITE_APPS = []

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.POSTGRES_APPS:
            return 'default'
        elif model._meta.app_label in self.MYSQL_APPS:
            return 'mysql_db'
        elif model._meta.app_label in self.SQLITE_APPS:
            return 'sqlite_db'
        return None

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        db_set = set([self.db_for_read(obj1._meta.model),
                      self.db_for_read(obj2._meta.model)])
        return len(db_set) == 1

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure apps go to correct database:
        - Tenant + Shared apps → default (PostgreSQL)
        - MySQL apps → mysql_db
        - SQLite apps → sqlite_db
        """
        if app_label in self.POSTGRES_APPS:
            return db == 'default'
        elif app_label in self.MYSQL_APPS:
            return db == 'mysql_db'
        elif app_label in self.SQLITE_APPS:
            return db == 'sqlite_db'
        return None