

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEnvironmentBlueprintResult', 'AwaitableGetEnvironmentBlueprintResult', 'get_environment_blueprint', 'get_environment_blueprint_output']
@pulumi.output_type
class GetEnvironmentBlueprintResult:
    
    def __init__(__self__, blueprint_provider=..., description=..., domain_id=..., id=..., managed=..., name=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blueprintProvider")
    def blueprint_provider(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def managed(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetEnvironmentBlueprintResult(GetEnvironmentBlueprintResult):
    def __await__(self): # -> Generator[Never, Any, GetEnvironmentBlueprintResult]:
        ...
    


def get_environment_blueprint(domain_id: Optional[_builtins.str] = ..., managed: Optional[_builtins.bool] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEnvironmentBlueprintResult:
    
    ...

def get_environment_blueprint_output(domain_id: Optional[pulumi.Input[_builtins.str]] = ..., managed: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEnvironmentBlueprintResult]:
    
    ...

