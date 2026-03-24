

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
__all__ = ['GetLocalGatewayRouteTablesResult', 'AwaitableGetLocalGatewayRouteTablesResult', 'get_local_gateway_route_tables', 'get_local_gateway_route_tables_output']
@pulumi.output_type
class GetLocalGatewayRouteTablesResult:
    
    def __init__(__self__, filters=..., id=..., ids=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetLocalGatewayRouteTablesFilterResult]]:
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
    


class AwaitableGetLocalGatewayRouteTablesResult(GetLocalGatewayRouteTablesResult):
    def __await__(self): # -> Generator[Never, Any, GetLocalGatewayRouteTablesResult]:
        ...
    


def get_local_gateway_route_tables(filters: Optional[Sequence[Union[GetLocalGatewayRouteTablesFilterArgs, GetLocalGatewayRouteTablesFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLocalGatewayRouteTablesResult:
    
    ...

def get_local_gateway_route_tables_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetLocalGatewayRouteTablesFilterArgs, GetLocalGatewayRouteTablesFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLocalGatewayRouteTablesResult]:
    
    ...

