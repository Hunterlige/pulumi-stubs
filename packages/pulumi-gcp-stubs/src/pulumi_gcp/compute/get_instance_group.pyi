

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetInstanceGroupResult', 'AwaitableGetInstanceGroupResult', 'get_instance_group', 'get_instance_group_output']
@pulumi.output_type
class GetInstanceGroupResult:
    
    def __init__(__self__, description=..., id=..., instances=..., name=..., named_ports=..., network=..., project=..., self_link=..., size=..., zone=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namedPorts")
    def named_ports(self) -> Sequence[outputs.GetInstanceGroupNamedPortResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        ...
    


class AwaitableGetInstanceGroupResult(GetInstanceGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetInstanceGroupResult]:
        ...
    


def get_instance_group(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., self_link: Optional[_builtins.str] = ..., zone: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInstanceGroupResult:
    
    ...

def get_instance_group_output(name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., self_link: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInstanceGroupResult]:
    
    ...

