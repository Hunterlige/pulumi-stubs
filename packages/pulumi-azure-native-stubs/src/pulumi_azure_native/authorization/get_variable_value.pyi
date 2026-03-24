

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVariableValueResult', 'AwaitableGetVariableValueResult', 'get_variable_value', 'get_variable_value_output']
@pulumi.output_type
class GetVariableValueResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., system_data=..., type=..., values=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[outputs.PolicyVariableValueColumnValueResponse]:
        
        ...
    


class AwaitableGetVariableValueResult(GetVariableValueResult):
    def __await__(self): # -> Generator[Never, Any, GetVariableValueResult]:
        ...
    


def get_variable_value(variable_name: Optional[_builtins.str] = ..., variable_value_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVariableValueResult:
    
    ...

def get_variable_value_output(variable_name: Optional[pulumi.Input[_builtins.str]] = ..., variable_value_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVariableValueResult]:
    
    ...

