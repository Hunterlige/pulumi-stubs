

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ServerInstanceArgs', 'ServerInstance']
@pulumi.input_type
class ServerInstanceArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], sap_discovery_site_name: pulumi.Input[_builtins.str], sap_instance_name: pulumi.Input[_builtins.str], server_instance_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sapDiscoverySiteName")
    def sap_discovery_site_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sap_discovery_site_name.setter
    def sap_discovery_site_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sapInstanceName")
    def sap_instance_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sap_instance_name.setter
    def sap_instance_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverInstanceName")
    def server_instance_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_instance_name.setter
    def server_instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:workloads:ServerInstance")
class ServerInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sap_discovery_site_name: Optional[pulumi.Input[_builtins.str]] = ..., sap_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., server_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ServerInstanceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ServerInstance:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationData")
    def configuration_data(self) -> pulumi.Output[outputs.ConfigurationDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> pulumi.Output[outputs.SAPMigrateErrorResponseV2]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSid")
    def instance_sid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceData")
    def performance_data(self) -> pulumi.Output[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sapInstanceType")
    def sap_instance_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sapProduct")
    def sap_product(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sapProductVersion")
    def sap_product_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


