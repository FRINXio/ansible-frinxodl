#!/usr/bin/python

DOCUMENTATION = '''
---
module: mountCiscoDevice

short_description: Ansible module to mount cisco device

version_added: "1.0"


author:
    - Frinx.io
'''

EXAMPLES = '''
# Mount Test
- name: Test
  mountCiscoDevice:
    odl_ip: <default> localhost: 8181 </>
    network-topology:node-id: IOS1
    cli-topology:host: 192.168.1.230
    cli-topology:port: 22
    cli-topology:transport-type: ssh
    cli-topology:device-type: ios
    cli-topology:device-version: all
    cli-topology:username: ****
    cli-topology:password: ****
    cli-topology:journal-size: 150
    cli-topology:dry-run-journal-size: 180
    cli-topology:keepalive-delay: 45
    cli-topology:keepalive-timeout: 45
    authorization: ****
'''

RETURN = '''
message:
    description:localhost   ok=2   changed=1
'''

from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
import json


def main():
    arguments = {
        "odl_ip": {"default": "localhost: 8181", "type": "str"},
        "network-topology:node-id": {"required": True, "type": "str"},
        "cli-topology:host": {"required": True, "type": "str"},
        "cli-topology:port": {"required": True, "type": "str"},
        "cli-topology:transport-type": {"requiured": True, "type": "str"},
        "cli-topology:device-type": {"required": True, "type": "str"},
        "cli-topology:device-version": {"required": True, "type": "str"},
        "cli-topology:username": {"required": True, "type": "str"},
        "cli-topology:password": {"required": True, "type": "str"},
        "cli-topology:journal-size": {"required": True, "type": "str"},
        "cli-topology:keepalive-delay": {"required": True, "type": "str"},
        "cli-topology:dry-run-journal-size": {"required": True, "type": "str"},
        "cli-topology:keepalive-timeout": {"required": True, "type": "str"},
        "authorization": {"required": True, "type": "str"}
    }

    module = AnsibleModule(argument_spec=arguments)
    response = dict(
        changed=False,
        original_message=arguments,
        result=''
    )
    mount(module, response)

def mount(module, response):
    open_url('http://' + module.params["odl_ip"] + '/restconf/config/network-topology:network-topology/topology/cli/node/' +
             module.params["network-topology:node-id"], method="PUT", data=json.dumps({
        "network-topology:node":
        {
          "network-topology:node-id": module.params["network-topology:node-id"],

          "cli-topology:host": module.params["cli-topology:host"],
          "cli-topology:port": module.params["cli-topology:port"],
          "cli-topology:transport-type": module.params["cli-topology:transport-type"],

          "cli-topology:device-type": module.params["cli-topology:device-type"],
          "cli-topology:device-version": module.params["cli-topology:device-version"],

          "cli-topology:username": module.params["cli-topology:username"],
          "cli-topology:password": module.params["cli-topology:password"],

          "cli-topology:journal-size": module.params["cli-topology:journal-size"],
          "cli-topology:dry-run-journal-size": module.params["cli-topology:dry-run-journal-size"],

          "cli-topology:keepalive-delay": module.params["cli-topology:keepalive-delay"],
          "cli-topology:keepalive-timeout": module.params["cli-topology:keepalive-timeout"]
        }
      }), force_basic_auth=True, validate_certs=False, headers={'Authorization': module.params["authorization"], 'Accept': 'application/json', 'Content-Type': 'application/json'})

    try:
        open_url('http://' + module.params["odl_ip"] + '/restconf/config/network-topology:network-topology/topology/cli/node/' +
                         module.params["network-topology:node-id"], method="GET",
                force_basic_auth=True,validate_certs=False,headers={'Authorization': module.params["authorization"], 'Accept': 'application/json',
                                                                    'Content-Type': 'application/json'})
    except:
        response['changed'] = False
        response['result'] = "Device not mounted"

    response['changed'] = True
    response['result'] = "device mounted"

    module.exit_json(**response)


if __name__ == '__main__':
    main()