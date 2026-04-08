import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApplicableScheduleResponse",
    "ArmTemplateParameterPropertiesResponse",
    "ArtifactDeploymentStatusPropertiesResponse",
    "ArtifactInstallPropertiesResponse",
    "ArtifactParameterPropertiesResponse",
    "AttachNewDataDiskOptionsResponse",
    "BulkCreationParametersResponse",
    "ComputeDataDiskResponse",
    "ComputeVmInstanceViewStatusResponse",
    "ComputeVmPropertiesResponse",
    "CustomImagePropertiesCustomResponse",
    "CustomImagePropertiesFromPlanResponse",
    "CustomImagePropertiesFromVmResponse",
    "DataDiskPropertiesResponse",
    "DataDiskStorageTypeInfoResponse",
    "DayDetailsResponse",
    "EnvironmentDeploymentPropertiesResponse",
    "EventResponse",
    "ExternalSubnetResponse",
    "FormulaPropertiesFromVmResponse",
    "GalleryImageReferenceResponse",
    "HourDetailsResponse",
    "IdentityPropertiesResponse",
    "InboundNatRuleResponse",
    "LabAnnouncementPropertiesResponse",
    "LabSupportPropertiesResponse",
    "LabVhdResponse",
    "LabVirtualMachineCreationParameterResponse",
    "LinuxOsInfoResponse",
    "NetworkInterfacePropertiesResponse",
    "NotificationSettingsResponse",
    "PortResponse",
    "ScheduleCreationParameterResponse",
    "ScheduleResponse",
    "SharedPublicIpAddressConfigurationResponse",
    "SubnetOverrideResponse",
    "SubnetResponse",
    "SubnetSharedPublicIpAddressConfigurationResponse",
    "SystemDataResponse",
    "UserIdentityResponse",
    "UserSecretStoreResponse",
    "WeekDetailsResponse",
    "WindowsOsInfoResponse",
]

@pulumi.output_type
class ApplicableScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        lab_vms_shutdown: Optional[outputs.ScheduleResponse] = ...,
        lab_vms_startup: Optional[outputs.ScheduleResponse] = ...,
        location: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="labVmsShutdown")
    def lab_vms_shutdown(self) -> Optional[outputs.ScheduleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="labVmsStartup")
    def lab_vms_startup(self) -> Optional[outputs.ScheduleResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ArmTemplateParameterPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ArtifactDeploymentStatusPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        artifacts_applied: Optional[_builtins.int] = ...,
        deployment_status: Optional[_builtins.str] = ...,
        total_artifacts: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactsApplied")
    def artifacts_applied(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="totalArtifacts")
    def total_artifacts(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ArtifactInstallPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        artifact_id: Optional[_builtins.str] = ...,
        artifact_title: Optional[_builtins.str] = ...,
        deployment_status_message: Optional[_builtins.str] = ...,
        install_time: Optional[_builtins.str] = ...,
        parameters: Optional[
            Sequence[outputs.ArtifactParameterPropertiesResponse]
        ] = ...,
        status: Optional[_builtins.str] = ...,
        vm_extension_status_message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="artifactTitle")
    def artifact_title(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentStatusMessage")
    def deployment_status_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="installTime")
    def install_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[Sequence[outputs.ArtifactParameterPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmExtensionStatusMessage")
    def vm_extension_status_message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ArtifactParameterPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AttachNewDataDiskOptionsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_name: Optional[_builtins.str] = ...,
        disk_size_gi_b: Optional[_builtins.int] = ...,
        disk_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGiB")
    def disk_size_gi_b(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BulkCreationParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, instance_count: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ComputeDataDiskResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_size_gi_b: Optional[_builtins.int] = ...,
        disk_uri: Optional[_builtins.str] = ...,
        managed_disk_id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGiB")
    def disk_size_gi_b(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="diskUri")
    def disk_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedDiskId")
    def managed_disk_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ComputeVmInstanceViewStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.str] = ...,
        display_status: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayStatus")
    def display_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ComputeVmPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_disk_ids: Optional[Sequence[_builtins.str]] = ...,
        data_disks: Optional[Sequence[outputs.ComputeDataDiskResponse]] = ...,
        network_interface_id: Optional[_builtins.str] = ...,
        os_disk_id: Optional[_builtins.str] = ...,
        os_type: Optional[_builtins.str] = ...,
        statuses: Optional[Sequence[outputs.ComputeVmInstanceViewStatusResponse]] = ...,
        vm_size: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataDiskIds")
    def data_disk_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> Optional[Sequence[outputs.ComputeDataDiskResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osDiskId")
    def os_disk_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[Sequence[outputs.ComputeVmInstanceViewStatusResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomImagePropertiesCustomResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        os_type: _builtins.str,
        image_name: Optional[_builtins.str] = ...,
        sys_prep: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sysPrep")
    def sys_prep(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CustomImagePropertiesFromPlanResponse(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        offer: Optional[_builtins.str] = ...,
        publisher: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def offer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomImagePropertiesFromVmResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        linux_os_info: Optional[outputs.LinuxOsInfoResponse] = ...,
        source_vm_id: Optional[_builtins.str] = ...,
        windows_os_info: Optional[outputs.WindowsOsInfoResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linuxOsInfo")
    def linux_os_info(self) -> Optional[outputs.LinuxOsInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sourceVmId")
    def source_vm_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="windowsOsInfo")
    def windows_os_info(self) -> Optional[outputs.WindowsOsInfoResponse]: ...

@pulumi.output_type
class DataDiskPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        attach_new_data_disk_options: Optional[
            outputs.AttachNewDataDiskOptionsResponse
        ] = ...,
        existing_lab_disk_id: Optional[_builtins.str] = ...,
        host_caching: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachNewDataDiskOptions")
    def attach_new_data_disk_options(
        self,
    ) -> Optional[outputs.AttachNewDataDiskOptionsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="existingLabDiskId")
    def existing_lab_disk_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostCaching")
    def host_caching(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataDiskStorageTypeInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        lun: Optional[_builtins.str] = ...,
        storage_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def lun(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DayDetailsResponse(dict):
    def __init__(__self__, *, time: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnvironmentDeploymentPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arm_template_id: Optional[_builtins.str] = ...,
        parameters: Optional[
            Sequence[outputs.ArmTemplateParameterPropertiesResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="armTemplateId")
    def arm_template_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[Sequence[outputs.ArmTemplateParameterPropertiesResponse]]: ...

@pulumi.output_type
class EventResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, event_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventName")
    def event_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExternalSubnetResponse(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FormulaPropertiesFromVmResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, lab_vm_id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="labVmId")
    def lab_vm_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GalleryImageReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        offer: Optional[_builtins.str] = ...,
        os_type: Optional[_builtins.str] = ...,
        publisher: Optional[_builtins.str] = ...,
        sku: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def offer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HourDetailsResponse(dict):
    def __init__(__self__, *, minute: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class IdentityPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_secret_url: Optional[_builtins.str] = ...,
        principal_id: Optional[_builtins.str] = ...,
        tenant_id: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretUrl")
    def client_secret_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InboundNatRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backend_port: Optional[_builtins.int] = ...,
        frontend_port: Optional[_builtins.int] = ...,
        transport_protocol: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="transportProtocol")
    def transport_protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LabAnnouncementPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        unique_identifier: _builtins.str,
        enabled: Optional[_builtins.str] = ...,
        expiration_date: Optional[_builtins.str] = ...,
        expired: Optional[_builtins.bool] = ...,
        markdown: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def expired(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def markdown(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LabSupportPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.str] = ...,
        markdown: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def markdown(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LabVhdResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LabVirtualMachineCreationParameterResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_claim: Optional[_builtins.bool] = ...,
        artifacts: Optional[Sequence[outputs.ArtifactInstallPropertiesResponse]] = ...,
        bulk_creation_parameters: Optional[
            outputs.BulkCreationParametersResponse
        ] = ...,
        created_date: Optional[_builtins.str] = ...,
        custom_image_id: Optional[_builtins.str] = ...,
        data_disk_parameters: Optional[
            Sequence[outputs.DataDiskPropertiesResponse]
        ] = ...,
        disallow_public_ip_address: Optional[_builtins.bool] = ...,
        environment_id: Optional[_builtins.str] = ...,
        expiration_date: Optional[_builtins.str] = ...,
        gallery_image_reference: Optional[outputs.GalleryImageReferenceResponse] = ...,
        is_authentication_with_ssh_key: Optional[_builtins.bool] = ...,
        lab_subnet_name: Optional[_builtins.str] = ...,
        lab_virtual_network_id: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        network_interface: Optional[outputs.NetworkInterfacePropertiesResponse] = ...,
        notes: Optional[_builtins.str] = ...,
        owner_object_id: Optional[_builtins.str] = ...,
        owner_user_principal_name: Optional[_builtins.str] = ...,
        password: Optional[_builtins.str] = ...,
        plan_id: Optional[_builtins.str] = ...,
        schedule_parameters: Optional[
            Sequence[outputs.ScheduleCreationParameterResponse]
        ] = ...,
        size: Optional[_builtins.str] = ...,
        ssh_key: Optional[_builtins.str] = ...,
        storage_type: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
        user_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowClaim")
    def allow_claim(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def artifacts(
        self,
    ) -> Optional[Sequence[outputs.ArtifactInstallPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="bulkCreationParameters")
    def bulk_creation_parameters(
        self,
    ) -> Optional[outputs.BulkCreationParametersResponse]: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customImageId")
    def custom_image_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataDiskParameters")
    def data_disk_parameters(
        self,
    ) -> Optional[Sequence[outputs.DataDiskPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="disallowPublicIpAddress")
    def disallow_public_ip_address(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="galleryImageReference")
    def gallery_image_reference(
        self,
    ) -> Optional[outputs.GalleryImageReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="isAuthenticationWithSshKey")
    def is_authentication_with_ssh_key(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="labSubnetName")
    def lab_subnet_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="labVirtualNetworkId")
    def lab_virtual_network_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterface")
    def network_interface(
        self,
    ) -> Optional[outputs.NetworkInterfacePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerObjectId")
    def owner_object_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerUserPrincipalName")
    def owner_user_principal_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleParameters")
    def schedule_parameters(
        self,
    ) -> Optional[Sequence[outputs.ScheduleCreationParameterResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sshKey")
    def ssh_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LinuxOsInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, linux_os_state: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linuxOsState")
    def linux_os_state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NetworkInterfacePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_name: Optional[_builtins.str] = ...,
        private_ip_address: Optional[_builtins.str] = ...,
        public_ip_address: Optional[_builtins.str] = ...,
        public_ip_address_id: Optional[_builtins.str] = ...,
        rdp_authority: Optional[_builtins.str] = ...,
        shared_public_ip_address_configuration: Optional[
            outputs.SharedPublicIpAddressConfigurationResponse
        ] = ...,
        ssh_authority: Optional[_builtins.str] = ...,
        subnet_id: Optional[_builtins.str] = ...,
        virtual_network_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicIpAddressId")
    def public_ip_address_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rdpAuthority")
    def rdp_authority(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedPublicIpAddressConfiguration")
    def shared_public_ip_address_configuration(
        self,
    ) -> Optional[outputs.SharedPublicIpAddressConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sshAuthority")
    def ssh_authority(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NotificationSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        email_recipient: Optional[_builtins.str] = ...,
        notification_locale: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        time_in_minutes: Optional[_builtins.int] = ...,
        webhook_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailRecipient")
    def email_recipient(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationLocale")
    def notification_locale(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeInMinutes")
    def time_in_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="webhookUrl")
    def webhook_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PortResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backend_port: Optional[_builtins.int] = ...,
        transport_protocol: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="transportProtocol")
    def transport_protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScheduleCreationParameterResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location: _builtins.str,
        daily_recurrence: Optional[outputs.DayDetailsResponse] = ...,
        hourly_recurrence: Optional[outputs.HourDetailsResponse] = ...,
        name: Optional[_builtins.str] = ...,
        notification_settings: Optional[outputs.NotificationSettingsResponse] = ...,
        status: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
        target_resource_id: Optional[_builtins.str] = ...,
        task_type: Optional[_builtins.str] = ...,
        time_zone_id: Optional[_builtins.str] = ...,
        weekly_recurrence: Optional[outputs.WeekDetailsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dailyRecurrence")
    def daily_recurrence(self) -> Optional[outputs.DayDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="hourlyRecurrence")
    def hourly_recurrence(self) -> Optional[outputs.HourDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(
        self,
    ) -> Optional[outputs.NotificationSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="weeklyRecurrence")
    def weekly_recurrence(self) -> Optional[outputs.WeekDetailsResponse]: ...

@pulumi.output_type
class ScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_date: _builtins.str,
        id: _builtins.str,
        name: _builtins.str,
        provisioning_state: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        unique_identifier: _builtins.str,
        daily_recurrence: Optional[outputs.DayDetailsResponse] = ...,
        hourly_recurrence: Optional[outputs.HourDetailsResponse] = ...,
        location: Optional[_builtins.str] = ...,
        notification_settings: Optional[outputs.NotificationSettingsResponse] = ...,
        status: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
        target_resource_id: Optional[_builtins.str] = ...,
        task_type: Optional[_builtins.str] = ...,
        time_zone_id: Optional[_builtins.str] = ...,
        weekly_recurrence: Optional[outputs.WeekDetailsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dailyRecurrence")
    def daily_recurrence(self) -> Optional[outputs.DayDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="hourlyRecurrence")
    def hourly_recurrence(self) -> Optional[outputs.HourDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(
        self,
    ) -> Optional[outputs.NotificationSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="weeklyRecurrence")
    def weekly_recurrence(self) -> Optional[outputs.WeekDetailsResponse]: ...

@pulumi.output_type
class SharedPublicIpAddressConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        inbound_nat_rules: Optional[Sequence[outputs.InboundNatRuleResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inboundNatRules")
    def inbound_nat_rules(
        self,
    ) -> Optional[Sequence[outputs.InboundNatRuleResponse]]: ...

@pulumi.output_type
class SubnetOverrideResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        lab_subnet_name: Optional[_builtins.str] = ...,
        resource_id: Optional[_builtins.str] = ...,
        shared_public_ip_address_configuration: Optional[
            outputs.SubnetSharedPublicIpAddressConfigurationResponse
        ] = ...,
        use_in_vm_creation_permission: Optional[_builtins.str] = ...,
        use_public_ip_address_permission: Optional[_builtins.str] = ...,
        virtual_network_pool_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="labSubnetName")
    def lab_subnet_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedPublicIpAddressConfiguration")
    def shared_public_ip_address_configuration(
        self,
    ) -> Optional[outputs.SubnetSharedPublicIpAddressConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="useInVmCreationPermission")
    def use_in_vm_creation_permission(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="usePublicIpAddressPermission")
    def use_public_ip_address_permission(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkPoolName")
    def virtual_network_pool_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SubnetResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_public_ip: Optional[_builtins.str] = ...,
        lab_subnet_name: Optional[_builtins.str] = ...,
        resource_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPublicIp")
    def allow_public_ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="labSubnetName")
    def lab_subnet_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SubnetSharedPublicIpAddressConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, allowed_ports: Optional[Sequence[outputs.PortResponse]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedPorts")
    def allowed_ports(self) -> Optional[Sequence[outputs.PortResponse]]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_id: Optional[_builtins.str] = ...,
        object_id: Optional[_builtins.str] = ...,
        principal_id: Optional[_builtins.str] = ...,
        principal_name: Optional[_builtins.str] = ...,
        tenant_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalName")
    def principal_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserSecretStoreResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_vault_id: Optional[_builtins.str] = ...,
        key_vault_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WeekDetailsResponse(dict):
    def __init__(
        __self__,
        *,
        time: Optional[_builtins.str] = ...,
        weekdays: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def weekdays(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class WindowsOsInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, windows_os_state: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="windowsOsState")
    def windows_os_state(self) -> Optional[_builtins.str]: ...
