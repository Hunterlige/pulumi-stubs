

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLocalGatewayResult', 'AwaitableGetLocalGatewayResult', 'get_local_gateway', 'get_local_gateway_output']
@pulumi.output_type
class GetLocalGatewayResult:
    
    def __init__(__self__, filters=..., id=..., outpost_arn=..., owner_id=..., region=..., state=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetLocalGatewayFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetLocalGatewayResult(GetLocalGatewayResult):
    def __await__(self): # -> Generator[Never, Any, GetLocalGatewayResult]:
        ...
    


def get_local_gateway(filters: Optional[Sequence[Union[GetLocalGatewayFilterArgs, GetLocalGatewayFilterArgsDict]]] = ..., id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLocalGatewayResult:
    
    ...

def get_local_gateway_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetLocalGatewayFilterArgs, GetLocalGatewayFilterArgsDict]]]]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., state: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLocalGatewayResult]:
    
    ...

