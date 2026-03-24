

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTemplateSpecResult', 'AwaitableGetTemplateSpecResult', 'get_template_spec', 'get_template_spec_output']
@pulumi.output_type
class GetTemplateSpecResult:
    
    def __init__(__self__, azure_api_version=..., description=..., display_name=..., id=..., location=..., metadata=..., name=..., system_data=..., tags=..., type=..., versions=...) -> None:
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
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Mapping[str, outputs.TemplateSpecVersionInfoResponse]:
        
        ...
    


class AwaitableGetTemplateSpecResult(GetTemplateSpecResult):
    def __await__(self): # -> Generator[Never, Any, GetTemplateSpecResult]:
        ...
    


def get_template_spec(expand: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., template_spec_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTemplateSpecResult:
    
    ...

def get_template_spec_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., template_spec_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTemplateSpecResult]:
    
    ...

