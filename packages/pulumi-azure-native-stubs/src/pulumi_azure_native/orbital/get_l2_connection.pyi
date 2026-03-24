

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetL2ConnectionResult', 'AwaitableGetL2ConnectionResult', 'get_l2_connection', 'get_l2_connection_output']
@pulumi.output_type
class GetL2ConnectionResult:
    
    def __init__(__self__, azure_api_version=..., circuit_id=..., edge_site=..., ground_station=..., ground_station_partner_router=..., id=..., location=..., name=..., system_data=..., tags=..., type=..., vlan_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="circuitId")
    def circuit_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgeSite")
    def edge_site(self) -> outputs.L2ConnectionsPropertiesResponseEdgeSite:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groundStation")
    def ground_station(self) -> outputs.L2ConnectionsPropertiesResponseGroundStation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groundStationPartnerRouter")
    def ground_station_partner_router(self) -> outputs.L2ConnectionsPropertiesResponseGroundStationPartnerRouter:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> _builtins.int:
        
        ...
    


class AwaitableGetL2ConnectionResult(GetL2ConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetL2ConnectionResult]:
        ...
    


def get_l2_connection(l2_connection_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetL2ConnectionResult:
    
    ...

def get_l2_connection_output(l2_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetL2ConnectionResult]:
    
    ...

