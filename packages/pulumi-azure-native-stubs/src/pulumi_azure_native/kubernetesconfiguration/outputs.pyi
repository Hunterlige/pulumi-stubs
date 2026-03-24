

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
__all__ = ['AzureBlobDefinitionResponse', 'BucketDefinitionResponse', 'ComplianceStatusResponse', 'ErrorAdditionalInfoResponse', 'ErrorDetailResponse', 'ExtensionResponseAksAssignedIdentity', 'ExtensionStatusResponse', 'GitRepositoryDefinitionResponse', 'HelmOperatorPropertiesResponse', 'HelmReleasePropertiesDefinitionResponse', 'IdentityResponse', ..., 'KustomizationDefinitionResponse', 'ManagedIdentityDefinitionResponse', 'ObjectReferenceDefinitionResponse', 'ObjectStatusConditionDefinitionResponse', 'ObjectStatusDefinitionResponse', 'PlanResponse', 'PostBuildDefinitionResponse', 'PrivateEndpointConnectionResponse', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', 'RepositoryRefDefinitionResponse', 'ScopeClusterResponse', 'ScopeNamespaceResponse', 'ScopeResponse', 'ServicePrincipalDefinitionResponse', 'SubstituteFromDefinitionResponse', 'SystemDataResponse']
@pulumi.output_type
class AzureBlobDefinitionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_key: Optional[_builtins.str] = ..., container_name: Optional[_builtins.str] = ..., local_auth_ref: Optional[_builtins.str] = ..., managed_identity: Optional[outputs.ManagedIdentityDefinitionResponse] = ..., sas_token: Optional[_builtins.str] = ..., service_principal: Optional[outputs.ServicePrincipalDefinitionResponse] = ..., sync_interval_in_seconds: Optional[_builtins.float] = ..., timeout_in_seconds: Optional[_builtins.float] = ..., url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localAuthRef")
    def local_auth_ref(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[outputs.ManagedIdentityDefinitionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasToken")
    def sas_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicePrincipal")
    def service_principal(self) -> Optional[outputs.ServicePrincipalDefinitionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncIntervalInSeconds")
    def sync_interval_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BucketDefinitionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_key: Optional[_builtins.str] = ..., bucket_name: Optional[_builtins.str] = ..., insecure: Optional[_builtins.bool] = ..., local_auth_ref: Optional[_builtins.str] = ..., sync_interval_in_seconds: Optional[_builtins.float] = ..., timeout_in_seconds: Optional[_builtins.float] = ..., url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def insecure(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localAuthRef")
    def local_auth_ref(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncIntervalInSeconds")
    def sync_interval_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ComplianceStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, compliance_state: _builtins.str, last_config_applied: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., message_level: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceState")
    def compliance_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastConfigApplied")
    def last_config_applied(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageLevel")
    def message_level(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ErrorAdditionalInfoResponse(dict):
    
    def __init__(__self__, *, info: Any, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def info(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ErrorDetailResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_info: Sequence[outputs.ErrorAdditionalInfoResponse], code: _builtins.str, details: Sequence[outputs.ErrorDetailResponse], message: _builtins.str, target: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence[outputs.ErrorAdditionalInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ExtensionResponseAksAssignedIdentity(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ...) -> None:
        
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
    


@pulumi.output_type
class ExtensionStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, code: Optional[_builtins.str] = ..., display_status: Optional[_builtins.str] = ..., level: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayStatus")
    def display_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GitRepositoryDefinitionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, https_ca_cert: Optional[_builtins.str] = ..., https_user: Optional[_builtins.str] = ..., local_auth_ref: Optional[_builtins.str] = ..., repository_ref: Optional[outputs.RepositoryRefDefinitionResponse] = ..., ssh_known_hosts: Optional[_builtins.str] = ..., sync_interval_in_seconds: Optional[_builtins.float] = ..., timeout_in_seconds: Optional[_builtins.float] = ..., url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsCACert")
    def https_ca_cert(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsUser")
    def https_user(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localAuthRef")
    def local_auth_ref(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryRef")
    def repository_ref(self) -> Optional[outputs.RepositoryRefDefinitionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sshKnownHosts")
    def ssh_known_hosts(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncIntervalInSeconds")
    def sync_interval_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HelmOperatorPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, chart_values: Optional[_builtins.str] = ..., chart_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="chartValues")
    def chart_values(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="chartVersion")
    def chart_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HelmReleasePropertiesDefinitionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_count: Optional[_builtins.float] = ..., helm_chart_ref: Optional[outputs.ObjectReferenceDefinitionResponse] = ..., install_failure_count: Optional[_builtins.float] = ..., last_revision_applied: Optional[_builtins.float] = ..., upgrade_failure_count: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureCount")
    def failure_count(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="helmChartRef")
    def helm_chart_ref(self) -> Optional[outputs.ObjectReferenceDefinitionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="installFailureCount")
    def install_failure_count(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRevisionApplied")
    def last_revision_applied(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeFailureCount")
    def upgrade_failure_count(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class IdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ...) -> None:
        
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
    


@pulumi.output_type
class KubernetesConfigurationPrivateLinkScopePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_resource_id: _builtins.str, private_endpoint_connections: Sequence[outputs.PrivateEndpointConnectionResponse], private_link_scope_id: _builtins.str, provisioning_state: _builtins.str, public_network_access: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkScopeId")
    def private_link_scope_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class KustomizationDefinitionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, depends_on: Optional[Sequence[_builtins.str]] = ..., force: Optional[_builtins.bool] = ..., path: Optional[_builtins.str] = ..., post_build: Optional[outputs.PostBuildDefinitionResponse] = ..., prune: Optional[_builtins.bool] = ..., retry_interval_in_seconds: Optional[_builtins.float] = ..., sync_interval_in_seconds: Optional[_builtins.float] = ..., timeout_in_seconds: Optional[_builtins.float] = ..., wait: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependsOn")
    def depends_on(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def force(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postBuild")
    def post_build(self) -> Optional[outputs.PostBuildDefinitionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prune(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryIntervalInSeconds")
    def retry_interval_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncIntervalInSeconds")
    def sync_interval_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def wait(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ManagedIdentityDefinitionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ObjectReferenceDefinitionResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., namespace: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ObjectStatusConditionDefinitionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ObjectStatusDefinitionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, applied_by: Optional[outputs.ObjectReferenceDefinitionResponse] = ..., compliance_state: Optional[_builtins.str] = ..., helm_release_properties: Optional[outputs.HelmReleasePropertiesDefinitionResponse] = ..., kind: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., namespace: Optional[_builtins.str] = ..., status_conditions: Optional[Sequence[outputs.ObjectStatusConditionDefinitionResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliedBy")
    def applied_by(self) -> Optional[outputs.ObjectReferenceDefinitionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceState")
    def compliance_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="helmReleaseProperties")
    def helm_release_properties(self) -> Optional[outputs.HelmReleasePropertiesDefinitionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusConditions")
    def status_conditions(self) -> Optional[Sequence[outputs.ObjectStatusConditionDefinitionResponse]]:
        
        ...
    


@pulumi.output_type
class PlanResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, product: _builtins.str, publisher: _builtins.str, promotion_code: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def product(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PostBuildDefinitionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, substitute: Optional[Mapping[str, _builtins.str]] = ..., substitute_from: Optional[Sequence[outputs.SubstituteFromDefinitionResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def substitute(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="substituteFrom")
    def substitute_from(self) -> Optional[Sequence[outputs.SubstituteFromDefinitionResponse]]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse, provisioning_state: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...) -> None:
        
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
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> outputs.PrivateLinkServiceConnectionStateResponse:
        
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
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]:
        
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
    
    def __init__(__self__, *, actions_required: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]:
        
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
class RepositoryRefDefinitionResponse(dict):
    
    def __init__(__self__, *, branch: Optional[_builtins.str] = ..., commit: Optional[_builtins.str] = ..., semver: Optional[_builtins.str] = ..., tag: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def semver(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ScopeClusterResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, release_namespace: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseNamespace")
    def release_namespace(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ScopeNamespaceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_namespace: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNamespace")
    def target_namespace(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ScopeResponse(dict):
    
    def __init__(__self__, *, cluster: Optional[outputs.ScopeClusterResponse] = ..., namespace: Optional[outputs.ScopeNamespaceResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[outputs.ScopeClusterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[outputs.ScopeNamespaceResponse]:
        
        ...
    


@pulumi.output_type
class ServicePrincipalDefinitionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_certificate: Optional[_builtins.str] = ..., client_certificate_password: Optional[_builtins.str] = ..., client_certificate_send_chain: Optional[_builtins.bool] = ..., client_id: Optional[_builtins.str] = ..., client_secret: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificatePassword")
    def client_certificate_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificateSendChain")
    def client_certificate_send_chain(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SubstituteFromDefinitionResponse(dict):
    
    def __init__(__self__, *, kind: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., optional: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def optional(self) -> Optional[_builtins.bool]:
        
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
    


