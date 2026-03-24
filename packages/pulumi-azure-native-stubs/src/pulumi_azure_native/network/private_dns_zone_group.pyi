

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PrivateDnsZoneGroupArgs', 'PrivateDnsZoneGroup']
@pulumi.input_type
class PrivateDnsZoneGroupArgs:
    def __init__(__self__, *, private_endpoint_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_zone_configs: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateDnsZoneConfigArgs]]]] = ..., private_dns_zone_group_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointName")
    def private_endpoint_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @private_endpoint_name.setter
    def private_endpoint_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsZoneConfigs")
    def private_dns_zone_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PrivateDnsZoneConfigArgs]]]]:
        
        ...
    
    @private_dns_zone_configs.setter
    def private_dns_zone_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateDnsZoneConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsZoneGroupName")
    def private_dns_zone_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_dns_zone_group_name.setter
    def private_dns_zone_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:PrivateDnsZoneGroup")
class PrivateDnsZoneGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_zone_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PrivateDnsZoneConfigArgs, PrivateDnsZoneConfigArgsDict]]]]] = ..., private_dns_zone_group_name: Optional[pulumi.Input[_builtins.str]] = ..., private_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PrivateDnsZoneGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> PrivateDnsZoneGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsZoneConfigs")
    def private_dns_zone_configs(self) -> pulumi.Output[Optional[Sequence[outputs.PrivateDnsZoneConfigResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


