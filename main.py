import tornado.ioloop
import tornado.web
from dbservices.initconnDB import *
from handlers.base_handler import *
from settings import *

def make_app():
    POOL = init_mysqldb_conn()
    return tornado.web.Application([
            (r"/", MainHandler, dict(db=POOL)),
            ],**settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8889)
    tornado.ioloop.IOLoop.current().start()

