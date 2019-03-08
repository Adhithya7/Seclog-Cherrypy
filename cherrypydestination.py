import cherrypy
import random
import string

cherrypy.config.update({
    'server.socket_host':'192.168.1.23',#Edit Ip address
    'server.socket_port':8000,
    'server.ssl_module':'builtin',
    'server.ssl_certificate':'/home/osm/VNFServer.pem',
    'server.ssl_private_key':'/home/osm/VNFServer.key',
    'server.ssl_certificate_chain':'/home/osm/logcertchain.pem'
    })

@cherrypy.expose
class service(object):
    def GET(self,sv,ln):
        listex = []
        path = '/seclog/log/'+sv+'/'+ln
        f = open(path,'r')
        for line in f:
            listex.append(line)
        return listex

cherrypy.tree.mount(service(), '/service',
    {'/':
         {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    }
)

cherrypy.engine.start()
