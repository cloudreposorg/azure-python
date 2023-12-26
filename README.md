Project Title
--------------
Cloud Stones Manager

# Azure Operations
* Step 1: Authentication to Azure
```
export ARM_TENANT_ID="" && export ARM_SUBSCRIPTION_ID="" && export ARM_CLIENT_ID="" && export ARM_CLIENT_SECRET=""
az login
export MSYS_NO_PATHCONV=1
az ad sp create-for-rbac --name <myserviceprincipal> --role Contributor

https://docs.microsoft.com/en-us/azure/developer/python/configure-local-development-environment?tabs=cmd
```
* Step 2: Clone repo and run actions
```
git clone https://github.com/fullstack2025/CSM.git && cd CSM
pip3 install -r requirements.txt
python3 entrypoint.py -cp cluster-profiles/azure_dev_cluster.json  stop
python3 entrypoint.py -cp cluster-profiles/azure_dev_cluster.json  start 
python3 entrypoint.py -cp cluster-profiles/azure_dev_cluster.json  deprovision
python3 entrypoint.py -cp cluster-profiles/azure_dev_cluster.json  sp_rotation
```