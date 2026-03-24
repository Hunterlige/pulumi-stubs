

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetApplicationProvidersResult', 'AwaitableGetApplicationProvidersResult', 'get_application_providers', 'get_application_providers_output']
@pulumi.output_type
class GetApplicationProvidersResult:
    
    def __init__(__self__, application_providers=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationProviders")
    def application_providers(self) -> Sequence[outputs.GetApplicationProvidersApplicationProviderResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetApplicationProvidersResult(GetApplicationProvidersResult):
    def __await__(self): # -> Generator[Never, Any, GetApplicationProvidersResult]:
        ...
    


def get_application_providers(region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetApplicationProvidersResult:
    
    ...

def get_application_providers_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetApplicationProvidersResult]:
    
    ...

