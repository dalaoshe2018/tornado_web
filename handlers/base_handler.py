import tornado.web
import json
from tornado import gen

from utils.utils import *

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db = db


class MainHandler(BaseHandler):
    @gen.coroutine 
    def post(self):
        pass
    def get(self):
        with open("images/0a3bc19bb2410df8979c806c4d75d470.jpg", "rb") as f:
            pic = f.read()
            self.write(pic)
            self.set_header("Content-type", "image/png")


class LoginHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        pass
        #callback=self.on_response)
    
    @tornado.web.asynchronous
    def on_response(self, response):
        if response.error: raise tornado.web.HTTPError(500)
        jsons = tornado.escape.json_decode(response.body)
        self.write("Fetched" +
                str(len(jsons["entries"]))
                + " entries "
                "from the FriendFeed API")
        self.finish()

class ThirdPartHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch("http://friendfeed-api.com/v2/feed/bret",
        callback=self.on_response)
    
    def on_response(self, response):
        if response.error: raise tornado.web.HTTPError(500)
        jsons = tornado.escape.json_decode(response.body)
        self.write("Fetched" +
                str(len(jsons["entries"]))
                + " entries "
                "from the FriendFeed API")
        self.finish()


