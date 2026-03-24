

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ThroughputPoolAccountArgs', 'ThroughputPoolAccount']
@pulumi.input_type
class ThroughputPoolAccountArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], throughput_pool_name: pulumi.Input[_builtins.str], account_location: Optional[pulumi.Input[_builtins.str]] = ..., account_resource_identifier: Optional[pulumi.Input[_builtins.str]] = ..., throughput_pool_account_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputPoolName")
    def throughput_pool_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @throughput_pool_name.setter
    def throughput_pool_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountLocation")
    def account_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_location.setter
    def account_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountResourceIdentifier")
    def account_resource_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_resource_identifier.setter
    def account_resource_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputPoolAccountName")
    def throughput_pool_account_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @throughput_pool_account_name.setter
    def throughput_pool_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:cosmosdb:ThroughputPoolAccount")
class ThroughputPoolAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_location: Optional[pulumi.Input[_builtins.str]] = ..., account_resource_identifier: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., throughput_pool_account_name: Optional[pulumi.Input[_builtins.str]] = ..., throughput_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ThroughputPoolAccountArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ThroughputPoolAccount:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountInstanceId")
    def account_instance_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountLocation")
    def account_location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountResourceIdentifier")
    def account_resource_identifier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


