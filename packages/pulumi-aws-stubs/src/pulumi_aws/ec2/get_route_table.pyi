

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
__all__ = ['GetRouteTableResult', 'AwaitableGetRouteTableResult', 'get_route_table', 'get_route_table_output']
@pulumi.output_type
class GetRouteTableResult:
    
    def __init__(__self__, arn=..., associations=..., filters=..., gateway_id=..., id=..., owner_id=..., region=..., route_table_id=..., routes=..., subnet_id=..., tags=..., vpc_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def associations(self) -> Sequence[outputs.GetRouteTableAssociationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetRouteTableFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Sequence[outputs.GetRouteTableRouteResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        ...
    


class AwaitableGetRouteTableResult(GetRouteTableResult):
    def __await__(self): # -> Generator[Never, Any, GetRouteTableResult]:
        ...
    


def get_route_table(filters: Optional[Sequence[Union[GetRouteTableFilterArgs, GetRouteTableFilterArgsDict]]] = ..., gateway_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., route_table_id: Optional[_builtins.str] = ..., subnet_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., vpc_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRouteTableResult:
    
    ...

def get_route_table_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetRouteTableFilterArgs, GetRouteTableFilterArgsDict]]]]] = ..., gateway_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., route_table_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., subnet_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRouteTableResult]:
    
    ...

