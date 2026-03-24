

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRegionalParameterVersionRenderResult', 'AwaitableGetRegionalParameterVersionRenderResult', 'get_regional_parameter_version_render', 'get_regional_parameter_version_render_output']
@pulumi.output_type
class GetRegionalParameterVersionRenderResult:
    
    def __init__(__self__, disabled=..., id=..., location=..., name=..., parameter=..., parameter_data=..., parameter_version_id=..., project=..., rendered_parameter_data=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool:
        
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
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterData")
    def parameter_data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterVersionId")
    def parameter_version_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="renderedParameterData")
    def rendered_parameter_data(self) -> _builtins.str:
        
        ...
    


class AwaitableGetRegionalParameterVersionRenderResult(GetRegionalParameterVersionRenderResult):
    def __await__(self): # -> Generator[Never, Any, GetRegionalParameterVersionRenderResult]:
        ...
    


def get_regional_parameter_version_render(location: Optional[_builtins.str] = ..., parameter: Optional[_builtins.str] = ..., parameter_version_id: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRegionalParameterVersionRenderResult:
    
    ...

def get_regional_parameter_version_render_output(location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., parameter: Optional[pulumi.Input[_builtins.str]] = ..., parameter_version_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRegionalParameterVersionRenderResult]:
    
    ...

