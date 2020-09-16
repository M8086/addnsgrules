# addnsgrules
Add rules to an existing NSG using the Azure SDK

Rules are supplied to the add_nsg_rules function as a dictionary of dictionaries.

key - Name of rule

value - a dictionary defining the Security rule

Here's an example:

rules = {

    "allow-http-in" : {
    
            'access':SecurityRuleAccess.allow,
            
            'description':'Allow HTTP In',
            
            'destination_address_prefix':'*',
            
            'destination_port_range':'80',
            
            'direction':SecurityRuleDirection.inbound,
            
            'priority':120,
            
            'protocol':SecurityRuleProtocol.tcp,
            
            'source_address_prefix':'*',
            
            'source_port_range':'*',
            
        }
        
}

Be sure to supply the necessary environment varialbes for the get_credentials function

You can see what to do for that here:
https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-authenticate?tabs=cmd#authenticate-with-token-credentials
