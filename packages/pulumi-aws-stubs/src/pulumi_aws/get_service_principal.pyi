

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServicePrincipalResult', 'AwaitableGetServicePrincipalResult', 'get_service_principal', 'get_service_principal_output']
@pulumi.output_type
class GetServicePrincipalResult:
    
    def __init__(__self__, id=..., name=..., region=..., service_name=..., suffix=...) -> None:
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
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> _builtins.str:
        
        ...
    


class AwaitableGetServicePrincipalResult(GetServicePrincipalResult):
    def __await__(self): # -> Generator[Never, Any, GetServicePrincipalResult]:
        ...
    


def get_service_principal(region: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServicePrincipalResult:
    
    ...

def get_service_principal_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServicePrincipalResult]:
    
    ...

