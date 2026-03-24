

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
__all__ = ['GetTransitGatewayRouteTablesResult', 'AwaitableGetTransitGatewayRouteTablesResult', 'get_transit_gateway_route_tables', 'get_transit_gateway_route_tables_output']
@pulumi.output_type
class GetTransitGatewayRouteTablesResult:
    
    def __init__(__self__, filters=..., id=..., ids=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetTransitGatewayRouteTablesFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetTransitGatewayRouteTablesResult(GetTransitGatewayRouteTablesResult):
    def __await__(self): # -> Generator[Never, Any, GetTransitGatewayRouteTablesResult]:
        ...
    


def get_transit_gateway_route_tables(filters: Optional[Sequence[Union[GetTransitGatewayRouteTablesFilterArgs, GetTransitGatewayRouteTablesFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTransitGatewayRouteTablesResult:
    
    ...

def get_transit_gateway_route_tables_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetTransitGatewayRouteTablesFilterArgs, GetTransitGatewayRouteTablesFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTransitGatewayRouteTablesResult]:
    
    ...

