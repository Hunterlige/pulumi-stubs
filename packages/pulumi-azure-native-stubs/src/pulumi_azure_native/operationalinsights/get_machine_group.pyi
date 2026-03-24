

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMachineGroupResult', 'AwaitableGetMachineGroupResult', 'get_machine_group', 'get_machine_group_output']
@pulumi.output_type
class GetMachineGroupResult:
    
    def __init__(__self__, azure_api_version=..., count=..., display_name=..., etag=..., group_type=..., id=..., kind=..., machines=..., name=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupType")
    def group_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def machines(self) -> Optional[Sequence[outputs.MachineReferenceWithHintsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetMachineGroupResult(GetMachineGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetMachineGroupResult]:
        ...
    


def get_machine_group(end_time: Optional[_builtins.str] = ..., machine_group_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., start_time: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMachineGroupResult:
    
    ...

def get_machine_group_output(end_time: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., machine_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., start_time: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMachineGroupResult]:
    
    ...

