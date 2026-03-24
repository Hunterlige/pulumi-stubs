

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRouteResult', 'AwaitableGetRouteResult', 'get_route', 'get_route_output']
@pulumi.output_type
class GetRouteResult:
    
    def __init__(__self__, address_prefix=..., azure_api_version=..., etag=..., has_bgp_override=..., id=..., name=..., next_hop_ip_address=..., next_hop_type=..., provisioning_state=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasBgpOverride")
    def has_bgp_override(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextHopIpAddress")
    def next_hop_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextHopType")
    def next_hop_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetRouteResult(GetRouteResult):
    def __await__(self): # -> Generator[Never, Any, GetRouteResult]:
        ...
    


def get_route(resource_group_name: Optional[_builtins.str] = ..., route_name: Optional[_builtins.str] = ..., route_table_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRouteResult:
    
    ...

def get_route_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., route_name: Optional[pulumi.Input[_builtins.str]] = ..., route_table_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRouteResult]:
    
    ...

