

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetParameterVersionResult', 'AwaitableGetParameterVersionResult', 'get_parameter_version', 'get_parameter_version_output']
@pulumi.output_type
class GetParameterVersionResult:
    
    def __init__(__self__, create_time=..., disabled=..., id=..., kms_key_version=..., name=..., parameter=..., parameter_data=..., parameter_version_id=..., project=..., update_time=...) -> None:
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
    


class AwaitableGetParameterVersionResult(GetParameterVersionResult):
    def __await__(self): # -> Generator[Never, Any, GetParameterVersionResult]:
        ...
    


def get_parameter_version(parameter: Optional[_builtins.str] = ..., parameter_version_id: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetParameterVersionResult:
    
    ...

def get_parameter_version_output(parameter: Optional[pulumi.Input[_builtins.str]] = ..., parameter_version_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetParameterVersionResult]:
    
    ...

