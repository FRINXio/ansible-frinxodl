#Ansible modules

Ansible modules to mount and create subInterface in IOS classic devices.

Network module is connecting to Frinx distribution of OpenDaylight which interacts with cisco devices

### Prerequisites


```
Ansible
Python
```

### Installing
```
Install Python from:
https://www.python.org/

Install ansible from:
http://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html?#basics-what-will-be-installed
```
Get the Ansible module code from Github
clone the repository from here into your folder:
```
https://github.com/FRINXio/ansible-frinxodl.git
```


### How to mount IOS classic device
Your *.yml file should have this paramters:
```
&#8211&#8211&#8211
- name: **You can name it whatever you want**
  hosts: localhost
  tasks:
  - name: **You can name it whatever you want**
    mountCiscoDevice:
      odl_ip: <default> localhost: 8181 </>
      network-topology:node-id:
      cli-topology:host:
      cli-topology:port:
      cli-topology:transport-type:
      cli-topology:device-type:
      cli-topology:device-version:
      cli-topology:username:
      cli-topology:password:
      cli-topology:journal-size:
      cli-topology:dry-run-journal-size:
      cli-topology:keepalive-delay:
      cli-topology:keepalive-timeout:
      authorization:
```

Fill the details after colon ':'
Then run your file with:
```
ansible-playbook yourFile.yml
```

### How to create subInterface

Your *.yml file should have this parameters:

```
&#8211&#8211&#8211
- name: **You can name it whatever you want**
  hosts: localhost
  tasks:
  - name: **You can name it whatever you want**
    createSubInt:
      node_id:
      odl_ip: <default> localhost: 8181 </>
      eth_url_intf_id:
      subinterfIndex: <default> 0 </>
      eth_ifc_ip:
      eth_ifc_pref_length:
      authorization:
```
Fill the details after colon ':'
Then run your file with:
```
ansible-playbook yourfile.yml
```