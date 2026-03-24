

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AutoPausePropertiesResponse', 'AutoScalePropertiesResponse', 'AzureSkuResponse', 'CmdkeySetupResponse', 'ComponentSetupResponse', 'CspWorkspaceAdminPropertiesResponse', 'CustomerManagedKeyDetailsResponse', 'DataLakeStorageAccountDetailsResponse', 'DatabaseStatisticsResponse', 'DynamicExecutorAllocationResponse', 'EncryptionDetailsResponse', 'EntityReferenceResponse', 'EnvironmentVariableSetupResponse', 'FollowerDatabaseDefinitionResponse', 'IntegrationRuntimeComputePropertiesResponse', ..., 'IntegrationRuntimeCustomerVirtualNetworkResponse', 'IntegrationRuntimeDataFlowPropertiesResponse', 'IntegrationRuntimeDataProxyPropertiesResponse', 'IntegrationRuntimeSsisCatalogInfoResponse', 'IntegrationRuntimeSsisPropertiesResponse', 'IntegrationRuntimeVNetPropertiesResponse', 'KekIdentityPropertiesResponse', 'LanguageExtensionResponse', 'LanguageExtensionsListResponse', 'LibraryInfoResponse', 'LibraryRequirementsResponse', 'LinkedIntegrationRuntimeKeyAuthorizationResponse', 'LinkedIntegrationRuntimeRbacAuthorizationResponse', 'LinkedIntegrationRuntimeResponse', 'ManagedIdentityResponse', 'ManagedIntegrationRuntimeErrorResponse', 'ManagedIntegrationRuntimeNodeResponse', 'ManagedIntegrationRuntimeOperationResultResponse', 'ManagedIntegrationRuntimeResponse', 'ManagedIntegrationRuntimeStatusResponse', 'ManagedVirtualNetworkSettingsResponse', 'OptimizedAutoscaleResponse', ..., 'PrivateEndpointConnectionResponse', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', 'PurviewConfigurationResponse', 'SecureStringResponse', 'SelfHostedIntegrationRuntimeNodeResponse', 'SelfHostedIntegrationRuntimeResponse', 'SelfHostedIntegrationRuntimeStatusResponse', 'SkuResponse', 'SparkConfigPropertiesResponse', ..., 'SsisEnvironmentReferenceResponse', 'SsisEnvironmentResponse', 'SsisFolderResponse', 'SsisPackageResponse', 'SsisParameterResponse', 'SsisProjectResponse', 'SsisVariableResponse', 'SystemDataResponse', 'TableLevelSharingPropertiesResponse', 'UserAssignedManagedIdentityResponse', 'VirtualNetworkProfileResponse', ..., 'WorkspaceKeyDetailsResponse', 'WorkspaceRepositoryConfigurationResponse']
@pulumi.output_type
class AutoPausePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delay_in_minutes: Optional[_builtins.int] = ..., enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delayInMinutes")
    def delay_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AutoScalePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., max_node_count: Optional[_builtins.int] = ..., min_node_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AzureSkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, size: _builtins.str, capacity: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class CmdkeySetupResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, password: outputs.SecureStringResponse, target_name: Any, type: _builtins.str, user_name: Any) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> outputs.SecureStringResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetName")
    def target_name(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Any:
        
        ...
    


@pulumi.output_type
class ComponentSetupResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, component_name: _builtins.str, type: _builtins.str, license_key: Optional[outputs.SecureStringResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentName")
    def component_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> Optional[outputs.SecureStringResponse]:
        
        ...
    


@pulumi.output_type
class CspWorkspaceAdminPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, initial_workspace_admin_object_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialWorkspaceAdminObjectId")
    def initial_workspace_admin_object_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CustomerManagedKeyDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, status: _builtins.str, kek_identity: Optional[outputs.KekIdentityPropertiesResponse] = ..., key: Optional[outputs.WorkspaceKeyDetailsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kekIdentity")
    def kek_identity(self) -> Optional[outputs.KekIdentityPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[outputs.WorkspaceKeyDetailsResponse]:
        
        ...
    


@pulumi.output_type
class DataLakeStorageAccountDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_url: Optional[_builtins.str] = ..., create_managed_private_endpoint: Optional[_builtins.bool] = ..., filesystem: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountUrl")
    def account_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createManagedPrivateEndpoint")
    def create_managed_private_endpoint(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filesystem(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseStatisticsResponse(dict):
    
    def __init__(__self__, *, size: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class DynamicExecutorAllocationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., max_executors: Optional[_builtins.int] = ..., min_executors: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxExecutors")
    def max_executors(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minExecutors")
    def min_executors(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class EncryptionDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, double_encryption_enabled: _builtins.bool, cmk: Optional[outputs.CustomerManagedKeyDetailsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="doubleEncryptionEnabled")
    def double_encryption_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cmk(self) -> Optional[outputs.CustomerManagedKeyDetailsResponse]:
        
        ...
    


@pulumi.output_type
class EntityReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, reference_name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="referenceName")
    def reference_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentVariableSetupResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, variable_name: _builtins.str, variable_value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="variableName")
    def variable_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="variableValue")
    def variable_value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FollowerDatabaseDefinitionResponse(dict):
    
    def __init__(__self__, *, attached_database_configuration_name: _builtins.str, database_name: _builtins.str, kusto_pool_resource_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedDatabaseConfigurationName")
    def attached_database_configuration_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kustoPoolResourceId")
    def kusto_pool_resource_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class IntegrationRuntimeComputePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_flow_properties: Optional[outputs.IntegrationRuntimeDataFlowPropertiesResponse] = ..., location: Optional[_builtins.str] = ..., max_parallel_executions_per_node: Optional[_builtins.int] = ..., node_size: Optional[_builtins.str] = ..., number_of_nodes: Optional[_builtins.int] = ..., v_net_properties: Optional[outputs.IntegrationRuntimeVNetPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFlowProperties")
    def data_flow_properties(self) -> Optional[outputs.IntegrationRuntimeDataFlowPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxParallelExecutionsPerNode")
    def max_parallel_executions_per_node(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeSize")
    def node_size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfNodes")
    def number_of_nodes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vNetProperties")
    def v_net_properties(self) -> Optional[outputs.IntegrationRuntimeVNetPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class IntegrationRuntimeCustomSetupScriptPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, blob_container_uri: Optional[_builtins.str] = ..., sas_token: Optional[outputs.SecureStringResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobContainerUri")
    def blob_container_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasToken")
    def sas_token(self) -> Optional[outputs.SecureStringResponse]:
        
        ...
    


@pulumi.output_type
class IntegrationRuntimeCustomerVirtualNetworkResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnet_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IntegrationRuntimeDataFlowPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, compute_type: Optional[_builtins.str] = ..., core_count: Optional[_builtins.int] = ..., time_to_live: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeToLive")
    def time_to_live(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class IntegrationRuntimeDataProxyPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connect_via: Optional[outputs.EntityReferenceResponse] = ..., path: Optional[_builtins.str] = ..., staging_linked_service: Optional[outputs.EntityReferenceResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectVia")
    def connect_via(self) -> Optional[outputs.EntityReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingLinkedService")
    def staging_linked_service(self) -> Optional[outputs.EntityReferenceResponse]:
        
        ...
    


@pulumi.output_type
class IntegrationRuntimeSsisCatalogInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, catalog_admin_password: Optional[outputs.SecureStringResponse] = ..., catalog_admin_user_name: Optional[_builtins.str] = ..., catalog_pricing_tier: Optional[_builtins.str] = ..., catalog_server_endpoint: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogAdminPassword")
    def catalog_admin_password(self) -> Optional[outputs.SecureStringResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogAdminUserName")
    def catalog_admin_user_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogPricingTier")
    def catalog_pricing_tier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogServerEndpoint")
    def catalog_server_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IntegrationRuntimeSsisPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, catalog_info: Optional[outputs.IntegrationRuntimeSsisCatalogInfoResponse] = ..., custom_setup_script_properties: Optional[outputs.IntegrationRuntimeCustomSetupScriptPropertiesResponse] = ..., data_proxy_properties: Optional[outputs.IntegrationRuntimeDataProxyPropertiesResponse] = ..., edition: Optional[_builtins.str] = ..., express_custom_setup_properties: Optional[Sequence[Any]] = ..., license_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogInfo")
    def catalog_info(self) -> Optional[outputs.IntegrationRuntimeSsisCatalogInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customSetupScriptProperties")
    def custom_setup_script_properties(self) -> Optional[outputs.IntegrationRuntimeCustomSetupScriptPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProxyProperties")
    def data_proxy_properties(self) -> Optional[outputs.IntegrationRuntimeDataProxyPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressCustomSetupProperties")
    def express_custom_setup_properties(self) -> Optional[Sequence[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IntegrationRuntimeVNetPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, public_ips: Optional[Sequence[_builtins.str]] = ..., subnet: Optional[_builtins.str] = ..., subnet_id: Optional[_builtins.str] = ..., v_net_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPs")
    def public_ips(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vNetId")
    def v_net_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class KekIdentityPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, use_system_assigned_identity: Optional[Any] = ..., user_assigned_identity: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useSystemAssignedIdentity")
    def use_system_assigned_identity(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LanguageExtensionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, language_extension_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageExtensionName")
    def language_extension_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LanguageExtensionsListResponse(dict):
    
    def __init__(__self__, *, value: Optional[Sequence[outputs.LanguageExtensionResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.LanguageExtensionResponse]]:
        
        ...
    


@pulumi.output_type
class LibraryInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, creator_id: _builtins.str, provisioning_status: _builtins.str, uploaded_timestamp: _builtins.str, container_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creatorId")
    def creator_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningStatus")
    def provisioning_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadedTimestamp")
    def uploaded_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LibraryRequirementsResponse(dict):
    
    def __init__(__self__, *, time: _builtins.str, content: Optional[_builtins.str] = ..., filename: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filename(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LinkedIntegrationRuntimeKeyAuthorizationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authorization_type: _builtins.str, key: outputs.SecureStringResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> outputs.SecureStringResponse:
        
        ...
    


@pulumi.output_type
class LinkedIntegrationRuntimeRbacAuthorizationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authorization_type: _builtins.str, resource_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class LinkedIntegrationRuntimeResponse(dict):
    
    def __init__(__self__, *, create_time: _builtins.str, data_factory_location: _builtins.str, data_factory_name: _builtins.str, name: _builtins.str, subscription_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFactoryLocation")
    def data_factory_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFactoryName")
    def data_factory_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ManagedIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ..., user_assigned_identities: Optional[Mapping[str, outputs.UserAssignedManagedIdentityResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserAssignedManagedIdentityResponse]]:
        
        ...
    


@pulumi.output_type
class ManagedIntegrationRuntimeErrorResponse(dict):
    
    def __init__(__self__, *, code: _builtins.str, message: _builtins.str, parameters: Sequence[_builtins.str], time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ManagedIntegrationRuntimeNodeResponse(dict):
    
    def __init__(__self__, *, node_id: _builtins.str, status: _builtins.str, errors: Optional[Sequence[outputs.ManagedIntegrationRuntimeErrorResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[Sequence[outputs.ManagedIntegrationRuntimeErrorResponse]]:
        
        ...
    


@pulumi.output_type
class ManagedIntegrationRuntimeOperationResultResponse(dict):
    
    def __init__(__self__, *, activity_id: _builtins.str, error_code: _builtins.str, parameters: Sequence[_builtins.str], result: _builtins.str, start_time: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activityId")
    def activity_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def result(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ManagedIntegrationRuntimeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, type: _builtins.str, compute_properties: Optional[outputs.IntegrationRuntimeComputePropertiesResponse] = ..., customer_virtual_network: Optional[outputs.IntegrationRuntimeCustomerVirtualNetworkResponse] = ..., description: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., reference_name: Optional[_builtins.str] = ..., ssis_properties: Optional[outputs.IntegrationRuntimeSsisPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeProperties")
    def compute_properties(self) -> Optional[outputs.IntegrationRuntimeComputePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerVirtualNetwork")
    def customer_virtual_network(self) -> Optional[outputs.IntegrationRuntimeCustomerVirtualNetworkResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="referenceName")
    def reference_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssisProperties")
    def ssis_properties(self) -> Optional[outputs.IntegrationRuntimeSsisPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class ManagedIntegrationRuntimeStatusResponse(dict):
    
    def __init__(__self__, *, create_time: _builtins.str, data_factory_name: _builtins.str, last_operation: outputs.ManagedIntegrationRuntimeOperationResultResponse, nodes: Sequence[outputs.ManagedIntegrationRuntimeNodeResponse], other_errors: Sequence[outputs.ManagedIntegrationRuntimeErrorResponse], state: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFactoryName")
    def data_factory_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastOperation")
    def last_operation(self) -> outputs.ManagedIntegrationRuntimeOperationResultResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nodes(self) -> Sequence[outputs.ManagedIntegrationRuntimeNodeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="otherErrors")
    def other_errors(self) -> Sequence[outputs.ManagedIntegrationRuntimeErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ManagedVirtualNetworkSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_aad_tenant_ids_for_linking: Optional[Sequence[_builtins.str]] = ..., linked_access_check_on_target_resource: Optional[_builtins.bool] = ..., prevent_data_exfiltration: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedAadTenantIdsForLinking")
    def allowed_aad_tenant_ids_for_linking(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedAccessCheckOnTargetResource")
    def linked_access_check_on_target_resource(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preventDataExfiltration")
    def prevent_data_exfiltration(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class OptimizedAutoscaleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_enabled: _builtins.bool, maximum: _builtins.int, minimum: _builtins.int, version: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionForPrivateLinkHubBasicResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, provisioning_state: _builtins.str, private_endpoint: Optional[outputs.PrivateEndpointResponse] = ..., private_link_service_connection_state: Optional[outputs.PrivateLinkServiceConnectionStateResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[outputs.PrivateLinkServiceConnectionStateResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, provisioning_state: _builtins.str, type: _builtins.str, private_endpoint: Optional[outputs.PrivateEndpointResponse] = ..., private_link_service_connection_state: Optional[outputs.PrivateLinkServiceConnectionStateResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[outputs.PrivateLinkServiceConnectionStateResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions_required: _builtins.str, description: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PurviewConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, purview_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="purviewResourceId")
    def purview_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecureStringResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SelfHostedIntegrationRuntimeNodeResponse(dict):
    
    def __init__(__self__, *, capabilities: Mapping[str, _builtins.str], concurrent_jobs_limit: _builtins.int, expiry_time: _builtins.str, host_service_uri: _builtins.str, is_active_dispatcher: _builtins.bool, last_connect_time: _builtins.str, last_end_update_time: _builtins.str, last_start_time: _builtins.str, last_start_update_time: _builtins.str, last_stop_time: _builtins.str, last_update_result: _builtins.str, machine_name: _builtins.str, max_concurrent_jobs: _builtins.int, node_name: _builtins.str, register_time: _builtins.str, status: _builtins.str, version: _builtins.str, version_status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="concurrentJobsLimit")
    def concurrent_jobs_limit(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostServiceUri")
    def host_service_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isActiveDispatcher")
    def is_active_dispatcher(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastConnectTime")
    def last_connect_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastEndUpdateTime")
    def last_end_update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStartTime")
    def last_start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStartUpdateTime")
    def last_start_update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStopTime")
    def last_stop_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdateResult")
    def last_update_result(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentJobs")
    def max_concurrent_jobs(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registerTime")
    def register_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionStatus")
    def version_status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SelfHostedIntegrationRuntimeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, description: Optional[_builtins.str] = ..., linked_info: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedInfo")
    def linked_info(self) -> Optional[Any]:
        
        ...
    


@pulumi.output_type
class SelfHostedIntegrationRuntimeStatusResponse(dict):
    
    def __init__(__self__, *, auto_update: _builtins.str, auto_update_eta: _builtins.str, capabilities: Mapping[str, _builtins.str], create_time: _builtins.str, data_factory_name: _builtins.str, internal_channel_encryption: _builtins.str, latest_version: _builtins.str, local_time_zone_offset: _builtins.str, node_communication_channel_encryption_mode: _builtins.str, pushed_version: _builtins.str, scheduled_update_date: _builtins.str, service_urls: Sequence[_builtins.str], state: _builtins.str, task_queue_id: _builtins.str, type: _builtins.str, update_delay_offset: _builtins.str, version: _builtins.str, version_status: _builtins.str, links: Optional[Sequence[outputs.LinkedIntegrationRuntimeResponse]] = ..., nodes: Optional[Sequence[outputs.SelfHostedIntegrationRuntimeNodeResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdate")
    def auto_update(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateETA")
    def auto_update_eta(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFactoryName")
    def data_factory_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalChannelEncryption")
    def internal_channel_encryption(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestVersion")
    def latest_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localTimeZoneOffset")
    def local_time_zone_offset(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCommunicationChannelEncryptionMode")
    def node_communication_channel_encryption_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pushedVersion")
    def pushed_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledUpdateDate")
    def scheduled_update_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceUrls")
    def service_urls(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskQueueId")
    def task_queue_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateDelayOffset")
    def update_delay_offset(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionStatus")
    def version_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def links(self) -> Optional[Sequence[outputs.LinkedIntegrationRuntimeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nodes(self) -> Optional[Sequence[outputs.SelfHostedIntegrationRuntimeNodeResponse]]:
        
        ...
    


@pulumi.output_type
class SkuResponse(dict):
    
    def __init__(__self__, *, capacity: Optional[_builtins.int] = ..., name: Optional[_builtins.str] = ..., tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SparkConfigPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, time: _builtins.str, configuration_type: Optional[_builtins.str] = ..., content: Optional[_builtins.str] = ..., filename: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filename(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlPoolVulnerabilityAssessmentRuleBaselineItemResponse(dict):
    
    def __init__(__self__, *, result: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def result(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SsisEnvironmentReferenceResponse(dict):
    
    def __init__(__self__, *, environment_folder_name: Optional[_builtins.str] = ..., environment_name: Optional[_builtins.str] = ..., id: Optional[_builtins.float] = ..., reference_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentFolderName")
    def environment_folder_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="referenceType")
    def reference_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SsisEnvironmentResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str, description: Optional[_builtins.str] = ..., folder_id: Optional[_builtins.float] = ..., id: Optional[_builtins.float] = ..., name: Optional[_builtins.str] = ..., variables: Optional[Sequence[outputs.SsisVariableResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variables(self) -> Optional[Sequence[outputs.SsisVariableResponse]]:
        
        ...
    


@pulumi.output_type
class SsisFolderResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str, description: Optional[_builtins.str] = ..., id: Optional[_builtins.float] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SsisPackageResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str, description: Optional[_builtins.str] = ..., folder_id: Optional[_builtins.float] = ..., id: Optional[_builtins.float] = ..., name: Optional[_builtins.str] = ..., parameters: Optional[Sequence[outputs.SsisParameterResponse]] = ..., project_id: Optional[_builtins.float] = ..., project_version: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[outputs.SsisParameterResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectVersion")
    def project_version(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class SsisParameterResponse(dict):
    
    def __init__(__self__, *, data_type: Optional[_builtins.str] = ..., default_value: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., design_default_value: Optional[_builtins.str] = ..., id: Optional[_builtins.float] = ..., name: Optional[_builtins.str] = ..., required: Optional[_builtins.bool] = ..., sensitive: Optional[_builtins.bool] = ..., sensitive_default_value: Optional[_builtins.str] = ..., value_set: Optional[_builtins.bool] = ..., value_type: Optional[_builtins.str] = ..., variable: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="designDefaultValue")
    def design_default_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sensitive(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitiveDefaultValue")
    def sensitive_default_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueSet")
    def value_set(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SsisProjectResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str, description: Optional[_builtins.str] = ..., environment_refs: Optional[Sequence[outputs.SsisEnvironmentReferenceResponse]] = ..., folder_id: Optional[_builtins.float] = ..., id: Optional[_builtins.float] = ..., name: Optional[_builtins.str] = ..., parameters: Optional[Sequence[outputs.SsisParameterResponse]] = ..., version: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentRefs")
    def environment_refs(self) -> Optional[Sequence[outputs.SsisEnvironmentReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[outputs.SsisParameterResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class SsisVariableResponse(dict):
    
    def __init__(__self__, *, data_type: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., id: Optional[_builtins.float] = ..., name: Optional[_builtins.str] = ..., sensitive: Optional[_builtins.bool] = ..., sensitive_value: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sensitive(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitiveValue")
    def sensitive_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TableLevelSharingPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, external_tables_to_exclude: Optional[Sequence[_builtins.str]] = ..., external_tables_to_include: Optional[Sequence[_builtins.str]] = ..., materialized_views_to_exclude: Optional[Sequence[_builtins.str]] = ..., materialized_views_to_include: Optional[Sequence[_builtins.str]] = ..., tables_to_exclude: Optional[Sequence[_builtins.str]] = ..., tables_to_include: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalTablesToExclude")
    def external_tables_to_exclude(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalTablesToInclude")
    def external_tables_to_include(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="materializedViewsToExclude")
    def materialized_views_to_exclude(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="materializedViewsToInclude")
    def materialized_views_to_include(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tablesToExclude")
    def tables_to_exclude(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tablesToInclude")
    def tables_to_include(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class UserAssignedManagedIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, principal_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VirtualNetworkProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, compute_subnet_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeSubnetId")
    def compute_subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VulnerabilityAssessmentRecurringScansPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, email_subscription_admins: Optional[_builtins.bool] = ..., emails: Optional[Sequence[_builtins.str]] = ..., is_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailSubscriptionAdmins")
    def email_subscription_admins(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def emails(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class WorkspaceKeyDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_vault_url: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUrl")
    def key_vault_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkspaceRepositoryConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_name: Optional[_builtins.str] = ..., collaboration_branch: Optional[_builtins.str] = ..., host_name: Optional[_builtins.str] = ..., last_commit_id: Optional[_builtins.str] = ..., project_name: Optional[_builtins.str] = ..., repository_name: Optional[_builtins.str] = ..., root_folder: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collaborationBranch")
    def collaboration_branch(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastCommitId")
    def last_commit_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootFolder")
    def root_folder(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


