import builtins as _builtins
import sys
import pulumi
from typing import Any, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AutoPausePropertiesArgs",
    "AutoPausePropertiesArgsDict",
    "AutoScalePropertiesArgs",
    "AutoScalePropertiesArgsDict",
    "AzureSkuArgs",
    "AzureSkuArgsDict",
    "CmdkeySetupArgs",
    "CmdkeySetupArgsDict",
    "ComponentSetupArgs",
    "ComponentSetupArgsDict",
    "CspWorkspaceAdminPropertiesArgs",
    "CspWorkspaceAdminPropertiesArgsDict",
    "CustomerManagedKeyDetailsArgs",
    "CustomerManagedKeyDetailsArgsDict",
    "DataLakeStorageAccountDetailsArgs",
    "DataLakeStorageAccountDetailsArgsDict",
    "DynamicExecutorAllocationArgs",
    "DynamicExecutorAllocationArgsDict",
    "EncryptionDetailsArgs",
    "EncryptionDetailsArgsDict",
    "EntityReferenceArgs",
    "EntityReferenceArgsDict",
    "EnvironmentVariableSetupArgs",
    "EnvironmentVariableSetupArgsDict",
    "IntegrationRuntimeComputePropertiesArgs",
    "IntegrationRuntimeComputePropertiesArgsDict",
    "IntegrationRuntimeCustomSetupScriptPropertiesArgs",
    ...,
    "IntegrationRuntimeCustomerVirtualNetworkArgs",
    "IntegrationRuntimeCustomerVirtualNetworkArgsDict",
    "IntegrationRuntimeDataFlowPropertiesArgs",
    "IntegrationRuntimeDataFlowPropertiesArgsDict",
    "IntegrationRuntimeDataProxyPropertiesArgs",
    "IntegrationRuntimeDataProxyPropertiesArgsDict",
    "IntegrationRuntimeSsisCatalogInfoArgs",
    "IntegrationRuntimeSsisCatalogInfoArgsDict",
    "IntegrationRuntimeSsisPropertiesArgs",
    "IntegrationRuntimeSsisPropertiesArgsDict",
    "IntegrationRuntimeVNetPropertiesArgs",
    "IntegrationRuntimeVNetPropertiesArgsDict",
    "KekIdentityPropertiesArgs",
    "KekIdentityPropertiesArgsDict",
    "LibraryInfoArgs",
    "LibraryInfoArgsDict",
    "LibraryRequirementsArgs",
    "LibraryRequirementsArgsDict",
    "LinkedIntegrationRuntimeKeyAuthorizationArgs",
    "LinkedIntegrationRuntimeKeyAuthorizationArgsDict",
    "LinkedIntegrationRuntimeRbacAuthorizationArgs",
    "LinkedIntegrationRuntimeRbacAuthorizationArgsDict",
    "ManagedIdentityArgs",
    "ManagedIdentityArgsDict",
    "ManagedIntegrationRuntimeArgs",
    "ManagedIntegrationRuntimeArgsDict",
    "ManagedVirtualNetworkSettingsArgs",
    "ManagedVirtualNetworkSettingsArgsDict",
    "OptimizedAutoscaleArgs",
    "OptimizedAutoscaleArgsDict",
    "PrivateEndpointConnectionArgs",
    "PrivateEndpointConnectionArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "PurviewConfigurationArgs",
    "PurviewConfigurationArgsDict",
    "SecureStringArgs",
    "SecureStringArgsDict",
    "SelfHostedIntegrationRuntimeArgs",
    "SelfHostedIntegrationRuntimeArgsDict",
    "SkuArgs",
    "SkuArgsDict",
    "SparkConfigPropertiesArgs",
    "SparkConfigPropertiesArgsDict",
    "SqlPoolVulnerabilityAssessmentRuleBaselineItemArgs",
    ...,
    "TableLevelSharingPropertiesArgs",
    "TableLevelSharingPropertiesArgsDict",
    "VirtualNetworkProfileArgs",
    "VirtualNetworkProfileArgsDict",
    ...,
    ...,
    "WorkspaceKeyDetailsArgs",
    "WorkspaceKeyDetailsArgsDict",
    "WorkspaceRepositoryConfigurationArgs",
    "WorkspaceRepositoryConfigurationArgsDict",
]

class AutoPausePropertiesArgsDict(TypedDict):
    delay_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AutoPausePropertiesArgs:
    def __init__(
        __self__,
        *,
        delay_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="delayInMinutes")
    def delay_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @delay_in_minutes.setter
    def delay_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AutoScalePropertiesArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    max_node_count: NotRequired[pulumi.Input[_builtins.int]]
    min_node_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AutoScalePropertiesArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_node_count.setter
    def max_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_node_count.setter
    def min_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AzureSkuArgsDict(TypedDict):
    name: pulumi.Input[Union[_builtins.str, SkuName]]
    size: pulumi.Input[Union[_builtins.str, SkuSize]]
    capacity: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AzureSkuArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[Union[_builtins.str, SkuName]],
        size: pulumi.Input[Union[_builtins.str, SkuSize]],
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, SkuName]]: ...
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, SkuName]]): ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Input[Union[_builtins.str, SkuSize]]: ...
    @size.setter
    def size(self, value: pulumi.Input[Union[_builtins.str, SkuSize]]): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CmdkeySetupArgsDict(TypedDict):
    password: pulumi.Input[SecureStringArgsDict]
    target_name: Any
    type: pulumi.Input[_builtins.str]
    user_name: Any

@pulumi.input_type
class CmdkeySetupArgs:
    def __init__(
        __self__,
        *,
        password: pulumi.Input[SecureStringArgs],
        target_name: Any,
        type: pulumi.Input[_builtins.str],
        user_name: Any,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[SecureStringArgs]: ...
    @password.setter
    def password(self, value: pulumi.Input[SecureStringArgs]): ...
    @_builtins.property
    @pulumi.getter(name="targetName")
    def target_name(self) -> Any: ...
    @target_name.setter
    def target_name(self, value: Any): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Any: ...
    @user_name.setter
    def user_name(self, value: Any): ...

class ComponentSetupArgsDict(TypedDict):
    component_name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    license_key: NotRequired[pulumi.Input[SecureStringArgsDict]]

@pulumi.input_type
class ComponentSetupArgs:
    def __init__(
        __self__,
        *,
        component_name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        license_key: Optional[pulumi.Input[SecureStringArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentName")
    def component_name(self) -> pulumi.Input[_builtins.str]: ...
    @component_name.setter
    def component_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> Optional[pulumi.Input[SecureStringArgs]]: ...
    @license_key.setter
    def license_key(self, value: Optional[pulumi.Input[SecureStringArgs]]): ...

class CspWorkspaceAdminPropertiesArgsDict(TypedDict):
    initial_workspace_admin_object_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CspWorkspaceAdminPropertiesArgs:
    def __init__(
        __self__,
        *,
        initial_workspace_admin_object_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="initialWorkspaceAdminObjectId")
    def initial_workspace_admin_object_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @initial_workspace_admin_object_id.setter
    def initial_workspace_admin_object_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class CustomerManagedKeyDetailsArgsDict(TypedDict):
    kek_identity: NotRequired[pulumi.Input[KekIdentityPropertiesArgsDict]]
    key: NotRequired[pulumi.Input[WorkspaceKeyDetailsArgsDict]]

@pulumi.input_type
class CustomerManagedKeyDetailsArgs:
    def __init__(
        __self__,
        *,
        kek_identity: Optional[pulumi.Input[KekIdentityPropertiesArgs]] = ...,
        key: Optional[pulumi.Input[WorkspaceKeyDetailsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kekIdentity")
    def kek_identity(self) -> Optional[pulumi.Input[KekIdentityPropertiesArgs]]: ...
    @kek_identity.setter
    def kek_identity(
        self, value: Optional[pulumi.Input[KekIdentityPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[WorkspaceKeyDetailsArgs]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[WorkspaceKeyDetailsArgs]]): ...

class DataLakeStorageAccountDetailsArgsDict(TypedDict):
    account_url: NotRequired[pulumi.Input[_builtins.str]]
    create_managed_private_endpoint: NotRequired[pulumi.Input[_builtins.bool]]
    filesystem: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataLakeStorageAccountDetailsArgs:
    def __init__(
        __self__,
        *,
        account_url: Optional[pulumi.Input[_builtins.str]] = ...,
        create_managed_private_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        filesystem: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountUrl")
    def account_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_url.setter
    def account_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createManagedPrivateEndpoint")
    def create_managed_private_endpoint(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_managed_private_endpoint.setter
    def create_managed_private_endpoint(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def filesystem(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filesystem.setter
    def filesystem(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DynamicExecutorAllocationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    max_executors: NotRequired[pulumi.Input[_builtins.int]]
    min_executors: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DynamicExecutorAllocationArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_executors: Optional[pulumi.Input[_builtins.int]] = ...,
        min_executors: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxExecutors")
    def max_executors(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_executors.setter
    def max_executors(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minExecutors")
    def min_executors(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_executors.setter
    def min_executors(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class EncryptionDetailsArgsDict(TypedDict):
    cmk: NotRequired[pulumi.Input[CustomerManagedKeyDetailsArgsDict]]

@pulumi.input_type
class EncryptionDetailsArgs:
    def __init__(
        __self__, *, cmk: Optional[pulumi.Input[CustomerManagedKeyDetailsArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cmk(self) -> Optional[pulumi.Input[CustomerManagedKeyDetailsArgs]]: ...
    @cmk.setter
    def cmk(self, value: Optional[pulumi.Input[CustomerManagedKeyDetailsArgs]]): ...

class EntityReferenceArgsDict(TypedDict):
    reference_name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[
        pulumi.Input[Union[_builtins.str, IntegrationRuntimeEntityReferenceType]]
    ]

@pulumi.input_type
class EntityReferenceArgs:
    def __init__(
        __self__,
        *,
        reference_name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[
            pulumi.Input[Union[_builtins.str, IntegrationRuntimeEntityReferenceType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="referenceName")
    def reference_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reference_name.setter
    def reference_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, IntegrationRuntimeEntityReferenceType]]
    ]: ...
    @type.setter
    def type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, IntegrationRuntimeEntityReferenceType]]
        ],
    ): ...

class EnvironmentVariableSetupArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    variable_name: pulumi.Input[_builtins.str]
    variable_value: pulumi.Input[_builtins.str]

@pulumi.input_type
class EnvironmentVariableSetupArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        variable_name: pulumi.Input[_builtins.str],
        variable_value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="variableName")
    def variable_name(self) -> pulumi.Input[_builtins.str]: ...
    @variable_name.setter
    def variable_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="variableValue")
    def variable_value(self) -> pulumi.Input[_builtins.str]: ...
    @variable_value.setter
    def variable_value(self, value: pulumi.Input[_builtins.str]): ...

class IntegrationRuntimeComputePropertiesArgsDict(TypedDict):
    data_flow_properties: NotRequired[
        pulumi.Input[IntegrationRuntimeDataFlowPropertiesArgsDict]
    ]
    location: NotRequired[pulumi.Input[_builtins.str]]
    max_parallel_executions_per_node: NotRequired[pulumi.Input[_builtins.int]]
    node_size: NotRequired[pulumi.Input[_builtins.str]]
    number_of_nodes: NotRequired[pulumi.Input[_builtins.int]]
    v_net_properties: NotRequired[
        pulumi.Input[IntegrationRuntimeVNetPropertiesArgsDict]
    ]

@pulumi.input_type
class IntegrationRuntimeComputePropertiesArgs:
    def __init__(
        __self__,
        *,
        data_flow_properties: Optional[
            pulumi.Input[IntegrationRuntimeDataFlowPropertiesArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_parallel_executions_per_node: Optional[pulumi.Input[_builtins.int]] = ...,
        node_size: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
        v_net_properties: Optional[
            pulumi.Input[IntegrationRuntimeVNetPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataFlowProperties")
    def data_flow_properties(
        self,
    ) -> Optional[pulumi.Input[IntegrationRuntimeDataFlowPropertiesArgs]]: ...
    @data_flow_properties.setter
    def data_flow_properties(
        self, value: Optional[pulumi.Input[IntegrationRuntimeDataFlowPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxParallelExecutionsPerNode")
    def max_parallel_executions_per_node(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_parallel_executions_per_node.setter
    def max_parallel_executions_per_node(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeSize")
    def node_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_size.setter
    def node_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfNodes")
    def number_of_nodes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_nodes.setter
    def number_of_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="vNetProperties")
    def v_net_properties(
        self,
    ) -> Optional[pulumi.Input[IntegrationRuntimeVNetPropertiesArgs]]: ...
    @v_net_properties.setter
    def v_net_properties(
        self, value: Optional[pulumi.Input[IntegrationRuntimeVNetPropertiesArgs]]
    ): ...

class IntegrationRuntimeCustomSetupScriptPropertiesArgsDict(TypedDict):
    blob_container_uri: NotRequired[pulumi.Input[_builtins.str]]
    sas_token: NotRequired[pulumi.Input[SecureStringArgsDict]]

@pulumi.input_type
class IntegrationRuntimeCustomSetupScriptPropertiesArgs:
    def __init__(
        __self__,
        *,
        blob_container_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        sas_token: Optional[pulumi.Input[SecureStringArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blobContainerUri")
    def blob_container_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @blob_container_uri.setter
    def blob_container_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sasToken")
    def sas_token(self) -> Optional[pulumi.Input[SecureStringArgs]]: ...
    @sas_token.setter
    def sas_token(self, value: Optional[pulumi.Input[SecureStringArgs]]): ...

class IntegrationRuntimeCustomerVirtualNetworkArgsDict(TypedDict):
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IntegrationRuntimeCustomerVirtualNetworkArgs:
    def __init__(
        __self__, *, subnet_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IntegrationRuntimeDataFlowPropertiesArgsDict(TypedDict):
    compute_type: NotRequired[pulumi.Input[Union[_builtins.str, DataFlowComputeType]]]
    core_count: NotRequired[pulumi.Input[_builtins.int]]
    time_to_live: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class IntegrationRuntimeDataFlowPropertiesArgs:
    def __init__(
        __self__,
        *,
        compute_type: Optional[
            pulumi.Input[Union[_builtins.str, DataFlowComputeType]]
        ] = ...,
        core_count: Optional[pulumi.Input[_builtins.int]] = ...,
        time_to_live: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DataFlowComputeType]]]: ...
    @compute_type.setter
    def compute_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DataFlowComputeType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @core_count.setter
    def core_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="timeToLive")
    def time_to_live(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @time_to_live.setter
    def time_to_live(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class IntegrationRuntimeDataProxyPropertiesArgsDict(TypedDict):
    connect_via: NotRequired[pulumi.Input[EntityReferenceArgsDict]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    staging_linked_service: NotRequired[pulumi.Input[EntityReferenceArgsDict]]

@pulumi.input_type
class IntegrationRuntimeDataProxyPropertiesArgs:
    def __init__(
        __self__,
        *,
        connect_via: Optional[pulumi.Input[EntityReferenceArgs]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        staging_linked_service: Optional[pulumi.Input[EntityReferenceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectVia")
    def connect_via(self) -> Optional[pulumi.Input[EntityReferenceArgs]]: ...
    @connect_via.setter
    def connect_via(self, value: Optional[pulumi.Input[EntityReferenceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stagingLinkedService")
    def staging_linked_service(self) -> Optional[pulumi.Input[EntityReferenceArgs]]: ...
    @staging_linked_service.setter
    def staging_linked_service(
        self, value: Optional[pulumi.Input[EntityReferenceArgs]]
    ): ...

class IntegrationRuntimeSsisCatalogInfoArgsDict(TypedDict):
    catalog_admin_password: NotRequired[pulumi.Input[SecureStringArgsDict]]
    catalog_admin_user_name: NotRequired[pulumi.Input[_builtins.str]]
    catalog_pricing_tier: NotRequired[
        pulumi.Input[Union[_builtins.str, IntegrationRuntimeSsisCatalogPricingTier]]
    ]
    catalog_server_endpoint: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IntegrationRuntimeSsisCatalogInfoArgs:
    def __init__(
        __self__,
        *,
        catalog_admin_password: Optional[pulumi.Input[SecureStringArgs]] = ...,
        catalog_admin_user_name: Optional[pulumi.Input[_builtins.str]] = ...,
        catalog_pricing_tier: Optional[
            pulumi.Input[Union[_builtins.str, IntegrationRuntimeSsisCatalogPricingTier]]
        ] = ...,
        catalog_server_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogAdminPassword")
    def catalog_admin_password(self) -> Optional[pulumi.Input[SecureStringArgs]]: ...
    @catalog_admin_password.setter
    def catalog_admin_password(
        self, value: Optional[pulumi.Input[SecureStringArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="catalogAdminUserName")
    def catalog_admin_user_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_admin_user_name.setter
    def catalog_admin_user_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="catalogPricingTier")
    def catalog_pricing_tier(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, IntegrationRuntimeSsisCatalogPricingTier]]
    ]: ...
    @catalog_pricing_tier.setter
    def catalog_pricing_tier(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, IntegrationRuntimeSsisCatalogPricingTier]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="catalogServerEndpoint")
    def catalog_server_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_server_endpoint.setter
    def catalog_server_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IntegrationRuntimeSsisPropertiesArgsDict(TypedDict):
    catalog_info: NotRequired[pulumi.Input[IntegrationRuntimeSsisCatalogInfoArgsDict]]
    custom_setup_script_properties: NotRequired[
        pulumi.Input[IntegrationRuntimeCustomSetupScriptPropertiesArgsDict]
    ]
    data_proxy_properties: NotRequired[
        pulumi.Input[IntegrationRuntimeDataProxyPropertiesArgsDict]
    ]
    edition: NotRequired[pulumi.Input[Union[_builtins.str, IntegrationRuntimeEdition]]]
    express_custom_setup_properties: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        CmdkeySetupArgsDict,
                        ComponentSetupArgsDict,
                        EnvironmentVariableSetupArgsDict,
                    ]
                ]
            ]
        ]
    ]
    license_type: NotRequired[
        pulumi.Input[Union[_builtins.str, IntegrationRuntimeLicenseType]]
    ]

@pulumi.input_type
class IntegrationRuntimeSsisPropertiesArgs:
    def __init__(
        __self__,
        *,
        catalog_info: Optional[
            pulumi.Input[IntegrationRuntimeSsisCatalogInfoArgs]
        ] = ...,
        custom_setup_script_properties: Optional[
            pulumi.Input[IntegrationRuntimeCustomSetupScriptPropertiesArgs]
        ] = ...,
        data_proxy_properties: Optional[
            pulumi.Input[IntegrationRuntimeDataProxyPropertiesArgs]
        ] = ...,
        edition: Optional[
            pulumi.Input[Union[_builtins.str, IntegrationRuntimeEdition]]
        ] = ...,
        express_custom_setup_properties: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CmdkeySetupArgs,
                            ComponentSetupArgs,
                            EnvironmentVariableSetupArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        license_type: Optional[
            pulumi.Input[Union[_builtins.str, IntegrationRuntimeLicenseType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogInfo")
    def catalog_info(
        self,
    ) -> Optional[pulumi.Input[IntegrationRuntimeSsisCatalogInfoArgs]]: ...
    @catalog_info.setter
    def catalog_info(
        self, value: Optional[pulumi.Input[IntegrationRuntimeSsisCatalogInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customSetupScriptProperties")
    def custom_setup_script_properties(
        self,
    ) -> Optional[pulumi.Input[IntegrationRuntimeCustomSetupScriptPropertiesArgs]]: ...
    @custom_setup_script_properties.setter
    def custom_setup_script_properties(
        self,
        value: Optional[
            pulumi.Input[IntegrationRuntimeCustomSetupScriptPropertiesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataProxyProperties")
    def data_proxy_properties(
        self,
    ) -> Optional[pulumi.Input[IntegrationRuntimeDataProxyPropertiesArgs]]: ...
    @data_proxy_properties.setter
    def data_proxy_properties(
        self, value: Optional[pulumi.Input[IntegrationRuntimeDataProxyPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def edition(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IntegrationRuntimeEdition]]]: ...
    @edition.setter
    def edition(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, IntegrationRuntimeEdition]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="expressCustomSetupProperties")
    def express_custom_setup_properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        CmdkeySetupArgs,
                        ComponentSetupArgs,
                        EnvironmentVariableSetupArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @express_custom_setup_properties.setter
    def express_custom_setup_properties(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CmdkeySetupArgs,
                            ComponentSetupArgs,
                            EnvironmentVariableSetupArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, IntegrationRuntimeLicenseType]]
    ]: ...
    @license_type.setter
    def license_type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, IntegrationRuntimeLicenseType]]
        ],
    ): ...

class IntegrationRuntimeVNetPropertiesArgsDict(TypedDict):
    public_ips: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subnet: NotRequired[pulumi.Input[_builtins.str]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    v_net_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IntegrationRuntimeVNetPropertiesArgs:
    def __init__(
        __self__,
        *,
        public_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        v_net_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicIPs")
    def public_ips(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @public_ips.setter
    def public_ips(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vNetId")
    def v_net_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @v_net_id.setter
    def v_net_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KekIdentityPropertiesArgsDict(TypedDict):
    use_system_assigned_identity: NotRequired[Any]
    user_assigned_identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KekIdentityPropertiesArgs:
    def __init__(
        __self__,
        *,
        use_system_assigned_identity: Optional[Any] = ...,
        user_assigned_identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="useSystemAssignedIdentity")
    def use_system_assigned_identity(self) -> Optional[Any]: ...
    @use_system_assigned_identity.setter
    def use_system_assigned_identity(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_assigned_identity.setter
    def user_assigned_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LibraryInfoArgsDict(TypedDict):
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LibraryInfoArgs:
    def __init__(
        __self__,
        *,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LibraryRequirementsArgsDict(TypedDict):
    content: NotRequired[pulumi.Input[_builtins.str]]
    filename: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LibraryRequirementsArgs:
    def __init__(
        __self__,
        *,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        filename: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def filename(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filename.setter
    def filename(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LinkedIntegrationRuntimeKeyAuthorizationArgsDict(TypedDict):
    authorization_type: pulumi.Input[_builtins.str]
    key: pulumi.Input[SecureStringArgsDict]

@pulumi.input_type
class LinkedIntegrationRuntimeKeyAuthorizationArgs:
    def __init__(
        __self__,
        *,
        authorization_type: pulumi.Input[_builtins.str],
        key: pulumi.Input[SecureStringArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> pulumi.Input[_builtins.str]: ...
    @authorization_type.setter
    def authorization_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[SecureStringArgs]: ...
    @key.setter
    def key(self, value: pulumi.Input[SecureStringArgs]): ...

class LinkedIntegrationRuntimeRbacAuthorizationArgsDict(TypedDict):
    authorization_type: pulumi.Input[_builtins.str]
    resource_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class LinkedIntegrationRuntimeRbacAuthorizationArgs:
    def __init__(
        __self__,
        *,
        authorization_type: pulumi.Input[_builtins.str],
        resource_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> pulumi.Input[_builtins.str]: ...
    @authorization_type.setter
    def authorization_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): ...

class ManagedIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[ResourceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ManagedIdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[ResourceIdentityType]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ManagedIntegrationRuntimeArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    compute_properties: NotRequired[
        pulumi.Input[IntegrationRuntimeComputePropertiesArgsDict]
    ]
    customer_virtual_network: NotRequired[
        pulumi.Input[IntegrationRuntimeCustomerVirtualNetworkArgsDict]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    reference_name: NotRequired[pulumi.Input[_builtins.str]]
    ssis_properties: NotRequired[pulumi.Input[IntegrationRuntimeSsisPropertiesArgsDict]]

@pulumi.input_type
class ManagedIntegrationRuntimeArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        compute_properties: Optional[
            pulumi.Input[IntegrationRuntimeComputePropertiesArgs]
        ] = ...,
        customer_virtual_network: Optional[
            pulumi.Input[IntegrationRuntimeCustomerVirtualNetworkArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        reference_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ssis_properties: Optional[
            pulumi.Input[IntegrationRuntimeSsisPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="computeProperties")
    def compute_properties(
        self,
    ) -> Optional[pulumi.Input[IntegrationRuntimeComputePropertiesArgs]]: ...
    @compute_properties.setter
    def compute_properties(
        self, value: Optional[pulumi.Input[IntegrationRuntimeComputePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customerVirtualNetwork")
    def customer_virtual_network(
        self,
    ) -> Optional[pulumi.Input[IntegrationRuntimeCustomerVirtualNetworkArgs]]: ...
    @customer_virtual_network.setter
    def customer_virtual_network(
        self,
        value: Optional[pulumi.Input[IntegrationRuntimeCustomerVirtualNetworkArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="referenceName")
    def reference_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reference_name.setter
    def reference_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ssisProperties")
    def ssis_properties(
        self,
    ) -> Optional[pulumi.Input[IntegrationRuntimeSsisPropertiesArgs]]: ...
    @ssis_properties.setter
    def ssis_properties(
        self, value: Optional[pulumi.Input[IntegrationRuntimeSsisPropertiesArgs]]
    ): ...

class ManagedVirtualNetworkSettingsArgsDict(TypedDict):
    allowed_aad_tenant_ids_for_linking: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    linked_access_check_on_target_resource: NotRequired[pulumi.Input[_builtins.bool]]
    prevent_data_exfiltration: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ManagedVirtualNetworkSettingsArgs:
    def __init__(
        __self__,
        *,
        allowed_aad_tenant_ids_for_linking: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        linked_access_check_on_target_resource: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        prevent_data_exfiltration: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAadTenantIdsForLinking")
    def allowed_aad_tenant_ids_for_linking(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_aad_tenant_ids_for_linking.setter
    def allowed_aad_tenant_ids_for_linking(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedAccessCheckOnTargetResource")
    def linked_access_check_on_target_resource(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @linked_access_check_on_target_resource.setter
    def linked_access_check_on_target_resource(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preventDataExfiltration")
    def prevent_data_exfiltration(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @prevent_data_exfiltration.setter
    def prevent_data_exfiltration(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class OptimizedAutoscaleArgsDict(TypedDict):
    is_enabled: pulumi.Input[_builtins.bool]
    maximum: pulumi.Input[_builtins.int]
    minimum: pulumi.Input[_builtins.int]
    version: pulumi.Input[_builtins.int]

@pulumi.input_type
class OptimizedAutoscaleArgs:
    def __init__(
        __self__,
        *,
        is_enabled: pulumi.Input[_builtins.bool],
        maximum: pulumi.Input[_builtins.int],
        minimum: pulumi.Input[_builtins.int],
        version: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> pulumi.Input[_builtins.int]: ...
    @maximum.setter
    def maximum(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> pulumi.Input[_builtins.int]: ...
    @minimum.setter
    def minimum(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.int]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.int]): ...

class PrivateEndpointConnectionArgsDict(TypedDict):
    private_link_service_connection_state: NotRequired[
        pulumi.Input[PrivateLinkServiceConnectionStateArgsDict]
    ]

@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(
        __self__,
        *,
        private_link_service_connection_state: Optional[
            pulumi.Input[PrivateLinkServiceConnectionStateArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]: ...
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(
        self, value: Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]
    ): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PurviewConfigurationArgsDict(TypedDict):
    purview_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PurviewConfigurationArgs:
    def __init__(
        __self__, *, purview_resource_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="purviewResourceId")
    def purview_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @purview_resource_id.setter
    def purview_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecureStringArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class SecureStringArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class SelfHostedIntegrationRuntimeArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    linked_info: NotRequired[
        pulumi.Input[
            Union[
                LinkedIntegrationRuntimeKeyAuthorizationArgsDict,
                LinkedIntegrationRuntimeRbacAuthorizationArgsDict,
            ]
        ]
    ]

@pulumi.input_type
class SelfHostedIntegrationRuntimeArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_info: Optional[
            pulumi.Input[
                Union[
                    LinkedIntegrationRuntimeKeyAuthorizationArgs,
                    LinkedIntegrationRuntimeRbacAuthorizationArgs,
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkedInfo")
    def linked_info(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                LinkedIntegrationRuntimeKeyAuthorizationArgs,
                LinkedIntegrationRuntimeRbacAuthorizationArgs,
            ]
        ]
    ]: ...
    @linked_info.setter
    def linked_info(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    LinkedIntegrationRuntimeKeyAuthorizationArgs,
                    LinkedIntegrationRuntimeRbacAuthorizationArgs,
                ]
            ]
        ],
    ): ...

class SkuArgsDict(TypedDict):
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__,
        *,
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SparkConfigPropertiesArgsDict(TypedDict):
    configuration_type: NotRequired[
        pulumi.Input[Union[_builtins.str, ConfigurationType]]
    ]
    content: NotRequired[pulumi.Input[_builtins.str]]
    filename: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SparkConfigPropertiesArgs:
    def __init__(
        __self__,
        *,
        configuration_type: Optional[
            pulumi.Input[Union[_builtins.str, ConfigurationType]]
        ] = ...,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        filename: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConfigurationType]]]: ...
    @configuration_type.setter
    def configuration_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConfigurationType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def filename(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filename.setter
    def filename(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SqlPoolVulnerabilityAssessmentRuleBaselineItemArgsDict(TypedDict):
    result: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class SqlPoolVulnerabilityAssessmentRuleBaselineItemArgs:
    def __init__(
        __self__, *, result: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def result(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @result.setter
    def result(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class TableLevelSharingPropertiesArgsDict(TypedDict):
    external_tables_to_exclude: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    external_tables_to_include: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    materialized_views_to_exclude: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    materialized_views_to_include: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    tables_to_exclude: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tables_to_include: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class TableLevelSharingPropertiesArgs:
    def __init__(
        __self__,
        *,
        external_tables_to_exclude: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        external_tables_to_include: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        materialized_views_to_exclude: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        materialized_views_to_include: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tables_to_exclude: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tables_to_include: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalTablesToExclude")
    def external_tables_to_exclude(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @external_tables_to_exclude.setter
    def external_tables_to_exclude(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="externalTablesToInclude")
    def external_tables_to_include(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @external_tables_to_include.setter
    def external_tables_to_include(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="materializedViewsToExclude")
    def materialized_views_to_exclude(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @materialized_views_to_exclude.setter
    def materialized_views_to_exclude(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="materializedViewsToInclude")
    def materialized_views_to_include(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @materialized_views_to_include.setter
    def materialized_views_to_include(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tablesToExclude")
    def tables_to_exclude(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tables_to_exclude.setter
    def tables_to_exclude(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tablesToInclude")
    def tables_to_include(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tables_to_include.setter
    def tables_to_include(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class VirtualNetworkProfileArgsDict(TypedDict):
    compute_subnet_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualNetworkProfileArgs:
    def __init__(
        __self__, *, compute_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeSubnetId")
    def compute_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_subnet_id.setter
    def compute_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VulnerabilityAssessmentRecurringScansPropertiesArgsDict(TypedDict):
    email_subscription_admins: NotRequired[pulumi.Input[_builtins.bool]]
    emails: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    is_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class VulnerabilityAssessmentRecurringScansPropertiesArgs:
    def __init__(
        __self__,
        *,
        email_subscription_admins: Optional[pulumi.Input[_builtins.bool]] = ...,
        emails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailSubscriptionAdmins")
    def email_subscription_admins(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @email_subscription_admins.setter
    def email_subscription_admins(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def emails(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @emails.setter
    def emails(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class WorkspaceKeyDetailsArgsDict(TypedDict):
    key_vault_url: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkspaceKeyDetailsArgs:
    def __init__(
        __self__,
        *,
        key_vault_url: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUrl")
    def key_vault_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_url.setter
    def key_vault_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkspaceRepositoryConfigurationArgsDict(TypedDict):
    account_name: NotRequired[pulumi.Input[_builtins.str]]
    collaboration_branch: NotRequired[pulumi.Input[_builtins.str]]
    host_name: NotRequired[pulumi.Input[_builtins.str]]
    last_commit_id: NotRequired[pulumi.Input[_builtins.str]]
    project_name: NotRequired[pulumi.Input[_builtins.str]]
    repository_name: NotRequired[pulumi.Input[_builtins.str]]
    root_folder: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkspaceRepositoryConfigurationArgs:
    def __init__(
        __self__,
        *,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        collaboration_branch: Optional[pulumi.Input[_builtins.str]] = ...,
        host_name: Optional[pulumi.Input[_builtins.str]] = ...,
        last_commit_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project_name: Optional[pulumi.Input[_builtins.str]] = ...,
        repository_name: Optional[pulumi.Input[_builtins.str]] = ...,
        root_folder: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="collaborationBranch")
    def collaboration_branch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collaboration_branch.setter
    def collaboration_branch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_name.setter
    def host_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastCommitId")
    def last_commit_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_commit_id.setter
    def last_commit_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_name.setter
    def project_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository_name.setter
    def repository_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootFolder")
    def root_folder(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_folder.setter
    def root_folder(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
