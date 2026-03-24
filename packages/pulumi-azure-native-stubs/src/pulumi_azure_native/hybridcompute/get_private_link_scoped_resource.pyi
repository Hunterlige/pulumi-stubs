

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPrivateLinkScopedResourceResult', 'AwaitableGetPrivateLinkScopedResourceResult', 'get_private_link_scoped_resource', 'get_private_link_scoped_resource_output']
@pulumi.output_type
class GetPrivateLinkScopedResourceResult:
    
    def __init__(__self__, azure_api_version=..., id=..., linked_resource_id=..., name=..., provisioning_state=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedResourceId")
    def linked_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetPrivateLinkScopedResourceResult(GetPrivateLinkScopedResourceResult):
    def __await__(self): # -> Generator[Never, Any, GetPrivateLinkScopedResourceResult]:
        ...
    


def get_private_link_scoped_resource(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., scope_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPrivateLinkScopedResourceResult:
    
    ...

def get_private_link_scoped_resource_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., scope_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPrivateLinkScopedResourceResult]:
    
    ...

