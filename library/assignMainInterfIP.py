#!/usr/bin/python

from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
import json

DOCUMENTATION = '''
---
module: create subinterface

short_description: Ansible module to create subinterface

version_added: "1.0"


author:
    - Frinx.io
'''

EXAMPLES = '''
# create subInterface test
- name: create subInterface
    createSubInt:
      node_id: IOS1
      odl_ip: <default> localhost: 8181 </>
      eth_url_intf_id: GigabitEthernet2/0
      eth_ifc_ip: 10.10.10.0
      subinterfIndex: <default> 0 </>
      eth_ifc_pref_length: 24
      authorization: ****
'''

RETURN = '''
message:
    description:localhost   ok=2   changed=1
'''


def main():
    arguments = {
        "node_id": {"required": True, "type": "str"},
        "odl_ip": {"default": "localhost", "type": "str"},
        "odl_ip_port": {"default": "8181", "type": "str"},
        "eth_url_intf_id": {"required": True, "type": "str"},
        "eth_ifc_ip": {"required": True, "type": "str"},
        "subinterfIndex": {"default": 0, "type": "str"},
        "eth_ifc_pref_length": {"required": True, "type": "str"},
        "authorization": {"default": "Basic YWRtaW46YWRtaW4=", "type": "str"}
    }

    module = AnsibleModule(argument_spec=arguments)
    response = dict(
        changed=False,
        result=''
    )
    createsubint(module, response)
    module.exit_json(changed=False, meta=response)


def createsubint(module, response):
    eth_url_intf_id = urllib_request.quote(module.params['eth_url_intf_id'], safe='')
    url = urllib_request.quote(module.params['odl_ip'] + ':' + module.params['odl_ip_port'] +
                        '/restconf/config/network-topology:network-topology/topology/uniconfig/node/' + module.params['node_id'] +
                        '/frinx-uniconfig-topology:configuration/frinx-openconfig-interfaces:interfaces/interface/' + eth_url_intf_id + '/subinterfaces')
    url = 'http://' + url

    try:
        open_url(url, method='PUT', data=json.dumps({
                "subinterfaces": {
                    "subinterface": [
                        {
                            "index": module.params['subinterfIndex'],
                            "config": {
                                "index": module.params['subinterfIndex']
                            },
                            "frinx-openconfig-if-ip:ipv4": {
                                "addresses": {
                                    "address": [
                                        {
                                            "ip": module.params["eth_ifc_ip"],
                                            "config": {
                                                "ip": module.params["eth_ifc_ip"],
                                                "prefix-length": module.params["eth_ifc_pref_length"]
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            }), force_basic_auth=True, validate_certs=False,
                 headers={'Authorization': module.params['authorization'], 'Accept': 'application/json', 'Content-Type': 'application/json'})
    except urllib_request.HTTPError:
        response['msg'] = 'http error'
        response['url'] = url
        module.fail_json(**response)

    try:
        open_url(url, method="GET", force_basic_auth=True, validate_certs=False, headers={'Authorization': module.params['authorization'], 'Accept': 'application/json', 'Content-Type': 'application/json'})
    except:
        response['changed'] = False
        response['result'] = 'Subinterface was not created'
        response['msg'] = 'Not created'
        module.fail_json(**response)

    response['changed'] = True
    response['result'] = 'Subinterface created'
    module.exit_json(**response)


if __name__ == '__main__':
    main()