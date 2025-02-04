import os
import sqlite3

from django.conf import settings
from django.db import connection
from huey import crontab
from huey.contrib.djhuey import db_periodic_task

from conreq.utils.environment import get_database_type

DB_ENGINE = get_database_type()
HUEY_FILENAME = getattr(settings, "HUEY_FILENAME")


@db_periodic_task(crontab(minute="0", hour="0", strict=True))
def vacuum_huey_sqlite_db():
    """Periodically preforms a SQLITE vacuum on the background task database."""
    if os.path.exists(HUEY_FILENAME):
        with sqlite3.connect(HUEY_FILENAME) as cursor:
            cursor.execute("VACUUM")


@db_periodic_task(crontab(minute="0", hour="0", strict=True))
def vacuum_conreq_sqlite_db():
    """Periodically performs any cleanup tasks needed for the default database."""
    if DB_ENGINE == "SQLITE3":
        with connection.cursor() as cursor:
            cursor.execute("VACUUM")
