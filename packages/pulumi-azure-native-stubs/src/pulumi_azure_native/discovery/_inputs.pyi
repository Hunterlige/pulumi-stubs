import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AzureNetAppFilesStoreArgs",
    "AzureNetAppFilesStoreArgsDict",
    "AzureStorageBlobStoreArgs",
    "AzureStorageBlobStoreArgsDict",
    "BookshelfKeyVaultPropertiesArgs",
    "BookshelfKeyVaultPropertiesArgsDict",
    "BookshelfPropertiesArgs",
    "BookshelfPropertiesArgsDict",
    "ChatModelDeploymentPropertiesArgs",
    "ChatModelDeploymentPropertiesArgsDict",
    "IdentityArgs",
    "IdentityArgsDict",
    "KeyVaultPropertiesArgs",
    "KeyVaultPropertiesArgsDict",
    "NodePoolPropertiesArgs",
    "NodePoolPropertiesArgsDict",
    "PrivateEndpointConnectionPropertiesArgs",
    "PrivateEndpointConnectionPropertiesArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "ProjectPropertiesArgs",
    "ProjectPropertiesArgsDict",
    "ProjectSettingsArgs",
    "ProjectSettingsArgsDict",
    "StorageAssetPropertiesArgs",
    "StorageAssetPropertiesArgsDict",
    "StorageContainerPropertiesArgs",
    "StorageContainerPropertiesArgsDict",
    "SupercomputerIdentitiesArgs",
    "SupercomputerIdentitiesArgsDict",
    "SupercomputerPropertiesArgs",
    "SupercomputerPropertiesArgsDict",
    "ToolPropertiesArgs",
    "ToolPropertiesArgsDict",
    "WorkspacePropertiesArgs",
    "WorkspacePropertiesArgsDict",
]

class AzureNetAppFilesStoreArgsDict(TypedDict):
    kind: pulumi.Input[_builtins.str]
    net_app_volume_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureNetAppFilesStoreArgs:
    def __init__(
        __self__,
        *,
        kind: pulumi.Input[_builtins.str],
        net_app_volume_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="netAppVolumeId")
    def net_app_volume_id(self) -> pulumi.Input[_builtins.str]: ...
    @net_app_volume_id.setter
    def net_app_volume_id(self, value: pulumi.Input[_builtins.str]): ...

class AzureStorageBlobStoreArgsDict(TypedDict):
    kind: pulumi.Input[_builtins.str]
    storage_account_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureStorageBlobStoreArgs:
    def __init__(
        __self__,
        *,
        kind: pulumi.Input[_builtins.str],
        storage_account_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @storage_account_id.setter
    def storage_account_id(self, value: pulumi.Input[_builtins.str]): ...

class BookshelfKeyVaultPropertiesArgsDict(TypedDict):
    identity_client_id: pulumi.Input[_builtins.str]
    key_name: pulumi.Input[_builtins.str]
    key_vault_uri: pulumi.Input[_builtins.str]
    key_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BookshelfKeyVaultPropertiesArgs:
    def __init__(
        __self__,
        *,
        identity_client_id: pulumi.Input[_builtins.str],
        key_name: pulumi.Input[_builtins.str],
        key_vault_uri: pulumi.Input[_builtins.str],
        key_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> pulumi.Input[_builtins.str]: ...
    @identity_client_id.setter
    def identity_client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[_builtins.str]: ...
    @key_name.setter
    def key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> pulumi.Input[_builtins.str]: ...
    @key_vault_uri.setter
    def key_vault_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_version.setter
    def key_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BookshelfPropertiesArgsDict(TypedDict):
    customer_managed_keys: NotRequired[
        pulumi.Input[Union[_builtins.str, CustomerManagedKeys]]
    ]
    key_vault_properties: NotRequired[pulumi.Input[BookshelfKeyVaultPropertiesArgsDict]]
    log_analytics_cluster_id: NotRequired[pulumi.Input[_builtins.str]]
    private_endpoint_subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
    ]
    search_subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    workload_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class BookshelfPropertiesArgs:
    def __init__(
        __self__,
        *,
        customer_managed_keys: Optional[
            pulumi.Input[Union[_builtins.str, CustomerManagedKeys]]
        ] = ...,
        key_vault_properties: Optional[
            pulumi.Input[BookshelfKeyVaultPropertiesArgs]
        ] = ...,
        log_analytics_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        private_endpoint_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        search_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKeys")
    def customer_managed_keys(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CustomerManagedKeys]]]: ...
    @customer_managed_keys.setter
    def customer_managed_keys(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CustomerManagedKeys]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(
        self,
    ) -> Optional[pulumi.Input[BookshelfKeyVaultPropertiesArgs]]: ...
    @key_vault_properties.setter
    def key_vault_properties(
        self, value: Optional[pulumi.Input[BookshelfKeyVaultPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logAnalyticsClusterId")
    def log_analytics_cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_analytics_cluster_id.setter
    def log_analytics_cluster_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointSubnetId")
    def private_endpoint_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_endpoint_subnet_id.setter
    def private_endpoint_subnet_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]: ...
    @public_network_access.setter
    def public_network_access(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="searchSubnetId")
    def search_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @search_subnet_id.setter
    def search_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentities")
    def workload_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @workload_identities.setter
    def workload_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ChatModelDeploymentPropertiesArgsDict(TypedDict):
    model_format: pulumi.Input[_builtins.str]
    model_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChatModelDeploymentPropertiesArgs:
    def __init__(
        __self__,
        *,
        model_format: pulumi.Input[_builtins.str],
        model_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelFormat")
    def model_format(self) -> pulumi.Input[_builtins.str]: ...
    @model_format.setter
    def model_format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> pulumi.Input[_builtins.str]: ...
    @model_name.setter
    def model_name(self, value: pulumi.Input[_builtins.str]): ...

class IdentityArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]

@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...

class KeyVaultPropertiesArgsDict(TypedDict):
    key_name: pulumi.Input[_builtins.str]
    key_vault_uri: pulumi.Input[_builtins.str]
    key_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(
        __self__,
        *,
        key_name: pulumi.Input[_builtins.str],
        key_vault_uri: pulumi.Input[_builtins.str],
        key_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[_builtins.str]: ...
    @key_name.setter
    def key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> pulumi.Input[_builtins.str]: ...
    @key_vault_uri.setter
    def key_vault_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_version.setter
    def key_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolPropertiesArgsDict(TypedDict):
    max_node_count: pulumi.Input[_builtins.int]
    subnet_id: pulumi.Input[_builtins.str]
    vm_size: pulumi.Input[Union[_builtins.str, VmSize]]
    min_node_count: NotRequired[pulumi.Input[_builtins.int]]
    scale_set_priority: NotRequired[
        pulumi.Input[Union[_builtins.str, ScaleSetPriority]]
    ]

@pulumi.input_type
class NodePoolPropertiesArgs:
    def __init__(
        __self__,
        *,
        max_node_count: pulumi.Input[_builtins.int],
        subnet_id: pulumi.Input[_builtins.str],
        vm_size: pulumi.Input[Union[_builtins.str, VmSize]],
        min_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        scale_set_priority: Optional[
            pulumi.Input[Union[_builtins.str, ScaleSetPriority]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> pulumi.Input[_builtins.int]: ...
    @max_node_count.setter
    def max_node_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> pulumi.Input[Union[_builtins.str, VmSize]]: ...
    @vm_size.setter
    def vm_size(self, value: pulumi.Input[Union[_builtins.str, VmSize]]): ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_node_count.setter
    def min_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="scaleSetPriority")
    def scale_set_priority(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ScaleSetPriority]]]: ...
    @scale_set_priority.setter
    def scale_set_priority(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ScaleSetPriority]]]
    ): ...

class PrivateEndpointConnectionPropertiesArgsDict(TypedDict):
    private_link_service_connection_state: pulumi.Input[
        PrivateLinkServiceConnectionStateArgsDict
    ]

@pulumi.input_type
class PrivateEndpointConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        private_link_service_connection_state: pulumi.Input[
            PrivateLinkServiceConnectionStateArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> pulumi.Input[PrivateLinkServiceConnectionStateArgs]: ...
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(
        self, value: pulumi.Input[PrivateLinkServiceConnectionStateArgs]
    ): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        actions_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ],
    ): ...

class ProjectPropertiesArgsDict(TypedDict):
    settings: NotRequired[pulumi.Input[ProjectSettingsArgsDict]]
    storage_container_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ProjectPropertiesArgs:
    def __init__(
        __self__,
        *,
        settings: Optional[pulumi.Input[ProjectSettingsArgs]] = ...,
        storage_container_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[ProjectSettingsArgs]]: ...
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[ProjectSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="storageContainerIds")
    def storage_container_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @storage_container_ids.setter
    def storage_container_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ProjectSettingsArgsDict(TypedDict):
    behavior_preferences: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectSettingsArgs:
    def __init__(
        __self__, *, behavior_preferences: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="behaviorPreferences")
    def behavior_preferences(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @behavior_preferences.setter
    def behavior_preferences(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageAssetPropertiesArgsDict(TypedDict):
    description: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StorageAssetPropertiesArgs:
    def __init__(
        __self__,
        *,
        description: pulumi.Input[_builtins.str],
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]: ...
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageContainerPropertiesArgsDict(TypedDict):
    storage_store: pulumi.Input[
        Union[AzureNetAppFilesStoreArgsDict, AzureStorageBlobStoreArgsDict]
    ]

@pulumi.input_type
class StorageContainerPropertiesArgs:
    def __init__(
        __self__,
        *,
        storage_store: pulumi.Input[
            Union[AzureNetAppFilesStoreArgs, AzureStorageBlobStoreArgs]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageStore")
    def storage_store(
        self,
    ) -> pulumi.Input[Union[AzureNetAppFilesStoreArgs, AzureStorageBlobStoreArgs]]: ...
    @storage_store.setter
    def storage_store(
        self,
        value: pulumi.Input[
            Union[AzureNetAppFilesStoreArgs, AzureStorageBlobStoreArgs]
        ],
    ): ...

class SupercomputerIdentitiesArgsDict(TypedDict):
    cluster_identity: pulumi.Input[IdentityArgsDict]
    kubelet_identity: pulumi.Input[IdentityArgsDict]
    workload_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class SupercomputerIdentitiesArgs:
    def __init__(
        __self__,
        *,
        cluster_identity: pulumi.Input[IdentityArgs],
        kubelet_identity: pulumi.Input[IdentityArgs],
        workload_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentity")
    def cluster_identity(self) -> pulumi.Input[IdentityArgs]: ...
    @cluster_identity.setter
    def cluster_identity(self, value: pulumi.Input[IdentityArgs]): ...
    @_builtins.property
    @pulumi.getter(name="kubeletIdentity")
    def kubelet_identity(self) -> pulumi.Input[IdentityArgs]: ...
    @kubelet_identity.setter
    def kubelet_identity(self, value: pulumi.Input[IdentityArgs]): ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentities")
    def workload_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @workload_identities.setter
    def workload_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class SupercomputerPropertiesArgsDict(TypedDict):
    identities: pulumi.Input[SupercomputerIdentitiesArgsDict]
    subnet_id: pulumi.Input[_builtins.str]
    customer_managed_keys: NotRequired[
        pulumi.Input[Union[_builtins.str, CustomerManagedKeys]]
    ]
    disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    log_analytics_cluster_id: NotRequired[pulumi.Input[_builtins.str]]
    management_subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    outbound_type: NotRequired[pulumi.Input[Union[_builtins.str, NetworkEgressType]]]
    system_sku: NotRequired[pulumi.Input[Union[_builtins.str, SystemSku]]]

@pulumi.input_type
class SupercomputerPropertiesArgs:
    def __init__(
        __self__,
        *,
        identities: pulumi.Input[SupercomputerIdentitiesArgs],
        subnet_id: pulumi.Input[_builtins.str],
        customer_managed_keys: Optional[
            pulumi.Input[Union[_builtins.str, CustomerManagedKeys]]
        ] = ...,
        disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        log_analytics_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        management_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        outbound_type: Optional[
            pulumi.Input[Union[_builtins.str, NetworkEgressType]]
        ] = ...,
        system_sku: Optional[pulumi.Input[Union[_builtins.str, SystemSku]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identities(self) -> pulumi.Input[SupercomputerIdentitiesArgs]: ...
    @identities.setter
    def identities(self, value: pulumi.Input[SupercomputerIdentitiesArgs]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKeys")
    def customer_managed_keys(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CustomerManagedKeys]]]: ...
    @customer_managed_keys.setter
    def customer_managed_keys(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CustomerManagedKeys]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logAnalyticsClusterId")
    def log_analytics_cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_analytics_cluster_id.setter
    def log_analytics_cluster_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="managementSubnetId")
    def management_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @management_subnet_id.setter
    def management_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outboundType")
    def outbound_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NetworkEgressType]]]: ...
    @outbound_type.setter
    def outbound_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkEgressType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="systemSku")
    def system_sku(self) -> Optional[pulumi.Input[Union[_builtins.str, SystemSku]]]: ...
    @system_sku.setter
    def system_sku(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SystemSku]]]
    ): ...

class ToolPropertiesArgsDict(TypedDict):
    definition_content: Any
    version: pulumi.Input[_builtins.str]
    environment_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ToolPropertiesArgs:
    def __init__(
        __self__,
        *,
        definition_content: Any,
        version: pulumi.Input[_builtins.str],
        environment_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="definitionContent")
    def definition_content(self) -> Any: ...
    @definition_content.setter
    def definition_content(self, value: Any): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @environment_variables.setter
    def environment_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkspacePropertiesArgsDict(TypedDict):
    workspace_identity: pulumi.Input[IdentityArgsDict]
    agent_subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    customer_managed_keys: NotRequired[
        pulumi.Input[Union[_builtins.str, CustomerManagedKeys]]
    ]
    key_vault_properties: NotRequired[pulumi.Input[KeyVaultPropertiesArgsDict]]
    log_analytics_cluster_id: NotRequired[pulumi.Input[_builtins.str]]
    private_endpoint_subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
    ]
    supercomputer_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    workspace_subnet_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkspacePropertiesArgs:
    def __init__(
        __self__,
        *,
        workspace_identity: pulumi.Input[IdentityArgs],
        agent_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_managed_keys: Optional[
            pulumi.Input[Union[_builtins.str, CustomerManagedKeys]]
        ] = ...,
        key_vault_properties: Optional[pulumi.Input[KeyVaultPropertiesArgs]] = ...,
        log_analytics_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        private_endpoint_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        supercomputer_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        workspace_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workspaceIdentity")
    def workspace_identity(self) -> pulumi.Input[IdentityArgs]: ...
    @workspace_identity.setter
    def workspace_identity(self, value: pulumi.Input[IdentityArgs]): ...
    @_builtins.property
    @pulumi.getter(name="agentSubnetId")
    def agent_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_subnet_id.setter
    def agent_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKeys")
    def customer_managed_keys(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CustomerManagedKeys]]]: ...
    @customer_managed_keys.setter
    def customer_managed_keys(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CustomerManagedKeys]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(
        self,
    ) -> Optional[pulumi.Input[KeyVaultPropertiesArgs]]: ...
    @key_vault_properties.setter
    def key_vault_properties(
        self, value: Optional[pulumi.Input[KeyVaultPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logAnalyticsClusterId")
    def log_analytics_cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_analytics_cluster_id.setter
    def log_analytics_cluster_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointSubnetId")
    def private_endpoint_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_endpoint_subnet_id.setter
    def private_endpoint_subnet_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]: ...
    @public_network_access.setter
    def public_network_access(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="supercomputerIds")
    def supercomputer_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @supercomputer_ids.setter
    def supercomputer_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceSubnetId")
    def workspace_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_subnet_id.setter
    def workspace_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
