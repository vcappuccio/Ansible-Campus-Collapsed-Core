Team,

This email is an opportunity to recap the objectives and deliverables from this week's SWAT session. The intention of this email is to delivery a high-level summary of objectives and challenges we faced:

## Objectives

### ARP DDoS monitoring
  - *Challenge*: Needed a method to baseline ARP denial-of-service violations across our Spring and Dallas data centers
  - *Solution*: Ansible playbook that retrieves these counters every hour, storing the data into a persistant database for on-demand download access

### Update denial-of-service thresholds
  - *Challenge*: Configuration changes were required to standarize on a higher threshold for ARP denial-of-services attacks
  - *Solution*: Ansible playbook apply these changes on appropriate devices throughout the environment

### Identify issues with timeout values
  - *Challenge*: It was known that ARP and MAC address timers were inconsistent, but we needed a method to identify where in order to remidiate.
  - *Solution*: Ansible playbook to retrieve and bring awareness around devices with settings that did not align with the standard practices

### Automate the documentation of VXLAN tunnels
  - *Challenge*: VXLAN EVPN tunnels have been enabled in different capacities across Dallas and Spring data centers, no documentation of these tunnels exists today
  - *Solution*: Ansible playbook was developed with a custom-built Python module to extrapolate the data necessary to automate the documentation process

### VXLAN tunnel useage monitoring
  - *Challenge*: No method for monitoring VXLAN tunnels exists today, ExxonMobil does not have the insight to know if a tunnel is still in use.
  - *Solution*: Ansible playbook to collect this data on cadence and perform the necessary logic to determine a tunnel's level of inactivity.

### Bridge-to-Nowhere detection
  - *Challenge*: The data center team cannot identify VXLAN tunnels that have not learned any other neighbors on the remote end of the tunnel
  - *Solution*: Ansible playbook to retrieve tables from the device and automate the documentation of a tunnel's usage

## Solution stack:
  - Ansible AWX: Web UI for Ansible
  - Gitlab: Source code repository to stage our projects executed by Ansible AWX
  - Python: custom Ansible module was built to perform complex logic with data received from the network
  - Flask: python web framework, used to stand up a REST API to interact with the database
  - Postgres: database used for persistent storage of DDoS monitoring solution
