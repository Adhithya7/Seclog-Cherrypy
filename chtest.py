import cherrypy
import random
import string

cherrypy.config.update({
    'server.socket_host':'192.168.1.23',
    'server.socket_port':8000,
    'server.ssl_module':'builtin',
    'server.ssl_certificate':'/home/osm/VNFServer.pem',
    'server.ssl_private_key':'/home/osm/VNFServer.key',
    'server.ssl_certificate_chain':'/home/osm/logcertchain.pem'
    })

@cherrypy.expose
class cind_backup(object):
    def GET(self):
        listex = []
        f = open('/var/log/cinder/backup.log','r')
        for line in f:
            listex.append(line)
        return listex

@cherrypy.expose
class cind_api(object):
    def GET(self):
        listex = []
        f = open('/var/log/cinder/api.log','r')
        for line in f:
            listex.append(line)
        return listex

@cherrypy.expose
class cind_scheduler(object):
    def GET(self):
        listex = []
        f = open('/var/log/cinder/scheduler.log','r')
        for line in f:
            listex.append(line)
        return listex

@cherrypy.expose
class cind_volume(object):
    def GET(self):
        listex = []
        f = open('/var/log/cinder/volume.log','r')
        for line in f:
            listex.append(line)
        return listex

cherrypy.tree.mount(cind_backup(), '/cind_backup',
    {'/':
         {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    }
)
cherrypy.tree.mount(cind_api(), '/cind_api',
    {'/':
         {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    }
)
cherrypy.tree.mount(cind_scheduler(), '/cind_scheduler',
    {'/':
         {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    }
)
cherrypy.tree.mount(cind_volume(), '/cind_volume',
    {'/':
         {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    }
)

cherrypy.engine.start()
