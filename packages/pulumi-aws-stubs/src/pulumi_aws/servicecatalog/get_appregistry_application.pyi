

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAppregistryApplicationResult', 'AwaitableGetAppregistryApplicationResult', 'get_appregistry_application', 'get_appregistry_application_output']
@pulumi.output_type
class GetAppregistryApplicationResult:
    
    def __init__(__self__, application_tag=..., arn=..., description=..., id=..., name=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationTag")
    def application_tag(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
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
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetAppregistryApplicationResult(GetAppregistryApplicationResult):
    def __await__(self): # -> Generator[Never, Any, GetAppregistryApplicationResult]:
        ...
    


def get_appregistry_application(id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAppregistryApplicationResult:
    
    ...

def get_appregistry_application_output(id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAppregistryApplicationResult]:
    
    ...

