

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualMachineResult', 'AwaitableGetVirtualMachineResult', 'get_virtual_machine', 'get_virtual_machine_output']
@pulumi.output_type
class GetVirtualMachineResult:
    def __init__(__self__, admin_username=..., availability_zone=..., azure_api_version=..., bare_metal_machine_id=..., boot_method=..., cloud_services_network_attachment=..., cluster_id=..., console_extended_location=..., cpu_cores=..., detailed_status=..., detailed_status_message=..., etag=..., extended_location=..., id=..., isolate_emulator_thread=..., location=..., memory_size_gb=..., name=..., network_attachments=..., network_data=..., placement_hints=..., power_state=..., provisioning_state=..., ssh_public_keys=..., storage_profile=..., system_data=..., tags=..., type=..., user_data=..., virtio_interface=..., vm_device_model=..., vm_image=..., vm_image_repository_credentials=..., volumes=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bareMetalMachineId")
    def bare_metal_machine_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootMethod")
    def boot_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudServicesNetworkAttachment")
    def cloud_services_network_attachment(self) -> outputs.NetworkAttachmentResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consoleExtendedLocation")
    def console_extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCores")
    def cpu_cores(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isolateEmulatorThread")
    def isolate_emulator_thread(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySizeGB")
    def memory_size_gb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAttachments")
    def network_attachments(self) -> Optional[Sequence[outputs.NetworkAttachmentResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkData")
    def network_data(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementHints")
    def placement_hints(self) -> Optional[Sequence[outputs.VirtualMachinePlacementHintResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="powerState")
    def power_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(self) -> Optional[Sequence[outputs.SshPublicKeyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> outputs.StorageProfileResponse:
        
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
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtioInterface")
    def virtio_interface(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmDeviceModel")
    def vm_device_model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmImage")
    def vm_image(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmImageRepositoryCredentials")
    def vm_image_repository_credentials(self) -> Optional[outputs.ImageRepositoryCredentialsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetVirtualMachineResult(GetVirtualMachineResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualMachineResult]:
        ...
    


def get_virtual_machine(resource_group_name: Optional[_builtins.str] = ..., virtual_machine_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualMachineResult:
    
    ...

def get_virtual_machine_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_machine_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualMachineResult]:
    
    ...

