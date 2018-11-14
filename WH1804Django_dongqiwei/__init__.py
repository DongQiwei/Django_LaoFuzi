import pymysql
from WH1804Django_dongqiwei.celery import app as celery_app

pymysql.install_as_MySQLdb()

__all__ = ['celery_app']
