

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetViewResult', 'AwaitableGetViewResult', 'get_view', 'get_view_output']
@pulumi.output_type
class GetViewResult:
    
    def __init__(__self__, azure_api_version=..., changed=..., created=..., definition=..., display_name=..., id=..., name=..., tenant_id=..., type=..., user_id=..., view_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def changed(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def created(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def definition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[Mapping[str, _builtins.str]]:
        
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
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewName")
    def view_name(self) -> _builtins.str:
        
        ...
    


class AwaitableGetViewResult(GetViewResult):
    def __await__(self): # -> Generator[Never, Any, GetViewResult]:
        ...
    


def get_view(hub_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., user_id: Optional[_builtins.str] = ..., view_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetViewResult:
    
    ...

def get_view_output(hub_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., user_id: Optional[pulumi.Input[_builtins.str]] = ..., view_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetViewResult]:
    
    ...

