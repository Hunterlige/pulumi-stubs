

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEnvironmentResult', 'AwaitableGetEnvironmentResult', 'get_environment', 'get_environment_output']
@pulumi.output_type
class GetEnvironmentResult:
    
    def __init__(__self__, application_id=..., arn=..., description=..., environment_id=..., id=..., monitors=..., name=..., region=..., state=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> _builtins.str:
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
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitors(self) -> Sequence[outputs.GetEnvironmentMonitorResult]:
        
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
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetEnvironmentResult(GetEnvironmentResult):
    def __await__(self): # -> Generator[Never, Any, GetEnvironmentResult]:
        ...
    


def get_environment(application_id: Optional[_builtins.str] = ..., environment_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEnvironmentResult:
    
    ...

def get_environment_output(application_id: Optional[pulumi.Input[_builtins.str]] = ..., environment_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEnvironmentResult]:
    
    ...

