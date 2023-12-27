import os
# from azure.identity import DefaultAzureCredential
# from azure.identity import ClientSecretCredential
from azure.identity import DefaultAzureCredential, ClientSecretCredential

from azure.mgmt.resource import ResourceManagementClient

def terminate_rg(rg_name):

    rg_name = rg_name
    # credential = DefaultAzureCredential()
    # subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
    tenantid = os.environ['ARM_TENANT_ID']
    clientid = os.environ['ARM_CLIENT_ID']
    clientsecret = os.environ['ARM_CLIENT_SECRET']
    subscriptionid = os.environ['ARM_SUBSCRIPTION_ID']
    credentials = ClientSecretCredential(tenant_id=tenantid, client_id=clientid, client_secret=clientsecret)

    resource_client = ResourceManagementClient(credential=credentials, subscription_id=subscriptionid)

    for item in resource_client.resource_groups.list():
        print(item)
        if item.name == rg_name:
            delete_async_operation = resource_client.resource_groups.begin_delete(rg_name)
            delete_async_operation.wait()
