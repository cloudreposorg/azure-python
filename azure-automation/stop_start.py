from azure.identity import DefaultAzureCredential, ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
# from azure.mgmt.resource import ResourceManagementClient
import os

class AzureStopStart():
    def __init__(self, reg_name):
        self.rg_name = reg_name
        self.tenantid = os.environ['ARM_TENANT_ID']
        self.clientid = os.environ['ARM_CLIENT_ID']
        self.clientsecret = os.environ['ARM_CLIENT_SECRET']
        self.subscriptionid = os.environ['ARM_SUBSCRIPTION_ID']
        self.credentials = ClientSecretCredential(tenant_id=self.tenantid, client_id=self.clientid, client_secret=self.clientsecret)
        self.compute_client = ComputeManagementClient(credential=self.credentials, subscription_id=self.subscriptionid)

    # def stop_vm(self, vm_name):
    #     get_cluster_vms()
    #     if vm_state.lower() == 'running':
    #         async_vm_stop = self.compute_client.virtual_machines.begin_deallocate(self.rg_name, vm_name)
    #         async_vm_stop.wait()

    def stop_cluster_vms(self):
        vm_list = self.compute_client.virtual_machines.list(self.rg_name)
        for vm in vm_list:
            vm_name = vm.name
            vm_state = self.get_vm_state(vm_name)
            if vm_state.lower() == 'running':
                print(vm_name)
                async_vm_stop = self.compute_client.virtual_machines.begin_deallocate(self.rg_name, vm_name)
                async_vm_stop.wait()
    def start_cluster_vms(self):
        vm_list = self.compute_client.virtual_machines.list(self.rg_name)
        for vm in vm_list:
            vm_name = vm.name
            vm_state = self.get_vm_state(vm_name)
            if vm_state.lower() != 'running':
                print(vm_name)
                async_vm_start = self.compute_client.virtual_machines.begin_start(self.rg_name, vm_name)
                async_vm_start.wait()

    def get_vm_state(self, vm_name):
        statuses = self.compute_client.virtual_machines.get(self.rg_name, vm_name, expand='instanceView').instance_view.statuses
        status = len(statuses) >=2 and statuses[1]
        # print(status.display_status.split(' ')[-1])
        return status.display_status.split(' ')[-1]

# a = StopStart()
# a.stop_cluster_vms()
# a.start_cluster_vms()