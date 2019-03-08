import cherrypy
import random
import string
import requests

cherrypy.config.update({
    'server.socket_host':'192.168.1.30',#Edit Ip address
    'server.socket_port':8080,
    'server.ssl_module':'builtin',
    'server.ssl_certificate':'/home/smrelay/InterCA.pem',
    'server.ssl_private_key':'/home/smrelay/InterCA.key',
    })

@cherrypy.expose
class service(object):
    def GET(self,host,sv,log_name):
        s=requests.Session()
        log_name=log_namein
        r = s.get('https://'+host+':8000/service',sv,log_name)
        return r.text

cherrypy.tree.mount(service(), '/service',
    {'/':
         {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    }
)

cherrypy.engine.start()
