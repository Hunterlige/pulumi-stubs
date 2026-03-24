

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetResourceGuardProxyResult', 'AwaitableGetResourceGuardProxyResult', 'get_resource_guard_proxy', 'get_resource_guard_proxy_output']
@pulumi.output_type
class GetResourceGuardProxyResult:
    def __init__(__self__, azure_api_version=..., e_tag=..., id=..., location=..., name=..., properties=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.ResourceGuardProxyBaseResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetResourceGuardProxyResult(GetResourceGuardProxyResult):
    def __await__(self): # -> Generator[Never, Any, GetResourceGuardProxyResult]:
        ...
    


def get_resource_guard_proxy(resource_group_name: Optional[_builtins.str] = ..., resource_guard_proxy_name: Optional[_builtins.str] = ..., vault_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetResourceGuardProxyResult:
    
    ...

def get_resource_guard_proxy_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_guard_proxy_name: Optional[pulumi.Input[_builtins.str]] = ..., vault_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetResourceGuardProxyResult]:
    
    ...

