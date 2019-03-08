import cherrypy
import random
import string
import requests

cherrypy.config.update({
    'server.socket_host':'192.168.1.30',
    'server.socket_port':8080,
    'server.ssl_module':'builtin',
    'server.ssl_certificate':'/home/smrelay/InterCA.pem',
    'server.ssl_private_key':'/home/smrelay/InterCA.key',
    })

@cherrypy.expose
class cinder(object):
    def GET(self,host_name,log_name):
        s=requests.Session()
        log_name=log_namein
        r = s.get('https://'+host_name+':8000/'+log_name)
        return r.text

log = ['cind_backup','cind_api','cind_scheduler','cind_volume','glan_api','glan_registry','keystone','nova_api','nova_manage','nova_novncproxy','nova_api-os-compute','nova_placement-api','nova_xvpvncproxy','nova_consoleauth','nova_console','nova_scheduler','nova_conductor','neu_dhcp','neu_metering','neu_server','neu_l3','neu_openvswitch','neu_metadata','neu_ovs-cleanup']

for w in log:
	cherrypy.tree.mount(cinder(), '/'+w,
	    {'/':
	         {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
	    }
	)

cherrypy.engine.start()
