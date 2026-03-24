

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGlobalReachConnectionResult', 'AwaitableGetGlobalReachConnectionResult', 'get_global_reach_connection', 'get_global_reach_connection_output']
@pulumi.output_type
class GetGlobalReachConnectionResult:
    
    def __init__(__self__, address_prefix=..., authorization_key=..., azure_api_version=..., circuit_connection_status=..., express_route_id=..., id=..., name=..., peer_express_route_circuit=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="circuitConnectionStatus")
    def circuit_connection_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRouteId")
    def express_route_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerExpressRouteCircuit")
    def peer_express_route_circuit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetGlobalReachConnectionResult(GetGlobalReachConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetGlobalReachConnectionResult]:
        ...
    


def get_global_reach_connection(global_reach_connection_name: Optional[_builtins.str] = ..., private_cloud_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGlobalReachConnectionResult:
    
    ...

def get_global_reach_connection_output(global_reach_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGlobalReachConnectionResult]:
    
    ...

