

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSharedLimitResult', 'AwaitableGetSharedLimitResult', 'get_shared_limit', 'get_shared_limit_output']
@pulumi.output_type
class GetSharedLimitResult:
    
    def __init__(__self__, azure_api_version=..., id=..., limit=..., name=..., provisioning_state=..., resource_name=..., system_data=..., type=..., unit=...) -> None:
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
    @pulumi.getter
    def limit(self) -> _builtins.int:
        
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
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> outputs.LimitNameResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSharedLimitResult(GetSharedLimitResult):
    def __await__(self): # -> Generator[Never, Any, GetSharedLimitResult]:
        ...
    


def get_shared_limit(location: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSharedLimitResult:
    
    ...

def get_shared_limit_output(location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSharedLimitResult]:
    
    ...

