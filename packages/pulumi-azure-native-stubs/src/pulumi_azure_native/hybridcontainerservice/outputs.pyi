import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AADProfileResponseResponse",
    "AddonProfilesResponse",
    "AddonStatusResponse",
    "AgentPoolProvisioningStatusResponseError",
    ...,
    "AgentPoolProvisioningStatusResponseStatus",
    "AgentPoolResponseExtendedLocation",
    "ArcAgentProfileResponse",
    "ArcAgentStatusResponse",
    "CloudProviderProfileResponse",
    "CloudProviderProfileResponseInfraNetworkProfile",
    "CloudProviderProfileResponseInfraStorageProfile",
    ...,
    "ControlPlaneProfileResponse",
    "CredentialResultResponse",
    "ExtendedLocationResponse",
    "HttpProxyConfigResponseResponse",
    "KubernetesPatchVersionsResponse",
    "KubernetesVersionProfileResponseProperties",
    "KubernetesVersionPropertiesResponse",
    "KubernetesVersionReadinessResponse",
    "LinuxProfilePropertiesResponse",
    "LinuxProfilePropertiesResponsePublicKeys",
    "LinuxProfilePropertiesResponseSsh",
    "ListCredentialResponseResponseError",
    "ListCredentialResponseResponseProperties",
    "LoadBalancerProfileResponse",
    "NamedAgentPoolProfileResponse",
    "NetworkProfileResponse",
    "ProvisionedClusterIdentityResponse",
    "ProvisionedClustersCommonPropertiesResponseError",
    ...,
    ...,
    ...,
    "ProvisionedClustersCommonPropertiesResponseStatus",
    "ProvisionedClustersResponsePropertiesResponse",
    ...,
    "StorageSpacesPropertiesResponse",
    "StorageSpacesPropertiesResponseError",
    "StorageSpacesPropertiesResponseHciStorageProfile",
    "StorageSpacesPropertiesResponseProvisioningStatus",
    "StorageSpacesPropertiesResponseStatus",
    ...,
    "StorageSpacesResponseExtendedLocation",
    "SystemDataResponse",
    "VirtualNetworksPropertiesResponse",
    "VirtualNetworksPropertiesResponseError",
    "VirtualNetworksPropertiesResponseHci",
    "VirtualNetworksPropertiesResponseInfraVnetProfile",
    "VirtualNetworksPropertiesResponseNetworkCloud",
    ...,
    "VirtualNetworksPropertiesResponseStatus",
    "VirtualNetworksPropertiesResponseVipPool",
    "VirtualNetworksPropertiesResponseVmipPool",
    "VirtualNetworksPropertiesResponseVmware",
    "VirtualNetworksResponseExtendedLocation",
    "VmSkuCapabilitiesResponse",
    "VmSkuProfileResponseProperties",
    "VmSkuPropertiesResponse",
    "WindowsProfileResponseResponse",
]

@pulumi.output_type
class AADProfileResponseResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        admin_group_object_ids: Optional[Sequence[_builtins.str]] = ...,
        client_app_id: Optional[_builtins.str] = ...,
        enable_azure_rbac: Optional[_builtins.bool] = ...,
        managed: Optional[_builtins.bool] = ...,
        server_app_id: Optional[_builtins.str] = ...,
        tenant_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminGroupObjectIDs")
    def admin_group_object_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="clientAppID")
    def client_app_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableAzureRbac")
    def enable_azure_rbac(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def managed(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="serverAppID")
    def server_app_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantID")
    def tenant_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AddonProfilesResponse(dict):
    def __init__(
        __self__,
        *,
        config: Optional[Mapping[str, _builtins.str]] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AddonStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_message: Optional[_builtins.str] = ...,
        phase: Optional[_builtins.str] = ...,
        ready: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def phase(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ready(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AgentPoolProvisioningStatusResponseError(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentPoolProvisioningStatusResponseProvisioningStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error: Optional[outputs.AgentPoolProvisioningStatusResponseError] = ...,
        operation_id: Optional[_builtins.str] = ...,
        phase: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.AgentPoolProvisioningStatusResponseError]: ...
    @_builtins.property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def phase(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentPoolProvisioningStatusResponseStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_message: Optional[_builtins.str] = ...,
        provisioning_status: Optional[
            outputs.AgentPoolProvisioningStatusResponseProvisioningStatus
        ] = ...,
        ready_replicas: Optional[_builtins.int] = ...,
        replicas: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatus")
    def provisioning_status(
        self,
    ) -> Optional[outputs.AgentPoolProvisioningStatusResponseProvisioningStatus]: ...
    @_builtins.property
    @pulumi.getter(name="readyReplicas")
    def ready_replicas(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AgentPoolResponseExtendedLocation(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ArcAgentProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        agent_auto_upgrade: Optional[_builtins.str] = ...,
        agent_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentAutoUpgrade")
    def agent_auto_upgrade(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ArcAgentStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        agent_version: Optional[_builtins.str] = ...,
        core_count: Optional[_builtins.float] = ...,
        deployment_state: Optional[_builtins.str] = ...,
        error_message: Optional[_builtins.str] = ...,
        last_connectivity_time: Optional[_builtins.str] = ...,
        managed_identity_certificate_expiration_time: Optional[_builtins.str] = ...,
        onboarding_public_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentState")
    def deployment_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastConnectivityTime")
    def last_connectivity_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedIdentityCertificateExpirationTime")
    def managed_identity_certificate_expiration_time(
        self,
    ) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="onboardingPublicKey")
    def onboarding_public_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CloudProviderProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        infra_network_profile: Optional[
            outputs.CloudProviderProfileResponseInfraNetworkProfile
        ] = ...,
        infra_storage_profile: Optional[
            outputs.CloudProviderProfileResponseInfraStorageProfile
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="infraNetworkProfile")
    def infra_network_profile(
        self,
    ) -> Optional[outputs.CloudProviderProfileResponseInfraNetworkProfile]: ...
    @_builtins.property
    @pulumi.getter(name="infraStorageProfile")
    def infra_storage_profile(
        self,
    ) -> Optional[outputs.CloudProviderProfileResponseInfraStorageProfile]: ...

@pulumi.output_type
class CloudProviderProfileResponseInfraNetworkProfile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, vnet_subnet_ids: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vnetSubnetIds")
    def vnet_subnet_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CloudProviderProfileResponseInfraStorageProfile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, storage_space_ids: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageSpaceIds")
    def storage_space_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ControlPlaneEndpointProfileResponseControlPlaneEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_ip: Optional[_builtins.str] = ...,
        port: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostIP")
    def host_ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ControlPlaneProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        availability_zones: Optional[Sequence[_builtins.str]] = ...,
        cloud_provider_profile: Optional[outputs.CloudProviderProfileResponse] = ...,
        control_plane_endpoint: Optional[
            outputs.ControlPlaneEndpointProfileResponseControlPlaneEndpoint
        ] = ...,
        count: Optional[_builtins.int] = ...,
        linux_profile: Optional[outputs.LinuxProfilePropertiesResponse] = ...,
        max_count: Optional[_builtins.int] = ...,
        max_pods: Optional[_builtins.int] = ...,
        min_count: Optional[_builtins.int] = ...,
        mode: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        node_image_version: Optional[_builtins.str] = ...,
        node_labels: Optional[Mapping[str, _builtins.str]] = ...,
        node_taints: Optional[Sequence[_builtins.str]] = ...,
        os_type: Optional[_builtins.str] = ...,
        vm_size: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cloudProviderProfile")
    def cloud_provider_profile(
        self,
    ) -> Optional[outputs.CloudProviderProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneEndpoint")
    def control_plane_endpoint(
        self,
    ) -> Optional[outputs.ControlPlaneEndpointProfileResponseControlPlaneEndpoint]: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="linuxProfile")
    def linux_profile(self) -> Optional[outputs.LinuxProfilePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxPods")
    def max_pods(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeImageVersion")
    def node_image_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeLabels")
    def node_labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeTaints")
    def node_taints(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CredentialResultResponse(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class ExtendedLocationResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HttpProxyConfigResponseResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        http_proxy: Optional[_builtins.str] = ...,
        https_proxy: Optional[_builtins.str] = ...,
        no_proxy: Optional[Sequence[_builtins.str]] = ...,
        trusted_ca: Optional[_builtins.str] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpProxy")
    def http_proxy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpsProxy")
    def https_proxy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="noProxy")
    def no_proxy(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="trustedCa")
    def trusted_ca(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KubernetesPatchVersionsResponse(dict):
    def __init__(
        __self__,
        *,
        readiness: Optional[Sequence[outputs.KubernetesVersionReadinessResponse]] = ...,
        upgrades: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def readiness(
        self,
    ) -> Optional[Sequence[outputs.KubernetesVersionReadinessResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def upgrades(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class KubernetesVersionProfileResponseProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        values: Optional[Sequence[outputs.KubernetesVersionPropertiesResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[Sequence[outputs.KubernetesVersionPropertiesResponse]]: ...

@pulumi.output_type
class KubernetesVersionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_preview: _builtins.bool,
        patch_versions: Mapping[str, outputs.KubernetesPatchVersionsResponse],
        version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isPreview")
    def is_preview(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="patchVersions")
    def patch_versions(
        self,
    ) -> Mapping[str, outputs.KubernetesPatchVersionsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class KubernetesVersionReadinessResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_message: _builtins.str,
        os_type: Optional[_builtins.str] = ...,
        ready: _builtins.bool,
        os_sku: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ready(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="osSku")
    def os_sku(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LinuxProfilePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        admin_username: Optional[_builtins.str] = ...,
        ssh: Optional[outputs.LinuxProfilePropertiesResponseSsh] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ssh(self) -> Optional[outputs.LinuxProfilePropertiesResponseSsh]: ...

@pulumi.output_type
class LinuxProfilePropertiesResponsePublicKeys(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, key_data: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyData")
    def key_data(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LinuxProfilePropertiesResponseSsh(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        public_keys: Optional[
            Sequence[outputs.LinuxProfilePropertiesResponsePublicKeys]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(
        self,
    ) -> Optional[Sequence[outputs.LinuxProfilePropertiesResponsePublicKeys]]: ...

@pulumi.output_type
class ListCredentialResponseResponseError(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListCredentialResponseResponseProperties(dict):
    def __init__(
        __self__, *, kubeconfigs: Sequence[outputs.CredentialResultResponse]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kubeconfigs(self) -> Sequence[outputs.CredentialResultResponse]: ...

@pulumi.output_type
class LoadBalancerProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        availability_zones: Optional[Sequence[_builtins.str]] = ...,
        cloud_provider_profile: Optional[outputs.CloudProviderProfileResponse] = ...,
        count: Optional[_builtins.int] = ...,
        linux_profile: Optional[outputs.LinuxProfilePropertiesResponse] = ...,
        max_count: Optional[_builtins.int] = ...,
        max_pods: Optional[_builtins.int] = ...,
        min_count: Optional[_builtins.int] = ...,
        mode: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        node_image_version: Optional[_builtins.str] = ...,
        node_labels: Optional[Mapping[str, _builtins.str]] = ...,
        node_taints: Optional[Sequence[_builtins.str]] = ...,
        os_type: Optional[_builtins.str] = ...,
        vm_size: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cloudProviderProfile")
    def cloud_provider_profile(
        self,
    ) -> Optional[outputs.CloudProviderProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="linuxProfile")
    def linux_profile(self) -> Optional[outputs.LinuxProfilePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxPods")
    def max_pods(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeImageVersion")
    def node_image_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeLabels")
    def node_labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeTaints")
    def node_taints(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NamedAgentPoolProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        availability_zones: Optional[Sequence[_builtins.str]] = ...,
        cloud_provider_profile: Optional[outputs.CloudProviderProfileResponse] = ...,
        count: Optional[_builtins.int] = ...,
        max_count: Optional[_builtins.int] = ...,
        max_pods: Optional[_builtins.int] = ...,
        min_count: Optional[_builtins.int] = ...,
        mode: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        node_image_version: Optional[_builtins.str] = ...,
        node_labels: Optional[Mapping[str, _builtins.str]] = ...,
        node_taints: Optional[Sequence[_builtins.str]] = ...,
        os_type: Optional[_builtins.str] = ...,
        vm_size: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cloudProviderProfile")
    def cloud_provider_profile(
        self,
    ) -> Optional[outputs.CloudProviderProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxPods")
    def max_pods(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeImageVersion")
    def node_image_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeLabels")
    def node_labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeTaints")
    def node_taints(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NetworkProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_service_ip: Optional[_builtins.str] = ...,
        load_balancer_profile: Optional[outputs.LoadBalancerProfileResponse] = ...,
        load_balancer_sku: Optional[_builtins.str] = ...,
        network_policy: Optional[_builtins.str] = ...,
        pod_cidr: Optional[_builtins.str] = ...,
        pod_cidrs: Optional[Sequence[_builtins.str]] = ...,
        service_cidr: Optional[_builtins.str] = ...,
        service_cidrs: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsServiceIP")
    def dns_service_ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerProfile")
    def load_balancer_profile(
        self,
    ) -> Optional[outputs.LoadBalancerProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerSku")
    def load_balancer_sku(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkPolicy")
    def network_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="podCidr")
    def pod_cidr(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="podCidrs")
    def pod_cidrs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceCidr")
    def service_cidr(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceCidrs")
    def service_cidrs(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ProvisionedClusterIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ProvisionedClustersCommonPropertiesResponseError(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProvisionedClustersCommonPropertiesResponseFeatures(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, arc_agent_profile: Optional[outputs.ArcAgentProfileResponse] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="arcAgentProfile")
    def arc_agent_profile(self) -> Optional[outputs.ArcAgentProfileResponse]: ...

@pulumi.output_type
class ProvisionedClustersCommonPropertiesResponseFeaturesStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, arc_agent_status: Optional[outputs.ArcAgentStatusResponse] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="arcAgentStatus")
    def arc_agent_status(self) -> Optional[outputs.ArcAgentStatusResponse]: ...

@pulumi.output_type
class ProvisionedClustersCommonPropertiesResponseProvisioningStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error: Optional[outputs.ProvisionedClustersCommonPropertiesResponseError] = ...,
        operation_id: Optional[_builtins.str] = ...,
        phase: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(
        self,
    ) -> Optional[outputs.ProvisionedClustersCommonPropertiesResponseError]: ...
    @_builtins.property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def phase(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProvisionedClustersCommonPropertiesResponseStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        addon_status: Optional[Mapping[str, outputs.AddonStatusResponse]] = ...,
        error_message: Optional[_builtins.str] = ...,
        features_status: Optional[
            outputs.ProvisionedClustersCommonPropertiesResponseFeaturesStatus
        ] = ...,
        provisioning_status: Optional[
            outputs.ProvisionedClustersCommonPropertiesResponseProvisioningStatus
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addonStatus")
    def addon_status(self) -> Optional[Mapping[str, outputs.AddonStatusResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="featuresStatus")
    def features_status(
        self,
    ) -> Optional[
        outputs.ProvisionedClustersCommonPropertiesResponseFeaturesStatus
    ]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatus")
    def provisioning_status(
        self,
    ) -> Optional[
        outputs.ProvisionedClustersCommonPropertiesResponseProvisioningStatus
    ]: ...

@pulumi.output_type
class ProvisionedClustersResponsePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        status: outputs.ProvisionedClustersCommonPropertiesResponseStatus,
        aad_profile: Optional[outputs.AADProfileResponseResponse] = ...,
        addon_profiles: Optional[Mapping[str, outputs.AddonProfilesResponse]] = ...,
        agent_pool_profiles: Optional[
            Sequence[outputs.NamedAgentPoolProfileResponse]
        ] = ...,
        cloud_provider_profile: Optional[outputs.CloudProviderProfileResponse] = ...,
        control_plane: Optional[outputs.ControlPlaneProfileResponse] = ...,
        enable_rbac: Optional[_builtins.bool] = ...,
        features: Optional[
            outputs.ProvisionedClustersCommonPropertiesResponseFeatures
        ] = ...,
        http_proxy_config: Optional[outputs.HttpProxyConfigResponseResponse] = ...,
        kubernetes_version: Optional[_builtins.str] = ...,
        linux_profile: Optional[outputs.LinuxProfilePropertiesResponse] = ...,
        network_profile: Optional[outputs.NetworkProfileResponse] = ...,
        node_resource_group: Optional[_builtins.str] = ...,
        windows_profile: Optional[outputs.WindowsProfileResponseResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.ProvisionedClustersCommonPropertiesResponseStatus: ...
    @_builtins.property
    @pulumi.getter(name="aadProfile")
    def aad_profile(self) -> Optional[outputs.AADProfileResponseResponse]: ...
    @_builtins.property
    @pulumi.getter(name="addonProfiles")
    def addon_profiles(
        self,
    ) -> Optional[Mapping[str, outputs.AddonProfilesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="agentPoolProfiles")
    def agent_pool_profiles(
        self,
    ) -> Optional[Sequence[outputs.NamedAgentPoolProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="cloudProviderProfile")
    def cloud_provider_profile(
        self,
    ) -> Optional[outputs.CloudProviderProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> Optional[outputs.ControlPlaneProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="enableRbac")
    def enable_rbac(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def features(
        self,
    ) -> Optional[outputs.ProvisionedClustersCommonPropertiesResponseFeatures]: ...
    @_builtins.property
    @pulumi.getter(name="httpProxyConfig")
    def http_proxy_config(
        self,
    ) -> Optional[outputs.HttpProxyConfigResponseResponse]: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linuxProfile")
    def linux_profile(self) -> Optional[outputs.LinuxProfilePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[outputs.NetworkProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="nodeResourceGroup")
    def node_resource_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="windowsProfile")
    def windows_profile(self) -> Optional[outputs.WindowsProfileResponseResponse]: ...

@pulumi.output_type
class ProvisionedClustersResponseResponseExtendedLocation(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageSpacesPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        hci_storage_profile: Optional[
            outputs.StorageSpacesPropertiesResponseHciStorageProfile
        ] = ...,
        status: Optional[outputs.StorageSpacesPropertiesResponseStatus] = ...,
        vmware_storage_profile: Optional[
            outputs.StorageSpacesPropertiesResponseVmwareStorageProfile
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hciStorageProfile")
    def hci_storage_profile(
        self,
    ) -> Optional[outputs.StorageSpacesPropertiesResponseHciStorageProfile]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[outputs.StorageSpacesPropertiesResponseStatus]: ...
    @_builtins.property
    @pulumi.getter(name="vmwareStorageProfile")
    def vmware_storage_profile(
        self,
    ) -> Optional[outputs.StorageSpacesPropertiesResponseVmwareStorageProfile]: ...

@pulumi.output_type
class StorageSpacesPropertiesResponseError(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageSpacesPropertiesResponseHciStorageProfile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        moc_group: Optional[_builtins.str] = ...,
        moc_location: Optional[_builtins.str] = ...,
        moc_storage_container: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mocGroup")
    def moc_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mocLocation")
    def moc_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mocStorageContainer")
    def moc_storage_container(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageSpacesPropertiesResponseProvisioningStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error: Optional[outputs.StorageSpacesPropertiesResponseError] = ...,
        operation_id: Optional[_builtins.str] = ...,
        phase: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.StorageSpacesPropertiesResponseError]: ...
    @_builtins.property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def phase(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageSpacesPropertiesResponseStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_status: Optional[
            outputs.StorageSpacesPropertiesResponseProvisioningStatus
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatus")
    def provisioning_status(
        self,
    ) -> Optional[outputs.StorageSpacesPropertiesResponseProvisioningStatus]: ...

@pulumi.output_type
class StorageSpacesPropertiesResponseVmwareStorageProfile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        datacenter: Optional[_builtins.str] = ...,
        datastore: Optional[_builtins.str] = ...,
        folder: Optional[_builtins.str] = ...,
        resource_pool: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def datacenter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def datastore(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourcePool")
    def resource_pool(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageSpacesResponseExtendedLocation(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

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
class VirtualNetworksPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dhcp_servers: Sequence[_builtins.str],
        provisioning_state: _builtins.str,
        status: outputs.VirtualNetworksPropertiesResponseStatus,
        vlan_id: _builtins.str,
        dns_servers: Optional[Sequence[_builtins.str]] = ...,
        gateway: Optional[_builtins.str] = ...,
        infra_vnet_profile: Optional[
            outputs.VirtualNetworksPropertiesResponseInfraVnetProfile
        ] = ...,
        ip_address_prefix: Optional[_builtins.str] = ...,
        vip_pool: Optional[
            Sequence[outputs.VirtualNetworksPropertiesResponseVipPool]
        ] = ...,
        vmip_pool: Optional[
            Sequence[outputs.VirtualNetworksPropertiesResponseVmipPool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dhcpServers")
    def dhcp_servers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.VirtualNetworksPropertiesResponseStatus: ...
    @_builtins.property
    @pulumi.getter(name="vlanID")
    def vlan_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="infraVnetProfile")
    def infra_vnet_profile(
        self,
    ) -> Optional[outputs.VirtualNetworksPropertiesResponseInfraVnetProfile]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressPrefix")
    def ip_address_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vipPool")
    def vip_pool(
        self,
    ) -> Optional[Sequence[outputs.VirtualNetworksPropertiesResponseVipPool]]: ...
    @_builtins.property
    @pulumi.getter(name="vmipPool")
    def vmip_pool(
        self,
    ) -> Optional[Sequence[outputs.VirtualNetworksPropertiesResponseVmipPool]]: ...

@pulumi.output_type
class VirtualNetworksPropertiesResponseError(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualNetworksPropertiesResponseHci(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        moc_group: Optional[_builtins.str] = ...,
        moc_location: Optional[_builtins.str] = ...,
        moc_vnet_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mocGroup")
    def moc_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mocLocation")
    def moc_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mocVnetName")
    def moc_vnet_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualNetworksPropertiesResponseInfraVnetProfile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hci: Optional[outputs.VirtualNetworksPropertiesResponseHci] = ...,
        network_cloud: Optional[
            outputs.VirtualNetworksPropertiesResponseNetworkCloud
        ] = ...,
        vmware: Optional[outputs.VirtualNetworksPropertiesResponseVmware] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hci(self) -> Optional[outputs.VirtualNetworksPropertiesResponseHci]: ...
    @_builtins.property
    @pulumi.getter(name="networkCloud")
    def network_cloud(
        self,
    ) -> Optional[outputs.VirtualNetworksPropertiesResponseNetworkCloud]: ...
    @_builtins.property
    @pulumi.getter
    def vmware(self) -> Optional[outputs.VirtualNetworksPropertiesResponseVmware]: ...

@pulumi.output_type
class VirtualNetworksPropertiesResponseNetworkCloud(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, network_id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualNetworksPropertiesResponseProvisioningStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error: Optional[outputs.VirtualNetworksPropertiesResponseError] = ...,
        operation_id: Optional[_builtins.str] = ...,
        phase: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.VirtualNetworksPropertiesResponseError]: ...
    @_builtins.property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def phase(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualNetworksPropertiesResponseStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_status: Optional[
            outputs.VirtualNetworksPropertiesResponseProvisioningStatus
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatus")
    def provisioning_status(
        self,
    ) -> Optional[outputs.VirtualNetworksPropertiesResponseProvisioningStatus]: ...

@pulumi.output_type
class VirtualNetworksPropertiesResponseVipPool(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_ip: Optional[_builtins.str] = ...,
        start_ip: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endIP")
    def end_ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startIP")
    def start_ip(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualNetworksPropertiesResponseVmipPool(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_ip: Optional[_builtins.str] = ...,
        start_ip: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endIP")
    def end_ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startIP")
    def start_ip(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualNetworksPropertiesResponseVmware(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, segment_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="segmentName")
    def segment_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualNetworksResponseExtendedLocation(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VmSkuCapabilitiesResponse(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class VmSkuProfileResponseProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        values: Optional[Sequence[outputs.VmSkuPropertiesResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[outputs.VmSkuPropertiesResponse]]: ...

@pulumi.output_type
class VmSkuPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capabilities: Sequence[outputs.VmSkuCapabilitiesResponse],
        name: _builtins.str,
        resource_type: _builtins.str,
        size: _builtins.str,
        tier: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Sequence[outputs.VmSkuCapabilitiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str: ...

@pulumi.output_type
class WindowsProfileResponseResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        admin_username: Optional[_builtins.str] = ...,
        enable_csi_proxy: Optional[_builtins.bool] = ...,
        license_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableCsiProxy")
    def enable_csi_proxy(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[_builtins.str]: ...
