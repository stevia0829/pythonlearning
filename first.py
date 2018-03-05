from tornado import web,ioloop,httpserver

class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('welcome to my page!')
        self.render('index.html')

class CreateDiaryMandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        #self.write('welcome to my page!')
        self.render('create.html')

application=web.Application([
    (r"/",MainPageHandler),
    (r"/create",CreateDiaryMandler),
])
if __name__ == '__main__':
 http_server=httpserver.HTTPServer(application)
 http_server.listen(8080)
 ioloop.IOLoop.current( ).start()

