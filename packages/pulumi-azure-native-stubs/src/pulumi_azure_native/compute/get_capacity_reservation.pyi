

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCapacityReservationResult', 'AwaitableGetCapacityReservationResult', 'get_capacity_reservation', 'get_capacity_reservation_output']
@pulumi.output_type
class GetCapacityReservationResult:
    
    def __init__(__self__, azure_api_version=..., id=..., instance_view=..., location=..., name=..., platform_fault_domain_count=..., provisioning_state=..., provisioning_time=..., reservation_id=..., sku=..., system_data=..., tags=..., time_created=..., type=..., virtual_machines_associated=..., zones=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> outputs.CapacityReservationInstanceViewResponse:
        
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
    @pulumi.getter(name="platformFaultDomainCount")
    def platform_fault_domain_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningTime")
    def provisioning_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationId")
    def reservation_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse:
        
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
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> _builtins.str:
        
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
    


class AwaitableGetCapacityReservationResult(GetCapacityReservationResult):
    def __await__(self): # -> Generator[Never, Any, GetCapacityReservationResult]:
        ...
    


def get_capacity_reservation(capacity_reservation_group_name: Optional[_builtins.str] = ..., capacity_reservation_name: Optional[_builtins.str] = ..., expand: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCapacityReservationResult:
    
    ...

def get_capacity_reservation_output(capacity_reservation_group_name: Optional[pulumi.Input[_builtins.str]] = ..., capacity_reservation_name: Optional[pulumi.Input[_builtins.str]] = ..., expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCapacityReservationResult]:
    
    ...

