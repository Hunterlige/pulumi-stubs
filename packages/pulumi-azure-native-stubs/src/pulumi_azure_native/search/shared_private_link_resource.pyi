

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SharedPrivateLinkResourceArgs', 'SharedPrivateLinkResource']
@pulumi.input_type
class SharedPrivateLinkResourceArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], search_service_name: pulumi.Input[_builtins.str], properties: Optional[pulumi.Input[SharedPrivateLinkResourcePropertiesArgs]] = ..., shared_private_link_resource_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchServiceName")
    def search_service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @search_service_name.setter
    def search_service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[SharedPrivateLinkResourcePropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[SharedPrivateLinkResourcePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedPrivateLinkResourceName")
    def shared_private_link_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @shared_private_link_resource_name.setter
    def shared_private_link_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:search:SharedPrivateLinkResource")
class SharedPrivateLinkResource(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., properties: Optional[pulumi.Input[Union[SharedPrivateLinkResourcePropertiesArgs, SharedPrivateLinkResourcePropertiesArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., search_service_name: Optional[pulumi.Input[_builtins.str]] = ..., shared_private_link_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SharedPrivateLinkResourceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> SharedPrivateLinkResource:
        
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
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.SharedPrivateLinkResourcePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


