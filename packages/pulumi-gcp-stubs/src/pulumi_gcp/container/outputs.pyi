import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AttachedClusterAuthorization",
    "AttachedClusterBinaryAuthorization",
    "AttachedClusterError",
    "AttachedClusterFleet",
    "AttachedClusterLoggingConfig",
    "AttachedClusterLoggingConfigComponentConfig",
    "AttachedClusterMonitoringConfig",
    ...,
    "AttachedClusterOidcConfig",
    "AttachedClusterProxyConfig",
    "AttachedClusterProxyConfigKubernetesSecret",
    "AttachedClusterSecurityPostureConfig",
    "AttachedClusterWorkloadIdentityConfig",
    "AwsClusterAuthorization",
    "AwsClusterAuthorizationAdminGroup",
    "AwsClusterAuthorizationAdminUser",
    "AwsClusterBinaryAuthorization",
    "AwsClusterControlPlane",
    "AwsClusterControlPlaneAwsServicesAuthentication",
    "AwsClusterControlPlaneConfigEncryption",
    "AwsClusterControlPlaneDatabaseEncryption",
    "AwsClusterControlPlaneInstancePlacement",
    "AwsClusterControlPlaneMainVolume",
    "AwsClusterControlPlaneProxyConfig",
    "AwsClusterControlPlaneRootVolume",
    "AwsClusterControlPlaneSshConfig",
    "AwsClusterFleet",
    "AwsClusterLoggingConfig",
    "AwsClusterLoggingConfigComponentConfig",
    "AwsClusterNetworking",
    "AwsClusterWorkloadIdentityConfig",
    "AwsNodePoolAutoscaling",
    "AwsNodePoolConfig",
    "AwsNodePoolConfigAutoscalingMetricsCollection",
    "AwsNodePoolConfigConfigEncryption",
    "AwsNodePoolConfigInstancePlacement",
    "AwsNodePoolConfigProxyConfig",
    "AwsNodePoolConfigRootVolume",
    "AwsNodePoolConfigSpotConfig",
    "AwsNodePoolConfigSshConfig",
    "AwsNodePoolConfigTaint",
    "AwsNodePoolKubeletConfig",
    "AwsNodePoolManagement",
    "AwsNodePoolMaxPodsConstraint",
    "AwsNodePoolUpdateSettings",
    "AwsNodePoolUpdateSettingsSurgeSettings",
    "AzureClusterAuthorization",
    "AzureClusterAuthorizationAdminGroup",
    "AzureClusterAuthorizationAdminUser",
    "AzureClusterAzureServicesAuthentication",
    "AzureClusterControlPlane",
    "AzureClusterControlPlaneDatabaseEncryption",
    "AzureClusterControlPlaneMainVolume",
    "AzureClusterControlPlaneProxyConfig",
    "AzureClusterControlPlaneReplicaPlacement",
    "AzureClusterControlPlaneRootVolume",
    "AzureClusterControlPlaneSshConfig",
    "AzureClusterFleet",
    "AzureClusterLoggingConfig",
    "AzureClusterLoggingConfigComponentConfig",
    "AzureClusterNetworking",
    "AzureClusterWorkloadIdentityConfig",
    "AzureNodePoolAutoscaling",
    "AzureNodePoolConfig",
    "AzureNodePoolConfigProxyConfig",
    "AzureNodePoolConfigRootVolume",
    "AzureNodePoolConfigSshConfig",
    "AzureNodePoolManagement",
    "AzureNodePoolMaxPodsConstraint",
    "ClusterAddonsConfig",
    "ClusterAddonsConfigCloudrunConfig",
    "ClusterAddonsConfigConfigConnectorConfig",
    "ClusterAddonsConfigDnsCacheConfig",
    ...,
    "ClusterAddonsConfigGcpFilestoreCsiDriverConfig",
    "ClusterAddonsConfigGcsFuseCsiDriverConfig",
    "ClusterAddonsConfigGkeBackupAgentConfig",
    "ClusterAddonsConfigHorizontalPodAutoscaling",
    "ClusterAddonsConfigHttpLoadBalancing",
    "ClusterAddonsConfigIstioConfig",
    "ClusterAddonsConfigKalmConfig",
    "ClusterAddonsConfigLustreCsiDriverConfig",
    "ClusterAddonsConfigNetworkPolicyConfig",
    "ClusterAddonsConfigParallelstoreCsiDriverConfig",
    "ClusterAddonsConfigPodSnapshotConfig",
    "ClusterAddonsConfigRayOperatorConfig",
    ...,
    ...,
    "ClusterAddonsConfigSliceControllerConfig",
    "ClusterAddonsConfigStatefulHaConfig",
    "ClusterAnonymousAuthenticationConfig",
    "ClusterAuthenticatorGroupsConfig",
    "ClusterBinaryAuthorization",
    "ClusterClusterAutoscaling",
    "ClusterClusterAutoscalingAutoProvisioningDefaults",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterClusterAutoscalingResourceLimit",
    "ClusterClusterTelemetry",
    "ClusterConfidentialNodes",
    "ClusterControlPlaneEndpointsConfig",
    ...,
    ...,
    "ClusterCostManagementConfig",
    "ClusterDatabaseEncryption",
    "ClusterDefaultSnatStatus",
    "ClusterDnsConfig",
    "ClusterEnableK8sBetaApis",
    "ClusterEnterpriseConfig",
    "ClusterFleet",
    "ClusterGatewayApiConfig",
    "ClusterGkeAutoUpgradeConfig",
    "ClusterIdentityServiceConfig",
    "ClusterIpAllocationPolicy",
    "ClusterIpAllocationPolicyAdditionalIpRangesConfig",
    "ClusterIpAllocationPolicyAdditionalPodRangesConfig",
    "ClusterIpAllocationPolicyAutoIpamConfig",
    "ClusterIpAllocationPolicyNetworkTierConfig",
    ...,
    "ClusterLoggingConfig",
    "ClusterMaintenancePolicy",
    "ClusterMaintenancePolicyDailyMaintenanceWindow",
    "ClusterMaintenancePolicyDisruptionBudget",
    "ClusterMaintenancePolicyMaintenanceExclusion",
    ...,
    "ClusterMaintenancePolicyRecurringWindow",
    "ClusterManagedOpentelemetryConfig",
    "ClusterMasterAuth",
    "ClusterMasterAuthClientCertificateConfig",
    "ClusterMasterAuthorizedNetworksConfig",
    "ClusterMasterAuthorizedNetworksConfigCidrBlock",
    "ClusterMeshCertificates",
    "ClusterMonitoringConfig",
    ...,
    "ClusterMonitoringConfigManagedPrometheus",
    ...,
    "ClusterNetworkPerformanceConfig",
    "ClusterNetworkPolicy",
    "ClusterNodeConfig",
    "ClusterNodeConfigAdvancedMachineFeatures",
    "ClusterNodeConfigBootDisk",
    "ClusterNodeConfigConfidentialNodes",
    "ClusterNodeConfigContainerdConfig",
    ...,
    ...,
    ...,
    "ClusterNodeConfigContainerdConfigRegistryHost",
    "ClusterNodeConfigContainerdConfigRegistryHostHost",
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterNodeConfigContainerdConfigWritableCgroups",
    "ClusterNodeConfigEffectiveTaint",
    "ClusterNodeConfigEphemeralStorageConfig",
    "ClusterNodeConfigEphemeralStorageLocalSsdConfig",
    "ClusterNodeConfigFastSocket",
    "ClusterNodeConfigGcfsConfig",
    "ClusterNodeConfigGuestAccelerator",
    ...,
    "ClusterNodeConfigGuestAcceleratorGpuSharingConfig",
    "ClusterNodeConfigGvnic",
    "ClusterNodeConfigHostMaintenancePolicy",
    "ClusterNodeConfigKubeletConfig",
    ...,
    "ClusterNodeConfigKubeletConfigEvictionSoft",
    ...,
    "ClusterNodeConfigKubeletConfigMemoryManager",
    "ClusterNodeConfigKubeletConfigTopologyManager",
    "ClusterNodeConfigLinuxNodeConfig",
    "ClusterNodeConfigLinuxNodeConfigHugepagesConfig",
    ...,
    "ClusterNodeConfigLocalNvmeSsdBlockConfig",
    "ClusterNodeConfigReservationAffinity",
    "ClusterNodeConfigSandboxConfig",
    "ClusterNodeConfigSecondaryBootDisk",
    "ClusterNodeConfigShieldedInstanceConfig",
    "ClusterNodeConfigSoleTenantConfig",
    "ClusterNodeConfigSoleTenantConfigNodeAffinity",
    "ClusterNodeConfigTaint",
    "ClusterNodeConfigWindowsNodeConfig",
    "ClusterNodeConfigWorkloadMetadataConfig",
    "ClusterNodePool",
    "ClusterNodePoolAutoConfig",
    "ClusterNodePoolAutoConfigLinuxNodeConfig",
    ...,
    "ClusterNodePoolAutoConfigNetworkTags",
    "ClusterNodePoolAutoConfigNodeKubeletConfig",
    "ClusterNodePoolAutoscaling",
    "ClusterNodePoolDefaults",
    "ClusterNodePoolDefaultsNodeConfigDefaults",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterNodePoolManagement",
    "ClusterNodePoolNetworkConfig",
    ...,
    ...,
    ...,
    ...,
    "ClusterNodePoolNodeConfig",
    "ClusterNodePoolNodeConfigAdvancedMachineFeatures",
    "ClusterNodePoolNodeConfigBootDisk",
    "ClusterNodePoolNodeConfigConfidentialNodes",
    "ClusterNodePoolNodeConfigContainerdConfig",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterNodePoolNodeConfigEffectiveTaint",
    "ClusterNodePoolNodeConfigEphemeralStorageConfig",
    ...,
    "ClusterNodePoolNodeConfigFastSocket",
    "ClusterNodePoolNodeConfigGcfsConfig",
    "ClusterNodePoolNodeConfigGuestAccelerator",
    ...,
    ...,
    "ClusterNodePoolNodeConfigGvnic",
    "ClusterNodePoolNodeConfigHostMaintenancePolicy",
    "ClusterNodePoolNodeConfigKubeletConfig",
    ...,
    "ClusterNodePoolNodeConfigKubeletConfigEvictionSoft",
    ...,
    ...,
    ...,
    "ClusterNodePoolNodeConfigLinuxNodeConfig",
    ...,
    ...,
    "ClusterNodePoolNodeConfigLocalNvmeSsdBlockConfig",
    "ClusterNodePoolNodeConfigReservationAffinity",
    "ClusterNodePoolNodeConfigSandboxConfig",
    "ClusterNodePoolNodeConfigSecondaryBootDisk",
    "ClusterNodePoolNodeConfigShieldedInstanceConfig",
    "ClusterNodePoolNodeConfigSoleTenantConfig",
    ...,
    "ClusterNodePoolNodeConfigTaint",
    "ClusterNodePoolNodeConfigWindowsNodeConfig",
    "ClusterNodePoolNodeConfigWorkloadMetadataConfig",
    "ClusterNodePoolNodeDrainConfig",
    "ClusterNodePoolPlacementPolicy",
    "ClusterNodePoolQueuedProvisioning",
    "ClusterNodePoolUpgradeSettings",
    "ClusterNodePoolUpgradeSettingsBlueGreenSettings",
    ...,
    ...,
    "ClusterNotificationConfig",
    "ClusterNotificationConfigPubsub",
    "ClusterNotificationConfigPubsubFilter",
    "ClusterPodAutoscaling",
    "ClusterPodSecurityPolicyConfig",
    "ClusterPrivateClusterConfig",
    ...,
    "ClusterProtectConfig",
    "ClusterProtectConfigWorkloadConfig",
    "ClusterRbacBindingConfig",
    "ClusterReleaseChannel",
    "ClusterResourceUsageExportConfig",
    ...,
    "ClusterSecretManagerConfig",
    "ClusterSecretManagerConfigRotationConfig",
    "ClusterSecretSyncConfig",
    "ClusterSecretSyncConfigRotationConfig",
    "ClusterSecurityPostureConfig",
    "ClusterServiceExternalIpsConfig",
    "ClusterTpuConfig",
    "ClusterUserManagedKeysConfig",
    "ClusterVerticalPodAutoscaling",
    "ClusterWorkloadAltsConfig",
    "ClusterWorkloadIdentityConfig",
    "NodePoolAutoscaling",
    "NodePoolManagement",
    "NodePoolNetworkConfig",
    "NodePoolNetworkConfigAdditionalNodeNetworkConfig",
    "NodePoolNetworkConfigAdditionalPodNetworkConfig",
    "NodePoolNetworkConfigNetworkPerformanceConfig",
    "NodePoolNetworkConfigPodCidrOverprovisionConfig",
    "NodePoolNodeConfig",
    "NodePoolNodeConfigAdvancedMachineFeatures",
    "NodePoolNodeConfigBootDisk",
    "NodePoolNodeConfigConfidentialNodes",
    "NodePoolNodeConfigContainerdConfig",
    ...,
    ...,
    ...,
    "NodePoolNodeConfigContainerdConfigRegistryHost",
    "NodePoolNodeConfigContainerdConfigRegistryHostHost",
    ...,
    ...,
    ...,
    ...,
    ...,
    "NodePoolNodeConfigContainerdConfigWritableCgroups",
    "NodePoolNodeConfigEffectiveTaint",
    "NodePoolNodeConfigEphemeralStorageConfig",
    "NodePoolNodeConfigEphemeralStorageLocalSsdConfig",
    "NodePoolNodeConfigFastSocket",
    "NodePoolNodeConfigGcfsConfig",
    "NodePoolNodeConfigGuestAccelerator",
    ...,
    "NodePoolNodeConfigGuestAcceleratorGpuSharingConfig",
    "NodePoolNodeConfigGvnic",
    "NodePoolNodeConfigHostMaintenancePolicy",
    "NodePoolNodeConfigKubeletConfig",
    ...,
    "NodePoolNodeConfigKubeletConfigEvictionSoft",
    ...,
    "NodePoolNodeConfigKubeletConfigMemoryManager",
    "NodePoolNodeConfigKubeletConfigTopologyManager",
    "NodePoolNodeConfigLinuxNodeConfig",
    "NodePoolNodeConfigLinuxNodeConfigHugepagesConfig",
    ...,
    "NodePoolNodeConfigLocalNvmeSsdBlockConfig",
    "NodePoolNodeConfigReservationAffinity",
    "NodePoolNodeConfigSandboxConfig",
    "NodePoolNodeConfigSecondaryBootDisk",
    "NodePoolNodeConfigShieldedInstanceConfig",
    "NodePoolNodeConfigSoleTenantConfig",
    "NodePoolNodeConfigSoleTenantConfigNodeAffinity",
    "NodePoolNodeConfigTaint",
    "NodePoolNodeConfigWindowsNodeConfig",
    "NodePoolNodeConfigWorkloadMetadataConfig",
    "NodePoolNodeDrainConfig",
    "NodePoolPlacementPolicy",
    "NodePoolQueuedProvisioning",
    "NodePoolUpgradeSettings",
    "NodePoolUpgradeSettingsBlueGreenSettings",
    ...,
    ...,
    "GetClusterAddonsConfigResult",
    "GetClusterAddonsConfigCloudrunConfigResult",
    "GetClusterAddonsConfigConfigConnectorConfigResult",
    "GetClusterAddonsConfigDnsCacheConfigResult",
    ...,
    ...,
    "GetClusterAddonsConfigGcsFuseCsiDriverConfigResult",
    "GetClusterAddonsConfigGkeBackupAgentConfigResult",
    ...,
    "GetClusterAddonsConfigHttpLoadBalancingResult",
    "GetClusterAddonsConfigIstioConfigResult",
    "GetClusterAddonsConfigKalmConfigResult",
    "GetClusterAddonsConfigLustreCsiDriverConfigResult",
    "GetClusterAddonsConfigNetworkPolicyConfigResult",
    ...,
    "GetClusterAddonsConfigPodSnapshotConfigResult",
    "GetClusterAddonsConfigRayOperatorConfigResult",
    ...,
    ...,
    "GetClusterAddonsConfigSliceControllerConfigResult",
    "GetClusterAddonsConfigStatefulHaConfigResult",
    "GetClusterAnonymousAuthenticationConfigResult",
    "GetClusterAuthenticatorGroupsConfigResult",
    "GetClusterBinaryAuthorizationResult",
    "GetClusterClusterAutoscalingResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetClusterClusterAutoscalingResourceLimitResult",
    "GetClusterClusterTelemetryResult",
    "GetClusterConfidentialNodeResult",
    "GetClusterControlPlaneEndpointsConfigResult",
    ...,
    ...,
    "GetClusterCostManagementConfigResult",
    "GetClusterDatabaseEncryptionResult",
    "GetClusterDefaultSnatStatusResult",
    "GetClusterDnsConfigResult",
    "GetClusterEnableK8sBetaApiResult",
    "GetClusterEnterpriseConfigResult",
    "GetClusterFleetResult",
    "GetClusterGatewayApiConfigResult",
    "GetClusterGkeAutoUpgradeConfigResult",
    "GetClusterIdentityServiceConfigResult",
    "GetClusterIpAllocationPolicyResult",
    ...,
    ...,
    "GetClusterIpAllocationPolicyAutoIpamConfigResult",
    ...,
    ...,
    "GetClusterLoggingConfigResult",
    "GetClusterMaintenancePolicyResult",
    ...,
    "GetClusterMaintenancePolicyDisruptionBudgetResult",
    ...,
    ...,
    "GetClusterMaintenancePolicyRecurringWindowResult",
    "GetClusterManagedOpentelemetryConfigResult",
    "GetClusterMasterAuthResult",
    "GetClusterMasterAuthClientCertificateConfigResult",
    "GetClusterMasterAuthorizedNetworksConfigResult",
    ...,
    "GetClusterMeshCertificateResult",
    "GetClusterMonitoringConfigResult",
    ...,
    "GetClusterMonitoringConfigManagedPrometheusResult",
    ...,
    "GetClusterNetworkPerformanceConfigResult",
    "GetClusterNetworkPolicyResult",
    "GetClusterNodeConfigResult",
    "GetClusterNodeConfigAdvancedMachineFeatureResult",
    "GetClusterNodeConfigBootDiskResult",
    "GetClusterNodeConfigConfidentialNodeResult",
    "GetClusterNodeConfigContainerdConfigResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetClusterNodeConfigEffectiveTaintResult",
    "GetClusterNodeConfigEphemeralStorageConfigResult",
    ...,
    "GetClusterNodeConfigFastSocketResult",
    "GetClusterNodeConfigGcfsConfigResult",
    "GetClusterNodeConfigGuestAcceleratorResult",
    ...,
    ...,
    "GetClusterNodeConfigGvnicResult",
    "GetClusterNodeConfigHostMaintenancePolicyResult",
    "GetClusterNodeConfigKubeletConfigResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetClusterNodeConfigLinuxNodeConfigResult",
    ...,
    ...,
    "GetClusterNodeConfigLocalNvmeSsdBlockConfigResult",
    "GetClusterNodeConfigReservationAffinityResult",
    "GetClusterNodeConfigSandboxConfigResult",
    "GetClusterNodeConfigSecondaryBootDiskResult",
    "GetClusterNodeConfigShieldedInstanceConfigResult",
    "GetClusterNodeConfigSoleTenantConfigResult",
    ...,
    "GetClusterNodeConfigTaintResult",
    "GetClusterNodeConfigWindowsNodeConfigResult",
    "GetClusterNodeConfigWorkloadMetadataConfigResult",
    "GetClusterNodePoolResult",
    "GetClusterNodePoolAutoConfigResult",
    "GetClusterNodePoolAutoConfigLinuxNodeConfigResult",
    ...,
    "GetClusterNodePoolAutoConfigNetworkTagResult",
    ...,
    "GetClusterNodePoolAutoscalingResult",
    "GetClusterNodePoolDefaultResult",
    "GetClusterNodePoolDefaultNodeConfigDefaultResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetClusterNodePoolManagementResult",
    "GetClusterNodePoolNetworkConfigResult",
    ...,
    ...,
    ...,
    ...,
    "GetClusterNodePoolNodeConfigResult",
    ...,
    "GetClusterNodePoolNodeConfigBootDiskResult",
    "GetClusterNodePoolNodeConfigConfidentialNodeResult",
    "GetClusterNodePoolNodeConfigContainerdConfigResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetClusterNodePoolNodeConfigEffectiveTaintResult",
    ...,
    ...,
    "GetClusterNodePoolNodeConfigFastSocketResult",
    "GetClusterNodePoolNodeConfigGcfsConfigResult",
    "GetClusterNodePoolNodeConfigGuestAcceleratorResult",
    ...,
    ...,
    "GetClusterNodePoolNodeConfigGvnicResult",
    ...,
    "GetClusterNodePoolNodeConfigKubeletConfigResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetClusterNodePoolNodeConfigLinuxNodeConfigResult",
    ...,
    ...,
    ...,
    ...,
    "GetClusterNodePoolNodeConfigSandboxConfigResult",
    ...,
    ...,
    "GetClusterNodePoolNodeConfigSoleTenantConfigResult",
    ...,
    "GetClusterNodePoolNodeConfigTaintResult",
    ...,
    ...,
    "GetClusterNodePoolNodeDrainConfigResult",
    "GetClusterNodePoolPlacementPolicyResult",
    "GetClusterNodePoolQueuedProvisioningResult",
    "GetClusterNodePoolUpgradeSettingResult",
    ...,
    ...,
    ...,
    "GetClusterNotificationConfigResult",
    "GetClusterNotificationConfigPubsubResult",
    "GetClusterNotificationConfigPubsubFilterResult",
    "GetClusterPodAutoscalingResult",
    "GetClusterPodSecurityPolicyConfigResult",
    "GetClusterPrivateClusterConfigResult",
    ...,
    "GetClusterProtectConfigResult",
    "GetClusterProtectConfigWorkloadConfigResult",
    "GetClusterRbacBindingConfigResult",
    "GetClusterReleaseChannelResult",
    "GetClusterResourceUsageExportConfigResult",
    ...,
    "GetClusterSecretManagerConfigResult",
    "GetClusterSecretManagerConfigRotationConfigResult",
    "GetClusterSecretSyncConfigResult",
    "GetClusterSecretSyncConfigRotationConfigResult",
    "GetClusterSecurityPostureConfigResult",
    "GetClusterServiceExternalIpsConfigResult",
    "GetClusterTpuConfigResult",
    "GetClusterUserManagedKeysConfigResult",
    "GetClusterVerticalPodAutoscalingResult",
    "GetClusterWorkloadAltsConfigResult",
    "GetClusterWorkloadIdentityConfigResult",
]

@pulumi.output_type
class AttachedClusterAuthorization(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        admin_groups: Optional[Sequence[_builtins.str]] = ...,
        admin_users: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminGroups")
    def admin_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="adminUsers")
    def admin_users(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AttachedClusterBinaryAuthorization(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, evaluation_mode: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="evaluationMode")
    def evaluation_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AttachedClusterError(dict):
    def __init__(__self__, *, message: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AttachedClusterFleet(dict):
    def __init__(
        __self__, *, project: _builtins.str, membership: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AttachedClusterLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        component_config: Optional[
            outputs.AttachedClusterLoggingConfigComponentConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentConfig")
    def component_config(
        self,
    ) -> Optional[outputs.AttachedClusterLoggingConfigComponentConfig]: ...

@pulumi.output_type
class AttachedClusterLoggingConfigComponentConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, enable_components: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableComponents")
    def enable_components(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AttachedClusterMonitoringConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        managed_prometheus_config: Optional[
            outputs.AttachedClusterMonitoringConfigManagedPrometheusConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedPrometheusConfig")
    def managed_prometheus_config(
        self,
    ) -> Optional[outputs.AttachedClusterMonitoringConfigManagedPrometheusConfig]: ...

@pulumi.output_type
class AttachedClusterMonitoringConfigManagedPrometheusConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AttachedClusterOidcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, issuer_url: _builtins.str, jwks: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="issuerUrl")
    def issuer_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def jwks(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AttachedClusterProxyConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kubernetes_secret: Optional[
            outputs.AttachedClusterProxyConfigKubernetesSecret
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesSecret")
    def kubernetes_secret(
        self,
    ) -> Optional[outputs.AttachedClusterProxyConfigKubernetesSecret]: ...

@pulumi.output_type
class AttachedClusterProxyConfigKubernetesSecret(dict):
    def __init__(
        __self__, *, name: _builtins.str, namespace: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...

@pulumi.output_type
class AttachedClusterSecurityPostureConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, vulnerability_mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vulnerabilityMode")
    def vulnerability_mode(self) -> _builtins.str: ...

@pulumi.output_type
class AttachedClusterWorkloadIdentityConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identity_provider: Optional[_builtins.str] = ...,
        issuer_uri: Optional[_builtins.str] = ...,
        workload_pool: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityProvider")
    def identity_provider(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadPool")
    def workload_pool(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AwsClusterAuthorization(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        admin_users: Sequence[outputs.AwsClusterAuthorizationAdminUser],
        admin_groups: Optional[
            Sequence[outputs.AwsClusterAuthorizationAdminGroup]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminUsers")
    def admin_users(self) -> Sequence[outputs.AwsClusterAuthorizationAdminUser]: ...
    @_builtins.property
    @pulumi.getter(name="adminGroups")
    def admin_groups(
        self,
    ) -> Optional[Sequence[outputs.AwsClusterAuthorizationAdminGroup]]: ...

@pulumi.output_type
class AwsClusterAuthorizationAdminGroup(dict):
    def __init__(__self__, *, group: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str: ...

@pulumi.output_type
class AwsClusterAuthorizationAdminUser(dict):
    def __init__(__self__, *, username: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class AwsClusterBinaryAuthorization(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, evaluation_mode: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="evaluationMode")
    def evaluation_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AwsClusterControlPlane(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aws_services_authentication: outputs.AwsClusterControlPlaneAwsServicesAuthentication,
        config_encryption: outputs.AwsClusterControlPlaneConfigEncryption,
        database_encryption: outputs.AwsClusterControlPlaneDatabaseEncryption,
        iam_instance_profile: _builtins.str,
        subnet_ids: Sequence[_builtins.str],
        version: _builtins.str,
        instance_placement: Optional[
            outputs.AwsClusterControlPlaneInstancePlacement
        ] = ...,
        instance_type: Optional[_builtins.str] = ...,
        main_volume: Optional[outputs.AwsClusterControlPlaneMainVolume] = ...,
        proxy_config: Optional[outputs.AwsClusterControlPlaneProxyConfig] = ...,
        root_volume: Optional[outputs.AwsClusterControlPlaneRootVolume] = ...,
        security_group_ids: Optional[Sequence[_builtins.str]] = ...,
        ssh_config: Optional[outputs.AwsClusterControlPlaneSshConfig] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsServicesAuthentication")
    def aws_services_authentication(
        self,
    ) -> outputs.AwsClusterControlPlaneAwsServicesAuthentication: ...
    @_builtins.property
    @pulumi.getter(name="configEncryption")
    def config_encryption(self) -> outputs.AwsClusterControlPlaneConfigEncryption: ...
    @_builtins.property
    @pulumi.getter(name="databaseEncryption")
    def database_encryption(
        self,
    ) -> outputs.AwsClusterControlPlaneDatabaseEncryption: ...
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instancePlacement")
    def instance_placement(
        self,
    ) -> Optional[outputs.AwsClusterControlPlaneInstancePlacement]: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mainVolume")
    def main_volume(self) -> Optional[outputs.AwsClusterControlPlaneMainVolume]: ...
    @_builtins.property
    @pulumi.getter(name="proxyConfig")
    def proxy_config(self) -> Optional[outputs.AwsClusterControlPlaneProxyConfig]: ...
    @_builtins.property
    @pulumi.getter(name="rootVolume")
    def root_volume(self) -> Optional[outputs.AwsClusterControlPlaneRootVolume]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sshConfig")
    def ssh_config(self) -> Optional[outputs.AwsClusterControlPlaneSshConfig]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class AwsClusterControlPlaneAwsServicesAuthentication(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        role_arn: _builtins.str,
        role_session_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleSessionName")
    def role_session_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AwsClusterControlPlaneConfigEncryption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AwsClusterControlPlaneDatabaseEncryption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AwsClusterControlPlaneInstancePlacement(dict):
    def __init__(__self__, *, tenancy: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AwsClusterControlPlaneMainVolume(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        iops: Optional[_builtins.int] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
        size_gib: Optional[_builtins.int] = ...,
        throughput: Optional[_builtins.int] = ...,
        volume_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sizeGib")
    def size_gib(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AwsClusterControlPlaneProxyConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, secret_arn: _builtins.str, secret_version: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class AwsClusterControlPlaneRootVolume(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        iops: Optional[_builtins.int] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
        size_gib: Optional[_builtins.int] = ...,
        throughput: Optional[_builtins.int] = ...,
        volume_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sizeGib")
    def size_gib(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AwsClusterControlPlaneSshConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, ec2_key_pair: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ec2KeyPair")
    def ec2_key_pair(self) -> _builtins.str: ...

@pulumi.output_type
class AwsClusterFleet(dict):
    def __init__(
        __self__,
        *,
        membership: Optional[_builtins.str] = ...,
        project: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AwsClusterLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        component_config: Optional[
            outputs.AwsClusterLoggingConfigComponentConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentConfig")
    def component_config(
        self,
    ) -> Optional[outputs.AwsClusterLoggingConfigComponentConfig]: ...

@pulumi.output_type
class AwsClusterLoggingConfigComponentConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, enable_components: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableComponents")
    def enable_components(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AwsClusterNetworking(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        pod_address_cidr_blocks: Sequence[_builtins.str],
        service_address_cidr_blocks: Sequence[_builtins.str],
        vpc_id: _builtins.str,
        per_node_pool_sg_rules_disabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="podAddressCidrBlocks")
    def pod_address_cidr_blocks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAddressCidrBlocks")
    def service_address_cidr_blocks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="perNodePoolSgRulesDisabled")
    def per_node_pool_sg_rules_disabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AwsClusterWorkloadIdentityConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identity_provider: Optional[_builtins.str] = ...,
        issuer_uri: Optional[_builtins.str] = ...,
        workload_pool: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityProvider")
    def identity_provider(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadPool")
    def workload_pool(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AwsNodePoolAutoscaling(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, max_node_count: _builtins.int, min_node_count: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> _builtins.int: ...

@pulumi.output_type
class AwsNodePoolConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        config_encryption: outputs.AwsNodePoolConfigConfigEncryption,
        iam_instance_profile: _builtins.str,
        autoscaling_metrics_collection: Optional[
            outputs.AwsNodePoolConfigAutoscalingMetricsCollection
        ] = ...,
        image_type: Optional[_builtins.str] = ...,
        instance_placement: Optional[outputs.AwsNodePoolConfigInstancePlacement] = ...,
        instance_type: Optional[_builtins.str] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        proxy_config: Optional[outputs.AwsNodePoolConfigProxyConfig] = ...,
        root_volume: Optional[outputs.AwsNodePoolConfigRootVolume] = ...,
        security_group_ids: Optional[Sequence[_builtins.str]] = ...,
        spot_config: Optional[outputs.AwsNodePoolConfigSpotConfig] = ...,
        ssh_config: Optional[outputs.AwsNodePoolConfigSshConfig] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
        taints: Optional[Sequence[outputs.AwsNodePoolConfigTaint]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configEncryption")
    def config_encryption(self) -> outputs.AwsNodePoolConfigConfigEncryption: ...
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingMetricsCollection")
    def autoscaling_metrics_collection(
        self,
    ) -> Optional[outputs.AwsNodePoolConfigAutoscalingMetricsCollection]: ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instancePlacement")
    def instance_placement(
        self,
    ) -> Optional[outputs.AwsNodePoolConfigInstancePlacement]: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="proxyConfig")
    def proxy_config(self) -> Optional[outputs.AwsNodePoolConfigProxyConfig]: ...
    @_builtins.property
    @pulumi.getter(name="rootVolume")
    def root_volume(self) -> Optional[outputs.AwsNodePoolConfigRootVolume]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="spotConfig")
    def spot_config(self) -> Optional[outputs.AwsNodePoolConfigSpotConfig]: ...
    @_builtins.property
    @pulumi.getter(name="sshConfig")
    def ssh_config(self) -> Optional[outputs.AwsNodePoolConfigSshConfig]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def taints(self) -> Optional[Sequence[outputs.AwsNodePoolConfigTaint]]: ...

@pulumi.output_type
class AwsNodePoolConfigAutoscalingMetricsCollection(dict):
    def __init__(
        __self__,
        *,
        granularity: _builtins.str,
        metrics: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def granularity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AwsNodePoolConfigConfigEncryption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AwsNodePoolConfigInstancePlacement(dict):
    def __init__(__self__, *, tenancy: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AwsNodePoolConfigProxyConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, secret_arn: _builtins.str, secret_version: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class AwsNodePoolConfigRootVolume(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        iops: Optional[_builtins.int] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
        size_gib: Optional[_builtins.int] = ...,
        throughput: Optional[_builtins.int] = ...,
        volume_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sizeGib")
    def size_gib(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AwsNodePoolConfigSpotConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, instance_types: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class AwsNodePoolConfigSshConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, ec2_key_pair: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ec2KeyPair")
    def ec2_key_pair(self) -> _builtins.str: ...

@pulumi.output_type
class AwsNodePoolConfigTaint(dict):
    def __init__(
        __self__, *, effect: _builtins.str, key: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class AwsNodePoolKubeletConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cpu_cfs_quota: Optional[_builtins.bool] = ...,
        cpu_cfs_quota_period: Optional[_builtins.str] = ...,
        cpu_manager_policy: Optional[_builtins.str] = ...,
        pod_pids_limit: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuota")
    def cpu_cfs_quota(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuotaPeriod")
    def cpu_cfs_quota_period(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cpuManagerPolicy")
    def cpu_manager_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="podPidsLimit")
    def pod_pids_limit(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AwsNodePoolManagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, auto_repair: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRepair")
    def auto_repair(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AwsNodePoolMaxPodsConstraint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, max_pods_per_node: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> _builtins.int: ...

@pulumi.output_type
class AwsNodePoolUpdateSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        surge_settings: Optional[outputs.AwsNodePoolUpdateSettingsSurgeSettings] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="surgeSettings")
    def surge_settings(
        self,
    ) -> Optional[outputs.AwsNodePoolUpdateSettingsSurgeSettings]: ...

@pulumi.output_type
class AwsNodePoolUpdateSettingsSurgeSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_surge: Optional[_builtins.int] = ...,
        max_unavailable: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxSurge")
    def max_surge(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxUnavailable")
    def max_unavailable(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AzureClusterAuthorization(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        admin_users: Sequence[outputs.AzureClusterAuthorizationAdminUser],
        admin_groups: Optional[
            Sequence[outputs.AzureClusterAuthorizationAdminGroup]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminUsers")
    def admin_users(self) -> Sequence[outputs.AzureClusterAuthorizationAdminUser]: ...
    @_builtins.property
    @pulumi.getter(name="adminGroups")
    def admin_groups(
        self,
    ) -> Optional[Sequence[outputs.AzureClusterAuthorizationAdminGroup]]: ...

@pulumi.output_type
class AzureClusterAuthorizationAdminGroup(dict):
    def __init__(__self__, *, group: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str: ...

@pulumi.output_type
class AzureClusterAuthorizationAdminUser(dict):
    def __init__(__self__, *, username: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class AzureClusterAzureServicesAuthentication(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, application_id: _builtins.str, tenant_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...

@pulumi.output_type
class AzureClusterControlPlane(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ssh_config: outputs.AzureClusterControlPlaneSshConfig,
        subnet_id: _builtins.str,
        version: _builtins.str,
        database_encryption: Optional[
            outputs.AzureClusterControlPlaneDatabaseEncryption
        ] = ...,
        main_volume: Optional[outputs.AzureClusterControlPlaneMainVolume] = ...,
        proxy_config: Optional[outputs.AzureClusterControlPlaneProxyConfig] = ...,
        replica_placements: Optional[
            Sequence[outputs.AzureClusterControlPlaneReplicaPlacement]
        ] = ...,
        root_volume: Optional[outputs.AzureClusterControlPlaneRootVolume] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
        vm_size: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sshConfig")
    def ssh_config(self) -> outputs.AzureClusterControlPlaneSshConfig: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseEncryption")
    def database_encryption(
        self,
    ) -> Optional[outputs.AzureClusterControlPlaneDatabaseEncryption]: ...
    @_builtins.property
    @pulumi.getter(name="mainVolume")
    def main_volume(self) -> Optional[outputs.AzureClusterControlPlaneMainVolume]: ...
    @_builtins.property
    @pulumi.getter(name="proxyConfig")
    def proxy_config(self) -> Optional[outputs.AzureClusterControlPlaneProxyConfig]: ...
    @_builtins.property
    @pulumi.getter(name="replicaPlacements")
    def replica_placements(
        self,
    ) -> Optional[Sequence[outputs.AzureClusterControlPlaneReplicaPlacement]]: ...
    @_builtins.property
    @pulumi.getter(name="rootVolume")
    def root_volume(self) -> Optional[outputs.AzureClusterControlPlaneRootVolume]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureClusterControlPlaneDatabaseEncryption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, key_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> _builtins.str: ...

@pulumi.output_type
class AzureClusterControlPlaneMainVolume(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, size_gib: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeGib")
    def size_gib(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AzureClusterControlPlaneProxyConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, resource_group_id: _builtins.str, secret_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> _builtins.str: ...

@pulumi.output_type
class AzureClusterControlPlaneReplicaPlacement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, azure_availability_zone: _builtins.str, subnet_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureAvailabilityZone")
    def azure_availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...

@pulumi.output_type
class AzureClusterControlPlaneRootVolume(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, size_gib: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeGib")
    def size_gib(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AzureClusterControlPlaneSshConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, authorized_key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizedKey")
    def authorized_key(self) -> _builtins.str: ...

@pulumi.output_type
class AzureClusterFleet(dict):
    def __init__(
        __self__,
        *,
        membership: Optional[_builtins.str] = ...,
        project: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureClusterLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        component_config: Optional[
            outputs.AzureClusterLoggingConfigComponentConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentConfig")
    def component_config(
        self,
    ) -> Optional[outputs.AzureClusterLoggingConfigComponentConfig]: ...

@pulumi.output_type
class AzureClusterLoggingConfigComponentConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, enable_components: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableComponents")
    def enable_components(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AzureClusterNetworking(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        pod_address_cidr_blocks: Sequence[_builtins.str],
        service_address_cidr_blocks: Sequence[_builtins.str],
        virtual_network_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="podAddressCidrBlocks")
    def pod_address_cidr_blocks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAddressCidrBlocks")
    def service_address_cidr_blocks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> _builtins.str: ...

@pulumi.output_type
class AzureClusterWorkloadIdentityConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identity_provider: Optional[_builtins.str] = ...,
        issuer_uri: Optional[_builtins.str] = ...,
        workload_pool: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityProvider")
    def identity_provider(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadPool")
    def workload_pool(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureNodePoolAutoscaling(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, max_node_count: _builtins.int, min_node_count: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> _builtins.int: ...

@pulumi.output_type
class AzureNodePoolConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ssh_config: outputs.AzureNodePoolConfigSshConfig,
        image_type: Optional[_builtins.str] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        proxy_config: Optional[outputs.AzureNodePoolConfigProxyConfig] = ...,
        root_volume: Optional[outputs.AzureNodePoolConfigRootVolume] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
        vm_size: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sshConfig")
    def ssh_config(self) -> outputs.AzureNodePoolConfigSshConfig: ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="proxyConfig")
    def proxy_config(self) -> Optional[outputs.AzureNodePoolConfigProxyConfig]: ...
    @_builtins.property
    @pulumi.getter(name="rootVolume")
    def root_volume(self) -> Optional[outputs.AzureNodePoolConfigRootVolume]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureNodePoolConfigProxyConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, resource_group_id: _builtins.str, secret_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> _builtins.str: ...

@pulumi.output_type
class AzureNodePoolConfigRootVolume(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, size_gib: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeGib")
    def size_gib(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AzureNodePoolConfigSshConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, authorized_key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizedKey")
    def authorized_key(self) -> _builtins.str: ...

@pulumi.output_type
class AzureNodePoolManagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, auto_repair: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRepair")
    def auto_repair(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AzureNodePoolMaxPodsConstraint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, max_pods_per_node: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> _builtins.int: ...

@pulumi.output_type
class ClusterAddonsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloudrun_config: Optional[outputs.ClusterAddonsConfigCloudrunConfig] = ...,
        config_connector_config: Optional[
            outputs.ClusterAddonsConfigConfigConnectorConfig
        ] = ...,
        dns_cache_config: Optional[outputs.ClusterAddonsConfigDnsCacheConfig] = ...,
        gce_persistent_disk_csi_driver_config: Optional[
            outputs.ClusterAddonsConfigGcePersistentDiskCsiDriverConfig
        ] = ...,
        gcp_filestore_csi_driver_config: Optional[
            outputs.ClusterAddonsConfigGcpFilestoreCsiDriverConfig
        ] = ...,
        gcs_fuse_csi_driver_config: Optional[
            outputs.ClusterAddonsConfigGcsFuseCsiDriverConfig
        ] = ...,
        gke_backup_agent_config: Optional[
            outputs.ClusterAddonsConfigGkeBackupAgentConfig
        ] = ...,
        horizontal_pod_autoscaling: Optional[
            outputs.ClusterAddonsConfigHorizontalPodAutoscaling
        ] = ...,
        http_load_balancing: Optional[
            outputs.ClusterAddonsConfigHttpLoadBalancing
        ] = ...,
        istio_config: Optional[outputs.ClusterAddonsConfigIstioConfig] = ...,
        kalm_config: Optional[outputs.ClusterAddonsConfigKalmConfig] = ...,
        lustre_csi_driver_config: Optional[
            outputs.ClusterAddonsConfigLustreCsiDriverConfig
        ] = ...,
        network_policy_config: Optional[
            outputs.ClusterAddonsConfigNetworkPolicyConfig
        ] = ...,
        parallelstore_csi_driver_config: Optional[
            outputs.ClusterAddonsConfigParallelstoreCsiDriverConfig
        ] = ...,
        pod_snapshot_config: Optional[
            outputs.ClusterAddonsConfigPodSnapshotConfig
        ] = ...,
        ray_operator_configs: Optional[
            Sequence[outputs.ClusterAddonsConfigRayOperatorConfig]
        ] = ...,
        slice_controller_config: Optional[
            outputs.ClusterAddonsConfigSliceControllerConfig
        ] = ...,
        stateful_ha_config: Optional[outputs.ClusterAddonsConfigStatefulHaConfig] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudrunConfig")
    def cloudrun_config(
        self,
    ) -> Optional[outputs.ClusterAddonsConfigCloudrunConfig]: ...
    @_builtins.property
    @pulumi.getter(name="configConnectorConfig")
    def config_connector_config(
        self,
    ) -> Optional[outputs.ClusterAddonsConfigConfigConnectorConfig]: ...
    @_builtins.property
    @pulumi.getter(name="dnsCacheConfig")
    def dns_cache_config(
        self,
    ) -> Optional[outputs.ClusterAddonsConfigDnsCacheConfig]: ...
    @_builtins.property
    @pulumi.getter(name="gcePersistentDiskCsiDriverConfig")
    def gce_persistent_disk_csi_driver_config(
        self,
    ) -> Optional[outputs.ClusterAddonsConfigGcePersistentDiskCsiDriverConfig]: ...
    @_builtins.property
    @pulumi.getter(name="gcpFilestoreCsiDriverConfig")
    def gcp_filestore_csi_driver_config(
        self,
    ) -> Optional[outputs.ClusterAddonsConfigGcpFilestoreCsiDriverConfig]: ...
    @_builtins.property
    @pulumi.getter(name="gcsFuseCsiDriverConfig")
    def gcs_fuse_csi_driver_config(
        self,
    ) -> Optional[outputs.ClusterAddonsConfigGcsFuseCsiDriverConfig]: ...
    @_builtins.property
    @pulumi.getter(name="gkeBackupAgentConfig")
    def gke_backup_agent_config(
        self,
    ) -> Optional[outputs.ClusterAddonsConfigGkeBackupAgentConfig]: ...
    @_builtins.property
    @pulumi.getter(name="horizontalPodAutoscaling")
    def horizontal_pod_autoscaling(
        self,
    ) -> Optional[outputs.ClusterAddonsConfigHorizontalPodAutoscaling]: ...
    @_builtins.property
    @pulumi.getter(name="httpLoadBalancing")
    def http_load_balancing(
        self,
    ) -> Optional[outputs.ClusterAddonsConfigHttpLoadBalancing]: ...
    @_builtins.property
    @pulumi.getter(name="istioConfig")
    def istio_config(self) -> Optional[outputs.ClusterAddonsConfigIstioConfig]: ...
    @_builtins.property
    @pulumi.getter(name="kalmConfig")
    def kalm_config(self) -> Optional[outputs.ClusterAddonsConfigKalmConfig]: ...
    @_builtins.property
    @pulumi.getter(name="lustreCsiDriverConfig")
    def lustre_csi_driver_config(
        self,
    ) -> Optional[outputs.ClusterAddonsConfigLustreCsiDriverConfig]: ...
    @_builtins.property
    @pulumi.getter(name="networkPolicyConfig")
    def network_policy_config(
        self,
    ) -> Optional[outputs.ClusterAddonsConfigNetworkPolicyConfig]: ...
    @_builtins.property
    @pulumi.getter(name="parallelstoreCsiDriverConfig")
    def parallelstore_csi_driver_config(
        self,
    ) -> Optional[outputs.ClusterAddonsConfigParallelstoreCsiDriverConfig]: ...
    @_builtins.property
    @pulumi.getter(name="podSnapshotConfig")
    def pod_snapshot_config(
        self,
    ) -> Optional[outputs.ClusterAddonsConfigPodSnapshotConfig]: ...
    @_builtins.property
    @pulumi.getter(name="rayOperatorConfigs")
    def ray_operator_configs(
        self,
    ) -> Optional[Sequence[outputs.ClusterAddonsConfigRayOperatorConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="sliceControllerConfig")
    def slice_controller_config(
        self,
    ) -> Optional[outputs.ClusterAddonsConfigSliceControllerConfig]: ...
    @_builtins.property
    @pulumi.getter(name="statefulHaConfig")
    def stateful_ha_config(
        self,
    ) -> Optional[outputs.ClusterAddonsConfigStatefulHaConfig]: ...

@pulumi.output_type
class ClusterAddonsConfigCloudrunConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disabled: _builtins.bool,
        load_balancer_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterAddonsConfigConfigConnectorConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAddonsConfigDnsCacheConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAddonsConfigGcePersistentDiskCsiDriverConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAddonsConfigGcpFilestoreCsiDriverConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAddonsConfigGcsFuseCsiDriverConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAddonsConfigGkeBackupAgentConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAddonsConfigHorizontalPodAutoscaling(dict):
    def __init__(__self__, *, disabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAddonsConfigHttpLoadBalancing(dict):
    def __init__(__self__, *, disabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAddonsConfigIstioConfig(dict):
    def __init__(
        __self__, *, disabled: _builtins.bool, auth: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterAddonsConfigKalmConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAddonsConfigLustreCsiDriverConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        enable_legacy_lustre_port: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableLegacyLustrePort")
    def enable_legacy_lustre_port(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterAddonsConfigNetworkPolicyConfig(dict):
    def __init__(__self__, *, disabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAddonsConfigParallelstoreCsiDriverConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAddonsConfigPodSnapshotConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAddonsConfigRayOperatorConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        ray_cluster_logging_config: Optional[
            outputs.ClusterAddonsConfigRayOperatorConfigRayClusterLoggingConfig
        ] = ...,
        ray_cluster_monitoring_config: Optional[
            outputs.ClusterAddonsConfigRayOperatorConfigRayClusterMonitoringConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="rayClusterLoggingConfig")
    def ray_cluster_logging_config(
        self,
    ) -> Optional[
        outputs.ClusterAddonsConfigRayOperatorConfigRayClusterLoggingConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="rayClusterMonitoringConfig")
    def ray_cluster_monitoring_config(
        self,
    ) -> Optional[
        outputs.ClusterAddonsConfigRayOperatorConfigRayClusterMonitoringConfig
    ]: ...

@pulumi.output_type
class ClusterAddonsConfigRayOperatorConfigRayClusterLoggingConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAddonsConfigRayOperatorConfigRayClusterMonitoringConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAddonsConfigSliceControllerConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAddonsConfigStatefulHaConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterAnonymousAuthenticationConfig(dict):
    def __init__(__self__, *, mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterAuthenticatorGroupsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, security_group: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroup")
    def security_group(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterBinaryAuthorization(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        evaluation_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""Deprecated in favor of evaluation_mode.""")
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="evaluationMode")
    def evaluation_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterClusterAutoscaling(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auto_provisioning_defaults: Optional[
            outputs.ClusterClusterAutoscalingAutoProvisioningDefaults
        ] = ...,
        auto_provisioning_locations: Optional[Sequence[_builtins.str]] = ...,
        autoscaling_profile: Optional[_builtins.str] = ...,
        default_compute_class_enabled: Optional[_builtins.bool] = ...,
        enabled: Optional[_builtins.bool] = ...,
        resource_limits: Optional[
            Sequence[outputs.ClusterClusterAutoscalingResourceLimit]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoProvisioningDefaults")
    def auto_provisioning_defaults(
        self,
    ) -> Optional[outputs.ClusterClusterAutoscalingAutoProvisioningDefaults]: ...
    @_builtins.property
    @pulumi.getter(name="autoProvisioningLocations")
    def auto_provisioning_locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingProfile")
    def autoscaling_profile(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultComputeClassEnabled")
    def default_compute_class_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="resourceLimits")
    def resource_limits(
        self,
    ) -> Optional[Sequence[outputs.ClusterClusterAutoscalingResourceLimit]]: ...

@pulumi.output_type
class ClusterClusterAutoscalingAutoProvisioningDefaults(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        boot_disk_kms_key: Optional[_builtins.str] = ...,
        disk_size: Optional[_builtins.int] = ...,
        disk_type: Optional[_builtins.str] = ...,
        image_type: Optional[_builtins.str] = ...,
        management: Optional[
            outputs.ClusterClusterAutoscalingAutoProvisioningDefaultsManagement
        ] = ...,
        min_cpu_platform: Optional[_builtins.str] = ...,
        oauth_scopes: Optional[Sequence[_builtins.str]] = ...,
        service_account: Optional[_builtins.str] = ...,
        shielded_instance_config: Optional[
            outputs.ClusterClusterAutoscalingAutoProvisioningDefaultsShieldedInstanceConfig
        ] = ...,
        upgrade_settings: Optional[
            outputs.ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskKmsKey")
    def boot_disk_kms_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def management(
        self,
    ) -> Optional[
        outputs.ClusterClusterAutoscalingAutoProvisioningDefaultsManagement
    ]: ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[
        outputs.ClusterClusterAutoscalingAutoProvisioningDefaultsShieldedInstanceConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(
        self,
    ) -> Optional[
        outputs.ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettings
    ]: ...

@pulumi.output_type
class ClusterClusterAutoscalingAutoProvisioningDefaultsManagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auto_repair: Optional[_builtins.bool] = ...,
        auto_upgrade: Optional[_builtins.bool] = ...,
        upgrade_options: Optional[
            Sequence[
                outputs.ClusterClusterAutoscalingAutoProvisioningDefaultsManagementUpgradeOption
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRepair")
    def auto_repair(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="autoUpgrade")
    def auto_upgrade(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="upgradeOptions")
    def upgrade_options(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClusterClusterAutoscalingAutoProvisioningDefaultsManagementUpgradeOption
        ]
    ]: ...

@pulumi.output_type
class ClusterClusterAutoscalingAutoProvisioningDefaultsManagementUpgradeOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auto_upgrade_start_time: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoUpgradeStartTime")
    def auto_upgrade_start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterClusterAutoscalingAutoProvisioningDefaultsShieldedInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: Optional[_builtins.bool] = ...,
        enable_secure_boot: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        blue_green_settings: Optional[
            outputs.ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettings
        ] = ...,
        max_surge: Optional[_builtins.int] = ...,
        max_unavailable: Optional[_builtins.int] = ...,
        strategy: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blueGreenSettings")
    def blue_green_settings(
        self,
    ) -> Optional[
        outputs.ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maxSurge")
    def max_surge(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxUnavailable")
    def max_unavailable(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def strategy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        node_pool_soak_duration: Optional[_builtins.str] = ...,
        standard_rollout_policy: Optional[
            outputs.ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodePoolSoakDuration")
    def node_pool_soak_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="standardRolloutPolicy")
    def standard_rollout_policy(
        self,
    ) -> Optional[
        outputs.ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy
    ]: ...

@pulumi.output_type
class ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        batch_node_count: Optional[_builtins.int] = ...,
        batch_percentage: Optional[_builtins.float] = ...,
        batch_soak_duration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchNodeCount")
    def batch_node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="batchPercentage")
    def batch_percentage(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="batchSoakDuration")
    def batch_soak_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterClusterAutoscalingResourceLimit(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        maximum: _builtins.int,
        resource_type: _builtins.str,
        minimum: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterClusterTelemetry(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterConfidentialNodes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        confidential_instance_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceType")
    def confidential_instance_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterControlPlaneEndpointsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_endpoint_config: Optional[
            outputs.ClusterControlPlaneEndpointsConfigDnsEndpointConfig
        ] = ...,
        ip_endpoints_config: Optional[
            outputs.ClusterControlPlaneEndpointsConfigIpEndpointsConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsEndpointConfig")
    def dns_endpoint_config(
        self,
    ) -> Optional[outputs.ClusterControlPlaneEndpointsConfigDnsEndpointConfig]: ...
    @_builtins.property
    @pulumi.getter(name="ipEndpointsConfig")
    def ip_endpoints_config(
        self,
    ) -> Optional[outputs.ClusterControlPlaneEndpointsConfigIpEndpointsConfig]: ...

@pulumi.output_type
class ClusterControlPlaneEndpointsConfigDnsEndpointConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_external_traffic: Optional[_builtins.bool] = ...,
        enable_k8s_certs_via_dns: Optional[_builtins.bool] = ...,
        enable_k8s_tokens_via_dns: Optional[_builtins.bool] = ...,
        endpoint: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowExternalTraffic")
    def allow_external_traffic(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableK8sCertsViaDns")
    def enable_k8s_certs_via_dns(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableK8sTokensViaDns")
    def enable_k8s_tokens_via_dns(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterControlPlaneEndpointsConfigIpEndpointsConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterCostManagementConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterDatabaseEncryption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, state: _builtins.str, key_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterDefaultSnatStatus(dict):
    def __init__(__self__, *, disabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterDnsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additive_vpc_scope_dns_domain: Optional[_builtins.str] = ...,
        cluster_dns: Optional[_builtins.str] = ...,
        cluster_dns_domain: Optional[_builtins.str] = ...,
        cluster_dns_scope: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additiveVpcScopeDnsDomain")
    def additive_vpc_scope_dns_domain(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterDns")
    def cluster_dns(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterDnsDomain")
    def cluster_dns_domain(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterDnsScope")
    def cluster_dns_scope(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterEnableK8sBetaApis(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, enabled_apis: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledApis")
    def enabled_apis(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ClusterEnterpriseConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_tier: Optional[_builtins.str] = ...,
        desired_tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterTier")
    @_utilities.deprecated(...)
    def cluster_tier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="desiredTier")
    @_utilities.deprecated(...)
    def desired_tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterFleet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        membership: Optional[_builtins.str] = ...,
        membership_id: Optional[_builtins.str] = ...,
        membership_location: Optional[_builtins.str] = ...,
        membership_type: Optional[_builtins.str] = ...,
        pre_registered: Optional[_builtins.bool] = ...,
        project: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="membershipId")
    def membership_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="membershipLocation")
    def membership_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="membershipType")
    def membership_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preRegistered")
    def pre_registered(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterGatewayApiConfig(dict):
    def __init__(__self__, *, channel: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterGkeAutoUpgradeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, patch_mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterIdentityServiceConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterIpAllocationPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_ip_ranges_configs: Optional[
            Sequence[outputs.ClusterIpAllocationPolicyAdditionalIpRangesConfig]
        ] = ...,
        additional_pod_ranges_config: Optional[
            outputs.ClusterIpAllocationPolicyAdditionalPodRangesConfig
        ] = ...,
        auto_ipam_config: Optional[
            outputs.ClusterIpAllocationPolicyAutoIpamConfig
        ] = ...,
        cluster_ipv4_cidr_block: Optional[_builtins.str] = ...,
        cluster_secondary_range_name: Optional[_builtins.str] = ...,
        network_tier_config: Optional[
            outputs.ClusterIpAllocationPolicyNetworkTierConfig
        ] = ...,
        pod_cidr_overprovision_config: Optional[
            outputs.ClusterIpAllocationPolicyPodCidrOverprovisionConfig
        ] = ...,
        services_ipv4_cidr_block: Optional[_builtins.str] = ...,
        services_secondary_range_name: Optional[_builtins.str] = ...,
        stack_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalIpRangesConfigs")
    def additional_ip_ranges_configs(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterIpAllocationPolicyAdditionalIpRangesConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="additionalPodRangesConfig")
    def additional_pod_ranges_config(
        self,
    ) -> Optional[outputs.ClusterIpAllocationPolicyAdditionalPodRangesConfig]: ...
    @_builtins.property
    @pulumi.getter(name="autoIpamConfig")
    def auto_ipam_config(
        self,
    ) -> Optional[outputs.ClusterIpAllocationPolicyAutoIpamConfig]: ...
    @_builtins.property
    @pulumi.getter(name="clusterIpv4CidrBlock")
    def cluster_ipv4_cidr_block(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterSecondaryRangeName")
    def cluster_secondary_range_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkTierConfig")
    def network_tier_config(
        self,
    ) -> Optional[outputs.ClusterIpAllocationPolicyNetworkTierConfig]: ...
    @_builtins.property
    @pulumi.getter(name="podCidrOverprovisionConfig")
    def pod_cidr_overprovision_config(
        self,
    ) -> Optional[outputs.ClusterIpAllocationPolicyPodCidrOverprovisionConfig]: ...
    @_builtins.property
    @pulumi.getter(name="servicesIpv4CidrBlock")
    def services_ipv4_cidr_block(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="servicesSecondaryRangeName")
    def services_secondary_range_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterIpAllocationPolicyAdditionalIpRangesConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subnetwork: _builtins.str,
        pod_ipv4_range_names: Optional[Sequence[_builtins.str]] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="podIpv4RangeNames")
    def pod_ipv4_range_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterIpAllocationPolicyAdditionalPodRangesConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, pod_range_names: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="podRangeNames")
    def pod_range_names(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ClusterIpAllocationPolicyAutoIpamConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterIpAllocationPolicyNetworkTierConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, network_tier: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterIpAllocationPolicyPodCidrOverprovisionConfig(dict):
    def __init__(__self__, *, disabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, enable_components: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableComponents")
    def enable_components(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ClusterMaintenancePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        daily_maintenance_window: Optional[
            outputs.ClusterMaintenancePolicyDailyMaintenanceWindow
        ] = ...,
        disruption_budget: Optional[
            outputs.ClusterMaintenancePolicyDisruptionBudget
        ] = ...,
        maintenance_exclusions: Optional[
            Sequence[outputs.ClusterMaintenancePolicyMaintenanceExclusion]
        ] = ...,
        recurring_window: Optional[
            outputs.ClusterMaintenancePolicyRecurringWindow
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dailyMaintenanceWindow")
    def daily_maintenance_window(
        self,
    ) -> Optional[outputs.ClusterMaintenancePolicyDailyMaintenanceWindow]: ...
    @_builtins.property
    @pulumi.getter(name="disruptionBudget")
    def disruption_budget(
        self,
    ) -> Optional[outputs.ClusterMaintenancePolicyDisruptionBudget]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceExclusions")
    def maintenance_exclusions(
        self,
    ) -> Optional[Sequence[outputs.ClusterMaintenancePolicyMaintenanceExclusion]]: ...
    @_builtins.property
    @pulumi.getter(name="recurringWindow")
    def recurring_window(
        self,
    ) -> Optional[outputs.ClusterMaintenancePolicyRecurringWindow]: ...

@pulumi.output_type
class ClusterMaintenancePolicyDailyMaintenanceWindow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, start_time: _builtins.str, duration: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterMaintenancePolicyDisruptionBudget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        last_disruption_time: Optional[_builtins.str] = ...,
        last_minor_version_disruption_time: Optional[_builtins.str] = ...,
        minor_version_disruption_interval: Optional[_builtins.str] = ...,
        patch_version_disruption_interval: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastDisruptionTime")
    def last_disruption_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastMinorVersionDisruptionTime")
    def last_minor_version_disruption_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minorVersionDisruptionInterval")
    def minor_version_disruption_interval(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="patchVersionDisruptionInterval")
    def patch_version_disruption_interval(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterMaintenancePolicyMaintenanceExclusion(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exclusion_name: _builtins.str,
        start_time: _builtins.str,
        end_time: Optional[_builtins.str] = ...,
        exclusion_options: Optional[
            outputs.ClusterMaintenancePolicyMaintenanceExclusionExclusionOptions
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exclusionName")
    def exclusion_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exclusionOptions")
    def exclusion_options(
        self,
    ) -> Optional[
        outputs.ClusterMaintenancePolicyMaintenanceExclusionExclusionOptions
    ]: ...

@pulumi.output_type
class ClusterMaintenancePolicyMaintenanceExclusionExclusionOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        scope: _builtins.str,
        end_time_behavior: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endTimeBehavior")
    def end_time_behavior(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterMaintenancePolicyRecurringWindow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_time: _builtins.str,
        recurrence: _builtins.str,
        start_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterManagedOpentelemetryConfig(dict):
    def __init__(__self__, *, scope: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterMasterAuth(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_certificate_config: outputs.ClusterMasterAuthClientCertificateConfig,
        client_certificate: Optional[_builtins.str] = ...,
        client_key: Optional[_builtins.str] = ...,
        cluster_ca_certificate: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificateConfig")
    def client_certificate_config(
        self,
    ) -> outputs.ClusterMasterAuthClientCertificateConfig: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterCaCertificate")
    def cluster_ca_certificate(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterMasterAuthClientCertificateConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, issue_client_certificate: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="issueClientCertificate")
    def issue_client_certificate(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterMasterAuthorizedNetworksConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cidr_blocks: Optional[
            Sequence[outputs.ClusterMasterAuthorizedNetworksConfigCidrBlock]
        ] = ...,
        gcp_public_cidrs_access_enabled: Optional[_builtins.bool] = ...,
        private_endpoint_enforcement_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(
        self,
    ) -> Optional[Sequence[outputs.ClusterMasterAuthorizedNetworksConfigCidrBlock]]: ...
    @_builtins.property
    @pulumi.getter(name="gcpPublicCidrsAccessEnabled")
    def gcp_public_cidrs_access_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointEnforcementEnabled")
    def private_endpoint_enforcement_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterMasterAuthorizedNetworksConfigCidrBlock(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cidr_block: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterMeshCertificates(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, enable_certificates: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableCertificates")
    def enable_certificates(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterMonitoringConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        advanced_datapath_observability_config: Optional[
            outputs.ClusterMonitoringConfigAdvancedDatapathObservabilityConfig
        ] = ...,
        enable_components: Optional[Sequence[_builtins.str]] = ...,
        managed_prometheus: Optional[
            outputs.ClusterMonitoringConfigManagedPrometheus
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedDatapathObservabilityConfig")
    def advanced_datapath_observability_config(
        self,
    ) -> Optional[
        outputs.ClusterMonitoringConfigAdvancedDatapathObservabilityConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableComponents")
    def enable_components(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="managedPrometheus")
    def managed_prometheus(
        self,
    ) -> Optional[outputs.ClusterMonitoringConfigManagedPrometheus]: ...

@pulumi.output_type
class ClusterMonitoringConfigAdvancedDatapathObservabilityConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, enable_metrics: _builtins.bool, enable_relay: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableMetrics")
    def enable_metrics(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableRelay")
    def enable_relay(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterMonitoringConfigManagedPrometheus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        auto_monitoring_config: Optional[
            outputs.ClusterMonitoringConfigManagedPrometheusAutoMonitoringConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="autoMonitoringConfig")
    def auto_monitoring_config(
        self,
    ) -> Optional[
        outputs.ClusterMonitoringConfigManagedPrometheusAutoMonitoringConfig
    ]: ...

@pulumi.output_type
class ClusterMonitoringConfigManagedPrometheusAutoMonitoringConfig(dict):
    def __init__(__self__, *, scope: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterNetworkPerformanceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, total_egress_bandwidth_tier: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="totalEgressBandwidthTier")
    def total_egress_bandwidth_tier(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterNetworkPolicy(dict):
    def __init__(
        __self__, *, enabled: _builtins.bool, provider: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        advanced_machine_features: Optional[
            outputs.ClusterNodeConfigAdvancedMachineFeatures
        ] = ...,
        boot_disk: Optional[outputs.ClusterNodeConfigBootDisk] = ...,
        boot_disk_kms_key: Optional[_builtins.str] = ...,
        confidential_nodes: Optional[outputs.ClusterNodeConfigConfidentialNodes] = ...,
        containerd_config: Optional[outputs.ClusterNodeConfigContainerdConfig] = ...,
        disk_size_gb: Optional[_builtins.int] = ...,
        disk_type: Optional[_builtins.str] = ...,
        effective_taints: Optional[
            Sequence[outputs.ClusterNodeConfigEffectiveTaint]
        ] = ...,
        enable_confidential_storage: Optional[_builtins.bool] = ...,
        ephemeral_storage_config: Optional[
            outputs.ClusterNodeConfigEphemeralStorageConfig
        ] = ...,
        ephemeral_storage_local_ssd_config: Optional[
            outputs.ClusterNodeConfigEphemeralStorageLocalSsdConfig
        ] = ...,
        fast_socket: Optional[outputs.ClusterNodeConfigFastSocket] = ...,
        flex_start: Optional[_builtins.bool] = ...,
        gcfs_config: Optional[outputs.ClusterNodeConfigGcfsConfig] = ...,
        guest_accelerators: Optional[
            Sequence[outputs.ClusterNodeConfigGuestAccelerator]
        ] = ...,
        gvnic: Optional[outputs.ClusterNodeConfigGvnic] = ...,
        host_maintenance_policy: Optional[
            outputs.ClusterNodeConfigHostMaintenancePolicy
        ] = ...,
        image_type: Optional[_builtins.str] = ...,
        kubelet_config: Optional[outputs.ClusterNodeConfigKubeletConfig] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        linux_node_config: Optional[outputs.ClusterNodeConfigLinuxNodeConfig] = ...,
        local_nvme_ssd_block_config: Optional[
            outputs.ClusterNodeConfigLocalNvmeSsdBlockConfig
        ] = ...,
        local_ssd_count: Optional[_builtins.int] = ...,
        local_ssd_encryption_mode: Optional[_builtins.str] = ...,
        logging_variant: Optional[_builtins.str] = ...,
        machine_type: Optional[_builtins.str] = ...,
        max_run_duration: Optional[_builtins.str] = ...,
        metadata: Optional[Mapping[str, _builtins.str]] = ...,
        min_cpu_platform: Optional[_builtins.str] = ...,
        node_group: Optional[_builtins.str] = ...,
        oauth_scopes: Optional[Sequence[_builtins.str]] = ...,
        preemptible: Optional[_builtins.bool] = ...,
        reservation_affinity: Optional[
            outputs.ClusterNodeConfigReservationAffinity
        ] = ...,
        resource_labels: Optional[Mapping[str, _builtins.str]] = ...,
        resource_manager_tags: Optional[Mapping[str, _builtins.str]] = ...,
        sandbox_config: Optional[outputs.ClusterNodeConfigSandboxConfig] = ...,
        secondary_boot_disks: Optional[
            Sequence[outputs.ClusterNodeConfigSecondaryBootDisk]
        ] = ...,
        service_account: Optional[_builtins.str] = ...,
        shielded_instance_config: Optional[
            outputs.ClusterNodeConfigShieldedInstanceConfig
        ] = ...,
        sole_tenant_config: Optional[outputs.ClusterNodeConfigSoleTenantConfig] = ...,
        spot: Optional[_builtins.bool] = ...,
        storage_pools: Optional[Sequence[_builtins.str]] = ...,
        tags: Optional[Sequence[_builtins.str]] = ...,
        taints: Optional[Sequence[outputs.ClusterNodeConfigTaint]] = ...,
        windows_node_config: Optional[outputs.ClusterNodeConfigWindowsNodeConfig] = ...,
        workload_metadata_config: Optional[
            outputs.ClusterNodeConfigWorkloadMetadataConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(
        self,
    ) -> Optional[outputs.ClusterNodeConfigAdvancedMachineFeatures]: ...
    @_builtins.property
    @pulumi.getter(name="bootDisk")
    def boot_disk(self) -> Optional[outputs.ClusterNodeConfigBootDisk]: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskKmsKey")
    def boot_disk_kms_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="confidentialNodes")
    def confidential_nodes(
        self,
    ) -> Optional[outputs.ClusterNodeConfigConfidentialNodes]: ...
    @_builtins.property
    @pulumi.getter(name="containerdConfig")
    def containerd_config(
        self,
    ) -> Optional[outputs.ClusterNodeConfigContainerdConfig]: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveTaints")
    def effective_taints(
        self,
    ) -> Optional[Sequence[outputs.ClusterNodeConfigEffectiveTaint]]: ...
    @_builtins.property
    @pulumi.getter(name="enableConfidentialStorage")
    def enable_confidential_storage(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageConfig")
    def ephemeral_storage_config(
        self,
    ) -> Optional[outputs.ClusterNodeConfigEphemeralStorageConfig]: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageLocalSsdConfig")
    def ephemeral_storage_local_ssd_config(
        self,
    ) -> Optional[outputs.ClusterNodeConfigEphemeralStorageLocalSsdConfig]: ...
    @_builtins.property
    @pulumi.getter(name="fastSocket")
    def fast_socket(self) -> Optional[outputs.ClusterNodeConfigFastSocket]: ...
    @_builtins.property
    @pulumi.getter(name="flexStart")
    def flex_start(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="gcfsConfig")
    def gcfs_config(self) -> Optional[outputs.ClusterNodeConfigGcfsConfig]: ...
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(
        self,
    ) -> Optional[Sequence[outputs.ClusterNodeConfigGuestAccelerator]]: ...
    @_builtins.property
    @pulumi.getter
    def gvnic(self) -> Optional[outputs.ClusterNodeConfigGvnic]: ...
    @_builtins.property
    @pulumi.getter(name="hostMaintenancePolicy")
    def host_maintenance_policy(
        self,
    ) -> Optional[outputs.ClusterNodeConfigHostMaintenancePolicy]: ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(self) -> Optional[outputs.ClusterNodeConfigKubeletConfig]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="linuxNodeConfig")
    def linux_node_config(
        self,
    ) -> Optional[outputs.ClusterNodeConfigLinuxNodeConfig]: ...
    @_builtins.property
    @pulumi.getter(name="localNvmeSsdBlockConfig")
    def local_nvme_ssd_block_config(
        self,
    ) -> Optional[outputs.ClusterNodeConfigLocalNvmeSsdBlockConfig]: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="localSsdEncryptionMode")
    def local_ssd_encryption_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loggingVariant")
    def logging_variant(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxRunDuration")
    def max_run_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeGroup")
    def node_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def preemptible(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> Optional[outputs.ClusterNodeConfigReservationAffinity]: ...
    @_builtins.property
    @pulumi.getter(name="resourceLabels")
    def resource_labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sandboxConfig")
    def sandbox_config(self) -> Optional[outputs.ClusterNodeConfigSandboxConfig]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryBootDisks")
    def secondary_boot_disks(
        self,
    ) -> Optional[Sequence[outputs.ClusterNodeConfigSecondaryBootDisk]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[outputs.ClusterNodeConfigShieldedInstanceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="soleTenantConfig")
    def sole_tenant_config(
        self,
    ) -> Optional[outputs.ClusterNodeConfigSoleTenantConfig]: ...
    @_builtins.property
    @pulumi.getter
    def spot(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="storagePools")
    def storage_pools(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def taints(self) -> Optional[Sequence[outputs.ClusterNodeConfigTaint]]: ...
    @_builtins.property
    @pulumi.getter(name="windowsNodeConfig")
    def windows_node_config(
        self,
    ) -> Optional[outputs.ClusterNodeConfigWindowsNodeConfig]: ...
    @_builtins.property
    @pulumi.getter(name="workloadMetadataConfig")
    def workload_metadata_config(
        self,
    ) -> Optional[outputs.ClusterNodeConfigWorkloadMetadataConfig]: ...

@pulumi.output_type
class ClusterNodeConfigAdvancedMachineFeatures(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        threads_per_core: _builtins.int,
        enable_nested_virtualization: Optional[_builtins.bool] = ...,
        performance_monitoring_unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="performanceMonitoringUnit")
    def performance_monitoring_unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigBootDisk(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_type: Optional[_builtins.str] = ...,
        provisioned_iops: Optional[_builtins.int] = ...,
        provisioned_throughput: Optional[_builtins.int] = ...,
        size_gb: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterNodeConfigConfidentialNodes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        confidential_instance_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceType")
    def confidential_instance_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigContainerdConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        private_registry_access_config: Optional[
            outputs.ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfig
        ] = ...,
        registry_hosts: Optional[
            Sequence[outputs.ClusterNodeConfigContainerdConfigRegistryHost]
        ] = ...,
        writable_cgroups: Optional[
            outputs.ClusterNodeConfigContainerdConfigWritableCgroups
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateRegistryAccessConfig")
    def private_registry_access_config(
        self,
    ) -> Optional[
        outputs.ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="registryHosts")
    def registry_hosts(
        self,
    ) -> Optional[Sequence[outputs.ClusterNodeConfigContainerdConfigRegistryHost]]: ...
    @_builtins.property
    @pulumi.getter(name="writableCgroups")
    def writable_cgroups(
        self,
    ) -> Optional[outputs.ClusterNodeConfigContainerdConfigWritableCgroups]: ...

@pulumi.output_type
class ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        certificate_authority_domain_configs: Optional[
            Sequence[
                outputs.ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfig
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityDomainConfigs")
    def certificate_authority_domain_configs(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfig
        ]
    ]: ...

@pulumi.output_type
class ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fqdns: Sequence[_builtins.str],
        gcp_secret_manager_certificate_config: outputs.ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfig,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerCertificateConfig")
    def gcp_secret_manager_certificate_config(
        self,
    ) -> outputs.ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfig: ...

@pulumi.output_type
class ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretUri")
    def secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterNodeConfigContainerdConfigRegistryHost(dict):
    def __init__(
        __self__,
        *,
        server: _builtins.str,
        hosts: Optional[
            Sequence[outputs.ClusterNodeConfigContainerdConfigRegistryHostHost]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hosts(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterNodeConfigContainerdConfigRegistryHostHost]
    ]: ...

@pulumi.output_type
class ClusterNodeConfigContainerdConfigRegistryHostHost(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host: _builtins.str,
        capabilities: Optional[Sequence[_builtins.str]] = ...,
        cas: Optional[
            Sequence[outputs.ClusterNodeConfigContainerdConfigRegistryHostHostCa]
        ] = ...,
        clients: Optional[
            Sequence[outputs.ClusterNodeConfigContainerdConfigRegistryHostHostClient]
        ] = ...,
        dial_timeout: Optional[_builtins.str] = ...,
        headers: Optional[
            Sequence[outputs.ClusterNodeConfigContainerdConfigRegistryHostHostHeader]
        ] = ...,
        override_path: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def cas(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterNodeConfigContainerdConfigRegistryHostHostCa]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def clients(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterNodeConfigContainerdConfigRegistryHostHostClient]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dialTimeout")
    def dial_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterNodeConfigContainerdConfigRegistryHostHostHeader]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="overridePath")
    def override_path(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterNodeConfigContainerdConfigRegistryHostHostCa(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, gcp_secret_manager_secret_uri: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigContainerdConfigRegistryHostHostClient(dict):
    def __init__(
        __self__,
        *,
        cert: outputs.ClusterNodeConfigContainerdConfigRegistryHostHostClientCert,
        key: Optional[
            outputs.ClusterNodeConfigContainerdConfigRegistryHostHostClientKey
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(
        self,
    ) -> outputs.ClusterNodeConfigContainerdConfigRegistryHostHostClientCert: ...
    @_builtins.property
    @pulumi.getter
    def key(
        self,
    ) -> Optional[
        outputs.ClusterNodeConfigContainerdConfigRegistryHostHostClientKey
    ]: ...

@pulumi.output_type
class ClusterNodeConfigContainerdConfigRegistryHostHostClientCert(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, gcp_secret_manager_secret_uri: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigContainerdConfigRegistryHostHostClientKey(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, gcp_secret_manager_secret_uri: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigContainerdConfigRegistryHostHostHeader(dict):
    def __init__(
        __self__, *, key: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigContainerdConfigWritableCgroups(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterNodeConfigEffectiveTaint(dict):
    def __init__(
        __self__,
        *,
        effect: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigEphemeralStorageConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, local_ssd_count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...

@pulumi.output_type
class ClusterNodeConfigEphemeralStorageLocalSsdConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        local_ssd_count: _builtins.int,
        data_cache_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dataCacheCount")
    def data_cache_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterNodeConfigFastSocket(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterNodeConfigGcfsConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterNodeConfigGuestAccelerator(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        count: _builtins.int,
        type: _builtins.str,
        gpu_driver_installation_config: Optional[
            outputs.ClusterNodeConfigGuestAcceleratorGpuDriverInstallationConfig
        ] = ...,
        gpu_partition_size: Optional[_builtins.str] = ...,
        gpu_sharing_config: Optional[
            outputs.ClusterNodeConfigGuestAcceleratorGpuSharingConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverInstallationConfig")
    def gpu_driver_installation_config(
        self,
    ) -> Optional[
        outputs.ClusterNodeConfigGuestAcceleratorGpuDriverInstallationConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="gpuPartitionSize")
    def gpu_partition_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingConfig")
    def gpu_sharing_config(
        self,
    ) -> Optional[outputs.ClusterNodeConfigGuestAcceleratorGpuSharingConfig]: ...

@pulumi.output_type
class ClusterNodeConfigGuestAcceleratorGpuDriverInstallationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, gpu_driver_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverVersion")
    def gpu_driver_version(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterNodeConfigGuestAcceleratorGpuSharingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        gpu_sharing_strategy: _builtins.str,
        max_shared_clients_per_gpu: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingStrategy")
    def gpu_sharing_strategy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxSharedClientsPerGpu")
    def max_shared_clients_per_gpu(self) -> _builtins.int: ...

@pulumi.output_type
class ClusterNodeConfigGvnic(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterNodeConfigHostMaintenancePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, maintenance_interval: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceInterval")
    def maintenance_interval(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterNodeConfigKubeletConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_unsafe_sysctls: Optional[Sequence[_builtins.str]] = ...,
        container_log_max_files: Optional[_builtins.int] = ...,
        container_log_max_size: Optional[_builtins.str] = ...,
        cpu_cfs_quota: Optional[_builtins.bool] = ...,
        cpu_cfs_quota_period: Optional[_builtins.str] = ...,
        cpu_manager_policy: Optional[_builtins.str] = ...,
        eviction_max_pod_grace_period_seconds: Optional[_builtins.int] = ...,
        eviction_minimum_reclaim: Optional[
            outputs.ClusterNodeConfigKubeletConfigEvictionMinimumReclaim
        ] = ...,
        eviction_soft: Optional[
            outputs.ClusterNodeConfigKubeletConfigEvictionSoft
        ] = ...,
        eviction_soft_grace_period: Optional[
            outputs.ClusterNodeConfigKubeletConfigEvictionSoftGracePeriod
        ] = ...,
        image_gc_high_threshold_percent: Optional[_builtins.int] = ...,
        image_gc_low_threshold_percent: Optional[_builtins.int] = ...,
        image_maximum_gc_age: Optional[_builtins.str] = ...,
        image_minimum_gc_age: Optional[_builtins.str] = ...,
        insecure_kubelet_readonly_port_enabled: Optional[_builtins.str] = ...,
        max_parallel_image_pulls: Optional[_builtins.int] = ...,
        memory_manager: Optional[
            outputs.ClusterNodeConfigKubeletConfigMemoryManager
        ] = ...,
        pod_pids_limit: Optional[_builtins.int] = ...,
        single_process_oom_kill: Optional[_builtins.bool] = ...,
        topology_manager: Optional[
            outputs.ClusterNodeConfigKubeletConfigTopologyManager
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedUnsafeSysctls")
    def allowed_unsafe_sysctls(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxFiles")
    def container_log_max_files(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxSize")
    def container_log_max_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuota")
    def cpu_cfs_quota(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuotaPeriod")
    def cpu_cfs_quota_period(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cpuManagerPolicy")
    def cpu_manager_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="evictionMaxPodGracePeriodSeconds")
    def eviction_max_pod_grace_period_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="evictionMinimumReclaim")
    def eviction_minimum_reclaim(
        self,
    ) -> Optional[outputs.ClusterNodeConfigKubeletConfigEvictionMinimumReclaim]: ...
    @_builtins.property
    @pulumi.getter(name="evictionSoft")
    def eviction_soft(
        self,
    ) -> Optional[outputs.ClusterNodeConfigKubeletConfigEvictionSoft]: ...
    @_builtins.property
    @pulumi.getter(name="evictionSoftGracePeriod")
    def eviction_soft_grace_period(
        self,
    ) -> Optional[outputs.ClusterNodeConfigKubeletConfigEvictionSoftGracePeriod]: ...
    @_builtins.property
    @pulumi.getter(name="imageGcHighThresholdPercent")
    def image_gc_high_threshold_percent(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="imageGcLowThresholdPercent")
    def image_gc_low_threshold_percent(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="imageMaximumGcAge")
    def image_maximum_gc_age(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageMinimumGcAge")
    def image_minimum_gc_age(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="insecureKubeletReadonlyPortEnabled")
    def insecure_kubelet_readonly_port_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxParallelImagePulls")
    def max_parallel_image_pulls(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="memoryManager")
    def memory_manager(
        self,
    ) -> Optional[outputs.ClusterNodeConfigKubeletConfigMemoryManager]: ...
    @_builtins.property
    @pulumi.getter(name="podPidsLimit")
    def pod_pids_limit(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="singleProcessOomKill")
    def single_process_oom_kill(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="topologyManager")
    def topology_manager(
        self,
    ) -> Optional[outputs.ClusterNodeConfigKubeletConfigTopologyManager]: ...

@pulumi.output_type
class ClusterNodeConfigKubeletConfigEvictionMinimumReclaim(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[_builtins.str] = ...,
        imagefs_inodes_free: Optional[_builtins.str] = ...,
        memory_available: Optional[_builtins.str] = ...,
        nodefs_available: Optional[_builtins.str] = ...,
        nodefs_inodes_free: Optional[_builtins.str] = ...,
        pid_available: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigKubeletConfigEvictionSoft(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[_builtins.str] = ...,
        imagefs_inodes_free: Optional[_builtins.str] = ...,
        memory_available: Optional[_builtins.str] = ...,
        nodefs_available: Optional[_builtins.str] = ...,
        nodefs_inodes_free: Optional[_builtins.str] = ...,
        pid_available: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigKubeletConfigEvictionSoftGracePeriod(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[_builtins.str] = ...,
        imagefs_inodes_free: Optional[_builtins.str] = ...,
        memory_available: Optional[_builtins.str] = ...,
        nodefs_available: Optional[_builtins.str] = ...,
        nodefs_inodes_free: Optional[_builtins.str] = ...,
        pid_available: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigKubeletConfigMemoryManager(dict):
    def __init__(__self__, *, policy: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigKubeletConfigTopologyManager(dict):
    def __init__(
        __self__,
        *,
        policy: Optional[_builtins.str] = ...,
        scope: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigLinuxNodeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cgroup_mode: Optional[_builtins.str] = ...,
        hugepages_config: Optional[
            outputs.ClusterNodeConfigLinuxNodeConfigHugepagesConfig
        ] = ...,
        node_kernel_module_loading: Optional[
            outputs.ClusterNodeConfigLinuxNodeConfigNodeKernelModuleLoading
        ] = ...,
        sysctls: Optional[Mapping[str, _builtins.str]] = ...,
        transparent_hugepage_defrag: Optional[_builtins.str] = ...,
        transparent_hugepage_enabled: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cgroupMode")
    def cgroup_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hugepagesConfig")
    def hugepages_config(
        self,
    ) -> Optional[outputs.ClusterNodeConfigLinuxNodeConfigHugepagesConfig]: ...
    @_builtins.property
    @pulumi.getter(name="nodeKernelModuleLoading")
    def node_kernel_module_loading(
        self,
    ) -> Optional[outputs.ClusterNodeConfigLinuxNodeConfigNodeKernelModuleLoading]: ...
    @_builtins.property
    @pulumi.getter
    def sysctls(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageDefrag")
    def transparent_hugepage_defrag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageEnabled")
    def transparent_hugepage_enabled(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigLinuxNodeConfigHugepagesConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hugepage_size1g: Optional[_builtins.int] = ...,
        hugepage_size2m: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize1g")
    def hugepage_size1g(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize2m")
    def hugepage_size2m(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterNodeConfigLinuxNodeConfigNodeKernelModuleLoading(dict):
    def __init__(__self__, *, policy: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigLocalNvmeSsdBlockConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, local_ssd_count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...

@pulumi.output_type
class ClusterNodeConfigReservationAffinity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        consume_reservation_type: _builtins.str,
        key: Optional[_builtins.str] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClusterNodeConfigSandboxConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sandbox_type: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sandboxType")
    @_utilities.deprecated(...)
    def sandbox_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigSecondaryBootDisk(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, disk_image: _builtins.str, mode: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskImage")
    def disk_image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigShieldedInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: Optional[_builtins.bool] = ...,
        enable_secure_boot: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterNodeConfigSoleTenantConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        node_affinities: Sequence[
            outputs.ClusterNodeConfigSoleTenantConfigNodeAffinity
        ],
        min_node_cpus: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeAffinities")
    def node_affinities(
        self,
    ) -> Sequence[outputs.ClusterNodeConfigSoleTenantConfigNodeAffinity]: ...
    @_builtins.property
    @pulumi.getter(name="minNodeCpus")
    def min_node_cpus(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterNodeConfigSoleTenantConfigNodeAffinity(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        operator: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigTaint(dict):
    def __init__(
        __self__, *, effect: _builtins.str, key: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterNodeConfigWindowsNodeConfig(dict):
    def __init__(__self__, *, osversion: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def osversion(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodeConfigWorkloadMetadataConfig(dict):
    def __init__(__self__, *, mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterNodePool(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        autoscaling: Optional[outputs.ClusterNodePoolAutoscaling] = ...,
        initial_node_count: Optional[_builtins.int] = ...,
        instance_group_urls: Optional[Sequence[_builtins.str]] = ...,
        managed_instance_group_urls: Optional[Sequence[_builtins.str]] = ...,
        management: Optional[outputs.ClusterNodePoolManagement] = ...,
        max_pods_per_node: Optional[_builtins.int] = ...,
        name: Optional[_builtins.str] = ...,
        name_prefix: Optional[_builtins.str] = ...,
        network_config: Optional[outputs.ClusterNodePoolNetworkConfig] = ...,
        node_config: Optional[outputs.ClusterNodePoolNodeConfig] = ...,
        node_count: Optional[_builtins.int] = ...,
        node_drain_configs: Optional[
            Sequence[outputs.ClusterNodePoolNodeDrainConfig]
        ] = ...,
        node_locations: Optional[Sequence[_builtins.str]] = ...,
        placement_policy: Optional[outputs.ClusterNodePoolPlacementPolicy] = ...,
        queued_provisioning: Optional[outputs.ClusterNodePoolQueuedProvisioning] = ...,
        upgrade_settings: Optional[outputs.ClusterNodePoolUpgradeSettings] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def autoscaling(self) -> Optional[outputs.ClusterNodePoolAutoscaling]: ...
    @_builtins.property
    @pulumi.getter(name="initialNodeCount")
    def initial_node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="instanceGroupUrls")
    def instance_group_urls(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="managedInstanceGroupUrls")
    def managed_instance_group_urls(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def management(self) -> Optional[outputs.ClusterNodePoolManagement]: ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[outputs.ClusterNodePoolNetworkConfig]: ...
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[outputs.ClusterNodePoolNodeConfig]: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="nodeDrainConfigs")
    def node_drain_configs(
        self,
    ) -> Optional[Sequence[outputs.ClusterNodePoolNodeDrainConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeLocations")
    def node_locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="placementPolicy")
    def placement_policy(self) -> Optional[outputs.ClusterNodePoolPlacementPolicy]: ...
    @_builtins.property
    @pulumi.getter(name="queuedProvisioning")
    def queued_provisioning(
        self,
    ) -> Optional[outputs.ClusterNodePoolQueuedProvisioning]: ...
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> Optional[outputs.ClusterNodePoolUpgradeSettings]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolAutoConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        linux_node_config: Optional[
            outputs.ClusterNodePoolAutoConfigLinuxNodeConfig
        ] = ...,
        network_tags: Optional[outputs.ClusterNodePoolAutoConfigNetworkTags] = ...,
        node_kubelet_config: Optional[
            outputs.ClusterNodePoolAutoConfigNodeKubeletConfig
        ] = ...,
        resource_manager_tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linuxNodeConfig")
    def linux_node_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolAutoConfigLinuxNodeConfig]: ...
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(
        self,
    ) -> Optional[outputs.ClusterNodePoolAutoConfigNetworkTags]: ...
    @_builtins.property
    @pulumi.getter(name="nodeKubeletConfig")
    def node_kubelet_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolAutoConfigNodeKubeletConfig]: ...
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ClusterNodePoolAutoConfigLinuxNodeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cgroup_mode: Optional[_builtins.str] = ...,
        node_kernel_module_loading: Optional[
            outputs.ClusterNodePoolAutoConfigLinuxNodeConfigNodeKernelModuleLoading
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cgroupMode")
    def cgroup_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeKernelModuleLoading")
    def node_kernel_module_loading(
        self,
    ) -> Optional[
        outputs.ClusterNodePoolAutoConfigLinuxNodeConfigNodeKernelModuleLoading
    ]: ...

@pulumi.output_type
class ClusterNodePoolAutoConfigLinuxNodeConfigNodeKernelModuleLoading(dict):
    def __init__(__self__, *, policy: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolAutoConfigNetworkTags(dict):
    def __init__(
        __self__, *, tags: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClusterNodePoolAutoConfigNodeKubeletConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        insecure_kubelet_readonly_port_enabled: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="insecureKubeletReadonlyPortEnabled")
    def insecure_kubelet_readonly_port_enabled(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolAutoscaling(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location_policy: Optional[_builtins.str] = ...,
        max_node_count: Optional[_builtins.int] = ...,
        min_node_count: Optional[_builtins.int] = ...,
        total_max_node_count: Optional[_builtins.int] = ...,
        total_min_node_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationPolicy")
    def location_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="totalMaxNodeCount")
    def total_max_node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="totalMinNodeCount")
    def total_min_node_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterNodePoolDefaults(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        node_config_defaults: Optional[
            outputs.ClusterNodePoolDefaultsNodeConfigDefaults
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeConfigDefaults")
    def node_config_defaults(
        self,
    ) -> Optional[outputs.ClusterNodePoolDefaultsNodeConfigDefaults]: ...

@pulumi.output_type
class ClusterNodePoolDefaultsNodeConfigDefaults(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        containerd_config: Optional[
            outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfig
        ] = ...,
        gcfs_config: Optional[
            outputs.ClusterNodePoolDefaultsNodeConfigDefaultsGcfsConfig
        ] = ...,
        insecure_kubelet_readonly_port_enabled: Optional[_builtins.str] = ...,
        logging_variant: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerdConfig")
    def containerd_config(
        self,
    ) -> Optional[
        outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="gcfsConfig")
    def gcfs_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolDefaultsNodeConfigDefaultsGcfsConfig]: ...
    @_builtins.property
    @pulumi.getter(name="insecureKubeletReadonlyPortEnabled")
    def insecure_kubelet_readonly_port_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loggingVariant")
    def logging_variant(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        private_registry_access_config: Optional[
            outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfig
        ] = ...,
        registry_hosts: Optional[
            Sequence[
                outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHost
            ]
        ] = ...,
        writable_cgroups: Optional[
            outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigWritableCgroups
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateRegistryAccessConfig")
    def private_registry_access_config(
        self,
    ) -> Optional[
        outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="registryHosts")
    def registry_hosts(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHost
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="writableCgroups")
    def writable_cgroups(
        self,
    ) -> Optional[
        outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigWritableCgroups
    ]: ...

@pulumi.output_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        certificate_authority_domain_configs: Optional[
            Sequence[
                outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfig
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityDomainConfigs")
    def certificate_authority_domain_configs(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfig
        ]
    ]: ...

@pulumi.output_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fqdns: Sequence[_builtins.str],
        gcp_secret_manager_certificate_config: outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfig,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerCertificateConfig")
    def gcp_secret_manager_certificate_config(
        self,
    ) -> outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfig: ...

@pulumi.output_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretUri")
    def secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHost(dict):
    def __init__(
        __self__,
        *,
        server: _builtins.str,
        hosts: Optional[
            Sequence[
                outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHost
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hosts(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHost
        ]
    ]: ...

@pulumi.output_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHost(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host: _builtins.str,
        capabilities: Optional[Sequence[_builtins.str]] = ...,
        cas: Optional[
            Sequence[
                outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostCa
            ]
        ] = ...,
        clients: Optional[
            Sequence[
                outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClient
            ]
        ] = ...,
        dial_timeout: Optional[_builtins.str] = ...,
        headers: Optional[
            Sequence[
                outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostHeader
            ]
        ] = ...,
        override_path: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def cas(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostCa
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def clients(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClient
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dialTimeout")
    def dial_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostHeader
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="overridePath")
    def override_path(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostCa(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, gcp_secret_manager_secret_uri: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClient(
    dict
):
    def __init__(
        __self__,
        *,
        cert: outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientCert,
        key: Optional[
            outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientKey
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(
        self,
    ) -> outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientCert: ...
    @_builtins.property
    @pulumi.getter
    def key(
        self,
    ) -> Optional[
        outputs.ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientKey
    ]: ...

@pulumi.output_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientCert(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, gcp_secret_manager_secret_uri: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientKey(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, gcp_secret_manager_secret_uri: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostHeader(
    dict
):
    def __init__(
        __self__, *, key: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigWritableCgroups(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterNodePoolDefaultsNodeConfigDefaultsGcfsConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterNodePoolManagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auto_repair: Optional[_builtins.bool] = ...,
        auto_upgrade: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRepair")
    def auto_repair(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="autoUpgrade")
    def auto_upgrade(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterNodePoolNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        accelerator_network_profile: Optional[_builtins.str] = ...,
        additional_node_network_configs: Optional[
            Sequence[outputs.ClusterNodePoolNetworkConfigAdditionalNodeNetworkConfig]
        ] = ...,
        additional_pod_network_configs: Optional[
            Sequence[outputs.ClusterNodePoolNetworkConfigAdditionalPodNetworkConfig]
        ] = ...,
        create_pod_range: Optional[_builtins.bool] = ...,
        enable_private_nodes: Optional[_builtins.bool] = ...,
        network_performance_config: Optional[
            outputs.ClusterNodePoolNetworkConfigNetworkPerformanceConfig
        ] = ...,
        pod_cidr_overprovision_config: Optional[
            outputs.ClusterNodePoolNetworkConfigPodCidrOverprovisionConfig
        ] = ...,
        pod_ipv4_cidr_block: Optional[_builtins.str] = ...,
        pod_range: Optional[_builtins.str] = ...,
        subnetwork: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorNetworkProfile")
    def accelerator_network_profile(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="additionalNodeNetworkConfigs")
    def additional_node_network_configs(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterNodePoolNetworkConfigAdditionalNodeNetworkConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="additionalPodNetworkConfigs")
    def additional_pod_network_configs(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterNodePoolNetworkConfigAdditionalPodNetworkConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="createPodRange")
    def create_pod_range(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateNodes")
    def enable_private_nodes(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfig")
    def network_performance_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolNetworkConfigNetworkPerformanceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="podCidrOverprovisionConfig")
    def pod_cidr_overprovision_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolNetworkConfigPodCidrOverprovisionConfig]: ...
    @_builtins.property
    @pulumi.getter(name="podIpv4CidrBlock")
    def pod_ipv4_cidr_block(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="podRange")
    def pod_range(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNetworkConfigAdditionalNodeNetworkConfig(dict):
    def __init__(
        __self__,
        *,
        network: Optional[_builtins.str] = ...,
        subnetwork: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNetworkConfigAdditionalPodNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_pods_per_node: Optional[_builtins.int] = ...,
        secondary_pod_range: Optional[_builtins.str] = ...,
        subnetwork: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryPodRange")
    def secondary_pod_range(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNetworkConfigNetworkPerformanceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, total_egress_bandwidth_tier: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="totalEgressBandwidthTier")
    def total_egress_bandwidth_tier(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterNodePoolNetworkConfigPodCidrOverprovisionConfig(dict):
    def __init__(__self__, *, disabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterNodePoolNodeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        advanced_machine_features: Optional[
            outputs.ClusterNodePoolNodeConfigAdvancedMachineFeatures
        ] = ...,
        boot_disk: Optional[outputs.ClusterNodePoolNodeConfigBootDisk] = ...,
        boot_disk_kms_key: Optional[_builtins.str] = ...,
        confidential_nodes: Optional[
            outputs.ClusterNodePoolNodeConfigConfidentialNodes
        ] = ...,
        containerd_config: Optional[
            outputs.ClusterNodePoolNodeConfigContainerdConfig
        ] = ...,
        disk_size_gb: Optional[_builtins.int] = ...,
        disk_type: Optional[_builtins.str] = ...,
        effective_taints: Optional[
            Sequence[outputs.ClusterNodePoolNodeConfigEffectiveTaint]
        ] = ...,
        enable_confidential_storage: Optional[_builtins.bool] = ...,
        ephemeral_storage_config: Optional[
            outputs.ClusterNodePoolNodeConfigEphemeralStorageConfig
        ] = ...,
        ephemeral_storage_local_ssd_config: Optional[
            outputs.ClusterNodePoolNodeConfigEphemeralStorageLocalSsdConfig
        ] = ...,
        fast_socket: Optional[outputs.ClusterNodePoolNodeConfigFastSocket] = ...,
        flex_start: Optional[_builtins.bool] = ...,
        gcfs_config: Optional[outputs.ClusterNodePoolNodeConfigGcfsConfig] = ...,
        guest_accelerators: Optional[
            Sequence[outputs.ClusterNodePoolNodeConfigGuestAccelerator]
        ] = ...,
        gvnic: Optional[outputs.ClusterNodePoolNodeConfigGvnic] = ...,
        host_maintenance_policy: Optional[
            outputs.ClusterNodePoolNodeConfigHostMaintenancePolicy
        ] = ...,
        image_type: Optional[_builtins.str] = ...,
        kubelet_config: Optional[outputs.ClusterNodePoolNodeConfigKubeletConfig] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        linux_node_config: Optional[
            outputs.ClusterNodePoolNodeConfigLinuxNodeConfig
        ] = ...,
        local_nvme_ssd_block_config: Optional[
            outputs.ClusterNodePoolNodeConfigLocalNvmeSsdBlockConfig
        ] = ...,
        local_ssd_count: Optional[_builtins.int] = ...,
        local_ssd_encryption_mode: Optional[_builtins.str] = ...,
        logging_variant: Optional[_builtins.str] = ...,
        machine_type: Optional[_builtins.str] = ...,
        max_run_duration: Optional[_builtins.str] = ...,
        metadata: Optional[Mapping[str, _builtins.str]] = ...,
        min_cpu_platform: Optional[_builtins.str] = ...,
        node_group: Optional[_builtins.str] = ...,
        oauth_scopes: Optional[Sequence[_builtins.str]] = ...,
        preemptible: Optional[_builtins.bool] = ...,
        reservation_affinity: Optional[
            outputs.ClusterNodePoolNodeConfigReservationAffinity
        ] = ...,
        resource_labels: Optional[Mapping[str, _builtins.str]] = ...,
        resource_manager_tags: Optional[Mapping[str, _builtins.str]] = ...,
        sandbox_config: Optional[outputs.ClusterNodePoolNodeConfigSandboxConfig] = ...,
        secondary_boot_disks: Optional[
            Sequence[outputs.ClusterNodePoolNodeConfigSecondaryBootDisk]
        ] = ...,
        service_account: Optional[_builtins.str] = ...,
        shielded_instance_config: Optional[
            outputs.ClusterNodePoolNodeConfigShieldedInstanceConfig
        ] = ...,
        sole_tenant_config: Optional[
            outputs.ClusterNodePoolNodeConfigSoleTenantConfig
        ] = ...,
        spot: Optional[_builtins.bool] = ...,
        storage_pools: Optional[Sequence[_builtins.str]] = ...,
        tags: Optional[Sequence[_builtins.str]] = ...,
        taints: Optional[Sequence[outputs.ClusterNodePoolNodeConfigTaint]] = ...,
        windows_node_config: Optional[
            outputs.ClusterNodePoolNodeConfigWindowsNodeConfig
        ] = ...,
        workload_metadata_config: Optional[
            outputs.ClusterNodePoolNodeConfigWorkloadMetadataConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigAdvancedMachineFeatures]: ...
    @_builtins.property
    @pulumi.getter(name="bootDisk")
    def boot_disk(self) -> Optional[outputs.ClusterNodePoolNodeConfigBootDisk]: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskKmsKey")
    def boot_disk_kms_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="confidentialNodes")
    def confidential_nodes(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigConfidentialNodes]: ...
    @_builtins.property
    @pulumi.getter(name="containerdConfig")
    def containerd_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigContainerdConfig]: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveTaints")
    def effective_taints(
        self,
    ) -> Optional[Sequence[outputs.ClusterNodePoolNodeConfigEffectiveTaint]]: ...
    @_builtins.property
    @pulumi.getter(name="enableConfidentialStorage")
    def enable_confidential_storage(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageConfig")
    def ephemeral_storage_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigEphemeralStorageConfig]: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageLocalSsdConfig")
    def ephemeral_storage_local_ssd_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigEphemeralStorageLocalSsdConfig]: ...
    @_builtins.property
    @pulumi.getter(name="fastSocket")
    def fast_socket(self) -> Optional[outputs.ClusterNodePoolNodeConfigFastSocket]: ...
    @_builtins.property
    @pulumi.getter(name="flexStart")
    def flex_start(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="gcfsConfig")
    def gcfs_config(self) -> Optional[outputs.ClusterNodePoolNodeConfigGcfsConfig]: ...
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(
        self,
    ) -> Optional[Sequence[outputs.ClusterNodePoolNodeConfigGuestAccelerator]]: ...
    @_builtins.property
    @pulumi.getter
    def gvnic(self) -> Optional[outputs.ClusterNodePoolNodeConfigGvnic]: ...
    @_builtins.property
    @pulumi.getter(name="hostMaintenancePolicy")
    def host_maintenance_policy(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigHostMaintenancePolicy]: ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigKubeletConfig]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="linuxNodeConfig")
    def linux_node_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigLinuxNodeConfig]: ...
    @_builtins.property
    @pulumi.getter(name="localNvmeSsdBlockConfig")
    def local_nvme_ssd_block_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigLocalNvmeSsdBlockConfig]: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="localSsdEncryptionMode")
    def local_ssd_encryption_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loggingVariant")
    def logging_variant(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxRunDuration")
    def max_run_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeGroup")
    def node_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def preemptible(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigReservationAffinity]: ...
    @_builtins.property
    @pulumi.getter(name="resourceLabels")
    def resource_labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sandboxConfig")
    def sandbox_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigSandboxConfig]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryBootDisks")
    def secondary_boot_disks(
        self,
    ) -> Optional[Sequence[outputs.ClusterNodePoolNodeConfigSecondaryBootDisk]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigShieldedInstanceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="soleTenantConfig")
    def sole_tenant_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigSoleTenantConfig]: ...
    @_builtins.property
    @pulumi.getter
    def spot(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="storagePools")
    def storage_pools(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def taints(self) -> Optional[Sequence[outputs.ClusterNodePoolNodeConfigTaint]]: ...
    @_builtins.property
    @pulumi.getter(name="windowsNodeConfig")
    def windows_node_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigWindowsNodeConfig]: ...
    @_builtins.property
    @pulumi.getter(name="workloadMetadataConfig")
    def workload_metadata_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigWorkloadMetadataConfig]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigAdvancedMachineFeatures(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        threads_per_core: _builtins.int,
        enable_nested_virtualization: Optional[_builtins.bool] = ...,
        performance_monitoring_unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="performanceMonitoringUnit")
    def performance_monitoring_unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigBootDisk(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_type: Optional[_builtins.str] = ...,
        provisioned_iops: Optional[_builtins.int] = ...,
        provisioned_throughput: Optional[_builtins.int] = ...,
        size_gb: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigConfidentialNodes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        confidential_instance_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceType")
    def confidential_instance_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigContainerdConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        private_registry_access_config: Optional[
            outputs.ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfig
        ] = ...,
        registry_hosts: Optional[
            Sequence[outputs.ClusterNodePoolNodeConfigContainerdConfigRegistryHost]
        ] = ...,
        writable_cgroups: Optional[
            outputs.ClusterNodePoolNodeConfigContainerdConfigWritableCgroups
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateRegistryAccessConfig")
    def private_registry_access_config(
        self,
    ) -> Optional[
        outputs.ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="registryHosts")
    def registry_hosts(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterNodePoolNodeConfigContainerdConfigRegistryHost]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="writableCgroups")
    def writable_cgroups(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigContainerdConfigWritableCgroups]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        certificate_authority_domain_configs: Optional[
            Sequence[
                outputs.ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfig
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityDomainConfigs")
    def certificate_authority_domain_configs(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfig
        ]
    ]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fqdns: Sequence[_builtins.str],
        gcp_secret_manager_certificate_config: outputs.ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfig,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerCertificateConfig")
    def gcp_secret_manager_certificate_config(
        self,
    ) -> outputs.ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfig: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretUri")
    def secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigContainerdConfigRegistryHost(dict):
    def __init__(
        __self__,
        *,
        server: _builtins.str,
        hosts: Optional[
            Sequence[outputs.ClusterNodePoolNodeConfigContainerdConfigRegistryHostHost]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hosts(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterNodePoolNodeConfigContainerdConfigRegistryHostHost]
    ]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHost(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host: _builtins.str,
        capabilities: Optional[Sequence[_builtins.str]] = ...,
        cas: Optional[
            Sequence[
                outputs.ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostCa
            ]
        ] = ...,
        clients: Optional[
            Sequence[
                outputs.ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClient
            ]
        ] = ...,
        dial_timeout: Optional[_builtins.str] = ...,
        headers: Optional[
            Sequence[
                outputs.ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostHeader
            ]
        ] = ...,
        override_path: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def cas(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostCa]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def clients(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClient
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dialTimeout")
    def dial_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostHeader
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="overridePath")
    def override_path(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostCa(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, gcp_secret_manager_secret_uri: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClient(dict):
    def __init__(
        __self__,
        *,
        cert: outputs.ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientCert,
        key: Optional[
            outputs.ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientKey
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(
        self,
    ) -> (
        outputs.ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientCert
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(
        self,
    ) -> Optional[
        outputs.ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientKey
    ]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientCert(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, gcp_secret_manager_secret_uri: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientKey(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, gcp_secret_manager_secret_uri: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostHeader(dict):
    def __init__(
        __self__, *, key: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigContainerdConfigWritableCgroups(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigEffectiveTaint(dict):
    def __init__(
        __self__,
        *,
        effect: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigEphemeralStorageConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, local_ssd_count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigEphemeralStorageLocalSsdConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        local_ssd_count: _builtins.int,
        data_cache_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dataCacheCount")
    def data_cache_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigFastSocket(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigGcfsConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigGuestAccelerator(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        count: _builtins.int,
        type: _builtins.str,
        gpu_driver_installation_config: Optional[
            outputs.ClusterNodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfig
        ] = ...,
        gpu_partition_size: Optional[_builtins.str] = ...,
        gpu_sharing_config: Optional[
            outputs.ClusterNodePoolNodeConfigGuestAcceleratorGpuSharingConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverInstallationConfig")
    def gpu_driver_installation_config(
        self,
    ) -> Optional[
        outputs.ClusterNodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="gpuPartitionSize")
    def gpu_partition_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingConfig")
    def gpu_sharing_config(
        self,
    ) -> Optional[
        outputs.ClusterNodePoolNodeConfigGuestAcceleratorGpuSharingConfig
    ]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, gpu_driver_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverVersion")
    def gpu_driver_version(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigGuestAcceleratorGpuSharingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        gpu_sharing_strategy: _builtins.str,
        max_shared_clients_per_gpu: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingStrategy")
    def gpu_sharing_strategy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxSharedClientsPerGpu")
    def max_shared_clients_per_gpu(self) -> _builtins.int: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigGvnic(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigHostMaintenancePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, maintenance_interval: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceInterval")
    def maintenance_interval(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigKubeletConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_unsafe_sysctls: Optional[Sequence[_builtins.str]] = ...,
        container_log_max_files: Optional[_builtins.int] = ...,
        container_log_max_size: Optional[_builtins.str] = ...,
        cpu_cfs_quota: Optional[_builtins.bool] = ...,
        cpu_cfs_quota_period: Optional[_builtins.str] = ...,
        cpu_manager_policy: Optional[_builtins.str] = ...,
        eviction_max_pod_grace_period_seconds: Optional[_builtins.int] = ...,
        eviction_minimum_reclaim: Optional[
            outputs.ClusterNodePoolNodeConfigKubeletConfigEvictionMinimumReclaim
        ] = ...,
        eviction_soft: Optional[
            outputs.ClusterNodePoolNodeConfigKubeletConfigEvictionSoft
        ] = ...,
        eviction_soft_grace_period: Optional[
            outputs.ClusterNodePoolNodeConfigKubeletConfigEvictionSoftGracePeriod
        ] = ...,
        image_gc_high_threshold_percent: Optional[_builtins.int] = ...,
        image_gc_low_threshold_percent: Optional[_builtins.int] = ...,
        image_maximum_gc_age: Optional[_builtins.str] = ...,
        image_minimum_gc_age: Optional[_builtins.str] = ...,
        insecure_kubelet_readonly_port_enabled: Optional[_builtins.str] = ...,
        max_parallel_image_pulls: Optional[_builtins.int] = ...,
        memory_manager: Optional[
            outputs.ClusterNodePoolNodeConfigKubeletConfigMemoryManager
        ] = ...,
        pod_pids_limit: Optional[_builtins.int] = ...,
        single_process_oom_kill: Optional[_builtins.bool] = ...,
        topology_manager: Optional[
            outputs.ClusterNodePoolNodeConfigKubeletConfigTopologyManager
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedUnsafeSysctls")
    def allowed_unsafe_sysctls(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxFiles")
    def container_log_max_files(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxSize")
    def container_log_max_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuota")
    def cpu_cfs_quota(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuotaPeriod")
    def cpu_cfs_quota_period(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cpuManagerPolicy")
    def cpu_manager_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="evictionMaxPodGracePeriodSeconds")
    def eviction_max_pod_grace_period_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="evictionMinimumReclaim")
    def eviction_minimum_reclaim(
        self,
    ) -> Optional[
        outputs.ClusterNodePoolNodeConfigKubeletConfigEvictionMinimumReclaim
    ]: ...
    @_builtins.property
    @pulumi.getter(name="evictionSoft")
    def eviction_soft(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigKubeletConfigEvictionSoft]: ...
    @_builtins.property
    @pulumi.getter(name="evictionSoftGracePeriod")
    def eviction_soft_grace_period(
        self,
    ) -> Optional[
        outputs.ClusterNodePoolNodeConfigKubeletConfigEvictionSoftGracePeriod
    ]: ...
    @_builtins.property
    @pulumi.getter(name="imageGcHighThresholdPercent")
    def image_gc_high_threshold_percent(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="imageGcLowThresholdPercent")
    def image_gc_low_threshold_percent(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="imageMaximumGcAge")
    def image_maximum_gc_age(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageMinimumGcAge")
    def image_minimum_gc_age(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="insecureKubeletReadonlyPortEnabled")
    def insecure_kubelet_readonly_port_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxParallelImagePulls")
    def max_parallel_image_pulls(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="memoryManager")
    def memory_manager(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigKubeletConfigMemoryManager]: ...
    @_builtins.property
    @pulumi.getter(name="podPidsLimit")
    def pod_pids_limit(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="singleProcessOomKill")
    def single_process_oom_kill(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="topologyManager")
    def topology_manager(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigKubeletConfigTopologyManager]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigKubeletConfigEvictionMinimumReclaim(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[_builtins.str] = ...,
        imagefs_inodes_free: Optional[_builtins.str] = ...,
        memory_available: Optional[_builtins.str] = ...,
        nodefs_available: Optional[_builtins.str] = ...,
        nodefs_inodes_free: Optional[_builtins.str] = ...,
        pid_available: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigKubeletConfigEvictionSoft(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[_builtins.str] = ...,
        imagefs_inodes_free: Optional[_builtins.str] = ...,
        memory_available: Optional[_builtins.str] = ...,
        nodefs_available: Optional[_builtins.str] = ...,
        nodefs_inodes_free: Optional[_builtins.str] = ...,
        pid_available: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigKubeletConfigEvictionSoftGracePeriod(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[_builtins.str] = ...,
        imagefs_inodes_free: Optional[_builtins.str] = ...,
        memory_available: Optional[_builtins.str] = ...,
        nodefs_available: Optional[_builtins.str] = ...,
        nodefs_inodes_free: Optional[_builtins.str] = ...,
        pid_available: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigKubeletConfigMemoryManager(dict):
    def __init__(__self__, *, policy: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigKubeletConfigTopologyManager(dict):
    def __init__(
        __self__,
        *,
        policy: Optional[_builtins.str] = ...,
        scope: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigLinuxNodeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cgroup_mode: Optional[_builtins.str] = ...,
        hugepages_config: Optional[
            outputs.ClusterNodePoolNodeConfigLinuxNodeConfigHugepagesConfig
        ] = ...,
        node_kernel_module_loading: Optional[
            outputs.ClusterNodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoading
        ] = ...,
        sysctls: Optional[Mapping[str, _builtins.str]] = ...,
        transparent_hugepage_defrag: Optional[_builtins.str] = ...,
        transparent_hugepage_enabled: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cgroupMode")
    def cgroup_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hugepagesConfig")
    def hugepages_config(
        self,
    ) -> Optional[outputs.ClusterNodePoolNodeConfigLinuxNodeConfigHugepagesConfig]: ...
    @_builtins.property
    @pulumi.getter(name="nodeKernelModuleLoading")
    def node_kernel_module_loading(
        self,
    ) -> Optional[
        outputs.ClusterNodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoading
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sysctls(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageDefrag")
    def transparent_hugepage_defrag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageEnabled")
    def transparent_hugepage_enabled(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigLinuxNodeConfigHugepagesConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hugepage_size1g: Optional[_builtins.int] = ...,
        hugepage_size2m: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize1g")
    def hugepage_size1g(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize2m")
    def hugepage_size2m(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoading(dict):
    def __init__(__self__, *, policy: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigLocalNvmeSsdBlockConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, local_ssd_count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigReservationAffinity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        consume_reservation_type: _builtins.str,
        key: Optional[_builtins.str] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigSandboxConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sandbox_type: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sandboxType")
    @_utilities.deprecated(...)
    def sandbox_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigSecondaryBootDisk(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, disk_image: _builtins.str, mode: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskImage")
    def disk_image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigShieldedInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: Optional[_builtins.bool] = ...,
        enable_secure_boot: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigSoleTenantConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        node_affinities: Sequence[
            outputs.ClusterNodePoolNodeConfigSoleTenantConfigNodeAffinity
        ],
        min_node_cpus: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeAffinities")
    def node_affinities(
        self,
    ) -> Sequence[outputs.ClusterNodePoolNodeConfigSoleTenantConfigNodeAffinity]: ...
    @_builtins.property
    @pulumi.getter(name="minNodeCpus")
    def min_node_cpus(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigSoleTenantConfigNodeAffinity(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        operator: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigTaint(dict):
    def __init__(
        __self__, *, effect: _builtins.str, key: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigWindowsNodeConfig(dict):
    def __init__(__self__, *, osversion: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def osversion(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolNodeConfigWorkloadMetadataConfig(dict):
    def __init__(__self__, *, mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterNodePoolNodeDrainConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        respect_pdb_during_node_pool_deletion: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="respectPdbDuringNodePoolDeletion")
    def respect_pdb_during_node_pool_deletion(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterNodePoolPlacementPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        policy_name: Optional[_builtins.str] = ...,
        tpu_topology: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tpuTopology")
    def tpu_topology(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolQueuedProvisioning(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterNodePoolUpgradeSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        blue_green_settings: Optional[
            outputs.ClusterNodePoolUpgradeSettingsBlueGreenSettings
        ] = ...,
        max_surge: Optional[_builtins.int] = ...,
        max_unavailable: Optional[_builtins.int] = ...,
        strategy: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blueGreenSettings")
    def blue_green_settings(
        self,
    ) -> Optional[outputs.ClusterNodePoolUpgradeSettingsBlueGreenSettings]: ...
    @_builtins.property
    @pulumi.getter(name="maxSurge")
    def max_surge(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxUnavailable")
    def max_unavailable(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def strategy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolUpgradeSettingsBlueGreenSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        autoscaled_rollout_policy: Optional[
            outputs.ClusterNodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicy
        ] = ...,
        node_pool_soak_duration: Optional[_builtins.str] = ...,
        standard_rollout_policy: Optional[
            outputs.ClusterNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscaledRolloutPolicy")
    def autoscaled_rollout_policy(
        self,
    ) -> Optional[
        outputs.ClusterNodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicy
    ]: ...
    @_builtins.property
    @pulumi.getter(name="nodePoolSoakDuration")
    def node_pool_soak_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="standardRolloutPolicy")
    def standard_rollout_policy(
        self,
    ) -> Optional[
        outputs.ClusterNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy
    ]: ...

@pulumi.output_type
class ClusterNodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, wait_for_drain_duration: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="waitForDrainDuration")
    def wait_for_drain_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        batch_node_count: Optional[_builtins.int] = ...,
        batch_percentage: Optional[_builtins.float] = ...,
        batch_soak_duration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchNodeCount")
    def batch_node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="batchPercentage")
    def batch_percentage(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="batchSoakDuration")
    def batch_soak_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNotificationConfig(dict):
    def __init__(
        __self__, *, pubsub: outputs.ClusterNotificationConfigPubsub
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pubsub(self) -> outputs.ClusterNotificationConfigPubsub: ...

@pulumi.output_type
class ClusterNotificationConfigPubsub(dict):
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        filter: Optional[outputs.ClusterNotificationConfigPubsubFilter] = ...,
        topic: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[outputs.ClusterNotificationConfigPubsubFilter]: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNotificationConfigPubsubFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, event_types: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventTypes")
    def event_types(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ClusterPodAutoscaling(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, hpa_profile: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hpaProfile")
    def hpa_profile(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterPodSecurityPolicyConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterPrivateClusterConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_private_endpoint: Optional[_builtins.bool] = ...,
        enable_private_nodes: Optional[_builtins.bool] = ...,
        master_global_access_config: Optional[
            outputs.ClusterPrivateClusterConfigMasterGlobalAccessConfig
        ] = ...,
        master_ipv4_cidr_block: Optional[_builtins.str] = ...,
        peering_name: Optional[_builtins.str] = ...,
        private_endpoint: Optional[_builtins.str] = ...,
        private_endpoint_subnetwork: Optional[_builtins.str] = ...,
        public_endpoint: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateEndpoint")
    def enable_private_endpoint(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateNodes")
    def enable_private_nodes(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="masterGlobalAccessConfig")
    def master_global_access_config(
        self,
    ) -> Optional[outputs.ClusterPrivateClusterConfigMasterGlobalAccessConfig]: ...
    @_builtins.property
    @pulumi.getter(name="masterIpv4CidrBlock")
    def master_ipv4_cidr_block(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peeringName")
    def peering_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointSubnetwork")
    def private_endpoint_subnetwork(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicEndpoint")
    def public_endpoint(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterPrivateClusterConfigMasterGlobalAccessConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterProtectConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        workload_config: Optional[outputs.ClusterProtectConfigWorkloadConfig] = ...,
        workload_vulnerability_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workloadConfig")
    def workload_config(
        self,
    ) -> Optional[outputs.ClusterProtectConfigWorkloadConfig]: ...
    @_builtins.property
    @pulumi.getter(name="workloadVulnerabilityMode")
    def workload_vulnerability_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterProtectConfigWorkloadConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, audit_mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditMode")
    def audit_mode(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterRbacBindingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_insecure_binding_system_authenticated: Optional[_builtins.bool] = ...,
        enable_insecure_binding_system_unauthenticated: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableInsecureBindingSystemAuthenticated")
    def enable_insecure_binding_system_authenticated(
        self,
    ) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableInsecureBindingSystemUnauthenticated")
    def enable_insecure_binding_system_unauthenticated(
        self,
    ) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterReleaseChannel(dict):
    def __init__(__self__, *, channel: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterResourceUsageExportConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bigquery_destination: outputs.ClusterResourceUsageExportConfigBigqueryDestination,
        enable_network_egress_metering: Optional[_builtins.bool] = ...,
        enable_resource_consumption_metering: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryDestination")
    def bigquery_destination(
        self,
    ) -> outputs.ClusterResourceUsageExportConfigBigqueryDestination: ...
    @_builtins.property
    @pulumi.getter(name="enableNetworkEgressMetering")
    def enable_network_egress_metering(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableResourceConsumptionMetering")
    def enable_resource_consumption_metering(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterResourceUsageExportConfigBigqueryDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, dataset_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterSecretManagerConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        rotation_config: Optional[
            outputs.ClusterSecretManagerConfigRotationConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="rotationConfig")
    def rotation_config(
        self,
    ) -> Optional[outputs.ClusterSecretManagerConfigRotationConfig]: ...

@pulumi.output_type
class ClusterSecretManagerConfigRotationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        rotation_interval: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="rotationInterval")
    def rotation_interval(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterSecretSyncConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        rotation_config: Optional[outputs.ClusterSecretSyncConfigRotationConfig] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="rotationConfig")
    def rotation_config(
        self,
    ) -> Optional[outputs.ClusterSecretSyncConfigRotationConfig]: ...

@pulumi.output_type
class ClusterSecretSyncConfigRotationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        rotation_interval: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="rotationInterval")
    def rotation_interval(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterSecurityPostureConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mode: Optional[_builtins.str] = ...,
        vulnerability_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vulnerabilityMode")
    def vulnerability_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterServiceExternalIpsConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterTpuConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        ipv4_cidr_block: Optional[_builtins.str] = ...,
        use_service_networking: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ipv4CidrBlock")
    def ipv4_cidr_block(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useServiceNetworking")
    def use_service_networking(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterUserManagedKeysConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aggregation_ca: Optional[_builtins.str] = ...,
        cluster_ca: Optional[_builtins.str] = ...,
        control_plane_disk_encryption_key: Optional[_builtins.str] = ...,
        control_plane_disk_encryption_key_versions: Optional[
            Sequence[_builtins.str]
        ] = ...,
        etcd_api_ca: Optional[_builtins.str] = ...,
        etcd_peer_ca: Optional[_builtins.str] = ...,
        gkeops_etcd_backup_encryption_key: Optional[_builtins.str] = ...,
        service_account_signing_keys: Optional[Sequence[_builtins.str]] = ...,
        service_account_verification_keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aggregationCa")
    def aggregation_ca(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterCa")
    def cluster_ca(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneDiskEncryptionKey")
    def control_plane_disk_encryption_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneDiskEncryptionKeyVersions")
    def control_plane_disk_encryption_key_versions(
        self,
    ) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="etcdApiCa")
    def etcd_api_ca(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="etcdPeerCa")
    def etcd_peer_ca(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gkeopsEtcdBackupEncryptionKey")
    def gkeops_etcd_backup_encryption_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountSigningKeys")
    def service_account_signing_keys(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountVerificationKeys")
    def service_account_verification_keys(
        self,
    ) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClusterVerticalPodAutoscaling(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterWorkloadAltsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, enable_alts: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableAlts")
    def enable_alts(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterWorkloadIdentityConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, workload_pool: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workloadPool")
    def workload_pool(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolAutoscaling(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location_policy: Optional[_builtins.str] = ...,
        max_node_count: Optional[_builtins.int] = ...,
        min_node_count: Optional[_builtins.int] = ...,
        total_max_node_count: Optional[_builtins.int] = ...,
        total_min_node_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationPolicy")
    def location_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="totalMaxNodeCount")
    def total_max_node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="totalMinNodeCount")
    def total_min_node_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class NodePoolManagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auto_repair: Optional[_builtins.bool] = ...,
        auto_upgrade: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRepair")
    def auto_repair(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="autoUpgrade")
    def auto_upgrade(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class NodePoolNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        accelerator_network_profile: Optional[_builtins.str] = ...,
        additional_node_network_configs: Optional[
            Sequence[outputs.NodePoolNetworkConfigAdditionalNodeNetworkConfig]
        ] = ...,
        additional_pod_network_configs: Optional[
            Sequence[outputs.NodePoolNetworkConfigAdditionalPodNetworkConfig]
        ] = ...,
        create_pod_range: Optional[_builtins.bool] = ...,
        enable_private_nodes: Optional[_builtins.bool] = ...,
        network_performance_config: Optional[
            outputs.NodePoolNetworkConfigNetworkPerformanceConfig
        ] = ...,
        pod_cidr_overprovision_config: Optional[
            outputs.NodePoolNetworkConfigPodCidrOverprovisionConfig
        ] = ...,
        pod_ipv4_cidr_block: Optional[_builtins.str] = ...,
        pod_range: Optional[_builtins.str] = ...,
        subnetwork: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorNetworkProfile")
    def accelerator_network_profile(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="additionalNodeNetworkConfigs")
    def additional_node_network_configs(
        self,
    ) -> Optional[
        Sequence[outputs.NodePoolNetworkConfigAdditionalNodeNetworkConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="additionalPodNetworkConfigs")
    def additional_pod_network_configs(
        self,
    ) -> Optional[
        Sequence[outputs.NodePoolNetworkConfigAdditionalPodNetworkConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="createPodRange")
    def create_pod_range(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateNodes")
    def enable_private_nodes(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfig")
    def network_performance_config(
        self,
    ) -> Optional[outputs.NodePoolNetworkConfigNetworkPerformanceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="podCidrOverprovisionConfig")
    def pod_cidr_overprovision_config(
        self,
    ) -> Optional[outputs.NodePoolNetworkConfigPodCidrOverprovisionConfig]: ...
    @_builtins.property
    @pulumi.getter(name="podIpv4CidrBlock")
    def pod_ipv4_cidr_block(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="podRange")
    def pod_range(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNetworkConfigAdditionalNodeNetworkConfig(dict):
    def __init__(
        __self__,
        *,
        network: Optional[_builtins.str] = ...,
        subnetwork: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNetworkConfigAdditionalPodNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_pods_per_node: Optional[_builtins.int] = ...,
        secondary_pod_range: Optional[_builtins.str] = ...,
        subnetwork: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryPodRange")
    def secondary_pod_range(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNetworkConfigNetworkPerformanceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, total_egress_bandwidth_tier: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="totalEgressBandwidthTier")
    def total_egress_bandwidth_tier(self) -> _builtins.str: ...

@pulumi.output_type
class NodePoolNetworkConfigPodCidrOverprovisionConfig(dict):
    def __init__(__self__, *, disabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...

@pulumi.output_type
class NodePoolNodeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        advanced_machine_features: Optional[
            outputs.NodePoolNodeConfigAdvancedMachineFeatures
        ] = ...,
        boot_disk: Optional[outputs.NodePoolNodeConfigBootDisk] = ...,
        boot_disk_kms_key: Optional[_builtins.str] = ...,
        confidential_nodes: Optional[outputs.NodePoolNodeConfigConfidentialNodes] = ...,
        containerd_config: Optional[outputs.NodePoolNodeConfigContainerdConfig] = ...,
        disk_size_gb: Optional[_builtins.int] = ...,
        disk_type: Optional[_builtins.str] = ...,
        effective_taints: Optional[
            Sequence[outputs.NodePoolNodeConfigEffectiveTaint]
        ] = ...,
        enable_confidential_storage: Optional[_builtins.bool] = ...,
        ephemeral_storage_config: Optional[
            outputs.NodePoolNodeConfigEphemeralStorageConfig
        ] = ...,
        ephemeral_storage_local_ssd_config: Optional[
            outputs.NodePoolNodeConfigEphemeralStorageLocalSsdConfig
        ] = ...,
        fast_socket: Optional[outputs.NodePoolNodeConfigFastSocket] = ...,
        flex_start: Optional[_builtins.bool] = ...,
        gcfs_config: Optional[outputs.NodePoolNodeConfigGcfsConfig] = ...,
        guest_accelerators: Optional[
            Sequence[outputs.NodePoolNodeConfigGuestAccelerator]
        ] = ...,
        gvnic: Optional[outputs.NodePoolNodeConfigGvnic] = ...,
        host_maintenance_policy: Optional[
            outputs.NodePoolNodeConfigHostMaintenancePolicy
        ] = ...,
        image_type: Optional[_builtins.str] = ...,
        kubelet_config: Optional[outputs.NodePoolNodeConfigKubeletConfig] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        linux_node_config: Optional[outputs.NodePoolNodeConfigLinuxNodeConfig] = ...,
        local_nvme_ssd_block_config: Optional[
            outputs.NodePoolNodeConfigLocalNvmeSsdBlockConfig
        ] = ...,
        local_ssd_count: Optional[_builtins.int] = ...,
        local_ssd_encryption_mode: Optional[_builtins.str] = ...,
        logging_variant: Optional[_builtins.str] = ...,
        machine_type: Optional[_builtins.str] = ...,
        max_run_duration: Optional[_builtins.str] = ...,
        metadata: Optional[Mapping[str, _builtins.str]] = ...,
        min_cpu_platform: Optional[_builtins.str] = ...,
        node_group: Optional[_builtins.str] = ...,
        oauth_scopes: Optional[Sequence[_builtins.str]] = ...,
        preemptible: Optional[_builtins.bool] = ...,
        reservation_affinity: Optional[
            outputs.NodePoolNodeConfigReservationAffinity
        ] = ...,
        resource_labels: Optional[Mapping[str, _builtins.str]] = ...,
        resource_manager_tags: Optional[Mapping[str, _builtins.str]] = ...,
        sandbox_config: Optional[outputs.NodePoolNodeConfigSandboxConfig] = ...,
        secondary_boot_disks: Optional[
            Sequence[outputs.NodePoolNodeConfigSecondaryBootDisk]
        ] = ...,
        service_account: Optional[_builtins.str] = ...,
        shielded_instance_config: Optional[
            outputs.NodePoolNodeConfigShieldedInstanceConfig
        ] = ...,
        sole_tenant_config: Optional[outputs.NodePoolNodeConfigSoleTenantConfig] = ...,
        spot: Optional[_builtins.bool] = ...,
        storage_pools: Optional[Sequence[_builtins.str]] = ...,
        tags: Optional[Sequence[_builtins.str]] = ...,
        taints: Optional[Sequence[outputs.NodePoolNodeConfigTaint]] = ...,
        windows_node_config: Optional[
            outputs.NodePoolNodeConfigWindowsNodeConfig
        ] = ...,
        workload_metadata_config: Optional[
            outputs.NodePoolNodeConfigWorkloadMetadataConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigAdvancedMachineFeatures]: ...
    @_builtins.property
    @pulumi.getter(name="bootDisk")
    def boot_disk(self) -> Optional[outputs.NodePoolNodeConfigBootDisk]: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskKmsKey")
    def boot_disk_kms_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="confidentialNodes")
    def confidential_nodes(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigConfidentialNodes]: ...
    @_builtins.property
    @pulumi.getter(name="containerdConfig")
    def containerd_config(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigContainerdConfig]: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveTaints")
    def effective_taints(
        self,
    ) -> Optional[Sequence[outputs.NodePoolNodeConfigEffectiveTaint]]: ...
    @_builtins.property
    @pulumi.getter(name="enableConfidentialStorage")
    def enable_confidential_storage(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageConfig")
    def ephemeral_storage_config(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigEphemeralStorageConfig]: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageLocalSsdConfig")
    def ephemeral_storage_local_ssd_config(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigEphemeralStorageLocalSsdConfig]: ...
    @_builtins.property
    @pulumi.getter(name="fastSocket")
    def fast_socket(self) -> Optional[outputs.NodePoolNodeConfigFastSocket]: ...
    @_builtins.property
    @pulumi.getter(name="flexStart")
    def flex_start(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="gcfsConfig")
    def gcfs_config(self) -> Optional[outputs.NodePoolNodeConfigGcfsConfig]: ...
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(
        self,
    ) -> Optional[Sequence[outputs.NodePoolNodeConfigGuestAccelerator]]: ...
    @_builtins.property
    @pulumi.getter
    def gvnic(self) -> Optional[outputs.NodePoolNodeConfigGvnic]: ...
    @_builtins.property
    @pulumi.getter(name="hostMaintenancePolicy")
    def host_maintenance_policy(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigHostMaintenancePolicy]: ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(self) -> Optional[outputs.NodePoolNodeConfigKubeletConfig]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="linuxNodeConfig")
    def linux_node_config(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigLinuxNodeConfig]: ...
    @_builtins.property
    @pulumi.getter(name="localNvmeSsdBlockConfig")
    def local_nvme_ssd_block_config(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigLocalNvmeSsdBlockConfig]: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="localSsdEncryptionMode")
    def local_ssd_encryption_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loggingVariant")
    def logging_variant(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxRunDuration")
    def max_run_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeGroup")
    def node_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def preemptible(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigReservationAffinity]: ...
    @_builtins.property
    @pulumi.getter(name="resourceLabels")
    def resource_labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sandboxConfig")
    def sandbox_config(self) -> Optional[outputs.NodePoolNodeConfigSandboxConfig]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryBootDisks")
    def secondary_boot_disks(
        self,
    ) -> Optional[Sequence[outputs.NodePoolNodeConfigSecondaryBootDisk]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigShieldedInstanceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="soleTenantConfig")
    def sole_tenant_config(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigSoleTenantConfig]: ...
    @_builtins.property
    @pulumi.getter
    def spot(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="storagePools")
    def storage_pools(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def taints(self) -> Optional[Sequence[outputs.NodePoolNodeConfigTaint]]: ...
    @_builtins.property
    @pulumi.getter(name="windowsNodeConfig")
    def windows_node_config(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigWindowsNodeConfig]: ...
    @_builtins.property
    @pulumi.getter(name="workloadMetadataConfig")
    def workload_metadata_config(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigWorkloadMetadataConfig]: ...

@pulumi.output_type
class NodePoolNodeConfigAdvancedMachineFeatures(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        threads_per_core: _builtins.int,
        enable_nested_virtualization: Optional[_builtins.bool] = ...,
        performance_monitoring_unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="performanceMonitoringUnit")
    def performance_monitoring_unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigBootDisk(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_type: Optional[_builtins.str] = ...,
        provisioned_iops: Optional[_builtins.int] = ...,
        provisioned_throughput: Optional[_builtins.int] = ...,
        size_gb: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class NodePoolNodeConfigConfidentialNodes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        confidential_instance_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceType")
    def confidential_instance_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigContainerdConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        private_registry_access_config: Optional[
            outputs.NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfig
        ] = ...,
        registry_hosts: Optional[
            Sequence[outputs.NodePoolNodeConfigContainerdConfigRegistryHost]
        ] = ...,
        writable_cgroups: Optional[
            outputs.NodePoolNodeConfigContainerdConfigWritableCgroups
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateRegistryAccessConfig")
    def private_registry_access_config(
        self,
    ) -> Optional[
        outputs.NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="registryHosts")
    def registry_hosts(
        self,
    ) -> Optional[Sequence[outputs.NodePoolNodeConfigContainerdConfigRegistryHost]]: ...
    @_builtins.property
    @pulumi.getter(name="writableCgroups")
    def writable_cgroups(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigContainerdConfigWritableCgroups]: ...

@pulumi.output_type
class NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        certificate_authority_domain_configs: Optional[
            Sequence[
                outputs.NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfig
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityDomainConfigs")
    def certificate_authority_domain_configs(
        self,
    ) -> Optional[
        Sequence[
            outputs.NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfig
        ]
    ]: ...

@pulumi.output_type
class NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fqdns: Sequence[_builtins.str],
        gcp_secret_manager_certificate_config: outputs.NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfig,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerCertificateConfig")
    def gcp_secret_manager_certificate_config(
        self,
    ) -> outputs.NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfig: ...

@pulumi.output_type
class NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretUri")
    def secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class NodePoolNodeConfigContainerdConfigRegistryHost(dict):
    def __init__(
        __self__,
        *,
        server: _builtins.str,
        hosts: Optional[
            Sequence[outputs.NodePoolNodeConfigContainerdConfigRegistryHostHost]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hosts(
        self,
    ) -> Optional[
        Sequence[outputs.NodePoolNodeConfigContainerdConfigRegistryHostHost]
    ]: ...

@pulumi.output_type
class NodePoolNodeConfigContainerdConfigRegistryHostHost(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host: _builtins.str,
        capabilities: Optional[Sequence[_builtins.str]] = ...,
        cas: Optional[
            Sequence[outputs.NodePoolNodeConfigContainerdConfigRegistryHostHostCa]
        ] = ...,
        clients: Optional[
            Sequence[outputs.NodePoolNodeConfigContainerdConfigRegistryHostHostClient]
        ] = ...,
        dial_timeout: Optional[_builtins.str] = ...,
        headers: Optional[
            Sequence[outputs.NodePoolNodeConfigContainerdConfigRegistryHostHostHeader]
        ] = ...,
        override_path: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def cas(
        self,
    ) -> Optional[
        Sequence[outputs.NodePoolNodeConfigContainerdConfigRegistryHostHostCa]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def clients(
        self,
    ) -> Optional[
        Sequence[outputs.NodePoolNodeConfigContainerdConfigRegistryHostHostClient]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dialTimeout")
    def dial_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        Sequence[outputs.NodePoolNodeConfigContainerdConfigRegistryHostHostHeader]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="overridePath")
    def override_path(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class NodePoolNodeConfigContainerdConfigRegistryHostHostCa(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, gcp_secret_manager_secret_uri: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigContainerdConfigRegistryHostHostClient(dict):
    def __init__(
        __self__,
        *,
        cert: outputs.NodePoolNodeConfigContainerdConfigRegistryHostHostClientCert,
        key: Optional[
            outputs.NodePoolNodeConfigContainerdConfigRegistryHostHostClientKey
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(
        self,
    ) -> outputs.NodePoolNodeConfigContainerdConfigRegistryHostHostClientCert: ...
    @_builtins.property
    @pulumi.getter
    def key(
        self,
    ) -> Optional[
        outputs.NodePoolNodeConfigContainerdConfigRegistryHostHostClientKey
    ]: ...

@pulumi.output_type
class NodePoolNodeConfigContainerdConfigRegistryHostHostClientCert(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, gcp_secret_manager_secret_uri: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigContainerdConfigRegistryHostHostClientKey(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, gcp_secret_manager_secret_uri: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigContainerdConfigRegistryHostHostHeader(dict):
    def __init__(
        __self__, *, key: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigContainerdConfigWritableCgroups(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class NodePoolNodeConfigEffectiveTaint(dict):
    def __init__(
        __self__,
        *,
        effect: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigEphemeralStorageConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, local_ssd_count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...

@pulumi.output_type
class NodePoolNodeConfigEphemeralStorageLocalSsdConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        local_ssd_count: _builtins.int,
        data_cache_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dataCacheCount")
    def data_cache_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class NodePoolNodeConfigFastSocket(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class NodePoolNodeConfigGcfsConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class NodePoolNodeConfigGuestAccelerator(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        count: _builtins.int,
        type: _builtins.str,
        gpu_driver_installation_config: Optional[
            outputs.NodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfig
        ] = ...,
        gpu_partition_size: Optional[_builtins.str] = ...,
        gpu_sharing_config: Optional[
            outputs.NodePoolNodeConfigGuestAcceleratorGpuSharingConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverInstallationConfig")
    def gpu_driver_installation_config(
        self,
    ) -> Optional[
        outputs.NodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="gpuPartitionSize")
    def gpu_partition_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingConfig")
    def gpu_sharing_config(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigGuestAcceleratorGpuSharingConfig]: ...

@pulumi.output_type
class NodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, gpu_driver_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverVersion")
    def gpu_driver_version(self) -> _builtins.str: ...

@pulumi.output_type
class NodePoolNodeConfigGuestAcceleratorGpuSharingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        gpu_sharing_strategy: _builtins.str,
        max_shared_clients_per_gpu: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingStrategy")
    def gpu_sharing_strategy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxSharedClientsPerGpu")
    def max_shared_clients_per_gpu(self) -> _builtins.int: ...

@pulumi.output_type
class NodePoolNodeConfigGvnic(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class NodePoolNodeConfigHostMaintenancePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, maintenance_interval: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceInterval")
    def maintenance_interval(self) -> _builtins.str: ...

@pulumi.output_type
class NodePoolNodeConfigKubeletConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_unsafe_sysctls: Optional[Sequence[_builtins.str]] = ...,
        container_log_max_files: Optional[_builtins.int] = ...,
        container_log_max_size: Optional[_builtins.str] = ...,
        cpu_cfs_quota: Optional[_builtins.bool] = ...,
        cpu_cfs_quota_period: Optional[_builtins.str] = ...,
        cpu_manager_policy: Optional[_builtins.str] = ...,
        eviction_max_pod_grace_period_seconds: Optional[_builtins.int] = ...,
        eviction_minimum_reclaim: Optional[
            outputs.NodePoolNodeConfigKubeletConfigEvictionMinimumReclaim
        ] = ...,
        eviction_soft: Optional[
            outputs.NodePoolNodeConfigKubeletConfigEvictionSoft
        ] = ...,
        eviction_soft_grace_period: Optional[
            outputs.NodePoolNodeConfigKubeletConfigEvictionSoftGracePeriod
        ] = ...,
        image_gc_high_threshold_percent: Optional[_builtins.int] = ...,
        image_gc_low_threshold_percent: Optional[_builtins.int] = ...,
        image_maximum_gc_age: Optional[_builtins.str] = ...,
        image_minimum_gc_age: Optional[_builtins.str] = ...,
        insecure_kubelet_readonly_port_enabled: Optional[_builtins.str] = ...,
        max_parallel_image_pulls: Optional[_builtins.int] = ...,
        memory_manager: Optional[
            outputs.NodePoolNodeConfigKubeletConfigMemoryManager
        ] = ...,
        pod_pids_limit: Optional[_builtins.int] = ...,
        single_process_oom_kill: Optional[_builtins.bool] = ...,
        topology_manager: Optional[
            outputs.NodePoolNodeConfigKubeletConfigTopologyManager
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedUnsafeSysctls")
    def allowed_unsafe_sysctls(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxFiles")
    def container_log_max_files(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxSize")
    def container_log_max_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuota")
    def cpu_cfs_quota(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuotaPeriod")
    def cpu_cfs_quota_period(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cpuManagerPolicy")
    def cpu_manager_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="evictionMaxPodGracePeriodSeconds")
    def eviction_max_pod_grace_period_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="evictionMinimumReclaim")
    def eviction_minimum_reclaim(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigKubeletConfigEvictionMinimumReclaim]: ...
    @_builtins.property
    @pulumi.getter(name="evictionSoft")
    def eviction_soft(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigKubeletConfigEvictionSoft]: ...
    @_builtins.property
    @pulumi.getter(name="evictionSoftGracePeriod")
    def eviction_soft_grace_period(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigKubeletConfigEvictionSoftGracePeriod]: ...
    @_builtins.property
    @pulumi.getter(name="imageGcHighThresholdPercent")
    def image_gc_high_threshold_percent(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="imageGcLowThresholdPercent")
    def image_gc_low_threshold_percent(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="imageMaximumGcAge")
    def image_maximum_gc_age(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageMinimumGcAge")
    def image_minimum_gc_age(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="insecureKubeletReadonlyPortEnabled")
    def insecure_kubelet_readonly_port_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxParallelImagePulls")
    def max_parallel_image_pulls(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="memoryManager")
    def memory_manager(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigKubeletConfigMemoryManager]: ...
    @_builtins.property
    @pulumi.getter(name="podPidsLimit")
    def pod_pids_limit(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="singleProcessOomKill")
    def single_process_oom_kill(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="topologyManager")
    def topology_manager(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigKubeletConfigTopologyManager]: ...

@pulumi.output_type
class NodePoolNodeConfigKubeletConfigEvictionMinimumReclaim(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[_builtins.str] = ...,
        imagefs_inodes_free: Optional[_builtins.str] = ...,
        memory_available: Optional[_builtins.str] = ...,
        nodefs_available: Optional[_builtins.str] = ...,
        nodefs_inodes_free: Optional[_builtins.str] = ...,
        pid_available: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigKubeletConfigEvictionSoft(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[_builtins.str] = ...,
        imagefs_inodes_free: Optional[_builtins.str] = ...,
        memory_available: Optional[_builtins.str] = ...,
        nodefs_available: Optional[_builtins.str] = ...,
        nodefs_inodes_free: Optional[_builtins.str] = ...,
        pid_available: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigKubeletConfigEvictionSoftGracePeriod(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[_builtins.str] = ...,
        imagefs_inodes_free: Optional[_builtins.str] = ...,
        memory_available: Optional[_builtins.str] = ...,
        nodefs_available: Optional[_builtins.str] = ...,
        nodefs_inodes_free: Optional[_builtins.str] = ...,
        pid_available: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigKubeletConfigMemoryManager(dict):
    def __init__(__self__, *, policy: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigKubeletConfigTopologyManager(dict):
    def __init__(
        __self__,
        *,
        policy: Optional[_builtins.str] = ...,
        scope: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigLinuxNodeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cgroup_mode: Optional[_builtins.str] = ...,
        hugepages_config: Optional[
            outputs.NodePoolNodeConfigLinuxNodeConfigHugepagesConfig
        ] = ...,
        node_kernel_module_loading: Optional[
            outputs.NodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoading
        ] = ...,
        sysctls: Optional[Mapping[str, _builtins.str]] = ...,
        transparent_hugepage_defrag: Optional[_builtins.str] = ...,
        transparent_hugepage_enabled: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cgroupMode")
    def cgroup_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hugepagesConfig")
    def hugepages_config(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigLinuxNodeConfigHugepagesConfig]: ...
    @_builtins.property
    @pulumi.getter(name="nodeKernelModuleLoading")
    def node_kernel_module_loading(
        self,
    ) -> Optional[outputs.NodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoading]: ...
    @_builtins.property
    @pulumi.getter
    def sysctls(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageDefrag")
    def transparent_hugepage_defrag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageEnabled")
    def transparent_hugepage_enabled(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigLinuxNodeConfigHugepagesConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hugepage_size1g: Optional[_builtins.int] = ...,
        hugepage_size2m: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize1g")
    def hugepage_size1g(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize2m")
    def hugepage_size2m(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class NodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoading(dict):
    def __init__(__self__, *, policy: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigLocalNvmeSsdBlockConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, local_ssd_count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...

@pulumi.output_type
class NodePoolNodeConfigReservationAffinity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        consume_reservation_type: _builtins.str,
        key: Optional[_builtins.str] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class NodePoolNodeConfigSandboxConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sandbox_type: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sandboxType")
    @_utilities.deprecated(...)
    def sandbox_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigSecondaryBootDisk(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, disk_image: _builtins.str, mode: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskImage")
    def disk_image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigShieldedInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: Optional[_builtins.bool] = ...,
        enable_secure_boot: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class NodePoolNodeConfigSoleTenantConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        node_affinities: Sequence[
            outputs.NodePoolNodeConfigSoleTenantConfigNodeAffinity
        ],
        min_node_cpus: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeAffinities")
    def node_affinities(
        self,
    ) -> Sequence[outputs.NodePoolNodeConfigSoleTenantConfigNodeAffinity]: ...
    @_builtins.property
    @pulumi.getter(name="minNodeCpus")
    def min_node_cpus(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class NodePoolNodeConfigSoleTenantConfigNodeAffinity(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        operator: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigTaint(dict):
    def __init__(
        __self__, *, effect: _builtins.str, key: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class NodePoolNodeConfigWindowsNodeConfig(dict):
    def __init__(__self__, *, osversion: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def osversion(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolNodeConfigWorkloadMetadataConfig(dict):
    def __init__(__self__, *, mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class NodePoolNodeDrainConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        respect_pdb_during_node_pool_deletion: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="respectPdbDuringNodePoolDeletion")
    def respect_pdb_during_node_pool_deletion(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class NodePoolPlacementPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        policy_name: Optional[_builtins.str] = ...,
        tpu_topology: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tpuTopology")
    def tpu_topology(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolQueuedProvisioning(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class NodePoolUpgradeSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        blue_green_settings: Optional[
            outputs.NodePoolUpgradeSettingsBlueGreenSettings
        ] = ...,
        max_surge: Optional[_builtins.int] = ...,
        max_unavailable: Optional[_builtins.int] = ...,
        strategy: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blueGreenSettings")
    def blue_green_settings(
        self,
    ) -> Optional[outputs.NodePoolUpgradeSettingsBlueGreenSettings]: ...
    @_builtins.property
    @pulumi.getter(name="maxSurge")
    def max_surge(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxUnavailable")
    def max_unavailable(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def strategy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolUpgradeSettingsBlueGreenSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        autoscaled_rollout_policy: Optional[
            outputs.NodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicy
        ] = ...,
        node_pool_soak_duration: Optional[_builtins.str] = ...,
        standard_rollout_policy: Optional[
            outputs.NodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscaledRolloutPolicy")
    def autoscaled_rollout_policy(
        self,
    ) -> Optional[
        outputs.NodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicy
    ]: ...
    @_builtins.property
    @pulumi.getter(name="nodePoolSoakDuration")
    def node_pool_soak_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="standardRolloutPolicy")
    def standard_rollout_policy(
        self,
    ) -> Optional[
        outputs.NodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy
    ]: ...

@pulumi.output_type
class NodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, wait_for_drain_duration: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="waitForDrainDuration")
    def wait_for_drain_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        batch_node_count: Optional[_builtins.int] = ...,
        batch_percentage: Optional[_builtins.float] = ...,
        batch_soak_duration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchNodeCount")
    def batch_node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="batchPercentage")
    def batch_percentage(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="batchSoakDuration")
    def batch_soak_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetClusterAddonsConfigResult(dict):
    def __init__(
        __self__,
        *,
        cloudrun_configs: Sequence[outputs.GetClusterAddonsConfigCloudrunConfigResult],
        config_connector_configs: Sequence[
            outputs.GetClusterAddonsConfigConfigConnectorConfigResult
        ],
        dns_cache_configs: Sequence[outputs.GetClusterAddonsConfigDnsCacheConfigResult],
        gce_persistent_disk_csi_driver_configs: Sequence[
            outputs.GetClusterAddonsConfigGcePersistentDiskCsiDriverConfigResult
        ],
        gcp_filestore_csi_driver_configs: Sequence[
            outputs.GetClusterAddonsConfigGcpFilestoreCsiDriverConfigResult
        ],
        gcs_fuse_csi_driver_configs: Sequence[
            outputs.GetClusterAddonsConfigGcsFuseCsiDriverConfigResult
        ],
        gke_backup_agent_configs: Sequence[
            outputs.GetClusterAddonsConfigGkeBackupAgentConfigResult
        ],
        horizontal_pod_autoscalings: Sequence[
            outputs.GetClusterAddonsConfigHorizontalPodAutoscalingResult
        ],
        http_load_balancings: Sequence[
            outputs.GetClusterAddonsConfigHttpLoadBalancingResult
        ],
        istio_configs: Sequence[outputs.GetClusterAddonsConfigIstioConfigResult],
        kalm_configs: Sequence[outputs.GetClusterAddonsConfigKalmConfigResult],
        lustre_csi_driver_configs: Sequence[
            outputs.GetClusterAddonsConfigLustreCsiDriverConfigResult
        ],
        network_policy_configs: Sequence[
            outputs.GetClusterAddonsConfigNetworkPolicyConfigResult
        ],
        parallelstore_csi_driver_configs: Sequence[
            outputs.GetClusterAddonsConfigParallelstoreCsiDriverConfigResult
        ],
        pod_snapshot_configs: Sequence[
            outputs.GetClusterAddonsConfigPodSnapshotConfigResult
        ],
        ray_operator_configs: Sequence[
            outputs.GetClusterAddonsConfigRayOperatorConfigResult
        ],
        slice_controller_configs: Sequence[
            outputs.GetClusterAddonsConfigSliceControllerConfigResult
        ],
        stateful_ha_configs: Sequence[
            outputs.GetClusterAddonsConfigStatefulHaConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudrunConfigs")
    def cloudrun_configs(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigCloudrunConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="configConnectorConfigs")
    def config_connector_configs(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigConfigConnectorConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="dnsCacheConfigs")
    def dns_cache_configs(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigDnsCacheConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="gcePersistentDiskCsiDriverConfigs")
    def gce_persistent_disk_csi_driver_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterAddonsConfigGcePersistentDiskCsiDriverConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="gcpFilestoreCsiDriverConfigs")
    def gcp_filestore_csi_driver_configs(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigGcpFilestoreCsiDriverConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="gcsFuseCsiDriverConfigs")
    def gcs_fuse_csi_driver_configs(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigGcsFuseCsiDriverConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="gkeBackupAgentConfigs")
    def gke_backup_agent_configs(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigGkeBackupAgentConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="horizontalPodAutoscalings")
    def horizontal_pod_autoscalings(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigHorizontalPodAutoscalingResult]: ...
    @_builtins.property
    @pulumi.getter(name="httpLoadBalancings")
    def http_load_balancings(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigHttpLoadBalancingResult]: ...
    @_builtins.property
    @pulumi.getter(name="istioConfigs")
    def istio_configs(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigIstioConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="kalmConfigs")
    def kalm_configs(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigKalmConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="lustreCsiDriverConfigs")
    def lustre_csi_driver_configs(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigLustreCsiDriverConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="networkPolicyConfigs")
    def network_policy_configs(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigNetworkPolicyConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="parallelstoreCsiDriverConfigs")
    def parallelstore_csi_driver_configs(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigParallelstoreCsiDriverConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="podSnapshotConfigs")
    def pod_snapshot_configs(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigPodSnapshotConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="rayOperatorConfigs")
    def ray_operator_configs(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigRayOperatorConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="sliceControllerConfigs")
    def slice_controller_configs(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigSliceControllerConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="statefulHaConfigs")
    def stateful_ha_configs(
        self,
    ) -> Sequence[outputs.GetClusterAddonsConfigStatefulHaConfigResult]: ...

@pulumi.output_type
class GetClusterAddonsConfigCloudrunConfigResult(dict):
    def __init__(
        __self__, *, disabled: _builtins.bool, load_balancer_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterAddonsConfigConfigConnectorConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigDnsCacheConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigGcePersistentDiskCsiDriverConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigGcpFilestoreCsiDriverConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigGcsFuseCsiDriverConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigGkeBackupAgentConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigHorizontalPodAutoscalingResult(dict):
    def __init__(__self__, *, disabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigHttpLoadBalancingResult(dict):
    def __init__(__self__, *, disabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigIstioConfigResult(dict):
    def __init__(
        __self__, *, auth: _builtins.str, disabled: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def auth(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigKalmConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigLustreCsiDriverConfigResult(dict):
    def __init__(
        __self__, *, enable_legacy_lustre_port: _builtins.bool, enabled: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableLegacyLustrePort")
    def enable_legacy_lustre_port(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigNetworkPolicyConfigResult(dict):
    def __init__(__self__, *, disabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigParallelstoreCsiDriverConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigPodSnapshotConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigRayOperatorConfigResult(dict):
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        ray_cluster_logging_configs: Sequence[
            outputs.GetClusterAddonsConfigRayOperatorConfigRayClusterLoggingConfigResult
        ],
        ray_cluster_monitoring_configs: Sequence[
            outputs.GetClusterAddonsConfigRayOperatorConfigRayClusterMonitoringConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="rayClusterLoggingConfigs")
    def ray_cluster_logging_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterAddonsConfigRayOperatorConfigRayClusterLoggingConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="rayClusterMonitoringConfigs")
    def ray_cluster_monitoring_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterAddonsConfigRayOperatorConfigRayClusterMonitoringConfigResult
    ]: ...

@pulumi.output_type
class GetClusterAddonsConfigRayOperatorConfigRayClusterLoggingConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigRayOperatorConfigRayClusterMonitoringConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigSliceControllerConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAddonsConfigStatefulHaConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterAnonymousAuthenticationConfigResult(dict):
    def __init__(__self__, *, mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterAuthenticatorGroupsConfigResult(dict):
    def __init__(__self__, *, security_group: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroup")
    def security_group(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterBinaryAuthorizationResult(dict):
    def __init__(
        __self__, *, enabled: _builtins.bool, evaluation_mode: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="evaluationMode")
    def evaluation_mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterClusterAutoscalingResult(dict):
    def __init__(
        __self__,
        *,
        auto_provisioning_defaults: Sequence[
            outputs.GetClusterClusterAutoscalingAutoProvisioningDefaultResult
        ],
        auto_provisioning_locations: Sequence[_builtins.str],
        autoscaling_profile: _builtins.str,
        default_compute_class_enabled: _builtins.bool,
        enabled: _builtins.bool,
        resource_limits: Sequence[
            outputs.GetClusterClusterAutoscalingResourceLimitResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoProvisioningDefaults")
    def auto_provisioning_defaults(
        self,
    ) -> Sequence[
        outputs.GetClusterClusterAutoscalingAutoProvisioningDefaultResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="autoProvisioningLocations")
    def auto_provisioning_locations(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingProfile")
    def autoscaling_profile(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultComputeClassEnabled")
    def default_compute_class_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="resourceLimits")
    def resource_limits(
        self,
    ) -> Sequence[outputs.GetClusterClusterAutoscalingResourceLimitResult]: ...

@pulumi.output_type
class GetClusterClusterAutoscalingAutoProvisioningDefaultResult(dict):
    def __init__(
        __self__,
        *,
        boot_disk_kms_key: _builtins.str,
        disk_size: _builtins.int,
        disk_type: _builtins.str,
        image_type: _builtins.str,
        managements: Sequence[
            outputs.GetClusterClusterAutoscalingAutoProvisioningDefaultManagementResult
        ],
        min_cpu_platform: _builtins.str,
        oauth_scopes: Sequence[_builtins.str],
        service_account: _builtins.str,
        shielded_instance_configs: Sequence[
            outputs.GetClusterClusterAutoscalingAutoProvisioningDefaultShieldedInstanceConfigResult
        ],
        upgrade_settings: Sequence[
            outputs.GetClusterClusterAutoscalingAutoProvisioningDefaultUpgradeSettingResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskKmsKey")
    def boot_disk_kms_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def managements(
        self,
    ) -> Sequence[
        outputs.GetClusterClusterAutoscalingAutoProvisioningDefaultManagementResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfigs")
    def shielded_instance_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterClusterAutoscalingAutoProvisioningDefaultShieldedInstanceConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(
        self,
    ) -> Sequence[
        outputs.GetClusterClusterAutoscalingAutoProvisioningDefaultUpgradeSettingResult
    ]: ...

@pulumi.output_type
class GetClusterClusterAutoscalingAutoProvisioningDefaultManagementResult(dict):
    def __init__(
        __self__,
        *,
        auto_repair: _builtins.bool,
        auto_upgrade: _builtins.bool,
        upgrade_options: Sequence[
            outputs.GetClusterClusterAutoscalingAutoProvisioningDefaultManagementUpgradeOptionResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRepair")
    def auto_repair(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="autoUpgrade")
    def auto_upgrade(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="upgradeOptions")
    def upgrade_options(
        self,
    ) -> Sequence[
        outputs.GetClusterClusterAutoscalingAutoProvisioningDefaultManagementUpgradeOptionResult
    ]: ...

@pulumi.output_type
class GetClusterClusterAutoscalingAutoProvisioningDefaultManagementUpgradeOptionResult(
    dict
):
    def __init__(
        __self__, *, auto_upgrade_start_time: _builtins.str, description: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoUpgradeStartTime")
    def auto_upgrade_start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterClusterAutoscalingAutoProvisioningDefaultShieldedInstanceConfigResult(
    dict
):
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: _builtins.bool,
        enable_secure_boot: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterClusterAutoscalingAutoProvisioningDefaultUpgradeSettingResult(dict):
    def __init__(
        __self__,
        *,
        blue_green_settings: Sequence[
            outputs.GetClusterClusterAutoscalingAutoProvisioningDefaultUpgradeSettingBlueGreenSettingResult
        ],
        max_surge: _builtins.int,
        max_unavailable: _builtins.int,
        strategy: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blueGreenSettings")
    def blue_green_settings(
        self,
    ) -> Sequence[
        outputs.GetClusterClusterAutoscalingAutoProvisioningDefaultUpgradeSettingBlueGreenSettingResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maxSurge")
    def max_surge(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxUnavailable")
    def max_unavailable(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def strategy(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterClusterAutoscalingAutoProvisioningDefaultUpgradeSettingBlueGreenSettingResult(
    dict
):
    def __init__(
        __self__,
        *,
        node_pool_soak_duration: _builtins.str,
        standard_rollout_policies: Sequence[
            outputs.GetClusterClusterAutoscalingAutoProvisioningDefaultUpgradeSettingBlueGreenSettingStandardRolloutPolicyResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodePoolSoakDuration")
    def node_pool_soak_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="standardRolloutPolicies")
    def standard_rollout_policies(
        self,
    ) -> Sequence[
        outputs.GetClusterClusterAutoscalingAutoProvisioningDefaultUpgradeSettingBlueGreenSettingStandardRolloutPolicyResult
    ]: ...

@pulumi.output_type
class GetClusterClusterAutoscalingAutoProvisioningDefaultUpgradeSettingBlueGreenSettingStandardRolloutPolicyResult(
    dict
):
    def __init__(
        __self__,
        *,
        batch_node_count: _builtins.int,
        batch_percentage: _builtins.float,
        batch_soak_duration: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchNodeCount")
    def batch_node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="batchPercentage")
    def batch_percentage(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="batchSoakDuration")
    def batch_soak_duration(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterClusterAutoscalingResourceLimitResult(dict):
    def __init__(
        __self__,
        *,
        maximum: _builtins.int,
        minimum: _builtins.int,
        resource_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterClusterTelemetryResult(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterConfidentialNodeResult(dict):
    def __init__(
        __self__, *, confidential_instance_type: _builtins.str, enabled: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceType")
    def confidential_instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterControlPlaneEndpointsConfigResult(dict):
    def __init__(
        __self__,
        *,
        dns_endpoint_configs: Sequence[
            outputs.GetClusterControlPlaneEndpointsConfigDnsEndpointConfigResult
        ],
        ip_endpoints_configs: Sequence[
            outputs.GetClusterControlPlaneEndpointsConfigIpEndpointsConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsEndpointConfigs")
    def dns_endpoint_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterControlPlaneEndpointsConfigDnsEndpointConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ipEndpointsConfigs")
    def ip_endpoints_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterControlPlaneEndpointsConfigIpEndpointsConfigResult
    ]: ...

@pulumi.output_type
class GetClusterControlPlaneEndpointsConfigDnsEndpointConfigResult(dict):
    def __init__(
        __self__,
        *,
        allow_external_traffic: _builtins.bool,
        enable_k8s_certs_via_dns: _builtins.bool,
        enable_k8s_tokens_via_dns: _builtins.bool,
        endpoint: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowExternalTraffic")
    def allow_external_traffic(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableK8sCertsViaDns")
    def enable_k8s_certs_via_dns(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableK8sTokensViaDns")
    def enable_k8s_tokens_via_dns(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterControlPlaneEndpointsConfigIpEndpointsConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterCostManagementConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterDatabaseEncryptionResult(dict):
    def __init__(
        __self__, *, key_name: _builtins.str, state: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterDefaultSnatStatusResult(dict):
    def __init__(__self__, *, disabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterDnsConfigResult(dict):
    def __init__(
        __self__,
        *,
        additive_vpc_scope_dns_domain: _builtins.str,
        cluster_dns: _builtins.str,
        cluster_dns_domain: _builtins.str,
        cluster_dns_scope: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additiveVpcScopeDnsDomain")
    def additive_vpc_scope_dns_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterDns")
    def cluster_dns(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterDnsDomain")
    def cluster_dns_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterDnsScope")
    def cluster_dns_scope(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterEnableK8sBetaApiResult(dict):
    def __init__(__self__, *, enabled_apis: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledApis")
    def enabled_apis(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterEnterpriseConfigResult(dict):
    def __init__(
        __self__, *, cluster_tier: _builtins.str, desired_tier: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterTier")
    def cluster_tier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="desiredTier")
    def desired_tier(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterFleetResult(dict):
    def __init__(
        __self__,
        *,
        membership: _builtins.str,
        membership_id: _builtins.str,
        membership_location: _builtins.str,
        membership_type: _builtins.str,
        pre_registered: _builtins.bool,
        project: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="membershipId")
    def membership_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="membershipLocation")
    def membership_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="membershipType")
    def membership_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="preRegistered")
    def pre_registered(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterGatewayApiConfigResult(dict):
    def __init__(__self__, *, channel: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterGkeAutoUpgradeConfigResult(dict):
    def __init__(__self__, *, patch_mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterIdentityServiceConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterIpAllocationPolicyResult(dict):
    def __init__(
        __self__,
        *,
        additional_ip_ranges_configs: Sequence[
            outputs.GetClusterIpAllocationPolicyAdditionalIpRangesConfigResult
        ],
        additional_pod_ranges_configs: Sequence[
            outputs.GetClusterIpAllocationPolicyAdditionalPodRangesConfigResult
        ],
        auto_ipam_configs: Sequence[
            outputs.GetClusterIpAllocationPolicyAutoIpamConfigResult
        ],
        cluster_ipv4_cidr_block: _builtins.str,
        cluster_secondary_range_name: _builtins.str,
        network_tier_configs: Sequence[
            outputs.GetClusterIpAllocationPolicyNetworkTierConfigResult
        ],
        pod_cidr_overprovision_configs: Sequence[
            outputs.GetClusterIpAllocationPolicyPodCidrOverprovisionConfigResult
        ],
        services_ipv4_cidr_block: _builtins.str,
        services_secondary_range_name: _builtins.str,
        stack_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalIpRangesConfigs")
    def additional_ip_ranges_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterIpAllocationPolicyAdditionalIpRangesConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="additionalPodRangesConfigs")
    def additional_pod_ranges_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterIpAllocationPolicyAdditionalPodRangesConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="autoIpamConfigs")
    def auto_ipam_configs(
        self,
    ) -> Sequence[outputs.GetClusterIpAllocationPolicyAutoIpamConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="clusterIpv4CidrBlock")
    def cluster_ipv4_cidr_block(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterSecondaryRangeName")
    def cluster_secondary_range_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkTierConfigs")
    def network_tier_configs(
        self,
    ) -> Sequence[outputs.GetClusterIpAllocationPolicyNetworkTierConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="podCidrOverprovisionConfigs")
    def pod_cidr_overprovision_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterIpAllocationPolicyPodCidrOverprovisionConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="servicesIpv4CidrBlock")
    def services_ipv4_cidr_block(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="servicesSecondaryRangeName")
    def services_secondary_range_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterIpAllocationPolicyAdditionalIpRangesConfigResult(dict):
    def __init__(
        __self__,
        *,
        pod_ipv4_range_names: Sequence[_builtins.str],
        status: _builtins.str,
        subnetwork: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="podIpv4RangeNames")
    def pod_ipv4_range_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterIpAllocationPolicyAdditionalPodRangesConfigResult(dict):
    def __init__(__self__, *, pod_range_names: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="podRangeNames")
    def pod_range_names(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterIpAllocationPolicyAutoIpamConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterIpAllocationPolicyNetworkTierConfigResult(dict):
    def __init__(__self__, *, network_tier: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterIpAllocationPolicyPodCidrOverprovisionConfigResult(dict):
    def __init__(__self__, *, disabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterLoggingConfigResult(dict):
    def __init__(__self__, *, enable_components: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableComponents")
    def enable_components(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterMaintenancePolicyResult(dict):
    def __init__(
        __self__,
        *,
        daily_maintenance_windows: Sequence[
            outputs.GetClusterMaintenancePolicyDailyMaintenanceWindowResult
        ],
        disruption_budgets: Sequence[
            outputs.GetClusterMaintenancePolicyDisruptionBudgetResult
        ],
        maintenance_exclusions: Sequence[
            outputs.GetClusterMaintenancePolicyMaintenanceExclusionResult
        ],
        recurring_windows: Sequence[
            outputs.GetClusterMaintenancePolicyRecurringWindowResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dailyMaintenanceWindows")
    def daily_maintenance_windows(
        self,
    ) -> Sequence[outputs.GetClusterMaintenancePolicyDailyMaintenanceWindowResult]: ...
    @_builtins.property
    @pulumi.getter(name="disruptionBudgets")
    def disruption_budgets(
        self,
    ) -> Sequence[outputs.GetClusterMaintenancePolicyDisruptionBudgetResult]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceExclusions")
    def maintenance_exclusions(
        self,
    ) -> Sequence[outputs.GetClusterMaintenancePolicyMaintenanceExclusionResult]: ...
    @_builtins.property
    @pulumi.getter(name="recurringWindows")
    def recurring_windows(
        self,
    ) -> Sequence[outputs.GetClusterMaintenancePolicyRecurringWindowResult]: ...

@pulumi.output_type
class GetClusterMaintenancePolicyDailyMaintenanceWindowResult(dict):
    def __init__(
        __self__, *, duration: _builtins.str, start_time: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterMaintenancePolicyDisruptionBudgetResult(dict):
    def __init__(
        __self__,
        *,
        last_disruption_time: _builtins.str,
        last_minor_version_disruption_time: _builtins.str,
        minor_version_disruption_interval: _builtins.str,
        patch_version_disruption_interval: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastDisruptionTime")
    def last_disruption_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastMinorVersionDisruptionTime")
    def last_minor_version_disruption_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minorVersionDisruptionInterval")
    def minor_version_disruption_interval(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="patchVersionDisruptionInterval")
    def patch_version_disruption_interval(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterMaintenancePolicyMaintenanceExclusionResult(dict):
    def __init__(
        __self__,
        *,
        end_time: _builtins.str,
        exclusion_name: _builtins.str,
        exclusion_options: Sequence[
            outputs.GetClusterMaintenancePolicyMaintenanceExclusionExclusionOptionResult
        ],
        start_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exclusionName")
    def exclusion_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exclusionOptions")
    def exclusion_options(
        self,
    ) -> Sequence[
        outputs.GetClusterMaintenancePolicyMaintenanceExclusionExclusionOptionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterMaintenancePolicyMaintenanceExclusionExclusionOptionResult(dict):
    def __init__(
        __self__, *, end_time_behavior: _builtins.str, scope: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTimeBehavior")
    def end_time_behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterMaintenancePolicyRecurringWindowResult(dict):
    def __init__(
        __self__,
        *,
        end_time: _builtins.str,
        recurrence: _builtins.str,
        start_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterManagedOpentelemetryConfigResult(dict):
    def __init__(__self__, *, scope: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterMasterAuthResult(dict):
    def __init__(
        __self__,
        *,
        client_certificate: _builtins.str,
        client_certificate_configs: Sequence[
            outputs.GetClusterMasterAuthClientCertificateConfigResult
        ],
        client_key: _builtins.str,
        cluster_ca_certificate: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificateConfigs")
    def client_certificate_configs(
        self,
    ) -> Sequence[outputs.GetClusterMasterAuthClientCertificateConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterCaCertificate")
    def cluster_ca_certificate(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterMasterAuthClientCertificateConfigResult(dict):
    def __init__(__self__, *, issue_client_certificate: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="issueClientCertificate")
    def issue_client_certificate(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterMasterAuthorizedNetworksConfigResult(dict):
    def __init__(
        __self__,
        *,
        cidr_blocks: Sequence[
            outputs.GetClusterMasterAuthorizedNetworksConfigCidrBlockResult
        ],
        gcp_public_cidrs_access_enabled: _builtins.bool,
        private_endpoint_enforcement_enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(
        self,
    ) -> Sequence[outputs.GetClusterMasterAuthorizedNetworksConfigCidrBlockResult]: ...
    @_builtins.property
    @pulumi.getter(name="gcpPublicCidrsAccessEnabled")
    def gcp_public_cidrs_access_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointEnforcementEnabled")
    def private_endpoint_enforcement_enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterMasterAuthorizedNetworksConfigCidrBlockResult(dict):
    def __init__(
        __self__, *, cidr_block: _builtins.str, display_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterMeshCertificateResult(dict):
    def __init__(__self__, *, enable_certificates: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableCertificates")
    def enable_certificates(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterMonitoringConfigResult(dict):
    def __init__(
        __self__,
        *,
        advanced_datapath_observability_configs: Sequence[
            outputs.GetClusterMonitoringConfigAdvancedDatapathObservabilityConfigResult
        ],
        enable_components: Sequence[_builtins.str],
        managed_prometheuses: Sequence[
            outputs.GetClusterMonitoringConfigManagedPrometheusResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedDatapathObservabilityConfigs")
    def advanced_datapath_observability_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterMonitoringConfigAdvancedDatapathObservabilityConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableComponents")
    def enable_components(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedPrometheuses")
    def managed_prometheuses(
        self,
    ) -> Sequence[outputs.GetClusterMonitoringConfigManagedPrometheusResult]: ...

@pulumi.output_type
class GetClusterMonitoringConfigAdvancedDatapathObservabilityConfigResult(dict):
    def __init__(
        __self__, *, enable_metrics: _builtins.bool, enable_relay: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableMetrics")
    def enable_metrics(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableRelay")
    def enable_relay(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterMonitoringConfigManagedPrometheusResult(dict):
    def __init__(
        __self__,
        *,
        auto_monitoring_configs: Sequence[
            outputs.GetClusterMonitoringConfigManagedPrometheusAutoMonitoringConfigResult
        ],
        enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoMonitoringConfigs")
    def auto_monitoring_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterMonitoringConfigManagedPrometheusAutoMonitoringConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterMonitoringConfigManagedPrometheusAutoMonitoringConfigResult(dict):
    def __init__(__self__, *, scope: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNetworkPerformanceConfigResult(dict):
    def __init__(__self__, *, total_egress_bandwidth_tier: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="totalEgressBandwidthTier")
    def total_egress_bandwidth_tier(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNetworkPolicyResult(dict):
    def __init__(
        __self__, *, enabled: _builtins.bool, provider: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigResult(dict):
    def __init__(
        __self__,
        *,
        advanced_machine_features: Sequence[
            outputs.GetClusterNodeConfigAdvancedMachineFeatureResult
        ],
        boot_disk_kms_key: _builtins.str,
        boot_disks: Sequence[outputs.GetClusterNodeConfigBootDiskResult],
        confidential_nodes: Sequence[
            outputs.GetClusterNodeConfigConfidentialNodeResult
        ],
        containerd_configs: Sequence[
            outputs.GetClusterNodeConfigContainerdConfigResult
        ],
        disk_size_gb: _builtins.int,
        disk_type: _builtins.str,
        effective_taints: Sequence[outputs.GetClusterNodeConfigEffectiveTaintResult],
        enable_confidential_storage: _builtins.bool,
        ephemeral_storage_configs: Sequence[
            outputs.GetClusterNodeConfigEphemeralStorageConfigResult
        ],
        ephemeral_storage_local_ssd_configs: Sequence[
            outputs.GetClusterNodeConfigEphemeralStorageLocalSsdConfigResult
        ],
        fast_sockets: Sequence[outputs.GetClusterNodeConfigFastSocketResult],
        flex_start: _builtins.bool,
        gcfs_configs: Sequence[outputs.GetClusterNodeConfigGcfsConfigResult],
        guest_accelerators: Sequence[
            outputs.GetClusterNodeConfigGuestAcceleratorResult
        ],
        gvnics: Sequence[outputs.GetClusterNodeConfigGvnicResult],
        host_maintenance_policies: Sequence[
            outputs.GetClusterNodeConfigHostMaintenancePolicyResult
        ],
        image_type: _builtins.str,
        kubelet_configs: Sequence[outputs.GetClusterNodeConfigKubeletConfigResult],
        labels: Mapping[str, _builtins.str],
        linux_node_configs: Sequence[outputs.GetClusterNodeConfigLinuxNodeConfigResult],
        local_nvme_ssd_block_configs: Sequence[
            outputs.GetClusterNodeConfigLocalNvmeSsdBlockConfigResult
        ],
        local_ssd_count: _builtins.int,
        local_ssd_encryption_mode: _builtins.str,
        logging_variant: _builtins.str,
        machine_type: _builtins.str,
        max_run_duration: _builtins.str,
        metadata: Mapping[str, _builtins.str],
        min_cpu_platform: _builtins.str,
        node_group: _builtins.str,
        oauth_scopes: Sequence[_builtins.str],
        preemptible: _builtins.bool,
        reservation_affinities: Sequence[
            outputs.GetClusterNodeConfigReservationAffinityResult
        ],
        resource_labels: Mapping[str, _builtins.str],
        resource_manager_tags: Mapping[str, _builtins.str],
        sandbox_configs: Sequence[outputs.GetClusterNodeConfigSandboxConfigResult],
        secondary_boot_disks: Sequence[
            outputs.GetClusterNodeConfigSecondaryBootDiskResult
        ],
        service_account: _builtins.str,
        shielded_instance_configs: Sequence[
            outputs.GetClusterNodeConfigShieldedInstanceConfigResult
        ],
        sole_tenant_configs: Sequence[
            outputs.GetClusterNodeConfigSoleTenantConfigResult
        ],
        spot: _builtins.bool,
        storage_pools: Sequence[_builtins.str],
        tags: Sequence[_builtins.str],
        taints: Sequence[outputs.GetClusterNodeConfigTaintResult],
        windows_node_configs: Sequence[
            outputs.GetClusterNodeConfigWindowsNodeConfigResult
        ],
        workload_metadata_configs: Sequence[
            outputs.GetClusterNodeConfigWorkloadMetadataConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigAdvancedMachineFeatureResult]: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskKmsKey")
    def boot_disk_kms_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bootDisks")
    def boot_disks(self) -> Sequence[outputs.GetClusterNodeConfigBootDiskResult]: ...
    @_builtins.property
    @pulumi.getter(name="confidentialNodes")
    def confidential_nodes(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigConfidentialNodeResult]: ...
    @_builtins.property
    @pulumi.getter(name="containerdConfigs")
    def containerd_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigContainerdConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveTaints")
    def effective_taints(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigEffectiveTaintResult]: ...
    @_builtins.property
    @pulumi.getter(name="enableConfidentialStorage")
    def enable_confidential_storage(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageConfigs")
    def ephemeral_storage_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigEphemeralStorageConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageLocalSsdConfigs")
    def ephemeral_storage_local_ssd_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigEphemeralStorageLocalSsdConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="fastSockets")
    def fast_sockets(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigFastSocketResult]: ...
    @_builtins.property
    @pulumi.getter(name="flexStart")
    def flex_start(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="gcfsConfigs")
    def gcfs_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigGcfsConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigGuestAcceleratorResult]: ...
    @_builtins.property
    @pulumi.getter
    def gvnics(self) -> Sequence[outputs.GetClusterNodeConfigGvnicResult]: ...
    @_builtins.property
    @pulumi.getter(name="hostMaintenancePolicies")
    def host_maintenance_policies(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigHostMaintenancePolicyResult]: ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kubeletConfigs")
    def kubelet_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigKubeletConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linuxNodeConfigs")
    def linux_node_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigLinuxNodeConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="localNvmeSsdBlockConfigs")
    def local_nvme_ssd_block_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigLocalNvmeSsdBlockConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="localSsdEncryptionMode")
    def local_ssd_encryption_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="loggingVariant")
    def logging_variant(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxRunDuration")
    def max_run_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeGroup")
    def node_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def preemptible(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinities")
    def reservation_affinities(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigReservationAffinityResult]: ...
    @_builtins.property
    @pulumi.getter(name="resourceLabels")
    def resource_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sandboxConfigs")
    def sandbox_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigSandboxConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryBootDisks")
    def secondary_boot_disks(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigSecondaryBootDiskResult]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfigs")
    def shielded_instance_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigShieldedInstanceConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="soleTenantConfigs")
    def sole_tenant_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigSoleTenantConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def spot(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="storagePools")
    def storage_pools(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def taints(self) -> Sequence[outputs.GetClusterNodeConfigTaintResult]: ...
    @_builtins.property
    @pulumi.getter(name="windowsNodeConfigs")
    def windows_node_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigWindowsNodeConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="workloadMetadataConfigs")
    def workload_metadata_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigWorkloadMetadataConfigResult]: ...

@pulumi.output_type
class GetClusterNodeConfigAdvancedMachineFeatureResult(dict):
    def __init__(
        __self__,
        *,
        enable_nested_virtualization: _builtins.bool,
        performance_monitoring_unit: _builtins.str,
        threads_per_core: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="performanceMonitoringUnit")
    def performance_monitoring_unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterNodeConfigBootDiskResult(dict):
    def __init__(
        __self__,
        *,
        disk_type: _builtins.str,
        provisioned_iops: _builtins.int,
        provisioned_throughput: _builtins.int,
        size_gb: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterNodeConfigConfidentialNodeResult(dict):
    def __init__(
        __self__, *, confidential_instance_type: _builtins.str, enabled: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceType")
    def confidential_instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodeConfigContainerdConfigResult(dict):
    def __init__(
        __self__,
        *,
        private_registry_access_configs: Sequence[
            outputs.GetClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigResult
        ],
        registry_hosts: Sequence[
            outputs.GetClusterNodeConfigContainerdConfigRegistryHostResult
        ],
        writable_cgroups: Sequence[
            outputs.GetClusterNodeConfigContainerdConfigWritableCgroupResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateRegistryAccessConfigs")
    def private_registry_access_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="registryHosts")
    def registry_hosts(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigContainerdConfigRegistryHostResult]: ...
    @_builtins.property
    @pulumi.getter(name="writableCgroups")
    def writable_cgroups(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigContainerdConfigWritableCgroupResult]: ...

@pulumi.output_type
class GetClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigResult(dict):
    def __init__(
        __self__,
        *,
        certificate_authority_domain_configs: Sequence[
            outputs.GetClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigResult
        ],
        enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityDomainConfigs")
    def certificate_authority_domain_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigResult(
    dict
):
    def __init__(
        __self__,
        *,
        fqdns: Sequence[_builtins.str],
        gcp_secret_manager_certificate_configs: Sequence[
            outputs.GetClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerCertificateConfigs")
    def gcp_secret_manager_certificate_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigResult
    ]: ...

@pulumi.output_type
class GetClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigResult(
    dict
):
    def __init__(__self__, *, secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretUri")
    def secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigContainerdConfigRegistryHostResult(dict):
    def __init__(
        __self__,
        *,
        hosts: Sequence[
            outputs.GetClusterNodeConfigContainerdConfigRegistryHostHostResult
        ],
        server: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hosts(
        self,
    ) -> Sequence[
        outputs.GetClusterNodeConfigContainerdConfigRegistryHostHostResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigContainerdConfigRegistryHostHostResult(dict):
    def __init__(
        __self__,
        *,
        capabilities: Sequence[_builtins.str],
        cas: Sequence[
            outputs.GetClusterNodeConfigContainerdConfigRegistryHostHostCaResult
        ],
        clients: Sequence[
            outputs.GetClusterNodeConfigContainerdConfigRegistryHostHostClientResult
        ],
        dial_timeout: _builtins.str,
        headers: Sequence[
            outputs.GetClusterNodeConfigContainerdConfigRegistryHostHostHeaderResult
        ],
        host: _builtins.str,
        override_path: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cas(
        self,
    ) -> Sequence[
        outputs.GetClusterNodeConfigContainerdConfigRegistryHostHostCaResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def clients(
        self,
    ) -> Sequence[
        outputs.GetClusterNodeConfigContainerdConfigRegistryHostHostClientResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dialTimeout")
    def dial_timeout(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Sequence[
        outputs.GetClusterNodeConfigContainerdConfigRegistryHostHostHeaderResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="overridePath")
    def override_path(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodeConfigContainerdConfigRegistryHostHostCaResult(dict):
    def __init__(__self__, *, gcp_secret_manager_secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigContainerdConfigRegistryHostHostClientResult(dict):
    def __init__(
        __self__,
        *,
        certs: Sequence[
            outputs.GetClusterNodeConfigContainerdConfigRegistryHostHostClientCertResult
        ],
        keys: Sequence[
            outputs.GetClusterNodeConfigContainerdConfigRegistryHostHostClientKeyResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodeConfigContainerdConfigRegistryHostHostClientCertResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def keys(
        self,
    ) -> Sequence[
        outputs.GetClusterNodeConfigContainerdConfigRegistryHostHostClientKeyResult
    ]: ...

@pulumi.output_type
class GetClusterNodeConfigContainerdConfigRegistryHostHostClientCertResult(dict):
    def __init__(__self__, *, gcp_secret_manager_secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigContainerdConfigRegistryHostHostClientKeyResult(dict):
    def __init__(__self__, *, gcp_secret_manager_secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigContainerdConfigRegistryHostHostHeaderResult(dict):
    def __init__(
        __self__, *, key: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterNodeConfigContainerdConfigWritableCgroupResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodeConfigEffectiveTaintResult(dict):
    def __init__(
        __self__, *, effect: _builtins.str, key: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigEphemeralStorageConfigResult(dict):
    def __init__(__self__, *, local_ssd_count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterNodeConfigEphemeralStorageLocalSsdConfigResult(dict):
    def __init__(
        __self__, *, data_cache_count: _builtins.int, local_ssd_count: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataCacheCount")
    def data_cache_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterNodeConfigFastSocketResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodeConfigGcfsConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodeConfigGuestAcceleratorResult(dict):
    def __init__(
        __self__,
        *,
        count: _builtins.int,
        gpu_driver_installation_configs: Sequence[
            outputs.GetClusterNodeConfigGuestAcceleratorGpuDriverInstallationConfigResult
        ],
        gpu_partition_size: _builtins.str,
        gpu_sharing_configs: Sequence[
            outputs.GetClusterNodeConfigGuestAcceleratorGpuSharingConfigResult
        ],
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverInstallationConfigs")
    def gpu_driver_installation_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodeConfigGuestAcceleratorGpuDriverInstallationConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="gpuPartitionSize")
    def gpu_partition_size(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingConfigs")
    def gpu_sharing_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodeConfigGuestAcceleratorGpuSharingConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigGuestAcceleratorGpuDriverInstallationConfigResult(dict):
    def __init__(__self__, *, gpu_driver_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverVersion")
    def gpu_driver_version(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigGuestAcceleratorGpuSharingConfigResult(dict):
    def __init__(
        __self__,
        *,
        gpu_sharing_strategy: _builtins.str,
        max_shared_clients_per_gpu: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingStrategy")
    def gpu_sharing_strategy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxSharedClientsPerGpu")
    def max_shared_clients_per_gpu(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterNodeConfigGvnicResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodeConfigHostMaintenancePolicyResult(dict):
    def __init__(__self__, *, maintenance_interval: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceInterval")
    def maintenance_interval(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigKubeletConfigResult(dict):
    def __init__(
        __self__,
        *,
        allowed_unsafe_sysctls: Sequence[_builtins.str],
        container_log_max_files: _builtins.int,
        container_log_max_size: _builtins.str,
        cpu_cfs_quota: _builtins.bool,
        cpu_cfs_quota_period: _builtins.str,
        cpu_manager_policy: _builtins.str,
        eviction_max_pod_grace_period_seconds: _builtins.int,
        eviction_minimum_reclaims: Sequence[
            outputs.GetClusterNodeConfigKubeletConfigEvictionMinimumReclaimResult
        ],
        eviction_soft_grace_periods: Sequence[
            outputs.GetClusterNodeConfigKubeletConfigEvictionSoftGracePeriodResult
        ],
        eviction_softs: Sequence[
            outputs.GetClusterNodeConfigKubeletConfigEvictionSoftResult
        ],
        image_gc_high_threshold_percent: _builtins.int,
        image_gc_low_threshold_percent: _builtins.int,
        image_maximum_gc_age: _builtins.str,
        image_minimum_gc_age: _builtins.str,
        insecure_kubelet_readonly_port_enabled: _builtins.str,
        max_parallel_image_pulls: _builtins.int,
        memory_managers: Sequence[
            outputs.GetClusterNodeConfigKubeletConfigMemoryManagerResult
        ],
        pod_pids_limit: _builtins.int,
        single_process_oom_kill: _builtins.bool,
        topology_managers: Sequence[
            outputs.GetClusterNodeConfigKubeletConfigTopologyManagerResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedUnsafeSysctls")
    def allowed_unsafe_sysctls(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxFiles")
    def container_log_max_files(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxSize")
    def container_log_max_size(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuota")
    def cpu_cfs_quota(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuotaPeriod")
    def cpu_cfs_quota_period(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cpuManagerPolicy")
    def cpu_manager_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="evictionMaxPodGracePeriodSeconds")
    def eviction_max_pod_grace_period_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="evictionMinimumReclaims")
    def eviction_minimum_reclaims(
        self,
    ) -> Sequence[
        outputs.GetClusterNodeConfigKubeletConfigEvictionMinimumReclaimResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="evictionSoftGracePeriods")
    def eviction_soft_grace_periods(
        self,
    ) -> Sequence[
        outputs.GetClusterNodeConfigKubeletConfigEvictionSoftGracePeriodResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="evictionSofts")
    def eviction_softs(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigKubeletConfigEvictionSoftResult]: ...
    @_builtins.property
    @pulumi.getter(name="imageGcHighThresholdPercent")
    def image_gc_high_threshold_percent(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="imageGcLowThresholdPercent")
    def image_gc_low_threshold_percent(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="imageMaximumGcAge")
    def image_maximum_gc_age(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageMinimumGcAge")
    def image_minimum_gc_age(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="insecureKubeletReadonlyPortEnabled")
    def insecure_kubelet_readonly_port_enabled(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxParallelImagePulls")
    def max_parallel_image_pulls(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memoryManagers")
    def memory_managers(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigKubeletConfigMemoryManagerResult]: ...
    @_builtins.property
    @pulumi.getter(name="podPidsLimit")
    def pod_pids_limit(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="singleProcessOomKill")
    def single_process_oom_kill(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="topologyManagers")
    def topology_managers(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigKubeletConfigTopologyManagerResult]: ...

@pulumi.output_type
class GetClusterNodeConfigKubeletConfigEvictionMinimumReclaimResult(dict):
    def __init__(
        __self__,
        *,
        imagefs_available: _builtins.str,
        imagefs_inodes_free: _builtins.str,
        memory_available: _builtins.str,
        nodefs_available: _builtins.str,
        nodefs_inodes_free: _builtins.str,
        pid_available: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigKubeletConfigEvictionSoftResult(dict):
    def __init__(
        __self__,
        *,
        imagefs_available: _builtins.str,
        imagefs_inodes_free: _builtins.str,
        memory_available: _builtins.str,
        nodefs_available: _builtins.str,
        nodefs_inodes_free: _builtins.str,
        pid_available: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigKubeletConfigEvictionSoftGracePeriodResult(dict):
    def __init__(
        __self__,
        *,
        imagefs_available: _builtins.str,
        imagefs_inodes_free: _builtins.str,
        memory_available: _builtins.str,
        nodefs_available: _builtins.str,
        nodefs_inodes_free: _builtins.str,
        pid_available: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigKubeletConfigMemoryManagerResult(dict):
    def __init__(__self__, *, policy: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigKubeletConfigTopologyManagerResult(dict):
    def __init__(__self__, *, policy: _builtins.str, scope: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigLinuxNodeConfigResult(dict):
    def __init__(
        __self__,
        *,
        cgroup_mode: _builtins.str,
        hugepages_configs: Sequence[
            outputs.GetClusterNodeConfigLinuxNodeConfigHugepagesConfigResult
        ],
        node_kernel_module_loadings: Sequence[
            outputs.GetClusterNodeConfigLinuxNodeConfigNodeKernelModuleLoadingResult
        ],
        sysctls: Mapping[str, _builtins.str],
        transparent_hugepage_defrag: _builtins.str,
        transparent_hugepage_enabled: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cgroupMode")
    def cgroup_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hugepagesConfigs")
    def hugepages_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigLinuxNodeConfigHugepagesConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="nodeKernelModuleLoadings")
    def node_kernel_module_loadings(
        self,
    ) -> Sequence[
        outputs.GetClusterNodeConfigLinuxNodeConfigNodeKernelModuleLoadingResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sysctls(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageDefrag")
    def transparent_hugepage_defrag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageEnabled")
    def transparent_hugepage_enabled(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigLinuxNodeConfigHugepagesConfigResult(dict):
    def __init__(
        __self__, *, hugepage_size1g: _builtins.int, hugepage_size2m: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize1g")
    def hugepage_size1g(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize2m")
    def hugepage_size2m(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterNodeConfigLinuxNodeConfigNodeKernelModuleLoadingResult(dict):
    def __init__(__self__, *, policy: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigLocalNvmeSsdBlockConfigResult(dict):
    def __init__(__self__, *, local_ssd_count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterNodeConfigReservationAffinityResult(dict):
    def __init__(
        __self__,
        *,
        consume_reservation_type: _builtins.str,
        key: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterNodeConfigSandboxConfigResult(dict):
    def __init__(
        __self__, *, sandbox_type: _builtins.str, type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sandboxType")
    def sandbox_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigSecondaryBootDiskResult(dict):
    def __init__(
        __self__, *, disk_image: _builtins.str, mode: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskImage")
    def disk_image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigShieldedInstanceConfigResult(dict):
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: _builtins.bool,
        enable_secure_boot: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodeConfigSoleTenantConfigResult(dict):
    def __init__(
        __self__,
        *,
        min_node_cpus: _builtins.int,
        node_affinities: Sequence[
            outputs.GetClusterNodeConfigSoleTenantConfigNodeAffinityResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minNodeCpus")
    def min_node_cpus(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="nodeAffinities")
    def node_affinities(
        self,
    ) -> Sequence[outputs.GetClusterNodeConfigSoleTenantConfigNodeAffinityResult]: ...

@pulumi.output_type
class GetClusterNodeConfigSoleTenantConfigNodeAffinityResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        operator: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterNodeConfigTaintResult(dict):
    def __init__(
        __self__, *, effect: _builtins.str, key: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigWindowsNodeConfigResult(dict):
    def __init__(__self__, *, osversion: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def osversion(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodeConfigWorkloadMetadataConfigResult(dict):
    def __init__(__self__, *, mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolResult(dict):
    def __init__(
        __self__,
        *,
        autoscalings: Sequence[outputs.GetClusterNodePoolAutoscalingResult],
        initial_node_count: _builtins.int,
        instance_group_urls: Sequence[_builtins.str],
        managed_instance_group_urls: Sequence[_builtins.str],
        managements: Sequence[outputs.GetClusterNodePoolManagementResult],
        max_pods_per_node: _builtins.int,
        name: _builtins.str,
        name_prefix: _builtins.str,
        network_configs: Sequence[outputs.GetClusterNodePoolNetworkConfigResult],
        node_configs: Sequence[outputs.GetClusterNodePoolNodeConfigResult],
        node_count: _builtins.int,
        node_drain_configs: Sequence[outputs.GetClusterNodePoolNodeDrainConfigResult],
        node_locations: Sequence[_builtins.str],
        placement_policies: Sequence[outputs.GetClusterNodePoolPlacementPolicyResult],
        queued_provisionings: Sequence[
            outputs.GetClusterNodePoolQueuedProvisioningResult
        ],
        upgrade_settings: Sequence[outputs.GetClusterNodePoolUpgradeSettingResult],
        version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def autoscalings(self) -> Sequence[outputs.GetClusterNodePoolAutoscalingResult]: ...
    @_builtins.property
    @pulumi.getter(name="initialNodeCount")
    def initial_node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="instanceGroupUrls")
    def instance_group_urls(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedInstanceGroupUrls")
    def managed_instance_group_urls(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def managements(self) -> Sequence[outputs.GetClusterNodePoolManagementResult]: ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkConfigs")
    def network_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNetworkConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(self) -> Sequence[outputs.GetClusterNodePoolNodeConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="nodeDrainConfigs")
    def node_drain_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeDrainConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="nodeLocations")
    def node_locations(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="placementPolicies")
    def placement_policies(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolPlacementPolicyResult]: ...
    @_builtins.property
    @pulumi.getter(name="queuedProvisionings")
    def queued_provisionings(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolQueuedProvisioningResult]: ...
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolUpgradeSettingResult]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolAutoConfigResult(dict):
    def __init__(
        __self__,
        *,
        linux_node_configs: Sequence[
            outputs.GetClusterNodePoolAutoConfigLinuxNodeConfigResult
        ],
        network_tags: Sequence[outputs.GetClusterNodePoolAutoConfigNetworkTagResult],
        node_kubelet_configs: Sequence[
            outputs.GetClusterNodePoolAutoConfigNodeKubeletConfigResult
        ],
        resource_manager_tags: Mapping[str, _builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linuxNodeConfigs")
    def linux_node_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolAutoConfigLinuxNodeConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolAutoConfigNetworkTagResult]: ...
    @_builtins.property
    @pulumi.getter(name="nodeKubeletConfigs")
    def node_kubelet_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolAutoConfigNodeKubeletConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GetClusterNodePoolAutoConfigLinuxNodeConfigResult(dict):
    def __init__(
        __self__,
        *,
        cgroup_mode: _builtins.str,
        node_kernel_module_loadings: Sequence[
            outputs.GetClusterNodePoolAutoConfigLinuxNodeConfigNodeKernelModuleLoadingResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cgroupMode")
    def cgroup_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeKernelModuleLoadings")
    def node_kernel_module_loadings(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolAutoConfigLinuxNodeConfigNodeKernelModuleLoadingResult
    ]: ...

@pulumi.output_type
class GetClusterNodePoolAutoConfigLinuxNodeConfigNodeKernelModuleLoadingResult(dict):
    def __init__(__self__, *, policy: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolAutoConfigNetworkTagResult(dict):
    def __init__(__self__, *, tags: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterNodePoolAutoConfigNodeKubeletConfigResult(dict):
    def __init__(
        __self__, *, insecure_kubelet_readonly_port_enabled: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="insecureKubeletReadonlyPortEnabled")
    def insecure_kubelet_readonly_port_enabled(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolAutoscalingResult(dict):
    def __init__(
        __self__,
        *,
        location_policy: _builtins.str,
        max_node_count: _builtins.int,
        min_node_count: _builtins.int,
        total_max_node_count: _builtins.int,
        total_min_node_count: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationPolicy")
    def location_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="totalMaxNodeCount")
    def total_max_node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="totalMinNodeCount")
    def total_min_node_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterNodePoolDefaultResult(dict):
    def __init__(
        __self__,
        *,
        node_config_defaults: Sequence[
            outputs.GetClusterNodePoolDefaultNodeConfigDefaultResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeConfigDefaults")
    def node_config_defaults(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolDefaultNodeConfigDefaultResult]: ...

@pulumi.output_type
class GetClusterNodePoolDefaultNodeConfigDefaultResult(dict):
    def __init__(
        __self__,
        *,
        containerd_configs: Sequence[
            outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigResult
        ],
        gcfs_configs: Sequence[
            outputs.GetClusterNodePoolDefaultNodeConfigDefaultGcfsConfigResult
        ],
        insecure_kubelet_readonly_port_enabled: _builtins.str,
        logging_variant: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerdConfigs")
    def containerd_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="gcfsConfigs")
    def gcfs_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolDefaultNodeConfigDefaultGcfsConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="insecureKubeletReadonlyPortEnabled")
    def insecure_kubelet_readonly_port_enabled(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="loggingVariant")
    def logging_variant(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigResult(dict):
    def __init__(
        __self__,
        *,
        private_registry_access_configs: Sequence[
            outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigPrivateRegistryAccessConfigResult
        ],
        registry_hosts: Sequence[
            outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostResult
        ],
        writable_cgroups: Sequence[
            outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigWritableCgroupResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateRegistryAccessConfigs")
    def private_registry_access_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigPrivateRegistryAccessConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="registryHosts")
    def registry_hosts(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="writableCgroups")
    def writable_cgroups(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigWritableCgroupResult
    ]: ...

@pulumi.output_type
class GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigPrivateRegistryAccessConfigResult(
    dict
):
    def __init__(
        __self__,
        *,
        certificate_authority_domain_configs: Sequence[
            outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigResult
        ],
        enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityDomainConfigs")
    def certificate_authority_domain_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigResult(
    dict
):
    def __init__(
        __self__,
        *,
        fqdns: Sequence[_builtins.str],
        gcp_secret_manager_certificate_configs: Sequence[
            outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerCertificateConfigs")
    def gcp_secret_manager_certificate_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigResult
    ]: ...

@pulumi.output_type
class GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigResult(
    dict
):
    def __init__(__self__, *, secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretUri")
    def secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostResult(
    dict
):
    def __init__(
        __self__,
        *,
        hosts: Sequence[
            outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostResult
        ],
        server: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hosts(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostResult(
    dict
):
    def __init__(
        __self__,
        *,
        capabilities: Sequence[_builtins.str],
        cas: Sequence[
            outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostCaResult
        ],
        clients: Sequence[
            outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostClientResult
        ],
        dial_timeout: _builtins.str,
        headers: Sequence[
            outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostHeaderResult
        ],
        host: _builtins.str,
        override_path: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cas(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostCaResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def clients(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostClientResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dialTimeout")
    def dial_timeout(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostHeaderResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="overridePath")
    def override_path(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostCaResult(
    dict
):
    def __init__(__self__, *, gcp_secret_manager_secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostClientResult(
    dict
):
    def __init__(
        __self__,
        *,
        certs: Sequence[
            outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostClientCertResult
        ],
        keys: Sequence[
            outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostClientKeyResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostClientCertResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def keys(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostClientKeyResult
    ]: ...

@pulumi.output_type
class GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostClientCertResult(
    dict
):
    def __init__(__self__, *, gcp_secret_manager_secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostClientKeyResult(
    dict
):
    def __init__(__self__, *, gcp_secret_manager_secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigRegistryHostHostHeaderResult(
    dict
):
    def __init__(
        __self__, *, key: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterNodePoolDefaultNodeConfigDefaultContainerdConfigWritableCgroupResult(
    dict
):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolDefaultNodeConfigDefaultGcfsConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolManagementResult(dict):
    def __init__(
        __self__, *, auto_repair: _builtins.bool, auto_upgrade: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRepair")
    def auto_repair(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="autoUpgrade")
    def auto_upgrade(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolNetworkConfigResult(dict):
    def __init__(
        __self__,
        *,
        accelerator_network_profile: _builtins.str,
        additional_node_network_configs: Sequence[
            outputs.GetClusterNodePoolNetworkConfigAdditionalNodeNetworkConfigResult
        ],
        additional_pod_network_configs: Sequence[
            outputs.GetClusterNodePoolNetworkConfigAdditionalPodNetworkConfigResult
        ],
        create_pod_range: _builtins.bool,
        enable_private_nodes: _builtins.bool,
        network_performance_configs: Sequence[
            outputs.GetClusterNodePoolNetworkConfigNetworkPerformanceConfigResult
        ],
        pod_cidr_overprovision_configs: Sequence[
            outputs.GetClusterNodePoolNetworkConfigPodCidrOverprovisionConfigResult
        ],
        pod_ipv4_cidr_block: _builtins.str,
        pod_range: _builtins.str,
        subnetwork: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorNetworkProfile")
    def accelerator_network_profile(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalNodeNetworkConfigs")
    def additional_node_network_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNetworkConfigAdditionalNodeNetworkConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="additionalPodNetworkConfigs")
    def additional_pod_network_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNetworkConfigAdditionalPodNetworkConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="createPodRange")
    def create_pod_range(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateNodes")
    def enable_private_nodes(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfigs")
    def network_performance_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNetworkConfigNetworkPerformanceConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="podCidrOverprovisionConfigs")
    def pod_cidr_overprovision_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNetworkConfigPodCidrOverprovisionConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="podIpv4CidrBlock")
    def pod_ipv4_cidr_block(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="podRange")
    def pod_range(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNetworkConfigAdditionalNodeNetworkConfigResult(dict):
    def __init__(
        __self__, *, network: _builtins.str, subnetwork: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNetworkConfigAdditionalPodNetworkConfigResult(dict):
    def __init__(
        __self__,
        *,
        max_pods_per_node: _builtins.int,
        secondary_pod_range: _builtins.str,
        subnetwork: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="secondaryPodRange")
    def secondary_pod_range(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNetworkConfigNetworkPerformanceConfigResult(dict):
    def __init__(__self__, *, total_egress_bandwidth_tier: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="totalEgressBandwidthTier")
    def total_egress_bandwidth_tier(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNetworkConfigPodCidrOverprovisionConfigResult(dict):
    def __init__(__self__, *, disabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigResult(dict):
    def __init__(
        __self__,
        *,
        advanced_machine_features: Sequence[
            outputs.GetClusterNodePoolNodeConfigAdvancedMachineFeatureResult
        ],
        boot_disk_kms_key: _builtins.str,
        boot_disks: Sequence[outputs.GetClusterNodePoolNodeConfigBootDiskResult],
        confidential_nodes: Sequence[
            outputs.GetClusterNodePoolNodeConfigConfidentialNodeResult
        ],
        containerd_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigContainerdConfigResult
        ],
        disk_size_gb: _builtins.int,
        disk_type: _builtins.str,
        effective_taints: Sequence[
            outputs.GetClusterNodePoolNodeConfigEffectiveTaintResult
        ],
        enable_confidential_storage: _builtins.bool,
        ephemeral_storage_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigEphemeralStorageConfigResult
        ],
        ephemeral_storage_local_ssd_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigEphemeralStorageLocalSsdConfigResult
        ],
        fast_sockets: Sequence[outputs.GetClusterNodePoolNodeConfigFastSocketResult],
        flex_start: _builtins.bool,
        gcfs_configs: Sequence[outputs.GetClusterNodePoolNodeConfigGcfsConfigResult],
        guest_accelerators: Sequence[
            outputs.GetClusterNodePoolNodeConfigGuestAcceleratorResult
        ],
        gvnics: Sequence[outputs.GetClusterNodePoolNodeConfigGvnicResult],
        host_maintenance_policies: Sequence[
            outputs.GetClusterNodePoolNodeConfigHostMaintenancePolicyResult
        ],
        image_type: _builtins.str,
        kubelet_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigKubeletConfigResult
        ],
        labels: Mapping[str, _builtins.str],
        linux_node_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigLinuxNodeConfigResult
        ],
        local_nvme_ssd_block_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigLocalNvmeSsdBlockConfigResult
        ],
        local_ssd_count: _builtins.int,
        local_ssd_encryption_mode: _builtins.str,
        logging_variant: _builtins.str,
        machine_type: _builtins.str,
        max_run_duration: _builtins.str,
        metadata: Mapping[str, _builtins.str],
        min_cpu_platform: _builtins.str,
        node_group: _builtins.str,
        oauth_scopes: Sequence[_builtins.str],
        preemptible: _builtins.bool,
        reservation_affinities: Sequence[
            outputs.GetClusterNodePoolNodeConfigReservationAffinityResult
        ],
        resource_labels: Mapping[str, _builtins.str],
        resource_manager_tags: Mapping[str, _builtins.str],
        sandbox_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigSandboxConfigResult
        ],
        secondary_boot_disks: Sequence[
            outputs.GetClusterNodePoolNodeConfigSecondaryBootDiskResult
        ],
        service_account: _builtins.str,
        shielded_instance_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigShieldedInstanceConfigResult
        ],
        sole_tenant_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigSoleTenantConfigResult
        ],
        spot: _builtins.bool,
        storage_pools: Sequence[_builtins.str],
        tags: Sequence[_builtins.str],
        taints: Sequence[outputs.GetClusterNodePoolNodeConfigTaintResult],
        windows_node_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigWindowsNodeConfigResult
        ],
        workload_metadata_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigWorkloadMetadataConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigAdvancedMachineFeatureResult]: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskKmsKey")
    def boot_disk_kms_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bootDisks")
    def boot_disks(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigBootDiskResult]: ...
    @_builtins.property
    @pulumi.getter(name="confidentialNodes")
    def confidential_nodes(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigConfidentialNodeResult]: ...
    @_builtins.property
    @pulumi.getter(name="containerdConfigs")
    def containerd_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigContainerdConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveTaints")
    def effective_taints(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigEffectiveTaintResult]: ...
    @_builtins.property
    @pulumi.getter(name="enableConfidentialStorage")
    def enable_confidential_storage(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageConfigs")
    def ephemeral_storage_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigEphemeralStorageConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageLocalSsdConfigs")
    def ephemeral_storage_local_ssd_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigEphemeralStorageLocalSsdConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="fastSockets")
    def fast_sockets(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigFastSocketResult]: ...
    @_builtins.property
    @pulumi.getter(name="flexStart")
    def flex_start(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="gcfsConfigs")
    def gcfs_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigGcfsConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigGuestAcceleratorResult]: ...
    @_builtins.property
    @pulumi.getter
    def gvnics(self) -> Sequence[outputs.GetClusterNodePoolNodeConfigGvnicResult]: ...
    @_builtins.property
    @pulumi.getter(name="hostMaintenancePolicies")
    def host_maintenance_policies(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigHostMaintenancePolicyResult]: ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kubeletConfigs")
    def kubelet_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigKubeletConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linuxNodeConfigs")
    def linux_node_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigLinuxNodeConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="localNvmeSsdBlockConfigs")
    def local_nvme_ssd_block_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigLocalNvmeSsdBlockConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="localSsdEncryptionMode")
    def local_ssd_encryption_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="loggingVariant")
    def logging_variant(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxRunDuration")
    def max_run_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeGroup")
    def node_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def preemptible(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinities")
    def reservation_affinities(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigReservationAffinityResult]: ...
    @_builtins.property
    @pulumi.getter(name="resourceLabels")
    def resource_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sandboxConfigs")
    def sandbox_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigSandboxConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryBootDisks")
    def secondary_boot_disks(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigSecondaryBootDiskResult]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfigs")
    def shielded_instance_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigShieldedInstanceConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="soleTenantConfigs")
    def sole_tenant_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigSoleTenantConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def spot(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="storagePools")
    def storage_pools(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def taints(self) -> Sequence[outputs.GetClusterNodePoolNodeConfigTaintResult]: ...
    @_builtins.property
    @pulumi.getter(name="windowsNodeConfigs")
    def windows_node_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigWindowsNodeConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="workloadMetadataConfigs")
    def workload_metadata_configs(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolNodeConfigWorkloadMetadataConfigResult]: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigAdvancedMachineFeatureResult(dict):
    def __init__(
        __self__,
        *,
        enable_nested_virtualization: _builtins.bool,
        performance_monitoring_unit: _builtins.str,
        threads_per_core: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="performanceMonitoringUnit")
    def performance_monitoring_unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigBootDiskResult(dict):
    def __init__(
        __self__,
        *,
        disk_type: _builtins.str,
        provisioned_iops: _builtins.int,
        provisioned_throughput: _builtins.int,
        size_gb: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigConfidentialNodeResult(dict):
    def __init__(
        __self__, *, confidential_instance_type: _builtins.str, enabled: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceType")
    def confidential_instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigContainerdConfigResult(dict):
    def __init__(
        __self__,
        *,
        private_registry_access_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigResult
        ],
        registry_hosts: Sequence[
            outputs.GetClusterNodePoolNodeConfigContainerdConfigRegistryHostResult
        ],
        writable_cgroups: Sequence[
            outputs.GetClusterNodePoolNodeConfigContainerdConfigWritableCgroupResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateRegistryAccessConfigs")
    def private_registry_access_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="registryHosts")
    def registry_hosts(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigContainerdConfigRegistryHostResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="writableCgroups")
    def writable_cgroups(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigContainerdConfigWritableCgroupResult
    ]: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigResult(
    dict
):
    def __init__(
        __self__,
        *,
        certificate_authority_domain_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigResult
        ],
        enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityDomainConfigs")
    def certificate_authority_domain_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigResult(
    dict
):
    def __init__(
        __self__,
        *,
        fqdns: Sequence[_builtins.str],
        gcp_secret_manager_certificate_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerCertificateConfigs")
    def gcp_secret_manager_certificate_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigResult
    ]: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigResult(
    dict
):
    def __init__(__self__, *, secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretUri")
    def secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigContainerdConfigRegistryHostResult(dict):
    def __init__(
        __self__,
        *,
        hosts: Sequence[
            outputs.GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostResult
        ],
        server: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hosts(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostResult(dict):
    def __init__(
        __self__,
        *,
        capabilities: Sequence[_builtins.str],
        cas: Sequence[
            outputs.GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostCaResult
        ],
        clients: Sequence[
            outputs.GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientResult
        ],
        dial_timeout: _builtins.str,
        headers: Sequence[
            outputs.GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostHeaderResult
        ],
        host: _builtins.str,
        override_path: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cas(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostCaResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def clients(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dialTimeout")
    def dial_timeout(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostHeaderResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="overridePath")
    def override_path(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostCaResult(dict):
    def __init__(__self__, *, gcp_secret_manager_secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientResult(dict):
    def __init__(
        __self__,
        *,
        certs: Sequence[
            outputs.GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientCertResult
        ],
        keys: Sequence[
            outputs.GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientKeyResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientCertResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def keys(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientKeyResult
    ]: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientCertResult(
    dict
):
    def __init__(__self__, *, gcp_secret_manager_secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientKeyResult(dict):
    def __init__(__self__, *, gcp_secret_manager_secret_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigContainerdConfigRegistryHostHostHeaderResult(dict):
    def __init__(
        __self__, *, key: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigContainerdConfigWritableCgroupResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigEffectiveTaintResult(dict):
    def __init__(
        __self__, *, effect: _builtins.str, key: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigEphemeralStorageConfigResult(dict):
    def __init__(__self__, *, local_ssd_count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigEphemeralStorageLocalSsdConfigResult(dict):
    def __init__(
        __self__, *, data_cache_count: _builtins.int, local_ssd_count: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataCacheCount")
    def data_cache_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigFastSocketResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigGcfsConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigGuestAcceleratorResult(dict):
    def __init__(
        __self__,
        *,
        count: _builtins.int,
        gpu_driver_installation_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfigResult
        ],
        gpu_partition_size: _builtins.str,
        gpu_sharing_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigGuestAcceleratorGpuSharingConfigResult
        ],
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverInstallationConfigs")
    def gpu_driver_installation_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="gpuPartitionSize")
    def gpu_partition_size(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingConfigs")
    def gpu_sharing_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigGuestAcceleratorGpuSharingConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfigResult(
    dict
):
    def __init__(__self__, *, gpu_driver_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverVersion")
    def gpu_driver_version(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigGuestAcceleratorGpuSharingConfigResult(dict):
    def __init__(
        __self__,
        *,
        gpu_sharing_strategy: _builtins.str,
        max_shared_clients_per_gpu: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingStrategy")
    def gpu_sharing_strategy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxSharedClientsPerGpu")
    def max_shared_clients_per_gpu(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigGvnicResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigHostMaintenancePolicyResult(dict):
    def __init__(__self__, *, maintenance_interval: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceInterval")
    def maintenance_interval(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigKubeletConfigResult(dict):
    def __init__(
        __self__,
        *,
        allowed_unsafe_sysctls: Sequence[_builtins.str],
        container_log_max_files: _builtins.int,
        container_log_max_size: _builtins.str,
        cpu_cfs_quota: _builtins.bool,
        cpu_cfs_quota_period: _builtins.str,
        cpu_manager_policy: _builtins.str,
        eviction_max_pod_grace_period_seconds: _builtins.int,
        eviction_minimum_reclaims: Sequence[
            outputs.GetClusterNodePoolNodeConfigKubeletConfigEvictionMinimumReclaimResult
        ],
        eviction_soft_grace_periods: Sequence[
            outputs.GetClusterNodePoolNodeConfigKubeletConfigEvictionSoftGracePeriodResult
        ],
        eviction_softs: Sequence[
            outputs.GetClusterNodePoolNodeConfigKubeletConfigEvictionSoftResult
        ],
        image_gc_high_threshold_percent: _builtins.int,
        image_gc_low_threshold_percent: _builtins.int,
        image_maximum_gc_age: _builtins.str,
        image_minimum_gc_age: _builtins.str,
        insecure_kubelet_readonly_port_enabled: _builtins.str,
        max_parallel_image_pulls: _builtins.int,
        memory_managers: Sequence[
            outputs.GetClusterNodePoolNodeConfigKubeletConfigMemoryManagerResult
        ],
        pod_pids_limit: _builtins.int,
        single_process_oom_kill: _builtins.bool,
        topology_managers: Sequence[
            outputs.GetClusterNodePoolNodeConfigKubeletConfigTopologyManagerResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedUnsafeSysctls")
    def allowed_unsafe_sysctls(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxFiles")
    def container_log_max_files(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxSize")
    def container_log_max_size(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuota")
    def cpu_cfs_quota(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuotaPeriod")
    def cpu_cfs_quota_period(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cpuManagerPolicy")
    def cpu_manager_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="evictionMaxPodGracePeriodSeconds")
    def eviction_max_pod_grace_period_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="evictionMinimumReclaims")
    def eviction_minimum_reclaims(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigKubeletConfigEvictionMinimumReclaimResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="evictionSoftGracePeriods")
    def eviction_soft_grace_periods(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigKubeletConfigEvictionSoftGracePeriodResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="evictionSofts")
    def eviction_softs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigKubeletConfigEvictionSoftResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="imageGcHighThresholdPercent")
    def image_gc_high_threshold_percent(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="imageGcLowThresholdPercent")
    def image_gc_low_threshold_percent(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="imageMaximumGcAge")
    def image_maximum_gc_age(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageMinimumGcAge")
    def image_minimum_gc_age(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="insecureKubeletReadonlyPortEnabled")
    def insecure_kubelet_readonly_port_enabled(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxParallelImagePulls")
    def max_parallel_image_pulls(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memoryManagers")
    def memory_managers(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigKubeletConfigMemoryManagerResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="podPidsLimit")
    def pod_pids_limit(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="singleProcessOomKill")
    def single_process_oom_kill(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="topologyManagers")
    def topology_managers(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigKubeletConfigTopologyManagerResult
    ]: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigKubeletConfigEvictionMinimumReclaimResult(dict):
    def __init__(
        __self__,
        *,
        imagefs_available: _builtins.str,
        imagefs_inodes_free: _builtins.str,
        memory_available: _builtins.str,
        nodefs_available: _builtins.str,
        nodefs_inodes_free: _builtins.str,
        pid_available: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigKubeletConfigEvictionSoftResult(dict):
    def __init__(
        __self__,
        *,
        imagefs_available: _builtins.str,
        imagefs_inodes_free: _builtins.str,
        memory_available: _builtins.str,
        nodefs_available: _builtins.str,
        nodefs_inodes_free: _builtins.str,
        pid_available: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigKubeletConfigEvictionSoftGracePeriodResult(dict):
    def __init__(
        __self__,
        *,
        imagefs_available: _builtins.str,
        imagefs_inodes_free: _builtins.str,
        memory_available: _builtins.str,
        nodefs_available: _builtins.str,
        nodefs_inodes_free: _builtins.str,
        pid_available: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigKubeletConfigMemoryManagerResult(dict):
    def __init__(__self__, *, policy: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigKubeletConfigTopologyManagerResult(dict):
    def __init__(__self__, *, policy: _builtins.str, scope: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigLinuxNodeConfigResult(dict):
    def __init__(
        __self__,
        *,
        cgroup_mode: _builtins.str,
        hugepages_configs: Sequence[
            outputs.GetClusterNodePoolNodeConfigLinuxNodeConfigHugepagesConfigResult
        ],
        node_kernel_module_loadings: Sequence[
            outputs.GetClusterNodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoadingResult
        ],
        sysctls: Mapping[str, _builtins.str],
        transparent_hugepage_defrag: _builtins.str,
        transparent_hugepage_enabled: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cgroupMode")
    def cgroup_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hugepagesConfigs")
    def hugepages_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigLinuxNodeConfigHugepagesConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="nodeKernelModuleLoadings")
    def node_kernel_module_loadings(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoadingResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sysctls(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageDefrag")
    def transparent_hugepage_defrag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageEnabled")
    def transparent_hugepage_enabled(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigLinuxNodeConfigHugepagesConfigResult(dict):
    def __init__(
        __self__, *, hugepage_size1g: _builtins.int, hugepage_size2m: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize1g")
    def hugepage_size1g(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize2m")
    def hugepage_size2m(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoadingResult(dict):
    def __init__(__self__, *, policy: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigLocalNvmeSsdBlockConfigResult(dict):
    def __init__(__self__, *, local_ssd_count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigReservationAffinityResult(dict):
    def __init__(
        __self__,
        *,
        consume_reservation_type: _builtins.str,
        key: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigSandboxConfigResult(dict):
    def __init__(
        __self__, *, sandbox_type: _builtins.str, type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sandboxType")
    def sandbox_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigSecondaryBootDiskResult(dict):
    def __init__(
        __self__, *, disk_image: _builtins.str, mode: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskImage")
    def disk_image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigShieldedInstanceConfigResult(dict):
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: _builtins.bool,
        enable_secure_boot: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigSoleTenantConfigResult(dict):
    def __init__(
        __self__,
        *,
        min_node_cpus: _builtins.int,
        node_affinities: Sequence[
            outputs.GetClusterNodePoolNodeConfigSoleTenantConfigNodeAffinityResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minNodeCpus")
    def min_node_cpus(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="nodeAffinities")
    def node_affinities(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolNodeConfigSoleTenantConfigNodeAffinityResult
    ]: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigSoleTenantConfigNodeAffinityResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        operator: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigTaintResult(dict):
    def __init__(
        __self__, *, effect: _builtins.str, key: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigWindowsNodeConfigResult(dict):
    def __init__(__self__, *, osversion: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def osversion(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeConfigWorkloadMetadataConfigResult(dict):
    def __init__(__self__, *, mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolNodeDrainConfigResult(dict):
    def __init__(
        __self__, *, respect_pdb_during_node_pool_deletion: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="respectPdbDuringNodePoolDeletion")
    def respect_pdb_during_node_pool_deletion(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolPlacementPolicyResult(dict):
    def __init__(
        __self__,
        *,
        policy_name: _builtins.str,
        tpu_topology: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tpuTopology")
    def tpu_topology(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolQueuedProvisioningResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterNodePoolUpgradeSettingResult(dict):
    def __init__(
        __self__,
        *,
        blue_green_settings: Sequence[
            outputs.GetClusterNodePoolUpgradeSettingBlueGreenSettingResult
        ],
        max_surge: _builtins.int,
        max_unavailable: _builtins.int,
        strategy: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blueGreenSettings")
    def blue_green_settings(
        self,
    ) -> Sequence[outputs.GetClusterNodePoolUpgradeSettingBlueGreenSettingResult]: ...
    @_builtins.property
    @pulumi.getter(name="maxSurge")
    def max_surge(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxUnavailable")
    def max_unavailable(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def strategy(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolUpgradeSettingBlueGreenSettingResult(dict):
    def __init__(
        __self__,
        *,
        autoscaled_rollout_policies: Sequence[
            outputs.GetClusterNodePoolUpgradeSettingBlueGreenSettingAutoscaledRolloutPolicyResult
        ],
        node_pool_soak_duration: _builtins.str,
        standard_rollout_policies: Sequence[
            outputs.GetClusterNodePoolUpgradeSettingBlueGreenSettingStandardRolloutPolicyResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscaledRolloutPolicies")
    def autoscaled_rollout_policies(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolUpgradeSettingBlueGreenSettingAutoscaledRolloutPolicyResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="nodePoolSoakDuration")
    def node_pool_soak_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="standardRolloutPolicies")
    def standard_rollout_policies(
        self,
    ) -> Sequence[
        outputs.GetClusterNodePoolUpgradeSettingBlueGreenSettingStandardRolloutPolicyResult
    ]: ...

@pulumi.output_type
class GetClusterNodePoolUpgradeSettingBlueGreenSettingAutoscaledRolloutPolicyResult(
    dict
):
    def __init__(__self__, *, wait_for_drain_duration: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="waitForDrainDuration")
    def wait_for_drain_duration(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNodePoolUpgradeSettingBlueGreenSettingStandardRolloutPolicyResult(dict):
    def __init__(
        __self__,
        *,
        batch_node_count: _builtins.int,
        batch_percentage: _builtins.float,
        batch_soak_duration: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchNodeCount")
    def batch_node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="batchPercentage")
    def batch_percentage(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="batchSoakDuration")
    def batch_soak_duration(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNotificationConfigResult(dict):
    def __init__(
        __self__, *, pubsubs: Sequence[outputs.GetClusterNotificationConfigPubsubResult]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pubsubs(self) -> Sequence[outputs.GetClusterNotificationConfigPubsubResult]: ...

@pulumi.output_type
class GetClusterNotificationConfigPubsubResult(dict):
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        filters: Sequence[outputs.GetClusterNotificationConfigPubsubFilterResult],
        topic: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Sequence[outputs.GetClusterNotificationConfigPubsubFilterResult]: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterNotificationConfigPubsubFilterResult(dict):
    def __init__(__self__, *, event_types: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventTypes")
    def event_types(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterPodAutoscalingResult(dict):
    def __init__(__self__, *, hpa_profile: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hpaProfile")
    def hpa_profile(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterPodSecurityPolicyConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterPrivateClusterConfigResult(dict):
    def __init__(
        __self__,
        *,
        enable_private_endpoint: _builtins.bool,
        enable_private_nodes: _builtins.bool,
        master_global_access_configs: Sequence[
            outputs.GetClusterPrivateClusterConfigMasterGlobalAccessConfigResult
        ],
        master_ipv4_cidr_block: _builtins.str,
        peering_name: _builtins.str,
        private_endpoint: _builtins.str,
        private_endpoint_subnetwork: _builtins.str,
        public_endpoint: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateEndpoint")
    def enable_private_endpoint(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateNodes")
    def enable_private_nodes(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="masterGlobalAccessConfigs")
    def master_global_access_configs(
        self,
    ) -> Sequence[
        outputs.GetClusterPrivateClusterConfigMasterGlobalAccessConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="masterIpv4CidrBlock")
    def master_ipv4_cidr_block(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peeringName")
    def peering_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointSubnetwork")
    def private_endpoint_subnetwork(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicEndpoint")
    def public_endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterPrivateClusterConfigMasterGlobalAccessConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterProtectConfigResult(dict):
    def __init__(
        __self__,
        *,
        workload_configs: Sequence[outputs.GetClusterProtectConfigWorkloadConfigResult],
        workload_vulnerability_mode: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workloadConfigs")
    def workload_configs(
        self,
    ) -> Sequence[outputs.GetClusterProtectConfigWorkloadConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="workloadVulnerabilityMode")
    def workload_vulnerability_mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterProtectConfigWorkloadConfigResult(dict):
    def __init__(__self__, *, audit_mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditMode")
    def audit_mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterRbacBindingConfigResult(dict):
    def __init__(
        __self__,
        *,
        enable_insecure_binding_system_authenticated: _builtins.bool,
        enable_insecure_binding_system_unauthenticated: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableInsecureBindingSystemAuthenticated")
    def enable_insecure_binding_system_authenticated(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableInsecureBindingSystemUnauthenticated")
    def enable_insecure_binding_system_unauthenticated(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterReleaseChannelResult(dict):
    def __init__(__self__, *, channel: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterResourceUsageExportConfigResult(dict):
    def __init__(
        __self__,
        *,
        bigquery_destinations: Sequence[
            outputs.GetClusterResourceUsageExportConfigBigqueryDestinationResult
        ],
        enable_network_egress_metering: _builtins.bool,
        enable_resource_consumption_metering: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryDestinations")
    def bigquery_destinations(
        self,
    ) -> Sequence[
        outputs.GetClusterResourceUsageExportConfigBigqueryDestinationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableNetworkEgressMetering")
    def enable_network_egress_metering(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableResourceConsumptionMetering")
    def enable_resource_consumption_metering(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterResourceUsageExportConfigBigqueryDestinationResult(dict):
    def __init__(__self__, *, dataset_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterSecretManagerConfigResult(dict):
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        rotation_configs: Sequence[
            outputs.GetClusterSecretManagerConfigRotationConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="rotationConfigs")
    def rotation_configs(
        self,
    ) -> Sequence[outputs.GetClusterSecretManagerConfigRotationConfigResult]: ...

@pulumi.output_type
class GetClusterSecretManagerConfigRotationConfigResult(dict):
    def __init__(
        __self__, *, enabled: _builtins.bool, rotation_interval: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="rotationInterval")
    def rotation_interval(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterSecretSyncConfigResult(dict):
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        rotation_configs: Sequence[
            outputs.GetClusterSecretSyncConfigRotationConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="rotationConfigs")
    def rotation_configs(
        self,
    ) -> Sequence[outputs.GetClusterSecretSyncConfigRotationConfigResult]: ...

@pulumi.output_type
class GetClusterSecretSyncConfigRotationConfigResult(dict):
    def __init__(
        __self__, *, enabled: _builtins.bool, rotation_interval: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="rotationInterval")
    def rotation_interval(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterSecurityPostureConfigResult(dict):
    def __init__(
        __self__, *, mode: _builtins.str, vulnerability_mode: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vulnerabilityMode")
    def vulnerability_mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterServiceExternalIpsConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterTpuConfigResult(dict):
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        ipv4_cidr_block: _builtins.str,
        use_service_networking: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ipv4CidrBlock")
    def ipv4_cidr_block(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="useServiceNetworking")
    def use_service_networking(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterUserManagedKeysConfigResult(dict):
    def __init__(
        __self__,
        *,
        aggregation_ca: _builtins.str,
        cluster_ca: _builtins.str,
        control_plane_disk_encryption_key: _builtins.str,
        control_plane_disk_encryption_key_versions: Sequence[_builtins.str],
        etcd_api_ca: _builtins.str,
        etcd_peer_ca: _builtins.str,
        gkeops_etcd_backup_encryption_key: _builtins.str,
        service_account_signing_keys: Sequence[_builtins.str],
        service_account_verification_keys: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aggregationCa")
    def aggregation_ca(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterCa")
    def cluster_ca(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneDiskEncryptionKey")
    def control_plane_disk_encryption_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneDiskEncryptionKeyVersions")
    def control_plane_disk_encryption_key_versions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="etcdApiCa")
    def etcd_api_ca(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="etcdPeerCa")
    def etcd_peer_ca(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gkeopsEtcdBackupEncryptionKey")
    def gkeops_etcd_backup_encryption_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountSigningKeys")
    def service_account_signing_keys(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountVerificationKeys")
    def service_account_verification_keys(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterVerticalPodAutoscalingResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterWorkloadAltsConfigResult(dict):
    def __init__(__self__, *, enable_alts: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableAlts")
    def enable_alts(self) -> _builtins.bool: ...

@pulumi.output_type
class GetClusterWorkloadIdentityConfigResult(dict):
    def __init__(__self__, *, workload_pool: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workloadPool")
    def workload_pool(self) -> _builtins.str: ...
