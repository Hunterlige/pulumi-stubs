

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
    
    def __init__(__self__, allow_claim=..., applicable_schedule=..., artifact_deployment_status=..., artifacts=..., azure_api_version=..., compute_id=..., compute_vm=..., created_by_user=..., created_by_user_id=..., created_date=..., custom_image_id=..., data_disk_parameters=..., disallow_public_ip_address=..., environment_id=..., expiration_date=..., fqdn=..., gallery_image_reference=..., id=..., is_authentication_with_ssh_key=..., lab_subnet_name=..., lab_virtual_network_id=..., last_known_power_state=..., location=..., name=..., network_interface=..., notes=..., os_type=..., owner_object_id=..., owner_user_principal_name=..., password=..., plan_id=..., provisioning_state=..., schedule_parameters=..., size=..., ssh_key=..., storage_type=..., system_data=..., tags=..., type=..., unique_identifier=..., user_name=..., virtual_machine_creation_source=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowClaim")
    def allow_claim(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicableSchedule")
    def applicable_schedule(self) -> outputs.ApplicableScheduleResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactDeploymentStatus")
    def artifact_deployment_status(self) -> outputs.ArtifactDeploymentStatusPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def artifacts(self) -> Optional[Sequence[outputs.ArtifactInstallPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeId")
    def compute_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeVm")
    def compute_vm(self) -> outputs.ComputeVmPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByUser")
    def created_by_user(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByUserId")
    def created_by_user_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customImageId")
    def custom_image_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskParameters")
    def data_disk_parameters(self) -> Optional[Sequence[outputs.DataDiskPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disallowPublicIpAddress")
    def disallow_public_ip_address(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="galleryImageReference")
    def gallery_image_reference(self) -> Optional[outputs.GalleryImageReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAuthenticationWithSshKey")
    def is_authentication_with_ssh_key(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labSubnetName")
    def lab_subnet_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labVirtualNetworkId")
    def lab_virtual_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastKnownPowerState")
    def last_known_power_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterface")
    def network_interface(self) -> Optional[outputs.NetworkInterfacePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerObjectId")
    def owner_object_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerUserPrincipalName")
    def owner_user_principal_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleParameters")
    def schedule_parameters(self) -> Optional[Sequence[outputs.ScheduleCreationParameterResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sshKey")
    def ssh_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineCreationSource")
    def virtual_machine_creation_source(self) -> _builtins.str:
        
        ...
    


class AwaitableGetVirtualMachineResult(GetVirtualMachineResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualMachineResult]:
        ...
    


def get_virtual_machine(expand: Optional[_builtins.str] = ..., lab_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualMachineResult:
    
    ...

def get_virtual_machine_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., lab_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualMachineResult]:
    
    ...

