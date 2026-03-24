

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetResourcePoolResult', 'AwaitableGetResourcePoolResult', 'get_resource_pool', 'get_resource_pool_output']
@pulumi.output_type
class GetResourcePoolResult:
    
    def __init__(__self__, azure_api_version=..., cpu_capacity_m_hz=..., cpu_limit_m_hz=..., cpu_overall_usage_m_hz=..., cpu_reservation_m_hz=..., cpu_shares_level=..., custom_resource_name=..., datastore_ids=..., extended_location=..., id=..., inventory_item_id=..., kind=..., location=..., mem_capacity_gb=..., mem_limit_mb=..., mem_overall_usage_gb=..., mem_reservation_mb=..., mem_shares_level=..., mo_name=..., mo_ref_id=..., name=..., network_ids=..., provisioning_state=..., statuses=..., system_data=..., tags=..., type=..., uuid=..., v_center_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCapacityMHz")
    def cpu_capacity_m_hz(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuLimitMHz")
    def cpu_limit_m_hz(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuOverallUsageMHz")
    def cpu_overall_usage_m_hz(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuReservationMHz")
    def cpu_reservation_m_hz(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuSharesLevel")
    def cpu_shares_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResourceName")
    def custom_resource_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datastoreIds")
    def datastore_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inventoryItemId")
    def inventory_item_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memCapacityGB")
    def mem_capacity_gb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memLimitMB")
    def mem_limit_mb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memOverallUsageGB")
    def mem_overall_usage_gb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memReservationMB")
    def mem_reservation_mb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memSharesLevel")
    def mem_shares_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moName")
    def mo_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moRefId")
    def mo_ref_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkIds")
    def network_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Sequence[outputs.ResourceStatusResponse]:
        
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
    @pulumi.getter
    def uuid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCenterId")
    def v_center_id(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetResourcePoolResult(GetResourcePoolResult):
    def __await__(self): # -> Generator[Never, Any, GetResourcePoolResult]:
        ...
    


def get_resource_pool(resource_group_name: Optional[_builtins.str] = ..., resource_pool_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetResourcePoolResult:
    
    ...

def get_resource_pool_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetResourcePoolResult]:
    
    ...

