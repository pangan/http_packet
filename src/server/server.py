import falcon
import json

from ..common.logger import get_logger

from wsgiref import simple_server

log = get_logger('test.log')

class Resources(object):
    def on_post(self, req, resp):

        try:
            received_data = req.stream.read()
            json.loads(received_data)
            received_size = len(received_data)
            doc = {'received_bytes': received_size}
            #log.debug('received data: {0}'.format(received_data))
            log.debug('received_size: {0}'.format(received_size))
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(doc, ensure_ascii=False)
        except Exception, e:
            log.error(e)

def myapp():
    app = falcon.API()
    resource = Resources()
    app.add_route('/', resource)
    return app


if __name__ == '__main__':

    server_port = 8090
    log.info('server started on port {0}!'.format(server_port))
    wsgi_app = myapp()

    httpd = simple_server.make_server('0.0.0.0', server_port, wsgi_app)
    httpd.serve_forever()