

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetInstanceSerialPortResult', 'AwaitableGetInstanceSerialPortResult', 'get_instance_serial_port', 'get_instance_serial_port_output']
@pulumi.output_type
class GetInstanceSerialPortResult:
    
    def __init__(__self__, contents=..., id=..., instance=..., port=..., project=..., zone=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def contents(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        ...
    


class AwaitableGetInstanceSerialPortResult(GetInstanceSerialPortResult):
    def __await__(self): # -> Generator[Never, Any, GetInstanceSerialPortResult]:
        ...
    


def get_instance_serial_port(instance: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ..., project: Optional[_builtins.str] = ..., zone: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInstanceSerialPortResult:
    
    ...

def get_instance_serial_port_output(instance: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInstanceSerialPortResult]:
    
    ...

