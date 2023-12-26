'''
https://docs.microsoft.com/azure/developer/python/azure-sdk-overview#inline-json-pattern-for-object-arguments.
'''

from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient

subscription_id = ''
tenant_id = ''
client_id = ''
client_secret = ''

credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
rm_client = ResourceManagementClient(credential, subscription_id)
rg_result = rm_client.resource_groups.create_or_update(
    "myrg",
    {
        "location": "centralus"
    }
)

print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")

