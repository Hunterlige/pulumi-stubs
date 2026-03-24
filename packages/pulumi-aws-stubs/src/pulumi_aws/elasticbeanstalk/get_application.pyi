

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetApplicationResult', 'AwaitableGetApplicationResult', 'get_application', 'get_application_output']
@pulumi.output_type
class GetApplicationResult:
    
    def __init__(__self__, appversion_lifecycle=..., arn=..., description=..., id=..., name=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appversionLifecycle")
    def appversion_lifecycle(self) -> outputs.GetApplicationAppversionLifecycleResult:
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
    


class AwaitableGetApplicationResult(GetApplicationResult):
    def __await__(self): # -> Generator[Never, Any, GetApplicationResult]:
        ...
    


def get_application(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetApplicationResult:
    
    ...

def get_application_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetApplicationResult]:
    
    ...

