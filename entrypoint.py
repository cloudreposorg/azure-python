"""
This module is intended to manage resources in Azure cloud platform.
"""
#!/usr/bin/env python3
import sys
import os
import json
import time
import argparse
from azure-automation.stop_start import AzureStopStart
from azure-automation.cleanup import terminate_rg
from azure-automation.service_principle_rotation import SPRotation

VALID_ACTIONS = ["stop", "start", "deprovision"]
parser = argparse.ArgumentParser()
parser.add_argument('action', help="Action %s"%VALID_ACTIONS )
parser.add_argument('-cn', '--cluster_name', help='name of the cluster')
# parser.add_argument('-p', '--cloud_provider', help='name of the cloud provider')
parser.add_argument('-cp', '--cluster_profile', help='name of the cluster profile')
args = parser.parse_args()
action = args.action
cluster_name = args.cluster_name
# cloud_provider= args.cloud_provider
cluster_profile = args.cluster_profile
print(cluster_profile)
time.sleep(5)

with open(cluster_profile, 'r') as cd: cluster_profile = json.loads(cd.read())
print(cluster_profile)

if cluster_profile['cloud_provider'] == 'azure':
    if  action == 'deprovision':
        cluster_name = cluster_profile['cluster_name'] 
        terminate_rg(cluster_name)
    elif action == 'stop':
        cluster_name = cluster_profile['cluster_name'] 
        a = AzureStopStart(cluster_name)
        a.stop_cluster_vms()
    elif action=='start':
        cluster_name = cluster_profile['cluster_name'] 
        a = AzureStopStart(cluster_name)
        a.start_cluster_vms()
    elif action == 'sp_rotation':
        spr = SPRotation()
        spr.check_sp_status('testsp')