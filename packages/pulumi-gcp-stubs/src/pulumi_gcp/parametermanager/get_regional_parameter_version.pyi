

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRegionalParameterVersionResult', 'AwaitableGetRegionalParameterVersionResult', 'get_regional_parameter_version', 'get_regional_parameter_version_output']
@pulumi.output_type
class GetRegionalParameterVersionResult:
    
    def __init__(__self__, create_time=..., disabled=..., id=..., kms_key_version=..., location=..., name=..., parameter=..., parameter_data=..., parameter_version_id=..., project=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
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
    @pulumi.getter(name="kmsKeyVersion")
    def kms_key_version(self) -> _builtins.str:
        
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
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


class AwaitableGetRegionalParameterVersionResult(GetRegionalParameterVersionResult):
    def __await__(self): # -> Generator[Never, Any, GetRegionalParameterVersionResult]:
        ...
    


def get_regional_parameter_version(location: Optional[_builtins.str] = ..., parameter: Optional[_builtins.str] = ..., parameter_version_id: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRegionalParameterVersionResult:
    
    ...

def get_regional_parameter_version_output(location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., parameter: Optional[pulumi.Input[_builtins.str]] = ..., parameter_version_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRegionalParameterVersionResult]:
    
    ...

