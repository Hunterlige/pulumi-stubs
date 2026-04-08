import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ArmTemplateParameterPropertiesArgs",
    "ArmTemplateParameterPropertiesArgsDict",
    "ArtifactInstallPropertiesArgs",
    "ArtifactInstallPropertiesArgsDict",
    "ArtifactParameterPropertiesArgs",
    "ArtifactParameterPropertiesArgsDict",
    "AttachNewDataDiskOptionsArgs",
    "AttachNewDataDiskOptionsArgsDict",
    "BulkCreationParametersArgs",
    "BulkCreationParametersArgsDict",
    "CustomImagePropertiesCustomArgs",
    "CustomImagePropertiesCustomArgsDict",
    "CustomImagePropertiesFromPlanArgs",
    "CustomImagePropertiesFromPlanArgsDict",
    "CustomImagePropertiesFromVmArgs",
    "CustomImagePropertiesFromVmArgsDict",
    "DataDiskPropertiesArgs",
    "DataDiskPropertiesArgsDict",
    "DataDiskStorageTypeInfoArgs",
    "DataDiskStorageTypeInfoArgsDict",
    "DayDetailsArgs",
    "DayDetailsArgsDict",
    "EnvironmentDeploymentPropertiesArgs",
    "EnvironmentDeploymentPropertiesArgsDict",
    "EventArgs",
    "EventArgsDict",
    "FormulaPropertiesFromVmArgs",
    "FormulaPropertiesFromVmArgsDict",
    "GalleryImageReferenceArgs",
    "GalleryImageReferenceArgsDict",
    "HourDetailsArgs",
    "HourDetailsArgsDict",
    "IdentityPropertiesArgs",
    "IdentityPropertiesArgsDict",
    "InboundNatRuleArgs",
    "InboundNatRuleArgsDict",
    "LabAnnouncementPropertiesArgs",
    "LabAnnouncementPropertiesArgsDict",
    "LabSupportPropertiesArgs",
    "LabSupportPropertiesArgsDict",
    "LabVirtualMachineCreationParameterArgs",
    "LabVirtualMachineCreationParameterArgsDict",
    "LinuxOsInfoArgs",
    "LinuxOsInfoArgsDict",
    "NetworkInterfacePropertiesArgs",
    "NetworkInterfacePropertiesArgsDict",
    "NotificationSettingsArgs",
    "NotificationSettingsArgsDict",
    "PortArgs",
    "PortArgsDict",
    "ScheduleCreationParameterArgs",
    "ScheduleCreationParameterArgsDict",
    "SharedPublicIpAddressConfigurationArgs",
    "SharedPublicIpAddressConfigurationArgsDict",
    "SubnetOverrideArgs",
    "SubnetOverrideArgsDict",
    "SubnetSharedPublicIpAddressConfigurationArgs",
    "SubnetSharedPublicIpAddressConfigurationArgsDict",
    "SubnetArgs",
    "SubnetArgsDict",
    "UserIdentityArgs",
    "UserIdentityArgsDict",
    "UserSecretStoreArgs",
    "UserSecretStoreArgsDict",
    "WeekDetailsArgs",
    "WeekDetailsArgsDict",
    "WindowsOsInfoArgs",
    "WindowsOsInfoArgsDict",
]

class ArmTemplateParameterPropertiesArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ArmTemplateParameterPropertiesArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ArtifactInstallPropertiesArgsDict(TypedDict):
    artifact_id: NotRequired[pulumi.Input[_builtins.str]]
    artifact_title: NotRequired[pulumi.Input[_builtins.str]]
    deployment_status_message: NotRequired[pulumi.Input[_builtins.str]]
    install_time: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ArtifactParameterPropertiesArgsDict]]]
    ]
    status: NotRequired[pulumi.Input[_builtins.str]]
    vm_extension_status_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ArtifactInstallPropertiesArgs:
    def __init__(
        __self__,
        *,
        artifact_id: Optional[pulumi.Input[_builtins.str]] = ...,
        artifact_title: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_status_message: Optional[pulumi.Input[_builtins.str]] = ...,
        install_time: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ArtifactParameterPropertiesArgs]]]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_extension_status_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactId")
    def artifact_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @artifact_id.setter
    def artifact_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="artifactTitle")
    def artifact_title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @artifact_title.setter
    def artifact_title(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentStatusMessage")
    def deployment_status_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_status_message.setter
    def deployment_status_message(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="installTime")
    def install_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @install_time.setter
    def install_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ArtifactParameterPropertiesArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ArtifactParameterPropertiesArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmExtensionStatusMessage")
    def vm_extension_status_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_extension_status_message.setter
    def vm_extension_status_message(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ArtifactParameterPropertiesArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ArtifactParameterPropertiesArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AttachNewDataDiskOptionsArgsDict(TypedDict):
    disk_name: NotRequired[pulumi.Input[_builtins.str]]
    disk_size_gi_b: NotRequired[pulumi.Input[_builtins.int]]
    disk_type: NotRequired[pulumi.Input[Union[_builtins.str, StorageType]]]

@pulumi.input_type
class AttachNewDataDiskOptionsArgs:
    def __init__(
        __self__,
        *,
        disk_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size_gi_b: Optional[pulumi.Input[_builtins.int]] = ...,
        disk_type: Optional[pulumi.Input[Union[_builtins.str, StorageType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_name.setter
    def disk_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGiB")
    def disk_size_gi_b(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gi_b.setter
    def disk_size_gi_b(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StorageType]]]: ...
    @disk_type.setter
    def disk_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StorageType]]]
    ): ...

class BulkCreationParametersArgsDict(TypedDict):
    instance_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class BulkCreationParametersArgs:
    def __init__(
        __self__, *, instance_count: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CustomImagePropertiesCustomArgsDict(TypedDict):
    os_type: pulumi.Input[Union[_builtins.str, CustomImageOsType]]
    image_name: NotRequired[pulumi.Input[_builtins.str]]
    sys_prep: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class CustomImagePropertiesCustomArgs:
    def __init__(
        __self__,
        *,
        os_type: pulumi.Input[Union[_builtins.str, CustomImageOsType]],
        image_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sys_prep: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Input[Union[_builtins.str, CustomImageOsType]]: ...
    @os_type.setter
    def os_type(self, value: pulumi.Input[Union[_builtins.str, CustomImageOsType]]): ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sysPrep")
    def sys_prep(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @sys_prep.setter
    def sys_prep(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class CustomImagePropertiesFromPlanArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    offer: NotRequired[pulumi.Input[_builtins.str]]
    publisher: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CustomImagePropertiesFromPlanArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        offer: Optional[pulumi.Input[_builtins.str]] = ...,
        publisher: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def offer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @offer.setter
    def offer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomImagePropertiesFromVmArgsDict(TypedDict):
    linux_os_info: NotRequired[pulumi.Input[LinuxOsInfoArgsDict]]
    source_vm_id: NotRequired[pulumi.Input[_builtins.str]]
    windows_os_info: NotRequired[pulumi.Input[WindowsOsInfoArgsDict]]

@pulumi.input_type
class CustomImagePropertiesFromVmArgs:
    def __init__(
        __self__,
        *,
        linux_os_info: Optional[pulumi.Input[LinuxOsInfoArgs]] = ...,
        source_vm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        windows_os_info: Optional[pulumi.Input[WindowsOsInfoArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linuxOsInfo")
    def linux_os_info(self) -> Optional[pulumi.Input[LinuxOsInfoArgs]]: ...
    @linux_os_info.setter
    def linux_os_info(self, value: Optional[pulumi.Input[LinuxOsInfoArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceVmId")
    def source_vm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_vm_id.setter
    def source_vm_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="windowsOsInfo")
    def windows_os_info(self) -> Optional[pulumi.Input[WindowsOsInfoArgs]]: ...
    @windows_os_info.setter
    def windows_os_info(self, value: Optional[pulumi.Input[WindowsOsInfoArgs]]): ...

class DataDiskPropertiesArgsDict(TypedDict):
    attach_new_data_disk_options: NotRequired[
        pulumi.Input[AttachNewDataDiskOptionsArgsDict]
    ]
    existing_lab_disk_id: NotRequired[pulumi.Input[_builtins.str]]
    host_caching: NotRequired[pulumi.Input[Union[_builtins.str, HostCachingOptions]]]

@pulumi.input_type
class DataDiskPropertiesArgs:
    def __init__(
        __self__,
        *,
        attach_new_data_disk_options: Optional[
            pulumi.Input[AttachNewDataDiskOptionsArgs]
        ] = ...,
        existing_lab_disk_id: Optional[pulumi.Input[_builtins.str]] = ...,
        host_caching: Optional[
            pulumi.Input[Union[_builtins.str, HostCachingOptions]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachNewDataDiskOptions")
    def attach_new_data_disk_options(
        self,
    ) -> Optional[pulumi.Input[AttachNewDataDiskOptionsArgs]]: ...
    @attach_new_data_disk_options.setter
    def attach_new_data_disk_options(
        self, value: Optional[pulumi.Input[AttachNewDataDiskOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="existingLabDiskId")
    def existing_lab_disk_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @existing_lab_disk_id.setter
    def existing_lab_disk_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostCaching")
    def host_caching(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, HostCachingOptions]]]: ...
    @host_caching.setter
    def host_caching(
        self, value: Optional[pulumi.Input[Union[_builtins.str, HostCachingOptions]]]
    ): ...

class DataDiskStorageTypeInfoArgsDict(TypedDict):
    lun: NotRequired[pulumi.Input[_builtins.str]]
    storage_type: NotRequired[pulumi.Input[Union[_builtins.str, StorageType]]]

@pulumi.input_type
class DataDiskStorageTypeInfoArgs:
    def __init__(
        __self__,
        *,
        lun: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_type: Optional[pulumi.Input[Union[_builtins.str, StorageType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def lun(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lun.setter
    def lun(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StorageType]]]: ...
    @storage_type.setter
    def storage_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StorageType]]]
    ): ...

class DayDetailsArgsDict(TypedDict):
    time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DayDetailsArgs:
    def __init__(
        __self__, *, time: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time.setter
    def time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentDeploymentPropertiesArgsDict(TypedDict):
    arm_template_id: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ArmTemplateParameterPropertiesArgsDict]]]
    ]

@pulumi.input_type
class EnvironmentDeploymentPropertiesArgs:
    def __init__(
        __self__,
        *,
        arm_template_id: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ArmTemplateParameterPropertiesArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="armTemplateId")
    def arm_template_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arm_template_id.setter
    def arm_template_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ArmTemplateParameterPropertiesArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ArmTemplateParameterPropertiesArgs]]]
        ],
    ): ...

class EventArgsDict(TypedDict):
    event_name: NotRequired[
        pulumi.Input[Union[_builtins.str, NotificationChannelEventType]]
    ]

@pulumi.input_type
class EventArgs:
    def __init__(
        __self__,
        *,
        event_name: Optional[
            pulumi.Input[Union[_builtins.str, NotificationChannelEventType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventName")
    def event_name(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NotificationChannelEventType]]]: ...
    @event_name.setter
    def event_name(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, NotificationChannelEventType]]
        ],
    ): ...

class FormulaPropertiesFromVmArgsDict(TypedDict):
    lab_vm_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FormulaPropertiesFromVmArgs:
    def __init__(
        __self__, *, lab_vm_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="labVmId")
    def lab_vm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lab_vm_id.setter
    def lab_vm_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GalleryImageReferenceArgsDict(TypedDict):
    offer: NotRequired[pulumi.Input[_builtins.str]]
    os_type: NotRequired[pulumi.Input[_builtins.str]]
    publisher: NotRequired[pulumi.Input[_builtins.str]]
    sku: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GalleryImageReferenceArgs:
    def __init__(
        __self__,
        *,
        offer: Optional[pulumi.Input[_builtins.str]] = ...,
        os_type: Optional[pulumi.Input[_builtins.str]] = ...,
        publisher: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def offer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @offer.setter
    def offer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HourDetailsArgsDict(TypedDict):
    minute: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class HourDetailsArgs:
    def __init__(
        __self__, *, minute: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minute.setter
    def minute(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class IdentityPropertiesArgsDict(TypedDict):
    client_secret_url: NotRequired[pulumi.Input[_builtins.str]]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ManagedIdentityType]]]

@pulumi.input_type
class IdentityPropertiesArgs:
    def __init__(
        __self__,
        *,
        client_secret_url: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretUrl")
    def client_secret_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret_url.setter
    def client_secret_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityType]]]
    ): ...

class InboundNatRuleArgsDict(TypedDict):
    backend_port: NotRequired[pulumi.Input[_builtins.int]]
    frontend_port: NotRequired[pulumi.Input[_builtins.int]]
    transport_protocol: NotRequired[
        pulumi.Input[Union[_builtins.str, TransportProtocol]]
    ]

@pulumi.input_type
class InboundNatRuleArgs:
    def __init__(
        __self__,
        *,
        backend_port: Optional[pulumi.Input[_builtins.int]] = ...,
        frontend_port: Optional[pulumi.Input[_builtins.int]] = ...,
        transport_protocol: Optional[
            pulumi.Input[Union[_builtins.str, TransportProtocol]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @backend_port.setter
    def backend_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @frontend_port.setter
    def frontend_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="transportProtocol")
    def transport_protocol(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TransportProtocol]]]: ...
    @transport_protocol.setter
    def transport_protocol(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TransportProtocol]]]
    ): ...

class LabAnnouncementPropertiesArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[Union[_builtins.str, EnableStatus]]]
    expiration_date: NotRequired[pulumi.Input[_builtins.str]]
    expired: NotRequired[pulumi.Input[_builtins.bool]]
    markdown: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LabAnnouncementPropertiesArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]] = ...,
        expiration_date: Optional[pulumi.Input[_builtins.str]] = ...,
        expired: Optional[pulumi.Input[_builtins.bool]] = ...,
        markdown: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]]: ...
    @enabled.setter
    def enabled(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiration_date.setter
    def expiration_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def expired(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @expired.setter
    def expired(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def markdown(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @markdown.setter
    def markdown(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LabSupportPropertiesArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[Union[_builtins.str, EnableStatus]]]
    markdown: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LabSupportPropertiesArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]] = ...,
        markdown: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]]: ...
    @enabled.setter
    def enabled(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def markdown(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @markdown.setter
    def markdown(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LabVirtualMachineCreationParameterArgsDict(TypedDict):
    allow_claim: NotRequired[pulumi.Input[_builtins.bool]]
    artifacts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ArtifactInstallPropertiesArgsDict]]]
    ]
    bulk_creation_parameters: NotRequired[pulumi.Input[BulkCreationParametersArgsDict]]
    created_date: NotRequired[pulumi.Input[_builtins.str]]
    custom_image_id: NotRequired[pulumi.Input[_builtins.str]]
    data_disk_parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DataDiskPropertiesArgsDict]]]
    ]
    disallow_public_ip_address: NotRequired[pulumi.Input[_builtins.bool]]
    environment_id: NotRequired[pulumi.Input[_builtins.str]]
    expiration_date: NotRequired[pulumi.Input[_builtins.str]]
    gallery_image_reference: NotRequired[pulumi.Input[GalleryImageReferenceArgsDict]]
    is_authentication_with_ssh_key: NotRequired[pulumi.Input[_builtins.bool]]
    lab_subnet_name: NotRequired[pulumi.Input[_builtins.str]]
    lab_virtual_network_id: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    network_interface: NotRequired[pulumi.Input[NetworkInterfacePropertiesArgsDict]]
    notes: NotRequired[pulumi.Input[_builtins.str]]
    owner_object_id: NotRequired[pulumi.Input[_builtins.str]]
    owner_user_principal_name: NotRequired[pulumi.Input[_builtins.str]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    plan_id: NotRequired[pulumi.Input[_builtins.str]]
    schedule_parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ScheduleCreationParameterArgsDict]]]
    ]
    size: NotRequired[pulumi.Input[_builtins.str]]
    ssh_key: NotRequired[pulumi.Input[_builtins.str]]
    storage_type: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LabVirtualMachineCreationParameterArgs:
    def __init__(
        __self__,
        *,
        allow_claim: Optional[pulumi.Input[_builtins.bool]] = ...,
        artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[ArtifactInstallPropertiesArgs]]]
        ] = ...,
        bulk_creation_parameters: Optional[
            pulumi.Input[BulkCreationParametersArgs]
        ] = ...,
        created_date: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_image_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_disk_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[DataDiskPropertiesArgs]]]
        ] = ...,
        disallow_public_ip_address: Optional[pulumi.Input[_builtins.bool]] = ...,
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        expiration_date: Optional[pulumi.Input[_builtins.str]] = ...,
        gallery_image_reference: Optional[
            pulumi.Input[GalleryImageReferenceArgs]
        ] = ...,
        is_authentication_with_ssh_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        lab_subnet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        lab_virtual_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface: Optional[pulumi.Input[NetworkInterfacePropertiesArgs]] = ...,
        notes: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_object_id: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_user_principal_name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ScheduleCreationParameterArgs]]]
        ] = ...,
        size: Optional[pulumi.Input[_builtins.str]] = ...,
        ssh_key: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowClaim")
    def allow_claim(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_claim.setter
    def allow_claim(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def artifacts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ArtifactInstallPropertiesArgs]]]
    ]: ...
    @artifacts.setter
    def artifacts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ArtifactInstallPropertiesArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bulkCreationParameters")
    def bulk_creation_parameters(
        self,
    ) -> Optional[pulumi.Input[BulkCreationParametersArgs]]: ...
    @bulk_creation_parameters.setter
    def bulk_creation_parameters(
        self, value: Optional[pulumi.Input[BulkCreationParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customImageId")
    def custom_image_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_image_id.setter
    def custom_image_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataDiskParameters")
    def data_disk_parameters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskPropertiesArgs]]]]: ...
    @data_disk_parameters.setter
    def data_disk_parameters(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskPropertiesArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="disallowPublicIpAddress")
    def disallow_public_ip_address(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disallow_public_ip_address.setter
    def disallow_public_ip_address(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiration_date.setter
    def expiration_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="galleryImageReference")
    def gallery_image_reference(
        self,
    ) -> Optional[pulumi.Input[GalleryImageReferenceArgs]]: ...
    @gallery_image_reference.setter
    def gallery_image_reference(
        self, value: Optional[pulumi.Input[GalleryImageReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isAuthenticationWithSshKey")
    def is_authentication_with_ssh_key(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_authentication_with_ssh_key.setter
    def is_authentication_with_ssh_key(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="labSubnetName")
    def lab_subnet_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lab_subnet_name.setter
    def lab_subnet_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="labVirtualNetworkId")
    def lab_virtual_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lab_virtual_network_id.setter
    def lab_virtual_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterface")
    def network_interface(
        self,
    ) -> Optional[pulumi.Input[NetworkInterfacePropertiesArgs]]: ...
    @network_interface.setter
    def network_interface(
        self, value: Optional[pulumi.Input[NetworkInterfacePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notes.setter
    def notes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerObjectId")
    def owner_object_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_object_id.setter
    def owner_object_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerUserPrincipalName")
    def owner_user_principal_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_user_principal_name.setter
    def owner_user_principal_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plan_id.setter
    def plan_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleParameters")
    def schedule_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ScheduleCreationParameterArgs]]]
    ]: ...
    @schedule_parameters.setter
    def schedule_parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ScheduleCreationParameterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sshKey")
    def ssh_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssh_key.setter
    def ssh_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LinuxOsInfoArgsDict(TypedDict):
    linux_os_state: NotRequired[pulumi.Input[Union[_builtins.str, LinuxOsState]]]

@pulumi.input_type
class LinuxOsInfoArgs:
    def __init__(
        __self__,
        *,
        linux_os_state: Optional[
            pulumi.Input[Union[_builtins.str, LinuxOsState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linuxOsState")
    def linux_os_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LinuxOsState]]]: ...
    @linux_os_state.setter
    def linux_os_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LinuxOsState]]]
    ): ...

class NetworkInterfacePropertiesArgsDict(TypedDict):
    dns_name: NotRequired[pulumi.Input[_builtins.str]]
    private_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    public_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    public_ip_address_id: NotRequired[pulumi.Input[_builtins.str]]
    rdp_authority: NotRequired[pulumi.Input[_builtins.str]]
    shared_public_ip_address_configuration: NotRequired[
        pulumi.Input[SharedPublicIpAddressConfigurationArgsDict]
    ]
    ssh_authority: NotRequired[pulumi.Input[_builtins.str]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    virtual_network_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkInterfacePropertiesArgs:
    def __init__(
        __self__,
        *,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        public_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        public_ip_address_id: Optional[pulumi.Input[_builtins.str]] = ...,
        rdp_authority: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_public_ip_address_configuration: Optional[
            pulumi.Input[SharedPublicIpAddressConfigurationArgs]
        ] = ...,
        ssh_authority: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_ip_address.setter
    def public_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicIpAddressId")
    def public_ip_address_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_ip_address_id.setter
    def public_ip_address_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rdpAuthority")
    def rdp_authority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rdp_authority.setter
    def rdp_authority(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedPublicIpAddressConfiguration")
    def shared_public_ip_address_configuration(
        self,
    ) -> Optional[pulumi.Input[SharedPublicIpAddressConfigurationArgs]]: ...
    @shared_public_ip_address_configuration.setter
    def shared_public_ip_address_configuration(
        self, value: Optional[pulumi.Input[SharedPublicIpAddressConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sshAuthority")
    def ssh_authority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssh_authority.setter
    def ssh_authority(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_network_id.setter
    def virtual_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NotificationSettingsArgsDict(TypedDict):
    email_recipient: NotRequired[pulumi.Input[_builtins.str]]
    notification_locale: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, EnableStatus]]]
    time_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    webhook_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NotificationSettingsArgs:
    def __init__(
        __self__,
        *,
        email_recipient: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_locale: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]] = ...,
        time_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        webhook_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailRecipient")
    def email_recipient(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_recipient.setter
    def email_recipient(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationLocale")
    def notification_locale(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_locale.setter
    def notification_locale(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeInMinutes")
    def time_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @time_in_minutes.setter
    def time_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="webhookUrl")
    def webhook_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @webhook_url.setter
    def webhook_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PortArgsDict(TypedDict):
    backend_port: NotRequired[pulumi.Input[_builtins.int]]
    transport_protocol: NotRequired[
        pulumi.Input[Union[_builtins.str, TransportProtocol]]
    ]

@pulumi.input_type
class PortArgs:
    def __init__(
        __self__,
        *,
        backend_port: Optional[pulumi.Input[_builtins.int]] = ...,
        transport_protocol: Optional[
            pulumi.Input[Union[_builtins.str, TransportProtocol]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @backend_port.setter
    def backend_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="transportProtocol")
    def transport_protocol(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TransportProtocol]]]: ...
    @transport_protocol.setter
    def transport_protocol(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TransportProtocol]]]
    ): ...

class ScheduleCreationParameterArgsDict(TypedDict):
    daily_recurrence: NotRequired[pulumi.Input[DayDetailsArgsDict]]
    hourly_recurrence: NotRequired[pulumi.Input[HourDetailsArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    notification_settings: NotRequired[pulumi.Input[NotificationSettingsArgsDict]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, EnableStatus]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    target_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    task_type: NotRequired[pulumi.Input[_builtins.str]]
    time_zone_id: NotRequired[pulumi.Input[_builtins.str]]
    weekly_recurrence: NotRequired[pulumi.Input[WeekDetailsArgsDict]]

@pulumi.input_type
class ScheduleCreationParameterArgs:
    def __init__(
        __self__,
        *,
        daily_recurrence: Optional[pulumi.Input[DayDetailsArgs]] = ...,
        hourly_recurrence: Optional[pulumi.Input[HourDetailsArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_settings: Optional[pulumi.Input[NotificationSettingsArgs]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        task_type: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_recurrence: Optional[pulumi.Input[WeekDetailsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dailyRecurrence")
    def daily_recurrence(self) -> Optional[pulumi.Input[DayDetailsArgs]]: ...
    @daily_recurrence.setter
    def daily_recurrence(self, value: Optional[pulumi.Input[DayDetailsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="hourlyRecurrence")
    def hourly_recurrence(self) -> Optional[pulumi.Input[HourDetailsArgs]]: ...
    @hourly_recurrence.setter
    def hourly_recurrence(self, value: Optional[pulumi.Input[HourDetailsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(
        self,
    ) -> Optional[pulumi.Input[NotificationSettingsArgs]]: ...
    @notification_settings.setter
    def notification_settings(
        self, value: Optional[pulumi.Input[NotificationSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EnableStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_id.setter
    def target_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @task_type.setter
    def task_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone_id.setter
    def time_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="weeklyRecurrence")
    def weekly_recurrence(self) -> Optional[pulumi.Input[WeekDetailsArgs]]: ...
    @weekly_recurrence.setter
    def weekly_recurrence(self, value: Optional[pulumi.Input[WeekDetailsArgs]]): ...

class SharedPublicIpAddressConfigurationArgsDict(TypedDict):
    inbound_nat_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InboundNatRuleArgsDict]]]
    ]

@pulumi.input_type
class SharedPublicIpAddressConfigurationArgs:
    def __init__(
        __self__,
        *,
        inbound_nat_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[InboundNatRuleArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inboundNatRules")
    def inbound_nat_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[InboundNatRuleArgs]]]]: ...
    @inbound_nat_rules.setter
    def inbound_nat_rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InboundNatRuleArgs]]]]
    ): ...

class SubnetOverrideArgsDict(TypedDict):
    lab_subnet_name: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]
    shared_public_ip_address_configuration: NotRequired[
        pulumi.Input[SubnetSharedPublicIpAddressConfigurationArgsDict]
    ]
    use_in_vm_creation_permission: NotRequired[
        pulumi.Input[Union[_builtins.str, UsagePermissionType]]
    ]
    use_public_ip_address_permission: NotRequired[
        pulumi.Input[Union[_builtins.str, UsagePermissionType]]
    ]
    virtual_network_pool_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SubnetOverrideArgs:
    def __init__(
        __self__,
        *,
        lab_subnet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_public_ip_address_configuration: Optional[
            pulumi.Input[SubnetSharedPublicIpAddressConfigurationArgs]
        ] = ...,
        use_in_vm_creation_permission: Optional[
            pulumi.Input[Union[_builtins.str, UsagePermissionType]]
        ] = ...,
        use_public_ip_address_permission: Optional[
            pulumi.Input[Union[_builtins.str, UsagePermissionType]]
        ] = ...,
        virtual_network_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="labSubnetName")
    def lab_subnet_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lab_subnet_name.setter
    def lab_subnet_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedPublicIpAddressConfiguration")
    def shared_public_ip_address_configuration(
        self,
    ) -> Optional[pulumi.Input[SubnetSharedPublicIpAddressConfigurationArgs]]: ...
    @shared_public_ip_address_configuration.setter
    def shared_public_ip_address_configuration(
        self,
        value: Optional[pulumi.Input[SubnetSharedPublicIpAddressConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="useInVmCreationPermission")
    def use_in_vm_creation_permission(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, UsagePermissionType]]]: ...
    @use_in_vm_creation_permission.setter
    def use_in_vm_creation_permission(
        self, value: Optional[pulumi.Input[Union[_builtins.str, UsagePermissionType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="usePublicIpAddressPermission")
    def use_public_ip_address_permission(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, UsagePermissionType]]]: ...
    @use_public_ip_address_permission.setter
    def use_public_ip_address_permission(
        self, value: Optional[pulumi.Input[Union[_builtins.str, UsagePermissionType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkPoolName")
    def virtual_network_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_network_pool_name.setter
    def virtual_network_pool_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class SubnetSharedPublicIpAddressConfigurationArgsDict(TypedDict):
    allowed_ports: NotRequired[pulumi.Input[Sequence[pulumi.Input[PortArgsDict]]]]

@pulumi.input_type
class SubnetSharedPublicIpAddressConfigurationArgs:
    def __init__(
        __self__,
        *,
        allowed_ports: Optional[pulumi.Input[Sequence[pulumi.Input[PortArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedPorts")
    def allowed_ports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PortArgs]]]]: ...
    @allowed_ports.setter
    def allowed_ports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PortArgs]]]]
    ): ...

class SubnetArgsDict(TypedDict):
    allow_public_ip: NotRequired[
        pulumi.Input[Union[_builtins.str, UsagePermissionType]]
    ]
    lab_subnet_name: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SubnetArgs:
    def __init__(
        __self__,
        *,
        allow_public_ip: Optional[
            pulumi.Input[Union[_builtins.str, UsagePermissionType]]
        ] = ...,
        lab_subnet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPublicIp")
    def allow_public_ip(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, UsagePermissionType]]]: ...
    @allow_public_ip.setter
    def allow_public_ip(
        self, value: Optional[pulumi.Input[Union[_builtins.str, UsagePermissionType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="labSubnetName")
    def lab_subnet_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lab_subnet_name.setter
    def lab_subnet_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserIdentityArgsDict(TypedDict):
    app_id: NotRequired[pulumi.Input[_builtins.str]]
    object_id: NotRequired[pulumi.Input[_builtins.str]]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]
    principal_name: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserIdentityArgs:
    def __init__(
        __self__,
        *,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        object_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalName")
    def principal_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_name.setter
    def principal_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserSecretStoreArgsDict(TypedDict):
    key_vault_id: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserSecretStoreArgs:
    def __init__(
        __self__,
        *,
        key_vault_id: Optional[pulumi.Input[_builtins.str]] = ...,
        key_vault_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_id.setter
    def key_vault_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_uri.setter
    def key_vault_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WeekDetailsArgsDict(TypedDict):
    time: NotRequired[pulumi.Input[_builtins.str]]
    weekdays: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WeekDetailsArgs:
    def __init__(
        __self__,
        *,
        time: Optional[pulumi.Input[_builtins.str]] = ...,
        weekdays: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time.setter
    def time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def weekdays(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @weekdays.setter
    def weekdays(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class WindowsOsInfoArgsDict(TypedDict):
    windows_os_state: NotRequired[pulumi.Input[Union[_builtins.str, WindowsOsState]]]

@pulumi.input_type
class WindowsOsInfoArgs:
    def __init__(
        __self__,
        *,
        windows_os_state: Optional[
            pulumi.Input[Union[_builtins.str, WindowsOsState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="windowsOsState")
    def windows_os_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, WindowsOsState]]]: ...
    @windows_os_state.setter
    def windows_os_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, WindowsOsState]]]
    ): ...
