

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
    
    def __init__(__self__, azure_api_version=..., custom_resource_name=..., disks=..., extended_location=..., firmware_type=..., folder_path=..., id=..., inventory_item_id=..., kind=..., location=..., memory_size_mb=..., mo_name=..., mo_ref_id=..., name=..., network_interfaces=..., num_cpus=..., num_cores_per_socket=..., os_name=..., os_type=..., provisioning_state=..., statuses=..., system_data=..., tags=..., tools_version=..., tools_version_status=..., type=..., uuid=..., v_center_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResourceName")
    def custom_resource_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Sequence[outputs.VirtualDiskResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firmwareType")
    def firmware_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> _builtins.str:
        
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
    @pulumi.getter(name="memorySizeMB")
    def memory_size_mb(self) -> _builtins.int:
        
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
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence[outputs.NetworkInterfaceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numCPUs")
    def num_cpus(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numCoresPerSocket")
    def num_cores_per_socket(self) -> _builtins.int:
        
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
    @pulumi.getter(name="toolsVersion")
    def tools_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolsVersionStatus")
    def tools_version_status(self) -> _builtins.str:
        
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
    


class AwaitableGetVirtualMachineTemplateResult(GetVirtualMachineTemplateResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualMachineTemplateResult]:
        ...
    


def get_virtual_machine_template(resource_group_name: Optional[_builtins.str] = ..., virtual_machine_template_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualMachineTemplateResult:
    
    ...

def get_virtual_machine_template_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_machine_template_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualMachineTemplateResult]:
    
    ...

