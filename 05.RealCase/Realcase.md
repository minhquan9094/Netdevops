# Real case


- Some realcase on network enterprise using devnet
  
  1.  Inventory network
  2.  Changing hostname --> DONE
  3.  Update IP address
  4.  Backup + Restore config
  5.  Automate Archiving Network Configurations and Device State
  6.  Implement Automated IP Conflict Detection
  7.  Automate IP Routing Validation
  8.  Automate IP Reachability Testing
  9.  Automate OSPF Error Detection
  10. Lookup MAC - ARP - Interface connect to
  11. Pineline deploy

- Tool:
  - Ansible Tower
  - Netbox
  - Workflow
  - Jsoncrack
  - Jenskin


### Project 1: Build Automation schedule to inventory network device to get:
  - Connection: CDP neighbor
  - Router: routing-table
  - Switch: Vlan, spanning tree,

### Project 2: Build Automation to deploy snmp config and create new device on monitor system (zabbix)
  - New device setup
  - Add to monitoring system

### Project 3: Build Automation to add new route on AWS VPC
  - Change request from OSticket or Manage Engine
  - Deploy via AWS CLI or SDK or Lambda

### Project 4: Build workflow dashboard to view pineline on each project

