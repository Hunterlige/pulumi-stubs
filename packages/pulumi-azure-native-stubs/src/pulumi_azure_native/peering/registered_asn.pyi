

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RegisteredAsnArgs', 'RegisteredAsn']
@pulumi.input_type
class RegisteredAsnArgs:
    def __init__(__self__, *, peering_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], asn: Optional[pulumi.Input[_builtins.int]] = ..., registered_asn_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringName")
    def peering_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @peering_name.setter
    def peering_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def asn(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @asn.setter
    def asn(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registeredAsnName")
    def registered_asn_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @registered_asn_name.setter
    def registered_asn_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:peering:RegisteredAsn")
class RegisteredAsn(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., asn: Optional[pulumi.Input[_builtins.int]] = ..., peering_name: Optional[pulumi.Input[_builtins.str]] = ..., registered_asn_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RegisteredAsnArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> RegisteredAsn:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def asn(self) -> pulumi.Output[Optional[_builtins.int]]:
        
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
    @pulumi.getter(name="peeringServicePrefixKey")
    def peering_service_prefix_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


