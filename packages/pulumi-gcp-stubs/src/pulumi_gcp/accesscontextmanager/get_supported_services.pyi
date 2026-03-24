

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSupportedServicesResult', 'AwaitableGetSupportedServicesResult', 'get_supported_services', 'get_supported_services_output']
@pulumi.output_type
class GetSupportedServicesResult:
    
    def __init__(__self__, id=..., supported_services=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedServices")
    def supported_services(self) -> Sequence[outputs.GetSupportedServicesSupportedServiceResult]:
        
        ...
    


class AwaitableGetSupportedServicesResult(GetSupportedServicesResult):
    def __await__(self): # -> Generator[Never, Any, GetSupportedServicesResult]:
        ...
    


def get_supported_services(opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSupportedServicesResult:
    
    ...

def get_supported_services_output(opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSupportedServicesResult]:
    
    ...

