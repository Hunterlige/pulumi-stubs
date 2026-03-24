

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebPubSubSharedPrivateLinkResourceResult', ..., 'get_web_pub_sub_shared_private_link_resource', ...]
@pulumi.output_type
class GetWebPubSubSharedPrivateLinkResourceResult:
    
    def __init__(__self__, azure_api_version=..., group_id=..., id=..., name=..., private_link_resource_id=..., provisioning_state=..., request_message=..., status=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWebPubSubSharedPrivateLinkResourceResult(GetWebPubSubSharedPrivateLinkResourceResult):
    def __await__(self): # -> Generator[Never, Any, GetWebPubSubSharedPrivateLinkResourceResult]:
        ...
    


def get_web_pub_sub_shared_private_link_resource(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., shared_private_link_resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebPubSubSharedPrivateLinkResourceResult:
    
    ...

def get_web_pub_sub_shared_private_link_resource_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., shared_private_link_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebPubSubSharedPrivateLinkResourceResult]:
    
    ...

