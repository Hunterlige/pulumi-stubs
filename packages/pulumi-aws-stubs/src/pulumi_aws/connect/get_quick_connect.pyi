

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetQuickConnectResult', 'AwaitableGetQuickConnectResult', 'get_quick_connect', 'get_quick_connect_output']
@pulumi.output_type
class GetQuickConnectResult:
    
    def __init__(__self__, arn=..., description=..., id=..., instance_id=..., name=..., quick_connect_configs=..., quick_connect_id=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
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
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="quickConnectConfigs")
    def quick_connect_configs(self) -> Sequence[outputs.GetQuickConnectQuickConnectConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quickConnectId")
    def quick_connect_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetQuickConnectResult(GetQuickConnectResult):
    def __await__(self): # -> Generator[Never, Any, GetQuickConnectResult]:
        ...
    


def get_quick_connect(instance_id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., quick_connect_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetQuickConnectResult:
    
    ...

def get_quick_connect_output(instance_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., quick_connect_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetQuickConnectResult]:
    
    ...

