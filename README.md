Project Title
--------------
Cloud Stones Manager

# Pre-Requisites
* Step 3: Authentication to Azure
```
Service principal creation=>Azure active directory => App registrations => New registration -> Name : mysp(any name we can give) -> Register -> Certificates & secrets -> Client secrets -> New client secret -> Add -> copy client secret value
```
```
Assiging Permission for the above service princiap mysp to create resources in Azure => Subscription => IAM => Add -> add role assignment -> Role => Privileged administrator roles=> contributor -> members -> select members => select: <<mysp>> => click on Review + assign
```
```
export ARM_TENANT_ID="" && export ARM_SUBSCRIPTION_ID="" && export ARM_CLIENT_ID="" && export ARM_CLIENT_SECRET=""
```
# Execution Flow
* Step 1: Clone repo
```
git clone https://github.com/cloudreposorg/azure-python.git && cd azure-python.git
```
* Step 2: Install dependencies
```
pip3 install -r requirements.txt
```
* Step 3: Run actions
```
python3 entrypoint.py -cp cluster-profiles/azure_dev_cluster.json  stop
python3 entrypoint.py -cp cluster-profiles/azure_dev_cluster.json  start 
python3 entrypoint.py -cp cluster-profiles/azure_dev_cluster.json  deprovision
python3 entrypoint.py -cp cluster-profiles/azure_dev_cluster.json  sp_rotation
```
# Features
```
Delete Resource group - Done
Stop and Start virtual machines - Done
Serive principle rotation - In Progress
Service Quota increase - TODO
Price calculation -TODO
Customer managed encryption key(CMEK) for disks - TODO
Private Link set up - TODO
Express Route set up - TODO
```
