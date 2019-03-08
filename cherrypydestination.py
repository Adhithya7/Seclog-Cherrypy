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
class cind_backup(object):
    def GET(self):
        listex = []
        f = open('/seclog/log/cinder/backup.log','r')
        for line in f:
            listex.append(line)
        return listex

@cherrypy.expose
class cind_api(object):
    def GET(self):
        listex = []
        f = open('/seclog/log/cinder/api.log','r')
        for line in f:
            listex.append(line)
        return listex

@cherrypy.expose
class cind_scheduler(object):
    def GET(self):
        listex = []
        f = open('/seclog/log/cinder/scheduler.log','r')
        for line in f:
            listex.append(line)
        return listex

@cherrypy.expose
class cind_volume(object):
    def GET(self):
        listex = []
        f = open('/seclog/log/cinder/volume.log','r')
        for line in f:
            listex.append(line)
        return listex

log = ['cind_backup','cind_api','cind_scheduler','cind_volume','glan_api','glan_registry','keystone','nova_api','nova_manage','nova_novncproxy','nova_api-os-compute','nova_placement-api','nova_xvpvncproxy','nova_consoleauth','nova_console','nova_scheduler','nova_conductor','neu_dhcp','neu_metering','neu_server','neu_l3','neu_openvswitch','neu_metadata','neu_ovs-cleanup']

for w in log:
	cherrypy.tree.mount(cinder(), '/'+w,
	    {'/':
	         {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
	    }
	)

cherrypy.engine.start()
