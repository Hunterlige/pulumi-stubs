import builtins as _builtins
import sys
import pulumi
from typing import Any, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApplicationPackageReferenceArgs",
    "ApplicationPackageReferenceArgsDict",
    "AutoScaleSettingsArgs",
    "AutoScaleSettingsArgsDict",
    "AutoStorageBasePropertiesArgs",
    "AutoStorageBasePropertiesArgsDict",
    "AutoUserSpecificationArgs",
    "AutoUserSpecificationArgsDict",
    "AutomaticOSUpgradePolicyArgs",
    "AutomaticOSUpgradePolicyArgsDict",
    "AzureBlobFileSystemConfigurationArgs",
    "AzureBlobFileSystemConfigurationArgsDict",
    "AzureFileShareConfigurationArgs",
    "AzureFileShareConfigurationArgsDict",
    "BatchAccountIdentityArgs",
    "BatchAccountIdentityArgsDict",
    "BatchPoolIdentityArgs",
    "BatchPoolIdentityArgsDict",
    "CIFSMountConfigurationArgs",
    "CIFSMountConfigurationArgsDict",
    "CertificateReferenceArgs",
    "CertificateReferenceArgsDict",
    "ComputeNodeIdentityReferenceArgs",
    "ComputeNodeIdentityReferenceArgsDict",
    "ContainerConfigurationArgs",
    "ContainerConfigurationArgsDict",
    "ContainerHostBatchBindMountEntryArgs",
    "ContainerHostBatchBindMountEntryArgsDict",
    "ContainerRegistryArgs",
    "ContainerRegistryArgsDict",
    "DataDiskArgs",
    "DataDiskArgsDict",
    "DeploymentConfigurationArgs",
    "DeploymentConfigurationArgsDict",
    "DiffDiskSettingsArgs",
    "DiffDiskSettingsArgsDict",
    "DiskEncryptionConfigurationArgs",
    "DiskEncryptionConfigurationArgsDict",
    "EncryptionPropertiesArgs",
    "EncryptionPropertiesArgsDict",
    "EndpointAccessProfileArgs",
    "EndpointAccessProfileArgsDict",
    "EnvironmentSettingArgs",
    "EnvironmentSettingArgsDict",
    "FixedScaleSettingsArgs",
    "FixedScaleSettingsArgsDict",
    "IPRuleArgs",
    "IPRuleArgsDict",
    "ImageReferenceArgs",
    "ImageReferenceArgsDict",
    "InboundNatPoolArgs",
    "InboundNatPoolArgsDict",
    "KeyVaultPropertiesArgs",
    "KeyVaultPropertiesArgsDict",
    "KeyVaultReferenceArgs",
    "KeyVaultReferenceArgsDict",
    "LinuxUserConfigurationArgs",
    "LinuxUserConfigurationArgsDict",
    "ManagedDiskArgs",
    "ManagedDiskArgsDict",
    "MetadataItemArgs",
    "MetadataItemArgsDict",
    "MountConfigurationArgs",
    "MountConfigurationArgsDict",
    "NFSMountConfigurationArgs",
    "NFSMountConfigurationArgsDict",
    "NetworkConfigurationArgs",
    "NetworkConfigurationArgsDict",
    "NetworkProfileArgs",
    "NetworkProfileArgsDict",
    "NetworkSecurityGroupRuleArgs",
    "NetworkSecurityGroupRuleArgsDict",
    "NodePlacementConfigurationArgs",
    "NodePlacementConfigurationArgsDict",
    "OSDiskArgs",
    "OSDiskArgsDict",
    "PoolEndpointConfigurationArgs",
    "PoolEndpointConfigurationArgsDict",
    "PublicIPAddressConfigurationArgs",
    "PublicIPAddressConfigurationArgsDict",
    "ResourceFileArgs",
    "ResourceFileArgsDict",
    "RollingUpgradePolicyArgs",
    "RollingUpgradePolicyArgsDict",
    "ScaleSettingsArgs",
    "ScaleSettingsArgsDict",
    "SecurityProfileArgs",
    "SecurityProfileArgsDict",
    "ServiceArtifactReferenceArgs",
    "ServiceArtifactReferenceArgsDict",
    "StartTaskArgs",
    "StartTaskArgsDict",
    "TaskContainerSettingsArgs",
    "TaskContainerSettingsArgsDict",
    "TaskSchedulingPolicyArgs",
    "TaskSchedulingPolicyArgsDict",
    "UefiSettingsArgs",
    "UefiSettingsArgsDict",
    "UpgradePolicyArgs",
    "UpgradePolicyArgsDict",
    "UserAccountArgs",
    "UserAccountArgsDict",
    "UserIdentityArgs",
    "UserIdentityArgsDict",
    "VMDiskSecurityProfileArgs",
    "VMDiskSecurityProfileArgsDict",
    "VMExtensionArgs",
    "VMExtensionArgsDict",
    "VirtualMachineConfigurationArgs",
    "VirtualMachineConfigurationArgsDict",
    "WindowsConfigurationArgs",
    "WindowsConfigurationArgsDict",
    "WindowsUserConfigurationArgs",
    "WindowsUserConfigurationArgsDict",
]

class ApplicationPackageReferenceArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApplicationPackageReferenceArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutoScaleSettingsArgsDict(TypedDict):
    formula: pulumi.Input[_builtins.str]
    evaluation_interval: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutoScaleSettingsArgs:
    def __init__(
        __self__,
        *,
        formula: pulumi.Input[_builtins.str],
        evaluation_interval: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def formula(self) -> pulumi.Input[_builtins.str]: ...
    @formula.setter
    def formula(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="evaluationInterval")
    def evaluation_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @evaluation_interval.setter
    def evaluation_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutoStorageBasePropertiesArgsDict(TypedDict):
    storage_account_id: pulumi.Input[_builtins.str]
    authentication_mode: NotRequired[pulumi.Input[AutoStorageAuthenticationMode]]
    node_identity_reference: NotRequired[
        pulumi.Input[ComputeNodeIdentityReferenceArgsDict]
    ]

@pulumi.input_type
class AutoStorageBasePropertiesArgs:
    def __init__(
        __self__,
        *,
        storage_account_id: pulumi.Input[_builtins.str],
        authentication_mode: Optional[
            pulumi.Input[AutoStorageAuthenticationMode]
        ] = ...,
        node_identity_reference: Optional[
            pulumi.Input[ComputeNodeIdentityReferenceArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @storage_account_id.setter
    def storage_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(
        self,
    ) -> Optional[pulumi.Input[AutoStorageAuthenticationMode]]: ...
    @authentication_mode.setter
    def authentication_mode(
        self, value: Optional[pulumi.Input[AutoStorageAuthenticationMode]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeIdentityReference")
    def node_identity_reference(
        self,
    ) -> Optional[pulumi.Input[ComputeNodeIdentityReferenceArgs]]: ...
    @node_identity_reference.setter
    def node_identity_reference(
        self, value: Optional[pulumi.Input[ComputeNodeIdentityReferenceArgs]]
    ): ...

class AutoUserSpecificationArgsDict(TypedDict):
    elevation_level: NotRequired[pulumi.Input[ElevationLevel]]
    scope: NotRequired[pulumi.Input[AutoUserScope]]

@pulumi.input_type
class AutoUserSpecificationArgs:
    def __init__(
        __self__,
        *,
        elevation_level: Optional[pulumi.Input[ElevationLevel]] = ...,
        scope: Optional[pulumi.Input[AutoUserScope]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="elevationLevel")
    def elevation_level(self) -> Optional[pulumi.Input[ElevationLevel]]: ...
    @elevation_level.setter
    def elevation_level(self, value: Optional[pulumi.Input[ElevationLevel]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[AutoUserScope]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[AutoUserScope]]): ...

class AutomaticOSUpgradePolicyArgsDict(TypedDict):
    disable_automatic_rollback: NotRequired[pulumi.Input[_builtins.bool]]
    enable_automatic_os_upgrade: NotRequired[pulumi.Input[_builtins.bool]]
    os_rolling_upgrade_deferral: NotRequired[pulumi.Input[_builtins.bool]]
    use_rolling_upgrade_policy: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AutomaticOSUpgradePolicyArgs:
    def __init__(
        __self__,
        *,
        disable_automatic_rollback: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_automatic_os_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        os_rolling_upgrade_deferral: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_rolling_upgrade_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableAutomaticRollback")
    def disable_automatic_rollback(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_automatic_rollback.setter
    def disable_automatic_rollback(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableAutomaticOSUpgrade")
    def enable_automatic_os_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_automatic_os_upgrade.setter
    def enable_automatic_os_upgrade(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="osRollingUpgradeDeferral")
    def os_rolling_upgrade_deferral(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @os_rolling_upgrade_deferral.setter
    def os_rolling_upgrade_deferral(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useRollingUpgradePolicy")
    def use_rolling_upgrade_policy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_rolling_upgrade_policy.setter
    def use_rolling_upgrade_policy(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AzureBlobFileSystemConfigurationArgsDict(TypedDict):
    account_name: pulumi.Input[_builtins.str]
    container_name: pulumi.Input[_builtins.str]
    relative_mount_path: pulumi.Input[_builtins.str]
    account_key: NotRequired[pulumi.Input[_builtins.str]]
    blobfuse_options: NotRequired[pulumi.Input[_builtins.str]]
    identity_reference: NotRequired[pulumi.Input[ComputeNodeIdentityReferenceArgsDict]]
    sas_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureBlobFileSystemConfigurationArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        container_name: pulumi.Input[_builtins.str],
        relative_mount_path: pulumi.Input[_builtins.str],
        account_key: Optional[pulumi.Input[_builtins.str]] = ...,
        blobfuse_options: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_reference: Optional[
            pulumi.Input[ComputeNodeIdentityReferenceArgs]
        ] = ...,
        sas_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[_builtins.str]: ...
    @container_name.setter
    def container_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="relativeMountPath")
    def relative_mount_path(self) -> pulumi.Input[_builtins.str]: ...
    @relative_mount_path.setter
    def relative_mount_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_key.setter
    def account_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="blobfuseOptions")
    def blobfuse_options(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @blobfuse_options.setter
    def blobfuse_options(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityReference")
    def identity_reference(
        self,
    ) -> Optional[pulumi.Input[ComputeNodeIdentityReferenceArgs]]: ...
    @identity_reference.setter
    def identity_reference(
        self, value: Optional[pulumi.Input[ComputeNodeIdentityReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sasKey")
    def sas_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sas_key.setter
    def sas_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureFileShareConfigurationArgsDict(TypedDict):
    account_key: pulumi.Input[_builtins.str]
    account_name: pulumi.Input[_builtins.str]
    azure_file_url: pulumi.Input[_builtins.str]
    relative_mount_path: pulumi.Input[_builtins.str]
    mount_options: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureFileShareConfigurationArgs:
    def __init__(
        __self__,
        *,
        account_key: pulumi.Input[_builtins.str],
        account_name: pulumi.Input[_builtins.str],
        azure_file_url: pulumi.Input[_builtins.str],
        relative_mount_path: pulumi.Input[_builtins.str],
        mount_options: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> pulumi.Input[_builtins.str]: ...
    @account_key.setter
    def account_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="azureFileUrl")
    def azure_file_url(self) -> pulumi.Input[_builtins.str]: ...
    @azure_file_url.setter
    def azure_file_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="relativeMountPath")
    def relative_mount_path(self) -> pulumi.Input[_builtins.str]: ...
    @relative_mount_path.setter
    def relative_mount_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mount_options.setter
    def mount_options(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BatchAccountIdentityArgsDict(TypedDict):
    type: pulumi.Input[ResourceIdentityType]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class BatchAccountIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[ResourceIdentityType],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[ResourceIdentityType]: ...
    @type.setter
    def type(self, value: pulumi.Input[ResourceIdentityType]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BatchPoolIdentityArgsDict(TypedDict):
    type: pulumi.Input[PoolIdentityType]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class BatchPoolIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[PoolIdentityType],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[PoolIdentityType]: ...
    @type.setter
    def type(self, value: pulumi.Input[PoolIdentityType]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CIFSMountConfigurationArgsDict(TypedDict):
    password: pulumi.Input[_builtins.str]
    relative_mount_path: pulumi.Input[_builtins.str]
    source: pulumi.Input[_builtins.str]
    user_name: pulumi.Input[_builtins.str]
    mount_options: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CIFSMountConfigurationArgs:
    def __init__(
        __self__,
        *,
        password: pulumi.Input[_builtins.str],
        relative_mount_path: pulumi.Input[_builtins.str],
        source: pulumi.Input[_builtins.str],
        user_name: pulumi.Input[_builtins.str],
        mount_options: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]: ...
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="relativeMountPath")
    def relative_mount_path(self) -> pulumi.Input[_builtins.str]: ...
    @relative_mount_path.setter
    def relative_mount_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[_builtins.str]: ...
    @user_name.setter
    def user_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mount_options.setter
    def mount_options(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateReferenceArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    store_location: NotRequired[pulumi.Input[CertificateStoreLocation]]
    store_name: NotRequired[pulumi.Input[_builtins.str]]
    visibility: NotRequired[pulumi.Input[Sequence[pulumi.Input[CertificateVisibility]]]]

@pulumi.input_type
class CertificateReferenceArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        store_location: Optional[pulumi.Input[CertificateStoreLocation]] = ...,
        store_name: Optional[pulumi.Input[_builtins.str]] = ...,
        visibility: Optional[
            pulumi.Input[Sequence[pulumi.Input[CertificateVisibility]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storeLocation")
    def store_location(self) -> Optional[pulumi.Input[CertificateStoreLocation]]: ...
    @store_location.setter
    def store_location(
        self, value: Optional[pulumi.Input[CertificateStoreLocation]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storeName")
    def store_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @store_name.setter
    def store_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def visibility(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CertificateVisibility]]]]: ...
    @visibility.setter
    def visibility(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateVisibility]]]],
    ): ...

class ComputeNodeIdentityReferenceArgsDict(TypedDict):
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ComputeNodeIdentityReferenceArgs:
    def __init__(
        __self__, *, resource_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ContainerConfigurationArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ContainerType]]
    container_image_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    container_registries: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ContainerRegistryArgsDict]]]
    ]

@pulumi.input_type
class ContainerConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ContainerType]],
        container_image_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        container_registries: Optional[
            pulumi.Input[Sequence[pulumi.Input[ContainerRegistryArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ContainerType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ContainerType]]): ...
    @_builtins.property
    @pulumi.getter(name="containerImageNames")
    def container_image_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @container_image_names.setter
    def container_image_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerRegistries")
    def container_registries(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ContainerRegistryArgs]]]]: ...
    @container_registries.setter
    def container_registries(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerRegistryArgs]]]],
    ): ...

class ContainerHostBatchBindMountEntryArgsDict(TypedDict):
    is_read_only: NotRequired[pulumi.Input[_builtins.bool]]
    source: NotRequired[pulumi.Input[Union[_builtins.str, ContainerHostDataPath]]]

@pulumi.input_type
class ContainerHostBatchBindMountEntryArgs:
    def __init__(
        __self__,
        *,
        is_read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        source: Optional[
            pulumi.Input[Union[_builtins.str, ContainerHostDataPath]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isReadOnly")
    def is_read_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_read_only.setter
    def is_read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ContainerHostDataPath]]]: ...
    @source.setter
    def source(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ContainerHostDataPath]]]
    ): ...

class ContainerRegistryArgsDict(TypedDict):
    identity_reference: NotRequired[pulumi.Input[ComputeNodeIdentityReferenceArgsDict]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    registry_server: NotRequired[pulumi.Input[_builtins.str]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ContainerRegistryArgs:
    def __init__(
        __self__,
        *,
        identity_reference: Optional[
            pulumi.Input[ComputeNodeIdentityReferenceArgs]
        ] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_server: Optional[pulumi.Input[_builtins.str]] = ...,
        user_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityReference")
    def identity_reference(
        self,
    ) -> Optional[pulumi.Input[ComputeNodeIdentityReferenceArgs]]: ...
    @identity_reference.setter
    def identity_reference(
        self, value: Optional[pulumi.Input[ComputeNodeIdentityReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registryServer")
    def registry_server(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registry_server.setter
    def registry_server(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataDiskArgsDict(TypedDict):
    disk_size_gb: pulumi.Input[_builtins.int]
    lun: pulumi.Input[_builtins.int]
    caching: NotRequired[pulumi.Input[CachingType]]
    storage_account_type: NotRequired[pulumi.Input[StorageAccountType]]

@pulumi.input_type
class DataDiskArgs:
    def __init__(
        __self__,
        *,
        disk_size_gb: pulumi.Input[_builtins.int],
        lun: pulumi.Input[_builtins.int],
        caching: Optional[pulumi.Input[CachingType]] = ...,
        storage_account_type: Optional[pulumi.Input[StorageAccountType]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> pulumi.Input[_builtins.int]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def lun(self) -> pulumi.Input[_builtins.int]: ...
    @lun.setter
    def lun(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[pulumi.Input[CachingType]]: ...
    @caching.setter
    def caching(self, value: Optional[pulumi.Input[CachingType]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[pulumi.Input[StorageAccountType]]: ...
    @storage_account_type.setter
    def storage_account_type(
        self, value: Optional[pulumi.Input[StorageAccountType]]
    ): ...

class DeploymentConfigurationArgsDict(TypedDict):
    virtual_machine_configuration: NotRequired[
        pulumi.Input[VirtualMachineConfigurationArgsDict]
    ]

@pulumi.input_type
class DeploymentConfigurationArgs:
    def __init__(
        __self__,
        *,
        virtual_machine_configuration: Optional[
            pulumi.Input[VirtualMachineConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineConfiguration")
    def virtual_machine_configuration(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineConfigurationArgs]]: ...
    @virtual_machine_configuration.setter
    def virtual_machine_configuration(
        self, value: Optional[pulumi.Input[VirtualMachineConfigurationArgs]]
    ): ...

class DiffDiskSettingsArgsDict(TypedDict):
    placement: NotRequired[pulumi.Input[DiffDiskPlacement]]

@pulumi.input_type
class DiffDiskSettingsArgs:
    def __init__(
        __self__, *, placement: Optional[pulumi.Input[DiffDiskPlacement]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def placement(self) -> Optional[pulumi.Input[DiffDiskPlacement]]: ...
    @placement.setter
    def placement(self, value: Optional[pulumi.Input[DiffDiskPlacement]]): ...

class DiskEncryptionConfigurationArgsDict(TypedDict):
    targets: NotRequired[pulumi.Input[Sequence[pulumi.Input[DiskEncryptionTarget]]]]

@pulumi.input_type
class DiskEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[DiskEncryptionTarget]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def targets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DiskEncryptionTarget]]]]: ...
    @targets.setter
    def targets(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DiskEncryptionTarget]]]],
    ): ...

class EncryptionPropertiesArgsDict(TypedDict):
    key_source: NotRequired[pulumi.Input[KeySource]]
    key_vault_properties: NotRequired[pulumi.Input[KeyVaultPropertiesArgsDict]]

@pulumi.input_type
class EncryptionPropertiesArgs:
    def __init__(
        __self__,
        *,
        key_source: Optional[pulumi.Input[KeySource]] = ...,
        key_vault_properties: Optional[pulumi.Input[KeyVaultPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keySource")
    def key_source(self) -> Optional[pulumi.Input[KeySource]]: ...
    @key_source.setter
    def key_source(self, value: Optional[pulumi.Input[KeySource]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(
        self,
    ) -> Optional[pulumi.Input[KeyVaultPropertiesArgs]]: ...
    @key_vault_properties.setter
    def key_vault_properties(
        self, value: Optional[pulumi.Input[KeyVaultPropertiesArgs]]
    ): ...

class EndpointAccessProfileArgsDict(TypedDict):
    default_action: pulumi.Input[EndpointAccessDefaultAction]
    ip_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[IPRuleArgsDict]]]]

@pulumi.input_type
class EndpointAccessProfileArgs:
    def __init__(
        __self__,
        *,
        default_action: pulumi.Input[EndpointAccessDefaultAction],
        ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[IPRuleArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Input[EndpointAccessDefaultAction]: ...
    @default_action.setter
    def default_action(self, value: pulumi.Input[EndpointAccessDefaultAction]): ...
    @_builtins.property
    @pulumi.getter(name="ipRules")
    def ip_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IPRuleArgs]]]]: ...
    @ip_rules.setter
    def ip_rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IPRuleArgs]]]]
    ): ...

class EnvironmentSettingArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EnvironmentSettingArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FixedScaleSettingsArgsDict(TypedDict):
    node_deallocation_option: NotRequired[pulumi.Input[ComputeNodeDeallocationOption]]
    resize_timeout: NotRequired[pulumi.Input[_builtins.str]]
    target_dedicated_nodes: NotRequired[pulumi.Input[_builtins.int]]
    target_low_priority_nodes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class FixedScaleSettingsArgs:
    def __init__(
        __self__,
        *,
        node_deallocation_option: Optional[
            pulumi.Input[ComputeNodeDeallocationOption]
        ] = ...,
        resize_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        target_dedicated_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
        target_low_priority_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeDeallocationOption")
    def node_deallocation_option(
        self,
    ) -> Optional[pulumi.Input[ComputeNodeDeallocationOption]]: ...
    @node_deallocation_option.setter
    def node_deallocation_option(
        self, value: Optional[pulumi.Input[ComputeNodeDeallocationOption]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resizeTimeout")
    def resize_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resize_timeout.setter
    def resize_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetDedicatedNodes")
    def target_dedicated_nodes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_dedicated_nodes.setter
    def target_dedicated_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="targetLowPriorityNodes")
    def target_low_priority_nodes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_low_priority_nodes.setter
    def target_low_priority_nodes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class IPRuleArgsDict(TypedDict):
    action: pulumi.Input[IPRuleAction]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class IPRuleArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[IPRuleAction],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[IPRuleAction]: ...
    @action.setter
    def action(self, value: pulumi.Input[IPRuleAction]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ImageReferenceArgsDict(TypedDict):
    community_gallery_image_id: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    offer: NotRequired[pulumi.Input[_builtins.str]]
    publisher: NotRequired[pulumi.Input[_builtins.str]]
    shared_gallery_image_id: NotRequired[pulumi.Input[_builtins.str]]
    sku: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageReferenceArgs:
    def __init__(
        __self__,
        *,
        community_gallery_image_id: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        offer: Optional[pulumi.Input[_builtins.str]] = ...,
        publisher: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_gallery_image_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="communityGalleryImageId")
    def community_gallery_image_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @community_gallery_image_id.setter
    def community_gallery_image_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
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
    @_builtins.property
    @pulumi.getter(name="sharedGalleryImageId")
    def shared_gallery_image_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shared_gallery_image_id.setter
    def shared_gallery_image_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

class InboundNatPoolArgsDict(TypedDict):
    backend_port: pulumi.Input[_builtins.int]
    frontend_port_range_end: pulumi.Input[_builtins.int]
    frontend_port_range_start: pulumi.Input[_builtins.int]
    name: pulumi.Input[_builtins.str]
    protocol: pulumi.Input[InboundEndpointProtocol]
    network_security_group_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NetworkSecurityGroupRuleArgsDict]]]
    ]

@pulumi.input_type
class InboundNatPoolArgs:
    def __init__(
        __self__,
        *,
        backend_port: pulumi.Input[_builtins.int],
        frontend_port_range_end: pulumi.Input[_builtins.int],
        frontend_port_range_start: pulumi.Input[_builtins.int],
        name: pulumi.Input[_builtins.str],
        protocol: pulumi.Input[InboundEndpointProtocol],
        network_security_group_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[NetworkSecurityGroupRuleArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> pulumi.Input[_builtins.int]: ...
    @backend_port.setter
    def backend_port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="frontendPortRangeEnd")
    def frontend_port_range_end(self) -> pulumi.Input[_builtins.int]: ...
    @frontend_port_range_end.setter
    def frontend_port_range_end(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="frontendPortRangeStart")
    def frontend_port_range_start(self) -> pulumi.Input[_builtins.int]: ...
    @frontend_port_range_start.setter
    def frontend_port_range_start(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[InboundEndpointProtocol]: ...
    @protocol.setter
    def protocol(self, value: pulumi.Input[InboundEndpointProtocol]): ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroupRules")
    def network_security_group_rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NetworkSecurityGroupRuleArgs]]]
    ]: ...
    @network_security_group_rules.setter
    def network_security_group_rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NetworkSecurityGroupRuleArgs]]]
        ],
    ): ...

class KeyVaultPropertiesArgsDict(TypedDict):
    key_identifier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(
        __self__, *, key_identifier: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyIdentifier")
    def key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_identifier.setter
    def key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KeyVaultReferenceArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    url: pulumi.Input[_builtins.str]

@pulumi.input_type
class KeyVaultReferenceArgs:
    def __init__(
        __self__, *, id: pulumi.Input[_builtins.str], url: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...

class LinuxUserConfigurationArgsDict(TypedDict):
    gid: NotRequired[pulumi.Input[_builtins.int]]
    ssh_private_key: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class LinuxUserConfigurationArgs:
    def __init__(
        __self__,
        *,
        gid: Optional[pulumi.Input[_builtins.int]] = ...,
        ssh_private_key: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gid(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @gid.setter
    def gid(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="sshPrivateKey")
    def ssh_private_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssh_private_key.setter
    def ssh_private_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ManagedDiskArgsDict(TypedDict):
    security_profile: NotRequired[pulumi.Input[VMDiskSecurityProfileArgsDict]]
    storage_account_type: NotRequired[pulumi.Input[StorageAccountType]]

@pulumi.input_type
class ManagedDiskArgs:
    def __init__(
        __self__,
        *,
        security_profile: Optional[pulumi.Input[VMDiskSecurityProfileArgs]] = ...,
        storage_account_type: Optional[pulumi.Input[StorageAccountType]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input[VMDiskSecurityProfileArgs]]: ...
    @security_profile.setter
    def security_profile(
        self, value: Optional[pulumi.Input[VMDiskSecurityProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[pulumi.Input[StorageAccountType]]: ...
    @storage_account_type.setter
    def storage_account_type(
        self, value: Optional[pulumi.Input[StorageAccountType]]
    ): ...

class MetadataItemArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class MetadataItemArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class MountConfigurationArgsDict(TypedDict):
    azure_blob_file_system_configuration: NotRequired[
        pulumi.Input[AzureBlobFileSystemConfigurationArgsDict]
    ]
    azure_file_share_configuration: NotRequired[
        pulumi.Input[AzureFileShareConfigurationArgsDict]
    ]
    cifs_mount_configuration: NotRequired[pulumi.Input[CIFSMountConfigurationArgsDict]]
    nfs_mount_configuration: NotRequired[pulumi.Input[NFSMountConfigurationArgsDict]]

@pulumi.input_type
class MountConfigurationArgs:
    def __init__(
        __self__,
        *,
        azure_blob_file_system_configuration: Optional[
            pulumi.Input[AzureBlobFileSystemConfigurationArgs]
        ] = ...,
        azure_file_share_configuration: Optional[
            pulumi.Input[AzureFileShareConfigurationArgs]
        ] = ...,
        cifs_mount_configuration: Optional[
            pulumi.Input[CIFSMountConfigurationArgs]
        ] = ...,
        nfs_mount_configuration: Optional[
            pulumi.Input[NFSMountConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureBlobFileSystemConfiguration")
    def azure_blob_file_system_configuration(
        self,
    ) -> Optional[pulumi.Input[AzureBlobFileSystemConfigurationArgs]]: ...
    @azure_blob_file_system_configuration.setter
    def azure_blob_file_system_configuration(
        self, value: Optional[pulumi.Input[AzureBlobFileSystemConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureFileShareConfiguration")
    def azure_file_share_configuration(
        self,
    ) -> Optional[pulumi.Input[AzureFileShareConfigurationArgs]]: ...
    @azure_file_share_configuration.setter
    def azure_file_share_configuration(
        self, value: Optional[pulumi.Input[AzureFileShareConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cifsMountConfiguration")
    def cifs_mount_configuration(
        self,
    ) -> Optional[pulumi.Input[CIFSMountConfigurationArgs]]: ...
    @cifs_mount_configuration.setter
    def cifs_mount_configuration(
        self, value: Optional[pulumi.Input[CIFSMountConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nfsMountConfiguration")
    def nfs_mount_configuration(
        self,
    ) -> Optional[pulumi.Input[NFSMountConfigurationArgs]]: ...
    @nfs_mount_configuration.setter
    def nfs_mount_configuration(
        self, value: Optional[pulumi.Input[NFSMountConfigurationArgs]]
    ): ...

class NFSMountConfigurationArgsDict(TypedDict):
    relative_mount_path: pulumi.Input[_builtins.str]
    source: pulumi.Input[_builtins.str]
    mount_options: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NFSMountConfigurationArgs:
    def __init__(
        __self__,
        *,
        relative_mount_path: pulumi.Input[_builtins.str],
        source: pulumi.Input[_builtins.str],
        mount_options: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="relativeMountPath")
    def relative_mount_path(self) -> pulumi.Input[_builtins.str]: ...
    @relative_mount_path.setter
    def relative_mount_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mount_options.setter
    def mount_options(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkConfigurationArgsDict(TypedDict):
    dynamic_vnet_assignment_scope: NotRequired[pulumi.Input[DynamicVNetAssignmentScope]]
    enable_accelerated_networking: NotRequired[pulumi.Input[_builtins.bool]]
    endpoint_configuration: NotRequired[pulumi.Input[PoolEndpointConfigurationArgsDict]]
    public_ip_address_configuration: NotRequired[
        pulumi.Input[PublicIPAddressConfigurationArgsDict]
    ]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        dynamic_vnet_assignment_scope: Optional[
            pulumi.Input[DynamicVNetAssignmentScope]
        ] = ...,
        enable_accelerated_networking: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint_configuration: Optional[
            pulumi.Input[PoolEndpointConfigurationArgs]
        ] = ...,
        public_ip_address_configuration: Optional[
            pulumi.Input[PublicIPAddressConfigurationArgs]
        ] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dynamicVnetAssignmentScope")
    def dynamic_vnet_assignment_scope(
        self,
    ) -> Optional[pulumi.Input[DynamicVNetAssignmentScope]]: ...
    @dynamic_vnet_assignment_scope.setter
    def dynamic_vnet_assignment_scope(
        self, value: Optional[pulumi.Input[DynamicVNetAssignmentScope]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_accelerated_networking.setter
    def enable_accelerated_networking(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointConfiguration")
    def endpoint_configuration(
        self,
    ) -> Optional[pulumi.Input[PoolEndpointConfigurationArgs]]: ...
    @endpoint_configuration.setter
    def endpoint_configuration(
        self, value: Optional[pulumi.Input[PoolEndpointConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddressConfiguration")
    def public_ip_address_configuration(
        self,
    ) -> Optional[pulumi.Input[PublicIPAddressConfigurationArgs]]: ...
    @public_ip_address_configuration.setter
    def public_ip_address_configuration(
        self, value: Optional[pulumi.Input[PublicIPAddressConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkProfileArgsDict(TypedDict):
    account_access: NotRequired[pulumi.Input[EndpointAccessProfileArgsDict]]
    node_management_access: NotRequired[pulumi.Input[EndpointAccessProfileArgsDict]]

@pulumi.input_type
class NetworkProfileArgs:
    def __init__(
        __self__,
        *,
        account_access: Optional[pulumi.Input[EndpointAccessProfileArgs]] = ...,
        node_management_access: Optional[pulumi.Input[EndpointAccessProfileArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountAccess")
    def account_access(self) -> Optional[pulumi.Input[EndpointAccessProfileArgs]]: ...
    @account_access.setter
    def account_access(
        self, value: Optional[pulumi.Input[EndpointAccessProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeManagementAccess")
    def node_management_access(
        self,
    ) -> Optional[pulumi.Input[EndpointAccessProfileArgs]]: ...
    @node_management_access.setter
    def node_management_access(
        self, value: Optional[pulumi.Input[EndpointAccessProfileArgs]]
    ): ...

class NetworkSecurityGroupRuleArgsDict(TypedDict):
    access: pulumi.Input[NetworkSecurityGroupRuleAccess]
    priority: pulumi.Input[_builtins.int]
    source_address_prefix: pulumi.Input[_builtins.str]
    source_port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class NetworkSecurityGroupRuleArgs:
    def __init__(
        __self__,
        *,
        access: pulumi.Input[NetworkSecurityGroupRuleAccess],
        priority: pulumi.Input[_builtins.int],
        source_address_prefix: pulumi.Input[_builtins.str],
        source_port_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def access(self) -> pulumi.Input[NetworkSecurityGroupRuleAccess]: ...
    @access.setter
    def access(self, value: pulumi.Input[NetworkSecurityGroupRuleAccess]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="sourceAddressPrefix")
    def source_address_prefix(self) -> pulumi.Input[_builtins.str]: ...
    @source_address_prefix.setter
    def source_address_prefix(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @source_port_ranges.setter
    def source_port_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class NodePlacementConfigurationArgsDict(TypedDict):
    policy: NotRequired[pulumi.Input[NodePlacementPolicyType]]

@pulumi.input_type
class NodePlacementConfigurationArgs:
    def __init__(
        __self__, *, policy: Optional[pulumi.Input[NodePlacementPolicyType]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[NodePlacementPolicyType]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[NodePlacementPolicyType]]): ...

class OSDiskArgsDict(TypedDict):
    caching: NotRequired[pulumi.Input[CachingType]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    ephemeral_os_disk_settings: NotRequired[pulumi.Input[DiffDiskSettingsArgsDict]]
    managed_disk: NotRequired[pulumi.Input[ManagedDiskArgsDict]]
    write_accelerator_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class OSDiskArgs:
    def __init__(
        __self__,
        *,
        caching: Optional[pulumi.Input[CachingType]] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        ephemeral_os_disk_settings: Optional[pulumi.Input[DiffDiskSettingsArgs]] = ...,
        managed_disk: Optional[pulumi.Input[ManagedDiskArgs]] = ...,
        write_accelerator_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def caching(self) -> Optional[pulumi.Input[CachingType]]: ...
    @caching.setter
    def caching(self, value: Optional[pulumi.Input[CachingType]]): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralOSDiskSettings")
    def ephemeral_os_disk_settings(
        self,
    ) -> Optional[pulumi.Input[DiffDiskSettingsArgs]]: ...
    @ephemeral_os_disk_settings.setter
    def ephemeral_os_disk_settings(
        self, value: Optional[pulumi.Input[DiffDiskSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(self) -> Optional[pulumi.Input[ManagedDiskArgs]]: ...
    @managed_disk.setter
    def managed_disk(self, value: Optional[pulumi.Input[ManagedDiskArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="writeAcceleratorEnabled")
    def write_accelerator_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @write_accelerator_enabled.setter
    def write_accelerator_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class PoolEndpointConfigurationArgsDict(TypedDict):
    inbound_nat_pools: pulumi.Input[Sequence[pulumi.Input[InboundNatPoolArgsDict]]]

@pulumi.input_type
class PoolEndpointConfigurationArgs:
    def __init__(
        __self__,
        *,
        inbound_nat_pools: pulumi.Input[Sequence[pulumi.Input[InboundNatPoolArgs]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inboundNatPools")
    def inbound_nat_pools(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[InboundNatPoolArgs]]]: ...
    @inbound_nat_pools.setter
    def inbound_nat_pools(
        self, value: pulumi.Input[Sequence[pulumi.Input[InboundNatPoolArgs]]]
    ): ...

class PublicIPAddressConfigurationArgsDict(TypedDict):
    ip_address_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    provision: NotRequired[pulumi.Input[IPAddressProvisioningType]]

@pulumi.input_type
class PublicIPAddressConfigurationArgs:
    def __init__(
        __self__,
        *,
        ip_address_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        provision: Optional[pulumi.Input[IPAddressProvisioningType]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressIds")
    def ip_address_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ip_address_ids.setter
    def ip_address_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def provision(self) -> Optional[pulumi.Input[IPAddressProvisioningType]]: ...
    @provision.setter
    def provision(self, value: Optional[pulumi.Input[IPAddressProvisioningType]]): ...

class ResourceFileArgsDict(TypedDict):
    auto_storage_container_name: NotRequired[pulumi.Input[_builtins.str]]
    blob_prefix: NotRequired[pulumi.Input[_builtins.str]]
    file_mode: NotRequired[pulumi.Input[_builtins.str]]
    file_path: NotRequired[pulumi.Input[_builtins.str]]
    http_url: NotRequired[pulumi.Input[_builtins.str]]
    identity_reference: NotRequired[pulumi.Input[ComputeNodeIdentityReferenceArgsDict]]
    storage_container_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceFileArgs:
    def __init__(
        __self__,
        *,
        auto_storage_container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        blob_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        file_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        http_url: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_reference: Optional[
            pulumi.Input[ComputeNodeIdentityReferenceArgs]
        ] = ...,
        storage_container_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoStorageContainerName")
    def auto_storage_container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_storage_container_name.setter
    def auto_storage_container_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="blobPrefix")
    def blob_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @blob_prefix.setter
    def blob_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileMode")
    def file_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_mode.setter
    def file_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_path.setter
    def file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpUrl")
    def http_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @http_url.setter
    def http_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityReference")
    def identity_reference(
        self,
    ) -> Optional[pulumi.Input[ComputeNodeIdentityReferenceArgs]]: ...
    @identity_reference.setter
    def identity_reference(
        self, value: Optional[pulumi.Input[ComputeNodeIdentityReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageContainerUrl")
    def storage_container_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_container_url.setter
    def storage_container_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RollingUpgradePolicyArgsDict(TypedDict):
    enable_cross_zone_upgrade: NotRequired[pulumi.Input[_builtins.bool]]
    max_batch_instance_percent: NotRequired[pulumi.Input[_builtins.int]]
    max_unhealthy_instance_percent: NotRequired[pulumi.Input[_builtins.int]]
    max_unhealthy_upgraded_instance_percent: NotRequired[pulumi.Input[_builtins.int]]
    pause_time_between_batches: NotRequired[pulumi.Input[_builtins.str]]
    prioritize_unhealthy_instances: NotRequired[pulumi.Input[_builtins.bool]]
    rollback_failed_instances_on_policy_breach: NotRequired[
        pulumi.Input[_builtins.bool]
    ]

@pulumi.input_type
class RollingUpgradePolicyArgs:
    def __init__(
        __self__,
        *,
        enable_cross_zone_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_batch_instance_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        max_unhealthy_instance_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        max_unhealthy_upgraded_instance_percent: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        pause_time_between_batches: Optional[pulumi.Input[_builtins.str]] = ...,
        prioritize_unhealthy_instances: Optional[pulumi.Input[_builtins.bool]] = ...,
        rollback_failed_instances_on_policy_breach: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableCrossZoneUpgrade")
    def enable_cross_zone_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_cross_zone_upgrade.setter
    def enable_cross_zone_upgrade(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxBatchInstancePercent")
    def max_batch_instance_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_batch_instance_percent.setter
    def max_batch_instance_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxUnhealthyInstancePercent")
    def max_unhealthy_instance_percent(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_unhealthy_instance_percent.setter
    def max_unhealthy_instance_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxUnhealthyUpgradedInstancePercent")
    def max_unhealthy_upgraded_instance_percent(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_unhealthy_upgraded_instance_percent.setter
    def max_unhealthy_upgraded_instance_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pauseTimeBetweenBatches")
    def pause_time_between_batches(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pause_time_between_batches.setter
    def pause_time_between_batches(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="prioritizeUnhealthyInstances")
    def prioritize_unhealthy_instances(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @prioritize_unhealthy_instances.setter
    def prioritize_unhealthy_instances(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rollbackFailedInstancesOnPolicyBreach")
    def rollback_failed_instances_on_policy_breach(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @rollback_failed_instances_on_policy_breach.setter
    def rollback_failed_instances_on_policy_breach(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ScaleSettingsArgsDict(TypedDict):
    auto_scale: NotRequired[pulumi.Input[AutoScaleSettingsArgsDict]]
    fixed_scale: NotRequired[pulumi.Input[FixedScaleSettingsArgsDict]]

@pulumi.input_type
class ScaleSettingsArgs:
    def __init__(
        __self__,
        *,
        auto_scale: Optional[pulumi.Input[AutoScaleSettingsArgs]] = ...,
        fixed_scale: Optional[pulumi.Input[FixedScaleSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoScale")
    def auto_scale(self) -> Optional[pulumi.Input[AutoScaleSettingsArgs]]: ...
    @auto_scale.setter
    def auto_scale(self, value: Optional[pulumi.Input[AutoScaleSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="fixedScale")
    def fixed_scale(self) -> Optional[pulumi.Input[FixedScaleSettingsArgs]]: ...
    @fixed_scale.setter
    def fixed_scale(self, value: Optional[pulumi.Input[FixedScaleSettingsArgs]]): ...

class SecurityProfileArgsDict(TypedDict):
    encryption_at_host: NotRequired[pulumi.Input[_builtins.bool]]
    security_type: NotRequired[pulumi.Input[SecurityTypes]]
    uefi_settings: NotRequired[pulumi.Input[UefiSettingsArgsDict]]

@pulumi.input_type
class SecurityProfileArgs:
    def __init__(
        __self__,
        *,
        encryption_at_host: Optional[pulumi.Input[_builtins.bool]] = ...,
        security_type: Optional[pulumi.Input[SecurityTypes]] = ...,
        uefi_settings: Optional[pulumi.Input[UefiSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encryption_at_host.setter
    def encryption_at_host(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="securityType")
    def security_type(self) -> Optional[pulumi.Input[SecurityTypes]]: ...
    @security_type.setter
    def security_type(self, value: Optional[pulumi.Input[SecurityTypes]]): ...
    @_builtins.property
    @pulumi.getter(name="uefiSettings")
    def uefi_settings(self) -> Optional[pulumi.Input[UefiSettingsArgs]]: ...
    @uefi_settings.setter
    def uefi_settings(self, value: Optional[pulumi.Input[UefiSettingsArgs]]): ...

class ServiceArtifactReferenceArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServiceArtifactReferenceArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...

class StartTaskArgsDict(TypedDict):
    command_line: NotRequired[pulumi.Input[_builtins.str]]
    container_settings: NotRequired[pulumi.Input[TaskContainerSettingsArgsDict]]
    environment_settings: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[EnvironmentSettingArgsDict]]]
    ]
    max_task_retry_count: NotRequired[pulumi.Input[_builtins.int]]
    resource_files: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceFileArgsDict]]]
    ]
    user_identity: NotRequired[pulumi.Input[UserIdentityArgsDict]]
    wait_for_success: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class StartTaskArgs:
    def __init__(
        __self__,
        *,
        command_line: Optional[pulumi.Input[_builtins.str]] = ...,
        container_settings: Optional[pulumi.Input[TaskContainerSettingsArgs]] = ...,
        environment_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentSettingArgs]]]
        ] = ...,
        max_task_retry_count: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_files: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceFileArgs]]]
        ] = ...,
        user_identity: Optional[pulumi.Input[UserIdentityArgs]] = ...,
        wait_for_success: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commandLine")
    def command_line(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @command_line.setter
    def command_line(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerSettings")
    def container_settings(
        self,
    ) -> Optional[pulumi.Input[TaskContainerSettingsArgs]]: ...
    @container_settings.setter
    def container_settings(
        self, value: Optional[pulumi.Input[TaskContainerSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentSettings")
    def environment_settings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentSettingArgs]]]]: ...
    @environment_settings.setter
    def environment_settings(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentSettingArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxTaskRetryCount")
    def max_task_retry_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_task_retry_count.setter
    def max_task_retry_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceFiles")
    def resource_files(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceFileArgs]]]]: ...
    @resource_files.setter
    def resource_files(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceFileArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userIdentity")
    def user_identity(self) -> Optional[pulumi.Input[UserIdentityArgs]]: ...
    @user_identity.setter
    def user_identity(self, value: Optional[pulumi.Input[UserIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="waitForSuccess")
    def wait_for_success(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wait_for_success.setter
    def wait_for_success(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TaskContainerSettingsArgsDict(TypedDict):
    image_name: pulumi.Input[_builtins.str]
    container_host_batch_bind_mounts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ContainerHostBatchBindMountEntryArgsDict]]]
    ]
    container_run_options: NotRequired[pulumi.Input[_builtins.str]]
    registry: NotRequired[pulumi.Input[ContainerRegistryArgsDict]]
    working_directory: NotRequired[pulumi.Input[ContainerWorkingDirectory]]

@pulumi.input_type
class TaskContainerSettingsArgs:
    def __init__(
        __self__,
        *,
        image_name: pulumi.Input[_builtins.str],
        container_host_batch_bind_mounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[ContainerHostBatchBindMountEntryArgs]]]
        ] = ...,
        container_run_options: Optional[pulumi.Input[_builtins.str]] = ...,
        registry: Optional[pulumi.Input[ContainerRegistryArgs]] = ...,
        working_directory: Optional[pulumi.Input[ContainerWorkingDirectory]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[_builtins.str]: ...
    @image_name.setter
    def image_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="containerHostBatchBindMounts")
    def container_host_batch_bind_mounts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ContainerHostBatchBindMountEntryArgs]]]
    ]: ...
    @container_host_batch_bind_mounts.setter
    def container_host_batch_bind_mounts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ContainerHostBatchBindMountEntryArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerRunOptions")
    def container_run_options(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_run_options.setter
    def container_run_options(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def registry(self) -> Optional[pulumi.Input[ContainerRegistryArgs]]: ...
    @registry.setter
    def registry(self, value: Optional[pulumi.Input[ContainerRegistryArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="workingDirectory")
    def working_directory(
        self,
    ) -> Optional[pulumi.Input[ContainerWorkingDirectory]]: ...
    @working_directory.setter
    def working_directory(
        self, value: Optional[pulumi.Input[ContainerWorkingDirectory]]
    ): ...

class TaskSchedulingPolicyArgsDict(TypedDict):
    node_fill_type: pulumi.Input[ComputeNodeFillType]

@pulumi.input_type
class TaskSchedulingPolicyArgs:
    def __init__(
        __self__, *, node_fill_type: Optional[pulumi.Input[ComputeNodeFillType]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeFillType")
    def node_fill_type(self) -> pulumi.Input[ComputeNodeFillType]: ...
    @node_fill_type.setter
    def node_fill_type(self, value: pulumi.Input[ComputeNodeFillType]): ...

class UefiSettingsArgsDict(TypedDict):
    secure_boot_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    v_tpm_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class UefiSettingsArgs:
    def __init__(
        __self__,
        *,
        secure_boot_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        v_tpm_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secureBootEnabled")
    def secure_boot_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @secure_boot_enabled.setter
    def secure_boot_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="vTpmEnabled")
    def v_tpm_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @v_tpm_enabled.setter
    def v_tpm_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class UpgradePolicyArgsDict(TypedDict):
    mode: pulumi.Input[UpgradeMode]
    automatic_os_upgrade_policy: NotRequired[
        pulumi.Input[AutomaticOSUpgradePolicyArgsDict]
    ]
    rolling_upgrade_policy: NotRequired[pulumi.Input[RollingUpgradePolicyArgsDict]]

@pulumi.input_type
class UpgradePolicyArgs:
    def __init__(
        __self__,
        *,
        mode: pulumi.Input[UpgradeMode],
        automatic_os_upgrade_policy: Optional[
            pulumi.Input[AutomaticOSUpgradePolicyArgs]
        ] = ...,
        rolling_upgrade_policy: Optional[pulumi.Input[RollingUpgradePolicyArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[UpgradeMode]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[UpgradeMode]): ...
    @_builtins.property
    @pulumi.getter(name="automaticOSUpgradePolicy")
    def automatic_os_upgrade_policy(
        self,
    ) -> Optional[pulumi.Input[AutomaticOSUpgradePolicyArgs]]: ...
    @automatic_os_upgrade_policy.setter
    def automatic_os_upgrade_policy(
        self, value: Optional[pulumi.Input[AutomaticOSUpgradePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rollingUpgradePolicy")
    def rolling_upgrade_policy(
        self,
    ) -> Optional[pulumi.Input[RollingUpgradePolicyArgs]]: ...
    @rolling_upgrade_policy.setter
    def rolling_upgrade_policy(
        self, value: Optional[pulumi.Input[RollingUpgradePolicyArgs]]
    ): ...

class UserAccountArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    password: pulumi.Input[_builtins.str]
    elevation_level: NotRequired[pulumi.Input[ElevationLevel]]
    linux_user_configuration: NotRequired[pulumi.Input[LinuxUserConfigurationArgsDict]]
    windows_user_configuration: NotRequired[
        pulumi.Input[WindowsUserConfigurationArgsDict]
    ]

@pulumi.input_type
class UserAccountArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        password: pulumi.Input[_builtins.str],
        elevation_level: Optional[pulumi.Input[ElevationLevel]] = ...,
        linux_user_configuration: Optional[
            pulumi.Input[LinuxUserConfigurationArgs]
        ] = ...,
        windows_user_configuration: Optional[
            pulumi.Input[WindowsUserConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]: ...
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="elevationLevel")
    def elevation_level(self) -> Optional[pulumi.Input[ElevationLevel]]: ...
    @elevation_level.setter
    def elevation_level(self, value: Optional[pulumi.Input[ElevationLevel]]): ...
    @_builtins.property
    @pulumi.getter(name="linuxUserConfiguration")
    def linux_user_configuration(
        self,
    ) -> Optional[pulumi.Input[LinuxUserConfigurationArgs]]: ...
    @linux_user_configuration.setter
    def linux_user_configuration(
        self, value: Optional[pulumi.Input[LinuxUserConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="windowsUserConfiguration")
    def windows_user_configuration(
        self,
    ) -> Optional[pulumi.Input[WindowsUserConfigurationArgs]]: ...
    @windows_user_configuration.setter
    def windows_user_configuration(
        self, value: Optional[pulumi.Input[WindowsUserConfigurationArgs]]
    ): ...

class UserIdentityArgsDict(TypedDict):
    auto_user: NotRequired[pulumi.Input[AutoUserSpecificationArgsDict]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserIdentityArgs:
    def __init__(
        __self__,
        *,
        auto_user: Optional[pulumi.Input[AutoUserSpecificationArgs]] = ...,
        user_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoUser")
    def auto_user(self) -> Optional[pulumi.Input[AutoUserSpecificationArgs]]: ...
    @auto_user.setter
    def auto_user(self, value: Optional[pulumi.Input[AutoUserSpecificationArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VMDiskSecurityProfileArgsDict(TypedDict):
    security_encryption_type: NotRequired[
        pulumi.Input[Union[_builtins.str, SecurityEncryptionTypes]]
    ]

@pulumi.input_type
class VMDiskSecurityProfileArgs:
    def __init__(
        __self__,
        *,
        security_encryption_type: Optional[
            pulumi.Input[Union[_builtins.str, SecurityEncryptionTypes]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityEncryptionType")
    def security_encryption_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SecurityEncryptionTypes]]]: ...
    @security_encryption_type.setter
    def security_encryption_type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, SecurityEncryptionTypes]]],
    ): ...

class VMExtensionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    publisher: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    auto_upgrade_minor_version: NotRequired[pulumi.Input[_builtins.bool]]
    enable_automatic_upgrade: NotRequired[pulumi.Input[_builtins.bool]]
    protected_settings: NotRequired[Any]
    provision_after_extensions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    settings: NotRequired[Any]
    type_handler_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VMExtensionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        publisher: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        auto_upgrade_minor_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_automatic_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        protected_settings: Optional[Any] = ...,
        provision_after_extensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        settings: Optional[Any] = ...,
        type_handler_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> pulumi.Input[_builtins.str]: ...
    @publisher.setter
    def publisher(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_upgrade_minor_version.setter
    def auto_upgrade_minor_version(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_automatic_upgrade.setter
    def enable_automatic_upgrade(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]: ...
    @protected_settings.setter
    def protected_settings(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="provisionAfterExtensions")
    def provision_after_extensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @provision_after_extensions.setter
    def provision_after_extensions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Any]: ...
    @settings.setter
    def settings(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_handler_version.setter
    def type_handler_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualMachineConfigurationArgsDict(TypedDict):
    image_reference: pulumi.Input[ImageReferenceArgsDict]
    node_agent_sku_id: pulumi.Input[_builtins.str]
    container_configuration: NotRequired[pulumi.Input[ContainerConfigurationArgsDict]]
    data_disks: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataDiskArgsDict]]]]
    disk_encryption_configuration: NotRequired[
        pulumi.Input[DiskEncryptionConfigurationArgsDict]
    ]
    extensions: NotRequired[pulumi.Input[Sequence[pulumi.Input[VMExtensionArgsDict]]]]
    license_type: NotRequired[pulumi.Input[_builtins.str]]
    node_placement_configuration: NotRequired[
        pulumi.Input[NodePlacementConfigurationArgsDict]
    ]
    os_disk: NotRequired[pulumi.Input[OSDiskArgsDict]]
    security_profile: NotRequired[pulumi.Input[SecurityProfileArgsDict]]
    service_artifact_reference: NotRequired[
        pulumi.Input[ServiceArtifactReferenceArgsDict]
    ]
    windows_configuration: NotRequired[pulumi.Input[WindowsConfigurationArgsDict]]

@pulumi.input_type
class VirtualMachineConfigurationArgs:
    def __init__(
        __self__,
        *,
        image_reference: pulumi.Input[ImageReferenceArgs],
        node_agent_sku_id: pulumi.Input[_builtins.str],
        container_configuration: Optional[
            pulumi.Input[ContainerConfigurationArgs]
        ] = ...,
        data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskArgs]]]] = ...,
        disk_encryption_configuration: Optional[
            pulumi.Input[DiskEncryptionConfigurationArgs]
        ] = ...,
        extensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMExtensionArgs]]]
        ] = ...,
        license_type: Optional[pulumi.Input[_builtins.str]] = ...,
        node_placement_configuration: Optional[
            pulumi.Input[NodePlacementConfigurationArgs]
        ] = ...,
        os_disk: Optional[pulumi.Input[OSDiskArgs]] = ...,
        security_profile: Optional[pulumi.Input[SecurityProfileArgs]] = ...,
        service_artifact_reference: Optional[
            pulumi.Input[ServiceArtifactReferenceArgs]
        ] = ...,
        windows_configuration: Optional[pulumi.Input[WindowsConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> pulumi.Input[ImageReferenceArgs]: ...
    @image_reference.setter
    def image_reference(self, value: pulumi.Input[ImageReferenceArgs]): ...
    @_builtins.property
    @pulumi.getter(name="nodeAgentSkuId")
    def node_agent_sku_id(self) -> pulumi.Input[_builtins.str]: ...
    @node_agent_sku_id.setter
    def node_agent_sku_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="containerConfiguration")
    def container_configuration(
        self,
    ) -> Optional[pulumi.Input[ContainerConfigurationArgs]]: ...
    @container_configuration.setter
    def container_configuration(
        self, value: Optional[pulumi.Input[ContainerConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskArgs]]]]: ...
    @data_disks.setter
    def data_disks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataDiskArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionConfiguration")
    def disk_encryption_configuration(
        self,
    ) -> Optional[pulumi.Input[DiskEncryptionConfigurationArgs]]: ...
    @disk_encryption_configuration.setter
    def disk_encryption_configuration(
        self, value: Optional[pulumi.Input[DiskEncryptionConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VMExtensionArgs]]]]: ...
    @extensions.setter
    def extensions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VMExtensionArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @license_type.setter
    def license_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodePlacementConfiguration")
    def node_placement_configuration(
        self,
    ) -> Optional[pulumi.Input[NodePlacementConfigurationArgs]]: ...
    @node_placement_configuration.setter
    def node_placement_configuration(
        self, value: Optional[pulumi.Input[NodePlacementConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="osDisk")
    def os_disk(self) -> Optional[pulumi.Input[OSDiskArgs]]: ...
    @os_disk.setter
    def os_disk(self, value: Optional[pulumi.Input[OSDiskArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input[SecurityProfileArgs]]: ...
    @security_profile.setter
    def security_profile(self, value: Optional[pulumi.Input[SecurityProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceArtifactReference")
    def service_artifact_reference(
        self,
    ) -> Optional[pulumi.Input[ServiceArtifactReferenceArgs]]: ...
    @service_artifact_reference.setter
    def service_artifact_reference(
        self, value: Optional[pulumi.Input[ServiceArtifactReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="windowsConfiguration")
    def windows_configuration(
        self,
    ) -> Optional[pulumi.Input[WindowsConfigurationArgs]]: ...
    @windows_configuration.setter
    def windows_configuration(
        self, value: Optional[pulumi.Input[WindowsConfigurationArgs]]
    ): ...

class WindowsConfigurationArgsDict(TypedDict):
    enable_automatic_updates: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class WindowsConfigurationArgs:
    def __init__(
        __self__,
        *,
        enable_automatic_updates: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpdates")
    def enable_automatic_updates(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_automatic_updates.setter
    def enable_automatic_updates(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class WindowsUserConfigurationArgsDict(TypedDict):
    login_mode: NotRequired[pulumi.Input[LoginMode]]

@pulumi.input_type
class WindowsUserConfigurationArgs:
    def __init__(
        __self__, *, login_mode: Optional[pulumi.Input[LoginMode]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loginMode")
    def login_mode(self) -> Optional[pulumi.Input[LoginMode]]: ...
    @login_mode.setter
    def login_mode(self, value: Optional[pulumi.Input[LoginMode]]): ...
