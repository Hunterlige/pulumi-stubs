

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPublishedBlueprintResult', 'AwaitableGetPublishedBlueprintResult', 'get_published_blueprint', 'get_published_blueprint_output']
@pulumi.output_type
class GetPublishedBlueprintResult:
    
    def __init__(__self__, azure_api_version=..., blueprint_name=..., change_notes=..., description=..., display_name=..., id=..., name=..., parameters=..., resource_groups=..., status=..., target_scope=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blueprintName")
    def blueprint_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="changeNotes")
    def change_notes(self) -> Optional[_builtins.str]:
        
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
    def target_scope(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetPublishedBlueprintResult(GetPublishedBlueprintResult):
    def __await__(self): # -> Generator[Never, Any, GetPublishedBlueprintResult]:
        ...
    


def get_published_blueprint(blueprint_name: Optional[_builtins.str] = ..., resource_scope: Optional[_builtins.str] = ..., version_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPublishedBlueprintResult:
    
    ...

def get_published_blueprint_output(blueprint_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_scope: Optional[pulumi.Input[_builtins.str]] = ..., version_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPublishedBlueprintResult]:
    
    ...

