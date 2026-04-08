import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AcceleratorBasicAuthSettingResponse",
    "AcceleratorGitRepositoryResponse",
    "AcceleratorPublicSettingResponse",
    "AcceleratorSshSettingResponse",
    "ApiPortalCustomDomainPropertiesResponse",
    "ApiPortalInstanceResponse",
    "ApiPortalPropertiesResponse",
    "ApiPortalResourceRequestsResponse",
    "ApmPropertiesResponse",
    "ApmReferenceResponse",
    "AppResourcePropertiesResponse",
    "AppVNetAddonsResponse",
    "ApplicationAcceleratorComponentResponse",
    "ApplicationAcceleratorInstanceResponse",
    "ApplicationAcceleratorPropertiesResponse",
    "ApplicationAcceleratorResourceRequestsResponse",
    "ApplicationInsightsAgentVersionsResponse",
    "ApplicationLiveViewComponentResponse",
    "ApplicationLiveViewInstanceResponse",
    "ApplicationLiveViewPropertiesResponse",
    "ApplicationLiveViewResourceRequestsResponse",
    "AzureFileVolumeResponse",
    "BindingResourcePropertiesResponse",
    "BuildPropertiesResponse",
    "BuildResourceRequestsResponse",
    "BuildResultUserSourceInfoResponse",
    "BuildServiceAgentPoolPropertiesResponse",
    "BuildServiceAgentPoolSizePropertiesResponse",
    "BuilderPropertiesResponse",
    "BuildpackBindingLaunchPropertiesResponse",
    "BuildpackBindingPropertiesResponse",
    "BuildpackPropertiesResponse",
    "BuildpacksGroupPropertiesResponse",
    "CertificateReferenceResponse",
    "ClusterResourcePropertiesResponse",
    "ConfigServerGitPropertyResponse",
    "ConfigServerPropertiesResponse",
    "ConfigServerSettingsResponse",
    "ConfigurationServiceGitPropertyResponse",
    "ConfigurationServiceGitRepositoryResponse",
    "ConfigurationServiceInstanceResponse",
    "ConfigurationServicePropertiesResponse",
    "ConfigurationServiceResourceRequestsResponse",
    "ConfigurationServiceSettingsResponse",
    "ContainerProbeSettingsResponse",
    "ContainerRegistryBasicCredentialsResponse",
    "ContainerRegistryPropertiesResponse",
    "ContentCertificatePropertiesResponse",
    "CustomContainerResponse",
    "CustomContainerUserSourceInfoResponse",
    "CustomDomainPropertiesResponse",
    "CustomPersistentDiskResourceResponse",
    "CustomScaleRuleResponse",
    "CustomizedAcceleratorPropertiesResponse",
    "DeploymentInstanceResponse",
    "DeploymentResourcePropertiesResponse",
    "DeploymentSettingsResponse",
    "DevToolPortalComponentResponse",
    "DevToolPortalFeatureDetailResponse",
    "DevToolPortalFeatureSettingsResponse",
    "DevToolPortalInstanceResponse",
    "DevToolPortalPropertiesResponse",
    "DevToolPortalResourceRequestsResponse",
    "DevToolPortalSsoPropertiesResponse",
    "EnvVarResponse",
    "ErrorResponse",
    "ExecActionResponse",
    "GatewayApiMetadataPropertiesResponse",
    "GatewayApiRouteResponse",
    "GatewayCorsPropertiesResponse",
    "GatewayCustomDomainPropertiesResponse",
    "GatewayInstanceResponse",
    ...,
    ...,
    "GatewayOperatorPropertiesResponse",
    "GatewayOperatorResourceRequestsResponse",
    "GatewayPropertiesResponse",
    "GatewayPropertiesResponseClientAuth",
    "GatewayPropertiesResponseEnvironmentVariables",
    "GatewayResourceRequestsResponse",
    "GatewayRouteConfigOpenApiPropertiesResponse",
    "GatewayRouteConfigPropertiesResponse",
    "GitPatternRepositoryResponse",
    "HTTPGetActionResponse",
    "HttpScaleRuleResponse",
    "ImageRegistryCredentialResponse",
    "IngressConfigResponse",
    "IngressSettingsResponse",
    "IngressSettingsResponseClientAuth",
    "JarUploadedUserSourceInfoResponse",
    "JobExecutionTemplateResponse",
    "JobResourcePropertiesResponse",
    "JobResourceRequestsResponse",
    "KeyVaultCertificatePropertiesResponse",
    "LoadedCertificateResponse",
    "ManagedComponentReferenceResponse",
    "ManagedIdentityPropertiesResponse",
    "ManualJobTriggerConfigResponse",
    "MarketplaceResourceResponse",
    "MonitoringSettingPropertiesResponse",
    "NetCoreZipUploadedUserSourceInfoResponse",
    "NetworkProfileResponse",
    "NetworkProfileResponseOutboundIPs",
    "PersistentDiskResponse",
    "ProbeResponse",
    "QueueScaleRuleResponse",
    "RequiredTrafficResponse",
    "ResourceRequestsResponse",
    "ScaleResponse",
    "ScaleRuleAuthResponse",
    "ScaleRuleResponse",
    "SecretResponse",
    "ServiceRegistryInstanceResponse",
    "ServiceRegistryPropertiesResponse",
    "ServiceRegistryResourceRequestsResponse",
    "ServiceVNetAddonsResponse",
    "SkuResponse",
    "SourceUploadedUserSourceInfoResponse",
    "SsoPropertiesResponse",
    "StackPropertiesResponse",
    "StorageAccountResponse",
    "SystemDataResponse",
    "TCPSocketActionResponse",
    "TcpScaleRuleResponse",
    "TemporaryDiskResponse",
    "TriggeredBuildResultResponse",
    "UploadedUserSourceInfoResponse",
    "UserAssignedManagedIdentityResponse",
    "WarUploadedUserSourceInfoResponse",
    "WeeklyMaintenanceScheduleConfigurationResponse",
]

@pulumi.output_type
class AcceleratorBasicAuthSettingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_type: _builtins.str,
        username: _builtins.str,
        ca_cert_resource_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="caCertResourceId")
    def ca_cert_resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AcceleratorGitRepositoryResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_setting: Any,
        url: _builtins.str,
        branch: Optional[_builtins.str] = ...,
        commit: Optional[_builtins.str] = ...,
        git_tag: Optional[_builtins.str] = ...,
        interval_in_seconds: Optional[_builtins.int] = ...,
        sub_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authSetting")
    def auth_setting(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def commit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gitTag")
    def git_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="intervalInSeconds")
    def interval_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AcceleratorPublicSettingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_type: _builtins.str,
        ca_cert_resource_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="caCertResourceId")
    def ca_cert_resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AcceleratorSshSettingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, auth_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str: ...

@pulumi.output_type
class ApiPortalCustomDomainPropertiesResponse(dict):
    def __init__(__self__, *, thumbprint: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApiPortalInstanceResponse(dict):
    def __init__(__self__, *, name: _builtins.str, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class ApiPortalPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instances: Sequence[outputs.ApiPortalInstanceResponse],
        provisioning_state: _builtins.str,
        resource_requests: outputs.ApiPortalResourceRequestsResponse,
        url: _builtins.str,
        api_try_out_enabled_state: Optional[_builtins.str] = ...,
        gateway_ids: Optional[Sequence[_builtins.str]] = ...,
        https_only: Optional[_builtins.bool] = ...,
        public: Optional[_builtins.bool] = ...,
        source_urls: Optional[Sequence[_builtins.str]] = ...,
        sso_properties: Optional[outputs.SsoPropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[outputs.ApiPortalInstanceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceRequests")
    def resource_requests(self) -> outputs.ApiPortalResourceRequestsResponse: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="apiTryOutEnabledState")
    def api_try_out_enabled_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gatewayIds")
    def gateway_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="httpsOnly")
    def https_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def public(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sourceUrls")
    def source_urls(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ssoProperties")
    def sso_properties(self) -> Optional[outputs.SsoPropertiesResponse]: ...

@pulumi.output_type
class ApiPortalResourceRequestsResponse(dict):
    def __init__(__self__, *, cpu: _builtins.str, memory: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> _builtins.str: ...

@pulumi.output_type
class ApmPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        type: _builtins.str,
        properties: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ApmReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str: ...

@pulumi.output_type
class AppResourcePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fqdn: _builtins.str,
        provisioning_state: _builtins.str,
        url: _builtins.str,
        addon_configs: Optional[Mapping[str, Any]] = ...,
        custom_persistent_disks: Optional[
            Sequence[outputs.CustomPersistentDiskResourceResponse]
        ] = ...,
        enable_end_to_end_tls: Optional[_builtins.bool] = ...,
        https_only: Optional[_builtins.bool] = ...,
        ingress_settings: Optional[outputs.IngressSettingsResponse] = ...,
        loaded_certificates: Optional[
            Sequence[outputs.LoadedCertificateResponse]
        ] = ...,
        persistent_disk: Optional[outputs.PersistentDiskResponse] = ...,
        public: Optional[_builtins.bool] = ...,
        secrets: Optional[Sequence[outputs.SecretResponse]] = ...,
        temporary_disk: Optional[outputs.TemporaryDiskResponse] = ...,
        test_endpoint_auth_state: Optional[_builtins.str] = ...,
        vnet_addons: Optional[outputs.AppVNetAddonsResponse] = ...,
        workload_profile_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addonConfigs")
    def addon_configs(self) -> Optional[Mapping[str, Any]]: ...
    @_builtins.property
    @pulumi.getter(name="customPersistentDisks")
    def custom_persistent_disks(
        self,
    ) -> Optional[Sequence[outputs.CustomPersistentDiskResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="enableEndToEndTLS")
    def enable_end_to_end_tls(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="httpsOnly")
    def https_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ingressSettings")
    def ingress_settings(self) -> Optional[outputs.IngressSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="loadedCertificates")
    def loaded_certificates(
        self,
    ) -> Optional[Sequence[outputs.LoadedCertificateResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="persistentDisk")
    def persistent_disk(self) -> Optional[outputs.PersistentDiskResponse]: ...
    @_builtins.property
    @pulumi.getter
    def public(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[Sequence[outputs.SecretResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="temporaryDisk")
    def temporary_disk(self) -> Optional[outputs.TemporaryDiskResponse]: ...
    @_builtins.property
    @pulumi.getter(name="testEndpointAuthState")
    def test_endpoint_auth_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vnetAddons")
    def vnet_addons(self) -> Optional[outputs.AppVNetAddonsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="workloadProfileName")
    def workload_profile_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppVNetAddonsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        public_endpoint_url: _builtins.str,
        public_endpoint: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicEndpointUrl")
    def public_endpoint_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicEndpoint")
    def public_endpoint(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ApplicationAcceleratorComponentResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instances: Sequence[outputs.ApplicationAcceleratorInstanceResponse],
        name: _builtins.str,
        resource_requests: Optional[
            outputs.ApplicationAcceleratorResourceRequestsResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[outputs.ApplicationAcceleratorInstanceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceRequests")
    def resource_requests(
        self,
    ) -> Optional[outputs.ApplicationAcceleratorResourceRequestsResponse]: ...

@pulumi.output_type
class ApplicationAcceleratorInstanceResponse(dict):
    def __init__(__self__, *, name: _builtins.str, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationAcceleratorPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        components: Sequence[outputs.ApplicationAcceleratorComponentResponse],
        provisioning_state: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def components(
        self,
    ) -> Sequence[outputs.ApplicationAcceleratorComponentResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationAcceleratorResourceRequestsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cpu: _builtins.str,
        instance_count: _builtins.int,
        memory: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationInsightsAgentVersionsResponse(dict):
    def __init__(__self__, *, java: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def java(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationLiveViewComponentResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instances: Sequence[outputs.ApplicationLiveViewInstanceResponse],
        name: Any,
        resource_requests: outputs.ApplicationLiveViewResourceRequestsResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[outputs.ApplicationLiveViewInstanceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="resourceRequests")
    def resource_requests(
        self,
    ) -> outputs.ApplicationLiveViewResourceRequestsResponse: ...

@pulumi.output_type
class ApplicationLiveViewInstanceResponse(dict):
    def __init__(__self__, *, name: _builtins.str, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationLiveViewPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        components: Sequence[outputs.ApplicationLiveViewComponentResponse],
        provisioning_state: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> Sequence[outputs.ApplicationLiveViewComponentResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationLiveViewResourceRequestsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cpu: _builtins.str,
        instance_count: _builtins.int,
        memory: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> _builtins.str: ...

@pulumi.output_type
class AzureFileVolumeResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mount_path: _builtins.str,
        type: _builtins.str,
        enable_sub_path: Optional[_builtins.bool] = ...,
        mount_options: Optional[Sequence[_builtins.str]] = ...,
        read_only: Optional[_builtins.bool] = ...,
        share_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enableSubPath")
    def enable_sub_path(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BindingResourcePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: _builtins.str,
        generated_properties: _builtins.str,
        resource_name: _builtins.str,
        resource_type: _builtins.str,
        updated_at: _builtins.str,
        binding_parameters: Optional[Mapping[str, _builtins.str]] = ...,
        key: Optional[_builtins.str] = ...,
        resource_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="generatedProperties")
    def generated_properties(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bindingParameters")
    def binding_parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BuildPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        triggered_build_result: outputs.TriggeredBuildResultResponse,
        agent_pool: Optional[_builtins.str] = ...,
        apms: Optional[Sequence[outputs.ApmReferenceResponse]] = ...,
        builder: Optional[_builtins.str] = ...,
        certificates: Optional[Sequence[outputs.CertificateReferenceResponse]] = ...,
        env: Optional[Mapping[str, _builtins.str]] = ...,
        relative_path: Optional[_builtins.str] = ...,
        resource_requests: Optional[outputs.BuildResourceRequestsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="triggeredBuildResult")
    def triggered_build_result(self) -> outputs.TriggeredBuildResultResponse: ...
    @_builtins.property
    @pulumi.getter(name="agentPool")
    def agent_pool(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def apms(self) -> Optional[Sequence[outputs.ApmReferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def builder(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def certificates(
        self,
    ) -> Optional[Sequence[outputs.CertificateReferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def env(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceRequests")
    def resource_requests(self) -> Optional[outputs.BuildResourceRequestsResponse]: ...

@pulumi.output_type
class BuildResourceRequestsResponse(dict):
    def __init__(
        __self__,
        *,
        cpu: Optional[_builtins.str] = ...,
        memory: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BuildResultUserSourceInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        build_result_id: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="buildResultId")
    def build_result_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BuildServiceAgentPoolPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        pool_size: Optional[outputs.BuildServiceAgentPoolSizePropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="poolSize")
    def pool_size(
        self,
    ) -> Optional[outputs.BuildServiceAgentPoolSizePropertiesResponse]: ...

@pulumi.output_type
class BuildServiceAgentPoolSizePropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        cpu: _builtins.str,
        memory: _builtins.str,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BuilderPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        buildpack_groups: Optional[
            Sequence[outputs.BuildpacksGroupPropertiesResponse]
        ] = ...,
        stack: Optional[outputs.StackPropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="buildpackGroups")
    def buildpack_groups(
        self,
    ) -> Optional[Sequence[outputs.BuildpacksGroupPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def stack(self) -> Optional[outputs.StackPropertiesResponse]: ...

@pulumi.output_type
class BuildpackBindingLaunchPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        properties: Optional[Mapping[str, _builtins.str]] = ...,
        secrets: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class BuildpackBindingPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        binding_type: Optional[_builtins.str] = ...,
        launch_properties: Optional[
            outputs.BuildpackBindingLaunchPropertiesResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bindingType")
    def binding_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="launchProperties")
    def launch_properties(
        self,
    ) -> Optional[outputs.BuildpackBindingLaunchPropertiesResponse]: ...

@pulumi.output_type
class BuildpackPropertiesResponse(dict):
    def __init__(
        __self__, *, version: _builtins.str, id: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BuildpacksGroupPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        buildpacks: Optional[Sequence[outputs.BuildpackPropertiesResponse]] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def buildpacks(self) -> Optional[Sequence[outputs.BuildpackPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterResourcePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fqdn: _builtins.str,
        power_state: _builtins.str,
        provisioning_state: _builtins.str,
        service_id: _builtins.str,
        version: _builtins.int,
        infra_resource_group: Optional[_builtins.str] = ...,
        maintenance_schedule_configuration: Optional[
            outputs.WeeklyMaintenanceScheduleConfigurationResponse
        ] = ...,
        managed_environment_id: Optional[_builtins.str] = ...,
        marketplace_resource: Optional[outputs.MarketplaceResourceResponse] = ...,
        network_profile: Optional[outputs.NetworkProfileResponse] = ...,
        vnet_addons: Optional[outputs.ServiceVNetAddonsResponse] = ...,
        zone_redundant: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="powerState")
    def power_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="infraResourceGroup")
    def infra_resource_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceScheduleConfiguration")
    def maintenance_schedule_configuration(
        self,
    ) -> Optional[outputs.WeeklyMaintenanceScheduleConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="managedEnvironmentId")
    def managed_environment_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="marketplaceResource")
    def marketplace_resource(self) -> Optional[outputs.MarketplaceResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[outputs.NetworkProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="vnetAddons")
    def vnet_addons(self) -> Optional[outputs.ServiceVNetAddonsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConfigServerGitPropertyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        uri: _builtins.str,
        host_key: Optional[_builtins.str] = ...,
        host_key_algorithm: Optional[_builtins.str] = ...,
        label: Optional[_builtins.str] = ...,
        password: Optional[_builtins.str] = ...,
        private_key: Optional[_builtins.str] = ...,
        repositories: Optional[Sequence[outputs.GitPatternRepositoryResponse]] = ...,
        search_paths: Optional[Sequence[_builtins.str]] = ...,
        strict_host_key_checking: Optional[_builtins.bool] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostKey")
    def host_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostKeyAlgorithm")
    def host_key_algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def repositories(
        self,
    ) -> Optional[Sequence[outputs.GitPatternRepositoryResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="searchPaths")
    def search_paths(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="strictHostKeyChecking")
    def strict_host_key_checking(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConfigServerPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        config_server: Optional[outputs.ConfigServerSettingsResponse] = ...,
        enabled_state: Optional[_builtins.str] = ...,
        error: Optional[outputs.ErrorResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="configServer")
    def config_server(self) -> Optional[outputs.ConfigServerSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ErrorResponse]: ...

@pulumi.output_type
class ConfigServerSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        git_property: Optional[outputs.ConfigServerGitPropertyResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gitProperty")
    def git_property(self) -> Optional[outputs.ConfigServerGitPropertyResponse]: ...

@pulumi.output_type
class ConfigurationServiceGitPropertyResponse(dict):
    def __init__(
        __self__,
        *,
        repositories: Optional[
            Sequence[outputs.ConfigurationServiceGitRepositoryResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def repositories(
        self,
    ) -> Optional[Sequence[outputs.ConfigurationServiceGitRepositoryResponse]]: ...

@pulumi.output_type
class ConfigurationServiceGitRepositoryResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        label: _builtins.str,
        name: _builtins.str,
        patterns: Sequence[_builtins.str],
        uri: _builtins.str,
        ca_cert_resource_id: Optional[_builtins.str] = ...,
        git_implementation: Optional[_builtins.str] = ...,
        host_key: Optional[_builtins.str] = ...,
        host_key_algorithm: Optional[_builtins.str] = ...,
        password: Optional[_builtins.str] = ...,
        private_key: Optional[_builtins.str] = ...,
        search_paths: Optional[Sequence[_builtins.str]] = ...,
        strict_host_key_checking: Optional[_builtins.bool] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def patterns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="caCertResourceId")
    def ca_cert_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gitImplementation")
    def git_implementation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostKey")
    def host_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostKeyAlgorithm")
    def host_key_algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="searchPaths")
    def search_paths(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="strictHostKeyChecking")
    def strict_host_key_checking(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConfigurationServiceInstanceResponse(dict):
    def __init__(__self__, *, name: _builtins.str, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class ConfigurationServicePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instances: Sequence[outputs.ConfigurationServiceInstanceResponse],
        provisioning_state: _builtins.str,
        resource_requests: outputs.ConfigurationServiceResourceRequestsResponse,
        generation: Optional[_builtins.str] = ...,
        settings: Optional[outputs.ConfigurationServiceSettingsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[outputs.ConfigurationServiceInstanceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceRequests")
    def resource_requests(
        self,
    ) -> outputs.ConfigurationServiceResourceRequestsResponse: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[outputs.ConfigurationServiceSettingsResponse]: ...

@pulumi.output_type
class ConfigurationServiceResourceRequestsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cpu: _builtins.str,
        instance_count: _builtins.int,
        memory: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> _builtins.str: ...

@pulumi.output_type
class ConfigurationServiceSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        git_property: Optional[outputs.ConfigurationServiceGitPropertyResponse] = ...,
        refresh_interval_in_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gitProperty")
    def git_property(
        self,
    ) -> Optional[outputs.ConfigurationServiceGitPropertyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="refreshIntervalInSeconds")
    def refresh_interval_in_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ContainerProbeSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, disable_probe: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableProbe")
    def disable_probe(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ContainerRegistryBasicCredentialsResponse(dict):
    def __init__(
        __self__, *, server: _builtins.str, type: _builtins.str, username: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class ContainerRegistryPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        credentials: outputs.ContainerRegistryBasicCredentialsResponse,
        provisioning_state: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> outputs.ContainerRegistryBasicCredentialsResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...

@pulumi.output_type
class ContentCertificatePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        activate_date: _builtins.str,
        dns_names: Sequence[_builtins.str],
        expiration_date: _builtins.str,
        issued_date: _builtins.str,
        issuer: _builtins.str,
        provisioning_state: _builtins.str,
        subject_name: _builtins.str,
        thumbprint: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activateDate")
    def activate_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsNames")
    def dns_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="issuedDate")
    def issued_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subjectName")
    def subject_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class CustomContainerResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        args: Optional[Sequence[_builtins.str]] = ...,
        command: Optional[Sequence[_builtins.str]] = ...,
        container_image: Optional[_builtins.str] = ...,
        image_registry_credential: Optional[
            outputs.ImageRegistryCredentialResponse
        ] = ...,
        language_framework: Optional[_builtins.str] = ...,
        server: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def command(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageRegistryCredential")
    def image_registry_credential(
        self,
    ) -> Optional[outputs.ImageRegistryCredentialResponse]: ...
    @_builtins.property
    @pulumi.getter(name="languageFramework")
    def language_framework(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomContainerUserSourceInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        custom_container: Optional[outputs.CustomContainerResponse] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customContainer")
    def custom_container(self) -> Optional[outputs.CustomContainerResponse]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomDomainPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_name: _builtins.str,
        provisioning_state: _builtins.str,
        cert_name: Optional[_builtins.str] = ...,
        thumbprint: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appName")
    def app_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certName")
    def cert_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomPersistentDiskResourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        storage_id: _builtins.str,
        custom_persistent_disk_properties: Optional[
            outputs.AzureFileVolumeResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageId")
    def storage_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customPersistentDiskProperties")
    def custom_persistent_disk_properties(
        self,
    ) -> Optional[outputs.AzureFileVolumeResponse]: ...

@pulumi.output_type
class CustomScaleRuleResponse(dict):
    def __init__(
        __self__,
        *,
        auth: Optional[Sequence[outputs.ScaleRuleAuthResponse]] = ...,
        metadata: Optional[Mapping[str, _builtins.str]] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[Sequence[outputs.ScaleRuleAuthResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomizedAcceleratorPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        git_repository: outputs.AcceleratorGitRepositoryResponse,
        imports: Sequence[_builtins.str],
        provisioning_state: _builtins.str,
        accelerator_tags: Optional[Sequence[_builtins.str]] = ...,
        accelerator_type: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        icon_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gitRepository")
    def git_repository(self) -> outputs.AcceleratorGitRepositoryResponse: ...
    @_builtins.property
    @pulumi.getter
    def imports(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorTags")
    def accelerator_tags(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iconUrl")
    def icon_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeploymentInstanceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        discovery_status: _builtins.str,
        name: _builtins.str,
        reason: _builtins.str,
        start_time: _builtins.str,
        status: _builtins.str,
        zone: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="discoveryStatus")
    def discovery_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...

@pulumi.output_type
class DeploymentResourcePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instances: Sequence[outputs.DeploymentInstanceResponse],
        provisioning_state: _builtins.str,
        status: _builtins.str,
        active: Optional[_builtins.bool] = ...,
        deployment_settings: Optional[outputs.DeploymentSettingsResponse] = ...,
        source: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[outputs.DeploymentInstanceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def active(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentSettings")
    def deployment_settings(self) -> Optional[outputs.DeploymentSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[Any]: ...

@pulumi.output_type
class DeploymentSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        addon_configs: Optional[Mapping[str, Any]] = ...,
        apms: Optional[Sequence[outputs.ApmReferenceResponse]] = ...,
        container_probe_settings: Optional[
            outputs.ContainerProbeSettingsResponse
        ] = ...,
        environment_variables: Optional[Mapping[str, _builtins.str]] = ...,
        liveness_probe: Optional[outputs.ProbeResponse] = ...,
        readiness_probe: Optional[outputs.ProbeResponse] = ...,
        resource_requests: Optional[outputs.ResourceRequestsResponse] = ...,
        scale: Optional[outputs.ScaleResponse] = ...,
        startup_probe: Optional[outputs.ProbeResponse] = ...,
        termination_grace_period_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addonConfigs")
    def addon_configs(self) -> Optional[Mapping[str, Any]]: ...
    @_builtins.property
    @pulumi.getter
    def apms(self) -> Optional[Sequence[outputs.ApmReferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="containerProbeSettings")
    def container_probe_settings(
        self,
    ) -> Optional[outputs.ContainerProbeSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="livenessProbe")
    def liveness_probe(self) -> Optional[outputs.ProbeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="readinessProbe")
    def readiness_probe(self) -> Optional[outputs.ProbeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceRequests")
    def resource_requests(self) -> Optional[outputs.ResourceRequestsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[outputs.ScaleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="startupProbe")
    def startup_probe(self) -> Optional[outputs.ProbeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="terminationGracePeriodSeconds")
    def termination_grace_period_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DevToolPortalComponentResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instances: Sequence[outputs.DevToolPortalInstanceResponse],
        name: _builtins.str,
        resource_requests: outputs.DevToolPortalResourceRequestsResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[outputs.DevToolPortalInstanceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceRequests")
    def resource_requests(self) -> outputs.DevToolPortalResourceRequestsResponse: ...

@pulumi.output_type
class DevToolPortalFeatureDetailResponse(dict):
    def __init__(
        __self__, *, route: _builtins.str, state: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def route(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DevToolPortalFeatureSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        application_accelerator: Optional[
            outputs.DevToolPortalFeatureDetailResponse
        ] = ...,
        application_live_view: Optional[
            outputs.DevToolPortalFeatureDetailResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationAccelerator")
    def application_accelerator(
        self,
    ) -> Optional[outputs.DevToolPortalFeatureDetailResponse]: ...
    @_builtins.property
    @pulumi.getter(name="applicationLiveView")
    def application_live_view(
        self,
    ) -> Optional[outputs.DevToolPortalFeatureDetailResponse]: ...

@pulumi.output_type
class DevToolPortalInstanceResponse(dict):
    def __init__(__self__, *, name: _builtins.str, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class DevToolPortalPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        components: Sequence[outputs.DevToolPortalComponentResponse],
        provisioning_state: _builtins.str,
        url: _builtins.str,
        features: Optional[outputs.DevToolPortalFeatureSettingsResponse] = ...,
        public: Optional[_builtins.bool] = ...,
        sso_properties: Optional[outputs.DevToolPortalSsoPropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> Sequence[outputs.DevToolPortalComponentResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def features(self) -> Optional[outputs.DevToolPortalFeatureSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def public(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ssoProperties")
    def sso_properties(
        self,
    ) -> Optional[outputs.DevToolPortalSsoPropertiesResponse]: ...

@pulumi.output_type
class DevToolPortalResourceRequestsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cpu: _builtins.str,
        instance_count: _builtins.int,
        memory: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> _builtins.str: ...

@pulumi.output_type
class DevToolPortalSsoPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: Optional[_builtins.str] = ...,
        client_secret: Optional[_builtins.str] = ...,
        metadata_url: Optional[_builtins.str] = ...,
        scopes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metadataUrl")
    def metadata_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class EnvVarResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        secret_value: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretValue")
    def secret_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ErrorResponse(dict):
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
class ExecActionResponse(dict):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        command: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def command(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GatewayApiMetadataPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        documentation: Optional[_builtins.str] = ...,
        server_url: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def documentation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serverUrl")
    def server_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayApiRouteResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        filters: Optional[Sequence[_builtins.str]] = ...,
        order: Optional[_builtins.int] = ...,
        predicates: Optional[Sequence[_builtins.str]] = ...,
        sso_enabled: Optional[_builtins.bool] = ...,
        tags: Optional[Sequence[_builtins.str]] = ...,
        title: Optional[_builtins.str] = ...,
        token_relay: Optional[_builtins.bool] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def predicates(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ssoEnabled")
    def sso_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenRelay")
    def token_relay(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayCorsPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_credentials: Optional[_builtins.bool] = ...,
        allowed_headers: Optional[Sequence[_builtins.str]] = ...,
        allowed_methods: Optional[Sequence[_builtins.str]] = ...,
        allowed_origin_patterns: Optional[Sequence[_builtins.str]] = ...,
        allowed_origins: Optional[Sequence[_builtins.str]] = ...,
        exposed_headers: Optional[Sequence[_builtins.str]] = ...,
        max_age: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedOriginPatterns")
    def allowed_origin_patterns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exposedHeaders")
    def exposed_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GatewayCustomDomainPropertiesResponse(dict):
    def __init__(__self__, *, thumbprint: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayInstanceResponse(dict):
    def __init__(__self__, *, name: _builtins.str, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GatewayLocalResponseCachePerInstancePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        response_cache_type: _builtins.str,
        size: Optional[_builtins.str] = ...,
        time_to_live: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="responseCacheType")
    def response_cache_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeToLive")
    def time_to_live(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayLocalResponseCachePerRoutePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        response_cache_type: _builtins.str,
        size: Optional[_builtins.str] = ...,
        time_to_live: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="responseCacheType")
    def response_cache_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeToLive")
    def time_to_live(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayOperatorPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instances: Sequence[outputs.GatewayInstanceResponse],
        resource_requests: outputs.GatewayOperatorResourceRequestsResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[outputs.GatewayInstanceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceRequests")
    def resource_requests(self) -> outputs.GatewayOperatorResourceRequestsResponse: ...

@pulumi.output_type
class GatewayOperatorResourceRequestsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cpu: _builtins.str,
        instance_count: _builtins.int,
        memory: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> _builtins.str: ...

@pulumi.output_type
class GatewayPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instances: Sequence[outputs.GatewayInstanceResponse],
        operator_properties: outputs.GatewayOperatorPropertiesResponse,
        provisioning_state: _builtins.str,
        url: _builtins.str,
        addon_configs: Optional[Mapping[str, Any]] = ...,
        api_metadata_properties: Optional[
            outputs.GatewayApiMetadataPropertiesResponse
        ] = ...,
        apm_types: Optional[Sequence[_builtins.str]] = ...,
        apms: Optional[Sequence[outputs.ApmReferenceResponse]] = ...,
        client_auth: Optional[outputs.GatewayPropertiesResponseClientAuth] = ...,
        cors_properties: Optional[outputs.GatewayCorsPropertiesResponse] = ...,
        environment_variables: Optional[
            outputs.GatewayPropertiesResponseEnvironmentVariables
        ] = ...,
        https_only: Optional[_builtins.bool] = ...,
        public: Optional[_builtins.bool] = ...,
        resource_requests: Optional[outputs.GatewayResourceRequestsResponse] = ...,
        response_cache_properties: Optional[Any] = ...,
        sso_properties: Optional[outputs.SsoPropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[outputs.GatewayInstanceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="operatorProperties")
    def operator_properties(self) -> outputs.GatewayOperatorPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addonConfigs")
    def addon_configs(self) -> Optional[Mapping[str, Any]]: ...
    @_builtins.property
    @pulumi.getter(name="apiMetadataProperties")
    def api_metadata_properties(
        self,
    ) -> Optional[outputs.GatewayApiMetadataPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="apmTypes")
    def apm_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def apms(self) -> Optional[Sequence[outputs.ApmReferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="clientAuth")
    def client_auth(self) -> Optional[outputs.GatewayPropertiesResponseClientAuth]: ...
    @_builtins.property
    @pulumi.getter(name="corsProperties")
    def cors_properties(self) -> Optional[outputs.GatewayCorsPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[outputs.GatewayPropertiesResponseEnvironmentVariables]: ...
    @_builtins.property
    @pulumi.getter(name="httpsOnly")
    def https_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def public(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="resourceRequests")
    def resource_requests(
        self,
    ) -> Optional[outputs.GatewayResourceRequestsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="responseCacheProperties")
    def response_cache_properties(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="ssoProperties")
    def sso_properties(self) -> Optional[outputs.SsoPropertiesResponse]: ...

@pulumi.output_type
class GatewayPropertiesResponseClientAuth(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_verification: Optional[_builtins.str] = ...,
        certificates: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateVerification")
    def certificate_verification(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GatewayPropertiesResponseEnvironmentVariables(dict):
    def __init__(
        __self__,
        *,
        properties: Optional[Mapping[str, _builtins.str]] = ...,
        secrets: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class GatewayResourceRequestsResponse(dict):
    def __init__(
        __self__,
        *,
        cpu: Optional[_builtins.str] = ...,
        memory: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayRouteConfigOpenApiPropertiesResponse(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayRouteConfigPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        app_resource_id: Optional[_builtins.str] = ...,
        filters: Optional[Sequence[_builtins.str]] = ...,
        open_api: Optional[outputs.GatewayRouteConfigOpenApiPropertiesResponse] = ...,
        predicates: Optional[Sequence[_builtins.str]] = ...,
        protocol: Optional[_builtins.str] = ...,
        routes: Optional[Sequence[outputs.GatewayApiRouteResponse]] = ...,
        sso_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="appResourceId")
    def app_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="openApi")
    def open_api(
        self,
    ) -> Optional[outputs.GatewayRouteConfigOpenApiPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def predicates(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Optional[Sequence[outputs.GatewayApiRouteResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="ssoEnabled")
    def sso_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class GitPatternRepositoryResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        uri: _builtins.str,
        host_key: Optional[_builtins.str] = ...,
        host_key_algorithm: Optional[_builtins.str] = ...,
        label: Optional[_builtins.str] = ...,
        password: Optional[_builtins.str] = ...,
        pattern: Optional[Sequence[_builtins.str]] = ...,
        private_key: Optional[_builtins.str] = ...,
        search_paths: Optional[Sequence[_builtins.str]] = ...,
        strict_host_key_checking: Optional[_builtins.bool] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostKey")
    def host_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostKeyAlgorithm")
    def host_key_algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="searchPaths")
    def search_paths(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="strictHostKeyChecking")
    def strict_host_key_checking(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HTTPGetActionResponse(dict):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        path: Optional[_builtins.str] = ...,
        scheme: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HttpScaleRuleResponse(dict):
    def __init__(
        __self__,
        *,
        auth: Optional[Sequence[outputs.ScaleRuleAuthResponse]] = ...,
        metadata: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[Sequence[outputs.ScaleRuleAuthResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ImageRegistryCredentialResponse(dict):
    def __init__(
        __self__,
        *,
        password: Optional[_builtins.str] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IngressConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, read_timeout_in_seconds: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="readTimeoutInSeconds")
    def read_timeout_in_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class IngressSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backend_protocol: Optional[_builtins.str] = ...,
        client_auth: Optional[outputs.IngressSettingsResponseClientAuth] = ...,
        read_timeout_in_seconds: Optional[_builtins.int] = ...,
        send_timeout_in_seconds: Optional[_builtins.int] = ...,
        session_affinity: Optional[_builtins.str] = ...,
        session_cookie_max_age: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendProtocol")
    def backend_protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientAuth")
    def client_auth(self) -> Optional[outputs.IngressSettingsResponseClientAuth]: ...
    @_builtins.property
    @pulumi.getter(name="readTimeoutInSeconds")
    def read_timeout_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sendTimeoutInSeconds")
    def send_timeout_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionCookieMaxAge")
    def session_cookie_max_age(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class IngressSettingsResponseClientAuth(dict):
    def __init__(
        __self__, *, certificates: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class JarUploadedUserSourceInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        jvm_options: Optional[_builtins.str] = ...,
        relative_path: Optional[_builtins.str] = ...,
        runtime_version: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jvmOptions")
    def jvm_options(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobExecutionTemplateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        args: Optional[Sequence[_builtins.str]] = ...,
        environment_variables: Optional[Sequence[outputs.EnvVarResponse]] = ...,
        resource_requests: Optional[outputs.JobResourceRequestsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Sequence[outputs.EnvVarResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceRequests")
    def resource_requests(self) -> Optional[outputs.JobResourceRequestsResponse]: ...

@pulumi.output_type
class JobResourcePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        managed_component_references: Optional[
            Sequence[outputs.ManagedComponentReferenceResponse]
        ] = ...,
        source: Optional[Any] = ...,
        template: Optional[outputs.JobExecutionTemplateResponse] = ...,
        trigger_config: Optional[outputs.ManualJobTriggerConfigResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedComponentReferences")
    def managed_component_references(
        self,
    ) -> Optional[Sequence[outputs.ManagedComponentReferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> Optional[outputs.JobExecutionTemplateResponse]: ...
    @_builtins.property
    @pulumi.getter(name="triggerConfig")
    def trigger_config(self) -> Optional[outputs.ManualJobTriggerConfigResponse]: ...

@pulumi.output_type
class JobResourceRequestsResponse(dict):
    def __init__(
        __self__,
        *,
        cpu: Optional[_builtins.str] = ...,
        memory: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KeyVaultCertificatePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        activate_date: _builtins.str,
        dns_names: Sequence[_builtins.str],
        expiration_date: _builtins.str,
        issued_date: _builtins.str,
        issuer: _builtins.str,
        key_vault_cert_name: _builtins.str,
        provisioning_state: _builtins.str,
        subject_name: _builtins.str,
        thumbprint: _builtins.str,
        type: _builtins.str,
        vault_uri: _builtins.str,
        auto_sync: Optional[_builtins.str] = ...,
        cert_version: Optional[_builtins.str] = ...,
        exclude_private_key: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activateDate")
    def activate_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsNames")
    def dns_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="issuedDate")
    def issued_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultCertName")
    def key_vault_cert_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subjectName")
    def subject_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vaultUri")
    def vault_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoSync")
    def auto_sync(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certVersion")
    def cert_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="excludePrivateKey")
    def exclude_private_key(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class LoadedCertificateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_id: _builtins.str,
        load_trust_store: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="loadTrustStore")
    def load_trust_store(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ManagedComponentReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str: ...

@pulumi.output_type
class ManagedIdentityPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: Optional[_builtins.str] = ...,
        tenant_id: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedManagedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedManagedIdentityResponse]]: ...

@pulumi.output_type
class ManualJobTriggerConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        trigger_type: Optional[_builtins.str] = ...,
        parallelism: Optional[_builtins.int] = ...,
        retry_limit: Optional[_builtins.int] = ...,
        timeout_in_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="triggerType")
    def trigger_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parallelism(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="retryLimit")
    def retry_limit(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class MarketplaceResourceResponse(dict):
    def __init__(
        __self__,
        *,
        plan: Optional[_builtins.str] = ...,
        product: Optional[_builtins.str] = ...,
        publisher: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def product(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MonitoringSettingPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        app_insights_agent_versions: Optional[
            outputs.ApplicationInsightsAgentVersionsResponse
        ] = ...,
        app_insights_instrumentation_key: Optional[_builtins.str] = ...,
        app_insights_sampling_rate: Optional[_builtins.float] = ...,
        error: Optional[outputs.ErrorResponse] = ...,
        trace_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="appInsightsAgentVersions")
    def app_insights_agent_versions(
        self,
    ) -> Optional[outputs.ApplicationInsightsAgentVersionsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="appInsightsInstrumentationKey")
    def app_insights_instrumentation_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="appInsightsSamplingRate")
    def app_insights_sampling_rate(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ErrorResponse]: ...
    @_builtins.property
    @pulumi.getter(name="traceEnabled")
    def trace_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class NetCoreZipUploadedUserSourceInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        net_core_main_entry_path: Optional[_builtins.str] = ...,
        relative_path: Optional[_builtins.str] = ...,
        runtime_version: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="netCoreMainEntryPath")
    def net_core_main_entry_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NetworkProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        outbound_ips: outputs.NetworkProfileResponseOutboundIPs,
        required_traffics: Sequence[outputs.RequiredTrafficResponse],
        app_network_resource_group: Optional[_builtins.str] = ...,
        app_subnet_id: Optional[_builtins.str] = ...,
        ingress_config: Optional[outputs.IngressConfigResponse] = ...,
        outbound_type: Optional[_builtins.str] = ...,
        service_cidr: Optional[_builtins.str] = ...,
        service_runtime_network_resource_group: Optional[_builtins.str] = ...,
        service_runtime_subnet_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outboundIPs")
    def outbound_ips(self) -> outputs.NetworkProfileResponseOutboundIPs: ...
    @_builtins.property
    @pulumi.getter(name="requiredTraffics")
    def required_traffics(self) -> Sequence[outputs.RequiredTrafficResponse]: ...
    @_builtins.property
    @pulumi.getter(name="appNetworkResourceGroup")
    def app_network_resource_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="appSubnetId")
    def app_subnet_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ingressConfig")
    def ingress_config(self) -> Optional[outputs.IngressConfigResponse]: ...
    @_builtins.property
    @pulumi.getter(name="outboundType")
    def outbound_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceCidr")
    def service_cidr(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceRuntimeNetworkResourceGroup")
    def service_runtime_network_resource_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceRuntimeSubnetId")
    def service_runtime_subnet_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NetworkProfileResponseOutboundIPs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, public_ips: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicIPs")
    def public_ips(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class PersistentDiskResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        used_in_gb: _builtins.int,
        mount_path: Optional[_builtins.str] = ...,
        size_in_gb: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="usedInGB")
    def used_in_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sizeInGB")
    def size_in_gb(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ProbeResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_probe: Optional[_builtins.bool] = ...,
        failure_threshold: Optional[_builtins.int] = ...,
        initial_delay_seconds: Optional[_builtins.int] = ...,
        period_seconds: Optional[_builtins.int] = ...,
        probe_action: Optional[Any] = ...,
        success_threshold: Optional[_builtins.int] = ...,
        timeout_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableProbe")
    def disable_probe(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="probeAction")
    def probe_action(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class QueueScaleRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth: Optional[Sequence[outputs.ScaleRuleAuthResponse]] = ...,
        queue_length: Optional[_builtins.int] = ...,
        queue_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[Sequence[outputs.ScaleRuleAuthResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="queueLength")
    def queue_length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RequiredTrafficResponse(dict):
    def __init__(
        __self__,
        *,
        direction: _builtins.str,
        fqdns: Sequence[_builtins.str],
        ips: Sequence[_builtins.str],
        port: _builtins.int,
        protocol: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def fqdns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ips(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...

@pulumi.output_type
class ResourceRequestsResponse(dict):
    def __init__(
        __self__,
        *,
        cpu: Optional[_builtins.str] = ...,
        memory: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScaleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_replicas: Optional[_builtins.int] = ...,
        min_replicas: Optional[_builtins.int] = ...,
        rules: Optional[Sequence[outputs.ScaleRuleResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxReplicas")
    def max_replicas(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minReplicas")
    def min_replicas(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.ScaleRuleResponse]]: ...

@pulumi.output_type
class ScaleRuleAuthResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        secret_ref: Optional[_builtins.str] = ...,
        trigger_parameter: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretRef")
    def secret_ref(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="triggerParameter")
    def trigger_parameter(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScaleRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        azure_queue: Optional[outputs.QueueScaleRuleResponse] = ...,
        custom: Optional[outputs.CustomScaleRuleResponse] = ...,
        http: Optional[outputs.HttpScaleRuleResponse] = ...,
        name: Optional[_builtins.str] = ...,
        tcp: Optional[outputs.TcpScaleRuleResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureQueue")
    def azure_queue(self) -> Optional[outputs.QueueScaleRuleResponse]: ...
    @_builtins.property
    @pulumi.getter
    def custom(self) -> Optional[outputs.CustomScaleRuleResponse]: ...
    @_builtins.property
    @pulumi.getter
    def http(self) -> Optional[outputs.HttpScaleRuleResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tcp(self) -> Optional[outputs.TcpScaleRuleResponse]: ...

@pulumi.output_type
class SecretResponse(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceRegistryInstanceResponse(dict):
    def __init__(__self__, *, name: _builtins.str, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class ServiceRegistryPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instances: Sequence[outputs.ServiceRegistryInstanceResponse],
        provisioning_state: _builtins.str,
        resource_requests: outputs.ServiceRegistryResourceRequestsResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[outputs.ServiceRegistryInstanceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceRequests")
    def resource_requests(self) -> outputs.ServiceRegistryResourceRequestsResponse: ...

@pulumi.output_type
class ServiceRegistryResourceRequestsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cpu: _builtins.str,
        instance_count: _builtins.int,
        memory: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> _builtins.str: ...

@pulumi.output_type
class ServiceVNetAddonsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_plane_public_endpoint: Optional[_builtins.bool] = ...,
        log_stream_public_endpoint: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataPlanePublicEndpoint")
    def data_plane_public_endpoint(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamPublicEndpoint")
    def log_stream_public_endpoint(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class SkuResponse(dict):
    def __init__(
        __self__,
        *,
        capacity: Optional[_builtins.int] = ...,
        name: Optional[_builtins.str] = ...,
        tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SourceUploadedUserSourceInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        artifact_selector: Optional[_builtins.str] = ...,
        relative_path: Optional[_builtins.str] = ...,
        runtime_version: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="artifactSelector")
    def artifact_selector(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SsoPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: Optional[_builtins.str] = ...,
        client_secret: Optional[_builtins.str] = ...,
        issuer_uri: Optional[_builtins.str] = ...,
        scope: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class StackPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageAccountResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, account_name: _builtins.str, storage_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> _builtins.str: ...

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
class TCPSocketActionResponse(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class TcpScaleRuleResponse(dict):
    def __init__(
        __self__,
        *,
        auth: Optional[Sequence[outputs.ScaleRuleAuthResponse]] = ...,
        metadata: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[Sequence[outputs.ScaleRuleAuthResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class TemporaryDiskResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mount_path: Optional[_builtins.str] = ...,
        size_in_gb: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sizeInGB")
    def size_in_gb(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TriggeredBuildResultResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        id: Optional[_builtins.str] = ...,
        image: Optional[_builtins.str] = ...,
        last_transition_reason: Optional[_builtins.str] = ...,
        last_transition_status: Optional[_builtins.str] = ...,
        last_transition_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionReason")
    def last_transition_reason(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionStatus")
    def last_transition_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UploadedUserSourceInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        relative_path: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserAssignedManagedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, principal_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...

@pulumi.output_type
class WarUploadedUserSourceInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        jvm_options: Optional[_builtins.str] = ...,
        relative_path: Optional[_builtins.str] = ...,
        runtime_version: Optional[_builtins.str] = ...,
        server_version: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jvmOptions")
    def jvm_options(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WeeklyMaintenanceScheduleConfigurationResponse(dict):
    def __init__(
        __self__,
        *,
        day: _builtins.str,
        duration: _builtins.str,
        frequency: _builtins.str,
        hour: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hour(self) -> _builtins.int: ...
