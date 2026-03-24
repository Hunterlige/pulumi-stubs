

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCapacityReservationGroupResult', 'AwaitableGetCapacityReservationGroupResult', 'get_capacity_reservation_group', 'get_capacity_reservation_group_output']
@pulumi.output_type
class GetCapacityReservationGroupResult:
    
    def __init__(__self__, azure_api_version=..., capacity_reservations=..., id=..., instance_view=..., location=..., name=..., sharing_profile=..., system_data=..., tags=..., type=..., virtual_machines_associated=..., zones=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservations")
    def capacity_reservations(self) -> Sequence[outputs.SubResourceReadOnlyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> outputs.CapacityReservationGroupInstanceViewResponse:
        
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
    @pulumi.getter(name="sharingProfile")
    def sharing_profile(self) -> Optional[outputs.ResourceSharingProfileResponse]:
        
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
    @pulumi.getter(name="virtualMachinesAssociated")
    def virtual_machines_associated(self) -> Sequence[outputs.SubResourceReadOnlyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableGetCapacityReservationGroupResult(GetCapacityReservationGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetCapacityReservationGroupResult]:
        ...
    


def get_capacity_reservation_group(capacity_reservation_group_name: Optional[_builtins.str] = ..., expand: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCapacityReservationGroupResult:
    
    ...

def get_capacity_reservation_group_output(capacity_reservation_group_name: Optional[pulumi.Input[_builtins.str]] = ..., expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCapacityReservationGroupResult]:
    
    ...

