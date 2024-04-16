from werkzeug.wrappers import Request, Response, ResponseStream

class middleware():
    def __init__(self, app):
        self.app = app
        self.userName = 'change'
        self.password = 'change'

    def __call__(self, environ, start_response):
        request = Request(environ)
        userName = request.authorization['username']
        password = request.authorization['password']

        if userName == self.userName and password == self.password:
            environ['user'] = {'': ''}
            return self.app(environ, start_response)

        res = Response(u'Authorization failed', mimetype= 'text/plain', status = 401)
        return res(environ, start_response)