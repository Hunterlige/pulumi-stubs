

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SignalRSharedPrivateLinkResourceArgs', 'SignalRSharedPrivateLinkResource']
@pulumi.input_type
class SignalRSharedPrivateLinkResourceArgs:
    def __init__(__self__, *, group_id: pulumi.Input[_builtins.str], private_link_resource_id: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], resource_name: pulumi.Input[_builtins.str], request_message: Optional[pulumi.Input[_builtins.str]] = ..., shared_private_link_resource_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @group_id.setter
    def group_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @private_link_resource_id.setter
    def private_link_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_message.setter
    def request_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedPrivateLinkResourceName")
    def shared_private_link_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @shared_private_link_resource_name.setter
    def shared_private_link_resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class SignalRSharedPrivateLinkResource(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., group_id: Optional[pulumi.Input[_builtins.str]] = ..., private_link_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., request_message: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name_: Optional[pulumi.Input[_builtins.str]] = ..., shared_private_link_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SignalRSharedPrivateLinkResourceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> SignalRSharedPrivateLinkResource:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


