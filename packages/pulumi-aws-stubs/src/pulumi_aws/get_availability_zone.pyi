

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAvailabilityZoneResult', 'AwaitableGetAvailabilityZoneResult', 'get_availability_zone', 'get_availability_zone_output']
@pulumi.output_type
class GetAvailabilityZoneResult:
    
    def __init__(__self__, all_availability_zones=..., filters=..., group_long_name=..., group_name=..., id=..., name=..., name_suffix=..., network_border_group=..., opt_in_status=..., parent_zone_id=..., parent_zone_name=..., region=..., state=..., zone_id=..., zone_type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allAvailabilityZones")
    def all_availability_zones(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetAvailabilityZoneFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupLongName")
    def group_long_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> _builtins.str:
        
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
    @pulumi.getter(name="nameSuffix")
    def name_suffix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBorderGroup")
    def network_border_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optInStatus")
    def opt_in_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentZoneId")
    def parent_zone_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentZoneName")
    def parent_zone_name(self) -> _builtins.str:
        
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
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneType")
    def zone_type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAvailabilityZoneResult(GetAvailabilityZoneResult):
    def __await__(self): # -> Generator[Never, Any, GetAvailabilityZoneResult]:
        ...
    


def get_availability_zone(all_availability_zones: Optional[_builtins.bool] = ..., filters: Optional[Sequence[Union[GetAvailabilityZoneFilterArgs, GetAvailabilityZoneFilterArgsDict]]] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., zone_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAvailabilityZoneResult:
    
    ...

def get_availability_zone_output(all_availability_zones: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., filters: Optional[pulumi.Input[Optional[Sequence[Union[GetAvailabilityZoneFilterArgs, GetAvailabilityZoneFilterArgsDict]]]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., state: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., zone_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAvailabilityZoneResult]:
    
    ...

