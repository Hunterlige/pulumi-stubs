

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBlueprintResult', 'AwaitableGetBlueprintResult', 'get_blueprint', 'get_blueprint_output']
@pulumi.output_type
class GetBlueprintResult:
    
    def __init__(__self__, azure_api_version=..., description=..., display_name=..., id=..., layout=..., name=..., parameters=..., resource_groups=..., status=..., target_scope=..., type=..., versions=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def layout(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, outputs.ParameterDefinitionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(self) -> Optional[Mapping[str, outputs.ResourceGroupDefinitionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.BlueprintStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetScope")
    def target_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Optional[Any]:
        
        ...
    


class AwaitableGetBlueprintResult(GetBlueprintResult):
    def __await__(self): # -> Generator[Never, Any, GetBlueprintResult]:
        ...
    


def get_blueprint(blueprint_name: Optional[_builtins.str] = ..., resource_scope: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBlueprintResult:
    
    ...

def get_blueprint_output(blueprint_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_scope: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBlueprintResult]:
    
    ...

