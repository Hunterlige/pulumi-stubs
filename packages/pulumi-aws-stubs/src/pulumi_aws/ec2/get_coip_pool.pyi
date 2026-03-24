

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
__all__ = ['GetCoipPoolResult', 'AwaitableGetCoipPoolResult', 'get_coip_pool', 'get_coip_pool_output']
@pulumi.output_type
class GetCoipPoolResult:
    
    def __init__(__self__, arn=..., filters=..., id=..., local_gateway_route_table_id=..., pool_cidrs=..., pool_id=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetCoipPoolFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localGatewayRouteTableId")
    def local_gateway_route_table_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolCidrs")
    def pool_cidrs(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolId")
    def pool_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetCoipPoolResult(GetCoipPoolResult):
    def __await__(self): # -> Generator[Never, Any, GetCoipPoolResult]:
        ...
    


def get_coip_pool(filters: Optional[Sequence[Union[GetCoipPoolFilterArgs, GetCoipPoolFilterArgsDict]]] = ..., local_gateway_route_table_id: Optional[_builtins.str] = ..., pool_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCoipPoolResult:
    
    ...

def get_coip_pool_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetCoipPoolFilterArgs, GetCoipPoolFilterArgsDict]]]]] = ..., local_gateway_route_table_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., pool_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCoipPoolResult]:
    
    ...

