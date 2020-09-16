# Updates an exsiting NSG with one or more rules
# Please see this script's README.md on how to populate the rules dictionary

import os
import traceback

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.network.models import NetworkSecurityGroup

# Split the below two imports to cut down on column length
from azure.mgmt.network.models import SecurityRule, SecurityRuleAccess 
from azure.mgmt.network.models import SecurityRuleDirection, SecurityRuleProtocol

from msrestazure.azure_exceptions import CloudError

# Supply the resource group name and the name of the Network Security Group below
GROUP_NAME = ""
NSG_NAME = ""

# You will want to supply the values in this function as environment variables
def get_credentials():
    subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_CLIENT_SECRET'],
        tenant=os.environ['AZURE_TENANT_ID']
    )
    return credentials, subscription_id

credentials, subscription_id = get_credentials()
network_client = NetworkManagementClient(credentials, subscription_id)

def add_nsg_rule(rules):
    try:
        for k, v in rules.items():
            print(f"\nAdd security rule '{k}' to {NSG_NAME}")
            security_rule = network_client.security_rules.create_or_update(GROUP_NAME, NSG_NAME, k, v)
            sec_rule_info = security_rule.result()
    except CloudError:
        print('Could not update the NSG:\n{}'.format(traceback.format_exc()))
    else:
        print(f"NSG {NSG_NAME} Updated Successfully!")

if __name__ == "__main__":
    rules = {}
    add_nsg_rule(rules)
