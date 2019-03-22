import cherrypy
import random
import string

cherrypy.config.update({
    'server.socket_host':'192.168.1.23',#Edit Ip address
    'server.socket_port':8000,
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

log = ['cind_backup','cind_api','cind_scheduler','cind_volume']
#'glan_api','glan_registry','keystone','nova_api','nova_manage','nova_novncproxy','nova_api-os-compute','nova_placement-api','nova_xvpvncproxy','nova_consoleauth','nova_console','nova_scheduler','nova_conductor','neu_dhcp','neu_metering','neu_server','neu_l3','neu_openvswitch','neu_metadata','neu_ovs-cleanup'

cherrypy.tree.mount(cind_backup(),'/cind_backup',
    {'/':
	{'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
	}
    )

cherrypy.tree.mount(cind_volume(),'/cind_volume',
    {'/':
	{'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
	}
    )

cherrypy.tree.mount(cind_scheduler(),'/cind_scheduler',
    {'/':
	{'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
	}
    )

cherrypy.tree.mount(cind_api(),'/cind_api',
    {'/':
	{'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
	}
    )

cherrypy.engine.start()
