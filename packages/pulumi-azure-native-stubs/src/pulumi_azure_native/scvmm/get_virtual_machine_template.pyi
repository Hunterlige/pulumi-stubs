

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualMachineTemplateResult', 'AwaitableGetVirtualMachineTemplateResult', 'get_virtual_machine_template', 'get_virtual_machine_template_output']
@pulumi.output_type
class GetVirtualMachineTemplateResult:
    
    def __init__(__self__, azure_api_version=..., computer_name=..., cpu_count=..., disks=..., dynamic_memory_enabled=..., dynamic_memory_max_mb=..., dynamic_memory_min_mb=..., extended_location=..., generation=..., id=..., inventory_item_id=..., is_customizable=..., is_highly_available=..., limit_cpu_for_migration=..., location=..., memory_mb=..., name=..., network_interfaces=..., os_name=..., os_type=..., provisioning_state=..., system_data=..., tags=..., type=..., uuid=..., vmm_server_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Sequence[outputs.VirtualDiskResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicMemoryEnabled")
    def dynamic_memory_enabled(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicMemoryMaxMB")
    def dynamic_memory_max_mb(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicMemoryMinMB")
    def dynamic_memory_min_mb(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> _builtins.int:
        
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
    @pulumi.getter(name="isCustomizable")
    def is_customizable(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isHighlyAvailable")
    def is_highly_available(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="limitCpuForMigration")
    def limit_cpu_for_migration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryMB")
    def memory_mb(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence[outputs.NetworkInterfacesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osName")
    def os_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str:
        
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
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmmServerId")
    def vmm_server_id(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetVirtualMachineTemplateResult(GetVirtualMachineTemplateResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualMachineTemplateResult]:
        ...
    


def get_virtual_machine_template(resource_group_name: Optional[_builtins.str] = ..., virtual_machine_template_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualMachineTemplateResult:
    
    ...

def get_virtual_machine_template_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_machine_template_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualMachineTemplateResult]:
    
    ...

