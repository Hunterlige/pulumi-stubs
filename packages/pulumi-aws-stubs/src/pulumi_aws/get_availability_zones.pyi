

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
__all__ = ['GetAvailabilityZonesResult', 'AwaitableGetAvailabilityZonesResult', 'get_availability_zones', 'get_availability_zones_output']
@pulumi.output_type
class GetAvailabilityZonesResult:
    
    def __init__(__self__, all_availability_zones=..., exclude_names=..., exclude_zone_ids=..., filters=..., group_names=..., id=..., names=..., region=..., state=..., zone_ids=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allAvailabilityZones")
    def all_availability_zones(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeNames")
    def exclude_names(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeZoneIds")
    def exclude_zone_ids(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetAvailabilityZonesFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupNames")
    def group_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneIds")
    def zone_ids(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetAvailabilityZonesResult(GetAvailabilityZonesResult):
    def __await__(self): # -> Generator[Never, Any, GetAvailabilityZonesResult]:
        ...
    


def get_availability_zones(all_availability_zones: Optional[_builtins.bool] = ..., exclude_names: Optional[Sequence[_builtins.str]] = ..., exclude_zone_ids: Optional[Sequence[_builtins.str]] = ..., filters: Optional[Sequence[Union[GetAvailabilityZonesFilterArgs, GetAvailabilityZonesFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAvailabilityZonesResult:
    
    ...

def get_availability_zones_output(all_availability_zones: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., exclude_names: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., exclude_zone_ids: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., filters: Optional[pulumi.Input[Optional[Sequence[Union[GetAvailabilityZonesFilterArgs, GetAvailabilityZonesFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., state: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAvailabilityZonesResult]:
    
    ...

