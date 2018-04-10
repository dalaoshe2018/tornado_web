from tornado_mysql import pools
from settings import settings

def init_mysqldb_conn():
    pools.DEBUG = True
    return pools.Pool(
        settings['mysql_config'],
        settings['mysql_max_idle_connections'],
        settings['mysql_max_recycle_sec'],
        )
