import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AttachedClusterAuthorizationArgs",
    "AttachedClusterAuthorizationArgsDict",
    "AttachedClusterBinaryAuthorizationArgs",
    "AttachedClusterBinaryAuthorizationArgsDict",
    "AttachedClusterErrorArgs",
    "AttachedClusterErrorArgsDict",
    "AttachedClusterFleetArgs",
    "AttachedClusterFleetArgsDict",
    "AttachedClusterLoggingConfigArgs",
    "AttachedClusterLoggingConfigArgsDict",
    "AttachedClusterLoggingConfigComponentConfigArgs",
    ...,
    "AttachedClusterMonitoringConfigArgs",
    "AttachedClusterMonitoringConfigArgsDict",
    ...,
    ...,
    "AttachedClusterOidcConfigArgs",
    "AttachedClusterOidcConfigArgsDict",
    "AttachedClusterProxyConfigArgs",
    "AttachedClusterProxyConfigArgsDict",
    "AttachedClusterProxyConfigKubernetesSecretArgs",
    "AttachedClusterProxyConfigKubernetesSecretArgsDict",
    "AttachedClusterSecurityPostureConfigArgs",
    "AttachedClusterSecurityPostureConfigArgsDict",
    "AttachedClusterWorkloadIdentityConfigArgs",
    "AttachedClusterWorkloadIdentityConfigArgsDict",
    "AwsClusterAuthorizationArgs",
    "AwsClusterAuthorizationArgsDict",
    "AwsClusterAuthorizationAdminGroupArgs",
    "AwsClusterAuthorizationAdminGroupArgsDict",
    "AwsClusterAuthorizationAdminUserArgs",
    "AwsClusterAuthorizationAdminUserArgsDict",
    "AwsClusterBinaryAuthorizationArgs",
    "AwsClusterBinaryAuthorizationArgsDict",
    "AwsClusterControlPlaneArgs",
    "AwsClusterControlPlaneArgsDict",
    ...,
    ...,
    "AwsClusterControlPlaneConfigEncryptionArgs",
    "AwsClusterControlPlaneConfigEncryptionArgsDict",
    "AwsClusterControlPlaneDatabaseEncryptionArgs",
    "AwsClusterControlPlaneDatabaseEncryptionArgsDict",
    "AwsClusterControlPlaneInstancePlacementArgs",
    "AwsClusterControlPlaneInstancePlacementArgsDict",
    "AwsClusterControlPlaneMainVolumeArgs",
    "AwsClusterControlPlaneMainVolumeArgsDict",
    "AwsClusterControlPlaneProxyConfigArgs",
    "AwsClusterControlPlaneProxyConfigArgsDict",
    "AwsClusterControlPlaneRootVolumeArgs",
    "AwsClusterControlPlaneRootVolumeArgsDict",
    "AwsClusterControlPlaneSshConfigArgs",
    "AwsClusterControlPlaneSshConfigArgsDict",
    "AwsClusterFleetArgs",
    "AwsClusterFleetArgsDict",
    "AwsClusterLoggingConfigArgs",
    "AwsClusterLoggingConfigArgsDict",
    "AwsClusterLoggingConfigComponentConfigArgs",
    "AwsClusterLoggingConfigComponentConfigArgsDict",
    "AwsClusterNetworkingArgs",
    "AwsClusterNetworkingArgsDict",
    "AwsClusterWorkloadIdentityConfigArgs",
    "AwsClusterWorkloadIdentityConfigArgsDict",
    "AwsNodePoolAutoscalingArgs",
    "AwsNodePoolAutoscalingArgsDict",
    "AwsNodePoolConfigArgs",
    "AwsNodePoolConfigArgsDict",
    "AwsNodePoolConfigAutoscalingMetricsCollectionArgs",
    ...,
    "AwsNodePoolConfigConfigEncryptionArgs",
    "AwsNodePoolConfigConfigEncryptionArgsDict",
    "AwsNodePoolConfigInstancePlacementArgs",
    "AwsNodePoolConfigInstancePlacementArgsDict",
    "AwsNodePoolConfigProxyConfigArgs",
    "AwsNodePoolConfigProxyConfigArgsDict",
    "AwsNodePoolConfigRootVolumeArgs",
    "AwsNodePoolConfigRootVolumeArgsDict",
    "AwsNodePoolConfigSpotConfigArgs",
    "AwsNodePoolConfigSpotConfigArgsDict",
    "AwsNodePoolConfigSshConfigArgs",
    "AwsNodePoolConfigSshConfigArgsDict",
    "AwsNodePoolConfigTaintArgs",
    "AwsNodePoolConfigTaintArgsDict",
    "AwsNodePoolKubeletConfigArgs",
    "AwsNodePoolKubeletConfigArgsDict",
    "AwsNodePoolManagementArgs",
    "AwsNodePoolManagementArgsDict",
    "AwsNodePoolMaxPodsConstraintArgs",
    "AwsNodePoolMaxPodsConstraintArgsDict",
    "AwsNodePoolUpdateSettingsArgs",
    "AwsNodePoolUpdateSettingsArgsDict",
    "AwsNodePoolUpdateSettingsSurgeSettingsArgs",
    "AwsNodePoolUpdateSettingsSurgeSettingsArgsDict",
    "AzureClusterAuthorizationArgs",
    "AzureClusterAuthorizationArgsDict",
    "AzureClusterAuthorizationAdminGroupArgs",
    "AzureClusterAuthorizationAdminGroupArgsDict",
    "AzureClusterAuthorizationAdminUserArgs",
    "AzureClusterAuthorizationAdminUserArgsDict",
    "AzureClusterAzureServicesAuthenticationArgs",
    "AzureClusterAzureServicesAuthenticationArgsDict",
    "AzureClusterControlPlaneArgs",
    "AzureClusterControlPlaneArgsDict",
    "AzureClusterControlPlaneDatabaseEncryptionArgs",
    "AzureClusterControlPlaneDatabaseEncryptionArgsDict",
    "AzureClusterControlPlaneMainVolumeArgs",
    "AzureClusterControlPlaneMainVolumeArgsDict",
    "AzureClusterControlPlaneProxyConfigArgs",
    "AzureClusterControlPlaneProxyConfigArgsDict",
    "AzureClusterControlPlaneReplicaPlacementArgs",
    "AzureClusterControlPlaneReplicaPlacementArgsDict",
    "AzureClusterControlPlaneRootVolumeArgs",
    "AzureClusterControlPlaneRootVolumeArgsDict",
    "AzureClusterControlPlaneSshConfigArgs",
    "AzureClusterControlPlaneSshConfigArgsDict",
    "AzureClusterFleetArgs",
    "AzureClusterFleetArgsDict",
    "AzureClusterLoggingConfigArgs",
    "AzureClusterLoggingConfigArgsDict",
    "AzureClusterLoggingConfigComponentConfigArgs",
    "AzureClusterLoggingConfigComponentConfigArgsDict",
    "AzureClusterNetworkingArgs",
    "AzureClusterNetworkingArgsDict",
    "AzureClusterWorkloadIdentityConfigArgs",
    "AzureClusterWorkloadIdentityConfigArgsDict",
    "AzureNodePoolAutoscalingArgs",
    "AzureNodePoolAutoscalingArgsDict",
    "AzureNodePoolConfigArgs",
    "AzureNodePoolConfigArgsDict",
    "AzureNodePoolConfigProxyConfigArgs",
    "AzureNodePoolConfigProxyConfigArgsDict",
    "AzureNodePoolConfigRootVolumeArgs",
    "AzureNodePoolConfigRootVolumeArgsDict",
    "AzureNodePoolConfigSshConfigArgs",
    "AzureNodePoolConfigSshConfigArgsDict",
    "AzureNodePoolManagementArgs",
    "AzureNodePoolManagementArgsDict",
    "AzureNodePoolMaxPodsConstraintArgs",
    "AzureNodePoolMaxPodsConstraintArgsDict",
    "ClusterAddonsConfigArgs",
    "ClusterAddonsConfigArgsDict",
    "ClusterAddonsConfigCloudrunConfigArgs",
    "ClusterAddonsConfigCloudrunConfigArgsDict",
    "ClusterAddonsConfigConfigConnectorConfigArgs",
    "ClusterAddonsConfigConfigConnectorConfigArgsDict",
    "ClusterAddonsConfigDnsCacheConfigArgs",
    "ClusterAddonsConfigDnsCacheConfigArgsDict",
    ...,
    ...,
    "ClusterAddonsConfigGcpFilestoreCsiDriverConfigArgs",
    ...,
    "ClusterAddonsConfigGcsFuseCsiDriverConfigArgs",
    "ClusterAddonsConfigGcsFuseCsiDriverConfigArgsDict",
    "ClusterAddonsConfigGkeBackupAgentConfigArgs",
    "ClusterAddonsConfigGkeBackupAgentConfigArgsDict",
    "ClusterAddonsConfigHorizontalPodAutoscalingArgs",
    ...,
    "ClusterAddonsConfigHttpLoadBalancingArgs",
    "ClusterAddonsConfigHttpLoadBalancingArgsDict",
    "ClusterAddonsConfigIstioConfigArgs",
    "ClusterAddonsConfigIstioConfigArgsDict",
    "ClusterAddonsConfigKalmConfigArgs",
    "ClusterAddonsConfigKalmConfigArgsDict",
    "ClusterAddonsConfigLustreCsiDriverConfigArgs",
    "ClusterAddonsConfigLustreCsiDriverConfigArgsDict",
    "ClusterAddonsConfigNetworkPolicyConfigArgs",
    "ClusterAddonsConfigNetworkPolicyConfigArgsDict",
    ...,
    ...,
    "ClusterAddonsConfigPodSnapshotConfigArgs",
    "ClusterAddonsConfigPodSnapshotConfigArgsDict",
    "ClusterAddonsConfigRayOperatorConfigArgs",
    "ClusterAddonsConfigRayOperatorConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ClusterAddonsConfigSliceControllerConfigArgs",
    "ClusterAddonsConfigSliceControllerConfigArgsDict",
    "ClusterAddonsConfigStatefulHaConfigArgs",
    "ClusterAddonsConfigStatefulHaConfigArgsDict",
    "ClusterAnonymousAuthenticationConfigArgs",
    "ClusterAnonymousAuthenticationConfigArgsDict",
    "ClusterAuthenticatorGroupsConfigArgs",
    "ClusterAuthenticatorGroupsConfigArgsDict",
    "ClusterBinaryAuthorizationArgs",
    "ClusterBinaryAuthorizationArgsDict",
    "ClusterClusterAutoscalingArgs",
    "ClusterClusterAutoscalingArgsDict",
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
    ...,
    "ClusterClusterAutoscalingResourceLimitArgs",
    "ClusterClusterAutoscalingResourceLimitArgsDict",
    "ClusterClusterTelemetryArgs",
    "ClusterClusterTelemetryArgsDict",
    "ClusterConfidentialNodesArgs",
    "ClusterConfidentialNodesArgsDict",
    "ClusterControlPlaneEndpointsConfigArgs",
    "ClusterControlPlaneEndpointsConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ClusterCostManagementConfigArgs",
    "ClusterCostManagementConfigArgsDict",
    "ClusterDatabaseEncryptionArgs",
    "ClusterDatabaseEncryptionArgsDict",
    "ClusterDefaultSnatStatusArgs",
    "ClusterDefaultSnatStatusArgsDict",
    "ClusterDnsConfigArgs",
    "ClusterDnsConfigArgsDict",
    "ClusterEnableK8sBetaApisArgs",
    "ClusterEnableK8sBetaApisArgsDict",
    "ClusterEnterpriseConfigArgs",
    "ClusterEnterpriseConfigArgsDict",
    "ClusterFleetArgs",
    "ClusterFleetArgsDict",
    "ClusterGatewayApiConfigArgs",
    "ClusterGatewayApiConfigArgsDict",
    "ClusterGkeAutoUpgradeConfigArgs",
    "ClusterGkeAutoUpgradeConfigArgsDict",
    "ClusterIdentityServiceConfigArgs",
    "ClusterIdentityServiceConfigArgsDict",
    "ClusterIpAllocationPolicyArgs",
    "ClusterIpAllocationPolicyArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ClusterIpAllocationPolicyAutoIpamConfigArgs",
    "ClusterIpAllocationPolicyAutoIpamConfigArgsDict",
    "ClusterIpAllocationPolicyNetworkTierConfigArgs",
    "ClusterIpAllocationPolicyNetworkTierConfigArgsDict",
    ...,
    ...,
    "ClusterLoggingConfigArgs",
    "ClusterLoggingConfigArgsDict",
    "ClusterMaintenancePolicyArgs",
    "ClusterMaintenancePolicyArgsDict",
    "ClusterMaintenancePolicyDailyMaintenanceWindowArgs",
    ...,
    "ClusterMaintenancePolicyDisruptionBudgetArgs",
    "ClusterMaintenancePolicyDisruptionBudgetArgsDict",
    "ClusterMaintenancePolicyMaintenanceExclusionArgs",
    ...,
    ...,
    ...,
    "ClusterMaintenancePolicyRecurringWindowArgs",
    "ClusterMaintenancePolicyRecurringWindowArgsDict",
    "ClusterManagedOpentelemetryConfigArgs",
    "ClusterManagedOpentelemetryConfigArgsDict",
    "ClusterMasterAuthArgs",
    "ClusterMasterAuthArgsDict",
    "ClusterMasterAuthClientCertificateConfigArgs",
    "ClusterMasterAuthClientCertificateConfigArgsDict",
    "ClusterMasterAuthorizedNetworksConfigArgs",
    "ClusterMasterAuthorizedNetworksConfigArgsDict",
    "ClusterMasterAuthorizedNetworksConfigCidrBlockArgs",
    ...,
    "ClusterMeshCertificatesArgs",
    "ClusterMeshCertificatesArgsDict",
    "ClusterMonitoringConfigArgs",
    "ClusterMonitoringConfigArgsDict",
    ...,
    ...,
    "ClusterMonitoringConfigManagedPrometheusArgs",
    "ClusterMonitoringConfigManagedPrometheusArgsDict",
    ...,
    ...,
    "ClusterNetworkPerformanceConfigArgs",
    "ClusterNetworkPerformanceConfigArgsDict",
    "ClusterNetworkPolicyArgs",
    "ClusterNetworkPolicyArgsDict",
    "ClusterNodeConfigArgs",
    "ClusterNodeConfigArgsDict",
    "ClusterNodeConfigAdvancedMachineFeaturesArgs",
    "ClusterNodeConfigAdvancedMachineFeaturesArgsDict",
    "ClusterNodeConfigBootDiskArgs",
    "ClusterNodeConfigBootDiskArgsDict",
    "ClusterNodeConfigConfidentialNodesArgs",
    "ClusterNodeConfigConfidentialNodesArgsDict",
    "ClusterNodeConfigContainerdConfigArgs",
    "ClusterNodeConfigContainerdConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterNodeConfigContainerdConfigRegistryHostArgs",
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
    ...,
    ...,
    "ClusterNodeConfigEffectiveTaintArgs",
    "ClusterNodeConfigEffectiveTaintArgsDict",
    "ClusterNodeConfigEphemeralStorageConfigArgs",
    "ClusterNodeConfigEphemeralStorageConfigArgsDict",
    ...,
    ...,
    "ClusterNodeConfigFastSocketArgs",
    "ClusterNodeConfigFastSocketArgsDict",
    "ClusterNodeConfigGcfsConfigArgs",
    "ClusterNodeConfigGcfsConfigArgsDict",
    "ClusterNodeConfigGuestAcceleratorArgs",
    "ClusterNodeConfigGuestAcceleratorArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ClusterNodeConfigGvnicArgs",
    "ClusterNodeConfigGvnicArgsDict",
    "ClusterNodeConfigHostMaintenancePolicyArgs",
    "ClusterNodeConfigHostMaintenancePolicyArgsDict",
    "ClusterNodeConfigKubeletConfigArgs",
    "ClusterNodeConfigKubeletConfigArgsDict",
    ...,
    ...,
    "ClusterNodeConfigKubeletConfigEvictionSoftArgs",
    "ClusterNodeConfigKubeletConfigEvictionSoftArgsDict",
    ...,
    ...,
    "ClusterNodeConfigKubeletConfigMemoryManagerArgs",
    ...,
    "ClusterNodeConfigKubeletConfigTopologyManagerArgs",
    ...,
    "ClusterNodeConfigLinuxNodeConfigArgs",
    "ClusterNodeConfigLinuxNodeConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ClusterNodeConfigLocalNvmeSsdBlockConfigArgs",
    "ClusterNodeConfigLocalNvmeSsdBlockConfigArgsDict",
    "ClusterNodeConfigReservationAffinityArgs",
    "ClusterNodeConfigReservationAffinityArgsDict",
    "ClusterNodeConfigSandboxConfigArgs",
    "ClusterNodeConfigSandboxConfigArgsDict",
    "ClusterNodeConfigSecondaryBootDiskArgs",
    "ClusterNodeConfigSecondaryBootDiskArgsDict",
    "ClusterNodeConfigShieldedInstanceConfigArgs",
    "ClusterNodeConfigShieldedInstanceConfigArgsDict",
    "ClusterNodeConfigSoleTenantConfigArgs",
    "ClusterNodeConfigSoleTenantConfigArgsDict",
    "ClusterNodeConfigSoleTenantConfigNodeAffinityArgs",
    ...,
    "ClusterNodeConfigTaintArgs",
    "ClusterNodeConfigTaintArgsDict",
    "ClusterNodeConfigWindowsNodeConfigArgs",
    "ClusterNodeConfigWindowsNodeConfigArgsDict",
    "ClusterNodeConfigWorkloadMetadataConfigArgs",
    "ClusterNodeConfigWorkloadMetadataConfigArgsDict",
    "ClusterNodePoolArgs",
    "ClusterNodePoolArgsDict",
    "ClusterNodePoolAutoConfigArgs",
    "ClusterNodePoolAutoConfigArgsDict",
    "ClusterNodePoolAutoConfigLinuxNodeConfigArgs",
    "ClusterNodePoolAutoConfigLinuxNodeConfigArgsDict",
    ...,
    ...,
    "ClusterNodePoolAutoConfigNetworkTagsArgs",
    "ClusterNodePoolAutoConfigNetworkTagsArgsDict",
    "ClusterNodePoolAutoConfigNodeKubeletConfigArgs",
    "ClusterNodePoolAutoConfigNodeKubeletConfigArgsDict",
    "ClusterNodePoolAutoscalingArgs",
    "ClusterNodePoolAutoscalingArgsDict",
    "ClusterNodePoolDefaultsArgs",
    "ClusterNodePoolDefaultsArgsDict",
    "ClusterNodePoolDefaultsNodeConfigDefaultsArgs",
    "ClusterNodePoolDefaultsNodeConfigDefaultsArgsDict",
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
    "ClusterNodePoolManagementArgs",
    "ClusterNodePoolManagementArgsDict",
    "ClusterNodePoolNetworkConfigArgs",
    "ClusterNodePoolNetworkConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterNodePoolNodeConfigArgs",
    "ClusterNodePoolNodeConfigArgsDict",
    ...,
    ...,
    "ClusterNodePoolNodeConfigBootDiskArgs",
    "ClusterNodePoolNodeConfigBootDiskArgsDict",
    "ClusterNodePoolNodeConfigConfidentialNodesArgs",
    "ClusterNodePoolNodeConfigConfidentialNodesArgsDict",
    "ClusterNodePoolNodeConfigContainerdConfigArgs",
    "ClusterNodePoolNodeConfigContainerdConfigArgsDict",
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
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterNodePoolNodeConfigEffectiveTaintArgs",
    "ClusterNodePoolNodeConfigEffectiveTaintArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ClusterNodePoolNodeConfigFastSocketArgs",
    "ClusterNodePoolNodeConfigFastSocketArgsDict",
    "ClusterNodePoolNodeConfigGcfsConfigArgs",
    "ClusterNodePoolNodeConfigGcfsConfigArgsDict",
    "ClusterNodePoolNodeConfigGuestAcceleratorArgs",
    "ClusterNodePoolNodeConfigGuestAcceleratorArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ClusterNodePoolNodeConfigGvnicArgs",
    "ClusterNodePoolNodeConfigGvnicArgsDict",
    "ClusterNodePoolNodeConfigHostMaintenancePolicyArgs",
    ...,
    "ClusterNodePoolNodeConfigKubeletConfigArgs",
    "ClusterNodePoolNodeConfigKubeletConfigArgsDict",
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
    "ClusterNodePoolNodeConfigLinuxNodeConfigArgs",
    "ClusterNodePoolNodeConfigLinuxNodeConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterNodePoolNodeConfigReservationAffinityArgs",
    ...,
    "ClusterNodePoolNodeConfigSandboxConfigArgs",
    "ClusterNodePoolNodeConfigSandboxConfigArgsDict",
    "ClusterNodePoolNodeConfigSecondaryBootDiskArgs",
    "ClusterNodePoolNodeConfigSecondaryBootDiskArgsDict",
    ...,
    ...,
    "ClusterNodePoolNodeConfigSoleTenantConfigArgs",
    "ClusterNodePoolNodeConfigSoleTenantConfigArgsDict",
    ...,
    ...,
    "ClusterNodePoolNodeConfigTaintArgs",
    "ClusterNodePoolNodeConfigTaintArgsDict",
    "ClusterNodePoolNodeConfigWindowsNodeConfigArgs",
    "ClusterNodePoolNodeConfigWindowsNodeConfigArgsDict",
    ...,
    ...,
    "ClusterNodePoolNodeDrainConfigArgs",
    "ClusterNodePoolNodeDrainConfigArgsDict",
    "ClusterNodePoolPlacementPolicyArgs",
    "ClusterNodePoolPlacementPolicyArgsDict",
    "ClusterNodePoolQueuedProvisioningArgs",
    "ClusterNodePoolQueuedProvisioningArgsDict",
    "ClusterNodePoolUpgradeSettingsArgs",
    "ClusterNodePoolUpgradeSettingsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterNotificationConfigArgs",
    "ClusterNotificationConfigArgsDict",
    "ClusterNotificationConfigPubsubArgs",
    "ClusterNotificationConfigPubsubArgsDict",
    "ClusterNotificationConfigPubsubFilterArgs",
    "ClusterNotificationConfigPubsubFilterArgsDict",
    "ClusterPodAutoscalingArgs",
    "ClusterPodAutoscalingArgsDict",
    "ClusterPodSecurityPolicyConfigArgs",
    "ClusterPodSecurityPolicyConfigArgsDict",
    "ClusterPrivateClusterConfigArgs",
    "ClusterPrivateClusterConfigArgsDict",
    ...,
    ...,
    "ClusterProtectConfigArgs",
    "ClusterProtectConfigArgsDict",
    "ClusterProtectConfigWorkloadConfigArgs",
    "ClusterProtectConfigWorkloadConfigArgsDict",
    "ClusterRbacBindingConfigArgs",
    "ClusterRbacBindingConfigArgsDict",
    "ClusterReleaseChannelArgs",
    "ClusterReleaseChannelArgsDict",
    "ClusterResourceUsageExportConfigArgs",
    "ClusterResourceUsageExportConfigArgsDict",
    ...,
    ...,
    "ClusterSecretManagerConfigArgs",
    "ClusterSecretManagerConfigArgsDict",
    "ClusterSecretManagerConfigRotationConfigArgs",
    "ClusterSecretManagerConfigRotationConfigArgsDict",
    "ClusterSecretSyncConfigArgs",
    "ClusterSecretSyncConfigArgsDict",
    "ClusterSecretSyncConfigRotationConfigArgs",
    "ClusterSecretSyncConfigRotationConfigArgsDict",
    "ClusterSecurityPostureConfigArgs",
    "ClusterSecurityPostureConfigArgsDict",
    "ClusterServiceExternalIpsConfigArgs",
    "ClusterServiceExternalIpsConfigArgsDict",
    "ClusterTpuConfigArgs",
    "ClusterTpuConfigArgsDict",
    "ClusterUserManagedKeysConfigArgs",
    "ClusterUserManagedKeysConfigArgsDict",
    "ClusterVerticalPodAutoscalingArgs",
    "ClusterVerticalPodAutoscalingArgsDict",
    "ClusterWorkloadAltsConfigArgs",
    "ClusterWorkloadAltsConfigArgsDict",
    "ClusterWorkloadIdentityConfigArgs",
    "ClusterWorkloadIdentityConfigArgsDict",
    "NodePoolAutoscalingArgs",
    "NodePoolAutoscalingArgsDict",
    "NodePoolManagementArgs",
    "NodePoolManagementArgsDict",
    "NodePoolNetworkConfigArgs",
    "NodePoolNetworkConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "NodePoolNetworkConfigNetworkPerformanceConfigArgs",
    ...,
    ...,
    ...,
    "NodePoolNodeConfigArgs",
    "NodePoolNodeConfigArgsDict",
    "NodePoolNodeConfigAdvancedMachineFeaturesArgs",
    "NodePoolNodeConfigAdvancedMachineFeaturesArgsDict",
    "NodePoolNodeConfigBootDiskArgs",
    "NodePoolNodeConfigBootDiskArgsDict",
    "NodePoolNodeConfigConfidentialNodesArgs",
    "NodePoolNodeConfigConfidentialNodesArgsDict",
    "NodePoolNodeConfigContainerdConfigArgs",
    "NodePoolNodeConfigContainerdConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "NodePoolNodeConfigContainerdConfigRegistryHostArgs",
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
    ...,
    ...,
    "NodePoolNodeConfigEffectiveTaintArgs",
    "NodePoolNodeConfigEffectiveTaintArgsDict",
    "NodePoolNodeConfigEphemeralStorageConfigArgs",
    "NodePoolNodeConfigEphemeralStorageConfigArgsDict",
    ...,
    ...,
    "NodePoolNodeConfigFastSocketArgs",
    "NodePoolNodeConfigFastSocketArgsDict",
    "NodePoolNodeConfigGcfsConfigArgs",
    "NodePoolNodeConfigGcfsConfigArgsDict",
    "NodePoolNodeConfigGuestAcceleratorArgs",
    "NodePoolNodeConfigGuestAcceleratorArgsDict",
    ...,
    ...,
    ...,
    ...,
    "NodePoolNodeConfigGvnicArgs",
    "NodePoolNodeConfigGvnicArgsDict",
    "NodePoolNodeConfigHostMaintenancePolicyArgs",
    "NodePoolNodeConfigHostMaintenancePolicyArgsDict",
    "NodePoolNodeConfigKubeletConfigArgs",
    "NodePoolNodeConfigKubeletConfigArgsDict",
    ...,
    ...,
    "NodePoolNodeConfigKubeletConfigEvictionSoftArgs",
    ...,
    ...,
    ...,
    "NodePoolNodeConfigKubeletConfigMemoryManagerArgs",
    ...,
    "NodePoolNodeConfigKubeletConfigTopologyManagerArgs",
    ...,
    "NodePoolNodeConfigLinuxNodeConfigArgs",
    "NodePoolNodeConfigLinuxNodeConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "NodePoolNodeConfigLocalNvmeSsdBlockConfigArgs",
    "NodePoolNodeConfigLocalNvmeSsdBlockConfigArgsDict",
    "NodePoolNodeConfigReservationAffinityArgs",
    "NodePoolNodeConfigReservationAffinityArgsDict",
    "NodePoolNodeConfigSandboxConfigArgs",
    "NodePoolNodeConfigSandboxConfigArgsDict",
    "NodePoolNodeConfigSecondaryBootDiskArgs",
    "NodePoolNodeConfigSecondaryBootDiskArgsDict",
    "NodePoolNodeConfigShieldedInstanceConfigArgs",
    "NodePoolNodeConfigShieldedInstanceConfigArgsDict",
    "NodePoolNodeConfigSoleTenantConfigArgs",
    "NodePoolNodeConfigSoleTenantConfigArgsDict",
    "NodePoolNodeConfigSoleTenantConfigNodeAffinityArgs",
    ...,
    "NodePoolNodeConfigTaintArgs",
    "NodePoolNodeConfigTaintArgsDict",
    "NodePoolNodeConfigWindowsNodeConfigArgs",
    "NodePoolNodeConfigWindowsNodeConfigArgsDict",
    "NodePoolNodeConfigWorkloadMetadataConfigArgs",
    "NodePoolNodeConfigWorkloadMetadataConfigArgsDict",
    "NodePoolNodeDrainConfigArgs",
    "NodePoolNodeDrainConfigArgsDict",
    "NodePoolPlacementPolicyArgs",
    "NodePoolPlacementPolicyArgsDict",
    "NodePoolQueuedProvisioningArgs",
    "NodePoolQueuedProvisioningArgsDict",
    "NodePoolUpgradeSettingsArgs",
    "NodePoolUpgradeSettingsArgsDict",
    "NodePoolUpgradeSettingsBlueGreenSettingsArgs",
    "NodePoolUpgradeSettingsBlueGreenSettingsArgsDict",
    ...,
    ...,
    ...,
    ...,
]

class AttachedClusterAuthorizationArgsDict(TypedDict):
    admin_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    admin_users: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AttachedClusterAuthorizationArgs:
    def __init__(
        __self__,
        *,
        admin_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        admin_users: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminGroups")
    def admin_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @admin_groups.setter
    def admin_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="adminUsers")
    def admin_users(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @admin_users.setter
    def admin_users(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AttachedClusterBinaryAuthorizationArgsDict(TypedDict):
    evaluation_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AttachedClusterBinaryAuthorizationArgs:
    def __init__(
        __self__, *, evaluation_mode: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="evaluationMode")
    def evaluation_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @evaluation_mode.setter
    def evaluation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AttachedClusterErrorArgsDict(TypedDict):
    message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AttachedClusterErrorArgs:
    def __init__(
        __self__, *, message: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AttachedClusterFleetArgsDict(TypedDict):
    project: pulumi.Input[_builtins.str]
    membership: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AttachedClusterFleetArgs:
    def __init__(
        __self__,
        *,
        project: pulumi.Input[_builtins.str],
        membership: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Input[_builtins.str]: ...
    @project.setter
    def project(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership.setter
    def membership(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AttachedClusterLoggingConfigArgsDict(TypedDict):
    component_config: NotRequired[
        pulumi.Input[AttachedClusterLoggingConfigComponentConfigArgsDict]
    ]

@pulumi.input_type
class AttachedClusterLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        component_config: Optional[
            pulumi.Input[AttachedClusterLoggingConfigComponentConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentConfig")
    def component_config(
        self,
    ) -> Optional[pulumi.Input[AttachedClusterLoggingConfigComponentConfigArgs]]: ...
    @component_config.setter
    def component_config(
        self,
        value: Optional[pulumi.Input[AttachedClusterLoggingConfigComponentConfigArgs]],
    ): ...

class AttachedClusterLoggingConfigComponentConfigArgsDict(TypedDict):
    enable_components: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AttachedClusterLoggingConfigComponentConfigArgs:
    def __init__(
        __self__,
        *,
        enable_components: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableComponents")
    def enable_components(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enable_components.setter
    def enable_components(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AttachedClusterMonitoringConfigArgsDict(TypedDict):
    managed_prometheus_config: NotRequired[
        pulumi.Input[AttachedClusterMonitoringConfigManagedPrometheusConfigArgsDict]
    ]

@pulumi.input_type
class AttachedClusterMonitoringConfigArgs:
    def __init__(
        __self__,
        *,
        managed_prometheus_config: Optional[
            pulumi.Input[AttachedClusterMonitoringConfigManagedPrometheusConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedPrometheusConfig")
    def managed_prometheus_config(
        self,
    ) -> Optional[
        pulumi.Input[AttachedClusterMonitoringConfigManagedPrometheusConfigArgs]
    ]: ...
    @managed_prometheus_config.setter
    def managed_prometheus_config(
        self,
        value: Optional[
            pulumi.Input[AttachedClusterMonitoringConfigManagedPrometheusConfigArgs]
        ],
    ): ...

class AttachedClusterMonitoringConfigManagedPrometheusConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AttachedClusterMonitoringConfigManagedPrometheusConfigArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AttachedClusterOidcConfigArgsDict(TypedDict):
    issuer_url: pulumi.Input[_builtins.str]
    jwks: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AttachedClusterOidcConfigArgs:
    def __init__(
        __self__,
        *,
        issuer_url: pulumi.Input[_builtins.str],
        jwks: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="issuerUrl")
    def issuer_url(self) -> pulumi.Input[_builtins.str]: ...
    @issuer_url.setter
    def issuer_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def jwks(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @jwks.setter
    def jwks(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AttachedClusterProxyConfigArgsDict(TypedDict):
    kubernetes_secret: NotRequired[
        pulumi.Input[AttachedClusterProxyConfigKubernetesSecretArgsDict]
    ]

@pulumi.input_type
class AttachedClusterProxyConfigArgs:
    def __init__(
        __self__,
        *,
        kubernetes_secret: Optional[
            pulumi.Input[AttachedClusterProxyConfigKubernetesSecretArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesSecret")
    def kubernetes_secret(
        self,
    ) -> Optional[pulumi.Input[AttachedClusterProxyConfigKubernetesSecretArgs]]: ...
    @kubernetes_secret.setter
    def kubernetes_secret(
        self,
        value: Optional[pulumi.Input[AttachedClusterProxyConfigKubernetesSecretArgs]],
    ): ...

class AttachedClusterProxyConfigKubernetesSecretArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]

@pulumi.input_type
class AttachedClusterProxyConfigKubernetesSecretArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...

class AttachedClusterSecurityPostureConfigArgsDict(TypedDict):
    vulnerability_mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class AttachedClusterSecurityPostureConfigArgs:
    def __init__(
        __self__, *, vulnerability_mode: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vulnerabilityMode")
    def vulnerability_mode(self) -> pulumi.Input[_builtins.str]: ...
    @vulnerability_mode.setter
    def vulnerability_mode(self, value: pulumi.Input[_builtins.str]): ...

class AttachedClusterWorkloadIdentityConfigArgsDict(TypedDict):
    identity_provider: NotRequired[pulumi.Input[_builtins.str]]
    issuer_uri: NotRequired[pulumi.Input[_builtins.str]]
    workload_pool: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AttachedClusterWorkloadIdentityConfigArgs:
    def __init__(
        __self__,
        *,
        identity_provider: Optional[pulumi.Input[_builtins.str]] = ...,
        issuer_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_pool: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityProvider")
    def identity_provider(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_provider.setter
    def identity_provider(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @issuer_uri.setter
    def issuer_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workloadPool")
    def workload_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workload_pool.setter
    def workload_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AwsClusterAuthorizationArgsDict(TypedDict):
    admin_users: pulumi.Input[
        Sequence[pulumi.Input[AwsClusterAuthorizationAdminUserArgsDict]]
    ]
    admin_groups: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AwsClusterAuthorizationAdminGroupArgsDict]]]
    ]

@pulumi.input_type
class AwsClusterAuthorizationArgs:
    def __init__(
        __self__,
        *,
        admin_users: pulumi.Input[
            Sequence[pulumi.Input[AwsClusterAuthorizationAdminUserArgs]]
        ],
        admin_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[AwsClusterAuthorizationAdminGroupArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminUsers")
    def admin_users(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[AwsClusterAuthorizationAdminUserArgs]]]: ...
    @admin_users.setter
    def admin_users(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[AwsClusterAuthorizationAdminUserArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="adminGroups")
    def admin_groups(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AwsClusterAuthorizationAdminGroupArgs]]]
    ]: ...
    @admin_groups.setter
    def admin_groups(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AwsClusterAuthorizationAdminGroupArgs]]]
        ],
    ): ...

class AwsClusterAuthorizationAdminGroupArgsDict(TypedDict):
    group: pulumi.Input[_builtins.str]

@pulumi.input_type
class AwsClusterAuthorizationAdminGroupArgs:
    def __init__(__self__, *, group: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> pulumi.Input[_builtins.str]: ...
    @group.setter
    def group(self, value: pulumi.Input[_builtins.str]): ...

class AwsClusterAuthorizationAdminUserArgsDict(TypedDict):
    username: pulumi.Input[_builtins.str]

@pulumi.input_type
class AwsClusterAuthorizationAdminUserArgs:
    def __init__(__self__, *, username: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...

class AwsClusterBinaryAuthorizationArgsDict(TypedDict):
    evaluation_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AwsClusterBinaryAuthorizationArgs:
    def __init__(
        __self__, *, evaluation_mode: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="evaluationMode")
    def evaluation_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @evaluation_mode.setter
    def evaluation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AwsClusterControlPlaneArgsDict(TypedDict):
    aws_services_authentication: pulumi.Input[
        AwsClusterControlPlaneAwsServicesAuthenticationArgsDict
    ]
    config_encryption: pulumi.Input[AwsClusterControlPlaneConfigEncryptionArgsDict]
    database_encryption: pulumi.Input[AwsClusterControlPlaneDatabaseEncryptionArgsDict]
    iam_instance_profile: pulumi.Input[_builtins.str]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    version: pulumi.Input[_builtins.str]
    instance_placement: NotRequired[
        pulumi.Input[AwsClusterControlPlaneInstancePlacementArgsDict]
    ]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    main_volume: NotRequired[pulumi.Input[AwsClusterControlPlaneMainVolumeArgsDict]]
    proxy_config: NotRequired[pulumi.Input[AwsClusterControlPlaneProxyConfigArgsDict]]
    root_volume: NotRequired[pulumi.Input[AwsClusterControlPlaneRootVolumeArgsDict]]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ssh_config: NotRequired[pulumi.Input[AwsClusterControlPlaneSshConfigArgsDict]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AwsClusterControlPlaneArgs:
    def __init__(
        __self__,
        *,
        aws_services_authentication: pulumi.Input[
            AwsClusterControlPlaneAwsServicesAuthenticationArgs
        ],
        config_encryption: pulumi.Input[AwsClusterControlPlaneConfigEncryptionArgs],
        database_encryption: pulumi.Input[AwsClusterControlPlaneDatabaseEncryptionArgs],
        iam_instance_profile: pulumi.Input[_builtins.str],
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        version: pulumi.Input[_builtins.str],
        instance_placement: Optional[
            pulumi.Input[AwsClusterControlPlaneInstancePlacementArgs]
        ] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        main_volume: Optional[pulumi.Input[AwsClusterControlPlaneMainVolumeArgs]] = ...,
        proxy_config: Optional[
            pulumi.Input[AwsClusterControlPlaneProxyConfigArgs]
        ] = ...,
        root_volume: Optional[pulumi.Input[AwsClusterControlPlaneRootVolumeArgs]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ssh_config: Optional[pulumi.Input[AwsClusterControlPlaneSshConfigArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsServicesAuthentication")
    def aws_services_authentication(
        self,
    ) -> pulumi.Input[AwsClusterControlPlaneAwsServicesAuthenticationArgs]: ...
    @aws_services_authentication.setter
    def aws_services_authentication(
        self, value: pulumi.Input[AwsClusterControlPlaneAwsServicesAuthenticationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="configEncryption")
    def config_encryption(
        self,
    ) -> pulumi.Input[AwsClusterControlPlaneConfigEncryptionArgs]: ...
    @config_encryption.setter
    def config_encryption(
        self, value: pulumi.Input[AwsClusterControlPlaneConfigEncryptionArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="databaseEncryption")
    def database_encryption(
        self,
    ) -> pulumi.Input[AwsClusterControlPlaneDatabaseEncryptionArgs]: ...
    @database_encryption.setter
    def database_encryption(
        self, value: pulumi.Input[AwsClusterControlPlaneDatabaseEncryptionArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> pulumi.Input[_builtins.str]: ...
    @iam_instance_profile.setter
    def iam_instance_profile(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instancePlacement")
    def instance_placement(
        self,
    ) -> Optional[pulumi.Input[AwsClusterControlPlaneInstancePlacementArgs]]: ...
    @instance_placement.setter
    def instance_placement(
        self, value: Optional[pulumi.Input[AwsClusterControlPlaneInstancePlacementArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mainVolume")
    def main_volume(
        self,
    ) -> Optional[pulumi.Input[AwsClusterControlPlaneMainVolumeArgs]]: ...
    @main_volume.setter
    def main_volume(
        self, value: Optional[pulumi.Input[AwsClusterControlPlaneMainVolumeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="proxyConfig")
    def proxy_config(
        self,
    ) -> Optional[pulumi.Input[AwsClusterControlPlaneProxyConfigArgs]]: ...
    @proxy_config.setter
    def proxy_config(
        self, value: Optional[pulumi.Input[AwsClusterControlPlaneProxyConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rootVolume")
    def root_volume(
        self,
    ) -> Optional[pulumi.Input[AwsClusterControlPlaneRootVolumeArgs]]: ...
    @root_volume.setter
    def root_volume(
        self, value: Optional[pulumi.Input[AwsClusterControlPlaneRootVolumeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sshConfig")
    def ssh_config(
        self,
    ) -> Optional[pulumi.Input[AwsClusterControlPlaneSshConfigArgs]]: ...
    @ssh_config.setter
    def ssh_config(
        self, value: Optional[pulumi.Input[AwsClusterControlPlaneSshConfigArgs]]
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

class AwsClusterControlPlaneAwsServicesAuthenticationArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    role_session_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AwsClusterControlPlaneAwsServicesAuthenticationArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        role_session_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleSessionName")
    def role_session_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_session_name.setter
    def role_session_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AwsClusterControlPlaneConfigEncryptionArgsDict(TypedDict):
    kms_key_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AwsClusterControlPlaneConfigEncryptionArgs:
    def __init__(__self__, *, kms_key_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: pulumi.Input[_builtins.str]): ...

class AwsClusterControlPlaneDatabaseEncryptionArgsDict(TypedDict):
    kms_key_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AwsClusterControlPlaneDatabaseEncryptionArgs:
    def __init__(__self__, *, kms_key_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: pulumi.Input[_builtins.str]): ...

class AwsClusterControlPlaneInstancePlacementArgsDict(TypedDict):
    tenancy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AwsClusterControlPlaneInstancePlacementArgs:
    def __init__(
        __self__, *, tenancy: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenancy.setter
    def tenancy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AwsClusterControlPlaneMainVolumeArgsDict(TypedDict):
    iops: NotRequired[pulumi.Input[_builtins.int]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    size_gib: NotRequired[pulumi.Input[_builtins.int]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AwsClusterControlPlaneMainVolumeArgs:
    def __init__(
        __self__,
        *,
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        size_gib: Optional[pulumi.Input[_builtins.int]] = ...,
        throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeGib")
    def size_gib(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size_gib.setter
    def size_gib(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AwsClusterControlPlaneProxyConfigArgsDict(TypedDict):
    secret_arn: pulumi.Input[_builtins.str]
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class AwsClusterControlPlaneProxyConfigArgs:
    def __init__(
        __self__,
        *,
        secret_arn: pulumi.Input[_builtins.str],
        secret_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> pulumi.Input[_builtins.str]: ...
    @secret_arn.setter
    def secret_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class AwsClusterControlPlaneRootVolumeArgsDict(TypedDict):
    iops: NotRequired[pulumi.Input[_builtins.int]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    size_gib: NotRequired[pulumi.Input[_builtins.int]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AwsClusterControlPlaneRootVolumeArgs:
    def __init__(
        __self__,
        *,
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        size_gib: Optional[pulumi.Input[_builtins.int]] = ...,
        throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeGib")
    def size_gib(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size_gib.setter
    def size_gib(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AwsClusterControlPlaneSshConfigArgsDict(TypedDict):
    ec2_key_pair: pulumi.Input[_builtins.str]

@pulumi.input_type
class AwsClusterControlPlaneSshConfigArgs:
    def __init__(__self__, *, ec2_key_pair: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ec2KeyPair")
    def ec2_key_pair(self) -> pulumi.Input[_builtins.str]: ...
    @ec2_key_pair.setter
    def ec2_key_pair(self, value: pulumi.Input[_builtins.str]): ...

class AwsClusterFleetArgsDict(TypedDict):
    membership: NotRequired[pulumi.Input[_builtins.str]]
    project: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AwsClusterFleetArgs:
    def __init__(
        __self__,
        *,
        membership: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership.setter
    def membership(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AwsClusterLoggingConfigArgsDict(TypedDict):
    component_config: NotRequired[
        pulumi.Input[AwsClusterLoggingConfigComponentConfigArgsDict]
    ]

@pulumi.input_type
class AwsClusterLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        component_config: Optional[
            pulumi.Input[AwsClusterLoggingConfigComponentConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentConfig")
    def component_config(
        self,
    ) -> Optional[pulumi.Input[AwsClusterLoggingConfigComponentConfigArgs]]: ...
    @component_config.setter
    def component_config(
        self, value: Optional[pulumi.Input[AwsClusterLoggingConfigComponentConfigArgs]]
    ): ...

class AwsClusterLoggingConfigComponentConfigArgsDict(TypedDict):
    enable_components: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AwsClusterLoggingConfigComponentConfigArgs:
    def __init__(
        __self__,
        *,
        enable_components: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableComponents")
    def enable_components(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enable_components.setter
    def enable_components(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AwsClusterNetworkingArgsDict(TypedDict):
    pod_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    service_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    vpc_id: pulumi.Input[_builtins.str]
    per_node_pool_sg_rules_disabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AwsClusterNetworkingArgs:
    def __init__(
        __self__,
        *,
        pod_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        service_address_cidr_blocks: pulumi.Input[
            Sequence[pulumi.Input[_builtins.str]]
        ],
        vpc_id: pulumi.Input[_builtins.str],
        per_node_pool_sg_rules_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="podAddressCidrBlocks")
    def pod_address_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @pod_address_cidr_blocks.setter
    def pod_address_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAddressCidrBlocks")
    def service_address_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @service_address_cidr_blocks.setter
    def service_address_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="perNodePoolSgRulesDisabled")
    def per_node_pool_sg_rules_disabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @per_node_pool_sg_rules_disabled.setter
    def per_node_pool_sg_rules_disabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AwsClusterWorkloadIdentityConfigArgsDict(TypedDict):
    identity_provider: NotRequired[pulumi.Input[_builtins.str]]
    issuer_uri: NotRequired[pulumi.Input[_builtins.str]]
    workload_pool: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AwsClusterWorkloadIdentityConfigArgs:
    def __init__(
        __self__,
        *,
        identity_provider: Optional[pulumi.Input[_builtins.str]] = ...,
        issuer_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_pool: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityProvider")
    def identity_provider(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_provider.setter
    def identity_provider(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @issuer_uri.setter
    def issuer_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workloadPool")
    def workload_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workload_pool.setter
    def workload_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AwsNodePoolAutoscalingArgsDict(TypedDict):
    max_node_count: pulumi.Input[_builtins.int]
    min_node_count: pulumi.Input[_builtins.int]

@pulumi.input_type
class AwsNodePoolAutoscalingArgs:
    def __init__(
        __self__,
        *,
        max_node_count: pulumi.Input[_builtins.int],
        min_node_count: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> pulumi.Input[_builtins.int]: ...
    @max_node_count.setter
    def max_node_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> pulumi.Input[_builtins.int]: ...
    @min_node_count.setter
    def min_node_count(self, value: pulumi.Input[_builtins.int]): ...

class AwsNodePoolConfigArgsDict(TypedDict):
    config_encryption: pulumi.Input[AwsNodePoolConfigConfigEncryptionArgsDict]
    iam_instance_profile: pulumi.Input[_builtins.str]
    autoscaling_metrics_collection: NotRequired[
        pulumi.Input[AwsNodePoolConfigAutoscalingMetricsCollectionArgsDict]
    ]
    image_type: NotRequired[pulumi.Input[_builtins.str]]
    instance_placement: NotRequired[
        pulumi.Input[AwsNodePoolConfigInstancePlacementArgsDict]
    ]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    proxy_config: NotRequired[pulumi.Input[AwsNodePoolConfigProxyConfigArgsDict]]
    root_volume: NotRequired[pulumi.Input[AwsNodePoolConfigRootVolumeArgsDict]]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    spot_config: NotRequired[pulumi.Input[AwsNodePoolConfigSpotConfigArgsDict]]
    ssh_config: NotRequired[pulumi.Input[AwsNodePoolConfigSshConfigArgsDict]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    taints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AwsNodePoolConfigTaintArgsDict]]]
    ]

@pulumi.input_type
class AwsNodePoolConfigArgs:
    def __init__(
        __self__,
        *,
        config_encryption: pulumi.Input[AwsNodePoolConfigConfigEncryptionArgs],
        iam_instance_profile: pulumi.Input[_builtins.str],
        autoscaling_metrics_collection: Optional[
            pulumi.Input[AwsNodePoolConfigAutoscalingMetricsCollectionArgs]
        ] = ...,
        image_type: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_placement: Optional[
            pulumi.Input[AwsNodePoolConfigInstancePlacementArgs]
        ] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        proxy_config: Optional[pulumi.Input[AwsNodePoolConfigProxyConfigArgs]] = ...,
        root_volume: Optional[pulumi.Input[AwsNodePoolConfigRootVolumeArgs]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        spot_config: Optional[pulumi.Input[AwsNodePoolConfigSpotConfigArgs]] = ...,
        ssh_config: Optional[pulumi.Input[AwsNodePoolConfigSshConfigArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        taints: Optional[
            pulumi.Input[Sequence[pulumi.Input[AwsNodePoolConfigTaintArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configEncryption")
    def config_encryption(
        self,
    ) -> pulumi.Input[AwsNodePoolConfigConfigEncryptionArgs]: ...
    @config_encryption.setter
    def config_encryption(
        self, value: pulumi.Input[AwsNodePoolConfigConfigEncryptionArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> pulumi.Input[_builtins.str]: ...
    @iam_instance_profile.setter
    def iam_instance_profile(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoscalingMetricsCollection")
    def autoscaling_metrics_collection(
        self,
    ) -> Optional[pulumi.Input[AwsNodePoolConfigAutoscalingMetricsCollectionArgs]]: ...
    @autoscaling_metrics_collection.setter
    def autoscaling_metrics_collection(
        self,
        value: Optional[
            pulumi.Input[AwsNodePoolConfigAutoscalingMetricsCollectionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_type.setter
    def image_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instancePlacement")
    def instance_placement(
        self,
    ) -> Optional[pulumi.Input[AwsNodePoolConfigInstancePlacementArgs]]: ...
    @instance_placement.setter
    def instance_placement(
        self, value: Optional[pulumi.Input[AwsNodePoolConfigInstancePlacementArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="proxyConfig")
    def proxy_config(
        self,
    ) -> Optional[pulumi.Input[AwsNodePoolConfigProxyConfigArgs]]: ...
    @proxy_config.setter
    def proxy_config(
        self, value: Optional[pulumi.Input[AwsNodePoolConfigProxyConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rootVolume")
    def root_volume(
        self,
    ) -> Optional[pulumi.Input[AwsNodePoolConfigRootVolumeArgs]]: ...
    @root_volume.setter
    def root_volume(
        self, value: Optional[pulumi.Input[AwsNodePoolConfigRootVolumeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="spotConfig")
    def spot_config(
        self,
    ) -> Optional[pulumi.Input[AwsNodePoolConfigSpotConfigArgs]]: ...
    @spot_config.setter
    def spot_config(
        self, value: Optional[pulumi.Input[AwsNodePoolConfigSpotConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sshConfig")
    def ssh_config(self) -> Optional[pulumi.Input[AwsNodePoolConfigSshConfigArgs]]: ...
    @ssh_config.setter
    def ssh_config(
        self, value: Optional[pulumi.Input[AwsNodePoolConfigSshConfigArgs]]
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
    @pulumi.getter
    def taints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AwsNodePoolConfigTaintArgs]]]]: ...
    @taints.setter
    def taints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AwsNodePoolConfigTaintArgs]]]
        ],
    ): ...

class AwsNodePoolConfigAutoscalingMetricsCollectionArgsDict(TypedDict):
    granularity: pulumi.Input[_builtins.str]
    metrics: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AwsNodePoolConfigAutoscalingMetricsCollectionArgs:
    def __init__(
        __self__,
        *,
        granularity: pulumi.Input[_builtins.str],
        metrics: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def granularity(self) -> pulumi.Input[_builtins.str]: ...
    @granularity.setter
    def granularity(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def metrics(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @metrics.setter
    def metrics(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AwsNodePoolConfigConfigEncryptionArgsDict(TypedDict):
    kms_key_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AwsNodePoolConfigConfigEncryptionArgs:
    def __init__(__self__, *, kms_key_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: pulumi.Input[_builtins.str]): ...

class AwsNodePoolConfigInstancePlacementArgsDict(TypedDict):
    tenancy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AwsNodePoolConfigInstancePlacementArgs:
    def __init__(
        __self__, *, tenancy: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenancy.setter
    def tenancy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AwsNodePoolConfigProxyConfigArgsDict(TypedDict):
    secret_arn: pulumi.Input[_builtins.str]
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class AwsNodePoolConfigProxyConfigArgs:
    def __init__(
        __self__,
        *,
        secret_arn: pulumi.Input[_builtins.str],
        secret_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> pulumi.Input[_builtins.str]: ...
    @secret_arn.setter
    def secret_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class AwsNodePoolConfigRootVolumeArgsDict(TypedDict):
    iops: NotRequired[pulumi.Input[_builtins.int]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    size_gib: NotRequired[pulumi.Input[_builtins.int]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AwsNodePoolConfigRootVolumeArgs:
    def __init__(
        __self__,
        *,
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        size_gib: Optional[pulumi.Input[_builtins.int]] = ...,
        throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeGib")
    def size_gib(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size_gib.setter
    def size_gib(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AwsNodePoolConfigSpotConfigArgsDict(TypedDict):
    instance_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class AwsNodePoolConfigSpotConfigArgs:
    def __init__(
        __self__, *, instance_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @instance_types.setter
    def instance_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class AwsNodePoolConfigSshConfigArgsDict(TypedDict):
    ec2_key_pair: pulumi.Input[_builtins.str]

@pulumi.input_type
class AwsNodePoolConfigSshConfigArgs:
    def __init__(__self__, *, ec2_key_pair: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ec2KeyPair")
    def ec2_key_pair(self) -> pulumi.Input[_builtins.str]: ...
    @ec2_key_pair.setter
    def ec2_key_pair(self, value: pulumi.Input[_builtins.str]): ...

class AwsNodePoolConfigTaintArgsDict(TypedDict):
    effect: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AwsNodePoolConfigTaintArgs:
    def __init__(
        __self__,
        *,
        effect: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> pulumi.Input[_builtins.str]: ...
    @effect.setter
    def effect(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AwsNodePoolKubeletConfigArgsDict(TypedDict):
    cpu_cfs_quota: NotRequired[pulumi.Input[_builtins.bool]]
    cpu_cfs_quota_period: NotRequired[pulumi.Input[_builtins.str]]
    cpu_manager_policy: NotRequired[pulumi.Input[_builtins.str]]
    pod_pids_limit: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AwsNodePoolKubeletConfigArgs:
    def __init__(
        __self__,
        *,
        cpu_cfs_quota: Optional[pulumi.Input[_builtins.bool]] = ...,
        cpu_cfs_quota_period: Optional[pulumi.Input[_builtins.str]] = ...,
        cpu_manager_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        pod_pids_limit: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuota")
    def cpu_cfs_quota(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cpu_cfs_quota.setter
    def cpu_cfs_quota(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuotaPeriod")
    def cpu_cfs_quota_period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu_cfs_quota_period.setter
    def cpu_cfs_quota_period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuManagerPolicy")
    def cpu_manager_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu_manager_policy.setter
    def cpu_manager_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="podPidsLimit")
    def pod_pids_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pod_pids_limit.setter
    def pod_pids_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AwsNodePoolManagementArgsDict(TypedDict):
    auto_repair: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AwsNodePoolManagementArgs:
    def __init__(
        __self__, *, auto_repair: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRepair")
    def auto_repair(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_repair.setter
    def auto_repair(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AwsNodePoolMaxPodsConstraintArgsDict(TypedDict):
    max_pods_per_node: pulumi.Input[_builtins.int]

@pulumi.input_type
class AwsNodePoolMaxPodsConstraintArgs:
    def __init__(
        __self__, *, max_pods_per_node: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> pulumi.Input[_builtins.int]: ...
    @max_pods_per_node.setter
    def max_pods_per_node(self, value: pulumi.Input[_builtins.int]): ...

class AwsNodePoolUpdateSettingsArgsDict(TypedDict):
    surge_settings: NotRequired[
        pulumi.Input[AwsNodePoolUpdateSettingsSurgeSettingsArgsDict]
    ]

@pulumi.input_type
class AwsNodePoolUpdateSettingsArgs:
    def __init__(
        __self__,
        *,
        surge_settings: Optional[
            pulumi.Input[AwsNodePoolUpdateSettingsSurgeSettingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="surgeSettings")
    def surge_settings(
        self,
    ) -> Optional[pulumi.Input[AwsNodePoolUpdateSettingsSurgeSettingsArgs]]: ...
    @surge_settings.setter
    def surge_settings(
        self, value: Optional[pulumi.Input[AwsNodePoolUpdateSettingsSurgeSettingsArgs]]
    ): ...

class AwsNodePoolUpdateSettingsSurgeSettingsArgsDict(TypedDict):
    max_surge: NotRequired[pulumi.Input[_builtins.int]]
    max_unavailable: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AwsNodePoolUpdateSettingsSurgeSettingsArgs:
    def __init__(
        __self__,
        *,
        max_surge: Optional[pulumi.Input[_builtins.int]] = ...,
        max_unavailable: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxSurge")
    def max_surge(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_surge.setter
    def max_surge(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxUnavailable")
    def max_unavailable(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_unavailable.setter
    def max_unavailable(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AzureClusterAuthorizationArgsDict(TypedDict):
    admin_users: pulumi.Input[
        Sequence[pulumi.Input[AzureClusterAuthorizationAdminUserArgsDict]]
    ]
    admin_groups: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AzureClusterAuthorizationAdminGroupArgsDict]]
        ]
    ]

@pulumi.input_type
class AzureClusterAuthorizationArgs:
    def __init__(
        __self__,
        *,
        admin_users: pulumi.Input[
            Sequence[pulumi.Input[AzureClusterAuthorizationAdminUserArgs]]
        ],
        admin_groups: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AzureClusterAuthorizationAdminGroupArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminUsers")
    def admin_users(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[AzureClusterAuthorizationAdminUserArgs]]
    ]: ...
    @admin_users.setter
    def admin_users(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[AzureClusterAuthorizationAdminUserArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="adminGroups")
    def admin_groups(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AzureClusterAuthorizationAdminGroupArgs]]]
    ]: ...
    @admin_groups.setter
    def admin_groups(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AzureClusterAuthorizationAdminGroupArgs]]
            ]
        ],
    ): ...

class AzureClusterAuthorizationAdminGroupArgsDict(TypedDict):
    group: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureClusterAuthorizationAdminGroupArgs:
    def __init__(__self__, *, group: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> pulumi.Input[_builtins.str]: ...
    @group.setter
    def group(self, value: pulumi.Input[_builtins.str]): ...

class AzureClusterAuthorizationAdminUserArgsDict(TypedDict):
    username: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureClusterAuthorizationAdminUserArgs:
    def __init__(__self__, *, username: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...

class AzureClusterAzureServicesAuthenticationArgsDict(TypedDict):
    application_id: pulumi.Input[_builtins.str]
    tenant_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureClusterAzureServicesAuthenticationArgs:
    def __init__(
        __self__,
        *,
        application_id: pulumi.Input[_builtins.str],
        tenant_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[_builtins.str]: ...
    @application_id.setter
    def application_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]: ...
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): ...

class AzureClusterControlPlaneArgsDict(TypedDict):
    ssh_config: pulumi.Input[AzureClusterControlPlaneSshConfigArgsDict]
    subnet_id: pulumi.Input[_builtins.str]
    version: pulumi.Input[_builtins.str]
    database_encryption: NotRequired[
        pulumi.Input[AzureClusterControlPlaneDatabaseEncryptionArgsDict]
    ]
    main_volume: NotRequired[pulumi.Input[AzureClusterControlPlaneMainVolumeArgsDict]]
    proxy_config: NotRequired[pulumi.Input[AzureClusterControlPlaneProxyConfigArgsDict]]
    replica_placements: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AzureClusterControlPlaneReplicaPlacementArgsDict]]
        ]
    ]
    root_volume: NotRequired[pulumi.Input[AzureClusterControlPlaneRootVolumeArgsDict]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    vm_size: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureClusterControlPlaneArgs:
    def __init__(
        __self__,
        *,
        ssh_config: pulumi.Input[AzureClusterControlPlaneSshConfigArgs],
        subnet_id: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
        database_encryption: Optional[
            pulumi.Input[AzureClusterControlPlaneDatabaseEncryptionArgs]
        ] = ...,
        main_volume: Optional[
            pulumi.Input[AzureClusterControlPlaneMainVolumeArgs]
        ] = ...,
        proxy_config: Optional[
            pulumi.Input[AzureClusterControlPlaneProxyConfigArgs]
        ] = ...,
        replica_placements: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AzureClusterControlPlaneReplicaPlacementArgs]]
            ]
        ] = ...,
        root_volume: Optional[
            pulumi.Input[AzureClusterControlPlaneRootVolumeArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sshConfig")
    def ssh_config(self) -> pulumi.Input[AzureClusterControlPlaneSshConfigArgs]: ...
    @ssh_config.setter
    def ssh_config(
        self, value: pulumi.Input[AzureClusterControlPlaneSshConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseEncryption")
    def database_encryption(
        self,
    ) -> Optional[pulumi.Input[AzureClusterControlPlaneDatabaseEncryptionArgs]]: ...
    @database_encryption.setter
    def database_encryption(
        self,
        value: Optional[pulumi.Input[AzureClusterControlPlaneDatabaseEncryptionArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mainVolume")
    def main_volume(
        self,
    ) -> Optional[pulumi.Input[AzureClusterControlPlaneMainVolumeArgs]]: ...
    @main_volume.setter
    def main_volume(
        self, value: Optional[pulumi.Input[AzureClusterControlPlaneMainVolumeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="proxyConfig")
    def proxy_config(
        self,
    ) -> Optional[pulumi.Input[AzureClusterControlPlaneProxyConfigArgs]]: ...
    @proxy_config.setter
    def proxy_config(
        self, value: Optional[pulumi.Input[AzureClusterControlPlaneProxyConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicaPlacements")
    def replica_placements(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AzureClusterControlPlaneReplicaPlacementArgs]]
        ]
    ]: ...
    @replica_placements.setter
    def replica_placements(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AzureClusterControlPlaneReplicaPlacementArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rootVolume")
    def root_volume(
        self,
    ) -> Optional[pulumi.Input[AzureClusterControlPlaneRootVolumeArgs]]: ...
    @root_volume.setter
    def root_volume(
        self, value: Optional[pulumi.Input[AzureClusterControlPlaneRootVolumeArgs]]
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
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureClusterControlPlaneDatabaseEncryptionArgsDict(TypedDict):
    key_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureClusterControlPlaneDatabaseEncryptionArgs:
    def __init__(__self__, *, key_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[_builtins.str]: ...
    @key_id.setter
    def key_id(self, value: pulumi.Input[_builtins.str]): ...

class AzureClusterControlPlaneMainVolumeArgsDict(TypedDict):
    size_gib: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AzureClusterControlPlaneMainVolumeArgs:
    def __init__(
        __self__, *, size_gib: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeGib")
    def size_gib(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size_gib.setter
    def size_gib(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AzureClusterControlPlaneProxyConfigArgsDict(TypedDict):
    resource_group_id: pulumi.Input[_builtins.str]
    secret_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureClusterControlPlaneProxyConfigArgs:
    def __init__(
        __self__,
        *,
        resource_group_id: pulumi.Input[_builtins.str],
        secret_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_id.setter
    def resource_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> pulumi.Input[_builtins.str]: ...
    @secret_id.setter
    def secret_id(self, value: pulumi.Input[_builtins.str]): ...

class AzureClusterControlPlaneReplicaPlacementArgsDict(TypedDict):
    azure_availability_zone: pulumi.Input[_builtins.str]
    subnet_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureClusterControlPlaneReplicaPlacementArgs:
    def __init__(
        __self__,
        *,
        azure_availability_zone: pulumi.Input[_builtins.str],
        subnet_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureAvailabilityZone")
    def azure_availability_zone(self) -> pulumi.Input[_builtins.str]: ...
    @azure_availability_zone.setter
    def azure_availability_zone(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): ...

class AzureClusterControlPlaneRootVolumeArgsDict(TypedDict):
    size_gib: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AzureClusterControlPlaneRootVolumeArgs:
    def __init__(
        __self__, *, size_gib: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeGib")
    def size_gib(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size_gib.setter
    def size_gib(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AzureClusterControlPlaneSshConfigArgsDict(TypedDict):
    authorized_key: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureClusterControlPlaneSshConfigArgs:
    def __init__(__self__, *, authorized_key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizedKey")
    def authorized_key(self) -> pulumi.Input[_builtins.str]: ...
    @authorized_key.setter
    def authorized_key(self, value: pulumi.Input[_builtins.str]): ...

class AzureClusterFleetArgsDict(TypedDict):
    membership: NotRequired[pulumi.Input[_builtins.str]]
    project: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureClusterFleetArgs:
    def __init__(
        __self__,
        *,
        membership: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership.setter
    def membership(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureClusterLoggingConfigArgsDict(TypedDict):
    component_config: NotRequired[
        pulumi.Input[AzureClusterLoggingConfigComponentConfigArgsDict]
    ]

@pulumi.input_type
class AzureClusterLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        component_config: Optional[
            pulumi.Input[AzureClusterLoggingConfigComponentConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentConfig")
    def component_config(
        self,
    ) -> Optional[pulumi.Input[AzureClusterLoggingConfigComponentConfigArgs]]: ...
    @component_config.setter
    def component_config(
        self,
        value: Optional[pulumi.Input[AzureClusterLoggingConfigComponentConfigArgs]],
    ): ...

class AzureClusterLoggingConfigComponentConfigArgsDict(TypedDict):
    enable_components: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AzureClusterLoggingConfigComponentConfigArgs:
    def __init__(
        __self__,
        *,
        enable_components: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableComponents")
    def enable_components(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enable_components.setter
    def enable_components(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AzureClusterNetworkingArgsDict(TypedDict):
    pod_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    service_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    virtual_network_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureClusterNetworkingArgs:
    def __init__(
        __self__,
        *,
        pod_address_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        service_address_cidr_blocks: pulumi.Input[
            Sequence[pulumi.Input[_builtins.str]]
        ],
        virtual_network_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="podAddressCidrBlocks")
    def pod_address_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @pod_address_cidr_blocks.setter
    def pod_address_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAddressCidrBlocks")
    def service_address_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @service_address_cidr_blocks.setter
    def service_address_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_network_id.setter
    def virtual_network_id(self, value: pulumi.Input[_builtins.str]): ...

class AzureClusterWorkloadIdentityConfigArgsDict(TypedDict):
    identity_provider: NotRequired[pulumi.Input[_builtins.str]]
    issuer_uri: NotRequired[pulumi.Input[_builtins.str]]
    workload_pool: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureClusterWorkloadIdentityConfigArgs:
    def __init__(
        __self__,
        *,
        identity_provider: Optional[pulumi.Input[_builtins.str]] = ...,
        issuer_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_pool: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityProvider")
    def identity_provider(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_provider.setter
    def identity_provider(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="issuerUri")
    def issuer_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @issuer_uri.setter
    def issuer_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workloadPool")
    def workload_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workload_pool.setter
    def workload_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureNodePoolAutoscalingArgsDict(TypedDict):
    max_node_count: pulumi.Input[_builtins.int]
    min_node_count: pulumi.Input[_builtins.int]

@pulumi.input_type
class AzureNodePoolAutoscalingArgs:
    def __init__(
        __self__,
        *,
        max_node_count: pulumi.Input[_builtins.int],
        min_node_count: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> pulumi.Input[_builtins.int]: ...
    @max_node_count.setter
    def max_node_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> pulumi.Input[_builtins.int]: ...
    @min_node_count.setter
    def min_node_count(self, value: pulumi.Input[_builtins.int]): ...

class AzureNodePoolConfigArgsDict(TypedDict):
    ssh_config: pulumi.Input[AzureNodePoolConfigSshConfigArgsDict]
    image_type: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    proxy_config: NotRequired[pulumi.Input[AzureNodePoolConfigProxyConfigArgsDict]]
    root_volume: NotRequired[pulumi.Input[AzureNodePoolConfigRootVolumeArgsDict]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    vm_size: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureNodePoolConfigArgs:
    def __init__(
        __self__,
        *,
        ssh_config: pulumi.Input[AzureNodePoolConfigSshConfigArgs],
        image_type: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        proxy_config: Optional[pulumi.Input[AzureNodePoolConfigProxyConfigArgs]] = ...,
        root_volume: Optional[pulumi.Input[AzureNodePoolConfigRootVolumeArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sshConfig")
    def ssh_config(self) -> pulumi.Input[AzureNodePoolConfigSshConfigArgs]: ...
    @ssh_config.setter
    def ssh_config(self, value: pulumi.Input[AzureNodePoolConfigSshConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_type.setter
    def image_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="proxyConfig")
    def proxy_config(
        self,
    ) -> Optional[pulumi.Input[AzureNodePoolConfigProxyConfigArgs]]: ...
    @proxy_config.setter
    def proxy_config(
        self, value: Optional[pulumi.Input[AzureNodePoolConfigProxyConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rootVolume")
    def root_volume(
        self,
    ) -> Optional[pulumi.Input[AzureNodePoolConfigRootVolumeArgs]]: ...
    @root_volume.setter
    def root_volume(
        self, value: Optional[pulumi.Input[AzureNodePoolConfigRootVolumeArgs]]
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
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureNodePoolConfigProxyConfigArgsDict(TypedDict):
    resource_group_id: pulumi.Input[_builtins.str]
    secret_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureNodePoolConfigProxyConfigArgs:
    def __init__(
        __self__,
        *,
        resource_group_id: pulumi.Input[_builtins.str],
        secret_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_id.setter
    def resource_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> pulumi.Input[_builtins.str]: ...
    @secret_id.setter
    def secret_id(self, value: pulumi.Input[_builtins.str]): ...

class AzureNodePoolConfigRootVolumeArgsDict(TypedDict):
    size_gib: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AzureNodePoolConfigRootVolumeArgs:
    def __init__(
        __self__, *, size_gib: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeGib")
    def size_gib(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size_gib.setter
    def size_gib(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AzureNodePoolConfigSshConfigArgsDict(TypedDict):
    authorized_key: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureNodePoolConfigSshConfigArgs:
    def __init__(__self__, *, authorized_key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizedKey")
    def authorized_key(self) -> pulumi.Input[_builtins.str]: ...
    @authorized_key.setter
    def authorized_key(self, value: pulumi.Input[_builtins.str]): ...

class AzureNodePoolManagementArgsDict(TypedDict):
    auto_repair: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AzureNodePoolManagementArgs:
    def __init__(
        __self__, *, auto_repair: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRepair")
    def auto_repair(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_repair.setter
    def auto_repair(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AzureNodePoolMaxPodsConstraintArgsDict(TypedDict):
    max_pods_per_node: pulumi.Input[_builtins.int]

@pulumi.input_type
class AzureNodePoolMaxPodsConstraintArgs:
    def __init__(
        __self__, *, max_pods_per_node: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> pulumi.Input[_builtins.int]: ...
    @max_pods_per_node.setter
    def max_pods_per_node(self, value: pulumi.Input[_builtins.int]): ...

class ClusterAddonsConfigArgsDict(TypedDict):
    cloudrun_config: NotRequired[
        pulumi.Input[ClusterAddonsConfigCloudrunConfigArgsDict]
    ]
    config_connector_config: NotRequired[
        pulumi.Input[ClusterAddonsConfigConfigConnectorConfigArgsDict]
    ]
    dns_cache_config: NotRequired[
        pulumi.Input[ClusterAddonsConfigDnsCacheConfigArgsDict]
    ]
    gce_persistent_disk_csi_driver_config: NotRequired[
        pulumi.Input[ClusterAddonsConfigGcePersistentDiskCsiDriverConfigArgsDict]
    ]
    gcp_filestore_csi_driver_config: NotRequired[
        pulumi.Input[ClusterAddonsConfigGcpFilestoreCsiDriverConfigArgsDict]
    ]
    gcs_fuse_csi_driver_config: NotRequired[
        pulumi.Input[ClusterAddonsConfigGcsFuseCsiDriverConfigArgsDict]
    ]
    gke_backup_agent_config: NotRequired[
        pulumi.Input[ClusterAddonsConfigGkeBackupAgentConfigArgsDict]
    ]
    horizontal_pod_autoscaling: NotRequired[
        pulumi.Input[ClusterAddonsConfigHorizontalPodAutoscalingArgsDict]
    ]
    http_load_balancing: NotRequired[
        pulumi.Input[ClusterAddonsConfigHttpLoadBalancingArgsDict]
    ]
    istio_config: NotRequired[pulumi.Input[ClusterAddonsConfigIstioConfigArgsDict]]
    kalm_config: NotRequired[pulumi.Input[ClusterAddonsConfigKalmConfigArgsDict]]
    lustre_csi_driver_config: NotRequired[
        pulumi.Input[ClusterAddonsConfigLustreCsiDriverConfigArgsDict]
    ]
    network_policy_config: NotRequired[
        pulumi.Input[ClusterAddonsConfigNetworkPolicyConfigArgsDict]
    ]
    parallelstore_csi_driver_config: NotRequired[
        pulumi.Input[ClusterAddonsConfigParallelstoreCsiDriverConfigArgsDict]
    ]
    pod_snapshot_config: NotRequired[
        pulumi.Input[ClusterAddonsConfigPodSnapshotConfigArgsDict]
    ]
    ray_operator_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterAddonsConfigRayOperatorConfigArgsDict]]
        ]
    ]
    slice_controller_config: NotRequired[
        pulumi.Input[ClusterAddonsConfigSliceControllerConfigArgsDict]
    ]
    stateful_ha_config: NotRequired[
        pulumi.Input[ClusterAddonsConfigStatefulHaConfigArgsDict]
    ]

@pulumi.input_type
class ClusterAddonsConfigArgs:
    def __init__(
        __self__,
        *,
        cloudrun_config: Optional[
            pulumi.Input[ClusterAddonsConfigCloudrunConfigArgs]
        ] = ...,
        config_connector_config: Optional[
            pulumi.Input[ClusterAddonsConfigConfigConnectorConfigArgs]
        ] = ...,
        dns_cache_config: Optional[
            pulumi.Input[ClusterAddonsConfigDnsCacheConfigArgs]
        ] = ...,
        gce_persistent_disk_csi_driver_config: Optional[
            pulumi.Input[ClusterAddonsConfigGcePersistentDiskCsiDriverConfigArgs]
        ] = ...,
        gcp_filestore_csi_driver_config: Optional[
            pulumi.Input[ClusterAddonsConfigGcpFilestoreCsiDriverConfigArgs]
        ] = ...,
        gcs_fuse_csi_driver_config: Optional[
            pulumi.Input[ClusterAddonsConfigGcsFuseCsiDriverConfigArgs]
        ] = ...,
        gke_backup_agent_config: Optional[
            pulumi.Input[ClusterAddonsConfigGkeBackupAgentConfigArgs]
        ] = ...,
        horizontal_pod_autoscaling: Optional[
            pulumi.Input[ClusterAddonsConfigHorizontalPodAutoscalingArgs]
        ] = ...,
        http_load_balancing: Optional[
            pulumi.Input[ClusterAddonsConfigHttpLoadBalancingArgs]
        ] = ...,
        istio_config: Optional[pulumi.Input[ClusterAddonsConfigIstioConfigArgs]] = ...,
        kalm_config: Optional[pulumi.Input[ClusterAddonsConfigKalmConfigArgs]] = ...,
        lustre_csi_driver_config: Optional[
            pulumi.Input[ClusterAddonsConfigLustreCsiDriverConfigArgs]
        ] = ...,
        network_policy_config: Optional[
            pulumi.Input[ClusterAddonsConfigNetworkPolicyConfigArgs]
        ] = ...,
        parallelstore_csi_driver_config: Optional[
            pulumi.Input[ClusterAddonsConfigParallelstoreCsiDriverConfigArgs]
        ] = ...,
        pod_snapshot_config: Optional[
            pulumi.Input[ClusterAddonsConfigPodSnapshotConfigArgs]
        ] = ...,
        ray_operator_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterAddonsConfigRayOperatorConfigArgs]]
            ]
        ] = ...,
        slice_controller_config: Optional[
            pulumi.Input[ClusterAddonsConfigSliceControllerConfigArgs]
        ] = ...,
        stateful_ha_config: Optional[
            pulumi.Input[ClusterAddonsConfigStatefulHaConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudrunConfig")
    def cloudrun_config(
        self,
    ) -> Optional[pulumi.Input[ClusterAddonsConfigCloudrunConfigArgs]]: ...
    @cloudrun_config.setter
    def cloudrun_config(
        self, value: Optional[pulumi.Input[ClusterAddonsConfigCloudrunConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="configConnectorConfig")
    def config_connector_config(
        self,
    ) -> Optional[pulumi.Input[ClusterAddonsConfigConfigConnectorConfigArgs]]: ...
    @config_connector_config.setter
    def config_connector_config(
        self,
        value: Optional[pulumi.Input[ClusterAddonsConfigConfigConnectorConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsCacheConfig")
    def dns_cache_config(
        self,
    ) -> Optional[pulumi.Input[ClusterAddonsConfigDnsCacheConfigArgs]]: ...
    @dns_cache_config.setter
    def dns_cache_config(
        self, value: Optional[pulumi.Input[ClusterAddonsConfigDnsCacheConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gcePersistentDiskCsiDriverConfig")
    def gce_persistent_disk_csi_driver_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterAddonsConfigGcePersistentDiskCsiDriverConfigArgs]
    ]: ...
    @gce_persistent_disk_csi_driver_config.setter
    def gce_persistent_disk_csi_driver_config(
        self,
        value: Optional[
            pulumi.Input[ClusterAddonsConfigGcePersistentDiskCsiDriverConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gcpFilestoreCsiDriverConfig")
    def gcp_filestore_csi_driver_config(
        self,
    ) -> Optional[pulumi.Input[ClusterAddonsConfigGcpFilestoreCsiDriverConfigArgs]]: ...
    @gcp_filestore_csi_driver_config.setter
    def gcp_filestore_csi_driver_config(
        self,
        value: Optional[
            pulumi.Input[ClusterAddonsConfigGcpFilestoreCsiDriverConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gcsFuseCsiDriverConfig")
    def gcs_fuse_csi_driver_config(
        self,
    ) -> Optional[pulumi.Input[ClusterAddonsConfigGcsFuseCsiDriverConfigArgs]]: ...
    @gcs_fuse_csi_driver_config.setter
    def gcs_fuse_csi_driver_config(
        self,
        value: Optional[pulumi.Input[ClusterAddonsConfigGcsFuseCsiDriverConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gkeBackupAgentConfig")
    def gke_backup_agent_config(
        self,
    ) -> Optional[pulumi.Input[ClusterAddonsConfigGkeBackupAgentConfigArgs]]: ...
    @gke_backup_agent_config.setter
    def gke_backup_agent_config(
        self, value: Optional[pulumi.Input[ClusterAddonsConfigGkeBackupAgentConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="horizontalPodAutoscaling")
    def horizontal_pod_autoscaling(
        self,
    ) -> Optional[pulumi.Input[ClusterAddonsConfigHorizontalPodAutoscalingArgs]]: ...
    @horizontal_pod_autoscaling.setter
    def horizontal_pod_autoscaling(
        self,
        value: Optional[pulumi.Input[ClusterAddonsConfigHorizontalPodAutoscalingArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpLoadBalancing")
    def http_load_balancing(
        self,
    ) -> Optional[pulumi.Input[ClusterAddonsConfigHttpLoadBalancingArgs]]: ...
    @http_load_balancing.setter
    def http_load_balancing(
        self, value: Optional[pulumi.Input[ClusterAddonsConfigHttpLoadBalancingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="istioConfig")
    def istio_config(
        self,
    ) -> Optional[pulumi.Input[ClusterAddonsConfigIstioConfigArgs]]: ...
    @istio_config.setter
    def istio_config(
        self, value: Optional[pulumi.Input[ClusterAddonsConfigIstioConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kalmConfig")
    def kalm_config(
        self,
    ) -> Optional[pulumi.Input[ClusterAddonsConfigKalmConfigArgs]]: ...
    @kalm_config.setter
    def kalm_config(
        self, value: Optional[pulumi.Input[ClusterAddonsConfigKalmConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lustreCsiDriverConfig")
    def lustre_csi_driver_config(
        self,
    ) -> Optional[pulumi.Input[ClusterAddonsConfigLustreCsiDriverConfigArgs]]: ...
    @lustre_csi_driver_config.setter
    def lustre_csi_driver_config(
        self,
        value: Optional[pulumi.Input[ClusterAddonsConfigLustreCsiDriverConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkPolicyConfig")
    def network_policy_config(
        self,
    ) -> Optional[pulumi.Input[ClusterAddonsConfigNetworkPolicyConfigArgs]]: ...
    @network_policy_config.setter
    def network_policy_config(
        self, value: Optional[pulumi.Input[ClusterAddonsConfigNetworkPolicyConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="parallelstoreCsiDriverConfig")
    def parallelstore_csi_driver_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterAddonsConfigParallelstoreCsiDriverConfigArgs]
    ]: ...
    @parallelstore_csi_driver_config.setter
    def parallelstore_csi_driver_config(
        self,
        value: Optional[
            pulumi.Input[ClusterAddonsConfigParallelstoreCsiDriverConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="podSnapshotConfig")
    def pod_snapshot_config(
        self,
    ) -> Optional[pulumi.Input[ClusterAddonsConfigPodSnapshotConfigArgs]]: ...
    @pod_snapshot_config.setter
    def pod_snapshot_config(
        self, value: Optional[pulumi.Input[ClusterAddonsConfigPodSnapshotConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rayOperatorConfigs")
    def ray_operator_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterAddonsConfigRayOperatorConfigArgs]]]
    ]: ...
    @ray_operator_configs.setter
    def ray_operator_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterAddonsConfigRayOperatorConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sliceControllerConfig")
    def slice_controller_config(
        self,
    ) -> Optional[pulumi.Input[ClusterAddonsConfigSliceControllerConfigArgs]]: ...
    @slice_controller_config.setter
    def slice_controller_config(
        self,
        value: Optional[pulumi.Input[ClusterAddonsConfigSliceControllerConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="statefulHaConfig")
    def stateful_ha_config(
        self,
    ) -> Optional[pulumi.Input[ClusterAddonsConfigStatefulHaConfigArgs]]: ...
    @stateful_ha_config.setter
    def stateful_ha_config(
        self, value: Optional[pulumi.Input[ClusterAddonsConfigStatefulHaConfigArgs]]
    ): ...

class ClusterAddonsConfigCloudrunConfigArgsDict(TypedDict):
    disabled: pulumi.Input[_builtins.bool]
    load_balancer_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterAddonsConfigCloudrunConfigArgs:
    def __init__(
        __self__,
        *,
        disabled: pulumi.Input[_builtins.bool],
        load_balancer_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Input[_builtins.bool]: ...
    @disabled.setter
    def disabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancer_type.setter
    def load_balancer_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterAddonsConfigConfigConnectorConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigConfigConnectorConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAddonsConfigDnsCacheConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigDnsCacheConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAddonsConfigGcePersistentDiskCsiDriverConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigGcePersistentDiskCsiDriverConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAddonsConfigGcpFilestoreCsiDriverConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigGcpFilestoreCsiDriverConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAddonsConfigGcsFuseCsiDriverConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigGcsFuseCsiDriverConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAddonsConfigGkeBackupAgentConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigGkeBackupAgentConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAddonsConfigHorizontalPodAutoscalingArgsDict(TypedDict):
    disabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigHorizontalPodAutoscalingArgs:
    def __init__(__self__, *, disabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Input[_builtins.bool]: ...
    @disabled.setter
    def disabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAddonsConfigHttpLoadBalancingArgsDict(TypedDict):
    disabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigHttpLoadBalancingArgs:
    def __init__(__self__, *, disabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Input[_builtins.bool]: ...
    @disabled.setter
    def disabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAddonsConfigIstioConfigArgsDict(TypedDict):
    disabled: pulumi.Input[_builtins.bool]
    auth: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterAddonsConfigIstioConfigArgs:
    def __init__(
        __self__,
        *,
        disabled: pulumi.Input[_builtins.bool],
        auth: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Input[_builtins.bool]: ...
    @disabled.setter
    def disabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth.setter
    def auth(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterAddonsConfigKalmConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigKalmConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAddonsConfigLustreCsiDriverConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    enable_legacy_lustre_port: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterAddonsConfigLustreCsiDriverConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        enable_legacy_lustre_port: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="enableLegacyLustrePort")
    def enable_legacy_lustre_port(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_legacy_lustre_port.setter
    def enable_legacy_lustre_port(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ClusterAddonsConfigNetworkPolicyConfigArgsDict(TypedDict):
    disabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigNetworkPolicyConfigArgs:
    def __init__(__self__, *, disabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Input[_builtins.bool]: ...
    @disabled.setter
    def disabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAddonsConfigParallelstoreCsiDriverConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigParallelstoreCsiDriverConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAddonsConfigPodSnapshotConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigPodSnapshotConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAddonsConfigRayOperatorConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    ray_cluster_logging_config: NotRequired[
        pulumi.Input[
            ClusterAddonsConfigRayOperatorConfigRayClusterLoggingConfigArgsDict
        ]
    ]
    ray_cluster_monitoring_config: NotRequired[
        pulumi.Input[
            ClusterAddonsConfigRayOperatorConfigRayClusterMonitoringConfigArgsDict
        ]
    ]

@pulumi.input_type
class ClusterAddonsConfigRayOperatorConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        ray_cluster_logging_config: Optional[
            pulumi.Input[
                ClusterAddonsConfigRayOperatorConfigRayClusterLoggingConfigArgs
            ]
        ] = ...,
        ray_cluster_monitoring_config: Optional[
            pulumi.Input[
                ClusterAddonsConfigRayOperatorConfigRayClusterMonitoringConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="rayClusterLoggingConfig")
    def ray_cluster_logging_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterAddonsConfigRayOperatorConfigRayClusterLoggingConfigArgs]
    ]: ...
    @ray_cluster_logging_config.setter
    def ray_cluster_logging_config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterAddonsConfigRayOperatorConfigRayClusterLoggingConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rayClusterMonitoringConfig")
    def ray_cluster_monitoring_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterAddonsConfigRayOperatorConfigRayClusterMonitoringConfigArgs]
    ]: ...
    @ray_cluster_monitoring_config.setter
    def ray_cluster_monitoring_config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterAddonsConfigRayOperatorConfigRayClusterMonitoringConfigArgs
            ]
        ],
    ): ...

class ClusterAddonsConfigRayOperatorConfigRayClusterLoggingConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigRayOperatorConfigRayClusterLoggingConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAddonsConfigRayOperatorConfigRayClusterMonitoringConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigRayOperatorConfigRayClusterMonitoringConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAddonsConfigSliceControllerConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigSliceControllerConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAddonsConfigStatefulHaConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterAddonsConfigStatefulHaConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterAnonymousAuthenticationConfigArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterAnonymousAuthenticationConfigArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...

class ClusterAuthenticatorGroupsConfigArgsDict(TypedDict):
    security_group: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterAuthenticatorGroupsConfigArgs:
    def __init__(__self__, *, security_group: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroup")
    def security_group(self) -> pulumi.Input[_builtins.str]: ...
    @security_group.setter
    def security_group(self, value: pulumi.Input[_builtins.str]): ...

class ClusterBinaryAuthorizationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    evaluation_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterBinaryAuthorizationArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        evaluation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""Deprecated in favor of evaluation_mode.""")
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="evaluationMode")
    def evaluation_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @evaluation_mode.setter
    def evaluation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterClusterAutoscalingArgsDict(TypedDict):
    auto_provisioning_defaults: NotRequired[
        pulumi.Input[ClusterClusterAutoscalingAutoProvisioningDefaultsArgsDict]
    ]
    auto_provisioning_locations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    autoscaling_profile: NotRequired[pulumi.Input[_builtins.str]]
    default_compute_class_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    resource_limits: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterClusterAutoscalingResourceLimitArgsDict]]
        ]
    ]

@pulumi.input_type
class ClusterClusterAutoscalingArgs:
    def __init__(
        __self__,
        *,
        auto_provisioning_defaults: Optional[
            pulumi.Input[ClusterClusterAutoscalingAutoProvisioningDefaultsArgs]
        ] = ...,
        auto_provisioning_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        autoscaling_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        default_compute_class_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        resource_limits: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterClusterAutoscalingResourceLimitArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoProvisioningDefaults")
    def auto_provisioning_defaults(
        self,
    ) -> Optional[
        pulumi.Input[ClusterClusterAutoscalingAutoProvisioningDefaultsArgs]
    ]: ...
    @auto_provisioning_defaults.setter
    def auto_provisioning_defaults(
        self,
        value: Optional[
            pulumi.Input[ClusterClusterAutoscalingAutoProvisioningDefaultsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoProvisioningLocations")
    def auto_provisioning_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @auto_provisioning_locations.setter
    def auto_provisioning_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoscalingProfile")
    def autoscaling_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @autoscaling_profile.setter
    def autoscaling_profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultComputeClassEnabled")
    def default_compute_class_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @default_compute_class_enabled.setter
    def default_compute_class_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceLimits")
    def resource_limits(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterClusterAutoscalingResourceLimitArgs]]]
    ]: ...
    @resource_limits.setter
    def resource_limits(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterClusterAutoscalingResourceLimitArgs]]
            ]
        ],
    ): ...

class ClusterClusterAutoscalingAutoProvisioningDefaultsArgsDict(TypedDict):
    boot_disk_kms_key: NotRequired[pulumi.Input[_builtins.str]]
    disk_size: NotRequired[pulumi.Input[_builtins.int]]
    disk_type: NotRequired[pulumi.Input[_builtins.str]]
    image_type: NotRequired[pulumi.Input[_builtins.str]]
    management: NotRequired[
        pulumi.Input[
            ClusterClusterAutoscalingAutoProvisioningDefaultsManagementArgsDict
        ]
    ]
    min_cpu_platform: NotRequired[pulumi.Input[_builtins.str]]
    oauth_scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    shielded_instance_config: NotRequired[
        pulumi.Input[
            ClusterClusterAutoscalingAutoProvisioningDefaultsShieldedInstanceConfigArgsDict
        ]
    ]
    upgrade_settings: NotRequired[
        pulumi.Input[
            ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsArgsDict
        ]
    ]

@pulumi.input_type
class ClusterClusterAutoscalingAutoProvisioningDefaultsArgs:
    def __init__(
        __self__,
        *,
        boot_disk_kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size: Optional[pulumi.Input[_builtins.int]] = ...,
        disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        image_type: Optional[pulumi.Input[_builtins.str]] = ...,
        management: Optional[
            pulumi.Input[
                ClusterClusterAutoscalingAutoProvisioningDefaultsManagementArgs
            ]
        ] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[
                ClusterClusterAutoscalingAutoProvisioningDefaultsShieldedInstanceConfigArgs
            ]
        ] = ...,
        upgrade_settings: Optional[
            pulumi.Input[
                ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskKmsKey")
    def boot_disk_kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @boot_disk_kms_key.setter
    def boot_disk_kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size.setter
    def disk_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_type.setter
    def image_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def management(
        self,
    ) -> Optional[
        pulumi.Input[ClusterClusterAutoscalingAutoProvisioningDefaultsManagementArgs]
    ]: ...
    @management.setter
    def management(
        self,
        value: Optional[
            pulumi.Input[
                ClusterClusterAutoscalingAutoProvisioningDefaultsManagementArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @oauth_scopes.setter
    def oauth_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterClusterAutoscalingAutoProvisioningDefaultsShieldedInstanceConfigArgs
        ]
    ]: ...
    @shielded_instance_config.setter
    def shielded_instance_config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterClusterAutoscalingAutoProvisioningDefaultsShieldedInstanceConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsArgs
        ]
    ]: ...
    @upgrade_settings.setter
    def upgrade_settings(
        self,
        value: Optional[
            pulumi.Input[
                ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsArgs
            ]
        ],
    ): ...

class ClusterClusterAutoscalingAutoProvisioningDefaultsManagementArgsDict(TypedDict):
    auto_repair: NotRequired[pulumi.Input[_builtins.bool]]
    auto_upgrade: NotRequired[pulumi.Input[_builtins.bool]]
    upgrade_options: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterAutoscalingAutoProvisioningDefaultsManagementUpgradeOptionArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ClusterClusterAutoscalingAutoProvisioningDefaultsManagementArgs:
    def __init__(
        __self__,
        *,
        auto_repair: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        upgrade_options: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterAutoscalingAutoProvisioningDefaultsManagementUpgradeOptionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRepair")
    def auto_repair(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_repair.setter
    def auto_repair(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="autoUpgrade")
    def auto_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_upgrade.setter
    def auto_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="upgradeOptions")
    def upgrade_options(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterAutoscalingAutoProvisioningDefaultsManagementUpgradeOptionArgs
                ]
            ]
        ]
    ]: ...
    @upgrade_options.setter
    def upgrade_options(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterAutoscalingAutoProvisioningDefaultsManagementUpgradeOptionArgs
                    ]
                ]
            ]
        ],
    ): ...

class ClusterClusterAutoscalingAutoProvisioningDefaultsManagementUpgradeOptionArgsDict(
    TypedDict
):
    auto_upgrade_start_time: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterClusterAutoscalingAutoProvisioningDefaultsManagementUpgradeOptionArgs:
    def __init__(
        __self__,
        *,
        auto_upgrade_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoUpgradeStartTime")
    def auto_upgrade_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_upgrade_start_time.setter
    def auto_upgrade_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterClusterAutoscalingAutoProvisioningDefaultsShieldedInstanceConfigArgsDict(
    TypedDict
):
    enable_integrity_monitoring: NotRequired[pulumi.Input[_builtins.bool]]
    enable_secure_boot: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterClusterAutoscalingAutoProvisioningDefaultsShieldedInstanceConfigArgs:
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_secure_boot: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_integrity_monitoring.setter
    def enable_integrity_monitoring(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_secure_boot.setter
    def enable_secure_boot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsArgsDict(
    TypedDict
):
    blue_green_settings: NotRequired[
        pulumi.Input[
            ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettingsArgsDict
        ]
    ]
    max_surge: NotRequired[pulumi.Input[_builtins.int]]
    max_unavailable: NotRequired[pulumi.Input[_builtins.int]]
    strategy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsArgs:
    def __init__(
        __self__,
        *,
        blue_green_settings: Optional[
            pulumi.Input[
                ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettingsArgs
            ]
        ] = ...,
        max_surge: Optional[pulumi.Input[_builtins.int]] = ...,
        max_unavailable: Optional[pulumi.Input[_builtins.int]] = ...,
        strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blueGreenSettings")
    def blue_green_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettingsArgs
        ]
    ]: ...
    @blue_green_settings.setter
    def blue_green_settings(
        self,
        value: Optional[
            pulumi.Input[
                ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxSurge")
    def max_surge(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_surge.setter
    def max_surge(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxUnavailable")
    def max_unavailable(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_unavailable.setter
    def max_unavailable(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @strategy.setter
    def strategy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettingsArgsDict(
    TypedDict
):
    node_pool_soak_duration: NotRequired[pulumi.Input[_builtins.str]]
    standard_rollout_policy: NotRequired[
        pulumi.Input[
            ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgsDict
        ]
    ]

@pulumi.input_type
class ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettingsArgs:
    def __init__(
        __self__,
        *,
        node_pool_soak_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        standard_rollout_policy: Optional[
            pulumi.Input[
                ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodePoolSoakDuration")
    def node_pool_soak_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_pool_soak_duration.setter
    def node_pool_soak_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="standardRolloutPolicy")
    def standard_rollout_policy(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgs
        ]
    ]: ...
    @standard_rollout_policy.setter
    def standard_rollout_policy(
        self,
        value: Optional[
            pulumi.Input[
                ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgs
            ]
        ],
    ): ...

class ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgsDict(
    TypedDict
):
    batch_node_count: NotRequired[pulumi.Input[_builtins.int]]
    batch_percentage: NotRequired[pulumi.Input[_builtins.float]]
    batch_soak_duration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterClusterAutoscalingAutoProvisioningDefaultsUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgs:
    def __init__(
        __self__,
        *,
        batch_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        batch_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        batch_soak_duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchNodeCount")
    def batch_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @batch_node_count.setter
    def batch_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="batchPercentage")
    def batch_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @batch_percentage.setter
    def batch_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="batchSoakDuration")
    def batch_soak_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @batch_soak_duration.setter
    def batch_soak_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterClusterAutoscalingResourceLimitArgsDict(TypedDict):
    maximum: pulumi.Input[_builtins.int]
    resource_type: pulumi.Input[_builtins.str]
    minimum: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterAutoscalingResourceLimitArgs:
    def __init__(
        __self__,
        *,
        maximum: pulumi.Input[_builtins.int],
        resource_type: pulumi.Input[_builtins.str],
        minimum: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> pulumi.Input[_builtins.int]: ...
    @maximum.setter
    def maximum(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minimum.setter
    def minimum(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterClusterTelemetryArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterClusterTelemetryArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class ClusterConfidentialNodesArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    confidential_instance_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterConfidentialNodesArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        confidential_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceType")
    def confidential_instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @confidential_instance_type.setter
    def confidential_instance_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterControlPlaneEndpointsConfigArgsDict(TypedDict):
    dns_endpoint_config: NotRequired[
        pulumi.Input[ClusterControlPlaneEndpointsConfigDnsEndpointConfigArgsDict]
    ]
    ip_endpoints_config: NotRequired[
        pulumi.Input[ClusterControlPlaneEndpointsConfigIpEndpointsConfigArgsDict]
    ]

@pulumi.input_type
class ClusterControlPlaneEndpointsConfigArgs:
    def __init__(
        __self__,
        *,
        dns_endpoint_config: Optional[
            pulumi.Input[ClusterControlPlaneEndpointsConfigDnsEndpointConfigArgs]
        ] = ...,
        ip_endpoints_config: Optional[
            pulumi.Input[ClusterControlPlaneEndpointsConfigIpEndpointsConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsEndpointConfig")
    def dns_endpoint_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterControlPlaneEndpointsConfigDnsEndpointConfigArgs]
    ]: ...
    @dns_endpoint_config.setter
    def dns_endpoint_config(
        self,
        value: Optional[
            pulumi.Input[ClusterControlPlaneEndpointsConfigDnsEndpointConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipEndpointsConfig")
    def ip_endpoints_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterControlPlaneEndpointsConfigIpEndpointsConfigArgs]
    ]: ...
    @ip_endpoints_config.setter
    def ip_endpoints_config(
        self,
        value: Optional[
            pulumi.Input[ClusterControlPlaneEndpointsConfigIpEndpointsConfigArgs]
        ],
    ): ...

class ClusterControlPlaneEndpointsConfigDnsEndpointConfigArgsDict(TypedDict):
    allow_external_traffic: NotRequired[pulumi.Input[_builtins.bool]]
    enable_k8s_certs_via_dns: NotRequired[pulumi.Input[_builtins.bool]]
    enable_k8s_tokens_via_dns: NotRequired[pulumi.Input[_builtins.bool]]
    endpoint: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterControlPlaneEndpointsConfigDnsEndpointConfigArgs:
    def __init__(
        __self__,
        *,
        allow_external_traffic: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_k8s_certs_via_dns: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_k8s_tokens_via_dns: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowExternalTraffic")
    def allow_external_traffic(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_external_traffic.setter
    def allow_external_traffic(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableK8sCertsViaDns")
    def enable_k8s_certs_via_dns(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_k8s_certs_via_dns.setter
    def enable_k8s_certs_via_dns(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableK8sTokensViaDns")
    def enable_k8s_tokens_via_dns(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_k8s_tokens_via_dns.setter
    def enable_k8s_tokens_via_dns(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterControlPlaneEndpointsConfigIpEndpointsConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterControlPlaneEndpointsConfigIpEndpointsConfigArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClusterCostManagementConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterCostManagementConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterDatabaseEncryptionArgsDict(TypedDict):
    state: pulumi.Input[_builtins.str]
    key_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterDatabaseEncryptionArgs:
    def __init__(
        __self__,
        *,
        state: pulumi.Input[_builtins.str],
        key_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]: ...
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterDefaultSnatStatusArgsDict(TypedDict):
    disabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterDefaultSnatStatusArgs:
    def __init__(__self__, *, disabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Input[_builtins.bool]: ...
    @disabled.setter
    def disabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterDnsConfigArgsDict(TypedDict):
    additive_vpc_scope_dns_domain: NotRequired[pulumi.Input[_builtins.str]]
    cluster_dns: NotRequired[pulumi.Input[_builtins.str]]
    cluster_dns_domain: NotRequired[pulumi.Input[_builtins.str]]
    cluster_dns_scope: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterDnsConfigArgs:
    def __init__(
        __self__,
        *,
        additive_vpc_scope_dns_domain: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_dns: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_dns_domain: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_dns_scope: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additiveVpcScopeDnsDomain")
    def additive_vpc_scope_dns_domain(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additive_vpc_scope_dns_domain.setter
    def additive_vpc_scope_dns_domain(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterDns")
    def cluster_dns(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_dns.setter
    def cluster_dns(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterDnsDomain")
    def cluster_dns_domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_dns_domain.setter
    def cluster_dns_domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterDnsScope")
    def cluster_dns_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_dns_scope.setter
    def cluster_dns_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterEnableK8sBetaApisArgsDict(TypedDict):
    enabled_apis: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ClusterEnableK8sBetaApisArgs:
    def __init__(
        __self__, *, enabled_apis: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledApis")
    def enabled_apis(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @enabled_apis.setter
    def enabled_apis(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class ClusterEnterpriseConfigArgsDict(TypedDict):
    cluster_tier: NotRequired[pulumi.Input[_builtins.str]]
    desired_tier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterEnterpriseConfigArgs:
    def __init__(
        __self__,
        *,
        cluster_tier: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_tier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterTier")
    @_utilities.deprecated(...)
    def cluster_tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_tier.setter
    def cluster_tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="desiredTier")
    @_utilities.deprecated(...)
    def desired_tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_tier.setter
    def desired_tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterFleetArgsDict(TypedDict):
    membership: NotRequired[pulumi.Input[_builtins.str]]
    membership_id: NotRequired[pulumi.Input[_builtins.str]]
    membership_location: NotRequired[pulumi.Input[_builtins.str]]
    membership_type: NotRequired[pulumi.Input[_builtins.str]]
    pre_registered: NotRequired[pulumi.Input[_builtins.bool]]
    project: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterFleetArgs:
    def __init__(
        __self__,
        *,
        membership: Optional[pulumi.Input[_builtins.str]] = ...,
        membership_id: Optional[pulumi.Input[_builtins.str]] = ...,
        membership_location: Optional[pulumi.Input[_builtins.str]] = ...,
        membership_type: Optional[pulumi.Input[_builtins.str]] = ...,
        pre_registered: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership.setter
    def membership(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="membershipId")
    def membership_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership_id.setter
    def membership_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="membershipLocation")
    def membership_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership_location.setter
    def membership_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="membershipType")
    def membership_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership_type.setter
    def membership_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preRegistered")
    def pre_registered(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @pre_registered.setter
    def pre_registered(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterGatewayApiConfigArgsDict(TypedDict):
    channel: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterGatewayApiConfigArgs:
    def __init__(__self__, *, channel: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> pulumi.Input[_builtins.str]: ...
    @channel.setter
    def channel(self, value: pulumi.Input[_builtins.str]): ...

class ClusterGkeAutoUpgradeConfigArgsDict(TypedDict):
    patch_mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterGkeAutoUpgradeConfigArgs:
    def __init__(__self__, *, patch_mode: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> pulumi.Input[_builtins.str]: ...
    @patch_mode.setter
    def patch_mode(self, value: pulumi.Input[_builtins.str]): ...

class ClusterIdentityServiceConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterIdentityServiceConfigArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClusterIpAllocationPolicyArgsDict(TypedDict):
    additional_ip_ranges_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClusterIpAllocationPolicyAdditionalIpRangesConfigArgsDict]
            ]
        ]
    ]
    additional_pod_ranges_config: NotRequired[
        pulumi.Input[ClusterIpAllocationPolicyAdditionalPodRangesConfigArgsDict]
    ]
    auto_ipam_config: NotRequired[
        pulumi.Input[ClusterIpAllocationPolicyAutoIpamConfigArgsDict]
    ]
    cluster_ipv4_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    cluster_secondary_range_name: NotRequired[pulumi.Input[_builtins.str]]
    network_tier_config: NotRequired[
        pulumi.Input[ClusterIpAllocationPolicyNetworkTierConfigArgsDict]
    ]
    pod_cidr_overprovision_config: NotRequired[
        pulumi.Input[ClusterIpAllocationPolicyPodCidrOverprovisionConfigArgsDict]
    ]
    services_ipv4_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    services_secondary_range_name: NotRequired[pulumi.Input[_builtins.str]]
    stack_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterIpAllocationPolicyArgs:
    def __init__(
        __self__,
        *,
        additional_ip_ranges_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClusterIpAllocationPolicyAdditionalIpRangesConfigArgs]
                ]
            ]
        ] = ...,
        additional_pod_ranges_config: Optional[
            pulumi.Input[ClusterIpAllocationPolicyAdditionalPodRangesConfigArgs]
        ] = ...,
        auto_ipam_config: Optional[
            pulumi.Input[ClusterIpAllocationPolicyAutoIpamConfigArgs]
        ] = ...,
        cluster_ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_secondary_range_name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_tier_config: Optional[
            pulumi.Input[ClusterIpAllocationPolicyNetworkTierConfigArgs]
        ] = ...,
        pod_cidr_overprovision_config: Optional[
            pulumi.Input[ClusterIpAllocationPolicyPodCidrOverprovisionConfigArgs]
        ] = ...,
        services_ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        services_secondary_range_name: Optional[pulumi.Input[_builtins.str]] = ...,
        stack_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalIpRangesConfigs")
    def additional_ip_ranges_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClusterIpAllocationPolicyAdditionalIpRangesConfigArgs]
            ]
        ]
    ]: ...
    @additional_ip_ranges_configs.setter
    def additional_ip_ranges_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClusterIpAllocationPolicyAdditionalIpRangesConfigArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalPodRangesConfig")
    def additional_pod_ranges_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterIpAllocationPolicyAdditionalPodRangesConfigArgs]
    ]: ...
    @additional_pod_ranges_config.setter
    def additional_pod_ranges_config(
        self,
        value: Optional[
            pulumi.Input[ClusterIpAllocationPolicyAdditionalPodRangesConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoIpamConfig")
    def auto_ipam_config(
        self,
    ) -> Optional[pulumi.Input[ClusterIpAllocationPolicyAutoIpamConfigArgs]]: ...
    @auto_ipam_config.setter
    def auto_ipam_config(
        self, value: Optional[pulumi.Input[ClusterIpAllocationPolicyAutoIpamConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterIpv4CidrBlock")
    def cluster_ipv4_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_ipv4_cidr_block.setter
    def cluster_ipv4_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterSecondaryRangeName")
    def cluster_secondary_range_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_secondary_range_name.setter
    def cluster_secondary_range_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkTierConfig")
    def network_tier_config(
        self,
    ) -> Optional[pulumi.Input[ClusterIpAllocationPolicyNetworkTierConfigArgs]]: ...
    @network_tier_config.setter
    def network_tier_config(
        self,
        value: Optional[pulumi.Input[ClusterIpAllocationPolicyNetworkTierConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="podCidrOverprovisionConfig")
    def pod_cidr_overprovision_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterIpAllocationPolicyPodCidrOverprovisionConfigArgs]
    ]: ...
    @pod_cidr_overprovision_config.setter
    def pod_cidr_overprovision_config(
        self,
        value: Optional[
            pulumi.Input[ClusterIpAllocationPolicyPodCidrOverprovisionConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="servicesIpv4CidrBlock")
    def services_ipv4_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @services_ipv4_cidr_block.setter
    def services_ipv4_cidr_block(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="servicesSecondaryRangeName")
    def services_secondary_range_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @services_secondary_range_name.setter
    def services_secondary_range_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stack_type.setter
    def stack_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterIpAllocationPolicyAdditionalIpRangesConfigArgsDict(TypedDict):
    subnetwork: pulumi.Input[_builtins.str]
    pod_ipv4_range_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterIpAllocationPolicyAdditionalIpRangesConfigArgs:
    def __init__(
        __self__,
        *,
        subnetwork: pulumi.Input[_builtins.str],
        pod_ipv4_range_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> pulumi.Input[_builtins.str]: ...
    @subnetwork.setter
    def subnetwork(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="podIpv4RangeNames")
    def pod_ipv4_range_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @pod_ipv4_range_names.setter
    def pod_ipv4_range_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterIpAllocationPolicyAdditionalPodRangesConfigArgsDict(TypedDict):
    pod_range_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ClusterIpAllocationPolicyAdditionalPodRangesConfigArgs:
    def __init__(
        __self__,
        *,
        pod_range_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="podRangeNames")
    def pod_range_names(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @pod_range_names.setter
    def pod_range_names(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class ClusterIpAllocationPolicyAutoIpamConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterIpAllocationPolicyAutoIpamConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterIpAllocationPolicyNetworkTierConfigArgsDict(TypedDict):
    network_tier: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterIpAllocationPolicyNetworkTierConfigArgs:
    def __init__(__self__, *, network_tier: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> pulumi.Input[_builtins.str]: ...
    @network_tier.setter
    def network_tier(self, value: pulumi.Input[_builtins.str]): ...

class ClusterIpAllocationPolicyPodCidrOverprovisionConfigArgsDict(TypedDict):
    disabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterIpAllocationPolicyPodCidrOverprovisionConfigArgs:
    def __init__(__self__, *, disabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Input[_builtins.bool]: ...
    @disabled.setter
    def disabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterLoggingConfigArgsDict(TypedDict):
    enable_components: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ClusterLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        enable_components: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableComponents")
    def enable_components(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @enable_components.setter
    def enable_components(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class ClusterMaintenancePolicyArgsDict(TypedDict):
    daily_maintenance_window: NotRequired[
        pulumi.Input[ClusterMaintenancePolicyDailyMaintenanceWindowArgsDict]
    ]
    disruption_budget: NotRequired[
        pulumi.Input[ClusterMaintenancePolicyDisruptionBudgetArgsDict]
    ]
    maintenance_exclusions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterMaintenancePolicyMaintenanceExclusionArgsDict]]
        ]
    ]
    recurring_window: NotRequired[
        pulumi.Input[ClusterMaintenancePolicyRecurringWindowArgsDict]
    ]

@pulumi.input_type
class ClusterMaintenancePolicyArgs:
    def __init__(
        __self__,
        *,
        daily_maintenance_window: Optional[
            pulumi.Input[ClusterMaintenancePolicyDailyMaintenanceWindowArgs]
        ] = ...,
        disruption_budget: Optional[
            pulumi.Input[ClusterMaintenancePolicyDisruptionBudgetArgs]
        ] = ...,
        maintenance_exclusions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterMaintenancePolicyMaintenanceExclusionArgs]]
            ]
        ] = ...,
        recurring_window: Optional[
            pulumi.Input[ClusterMaintenancePolicyRecurringWindowArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dailyMaintenanceWindow")
    def daily_maintenance_window(
        self,
    ) -> Optional[pulumi.Input[ClusterMaintenancePolicyDailyMaintenanceWindowArgs]]: ...
    @daily_maintenance_window.setter
    def daily_maintenance_window(
        self,
        value: Optional[
            pulumi.Input[ClusterMaintenancePolicyDailyMaintenanceWindowArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="disruptionBudget")
    def disruption_budget(
        self,
    ) -> Optional[pulumi.Input[ClusterMaintenancePolicyDisruptionBudgetArgs]]: ...
    @disruption_budget.setter
    def disruption_budget(
        self,
        value: Optional[pulumi.Input[ClusterMaintenancePolicyDisruptionBudgetArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceExclusions")
    def maintenance_exclusions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterMaintenancePolicyMaintenanceExclusionArgs]]
        ]
    ]: ...
    @maintenance_exclusions.setter
    def maintenance_exclusions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterMaintenancePolicyMaintenanceExclusionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="recurringWindow")
    def recurring_window(
        self,
    ) -> Optional[pulumi.Input[ClusterMaintenancePolicyRecurringWindowArgs]]: ...
    @recurring_window.setter
    def recurring_window(
        self, value: Optional[pulumi.Input[ClusterMaintenancePolicyRecurringWindowArgs]]
    ): ...

class ClusterMaintenancePolicyDailyMaintenanceWindowArgsDict(TypedDict):
    start_time: pulumi.Input[_builtins.str]
    duration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterMaintenancePolicyDailyMaintenanceWindowArgs:
    def __init__(
        __self__,
        *,
        start_time: pulumi.Input[_builtins.str],
        duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[_builtins.str]: ...
    @start_time.setter
    def start_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterMaintenancePolicyDisruptionBudgetArgsDict(TypedDict):
    last_disruption_time: NotRequired[pulumi.Input[_builtins.str]]
    last_minor_version_disruption_time: NotRequired[pulumi.Input[_builtins.str]]
    minor_version_disruption_interval: NotRequired[pulumi.Input[_builtins.str]]
    patch_version_disruption_interval: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterMaintenancePolicyDisruptionBudgetArgs:
    def __init__(
        __self__,
        *,
        last_disruption_time: Optional[pulumi.Input[_builtins.str]] = ...,
        last_minor_version_disruption_time: Optional[pulumi.Input[_builtins.str]] = ...,
        minor_version_disruption_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        patch_version_disruption_interval: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastDisruptionTime")
    def last_disruption_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_disruption_time.setter
    def last_disruption_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastMinorVersionDisruptionTime")
    def last_minor_version_disruption_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_minor_version_disruption_time.setter
    def last_minor_version_disruption_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minorVersionDisruptionInterval")
    def minor_version_disruption_interval(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @minor_version_disruption_interval.setter
    def minor_version_disruption_interval(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="patchVersionDisruptionInterval")
    def patch_version_disruption_interval(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @patch_version_disruption_interval.setter
    def patch_version_disruption_interval(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterMaintenancePolicyMaintenanceExclusionArgsDict(TypedDict):
    exclusion_name: pulumi.Input[_builtins.str]
    start_time: pulumi.Input[_builtins.str]
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    exclusion_options: NotRequired[
        pulumi.Input[
            ClusterMaintenancePolicyMaintenanceExclusionExclusionOptionsArgsDict
        ]
    ]

@pulumi.input_type
class ClusterMaintenancePolicyMaintenanceExclusionArgs:
    def __init__(
        __self__,
        *,
        exclusion_name: pulumi.Input[_builtins.str],
        start_time: pulumi.Input[_builtins.str],
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        exclusion_options: Optional[
            pulumi.Input[
                ClusterMaintenancePolicyMaintenanceExclusionExclusionOptionsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exclusionName")
    def exclusion_name(self) -> pulumi.Input[_builtins.str]: ...
    @exclusion_name.setter
    def exclusion_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[_builtins.str]: ...
    @start_time.setter
    def start_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="exclusionOptions")
    def exclusion_options(
        self,
    ) -> Optional[
        pulumi.Input[ClusterMaintenancePolicyMaintenanceExclusionExclusionOptionsArgs]
    ]: ...
    @exclusion_options.setter
    def exclusion_options(
        self,
        value: Optional[
            pulumi.Input[
                ClusterMaintenancePolicyMaintenanceExclusionExclusionOptionsArgs
            ]
        ],
    ): ...

class ClusterMaintenancePolicyMaintenanceExclusionExclusionOptionsArgsDict(TypedDict):
    scope: pulumi.Input[_builtins.str]
    end_time_behavior: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterMaintenancePolicyMaintenanceExclusionExclusionOptionsArgs:
    def __init__(
        __self__,
        *,
        scope: pulumi.Input[_builtins.str],
        end_time_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endTimeBehavior")
    def end_time_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time_behavior.setter
    def end_time_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterMaintenancePolicyRecurringWindowArgsDict(TypedDict):
    end_time: pulumi.Input[_builtins.str]
    recurrence: pulumi.Input[_builtins.str]
    start_time: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterMaintenancePolicyRecurringWindowArgs:
    def __init__(
        __self__,
        *,
        end_time: pulumi.Input[_builtins.str],
        recurrence: pulumi.Input[_builtins.str],
        start_time: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Input[_builtins.str]: ...
    @end_time.setter
    def end_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> pulumi.Input[_builtins.str]: ...
    @recurrence.setter
    def recurrence(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[_builtins.str]: ...
    @start_time.setter
    def start_time(self, value: pulumi.Input[_builtins.str]): ...

class ClusterManagedOpentelemetryConfigArgsDict(TypedDict):
    scope: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterManagedOpentelemetryConfigArgs:
    def __init__(
        __self__, *, scope: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterMasterAuthArgsDict(TypedDict):
    client_certificate_config: pulumi.Input[
        ClusterMasterAuthClientCertificateConfigArgsDict
    ]
    client_certificate: NotRequired[pulumi.Input[_builtins.str]]
    client_key: NotRequired[pulumi.Input[_builtins.str]]
    cluster_ca_certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterMasterAuthArgs:
    def __init__(
        __self__,
        *,
        client_certificate_config: pulumi.Input[
            ClusterMasterAuthClientCertificateConfigArgs
        ],
        client_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        client_key: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_ca_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificateConfig")
    def client_certificate_config(
        self,
    ) -> pulumi.Input[ClusterMasterAuthClientCertificateConfigArgs]: ...
    @client_certificate_config.setter
    def client_certificate_config(
        self, value: pulumi.Input[ClusterMasterAuthClientCertificateConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_certificate.setter
    def client_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_key.setter
    def client_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterCaCertificate")
    def cluster_ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_ca_certificate.setter
    def cluster_ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterMasterAuthClientCertificateConfigArgsDict(TypedDict):
    issue_client_certificate: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterMasterAuthClientCertificateConfigArgs:
    def __init__(
        __self__, *, issue_client_certificate: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="issueClientCertificate")
    def issue_client_certificate(self) -> pulumi.Input[_builtins.bool]: ...
    @issue_client_certificate.setter
    def issue_client_certificate(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterMasterAuthorizedNetworksConfigArgsDict(TypedDict):
    cidr_blocks: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClusterMasterAuthorizedNetworksConfigCidrBlockArgsDict]
            ]
        ]
    ]
    gcp_public_cidrs_access_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    private_endpoint_enforcement_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterMasterAuthorizedNetworksConfigArgs:
    def __init__(
        __self__,
        *,
        cidr_blocks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClusterMasterAuthorizedNetworksConfigCidrBlockArgs]
                ]
            ]
        ] = ...,
        gcp_public_cidrs_access_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        private_endpoint_enforcement_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterMasterAuthorizedNetworksConfigCidrBlockArgs]]
        ]
    ]: ...
    @cidr_blocks.setter
    def cidr_blocks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClusterMasterAuthorizedNetworksConfigCidrBlockArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gcpPublicCidrsAccessEnabled")
    def gcp_public_cidrs_access_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @gcp_public_cidrs_access_enabled.setter
    def gcp_public_cidrs_access_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointEnforcementEnabled")
    def private_endpoint_enforcement_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @private_endpoint_enforcement_enabled.setter
    def private_endpoint_enforcement_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ClusterMasterAuthorizedNetworksConfigCidrBlockArgsDict(TypedDict):
    cidr_block: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterMasterAuthorizedNetworksConfigCidrBlockArgs:
    def __init__(
        __self__,
        *,
        cidr_block: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Input[_builtins.str]: ...
    @cidr_block.setter
    def cidr_block(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterMeshCertificatesArgsDict(TypedDict):
    enable_certificates: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterMeshCertificatesArgs:
    def __init__(
        __self__, *, enable_certificates: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableCertificates")
    def enable_certificates(self) -> pulumi.Input[_builtins.bool]: ...
    @enable_certificates.setter
    def enable_certificates(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterMonitoringConfigArgsDict(TypedDict):
    advanced_datapath_observability_config: NotRequired[
        pulumi.Input[ClusterMonitoringConfigAdvancedDatapathObservabilityConfigArgsDict]
    ]
    enable_components: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    managed_prometheus: NotRequired[
        pulumi.Input[ClusterMonitoringConfigManagedPrometheusArgsDict]
    ]

@pulumi.input_type
class ClusterMonitoringConfigArgs:
    def __init__(
        __self__,
        *,
        advanced_datapath_observability_config: Optional[
            pulumi.Input[ClusterMonitoringConfigAdvancedDatapathObservabilityConfigArgs]
        ] = ...,
        enable_components: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        managed_prometheus: Optional[
            pulumi.Input[ClusterMonitoringConfigManagedPrometheusArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedDatapathObservabilityConfig")
    def advanced_datapath_observability_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterMonitoringConfigAdvancedDatapathObservabilityConfigArgs]
    ]: ...
    @advanced_datapath_observability_config.setter
    def advanced_datapath_observability_config(
        self,
        value: Optional[
            pulumi.Input[ClusterMonitoringConfigAdvancedDatapathObservabilityConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableComponents")
    def enable_components(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enable_components.setter
    def enable_components(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedPrometheus")
    def managed_prometheus(
        self,
    ) -> Optional[pulumi.Input[ClusterMonitoringConfigManagedPrometheusArgs]]: ...
    @managed_prometheus.setter
    def managed_prometheus(
        self,
        value: Optional[pulumi.Input[ClusterMonitoringConfigManagedPrometheusArgs]],
    ): ...

class ClusterMonitoringConfigAdvancedDatapathObservabilityConfigArgsDict(TypedDict):
    enable_metrics: pulumi.Input[_builtins.bool]
    enable_relay: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterMonitoringConfigAdvancedDatapathObservabilityConfigArgs:
    def __init__(
        __self__,
        *,
        enable_metrics: pulumi.Input[_builtins.bool],
        enable_relay: pulumi.Input[_builtins.bool],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableMetrics")
    def enable_metrics(self) -> pulumi.Input[_builtins.bool]: ...
    @enable_metrics.setter
    def enable_metrics(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="enableRelay")
    def enable_relay(self) -> pulumi.Input[_builtins.bool]: ...
    @enable_relay.setter
    def enable_relay(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterMonitoringConfigManagedPrometheusArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    auto_monitoring_config: NotRequired[
        pulumi.Input[
            ClusterMonitoringConfigManagedPrometheusAutoMonitoringConfigArgsDict
        ]
    ]

@pulumi.input_type
class ClusterMonitoringConfigManagedPrometheusArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        auto_monitoring_config: Optional[
            pulumi.Input[
                ClusterMonitoringConfigManagedPrometheusAutoMonitoringConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="autoMonitoringConfig")
    def auto_monitoring_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterMonitoringConfigManagedPrometheusAutoMonitoringConfigArgs]
    ]: ...
    @auto_monitoring_config.setter
    def auto_monitoring_config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterMonitoringConfigManagedPrometheusAutoMonitoringConfigArgs
            ]
        ],
    ): ...

class ClusterMonitoringConfigManagedPrometheusAutoMonitoringConfigArgsDict(TypedDict):
    scope: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterMonitoringConfigManagedPrometheusAutoMonitoringConfigArgs:
    def __init__(__self__, *, scope: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...

class ClusterNetworkPerformanceConfigArgsDict(TypedDict):
    total_egress_bandwidth_tier: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterNetworkPerformanceConfigArgs:
    def __init__(
        __self__, *, total_egress_bandwidth_tier: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="totalEgressBandwidthTier")
    def total_egress_bandwidth_tier(self) -> pulumi.Input[_builtins.str]: ...
    @total_egress_bandwidth_tier.setter
    def total_egress_bandwidth_tier(self, value: pulumi.Input[_builtins.str]): ...

class ClusterNetworkPolicyArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    provider: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNetworkPolicyArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        provider: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provider.setter
    def provider(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodeConfigArgsDict(TypedDict):
    advanced_machine_features: NotRequired[
        pulumi.Input[ClusterNodeConfigAdvancedMachineFeaturesArgsDict]
    ]
    boot_disk: NotRequired[pulumi.Input[ClusterNodeConfigBootDiskArgsDict]]
    boot_disk_kms_key: NotRequired[pulumi.Input[_builtins.str]]
    confidential_nodes: NotRequired[
        pulumi.Input[ClusterNodeConfigConfidentialNodesArgsDict]
    ]
    containerd_config: NotRequired[
        pulumi.Input[ClusterNodeConfigContainerdConfigArgsDict]
    ]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    disk_type: NotRequired[pulumi.Input[_builtins.str]]
    effective_taints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigEffectiveTaintArgsDict]]]
    ]
    enable_confidential_storage: NotRequired[pulumi.Input[_builtins.bool]]
    ephemeral_storage_config: NotRequired[
        pulumi.Input[ClusterNodeConfigEphemeralStorageConfigArgsDict]
    ]
    ephemeral_storage_local_ssd_config: NotRequired[
        pulumi.Input[ClusterNodeConfigEphemeralStorageLocalSsdConfigArgsDict]
    ]
    fast_socket: NotRequired[pulumi.Input[ClusterNodeConfigFastSocketArgsDict]]
    flex_start: NotRequired[pulumi.Input[_builtins.bool]]
    gcfs_config: NotRequired[pulumi.Input[ClusterNodeConfigGcfsConfigArgsDict]]
    guest_accelerators: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigGuestAcceleratorArgsDict]]]
    ]
    gvnic: NotRequired[pulumi.Input[ClusterNodeConfigGvnicArgsDict]]
    host_maintenance_policy: NotRequired[
        pulumi.Input[ClusterNodeConfigHostMaintenancePolicyArgsDict]
    ]
    image_type: NotRequired[pulumi.Input[_builtins.str]]
    kubelet_config: NotRequired[pulumi.Input[ClusterNodeConfigKubeletConfigArgsDict]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    linux_node_config: NotRequired[
        pulumi.Input[ClusterNodeConfigLinuxNodeConfigArgsDict]
    ]
    local_nvme_ssd_block_config: NotRequired[
        pulumi.Input[ClusterNodeConfigLocalNvmeSsdBlockConfigArgsDict]
    ]
    local_ssd_count: NotRequired[pulumi.Input[_builtins.int]]
    local_ssd_encryption_mode: NotRequired[pulumi.Input[_builtins.str]]
    logging_variant: NotRequired[pulumi.Input[_builtins.str]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    max_run_duration: NotRequired[pulumi.Input[_builtins.str]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    min_cpu_platform: NotRequired[pulumi.Input[_builtins.str]]
    node_group: NotRequired[pulumi.Input[_builtins.str]]
    oauth_scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    preemptible: NotRequired[pulumi.Input[_builtins.bool]]
    reservation_affinity: NotRequired[
        pulumi.Input[ClusterNodeConfigReservationAffinityArgsDict]
    ]
    resource_labels: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    resource_manager_tags: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    sandbox_config: NotRequired[pulumi.Input[ClusterNodeConfigSandboxConfigArgsDict]]
    secondary_boot_disks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigSecondaryBootDiskArgsDict]]]
    ]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    shielded_instance_config: NotRequired[
        pulumi.Input[ClusterNodeConfigShieldedInstanceConfigArgsDict]
    ]
    sole_tenant_config: NotRequired[
        pulumi.Input[ClusterNodeConfigSoleTenantConfigArgsDict]
    ]
    spot: NotRequired[pulumi.Input[_builtins.bool]]
    storage_pools: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    taints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigTaintArgsDict]]]
    ]
    windows_node_config: NotRequired[
        pulumi.Input[ClusterNodeConfigWindowsNodeConfigArgsDict]
    ]
    workload_metadata_config: NotRequired[
        pulumi.Input[ClusterNodeConfigWorkloadMetadataConfigArgsDict]
    ]

@pulumi.input_type
class ClusterNodeConfigArgs:
    def __init__(
        __self__,
        *,
        advanced_machine_features: Optional[
            pulumi.Input[ClusterNodeConfigAdvancedMachineFeaturesArgs]
        ] = ...,
        boot_disk: Optional[pulumi.Input[ClusterNodeConfigBootDiskArgs]] = ...,
        boot_disk_kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        confidential_nodes: Optional[
            pulumi.Input[ClusterNodeConfigConfidentialNodesArgs]
        ] = ...,
        containerd_config: Optional[
            pulumi.Input[ClusterNodeConfigContainerdConfigArgs]
        ] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_taints: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigEffectiveTaintArgs]]]
        ] = ...,
        enable_confidential_storage: Optional[pulumi.Input[_builtins.bool]] = ...,
        ephemeral_storage_config: Optional[
            pulumi.Input[ClusterNodeConfigEphemeralStorageConfigArgs]
        ] = ...,
        ephemeral_storage_local_ssd_config: Optional[
            pulumi.Input[ClusterNodeConfigEphemeralStorageLocalSsdConfigArgs]
        ] = ...,
        fast_socket: Optional[pulumi.Input[ClusterNodeConfigFastSocketArgs]] = ...,
        flex_start: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcfs_config: Optional[pulumi.Input[ClusterNodeConfigGcfsConfigArgs]] = ...,
        guest_accelerators: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigGuestAcceleratorArgs]]]
        ] = ...,
        gvnic: Optional[pulumi.Input[ClusterNodeConfigGvnicArgs]] = ...,
        host_maintenance_policy: Optional[
            pulumi.Input[ClusterNodeConfigHostMaintenancePolicyArgs]
        ] = ...,
        image_type: Optional[pulumi.Input[_builtins.str]] = ...,
        kubelet_config: Optional[
            pulumi.Input[ClusterNodeConfigKubeletConfigArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        linux_node_config: Optional[
            pulumi.Input[ClusterNodeConfigLinuxNodeConfigArgs]
        ] = ...,
        local_nvme_ssd_block_config: Optional[
            pulumi.Input[ClusterNodeConfigLocalNvmeSsdBlockConfigArgs]
        ] = ...,
        local_ssd_count: Optional[pulumi.Input[_builtins.int]] = ...,
        local_ssd_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_variant: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        max_run_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        node_group: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        preemptible: Optional[pulumi.Input[_builtins.bool]] = ...,
        reservation_affinity: Optional[
            pulumi.Input[ClusterNodeConfigReservationAffinityArgs]
        ] = ...,
        resource_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_manager_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        sandbox_config: Optional[
            pulumi.Input[ClusterNodeConfigSandboxConfigArgs]
        ] = ...,
        secondary_boot_disks: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigSecondaryBootDiskArgs]]]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[ClusterNodeConfigShieldedInstanceConfigArgs]
        ] = ...,
        sole_tenant_config: Optional[
            pulumi.Input[ClusterNodeConfigSoleTenantConfigArgs]
        ] = ...,
        spot: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_pools: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        taints: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigTaintArgs]]]
        ] = ...,
        windows_node_config: Optional[
            pulumi.Input[ClusterNodeConfigWindowsNodeConfigArgs]
        ] = ...,
        workload_metadata_config: Optional[
            pulumi.Input[ClusterNodeConfigWorkloadMetadataConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigAdvancedMachineFeaturesArgs]]: ...
    @advanced_machine_features.setter
    def advanced_machine_features(
        self,
        value: Optional[pulumi.Input[ClusterNodeConfigAdvancedMachineFeaturesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bootDisk")
    def boot_disk(self) -> Optional[pulumi.Input[ClusterNodeConfigBootDiskArgs]]: ...
    @boot_disk.setter
    def boot_disk(
        self, value: Optional[pulumi.Input[ClusterNodeConfigBootDiskArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bootDiskKmsKey")
    def boot_disk_kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @boot_disk_kms_key.setter
    def boot_disk_kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="confidentialNodes")
    def confidential_nodes(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigConfidentialNodesArgs]]: ...
    @confidential_nodes.setter
    def confidential_nodes(
        self, value: Optional[pulumi.Input[ClusterNodeConfigConfidentialNodesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerdConfig")
    def containerd_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigContainerdConfigArgs]]: ...
    @containerd_config.setter
    def containerd_config(
        self, value: Optional[pulumi.Input[ClusterNodeConfigContainerdConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveTaints")
    def effective_taints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigEffectiveTaintArgs]]]
    ]: ...
    @effective_taints.setter
    def effective_taints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigEffectiveTaintArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableConfidentialStorage")
    def enable_confidential_storage(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_confidential_storage.setter
    def enable_confidential_storage(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageConfig")
    def ephemeral_storage_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigEphemeralStorageConfigArgs]]: ...
    @ephemeral_storage_config.setter
    def ephemeral_storage_config(
        self, value: Optional[pulumi.Input[ClusterNodeConfigEphemeralStorageConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageLocalSsdConfig")
    def ephemeral_storage_local_ssd_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodeConfigEphemeralStorageLocalSsdConfigArgs]
    ]: ...
    @ephemeral_storage_local_ssd_config.setter
    def ephemeral_storage_local_ssd_config(
        self,
        value: Optional[
            pulumi.Input[ClusterNodeConfigEphemeralStorageLocalSsdConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fastSocket")
    def fast_socket(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigFastSocketArgs]]: ...
    @fast_socket.setter
    def fast_socket(
        self, value: Optional[pulumi.Input[ClusterNodeConfigFastSocketArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="flexStart")
    def flex_start(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @flex_start.setter
    def flex_start(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="gcfsConfig")
    def gcfs_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigGcfsConfigArgs]]: ...
    @gcfs_config.setter
    def gcfs_config(
        self, value: Optional[pulumi.Input[ClusterNodeConfigGcfsConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigGuestAcceleratorArgs]]]
    ]: ...
    @guest_accelerators.setter
    def guest_accelerators(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigGuestAcceleratorArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def gvnic(self) -> Optional[pulumi.Input[ClusterNodeConfigGvnicArgs]]: ...
    @gvnic.setter
    def gvnic(self, value: Optional[pulumi.Input[ClusterNodeConfigGvnicArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="hostMaintenancePolicy")
    def host_maintenance_policy(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigHostMaintenancePolicyArgs]]: ...
    @host_maintenance_policy.setter
    def host_maintenance_policy(
        self, value: Optional[pulumi.Input[ClusterNodeConfigHostMaintenancePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_type.setter
    def image_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigKubeletConfigArgs]]: ...
    @kubelet_config.setter
    def kubelet_config(
        self, value: Optional[pulumi.Input[ClusterNodeConfigKubeletConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linuxNodeConfig")
    def linux_node_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigLinuxNodeConfigArgs]]: ...
    @linux_node_config.setter
    def linux_node_config(
        self, value: Optional[pulumi.Input[ClusterNodeConfigLinuxNodeConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="localNvmeSsdBlockConfig")
    def local_nvme_ssd_block_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigLocalNvmeSsdBlockConfigArgs]]: ...
    @local_nvme_ssd_block_config.setter
    def local_nvme_ssd_block_config(
        self,
        value: Optional[pulumi.Input[ClusterNodeConfigLocalNvmeSsdBlockConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @local_ssd_count.setter
    def local_ssd_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="localSsdEncryptionMode")
    def local_ssd_encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_ssd_encryption_mode.setter
    def local_ssd_encryption_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingVariant")
    def logging_variant(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logging_variant.setter
    def logging_variant(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRunDuration")
    def max_run_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_run_duration.setter
    def max_run_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeGroup")
    def node_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_group.setter
    def node_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @oauth_scopes.setter
    def oauth_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def preemptible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preemptible.setter
    def preemptible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigReservationAffinityArgs]]: ...
    @reservation_affinity.setter
    def reservation_affinity(
        self, value: Optional[pulumi.Input[ClusterNodeConfigReservationAffinityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceLabels")
    def resource_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @resource_labels.setter
    def resource_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @resource_manager_tags.setter
    def resource_manager_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sandboxConfig")
    def sandbox_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigSandboxConfigArgs]]: ...
    @sandbox_config.setter
    def sandbox_config(
        self, value: Optional[pulumi.Input[ClusterNodeConfigSandboxConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secondaryBootDisks")
    def secondary_boot_disks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigSecondaryBootDiskArgs]]]
    ]: ...
    @secondary_boot_disks.setter
    def secondary_boot_disks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigSecondaryBootDiskArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigShieldedInstanceConfigArgs]]: ...
    @shielded_instance_config.setter
    def shielded_instance_config(
        self, value: Optional[pulumi.Input[ClusterNodeConfigShieldedInstanceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="soleTenantConfig")
    def sole_tenant_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigSoleTenantConfigArgs]]: ...
    @sole_tenant_config.setter
    def sole_tenant_config(
        self, value: Optional[pulumi.Input[ClusterNodeConfigSoleTenantConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def spot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @spot.setter
    def spot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="storagePools")
    def storage_pools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @storage_pools.setter
    def storage_pools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def taints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigTaintArgs]]]]: ...
    @taints.setter
    def taints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterNodeConfigTaintArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="windowsNodeConfig")
    def windows_node_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigWindowsNodeConfigArgs]]: ...
    @windows_node_config.setter
    def windows_node_config(
        self, value: Optional[pulumi.Input[ClusterNodeConfigWindowsNodeConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workloadMetadataConfig")
    def workload_metadata_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigWorkloadMetadataConfigArgs]]: ...
    @workload_metadata_config.setter
    def workload_metadata_config(
        self, value: Optional[pulumi.Input[ClusterNodeConfigWorkloadMetadataConfigArgs]]
    ): ...

class ClusterNodeConfigAdvancedMachineFeaturesArgsDict(TypedDict):
    threads_per_core: pulumi.Input[_builtins.int]
    enable_nested_virtualization: NotRequired[pulumi.Input[_builtins.bool]]
    performance_monitoring_unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigAdvancedMachineFeaturesArgs:
    def __init__(
        __self__,
        *,
        threads_per_core: pulumi.Input[_builtins.int],
        enable_nested_virtualization: Optional[pulumi.Input[_builtins.bool]] = ...,
        performance_monitoring_unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> pulumi.Input[_builtins.int]: ...
    @threads_per_core.setter
    def threads_per_core(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_nested_virtualization.setter
    def enable_nested_virtualization(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceMonitoringUnit")
    def performance_monitoring_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @performance_monitoring_unit.setter
    def performance_monitoring_unit(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodeConfigBootDiskArgsDict(TypedDict):
    disk_type: NotRequired[pulumi.Input[_builtins.str]]
    provisioned_iops: NotRequired[pulumi.Input[_builtins.int]]
    provisioned_throughput: NotRequired[pulumi.Input[_builtins.int]]
    size_gb: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterNodeConfigBootDiskArgs:
    def __init__(
        __self__,
        *,
        disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_iops: Optional[pulumi.Input[_builtins.int]] = ...,
        provisioned_throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_iops.setter
    def provisioned_iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_throughput.setter
    def provisioned_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size_gb.setter
    def size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterNodeConfigConfidentialNodesArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    confidential_instance_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigConfidentialNodesArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        confidential_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceType")
    def confidential_instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @confidential_instance_type.setter
    def confidential_instance_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodeConfigContainerdConfigArgsDict(TypedDict):
    private_registry_access_config: NotRequired[
        pulumi.Input[
            ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigArgsDict
        ]
    ]
    registry_hosts: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClusterNodeConfigContainerdConfigRegistryHostArgsDict]
            ]
        ]
    ]
    writable_cgroups: NotRequired[
        pulumi.Input[ClusterNodeConfigContainerdConfigWritableCgroupsArgsDict]
    ]

@pulumi.input_type
class ClusterNodeConfigContainerdConfigArgs:
    def __init__(
        __self__,
        *,
        private_registry_access_config: Optional[
            pulumi.Input[
                ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigArgs
            ]
        ] = ...,
        registry_hosts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClusterNodeConfigContainerdConfigRegistryHostArgs]
                ]
            ]
        ] = ...,
        writable_cgroups: Optional[
            pulumi.Input[ClusterNodeConfigContainerdConfigWritableCgroupsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateRegistryAccessConfig")
    def private_registry_access_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigArgs]
    ]: ...
    @private_registry_access_config.setter
    def private_registry_access_config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="registryHosts")
    def registry_hosts(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterNodeConfigContainerdConfigRegistryHostArgs]]
        ]
    ]: ...
    @registry_hosts.setter
    def registry_hosts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClusterNodeConfigContainerdConfigRegistryHostArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="writableCgroups")
    def writable_cgroups(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodeConfigContainerdConfigWritableCgroupsArgs]
    ]: ...
    @writable_cgroups.setter
    def writable_cgroups(
        self,
        value: Optional[
            pulumi.Input[ClusterNodeConfigContainerdConfigWritableCgroupsArgs]
        ],
    ): ...

class ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    certificate_authority_domain_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        certificate_authority_domain_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityDomainConfigs")
    def certificate_authority_domain_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs
                ]
            ]
        ]
    ]: ...
    @certificate_authority_domain_configs.setter
    def certificate_authority_domain_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgsDict(
    TypedDict
):
    fqdns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    gcp_secret_manager_certificate_config: pulumi.Input[
        ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgsDict
    ]

@pulumi.input_type
class ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs:
    def __init__(
        __self__,
        *,
        fqdns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        gcp_secret_manager_certificate_config: pulumi.Input[
            ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @fqdns.setter
    def fqdns(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerCertificateConfig")
    def gcp_secret_manager_certificate_config(
        self,
    ) -> pulumi.Input[
        ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs
    ]: ...
    @gcp_secret_manager_certificate_config.setter
    def gcp_secret_manager_certificate_config(
        self,
        value: pulumi.Input[
            ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs
        ],
    ): ...

class ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgsDict(
    TypedDict
):
    secret_uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs:
    def __init__(__self__, *, secret_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretUri")
    def secret_uri(self) -> pulumi.Input[_builtins.str]: ...
    @secret_uri.setter
    def secret_uri(self, value: pulumi.Input[_builtins.str]): ...

class ClusterNodeConfigContainerdConfigRegistryHostArgsDict(TypedDict):
    server: pulumi.Input[_builtins.str]
    hosts: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClusterNodeConfigContainerdConfigRegistryHostHostArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class ClusterNodeConfigContainerdConfigRegistryHostArgs:
    def __init__(
        __self__,
        *,
        server: pulumi.Input[_builtins.str],
        hosts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClusterNodeConfigContainerdConfigRegistryHostHostArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> pulumi.Input[_builtins.str]: ...
    @server.setter
    def server(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def hosts(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClusterNodeConfigContainerdConfigRegistryHostHostArgs]
            ]
        ]
    ]: ...
    @hosts.setter
    def hosts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClusterNodeConfigContainerdConfigRegistryHostHostArgs]
                ]
            ]
        ],
    ): ...

class ClusterNodeConfigContainerdConfigRegistryHostHostArgsDict(TypedDict):
    host: pulumi.Input[_builtins.str]
    capabilities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    cas: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodeConfigContainerdConfigRegistryHostHostCaArgsDict
                ]
            ]
        ]
    ]
    clients: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodeConfigContainerdConfigRegistryHostHostClientArgsDict
                ]
            ]
        ]
    ]
    dial_timeout: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodeConfigContainerdConfigRegistryHostHostHeaderArgsDict
                ]
            ]
        ]
    ]
    override_path: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterNodeConfigContainerdConfigRegistryHostHostArgs:
    def __init__(
        __self__,
        *,
        host: pulumi.Input[_builtins.str],
        capabilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodeConfigContainerdConfigRegistryHostHostCaArgs
                    ]
                ]
            ]
        ] = ...,
        clients: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodeConfigContainerdConfigRegistryHostHostClientArgs
                    ]
                ]
            ]
        ] = ...,
        dial_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        headers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodeConfigContainerdConfigRegistryHostHostHeaderArgs
                    ]
                ]
            ]
        ] = ...,
        override_path: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def capabilities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @capabilities.setter
    def capabilities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def cas(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClusterNodeConfigContainerdConfigRegistryHostHostCaArgs]
            ]
        ]
    ]: ...
    @cas.setter
    def cas(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodeConfigContainerdConfigRegistryHostHostCaArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def clients(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodeConfigContainerdConfigRegistryHostHostClientArgs
                ]
            ]
        ]
    ]: ...
    @clients.setter
    def clients(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodeConfigContainerdConfigRegistryHostHostClientArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dialTimeout")
    def dial_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dial_timeout.setter
    def dial_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodeConfigContainerdConfigRegistryHostHostHeaderArgs
                ]
            ]
        ]
    ]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodeConfigContainerdConfigRegistryHostHostHeaderArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="overridePath")
    def override_path(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @override_path.setter
    def override_path(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClusterNodeConfigContainerdConfigRegistryHostHostCaArgsDict(TypedDict):
    gcp_secret_manager_secret_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigContainerdConfigRegistryHostHostCaArgs:
    def __init__(
        __self__,
        *,
        gcp_secret_manager_secret_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_secret_manager_secret_uri.setter
    def gcp_secret_manager_secret_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodeConfigContainerdConfigRegistryHostHostClientArgsDict(TypedDict):
    cert: pulumi.Input[
        ClusterNodeConfigContainerdConfigRegistryHostHostClientCertArgsDict
    ]
    key: NotRequired[
        pulumi.Input[ClusterNodeConfigContainerdConfigRegistryHostHostClientKeyArgsDict]
    ]

@pulumi.input_type
class ClusterNodeConfigContainerdConfigRegistryHostHostClientArgs:
    def __init__(
        __self__,
        *,
        cert: pulumi.Input[
            ClusterNodeConfigContainerdConfigRegistryHostHostClientCertArgs
        ],
        key: Optional[
            pulumi.Input[ClusterNodeConfigContainerdConfigRegistryHostHostClientKeyArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(
        self,
    ) -> pulumi.Input[
        ClusterNodeConfigContainerdConfigRegistryHostHostClientCertArgs
    ]: ...
    @cert.setter
    def cert(
        self,
        value: pulumi.Input[
            ClusterNodeConfigContainerdConfigRegistryHostHostClientCertArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodeConfigContainerdConfigRegistryHostHostClientKeyArgs]
    ]: ...
    @key.setter
    def key(
        self,
        value: Optional[
            pulumi.Input[ClusterNodeConfigContainerdConfigRegistryHostHostClientKeyArgs]
        ],
    ): ...

class ClusterNodeConfigContainerdConfigRegistryHostHostClientCertArgsDict(TypedDict):
    gcp_secret_manager_secret_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigContainerdConfigRegistryHostHostClientCertArgs:
    def __init__(
        __self__,
        *,
        gcp_secret_manager_secret_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_secret_manager_secret_uri.setter
    def gcp_secret_manager_secret_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodeConfigContainerdConfigRegistryHostHostClientKeyArgsDict(TypedDict):
    gcp_secret_manager_secret_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigContainerdConfigRegistryHostHostClientKeyArgs:
    def __init__(
        __self__,
        *,
        gcp_secret_manager_secret_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_secret_manager_secret_uri.setter
    def gcp_secret_manager_secret_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodeConfigContainerdConfigRegistryHostHostHeaderArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ClusterNodeConfigContainerdConfigRegistryHostHostHeaderArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ClusterNodeConfigContainerdConfigWritableCgroupsArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterNodeConfigContainerdConfigWritableCgroupsArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterNodeConfigEffectiveTaintArgsDict(TypedDict):
    effect: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigEffectiveTaintArgs:
    def __init__(
        __self__,
        *,
        effect: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effect.setter
    def effect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodeConfigEphemeralStorageConfigArgsDict(TypedDict):
    local_ssd_count: pulumi.Input[_builtins.int]

@pulumi.input_type
class ClusterNodeConfigEphemeralStorageConfigArgs:
    def __init__(__self__, *, local_ssd_count: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> pulumi.Input[_builtins.int]: ...
    @local_ssd_count.setter
    def local_ssd_count(self, value: pulumi.Input[_builtins.int]): ...

class ClusterNodeConfigEphemeralStorageLocalSsdConfigArgsDict(TypedDict):
    local_ssd_count: pulumi.Input[_builtins.int]
    data_cache_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterNodeConfigEphemeralStorageLocalSsdConfigArgs:
    def __init__(
        __self__,
        *,
        local_ssd_count: pulumi.Input[_builtins.int],
        data_cache_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> pulumi.Input[_builtins.int]: ...
    @local_ssd_count.setter
    def local_ssd_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="dataCacheCount")
    def data_cache_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_cache_count.setter
    def data_cache_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterNodeConfigFastSocketArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterNodeConfigFastSocketArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterNodeConfigGcfsConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterNodeConfigGcfsConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterNodeConfigGuestAcceleratorArgsDict(TypedDict):
    count: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]
    gpu_driver_installation_config: NotRequired[
        pulumi.Input[
            ClusterNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgsDict
        ]
    ]
    gpu_partition_size: NotRequired[pulumi.Input[_builtins.str]]
    gpu_sharing_config: NotRequired[
        pulumi.Input[ClusterNodeConfigGuestAcceleratorGpuSharingConfigArgsDict]
    ]

@pulumi.input_type
class ClusterNodeConfigGuestAcceleratorArgs:
    def __init__(
        __self__,
        *,
        count: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.str],
        gpu_driver_installation_config: Optional[
            pulumi.Input[
                ClusterNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgs
            ]
        ] = ...,
        gpu_partition_size: Optional[pulumi.Input[_builtins.str]] = ...,
        gpu_sharing_config: Optional[
            pulumi.Input[ClusterNodeConfigGuestAcceleratorGpuSharingConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> pulumi.Input[_builtins.int]: ...
    @count.setter
    def count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverInstallationConfig")
    def gpu_driver_installation_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgs]
    ]: ...
    @gpu_driver_installation_config.setter
    def gpu_driver_installation_config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gpuPartitionSize")
    def gpu_partition_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gpu_partition_size.setter
    def gpu_partition_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingConfig")
    def gpu_sharing_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodeConfigGuestAcceleratorGpuSharingConfigArgs]
    ]: ...
    @gpu_sharing_config.setter
    def gpu_sharing_config(
        self,
        value: Optional[
            pulumi.Input[ClusterNodeConfigGuestAcceleratorGpuSharingConfigArgs]
        ],
    ): ...

class ClusterNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgsDict(TypedDict):
    gpu_driver_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgs:
    def __init__(
        __self__, *, gpu_driver_version: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverVersion")
    def gpu_driver_version(self) -> pulumi.Input[_builtins.str]: ...
    @gpu_driver_version.setter
    def gpu_driver_version(self, value: pulumi.Input[_builtins.str]): ...

class ClusterNodeConfigGuestAcceleratorGpuSharingConfigArgsDict(TypedDict):
    gpu_sharing_strategy: pulumi.Input[_builtins.str]
    max_shared_clients_per_gpu: pulumi.Input[_builtins.int]

@pulumi.input_type
class ClusterNodeConfigGuestAcceleratorGpuSharingConfigArgs:
    def __init__(
        __self__,
        *,
        gpu_sharing_strategy: pulumi.Input[_builtins.str],
        max_shared_clients_per_gpu: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingStrategy")
    def gpu_sharing_strategy(self) -> pulumi.Input[_builtins.str]: ...
    @gpu_sharing_strategy.setter
    def gpu_sharing_strategy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maxSharedClientsPerGpu")
    def max_shared_clients_per_gpu(self) -> pulumi.Input[_builtins.int]: ...
    @max_shared_clients_per_gpu.setter
    def max_shared_clients_per_gpu(self, value: pulumi.Input[_builtins.int]): ...

class ClusterNodeConfigGvnicArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterNodeConfigGvnicArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterNodeConfigHostMaintenancePolicyArgsDict(TypedDict):
    maintenance_interval: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterNodeConfigHostMaintenancePolicyArgs:
    def __init__(
        __self__, *, maintenance_interval: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceInterval")
    def maintenance_interval(self) -> pulumi.Input[_builtins.str]: ...
    @maintenance_interval.setter
    def maintenance_interval(self, value: pulumi.Input[_builtins.str]): ...

class ClusterNodeConfigKubeletConfigArgsDict(TypedDict):
    allowed_unsafe_sysctls: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    container_log_max_files: NotRequired[pulumi.Input[_builtins.int]]
    container_log_max_size: NotRequired[pulumi.Input[_builtins.str]]
    cpu_cfs_quota: NotRequired[pulumi.Input[_builtins.bool]]
    cpu_cfs_quota_period: NotRequired[pulumi.Input[_builtins.str]]
    cpu_manager_policy: NotRequired[pulumi.Input[_builtins.str]]
    eviction_max_pod_grace_period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    eviction_minimum_reclaim: NotRequired[
        pulumi.Input[ClusterNodeConfigKubeletConfigEvictionMinimumReclaimArgsDict]
    ]
    eviction_soft: NotRequired[
        pulumi.Input[ClusterNodeConfigKubeletConfigEvictionSoftArgsDict]
    ]
    eviction_soft_grace_period: NotRequired[
        pulumi.Input[ClusterNodeConfigKubeletConfigEvictionSoftGracePeriodArgsDict]
    ]
    image_gc_high_threshold_percent: NotRequired[pulumi.Input[_builtins.int]]
    image_gc_low_threshold_percent: NotRequired[pulumi.Input[_builtins.int]]
    image_maximum_gc_age: NotRequired[pulumi.Input[_builtins.str]]
    image_minimum_gc_age: NotRequired[pulumi.Input[_builtins.str]]
    insecure_kubelet_readonly_port_enabled: NotRequired[pulumi.Input[_builtins.str]]
    max_parallel_image_pulls: NotRequired[pulumi.Input[_builtins.int]]
    memory_manager: NotRequired[
        pulumi.Input[ClusterNodeConfigKubeletConfigMemoryManagerArgsDict]
    ]
    pod_pids_limit: NotRequired[pulumi.Input[_builtins.int]]
    single_process_oom_kill: NotRequired[pulumi.Input[_builtins.bool]]
    topology_manager: NotRequired[
        pulumi.Input[ClusterNodeConfigKubeletConfigTopologyManagerArgsDict]
    ]

@pulumi.input_type
class ClusterNodeConfigKubeletConfigArgs:
    def __init__(
        __self__,
        *,
        allowed_unsafe_sysctls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        container_log_max_files: Optional[pulumi.Input[_builtins.int]] = ...,
        container_log_max_size: Optional[pulumi.Input[_builtins.str]] = ...,
        cpu_cfs_quota: Optional[pulumi.Input[_builtins.bool]] = ...,
        cpu_cfs_quota_period: Optional[pulumi.Input[_builtins.str]] = ...,
        cpu_manager_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        eviction_max_pod_grace_period_seconds: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        eviction_minimum_reclaim: Optional[
            pulumi.Input[ClusterNodeConfigKubeletConfigEvictionMinimumReclaimArgs]
        ] = ...,
        eviction_soft: Optional[
            pulumi.Input[ClusterNodeConfigKubeletConfigEvictionSoftArgs]
        ] = ...,
        eviction_soft_grace_period: Optional[
            pulumi.Input[ClusterNodeConfigKubeletConfigEvictionSoftGracePeriodArgs]
        ] = ...,
        image_gc_high_threshold_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        image_gc_low_threshold_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        image_maximum_gc_age: Optional[pulumi.Input[_builtins.str]] = ...,
        image_minimum_gc_age: Optional[pulumi.Input[_builtins.str]] = ...,
        insecure_kubelet_readonly_port_enabled: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        max_parallel_image_pulls: Optional[pulumi.Input[_builtins.int]] = ...,
        memory_manager: Optional[
            pulumi.Input[ClusterNodeConfigKubeletConfigMemoryManagerArgs]
        ] = ...,
        pod_pids_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        single_process_oom_kill: Optional[pulumi.Input[_builtins.bool]] = ...,
        topology_manager: Optional[
            pulumi.Input[ClusterNodeConfigKubeletConfigTopologyManagerArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedUnsafeSysctls")
    def allowed_unsafe_sysctls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_unsafe_sysctls.setter
    def allowed_unsafe_sysctls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxFiles")
    def container_log_max_files(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @container_log_max_files.setter
    def container_log_max_files(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxSize")
    def container_log_max_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_log_max_size.setter
    def container_log_max_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuota")
    def cpu_cfs_quota(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cpu_cfs_quota.setter
    def cpu_cfs_quota(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuotaPeriod")
    def cpu_cfs_quota_period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu_cfs_quota_period.setter
    def cpu_cfs_quota_period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuManagerPolicy")
    def cpu_manager_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu_manager_policy.setter
    def cpu_manager_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="evictionMaxPodGracePeriodSeconds")
    def eviction_max_pod_grace_period_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @eviction_max_pod_grace_period_seconds.setter
    def eviction_max_pod_grace_period_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="evictionMinimumReclaim")
    def eviction_minimum_reclaim(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodeConfigKubeletConfigEvictionMinimumReclaimArgs]
    ]: ...
    @eviction_minimum_reclaim.setter
    def eviction_minimum_reclaim(
        self,
        value: Optional[
            pulumi.Input[ClusterNodeConfigKubeletConfigEvictionMinimumReclaimArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="evictionSoft")
    def eviction_soft(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigKubeletConfigEvictionSoftArgs]]: ...
    @eviction_soft.setter
    def eviction_soft(
        self,
        value: Optional[pulumi.Input[ClusterNodeConfigKubeletConfigEvictionSoftArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="evictionSoftGracePeriod")
    def eviction_soft_grace_period(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodeConfigKubeletConfigEvictionSoftGracePeriodArgs]
    ]: ...
    @eviction_soft_grace_period.setter
    def eviction_soft_grace_period(
        self,
        value: Optional[
            pulumi.Input[ClusterNodeConfigKubeletConfigEvictionSoftGracePeriodArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageGcHighThresholdPercent")
    def image_gc_high_threshold_percent(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @image_gc_high_threshold_percent.setter
    def image_gc_high_threshold_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageGcLowThresholdPercent")
    def image_gc_low_threshold_percent(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @image_gc_low_threshold_percent.setter
    def image_gc_low_threshold_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageMaximumGcAge")
    def image_maximum_gc_age(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_maximum_gc_age.setter
    def image_maximum_gc_age(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageMinimumGcAge")
    def image_minimum_gc_age(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_minimum_gc_age.setter
    def image_minimum_gc_age(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="insecureKubeletReadonlyPortEnabled")
    def insecure_kubelet_readonly_port_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @insecure_kubelet_readonly_port_enabled.setter
    def insecure_kubelet_readonly_port_enabled(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxParallelImagePulls")
    def max_parallel_image_pulls(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_parallel_image_pulls.setter
    def max_parallel_image_pulls(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="memoryManager")
    def memory_manager(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigKubeletConfigMemoryManagerArgs]]: ...
    @memory_manager.setter
    def memory_manager(
        self,
        value: Optional[pulumi.Input[ClusterNodeConfigKubeletConfigMemoryManagerArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="podPidsLimit")
    def pod_pids_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pod_pids_limit.setter
    def pod_pids_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="singleProcessOomKill")
    def single_process_oom_kill(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @single_process_oom_kill.setter
    def single_process_oom_kill(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="topologyManager")
    def topology_manager(
        self,
    ) -> Optional[pulumi.Input[ClusterNodeConfigKubeletConfigTopologyManagerArgs]]: ...
    @topology_manager.setter
    def topology_manager(
        self,
        value: Optional[
            pulumi.Input[ClusterNodeConfigKubeletConfigTopologyManagerArgs]
        ],
    ): ...

class ClusterNodeConfigKubeletConfigEvictionMinimumReclaimArgsDict(TypedDict):
    imagefs_available: NotRequired[pulumi.Input[_builtins.str]]
    imagefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    memory_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    pid_available: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigKubeletConfigEvictionMinimumReclaimArgs:
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        imagefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        pid_available: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_available.setter
    def imagefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_inodes_free.setter
    def imagefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory_available.setter
    def memory_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_available.setter
    def nodefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_inodes_free.setter
    def nodefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pid_available.setter
    def pid_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodeConfigKubeletConfigEvictionSoftArgsDict(TypedDict):
    imagefs_available: NotRequired[pulumi.Input[_builtins.str]]
    imagefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    memory_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    pid_available: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigKubeletConfigEvictionSoftArgs:
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        imagefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        pid_available: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_available.setter
    def imagefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_inodes_free.setter
    def imagefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory_available.setter
    def memory_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_available.setter
    def nodefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_inodes_free.setter
    def nodefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pid_available.setter
    def pid_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodeConfigKubeletConfigEvictionSoftGracePeriodArgsDict(TypedDict):
    imagefs_available: NotRequired[pulumi.Input[_builtins.str]]
    imagefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    memory_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    pid_available: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigKubeletConfigEvictionSoftGracePeriodArgs:
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        imagefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        pid_available: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_available.setter
    def imagefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_inodes_free.setter
    def imagefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory_available.setter
    def memory_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_available.setter
    def nodefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_inodes_free.setter
    def nodefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pid_available.setter
    def pid_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodeConfigKubeletConfigMemoryManagerArgsDict(TypedDict):
    policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigKubeletConfigMemoryManagerArgs:
    def __init__(
        __self__, *, policy: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodeConfigKubeletConfigTopologyManagerArgsDict(TypedDict):
    policy: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigKubeletConfigTopologyManagerArgs:
    def __init__(
        __self__,
        *,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodeConfigLinuxNodeConfigArgsDict(TypedDict):
    cgroup_mode: NotRequired[pulumi.Input[_builtins.str]]
    hugepages_config: NotRequired[
        pulumi.Input[ClusterNodeConfigLinuxNodeConfigHugepagesConfigArgsDict]
    ]
    node_kernel_module_loading: NotRequired[
        pulumi.Input[ClusterNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgsDict]
    ]
    sysctls: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    transparent_hugepage_defrag: NotRequired[pulumi.Input[_builtins.str]]
    transparent_hugepage_enabled: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigLinuxNodeConfigArgs:
    def __init__(
        __self__,
        *,
        cgroup_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        hugepages_config: Optional[
            pulumi.Input[ClusterNodeConfigLinuxNodeConfigHugepagesConfigArgs]
        ] = ...,
        node_kernel_module_loading: Optional[
            pulumi.Input[ClusterNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgs]
        ] = ...,
        sysctls: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transparent_hugepage_defrag: Optional[pulumi.Input[_builtins.str]] = ...,
        transparent_hugepage_enabled: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cgroupMode")
    def cgroup_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cgroup_mode.setter
    def cgroup_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hugepagesConfig")
    def hugepages_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodeConfigLinuxNodeConfigHugepagesConfigArgs]
    ]: ...
    @hugepages_config.setter
    def hugepages_config(
        self,
        value: Optional[
            pulumi.Input[ClusterNodeConfigLinuxNodeConfigHugepagesConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeKernelModuleLoading")
    def node_kernel_module_loading(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgs]
    ]: ...
    @node_kernel_module_loading.setter
    def node_kernel_module_loading(
        self,
        value: Optional[
            pulumi.Input[ClusterNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sysctls(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @sysctls.setter
    def sysctls(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageDefrag")
    def transparent_hugepage_defrag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transparent_hugepage_defrag.setter
    def transparent_hugepage_defrag(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageEnabled")
    def transparent_hugepage_enabled(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transparent_hugepage_enabled.setter
    def transparent_hugepage_enabled(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodeConfigLinuxNodeConfigHugepagesConfigArgsDict(TypedDict):
    hugepage_size1g: NotRequired[pulumi.Input[_builtins.int]]
    hugepage_size2m: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterNodeConfigLinuxNodeConfigHugepagesConfigArgs:
    def __init__(
        __self__,
        *,
        hugepage_size1g: Optional[pulumi.Input[_builtins.int]] = ...,
        hugepage_size2m: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize1g")
    def hugepage_size1g(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hugepage_size1g.setter
    def hugepage_size1g(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize2m")
    def hugepage_size2m(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hugepage_size2m.setter
    def hugepage_size2m(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgsDict(TypedDict):
    policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgs:
    def __init__(
        __self__, *, policy: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodeConfigLocalNvmeSsdBlockConfigArgsDict(TypedDict):
    local_ssd_count: pulumi.Input[_builtins.int]

@pulumi.input_type
class ClusterNodeConfigLocalNvmeSsdBlockConfigArgs:
    def __init__(__self__, *, local_ssd_count: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> pulumi.Input[_builtins.int]: ...
    @local_ssd_count.setter
    def local_ssd_count(self, value: pulumi.Input[_builtins.int]): ...

class ClusterNodeConfigReservationAffinityArgsDict(TypedDict):
    consume_reservation_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ClusterNodeConfigReservationAffinityArgs:
    def __init__(
        __self__,
        *,
        consume_reservation_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> pulumi.Input[_builtins.str]: ...
    @consume_reservation_type.setter
    def consume_reservation_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterNodeConfigSandboxConfigArgsDict(TypedDict):
    sandbox_type: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigSandboxConfigArgs:
    def __init__(
        __self__,
        *,
        sandbox_type: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sandboxType")
    @_utilities.deprecated(...)
    def sandbox_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sandbox_type.setter
    def sandbox_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodeConfigSecondaryBootDiskArgsDict(TypedDict):
    disk_image: pulumi.Input[_builtins.str]
    mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigSecondaryBootDiskArgs:
    def __init__(
        __self__,
        *,
        disk_image: pulumi.Input[_builtins.str],
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskImage")
    def disk_image(self) -> pulumi.Input[_builtins.str]: ...
    @disk_image.setter
    def disk_image(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodeConfigShieldedInstanceConfigArgsDict(TypedDict):
    enable_integrity_monitoring: NotRequired[pulumi.Input[_builtins.bool]]
    enable_secure_boot: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterNodeConfigShieldedInstanceConfigArgs:
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_secure_boot: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_integrity_monitoring.setter
    def enable_integrity_monitoring(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_secure_boot.setter
    def enable_secure_boot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClusterNodeConfigSoleTenantConfigArgsDict(TypedDict):
    node_affinities: pulumi.Input[
        Sequence[pulumi.Input[ClusterNodeConfigSoleTenantConfigNodeAffinityArgsDict]]
    ]
    min_node_cpus: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterNodeConfigSoleTenantConfigArgs:
    def __init__(
        __self__,
        *,
        node_affinities: pulumi.Input[
            Sequence[pulumi.Input[ClusterNodeConfigSoleTenantConfigNodeAffinityArgs]]
        ],
        min_node_cpus: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeAffinities")
    def node_affinities(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ClusterNodeConfigSoleTenantConfigNodeAffinityArgs]]
    ]: ...
    @node_affinities.setter
    def node_affinities(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ClusterNodeConfigSoleTenantConfigNodeAffinityArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minNodeCpus")
    def min_node_cpus(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_node_cpus.setter
    def min_node_cpus(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterNodeConfigSoleTenantConfigNodeAffinityArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    operator: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ClusterNodeConfigSoleTenantConfigNodeAffinityArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        operator: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[_builtins.str]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ClusterNodeConfigTaintArgsDict(TypedDict):
    effect: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterNodeConfigTaintArgs:
    def __init__(
        __self__,
        *,
        effect: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> pulumi.Input[_builtins.str]: ...
    @effect.setter
    def effect(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ClusterNodeConfigWindowsNodeConfigArgsDict(TypedDict):
    osversion: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodeConfigWindowsNodeConfigArgs:
    def __init__(
        __self__, *, osversion: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def osversion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @osversion.setter
    def osversion(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodeConfigWorkloadMetadataConfigArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterNodeConfigWorkloadMetadataConfigArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...

class ClusterNodePoolArgsDict(TypedDict):
    autoscaling: NotRequired[pulumi.Input[ClusterNodePoolAutoscalingArgsDict]]
    initial_node_count: NotRequired[pulumi.Input[_builtins.int]]
    instance_group_urls: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    managed_instance_group_urls: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    management: NotRequired[pulumi.Input[ClusterNodePoolManagementArgsDict]]
    max_pods_per_node: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    name_prefix: NotRequired[pulumi.Input[_builtins.str]]
    network_config: NotRequired[pulumi.Input[ClusterNodePoolNetworkConfigArgsDict]]
    node_config: NotRequired[pulumi.Input[ClusterNodePoolNodeConfigArgsDict]]
    node_count: NotRequired[pulumi.Input[_builtins.int]]
    node_drain_configs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ClusterNodePoolNodeDrainConfigArgsDict]]]
    ]
    node_locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    placement_policy: NotRequired[pulumi.Input[ClusterNodePoolPlacementPolicyArgsDict]]
    queued_provisioning: NotRequired[
        pulumi.Input[ClusterNodePoolQueuedProvisioningArgsDict]
    ]
    upgrade_settings: NotRequired[pulumi.Input[ClusterNodePoolUpgradeSettingsArgsDict]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolArgs:
    def __init__(
        __self__,
        *,
        autoscaling: Optional[pulumi.Input[ClusterNodePoolAutoscalingArgs]] = ...,
        initial_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        instance_group_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        managed_instance_group_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        management: Optional[pulumi.Input[ClusterNodePoolManagementArgs]] = ...,
        max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[pulumi.Input[ClusterNodePoolNetworkConfigArgs]] = ...,
        node_config: Optional[pulumi.Input[ClusterNodePoolNodeConfigArgs]] = ...,
        node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        node_drain_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterNodePoolNodeDrainConfigArgs]]]
        ] = ...,
        node_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        placement_policy: Optional[
            pulumi.Input[ClusterNodePoolPlacementPolicyArgs]
        ] = ...,
        queued_provisioning: Optional[
            pulumi.Input[ClusterNodePoolQueuedProvisioningArgs]
        ] = ...,
        upgrade_settings: Optional[
            pulumi.Input[ClusterNodePoolUpgradeSettingsArgs]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def autoscaling(self) -> Optional[pulumi.Input[ClusterNodePoolAutoscalingArgs]]: ...
    @autoscaling.setter
    def autoscaling(
        self, value: Optional[pulumi.Input[ClusterNodePoolAutoscalingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialNodeCount")
    def initial_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_node_count.setter
    def initial_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceGroupUrls")
    def instance_group_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_group_urls.setter
    def instance_group_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedInstanceGroupUrls")
    def managed_instance_group_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @managed_instance_group_urls.setter
    def managed_instance_group_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def management(self) -> Optional[pulumi.Input[ClusterNodePoolManagementArgs]]: ...
    @management.setter
    def management(
        self, value: Optional[pulumi.Input[ClusterNodePoolManagementArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_pods_per_node.setter
    def max_pods_per_node(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolNetworkConfigArgs]]: ...
    @network_config.setter
    def network_config(
        self, value: Optional[pulumi.Input[ClusterNodePoolNetworkConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[ClusterNodePoolNodeConfigArgs]]: ...
    @node_config.setter
    def node_config(
        self, value: Optional[pulumi.Input[ClusterNodePoolNodeConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeDrainConfigs")
    def node_drain_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterNodePoolNodeDrainConfigArgs]]]
    ]: ...
    @node_drain_configs.setter
    def node_drain_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterNodePoolNodeDrainConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeLocations")
    def node_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @node_locations.setter
    def node_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="placementPolicy")
    def placement_policy(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolPlacementPolicyArgs]]: ...
    @placement_policy.setter
    def placement_policy(
        self, value: Optional[pulumi.Input[ClusterNodePoolPlacementPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queuedProvisioning")
    def queued_provisioning(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolQueuedProvisioningArgs]]: ...
    @queued_provisioning.setter
    def queued_provisioning(
        self, value: Optional[pulumi.Input[ClusterNodePoolQueuedProvisioningArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolUpgradeSettingsArgs]]: ...
    @upgrade_settings.setter
    def upgrade_settings(
        self, value: Optional[pulumi.Input[ClusterNodePoolUpgradeSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolAutoConfigArgsDict(TypedDict):
    linux_node_config: NotRequired[
        pulumi.Input[ClusterNodePoolAutoConfigLinuxNodeConfigArgsDict]
    ]
    network_tags: NotRequired[
        pulumi.Input[ClusterNodePoolAutoConfigNetworkTagsArgsDict]
    ]
    node_kubelet_config: NotRequired[
        pulumi.Input[ClusterNodePoolAutoConfigNodeKubeletConfigArgsDict]
    ]
    resource_manager_tags: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ClusterNodePoolAutoConfigArgs:
    def __init__(
        __self__,
        *,
        linux_node_config: Optional[
            pulumi.Input[ClusterNodePoolAutoConfigLinuxNodeConfigArgs]
        ] = ...,
        network_tags: Optional[
            pulumi.Input[ClusterNodePoolAutoConfigNetworkTagsArgs]
        ] = ...,
        node_kubelet_config: Optional[
            pulumi.Input[ClusterNodePoolAutoConfigNodeKubeletConfigArgs]
        ] = ...,
        resource_manager_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linuxNodeConfig")
    def linux_node_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolAutoConfigLinuxNodeConfigArgs]]: ...
    @linux_node_config.setter
    def linux_node_config(
        self,
        value: Optional[pulumi.Input[ClusterNodePoolAutoConfigLinuxNodeConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolAutoConfigNetworkTagsArgs]]: ...
    @network_tags.setter
    def network_tags(
        self, value: Optional[pulumi.Input[ClusterNodePoolAutoConfigNetworkTagsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeKubeletConfig")
    def node_kubelet_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolAutoConfigNodeKubeletConfigArgs]]: ...
    @node_kubelet_config.setter
    def node_kubelet_config(
        self,
        value: Optional[pulumi.Input[ClusterNodePoolAutoConfigNodeKubeletConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @resource_manager_tags.setter
    def resource_manager_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterNodePoolAutoConfigLinuxNodeConfigArgsDict(TypedDict):
    cgroup_mode: NotRequired[pulumi.Input[_builtins.str]]
    node_kernel_module_loading: NotRequired[
        pulumi.Input[
            ClusterNodePoolAutoConfigLinuxNodeConfigNodeKernelModuleLoadingArgsDict
        ]
    ]

@pulumi.input_type
class ClusterNodePoolAutoConfigLinuxNodeConfigArgs:
    def __init__(
        __self__,
        *,
        cgroup_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        node_kernel_module_loading: Optional[
            pulumi.Input[
                ClusterNodePoolAutoConfigLinuxNodeConfigNodeKernelModuleLoadingArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cgroupMode")
    def cgroup_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cgroup_mode.setter
    def cgroup_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeKernelModuleLoading")
    def node_kernel_module_loading(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterNodePoolAutoConfigLinuxNodeConfigNodeKernelModuleLoadingArgs
        ]
    ]: ...
    @node_kernel_module_loading.setter
    def node_kernel_module_loading(
        self,
        value: Optional[
            pulumi.Input[
                ClusterNodePoolAutoConfigLinuxNodeConfigNodeKernelModuleLoadingArgs
            ]
        ],
    ): ...

class ClusterNodePoolAutoConfigLinuxNodeConfigNodeKernelModuleLoadingArgsDict(
    TypedDict
):
    policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolAutoConfigLinuxNodeConfigNodeKernelModuleLoadingArgs:
    def __init__(
        __self__, *, policy: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolAutoConfigNetworkTagsArgsDict(TypedDict):
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ClusterNodePoolAutoConfigNetworkTagsArgs:
    def __init__(
        __self__,
        *,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterNodePoolAutoConfigNodeKubeletConfigArgsDict(TypedDict):
    insecure_kubelet_readonly_port_enabled: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolAutoConfigNodeKubeletConfigArgs:
    def __init__(
        __self__,
        *,
        insecure_kubelet_readonly_port_enabled: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="insecureKubeletReadonlyPortEnabled")
    def insecure_kubelet_readonly_port_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @insecure_kubelet_readonly_port_enabled.setter
    def insecure_kubelet_readonly_port_enabled(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodePoolAutoscalingArgsDict(TypedDict):
    location_policy: NotRequired[pulumi.Input[_builtins.str]]
    max_node_count: NotRequired[pulumi.Input[_builtins.int]]
    min_node_count: NotRequired[pulumi.Input[_builtins.int]]
    total_max_node_count: NotRequired[pulumi.Input[_builtins.int]]
    total_min_node_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterNodePoolAutoscalingArgs:
    def __init__(
        __self__,
        *,
        location_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        max_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        total_max_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        total_min_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationPolicy")
    def location_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location_policy.setter
    def location_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @_builtins.property
    @pulumi.getter(name="totalMaxNodeCount")
    def total_max_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @total_max_node_count.setter
    def total_max_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="totalMinNodeCount")
    def total_min_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @total_min_node_count.setter
    def total_min_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterNodePoolDefaultsArgsDict(TypedDict):
    node_config_defaults: NotRequired[
        pulumi.Input[ClusterNodePoolDefaultsNodeConfigDefaultsArgsDict]
    ]

@pulumi.input_type
class ClusterNodePoolDefaultsArgs:
    def __init__(
        __self__,
        *,
        node_config_defaults: Optional[
            pulumi.Input[ClusterNodePoolDefaultsNodeConfigDefaultsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeConfigDefaults")
    def node_config_defaults(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolDefaultsNodeConfigDefaultsArgs]]: ...
    @node_config_defaults.setter
    def node_config_defaults(
        self,
        value: Optional[pulumi.Input[ClusterNodePoolDefaultsNodeConfigDefaultsArgs]],
    ): ...

class ClusterNodePoolDefaultsNodeConfigDefaultsArgsDict(TypedDict):
    containerd_config: NotRequired[
        pulumi.Input[ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigArgsDict]
    ]
    gcfs_config: NotRequired[
        pulumi.Input[ClusterNodePoolDefaultsNodeConfigDefaultsGcfsConfigArgsDict]
    ]
    insecure_kubelet_readonly_port_enabled: NotRequired[pulumi.Input[_builtins.str]]
    logging_variant: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolDefaultsNodeConfigDefaultsArgs:
    def __init__(
        __self__,
        *,
        containerd_config: Optional[
            pulumi.Input[ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigArgs]
        ] = ...,
        gcfs_config: Optional[
            pulumi.Input[ClusterNodePoolDefaultsNodeConfigDefaultsGcfsConfigArgs]
        ] = ...,
        insecure_kubelet_readonly_port_enabled: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        logging_variant: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerdConfig")
    def containerd_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigArgs]
    ]: ...
    @containerd_config.setter
    def containerd_config(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gcfsConfig")
    def gcfs_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolDefaultsNodeConfigDefaultsGcfsConfigArgs]
    ]: ...
    @gcfs_config.setter
    def gcfs_config(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolDefaultsNodeConfigDefaultsGcfsConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="insecureKubeletReadonlyPortEnabled")
    def insecure_kubelet_readonly_port_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @insecure_kubelet_readonly_port_enabled.setter
    def insecure_kubelet_readonly_port_enabled(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingVariant")
    def logging_variant(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logging_variant.setter
    def logging_variant(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigArgsDict(TypedDict):
    private_registry_access_config: NotRequired[
        pulumi.Input[
            ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigArgsDict
        ]
    ]
    registry_hosts: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostArgsDict
                ]
            ]
        ]
    ]
    writable_cgroups: NotRequired[
        pulumi.Input[
            ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigWritableCgroupsArgsDict
        ]
    ]

@pulumi.input_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigArgs:
    def __init__(
        __self__,
        *,
        private_registry_access_config: Optional[
            pulumi.Input[
                ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigArgs
            ]
        ] = ...,
        registry_hosts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostArgs
                    ]
                ]
            ]
        ] = ...,
        writable_cgroups: Optional[
            pulumi.Input[
                ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigWritableCgroupsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateRegistryAccessConfig")
    def private_registry_access_config(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigArgs
        ]
    ]: ...
    @private_registry_access_config.setter
    def private_registry_access_config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="registryHosts")
    def registry_hosts(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostArgs
                ]
            ]
        ]
    ]: ...
    @registry_hosts.setter
    def registry_hosts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="writableCgroups")
    def writable_cgroups(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigWritableCgroupsArgs
        ]
    ]: ...
    @writable_cgroups.setter
    def writable_cgroups(
        self,
        value: Optional[
            pulumi.Input[
                ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigWritableCgroupsArgs
            ]
        ],
    ): ...

class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigArgsDict(
    TypedDict
):
    enabled: pulumi.Input[_builtins.bool]
    certificate_authority_domain_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        certificate_authority_domain_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityDomainConfigs")
    def certificate_authority_domain_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs
                ]
            ]
        ]
    ]: ...
    @certificate_authority_domain_configs.setter
    def certificate_authority_domain_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgsDict(
    TypedDict
):
    fqdns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    gcp_secret_manager_certificate_config: pulumi.Input[
        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgsDict
    ]

@pulumi.input_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs:
    def __init__(
        __self__,
        *,
        fqdns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        gcp_secret_manager_certificate_config: pulumi.Input[
            ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @fqdns.setter
    def fqdns(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerCertificateConfig")
    def gcp_secret_manager_certificate_config(
        self,
    ) -> pulumi.Input[
        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs
    ]: ...
    @gcp_secret_manager_certificate_config.setter
    def gcp_secret_manager_certificate_config(
        self,
        value: pulumi.Input[
            ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs
        ],
    ): ...

class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgsDict(
    TypedDict
):
    secret_uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs:
    def __init__(__self__, *, secret_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretUri")
    def secret_uri(self) -> pulumi.Input[_builtins.str]: ...
    @secret_uri.setter
    def secret_uri(self, value: pulumi.Input[_builtins.str]): ...

class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostArgsDict(
    TypedDict
):
    server: pulumi.Input[_builtins.str]
    hosts: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostArgs:
    def __init__(
        __self__,
        *,
        server: pulumi.Input[_builtins.str],
        hosts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> pulumi.Input[_builtins.str]: ...
    @server.setter
    def server(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def hosts(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostArgs
                ]
            ]
        ]
    ]: ...
    @hosts.setter
    def hosts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostArgs
                    ]
                ]
            ]
        ],
    ): ...

class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostArgsDict(
    TypedDict
):
    host: pulumi.Input[_builtins.str]
    capabilities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    cas: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostCaArgsDict
                ]
            ]
        ]
    ]
    clients: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientArgsDict
                ]
            ]
        ]
    ]
    dial_timeout: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostHeaderArgsDict
                ]
            ]
        ]
    ]
    override_path: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostArgs:
    def __init__(
        __self__,
        *,
        host: pulumi.Input[_builtins.str],
        capabilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostCaArgs
                    ]
                ]
            ]
        ] = ...,
        clients: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientArgs
                    ]
                ]
            ]
        ] = ...,
        dial_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        headers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostHeaderArgs
                    ]
                ]
            ]
        ] = ...,
        override_path: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def capabilities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @capabilities.setter
    def capabilities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def cas(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostCaArgs
                ]
            ]
        ]
    ]: ...
    @cas.setter
    def cas(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostCaArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def clients(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientArgs
                ]
            ]
        ]
    ]: ...
    @clients.setter
    def clients(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dialTimeout")
    def dial_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dial_timeout.setter
    def dial_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostHeaderArgs
                ]
            ]
        ]
    ]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostHeaderArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="overridePath")
    def override_path(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @override_path.setter
    def override_path(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostCaArgsDict(
    TypedDict
):
    gcp_secret_manager_secret_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostCaArgs:
    def __init__(
        __self__,
        *,
        gcp_secret_manager_secret_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_secret_manager_secret_uri.setter
    def gcp_secret_manager_secret_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientArgsDict(
    TypedDict
):
    cert: pulumi.Input[
        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientCertArgsDict
    ]
    key: NotRequired[
        pulumi.Input[
            ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientKeyArgsDict
        ]
    ]

@pulumi.input_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientArgs:
    def __init__(
        __self__,
        *,
        cert: pulumi.Input[
            ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientCertArgs
        ],
        key: Optional[
            pulumi.Input[
                ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientKeyArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(
        self,
    ) -> pulumi.Input[
        ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientCertArgs
    ]: ...
    @cert.setter
    def cert(
        self,
        value: pulumi.Input[
            ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientCertArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientKeyArgs
        ]
    ]: ...
    @key.setter
    def key(
        self,
        value: Optional[
            pulumi.Input[
                ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientKeyArgs
            ]
        ],
    ): ...

class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientCertArgsDict(
    TypedDict
):
    gcp_secret_manager_secret_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientCertArgs:
    def __init__(
        __self__,
        *,
        gcp_secret_manager_secret_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_secret_manager_secret_uri.setter
    def gcp_secret_manager_secret_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientKeyArgsDict(
    TypedDict
):
    gcp_secret_manager_secret_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostClientKeyArgs:
    def __init__(
        __self__,
        *,
        gcp_secret_manager_secret_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_secret_manager_secret_uri.setter
    def gcp_secret_manager_secret_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostHeaderArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigRegistryHostHostHeaderArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigWritableCgroupsArgsDict(
    TypedDict
):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterNodePoolDefaultsNodeConfigDefaultsContainerdConfigWritableCgroupsArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterNodePoolDefaultsNodeConfigDefaultsGcfsConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterNodePoolDefaultsNodeConfigDefaultsGcfsConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterNodePoolManagementArgsDict(TypedDict):
    auto_repair: NotRequired[pulumi.Input[_builtins.bool]]
    auto_upgrade: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterNodePoolManagementArgs:
    def __init__(
        __self__,
        *,
        auto_repair: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRepair")
    def auto_repair(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_repair.setter
    def auto_repair(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="autoUpgrade")
    def auto_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_upgrade.setter
    def auto_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClusterNodePoolNetworkConfigArgsDict(TypedDict):
    accelerator_network_profile: NotRequired[pulumi.Input[_builtins.str]]
    additional_node_network_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolNetworkConfigAdditionalNodeNetworkConfigArgsDict
                ]
            ]
        ]
    ]
    additional_pod_network_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolNetworkConfigAdditionalPodNetworkConfigArgsDict
                ]
            ]
        ]
    ]
    create_pod_range: NotRequired[pulumi.Input[_builtins.bool]]
    enable_private_nodes: NotRequired[pulumi.Input[_builtins.bool]]
    network_performance_config: NotRequired[
        pulumi.Input[ClusterNodePoolNetworkConfigNetworkPerformanceConfigArgsDict]
    ]
    pod_cidr_overprovision_config: NotRequired[
        pulumi.Input[ClusterNodePoolNetworkConfigPodCidrOverprovisionConfigArgsDict]
    ]
    pod_ipv4_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    pod_range: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        accelerator_network_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        additional_node_network_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNetworkConfigAdditionalNodeNetworkConfigArgs
                    ]
                ]
            ]
        ] = ...,
        additional_pod_network_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNetworkConfigAdditionalPodNetworkConfigArgs
                    ]
                ]
            ]
        ] = ...,
        create_pod_range: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_private_nodes: Optional[pulumi.Input[_builtins.bool]] = ...,
        network_performance_config: Optional[
            pulumi.Input[ClusterNodePoolNetworkConfigNetworkPerformanceConfigArgs]
        ] = ...,
        pod_cidr_overprovision_config: Optional[
            pulumi.Input[ClusterNodePoolNetworkConfigPodCidrOverprovisionConfigArgs]
        ] = ...,
        pod_ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        pod_range: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorNetworkProfile")
    def accelerator_network_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accelerator_network_profile.setter
    def accelerator_network_profile(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalNodeNetworkConfigs")
    def additional_node_network_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolNetworkConfigAdditionalNodeNetworkConfigArgs
                ]
            ]
        ]
    ]: ...
    @additional_node_network_configs.setter
    def additional_node_network_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNetworkConfigAdditionalNodeNetworkConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalPodNetworkConfigs")
    def additional_pod_network_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClusterNodePoolNetworkConfigAdditionalPodNetworkConfigArgs]
            ]
        ]
    ]: ...
    @additional_pod_network_configs.setter
    def additional_pod_network_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNetworkConfigAdditionalPodNetworkConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createPodRange")
    def create_pod_range(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_pod_range.setter
    def create_pod_range(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateNodes")
    def enable_private_nodes(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_private_nodes.setter
    def enable_private_nodes(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfig")
    def network_performance_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNetworkConfigNetworkPerformanceConfigArgs]
    ]: ...
    @network_performance_config.setter
    def network_performance_config(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolNetworkConfigNetworkPerformanceConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="podCidrOverprovisionConfig")
    def pod_cidr_overprovision_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNetworkConfigPodCidrOverprovisionConfigArgs]
    ]: ...
    @pod_cidr_overprovision_config.setter
    def pod_cidr_overprovision_config(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolNetworkConfigPodCidrOverprovisionConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="podIpv4CidrBlock")
    def pod_ipv4_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pod_ipv4_cidr_block.setter
    def pod_ipv4_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="podRange")
    def pod_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pod_range.setter
    def pod_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolNetworkConfigAdditionalNodeNetworkConfigArgsDict(TypedDict):
    network: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNetworkConfigAdditionalNodeNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolNetworkConfigAdditionalPodNetworkConfigArgsDict(TypedDict):
    max_pods_per_node: NotRequired[pulumi.Input[_builtins.int]]
    secondary_pod_range: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNetworkConfigAdditionalPodNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ...,
        secondary_pod_range: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_pods_per_node.setter
    def max_pods_per_node(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryPodRange")
    def secondary_pod_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secondary_pod_range.setter
    def secondary_pod_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolNetworkConfigNetworkPerformanceConfigArgsDict(TypedDict):
    total_egress_bandwidth_tier: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterNodePoolNetworkConfigNetworkPerformanceConfigArgs:
    def __init__(
        __self__, *, total_egress_bandwidth_tier: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="totalEgressBandwidthTier")
    def total_egress_bandwidth_tier(self) -> pulumi.Input[_builtins.str]: ...
    @total_egress_bandwidth_tier.setter
    def total_egress_bandwidth_tier(self, value: pulumi.Input[_builtins.str]): ...

class ClusterNodePoolNetworkConfigPodCidrOverprovisionConfigArgsDict(TypedDict):
    disabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterNodePoolNetworkConfigPodCidrOverprovisionConfigArgs:
    def __init__(__self__, *, disabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Input[_builtins.bool]: ...
    @disabled.setter
    def disabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterNodePoolNodeConfigArgsDict(TypedDict):
    advanced_machine_features: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigAdvancedMachineFeaturesArgsDict]
    ]
    boot_disk: NotRequired[pulumi.Input[ClusterNodePoolNodeConfigBootDiskArgsDict]]
    boot_disk_kms_key: NotRequired[pulumi.Input[_builtins.str]]
    confidential_nodes: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigConfidentialNodesArgsDict]
    ]
    containerd_config: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigContainerdConfigArgsDict]
    ]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    disk_type: NotRequired[pulumi.Input[_builtins.str]]
    effective_taints: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterNodePoolNodeConfigEffectiveTaintArgsDict]]
        ]
    ]
    enable_confidential_storage: NotRequired[pulumi.Input[_builtins.bool]]
    ephemeral_storage_config: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigEphemeralStorageConfigArgsDict]
    ]
    ephemeral_storage_local_ssd_config: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigEphemeralStorageLocalSsdConfigArgsDict]
    ]
    fast_socket: NotRequired[pulumi.Input[ClusterNodePoolNodeConfigFastSocketArgsDict]]
    flex_start: NotRequired[pulumi.Input[_builtins.bool]]
    gcfs_config: NotRequired[pulumi.Input[ClusterNodePoolNodeConfigGcfsConfigArgsDict]]
    guest_accelerators: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterNodePoolNodeConfigGuestAcceleratorArgsDict]]
        ]
    ]
    gvnic: NotRequired[pulumi.Input[ClusterNodePoolNodeConfigGvnicArgsDict]]
    host_maintenance_policy: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigHostMaintenancePolicyArgsDict]
    ]
    image_type: NotRequired[pulumi.Input[_builtins.str]]
    kubelet_config: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigArgsDict]
    ]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    linux_node_config: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigLinuxNodeConfigArgsDict]
    ]
    local_nvme_ssd_block_config: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigLocalNvmeSsdBlockConfigArgsDict]
    ]
    local_ssd_count: NotRequired[pulumi.Input[_builtins.int]]
    local_ssd_encryption_mode: NotRequired[pulumi.Input[_builtins.str]]
    logging_variant: NotRequired[pulumi.Input[_builtins.str]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    max_run_duration: NotRequired[pulumi.Input[_builtins.str]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    min_cpu_platform: NotRequired[pulumi.Input[_builtins.str]]
    node_group: NotRequired[pulumi.Input[_builtins.str]]
    oauth_scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    preemptible: NotRequired[pulumi.Input[_builtins.bool]]
    reservation_affinity: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigReservationAffinityArgsDict]
    ]
    resource_labels: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    resource_manager_tags: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    sandbox_config: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigSandboxConfigArgsDict]
    ]
    secondary_boot_disks: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterNodePoolNodeConfigSecondaryBootDiskArgsDict]]
        ]
    ]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    shielded_instance_config: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigShieldedInstanceConfigArgsDict]
    ]
    sole_tenant_config: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigSoleTenantConfigArgsDict]
    ]
    spot: NotRequired[pulumi.Input[_builtins.bool]]
    storage_pools: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    taints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ClusterNodePoolNodeConfigTaintArgsDict]]]
    ]
    windows_node_config: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigWindowsNodeConfigArgsDict]
    ]
    workload_metadata_config: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigWorkloadMetadataConfigArgsDict]
    ]

@pulumi.input_type
class ClusterNodePoolNodeConfigArgs:
    def __init__(
        __self__,
        *,
        advanced_machine_features: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigAdvancedMachineFeaturesArgs]
        ] = ...,
        boot_disk: Optional[pulumi.Input[ClusterNodePoolNodeConfigBootDiskArgs]] = ...,
        boot_disk_kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        confidential_nodes: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigConfidentialNodesArgs]
        ] = ...,
        containerd_config: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigContainerdConfigArgs]
        ] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_taints: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterNodePoolNodeConfigEffectiveTaintArgs]]
            ]
        ] = ...,
        enable_confidential_storage: Optional[pulumi.Input[_builtins.bool]] = ...,
        ephemeral_storage_config: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigEphemeralStorageConfigArgs]
        ] = ...,
        ephemeral_storage_local_ssd_config: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigEphemeralStorageLocalSsdConfigArgs]
        ] = ...,
        fast_socket: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigFastSocketArgs]
        ] = ...,
        flex_start: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcfs_config: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigGcfsConfigArgs]
        ] = ...,
        guest_accelerators: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterNodePoolNodeConfigGuestAcceleratorArgs]]
            ]
        ] = ...,
        gvnic: Optional[pulumi.Input[ClusterNodePoolNodeConfigGvnicArgs]] = ...,
        host_maintenance_policy: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigHostMaintenancePolicyArgs]
        ] = ...,
        image_type: Optional[pulumi.Input[_builtins.str]] = ...,
        kubelet_config: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        linux_node_config: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigLinuxNodeConfigArgs]
        ] = ...,
        local_nvme_ssd_block_config: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigLocalNvmeSsdBlockConfigArgs]
        ] = ...,
        local_ssd_count: Optional[pulumi.Input[_builtins.int]] = ...,
        local_ssd_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_variant: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        max_run_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        node_group: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        preemptible: Optional[pulumi.Input[_builtins.bool]] = ...,
        reservation_affinity: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigReservationAffinityArgs]
        ] = ...,
        resource_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_manager_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        sandbox_config: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigSandboxConfigArgs]
        ] = ...,
        secondary_boot_disks: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterNodePoolNodeConfigSecondaryBootDiskArgs]]
            ]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigShieldedInstanceConfigArgs]
        ] = ...,
        sole_tenant_config: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigSoleTenantConfigArgs]
        ] = ...,
        spot: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_pools: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        taints: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterNodePoolNodeConfigTaintArgs]]]
        ] = ...,
        windows_node_config: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigWindowsNodeConfigArgs]
        ] = ...,
        workload_metadata_config: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigWorkloadMetadataConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNodeConfigAdvancedMachineFeaturesArgs]
    ]: ...
    @advanced_machine_features.setter
    def advanced_machine_features(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigAdvancedMachineFeaturesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bootDisk")
    def boot_disk(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolNodeConfigBootDiskArgs]]: ...
    @boot_disk.setter
    def boot_disk(
        self, value: Optional[pulumi.Input[ClusterNodePoolNodeConfigBootDiskArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bootDiskKmsKey")
    def boot_disk_kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @boot_disk_kms_key.setter
    def boot_disk_kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="confidentialNodes")
    def confidential_nodes(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolNodeConfigConfidentialNodesArgs]]: ...
    @confidential_nodes.setter
    def confidential_nodes(
        self,
        value: Optional[pulumi.Input[ClusterNodePoolNodeConfigConfidentialNodesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerdConfig")
    def containerd_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolNodeConfigContainerdConfigArgs]]: ...
    @containerd_config.setter
    def containerd_config(
        self,
        value: Optional[pulumi.Input[ClusterNodePoolNodeConfigContainerdConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveTaints")
    def effective_taints(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterNodePoolNodeConfigEffectiveTaintArgs]]
        ]
    ]: ...
    @effective_taints.setter
    def effective_taints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterNodePoolNodeConfigEffectiveTaintArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableConfidentialStorage")
    def enable_confidential_storage(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_confidential_storage.setter
    def enable_confidential_storage(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageConfig")
    def ephemeral_storage_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNodeConfigEphemeralStorageConfigArgs]
    ]: ...
    @ephemeral_storage_config.setter
    def ephemeral_storage_config(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigEphemeralStorageConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageLocalSsdConfig")
    def ephemeral_storage_local_ssd_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNodeConfigEphemeralStorageLocalSsdConfigArgs]
    ]: ...
    @ephemeral_storage_local_ssd_config.setter
    def ephemeral_storage_local_ssd_config(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigEphemeralStorageLocalSsdConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fastSocket")
    def fast_socket(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolNodeConfigFastSocketArgs]]: ...
    @fast_socket.setter
    def fast_socket(
        self, value: Optional[pulumi.Input[ClusterNodePoolNodeConfigFastSocketArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="flexStart")
    def flex_start(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @flex_start.setter
    def flex_start(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="gcfsConfig")
    def gcfs_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolNodeConfigGcfsConfigArgs]]: ...
    @gcfs_config.setter
    def gcfs_config(
        self, value: Optional[pulumi.Input[ClusterNodePoolNodeConfigGcfsConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterNodePoolNodeConfigGuestAcceleratorArgs]]
        ]
    ]: ...
    @guest_accelerators.setter
    def guest_accelerators(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterNodePoolNodeConfigGuestAcceleratorArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def gvnic(self) -> Optional[pulumi.Input[ClusterNodePoolNodeConfigGvnicArgs]]: ...
    @gvnic.setter
    def gvnic(
        self, value: Optional[pulumi.Input[ClusterNodePoolNodeConfigGvnicArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hostMaintenancePolicy")
    def host_maintenance_policy(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolNodeConfigHostMaintenancePolicyArgs]]: ...
    @host_maintenance_policy.setter
    def host_maintenance_policy(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigHostMaintenancePolicyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_type.setter
    def image_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigArgs]]: ...
    @kubelet_config.setter
    def kubelet_config(
        self, value: Optional[pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linuxNodeConfig")
    def linux_node_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolNodeConfigLinuxNodeConfigArgs]]: ...
    @linux_node_config.setter
    def linux_node_config(
        self,
        value: Optional[pulumi.Input[ClusterNodePoolNodeConfigLinuxNodeConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localNvmeSsdBlockConfig")
    def local_nvme_ssd_block_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNodeConfigLocalNvmeSsdBlockConfigArgs]
    ]: ...
    @local_nvme_ssd_block_config.setter
    def local_nvme_ssd_block_config(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigLocalNvmeSsdBlockConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @local_ssd_count.setter
    def local_ssd_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="localSsdEncryptionMode")
    def local_ssd_encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_ssd_encryption_mode.setter
    def local_ssd_encryption_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingVariant")
    def logging_variant(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logging_variant.setter
    def logging_variant(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRunDuration")
    def max_run_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_run_duration.setter
    def max_run_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeGroup")
    def node_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_group.setter
    def node_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @oauth_scopes.setter
    def oauth_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def preemptible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preemptible.setter
    def preemptible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolNodeConfigReservationAffinityArgs]]: ...
    @reservation_affinity.setter
    def reservation_affinity(
        self,
        value: Optional[pulumi.Input[ClusterNodePoolNodeConfigReservationAffinityArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceLabels")
    def resource_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @resource_labels.setter
    def resource_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @resource_manager_tags.setter
    def resource_manager_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sandboxConfig")
    def sandbox_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolNodeConfigSandboxConfigArgs]]: ...
    @sandbox_config.setter
    def sandbox_config(
        self, value: Optional[pulumi.Input[ClusterNodePoolNodeConfigSandboxConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secondaryBootDisks")
    def secondary_boot_disks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterNodePoolNodeConfigSecondaryBootDiskArgs]]
        ]
    ]: ...
    @secondary_boot_disks.setter
    def secondary_boot_disks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterNodePoolNodeConfigSecondaryBootDiskArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNodeConfigShieldedInstanceConfigArgs]
    ]: ...
    @shielded_instance_config.setter
    def shielded_instance_config(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigShieldedInstanceConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="soleTenantConfig")
    def sole_tenant_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolNodeConfigSoleTenantConfigArgs]]: ...
    @sole_tenant_config.setter
    def sole_tenant_config(
        self,
        value: Optional[pulumi.Input[ClusterNodePoolNodeConfigSoleTenantConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def spot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @spot.setter
    def spot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="storagePools")
    def storage_pools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @storage_pools.setter
    def storage_pools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def taints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterNodePoolNodeConfigTaintArgs]]]
    ]: ...
    @taints.setter
    def taints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterNodePoolNodeConfigTaintArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="windowsNodeConfig")
    def windows_node_config(
        self,
    ) -> Optional[pulumi.Input[ClusterNodePoolNodeConfigWindowsNodeConfigArgs]]: ...
    @windows_node_config.setter
    def windows_node_config(
        self,
        value: Optional[pulumi.Input[ClusterNodePoolNodeConfigWindowsNodeConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="workloadMetadataConfig")
    def workload_metadata_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNodeConfigWorkloadMetadataConfigArgs]
    ]: ...
    @workload_metadata_config.setter
    def workload_metadata_config(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigWorkloadMetadataConfigArgs]
        ],
    ): ...

class ClusterNodePoolNodeConfigAdvancedMachineFeaturesArgsDict(TypedDict):
    threads_per_core: pulumi.Input[_builtins.int]
    enable_nested_virtualization: NotRequired[pulumi.Input[_builtins.bool]]
    performance_monitoring_unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigAdvancedMachineFeaturesArgs:
    def __init__(
        __self__,
        *,
        threads_per_core: pulumi.Input[_builtins.int],
        enable_nested_virtualization: Optional[pulumi.Input[_builtins.bool]] = ...,
        performance_monitoring_unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> pulumi.Input[_builtins.int]: ...
    @threads_per_core.setter
    def threads_per_core(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_nested_virtualization.setter
    def enable_nested_virtualization(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceMonitoringUnit")
    def performance_monitoring_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @performance_monitoring_unit.setter
    def performance_monitoring_unit(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodePoolNodeConfigBootDiskArgsDict(TypedDict):
    disk_type: NotRequired[pulumi.Input[_builtins.str]]
    provisioned_iops: NotRequired[pulumi.Input[_builtins.int]]
    provisioned_throughput: NotRequired[pulumi.Input[_builtins.int]]
    size_gb: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterNodePoolNodeConfigBootDiskArgs:
    def __init__(
        __self__,
        *,
        disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_iops: Optional[pulumi.Input[_builtins.int]] = ...,
        provisioned_throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_iops.setter
    def provisioned_iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_throughput.setter
    def provisioned_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size_gb.setter
    def size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterNodePoolNodeConfigConfidentialNodesArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    confidential_instance_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigConfidentialNodesArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        confidential_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceType")
    def confidential_instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @confidential_instance_type.setter
    def confidential_instance_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodePoolNodeConfigContainerdConfigArgsDict(TypedDict):
    private_registry_access_config: NotRequired[
        pulumi.Input[
            ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigArgsDict
        ]
    ]
    registry_hosts: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolNodeConfigContainerdConfigRegistryHostArgsDict
                ]
            ]
        ]
    ]
    writable_cgroups: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigContainerdConfigWritableCgroupsArgsDict]
    ]

@pulumi.input_type
class ClusterNodePoolNodeConfigContainerdConfigArgs:
    def __init__(
        __self__,
        *,
        private_registry_access_config: Optional[
            pulumi.Input[
                ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigArgs
            ]
        ] = ...,
        registry_hosts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNodeConfigContainerdConfigRegistryHostArgs
                    ]
                ]
            ]
        ] = ...,
        writable_cgroups: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigContainerdConfigWritableCgroupsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateRegistryAccessConfig")
    def private_registry_access_config(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigArgs
        ]
    ]: ...
    @private_registry_access_config.setter
    def private_registry_access_config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="registryHosts")
    def registry_hosts(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClusterNodePoolNodeConfigContainerdConfigRegistryHostArgs]
            ]
        ]
    ]: ...
    @registry_hosts.setter
    def registry_hosts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNodeConfigContainerdConfigRegistryHostArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="writableCgroups")
    def writable_cgroups(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNodeConfigContainerdConfigWritableCgroupsArgs]
    ]: ...
    @writable_cgroups.setter
    def writable_cgroups(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigContainerdConfigWritableCgroupsArgs]
        ],
    ): ...

class ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigArgsDict(
    TypedDict
):
    enabled: pulumi.Input[_builtins.bool]
    certificate_authority_domain_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        certificate_authority_domain_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityDomainConfigs")
    def certificate_authority_domain_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs
                ]
            ]
        ]
    ]: ...
    @certificate_authority_domain_configs.setter
    def certificate_authority_domain_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgsDict(
    TypedDict
):
    fqdns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    gcp_secret_manager_certificate_config: pulumi.Input[
        ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgsDict
    ]

@pulumi.input_type
class ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs:
    def __init__(
        __self__,
        *,
        fqdns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        gcp_secret_manager_certificate_config: pulumi.Input[
            ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @fqdns.setter
    def fqdns(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerCertificateConfig")
    def gcp_secret_manager_certificate_config(
        self,
    ) -> pulumi.Input[
        ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs
    ]: ...
    @gcp_secret_manager_certificate_config.setter
    def gcp_secret_manager_certificate_config(
        self,
        value: pulumi.Input[
            ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs
        ],
    ): ...

class ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgsDict(
    TypedDict
):
    secret_uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterNodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs:
    def __init__(__self__, *, secret_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretUri")
    def secret_uri(self) -> pulumi.Input[_builtins.str]: ...
    @secret_uri.setter
    def secret_uri(self, value: pulumi.Input[_builtins.str]): ...

class ClusterNodePoolNodeConfigContainerdConfigRegistryHostArgsDict(TypedDict):
    server: pulumi.Input[_builtins.str]
    hosts: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ClusterNodePoolNodeConfigContainerdConfigRegistryHostArgs:
    def __init__(
        __self__,
        *,
        server: pulumi.Input[_builtins.str],
        hosts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> pulumi.Input[_builtins.str]: ...
    @server.setter
    def server(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def hosts(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostArgs
                ]
            ]
        ]
    ]: ...
    @hosts.setter
    def hosts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostArgs
                    ]
                ]
            ]
        ],
    ): ...

class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostArgsDict(TypedDict):
    host: pulumi.Input[_builtins.str]
    capabilities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    cas: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostCaArgsDict
                ]
            ]
        ]
    ]
    clients: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientArgsDict
                ]
            ]
        ]
    ]
    dial_timeout: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostHeaderArgsDict
                ]
            ]
        ]
    ]
    override_path: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostArgs:
    def __init__(
        __self__,
        *,
        host: pulumi.Input[_builtins.str],
        capabilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostCaArgs
                    ]
                ]
            ]
        ] = ...,
        clients: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientArgs
                    ]
                ]
            ]
        ] = ...,
        dial_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        headers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostHeaderArgs
                    ]
                ]
            ]
        ] = ...,
        override_path: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def capabilities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @capabilities.setter
    def capabilities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def cas(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostCaArgs
                ]
            ]
        ]
    ]: ...
    @cas.setter
    def cas(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostCaArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def clients(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientArgs
                ]
            ]
        ]
    ]: ...
    @clients.setter
    def clients(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dialTimeout")
    def dial_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dial_timeout.setter
    def dial_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostHeaderArgs
                ]
            ]
        ]
    ]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostHeaderArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="overridePath")
    def override_path(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @override_path.setter
    def override_path(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostCaArgsDict(TypedDict):
    gcp_secret_manager_secret_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostCaArgs:
    def __init__(
        __self__,
        *,
        gcp_secret_manager_secret_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_secret_manager_secret_uri.setter
    def gcp_secret_manager_secret_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientArgsDict(
    TypedDict
):
    cert: pulumi.Input[
        ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientCertArgsDict
    ]
    key: NotRequired[
        pulumi.Input[
            ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientKeyArgsDict
        ]
    ]

@pulumi.input_type
class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientArgs:
    def __init__(
        __self__,
        *,
        cert: pulumi.Input[
            ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientCertArgs
        ],
        key: Optional[
            pulumi.Input[
                ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientKeyArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(
        self,
    ) -> pulumi.Input[
        ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientCertArgs
    ]: ...
    @cert.setter
    def cert(
        self,
        value: pulumi.Input[
            ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientCertArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientKeyArgs
        ]
    ]: ...
    @key.setter
    def key(
        self,
        value: Optional[
            pulumi.Input[
                ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientKeyArgs
            ]
        ],
    ): ...

class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientCertArgsDict(
    TypedDict
):
    gcp_secret_manager_secret_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientCertArgs:
    def __init__(
        __self__,
        *,
        gcp_secret_manager_secret_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_secret_manager_secret_uri.setter
    def gcp_secret_manager_secret_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientKeyArgsDict(
    TypedDict
):
    gcp_secret_manager_secret_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostClientKeyArgs:
    def __init__(
        __self__,
        *,
        gcp_secret_manager_secret_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_secret_manager_secret_uri.setter
    def gcp_secret_manager_secret_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostHeaderArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ClusterNodePoolNodeConfigContainerdConfigRegistryHostHostHeaderArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ClusterNodePoolNodeConfigContainerdConfigWritableCgroupsArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterNodePoolNodeConfigContainerdConfigWritableCgroupsArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterNodePoolNodeConfigEffectiveTaintArgsDict(TypedDict):
    effect: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigEffectiveTaintArgs:
    def __init__(
        __self__,
        *,
        effect: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effect.setter
    def effect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolNodeConfigEphemeralStorageConfigArgsDict(TypedDict):
    local_ssd_count: pulumi.Input[_builtins.int]

@pulumi.input_type
class ClusterNodePoolNodeConfigEphemeralStorageConfigArgs:
    def __init__(__self__, *, local_ssd_count: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> pulumi.Input[_builtins.int]: ...
    @local_ssd_count.setter
    def local_ssd_count(self, value: pulumi.Input[_builtins.int]): ...

class ClusterNodePoolNodeConfigEphemeralStorageLocalSsdConfigArgsDict(TypedDict):
    local_ssd_count: pulumi.Input[_builtins.int]
    data_cache_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterNodePoolNodeConfigEphemeralStorageLocalSsdConfigArgs:
    def __init__(
        __self__,
        *,
        local_ssd_count: pulumi.Input[_builtins.int],
        data_cache_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> pulumi.Input[_builtins.int]: ...
    @local_ssd_count.setter
    def local_ssd_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="dataCacheCount")
    def data_cache_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_cache_count.setter
    def data_cache_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterNodePoolNodeConfigFastSocketArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterNodePoolNodeConfigFastSocketArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterNodePoolNodeConfigGcfsConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterNodePoolNodeConfigGcfsConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterNodePoolNodeConfigGuestAcceleratorArgsDict(TypedDict):
    count: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]
    gpu_driver_installation_config: NotRequired[
        pulumi.Input[
            ClusterNodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgsDict
        ]
    ]
    gpu_partition_size: NotRequired[pulumi.Input[_builtins.str]]
    gpu_sharing_config: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigGuestAcceleratorGpuSharingConfigArgsDict]
    ]

@pulumi.input_type
class ClusterNodePoolNodeConfigGuestAcceleratorArgs:
    def __init__(
        __self__,
        *,
        count: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.str],
        gpu_driver_installation_config: Optional[
            pulumi.Input[
                ClusterNodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgs
            ]
        ] = ...,
        gpu_partition_size: Optional[pulumi.Input[_builtins.str]] = ...,
        gpu_sharing_config: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigGuestAcceleratorGpuSharingConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> pulumi.Input[_builtins.int]: ...
    @count.setter
    def count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverInstallationConfig")
    def gpu_driver_installation_config(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterNodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgs
        ]
    ]: ...
    @gpu_driver_installation_config.setter
    def gpu_driver_installation_config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterNodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gpuPartitionSize")
    def gpu_partition_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gpu_partition_size.setter
    def gpu_partition_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingConfig")
    def gpu_sharing_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNodeConfigGuestAcceleratorGpuSharingConfigArgs]
    ]: ...
    @gpu_sharing_config.setter
    def gpu_sharing_config(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigGuestAcceleratorGpuSharingConfigArgs]
        ],
    ): ...

class ClusterNodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgsDict(
    TypedDict
):
    gpu_driver_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterNodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgs:
    def __init__(
        __self__, *, gpu_driver_version: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverVersion")
    def gpu_driver_version(self) -> pulumi.Input[_builtins.str]: ...
    @gpu_driver_version.setter
    def gpu_driver_version(self, value: pulumi.Input[_builtins.str]): ...

class ClusterNodePoolNodeConfigGuestAcceleratorGpuSharingConfigArgsDict(TypedDict):
    gpu_sharing_strategy: pulumi.Input[_builtins.str]
    max_shared_clients_per_gpu: pulumi.Input[_builtins.int]

@pulumi.input_type
class ClusterNodePoolNodeConfigGuestAcceleratorGpuSharingConfigArgs:
    def __init__(
        __self__,
        *,
        gpu_sharing_strategy: pulumi.Input[_builtins.str],
        max_shared_clients_per_gpu: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingStrategy")
    def gpu_sharing_strategy(self) -> pulumi.Input[_builtins.str]: ...
    @gpu_sharing_strategy.setter
    def gpu_sharing_strategy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maxSharedClientsPerGpu")
    def max_shared_clients_per_gpu(self) -> pulumi.Input[_builtins.int]: ...
    @max_shared_clients_per_gpu.setter
    def max_shared_clients_per_gpu(self, value: pulumi.Input[_builtins.int]): ...

class ClusterNodePoolNodeConfigGvnicArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterNodePoolNodeConfigGvnicArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterNodePoolNodeConfigHostMaintenancePolicyArgsDict(TypedDict):
    maintenance_interval: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterNodePoolNodeConfigHostMaintenancePolicyArgs:
    def __init__(
        __self__, *, maintenance_interval: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceInterval")
    def maintenance_interval(self) -> pulumi.Input[_builtins.str]: ...
    @maintenance_interval.setter
    def maintenance_interval(self, value: pulumi.Input[_builtins.str]): ...

class ClusterNodePoolNodeConfigKubeletConfigArgsDict(TypedDict):
    allowed_unsafe_sysctls: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    container_log_max_files: NotRequired[pulumi.Input[_builtins.int]]
    container_log_max_size: NotRequired[pulumi.Input[_builtins.str]]
    cpu_cfs_quota: NotRequired[pulumi.Input[_builtins.bool]]
    cpu_cfs_quota_period: NotRequired[pulumi.Input[_builtins.str]]
    cpu_manager_policy: NotRequired[pulumi.Input[_builtins.str]]
    eviction_max_pod_grace_period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    eviction_minimum_reclaim: NotRequired[
        pulumi.Input[
            ClusterNodePoolNodeConfigKubeletConfigEvictionMinimumReclaimArgsDict
        ]
    ]
    eviction_soft: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigEvictionSoftArgsDict]
    ]
    eviction_soft_grace_period: NotRequired[
        pulumi.Input[
            ClusterNodePoolNodeConfigKubeletConfigEvictionSoftGracePeriodArgsDict
        ]
    ]
    image_gc_high_threshold_percent: NotRequired[pulumi.Input[_builtins.int]]
    image_gc_low_threshold_percent: NotRequired[pulumi.Input[_builtins.int]]
    image_maximum_gc_age: NotRequired[pulumi.Input[_builtins.str]]
    image_minimum_gc_age: NotRequired[pulumi.Input[_builtins.str]]
    insecure_kubelet_readonly_port_enabled: NotRequired[pulumi.Input[_builtins.str]]
    max_parallel_image_pulls: NotRequired[pulumi.Input[_builtins.int]]
    memory_manager: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigMemoryManagerArgsDict]
    ]
    pod_pids_limit: NotRequired[pulumi.Input[_builtins.int]]
    single_process_oom_kill: NotRequired[pulumi.Input[_builtins.bool]]
    topology_manager: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigTopologyManagerArgsDict]
    ]

@pulumi.input_type
class ClusterNodePoolNodeConfigKubeletConfigArgs:
    def __init__(
        __self__,
        *,
        allowed_unsafe_sysctls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        container_log_max_files: Optional[pulumi.Input[_builtins.int]] = ...,
        container_log_max_size: Optional[pulumi.Input[_builtins.str]] = ...,
        cpu_cfs_quota: Optional[pulumi.Input[_builtins.bool]] = ...,
        cpu_cfs_quota_period: Optional[pulumi.Input[_builtins.str]] = ...,
        cpu_manager_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        eviction_max_pod_grace_period_seconds: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        eviction_minimum_reclaim: Optional[
            pulumi.Input[
                ClusterNodePoolNodeConfigKubeletConfigEvictionMinimumReclaimArgs
            ]
        ] = ...,
        eviction_soft: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigEvictionSoftArgs]
        ] = ...,
        eviction_soft_grace_period: Optional[
            pulumi.Input[
                ClusterNodePoolNodeConfigKubeletConfigEvictionSoftGracePeriodArgs
            ]
        ] = ...,
        image_gc_high_threshold_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        image_gc_low_threshold_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        image_maximum_gc_age: Optional[pulumi.Input[_builtins.str]] = ...,
        image_minimum_gc_age: Optional[pulumi.Input[_builtins.str]] = ...,
        insecure_kubelet_readonly_port_enabled: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        max_parallel_image_pulls: Optional[pulumi.Input[_builtins.int]] = ...,
        memory_manager: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigMemoryManagerArgs]
        ] = ...,
        pod_pids_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        single_process_oom_kill: Optional[pulumi.Input[_builtins.bool]] = ...,
        topology_manager: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigTopologyManagerArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedUnsafeSysctls")
    def allowed_unsafe_sysctls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_unsafe_sysctls.setter
    def allowed_unsafe_sysctls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxFiles")
    def container_log_max_files(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @container_log_max_files.setter
    def container_log_max_files(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxSize")
    def container_log_max_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_log_max_size.setter
    def container_log_max_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuota")
    def cpu_cfs_quota(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cpu_cfs_quota.setter
    def cpu_cfs_quota(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuotaPeriod")
    def cpu_cfs_quota_period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu_cfs_quota_period.setter
    def cpu_cfs_quota_period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuManagerPolicy")
    def cpu_manager_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu_manager_policy.setter
    def cpu_manager_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="evictionMaxPodGracePeriodSeconds")
    def eviction_max_pod_grace_period_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @eviction_max_pod_grace_period_seconds.setter
    def eviction_max_pod_grace_period_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="evictionMinimumReclaim")
    def eviction_minimum_reclaim(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigEvictionMinimumReclaimArgs]
    ]: ...
    @eviction_minimum_reclaim.setter
    def eviction_minimum_reclaim(
        self,
        value: Optional[
            pulumi.Input[
                ClusterNodePoolNodeConfigKubeletConfigEvictionMinimumReclaimArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="evictionSoft")
    def eviction_soft(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigEvictionSoftArgs]
    ]: ...
    @eviction_soft.setter
    def eviction_soft(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigEvictionSoftArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="evictionSoftGracePeriod")
    def eviction_soft_grace_period(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigEvictionSoftGracePeriodArgs]
    ]: ...
    @eviction_soft_grace_period.setter
    def eviction_soft_grace_period(
        self,
        value: Optional[
            pulumi.Input[
                ClusterNodePoolNodeConfigKubeletConfigEvictionSoftGracePeriodArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageGcHighThresholdPercent")
    def image_gc_high_threshold_percent(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @image_gc_high_threshold_percent.setter
    def image_gc_high_threshold_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageGcLowThresholdPercent")
    def image_gc_low_threshold_percent(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @image_gc_low_threshold_percent.setter
    def image_gc_low_threshold_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageMaximumGcAge")
    def image_maximum_gc_age(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_maximum_gc_age.setter
    def image_maximum_gc_age(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageMinimumGcAge")
    def image_minimum_gc_age(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_minimum_gc_age.setter
    def image_minimum_gc_age(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="insecureKubeletReadonlyPortEnabled")
    def insecure_kubelet_readonly_port_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @insecure_kubelet_readonly_port_enabled.setter
    def insecure_kubelet_readonly_port_enabled(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxParallelImagePulls")
    def max_parallel_image_pulls(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_parallel_image_pulls.setter
    def max_parallel_image_pulls(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="memoryManager")
    def memory_manager(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigMemoryManagerArgs]
    ]: ...
    @memory_manager.setter
    def memory_manager(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigMemoryManagerArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="podPidsLimit")
    def pod_pids_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pod_pids_limit.setter
    def pod_pids_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="singleProcessOomKill")
    def single_process_oom_kill(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @single_process_oom_kill.setter
    def single_process_oom_kill(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="topologyManager")
    def topology_manager(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigTopologyManagerArgs]
    ]: ...
    @topology_manager.setter
    def topology_manager(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigKubeletConfigTopologyManagerArgs]
        ],
    ): ...

class ClusterNodePoolNodeConfigKubeletConfigEvictionMinimumReclaimArgsDict(TypedDict):
    imagefs_available: NotRequired[pulumi.Input[_builtins.str]]
    imagefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    memory_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    pid_available: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigKubeletConfigEvictionMinimumReclaimArgs:
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        imagefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        pid_available: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_available.setter
    def imagefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_inodes_free.setter
    def imagefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory_available.setter
    def memory_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_available.setter
    def nodefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_inodes_free.setter
    def nodefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pid_available.setter
    def pid_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolNodeConfigKubeletConfigEvictionSoftArgsDict(TypedDict):
    imagefs_available: NotRequired[pulumi.Input[_builtins.str]]
    imagefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    memory_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    pid_available: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigKubeletConfigEvictionSoftArgs:
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        imagefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        pid_available: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_available.setter
    def imagefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_inodes_free.setter
    def imagefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory_available.setter
    def memory_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_available.setter
    def nodefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_inodes_free.setter
    def nodefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pid_available.setter
    def pid_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolNodeConfigKubeletConfigEvictionSoftGracePeriodArgsDict(TypedDict):
    imagefs_available: NotRequired[pulumi.Input[_builtins.str]]
    imagefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    memory_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    pid_available: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigKubeletConfigEvictionSoftGracePeriodArgs:
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        imagefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        pid_available: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_available.setter
    def imagefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_inodes_free.setter
    def imagefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory_available.setter
    def memory_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_available.setter
    def nodefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_inodes_free.setter
    def nodefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pid_available.setter
    def pid_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolNodeConfigKubeletConfigMemoryManagerArgsDict(TypedDict):
    policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigKubeletConfigMemoryManagerArgs:
    def __init__(
        __self__, *, policy: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolNodeConfigKubeletConfigTopologyManagerArgsDict(TypedDict):
    policy: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigKubeletConfigTopologyManagerArgs:
    def __init__(
        __self__,
        *,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolNodeConfigLinuxNodeConfigArgsDict(TypedDict):
    cgroup_mode: NotRequired[pulumi.Input[_builtins.str]]
    hugepages_config: NotRequired[
        pulumi.Input[ClusterNodePoolNodeConfigLinuxNodeConfigHugepagesConfigArgsDict]
    ]
    node_kernel_module_loading: NotRequired[
        pulumi.Input[
            ClusterNodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgsDict
        ]
    ]
    sysctls: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    transparent_hugepage_defrag: NotRequired[pulumi.Input[_builtins.str]]
    transparent_hugepage_enabled: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigLinuxNodeConfigArgs:
    def __init__(
        __self__,
        *,
        cgroup_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        hugepages_config: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigLinuxNodeConfigHugepagesConfigArgs]
        ] = ...,
        node_kernel_module_loading: Optional[
            pulumi.Input[
                ClusterNodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgs
            ]
        ] = ...,
        sysctls: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transparent_hugepage_defrag: Optional[pulumi.Input[_builtins.str]] = ...,
        transparent_hugepage_enabled: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cgroupMode")
    def cgroup_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cgroup_mode.setter
    def cgroup_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hugepagesConfig")
    def hugepages_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolNodeConfigLinuxNodeConfigHugepagesConfigArgs]
    ]: ...
    @hugepages_config.setter
    def hugepages_config(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolNodeConfigLinuxNodeConfigHugepagesConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeKernelModuleLoading")
    def node_kernel_module_loading(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterNodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgs
        ]
    ]: ...
    @node_kernel_module_loading.setter
    def node_kernel_module_loading(
        self,
        value: Optional[
            pulumi.Input[
                ClusterNodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sysctls(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @sysctls.setter
    def sysctls(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageDefrag")
    def transparent_hugepage_defrag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transparent_hugepage_defrag.setter
    def transparent_hugepage_defrag(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageEnabled")
    def transparent_hugepage_enabled(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transparent_hugepage_enabled.setter
    def transparent_hugepage_enabled(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterNodePoolNodeConfigLinuxNodeConfigHugepagesConfigArgsDict(TypedDict):
    hugepage_size1g: NotRequired[pulumi.Input[_builtins.int]]
    hugepage_size2m: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterNodePoolNodeConfigLinuxNodeConfigHugepagesConfigArgs:
    def __init__(
        __self__,
        *,
        hugepage_size1g: Optional[pulumi.Input[_builtins.int]] = ...,
        hugepage_size2m: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize1g")
    def hugepage_size1g(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hugepage_size1g.setter
    def hugepage_size1g(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize2m")
    def hugepage_size2m(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hugepage_size2m.setter
    def hugepage_size2m(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterNodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgsDict(
    TypedDict
):
    policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgs:
    def __init__(
        __self__, *, policy: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolNodeConfigLocalNvmeSsdBlockConfigArgsDict(TypedDict):
    local_ssd_count: pulumi.Input[_builtins.int]

@pulumi.input_type
class ClusterNodePoolNodeConfigLocalNvmeSsdBlockConfigArgs:
    def __init__(__self__, *, local_ssd_count: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> pulumi.Input[_builtins.int]: ...
    @local_ssd_count.setter
    def local_ssd_count(self, value: pulumi.Input[_builtins.int]): ...

class ClusterNodePoolNodeConfigReservationAffinityArgsDict(TypedDict):
    consume_reservation_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ClusterNodePoolNodeConfigReservationAffinityArgs:
    def __init__(
        __self__,
        *,
        consume_reservation_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> pulumi.Input[_builtins.str]: ...
    @consume_reservation_type.setter
    def consume_reservation_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterNodePoolNodeConfigSandboxConfigArgsDict(TypedDict):
    sandbox_type: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigSandboxConfigArgs:
    def __init__(
        __self__,
        *,
        sandbox_type: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sandboxType")
    @_utilities.deprecated(...)
    def sandbox_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sandbox_type.setter
    def sandbox_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolNodeConfigSecondaryBootDiskArgsDict(TypedDict):
    disk_image: pulumi.Input[_builtins.str]
    mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigSecondaryBootDiskArgs:
    def __init__(
        __self__,
        *,
        disk_image: pulumi.Input[_builtins.str],
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskImage")
    def disk_image(self) -> pulumi.Input[_builtins.str]: ...
    @disk_image.setter
    def disk_image(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolNodeConfigShieldedInstanceConfigArgsDict(TypedDict):
    enable_integrity_monitoring: NotRequired[pulumi.Input[_builtins.bool]]
    enable_secure_boot: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterNodePoolNodeConfigShieldedInstanceConfigArgs:
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_secure_boot: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_integrity_monitoring.setter
    def enable_integrity_monitoring(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_secure_boot.setter
    def enable_secure_boot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClusterNodePoolNodeConfigSoleTenantConfigArgsDict(TypedDict):
    node_affinities: pulumi.Input[
        Sequence[
            pulumi.Input[ClusterNodePoolNodeConfigSoleTenantConfigNodeAffinityArgsDict]
        ]
    ]
    min_node_cpus: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterNodePoolNodeConfigSoleTenantConfigArgs:
    def __init__(
        __self__,
        *,
        node_affinities: pulumi.Input[
            Sequence[
                pulumi.Input[ClusterNodePoolNodeConfigSoleTenantConfigNodeAffinityArgs]
            ]
        ],
        min_node_cpus: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeAffinities")
    def node_affinities(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[ClusterNodePoolNodeConfigSoleTenantConfigNodeAffinityArgs]
        ]
    ]: ...
    @node_affinities.setter
    def node_affinities(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[ClusterNodePoolNodeConfigSoleTenantConfigNodeAffinityArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minNodeCpus")
    def min_node_cpus(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_node_cpus.setter
    def min_node_cpus(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterNodePoolNodeConfigSoleTenantConfigNodeAffinityArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    operator: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ClusterNodePoolNodeConfigSoleTenantConfigNodeAffinityArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        operator: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[_builtins.str]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ClusterNodePoolNodeConfigTaintArgsDict(TypedDict):
    effect: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterNodePoolNodeConfigTaintArgs:
    def __init__(
        __self__,
        *,
        effect: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> pulumi.Input[_builtins.str]: ...
    @effect.setter
    def effect(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ClusterNodePoolNodeConfigWindowsNodeConfigArgsDict(TypedDict):
    osversion: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolNodeConfigWindowsNodeConfigArgs:
    def __init__(
        __self__, *, osversion: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def osversion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @osversion.setter
    def osversion(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolNodeConfigWorkloadMetadataConfigArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterNodePoolNodeConfigWorkloadMetadataConfigArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...

class ClusterNodePoolNodeDrainConfigArgsDict(TypedDict):
    respect_pdb_during_node_pool_deletion: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterNodePoolNodeDrainConfigArgs:
    def __init__(
        __self__,
        *,
        respect_pdb_during_node_pool_deletion: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="respectPdbDuringNodePoolDeletion")
    def respect_pdb_during_node_pool_deletion(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @respect_pdb_during_node_pool_deletion.setter
    def respect_pdb_during_node_pool_deletion(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ClusterNodePoolPlacementPolicyArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]
    tpu_topology: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolPlacementPolicyArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tpu_topology: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tpuTopology")
    def tpu_topology(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tpu_topology.setter
    def tpu_topology(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolQueuedProvisioningArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterNodePoolQueuedProvisioningArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterNodePoolUpgradeSettingsArgsDict(TypedDict):
    blue_green_settings: NotRequired[
        pulumi.Input[ClusterNodePoolUpgradeSettingsBlueGreenSettingsArgsDict]
    ]
    max_surge: NotRequired[pulumi.Input[_builtins.int]]
    max_unavailable: NotRequired[pulumi.Input[_builtins.int]]
    strategy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolUpgradeSettingsArgs:
    def __init__(
        __self__,
        *,
        blue_green_settings: Optional[
            pulumi.Input[ClusterNodePoolUpgradeSettingsBlueGreenSettingsArgs]
        ] = ...,
        max_surge: Optional[pulumi.Input[_builtins.int]] = ...,
        max_unavailable: Optional[pulumi.Input[_builtins.int]] = ...,
        strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blueGreenSettings")
    def blue_green_settings(
        self,
    ) -> Optional[
        pulumi.Input[ClusterNodePoolUpgradeSettingsBlueGreenSettingsArgs]
    ]: ...
    @blue_green_settings.setter
    def blue_green_settings(
        self,
        value: Optional[
            pulumi.Input[ClusterNodePoolUpgradeSettingsBlueGreenSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxSurge")
    def max_surge(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_surge.setter
    def max_surge(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxUnavailable")
    def max_unavailable(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_unavailable.setter
    def max_unavailable(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @strategy.setter
    def strategy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolUpgradeSettingsBlueGreenSettingsArgsDict(TypedDict):
    autoscaled_rollout_policy: NotRequired[
        pulumi.Input[
            ClusterNodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicyArgsDict
        ]
    ]
    node_pool_soak_duration: NotRequired[pulumi.Input[_builtins.str]]
    standard_rollout_policy: NotRequired[
        pulumi.Input[
            ClusterNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgsDict
        ]
    ]

@pulumi.input_type
class ClusterNodePoolUpgradeSettingsBlueGreenSettingsArgs:
    def __init__(
        __self__,
        *,
        autoscaled_rollout_policy: Optional[
            pulumi.Input[
                ClusterNodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicyArgs
            ]
        ] = ...,
        node_pool_soak_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        standard_rollout_policy: Optional[
            pulumi.Input[
                ClusterNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscaledRolloutPolicy")
    def autoscaled_rollout_policy(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterNodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicyArgs
        ]
    ]: ...
    @autoscaled_rollout_policy.setter
    def autoscaled_rollout_policy(
        self,
        value: Optional[
            pulumi.Input[
                ClusterNodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodePoolSoakDuration")
    def node_pool_soak_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_pool_soak_duration.setter
    def node_pool_soak_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="standardRolloutPolicy")
    def standard_rollout_policy(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgs
        ]
    ]: ...
    @standard_rollout_policy.setter
    def standard_rollout_policy(
        self,
        value: Optional[
            pulumi.Input[
                ClusterNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgs
            ]
        ],
    ): ...

class ClusterNodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicyArgsDict(
    TypedDict
):
    wait_for_drain_duration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicyArgs:
    def __init__(
        __self__,
        *,
        wait_for_drain_duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="waitForDrainDuration")
    def wait_for_drain_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait_for_drain_duration.setter
    def wait_for_drain_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgsDict(
    TypedDict
):
    batch_node_count: NotRequired[pulumi.Input[_builtins.int]]
    batch_percentage: NotRequired[pulumi.Input[_builtins.float]]
    batch_soak_duration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgs:
    def __init__(
        __self__,
        *,
        batch_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        batch_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        batch_soak_duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchNodeCount")
    def batch_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @batch_node_count.setter
    def batch_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="batchPercentage")
    def batch_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @batch_percentage.setter
    def batch_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="batchSoakDuration")
    def batch_soak_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @batch_soak_duration.setter
    def batch_soak_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNotificationConfigArgsDict(TypedDict):
    pubsub: pulumi.Input[ClusterNotificationConfigPubsubArgsDict]

@pulumi.input_type
class ClusterNotificationConfigArgs:
    def __init__(
        __self__, *, pubsub: pulumi.Input[ClusterNotificationConfigPubsubArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pubsub(self) -> pulumi.Input[ClusterNotificationConfigPubsubArgs]: ...
    @pubsub.setter
    def pubsub(self, value: pulumi.Input[ClusterNotificationConfigPubsubArgs]): ...

class ClusterNotificationConfigPubsubArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    filter: NotRequired[pulumi.Input[ClusterNotificationConfigPubsubFilterArgsDict]]
    topic: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNotificationConfigPubsubArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        filter: Optional[pulumi.Input[ClusterNotificationConfigPubsubFilterArgs]] = ...,
        topic: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def filter(
        self,
    ) -> Optional[pulumi.Input[ClusterNotificationConfigPubsubFilterArgs]]: ...
    @filter.setter
    def filter(
        self, value: Optional[pulumi.Input[ClusterNotificationConfigPubsubFilterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNotificationConfigPubsubFilterArgsDict(TypedDict):
    event_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ClusterNotificationConfigPubsubFilterArgs:
    def __init__(
        __self__, *, event_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventTypes")
    def event_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @event_types.setter
    def event_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class ClusterPodAutoscalingArgsDict(TypedDict):
    hpa_profile: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterPodAutoscalingArgs:
    def __init__(__self__, *, hpa_profile: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hpaProfile")
    def hpa_profile(self) -> pulumi.Input[_builtins.str]: ...
    @hpa_profile.setter
    def hpa_profile(self, value: pulumi.Input[_builtins.str]): ...

class ClusterPodSecurityPolicyConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterPodSecurityPolicyConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterPrivateClusterConfigArgsDict(TypedDict):
    enable_private_endpoint: NotRequired[pulumi.Input[_builtins.bool]]
    enable_private_nodes: NotRequired[pulumi.Input[_builtins.bool]]
    master_global_access_config: NotRequired[
        pulumi.Input[ClusterPrivateClusterConfigMasterGlobalAccessConfigArgsDict]
    ]
    master_ipv4_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    peering_name: NotRequired[pulumi.Input[_builtins.str]]
    private_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    private_endpoint_subnetwork: NotRequired[pulumi.Input[_builtins.str]]
    public_endpoint: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterPrivateClusterConfigArgs:
    def __init__(
        __self__,
        *,
        enable_private_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_private_nodes: Optional[pulumi.Input[_builtins.bool]] = ...,
        master_global_access_config: Optional[
            pulumi.Input[ClusterPrivateClusterConfigMasterGlobalAccessConfigArgs]
        ] = ...,
        master_ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        peering_name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        private_endpoint_subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
        public_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateEndpoint")
    def enable_private_endpoint(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_private_endpoint.setter
    def enable_private_endpoint(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateNodes")
    def enable_private_nodes(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_private_nodes.setter
    def enable_private_nodes(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="masterGlobalAccessConfig")
    def master_global_access_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterPrivateClusterConfigMasterGlobalAccessConfigArgs]
    ]: ...
    @master_global_access_config.setter
    def master_global_access_config(
        self,
        value: Optional[
            pulumi.Input[ClusterPrivateClusterConfigMasterGlobalAccessConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterIpv4CidrBlock")
    def master_ipv4_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_ipv4_cidr_block.setter
    def master_ipv4_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="peeringName")
    def peering_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peering_name.setter
    def peering_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointSubnetwork")
    def private_endpoint_subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_endpoint_subnetwork.setter
    def private_endpoint_subnetwork(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicEndpoint")
    def public_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_endpoint.setter
    def public_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterPrivateClusterConfigMasterGlobalAccessConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterPrivateClusterConfigMasterGlobalAccessConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterProtectConfigArgsDict(TypedDict):
    workload_config: NotRequired[
        pulumi.Input[ClusterProtectConfigWorkloadConfigArgsDict]
    ]
    workload_vulnerability_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterProtectConfigArgs:
    def __init__(
        __self__,
        *,
        workload_config: Optional[
            pulumi.Input[ClusterProtectConfigWorkloadConfigArgs]
        ] = ...,
        workload_vulnerability_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workloadConfig")
    def workload_config(
        self,
    ) -> Optional[pulumi.Input[ClusterProtectConfigWorkloadConfigArgs]]: ...
    @workload_config.setter
    def workload_config(
        self, value: Optional[pulumi.Input[ClusterProtectConfigWorkloadConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workloadVulnerabilityMode")
    def workload_vulnerability_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workload_vulnerability_mode.setter
    def workload_vulnerability_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterProtectConfigWorkloadConfigArgsDict(TypedDict):
    audit_mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterProtectConfigWorkloadConfigArgs:
    def __init__(__self__, *, audit_mode: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditMode")
    def audit_mode(self) -> pulumi.Input[_builtins.str]: ...
    @audit_mode.setter
    def audit_mode(self, value: pulumi.Input[_builtins.str]): ...

class ClusterRbacBindingConfigArgsDict(TypedDict):
    enable_insecure_binding_system_authenticated: NotRequired[
        pulumi.Input[_builtins.bool]
    ]
    enable_insecure_binding_system_unauthenticated: NotRequired[
        pulumi.Input[_builtins.bool]
    ]

@pulumi.input_type
class ClusterRbacBindingConfigArgs:
    def __init__(
        __self__,
        *,
        enable_insecure_binding_system_authenticated: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        enable_insecure_binding_system_unauthenticated: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableInsecureBindingSystemAuthenticated")
    def enable_insecure_binding_system_authenticated(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_insecure_binding_system_authenticated.setter
    def enable_insecure_binding_system_authenticated(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableInsecureBindingSystemUnauthenticated")
    def enable_insecure_binding_system_unauthenticated(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_insecure_binding_system_unauthenticated.setter
    def enable_insecure_binding_system_unauthenticated(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ClusterReleaseChannelArgsDict(TypedDict):
    channel: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterReleaseChannelArgs:
    def __init__(__self__, *, channel: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> pulumi.Input[_builtins.str]: ...
    @channel.setter
    def channel(self, value: pulumi.Input[_builtins.str]): ...

class ClusterResourceUsageExportConfigArgsDict(TypedDict):
    bigquery_destination: pulumi.Input[
        ClusterResourceUsageExportConfigBigqueryDestinationArgsDict
    ]
    enable_network_egress_metering: NotRequired[pulumi.Input[_builtins.bool]]
    enable_resource_consumption_metering: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterResourceUsageExportConfigArgs:
    def __init__(
        __self__,
        *,
        bigquery_destination: pulumi.Input[
            ClusterResourceUsageExportConfigBigqueryDestinationArgs
        ],
        enable_network_egress_metering: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_resource_consumption_metering: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryDestination")
    def bigquery_destination(
        self,
    ) -> pulumi.Input[ClusterResourceUsageExportConfigBigqueryDestinationArgs]: ...
    @bigquery_destination.setter
    def bigquery_destination(
        self,
        value: pulumi.Input[ClusterResourceUsageExportConfigBigqueryDestinationArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableNetworkEgressMetering")
    def enable_network_egress_metering(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_network_egress_metering.setter
    def enable_network_egress_metering(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableResourceConsumptionMetering")
    def enable_resource_consumption_metering(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_resource_consumption_metering.setter
    def enable_resource_consumption_metering(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ClusterResourceUsageExportConfigBigqueryDestinationArgsDict(TypedDict):
    dataset_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterResourceUsageExportConfigBigqueryDestinationArgs:
    def __init__(__self__, *, dataset_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...

class ClusterSecretManagerConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    rotation_config: NotRequired[
        pulumi.Input[ClusterSecretManagerConfigRotationConfigArgsDict]
    ]

@pulumi.input_type
class ClusterSecretManagerConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        rotation_config: Optional[
            pulumi.Input[ClusterSecretManagerConfigRotationConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="rotationConfig")
    def rotation_config(
        self,
    ) -> Optional[pulumi.Input[ClusterSecretManagerConfigRotationConfigArgs]]: ...
    @rotation_config.setter
    def rotation_config(
        self,
        value: Optional[pulumi.Input[ClusterSecretManagerConfigRotationConfigArgs]],
    ): ...

class ClusterSecretManagerConfigRotationConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    rotation_interval: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterSecretManagerConfigRotationConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        rotation_interval: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="rotationInterval")
    def rotation_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rotation_interval.setter
    def rotation_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterSecretSyncConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    rotation_config: NotRequired[
        pulumi.Input[ClusterSecretSyncConfigRotationConfigArgsDict]
    ]

@pulumi.input_type
class ClusterSecretSyncConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        rotation_config: Optional[
            pulumi.Input[ClusterSecretSyncConfigRotationConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="rotationConfig")
    def rotation_config(
        self,
    ) -> Optional[pulumi.Input[ClusterSecretSyncConfigRotationConfigArgs]]: ...
    @rotation_config.setter
    def rotation_config(
        self, value: Optional[pulumi.Input[ClusterSecretSyncConfigRotationConfigArgs]]
    ): ...

class ClusterSecretSyncConfigRotationConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    rotation_interval: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterSecretSyncConfigRotationConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        rotation_interval: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="rotationInterval")
    def rotation_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rotation_interval.setter
    def rotation_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterSecurityPostureConfigArgsDict(TypedDict):
    mode: NotRequired[pulumi.Input[_builtins.str]]
    vulnerability_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterSecurityPostureConfigArgs:
    def __init__(
        __self__,
        *,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        vulnerability_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vulnerabilityMode")
    def vulnerability_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vulnerability_mode.setter
    def vulnerability_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterServiceExternalIpsConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterServiceExternalIpsConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterTpuConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    ipv4_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    use_service_networking: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterTpuConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        use_service_networking: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="ipv4CidrBlock")
    def ipv4_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv4_cidr_block.setter
    def ipv4_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useServiceNetworking")
    def use_service_networking(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_service_networking.setter
    def use_service_networking(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClusterUserManagedKeysConfigArgsDict(TypedDict):
    aggregation_ca: NotRequired[pulumi.Input[_builtins.str]]
    cluster_ca: NotRequired[pulumi.Input[_builtins.str]]
    control_plane_disk_encryption_key: NotRequired[pulumi.Input[_builtins.str]]
    control_plane_disk_encryption_key_versions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    etcd_api_ca: NotRequired[pulumi.Input[_builtins.str]]
    etcd_peer_ca: NotRequired[pulumi.Input[_builtins.str]]
    gkeops_etcd_backup_encryption_key: NotRequired[pulumi.Input[_builtins.str]]
    service_account_signing_keys: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    service_account_verification_keys: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ClusterUserManagedKeysConfigArgs:
    def __init__(
        __self__,
        *,
        aggregation_ca: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_ca: Optional[pulumi.Input[_builtins.str]] = ...,
        control_plane_disk_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        control_plane_disk_encryption_key_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        etcd_api_ca: Optional[pulumi.Input[_builtins.str]] = ...,
        etcd_peer_ca: Optional[pulumi.Input[_builtins.str]] = ...,
        gkeops_etcd_backup_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_signing_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        service_account_verification_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aggregationCa")
    def aggregation_ca(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aggregation_ca.setter
    def aggregation_ca(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterCa")
    def cluster_ca(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_ca.setter
    def cluster_ca(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneDiskEncryptionKey")
    def control_plane_disk_encryption_key(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @control_plane_disk_encryption_key.setter
    def control_plane_disk_encryption_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneDiskEncryptionKeyVersions")
    def control_plane_disk_encryption_key_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @control_plane_disk_encryption_key_versions.setter
    def control_plane_disk_encryption_key_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="etcdApiCa")
    def etcd_api_ca(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etcd_api_ca.setter
    def etcd_api_ca(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="etcdPeerCa")
    def etcd_peer_ca(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etcd_peer_ca.setter
    def etcd_peer_ca(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gkeopsEtcdBackupEncryptionKey")
    def gkeops_etcd_backup_encryption_key(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gkeops_etcd_backup_encryption_key.setter
    def gkeops_etcd_backup_encryption_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountSigningKeys")
    def service_account_signing_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @service_account_signing_keys.setter
    def service_account_signing_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountVerificationKeys")
    def service_account_verification_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @service_account_verification_keys.setter
    def service_account_verification_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterVerticalPodAutoscalingArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterVerticalPodAutoscalingArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterWorkloadAltsConfigArgsDict(TypedDict):
    enable_alts: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterWorkloadAltsConfigArgs:
    def __init__(__self__, *, enable_alts: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableAlts")
    def enable_alts(self) -> pulumi.Input[_builtins.bool]: ...
    @enable_alts.setter
    def enable_alts(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterWorkloadIdentityConfigArgsDict(TypedDict):
    workload_pool: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterWorkloadIdentityConfigArgs:
    def __init__(
        __self__, *, workload_pool: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workloadPool")
    def workload_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workload_pool.setter
    def workload_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolAutoscalingArgsDict(TypedDict):
    location_policy: NotRequired[pulumi.Input[_builtins.str]]
    max_node_count: NotRequired[pulumi.Input[_builtins.int]]
    min_node_count: NotRequired[pulumi.Input[_builtins.int]]
    total_max_node_count: NotRequired[pulumi.Input[_builtins.int]]
    total_min_node_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class NodePoolAutoscalingArgs:
    def __init__(
        __self__,
        *,
        location_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        max_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        total_max_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        total_min_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationPolicy")
    def location_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location_policy.setter
    def location_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @_builtins.property
    @pulumi.getter(name="totalMaxNodeCount")
    def total_max_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @total_max_node_count.setter
    def total_max_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="totalMinNodeCount")
    def total_min_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @total_min_node_count.setter
    def total_min_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class NodePoolManagementArgsDict(TypedDict):
    auto_repair: NotRequired[pulumi.Input[_builtins.bool]]
    auto_upgrade: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class NodePoolManagementArgs:
    def __init__(
        __self__,
        *,
        auto_repair: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRepair")
    def auto_repair(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_repair.setter
    def auto_repair(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="autoUpgrade")
    def auto_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_upgrade.setter
    def auto_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class NodePoolNetworkConfigArgsDict(TypedDict):
    accelerator_network_profile: NotRequired[pulumi.Input[_builtins.str]]
    additional_node_network_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[NodePoolNetworkConfigAdditionalNodeNetworkConfigArgsDict]
            ]
        ]
    ]
    additional_pod_network_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[NodePoolNetworkConfigAdditionalPodNetworkConfigArgsDict]
            ]
        ]
    ]
    create_pod_range: NotRequired[pulumi.Input[_builtins.bool]]
    enable_private_nodes: NotRequired[pulumi.Input[_builtins.bool]]
    network_performance_config: NotRequired[
        pulumi.Input[NodePoolNetworkConfigNetworkPerformanceConfigArgsDict]
    ]
    pod_cidr_overprovision_config: NotRequired[
        pulumi.Input[NodePoolNetworkConfigPodCidrOverprovisionConfigArgsDict]
    ]
    pod_ipv4_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    pod_range: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        accelerator_network_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        additional_node_network_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[NodePoolNetworkConfigAdditionalNodeNetworkConfigArgs]
                ]
            ]
        ] = ...,
        additional_pod_network_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[NodePoolNetworkConfigAdditionalPodNetworkConfigArgs]
                ]
            ]
        ] = ...,
        create_pod_range: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_private_nodes: Optional[pulumi.Input[_builtins.bool]] = ...,
        network_performance_config: Optional[
            pulumi.Input[NodePoolNetworkConfigNetworkPerformanceConfigArgs]
        ] = ...,
        pod_cidr_overprovision_config: Optional[
            pulumi.Input[NodePoolNetworkConfigPodCidrOverprovisionConfigArgs]
        ] = ...,
        pod_ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        pod_range: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorNetworkProfile")
    def accelerator_network_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accelerator_network_profile.setter
    def accelerator_network_profile(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalNodeNetworkConfigs")
    def additional_node_network_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[NodePoolNetworkConfigAdditionalNodeNetworkConfigArgs]]
        ]
    ]: ...
    @additional_node_network_configs.setter
    def additional_node_network_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[NodePoolNetworkConfigAdditionalNodeNetworkConfigArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalPodNetworkConfigs")
    def additional_pod_network_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[NodePoolNetworkConfigAdditionalPodNetworkConfigArgs]]
        ]
    ]: ...
    @additional_pod_network_configs.setter
    def additional_pod_network_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[NodePoolNetworkConfigAdditionalPodNetworkConfigArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createPodRange")
    def create_pod_range(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_pod_range.setter
    def create_pod_range(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateNodes")
    def enable_private_nodes(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_private_nodes.setter
    def enable_private_nodes(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfig")
    def network_performance_config(
        self,
    ) -> Optional[pulumi.Input[NodePoolNetworkConfigNetworkPerformanceConfigArgs]]: ...
    @network_performance_config.setter
    def network_performance_config(
        self,
        value: Optional[
            pulumi.Input[NodePoolNetworkConfigNetworkPerformanceConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="podCidrOverprovisionConfig")
    def pod_cidr_overprovision_config(
        self,
    ) -> Optional[
        pulumi.Input[NodePoolNetworkConfigPodCidrOverprovisionConfigArgs]
    ]: ...
    @pod_cidr_overprovision_config.setter
    def pod_cidr_overprovision_config(
        self,
        value: Optional[
            pulumi.Input[NodePoolNetworkConfigPodCidrOverprovisionConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="podIpv4CidrBlock")
    def pod_ipv4_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pod_ipv4_cidr_block.setter
    def pod_ipv4_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="podRange")
    def pod_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pod_range.setter
    def pod_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolNetworkConfigAdditionalNodeNetworkConfigArgsDict(TypedDict):
    network: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNetworkConfigAdditionalNodeNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolNetworkConfigAdditionalPodNetworkConfigArgsDict(TypedDict):
    max_pods_per_node: NotRequired[pulumi.Input[_builtins.int]]
    secondary_pod_range: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNetworkConfigAdditionalPodNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ...,
        secondary_pod_range: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_pods_per_node.setter
    def max_pods_per_node(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryPodRange")
    def secondary_pod_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secondary_pod_range.setter
    def secondary_pod_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolNetworkConfigNetworkPerformanceConfigArgsDict(TypedDict):
    total_egress_bandwidth_tier: pulumi.Input[_builtins.str]

@pulumi.input_type
class NodePoolNetworkConfigNetworkPerformanceConfigArgs:
    def __init__(
        __self__, *, total_egress_bandwidth_tier: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="totalEgressBandwidthTier")
    def total_egress_bandwidth_tier(self) -> pulumi.Input[_builtins.str]: ...
    @total_egress_bandwidth_tier.setter
    def total_egress_bandwidth_tier(self, value: pulumi.Input[_builtins.str]): ...

class NodePoolNetworkConfigPodCidrOverprovisionConfigArgsDict(TypedDict):
    disabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class NodePoolNetworkConfigPodCidrOverprovisionConfigArgs:
    def __init__(__self__, *, disabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Input[_builtins.bool]: ...
    @disabled.setter
    def disabled(self, value: pulumi.Input[_builtins.bool]): ...

class NodePoolNodeConfigArgsDict(TypedDict):
    advanced_machine_features: NotRequired[
        pulumi.Input[NodePoolNodeConfigAdvancedMachineFeaturesArgsDict]
    ]
    boot_disk: NotRequired[pulumi.Input[NodePoolNodeConfigBootDiskArgsDict]]
    boot_disk_kms_key: NotRequired[pulumi.Input[_builtins.str]]
    confidential_nodes: NotRequired[
        pulumi.Input[NodePoolNodeConfigConfidentialNodesArgsDict]
    ]
    containerd_config: NotRequired[
        pulumi.Input[NodePoolNodeConfigContainerdConfigArgsDict]
    ]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    disk_type: NotRequired[pulumi.Input[_builtins.str]]
    effective_taints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NodePoolNodeConfigEffectiveTaintArgsDict]]]
    ]
    enable_confidential_storage: NotRequired[pulumi.Input[_builtins.bool]]
    ephemeral_storage_config: NotRequired[
        pulumi.Input[NodePoolNodeConfigEphemeralStorageConfigArgsDict]
    ]
    ephemeral_storage_local_ssd_config: NotRequired[
        pulumi.Input[NodePoolNodeConfigEphemeralStorageLocalSsdConfigArgsDict]
    ]
    fast_socket: NotRequired[pulumi.Input[NodePoolNodeConfigFastSocketArgsDict]]
    flex_start: NotRequired[pulumi.Input[_builtins.bool]]
    gcfs_config: NotRequired[pulumi.Input[NodePoolNodeConfigGcfsConfigArgsDict]]
    guest_accelerators: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NodePoolNodeConfigGuestAcceleratorArgsDict]]]
    ]
    gvnic: NotRequired[pulumi.Input[NodePoolNodeConfigGvnicArgsDict]]
    host_maintenance_policy: NotRequired[
        pulumi.Input[NodePoolNodeConfigHostMaintenancePolicyArgsDict]
    ]
    image_type: NotRequired[pulumi.Input[_builtins.str]]
    kubelet_config: NotRequired[pulumi.Input[NodePoolNodeConfigKubeletConfigArgsDict]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    linux_node_config: NotRequired[
        pulumi.Input[NodePoolNodeConfigLinuxNodeConfigArgsDict]
    ]
    local_nvme_ssd_block_config: NotRequired[
        pulumi.Input[NodePoolNodeConfigLocalNvmeSsdBlockConfigArgsDict]
    ]
    local_ssd_count: NotRequired[pulumi.Input[_builtins.int]]
    local_ssd_encryption_mode: NotRequired[pulumi.Input[_builtins.str]]
    logging_variant: NotRequired[pulumi.Input[_builtins.str]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    max_run_duration: NotRequired[pulumi.Input[_builtins.str]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    min_cpu_platform: NotRequired[pulumi.Input[_builtins.str]]
    node_group: NotRequired[pulumi.Input[_builtins.str]]
    oauth_scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    preemptible: NotRequired[pulumi.Input[_builtins.bool]]
    reservation_affinity: NotRequired[
        pulumi.Input[NodePoolNodeConfigReservationAffinityArgsDict]
    ]
    resource_labels: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    resource_manager_tags: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    sandbox_config: NotRequired[pulumi.Input[NodePoolNodeConfigSandboxConfigArgsDict]]
    secondary_boot_disks: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[NodePoolNodeConfigSecondaryBootDiskArgsDict]]
        ]
    ]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    shielded_instance_config: NotRequired[
        pulumi.Input[NodePoolNodeConfigShieldedInstanceConfigArgsDict]
    ]
    sole_tenant_config: NotRequired[
        pulumi.Input[NodePoolNodeConfigSoleTenantConfigArgsDict]
    ]
    spot: NotRequired[pulumi.Input[_builtins.bool]]
    storage_pools: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    taints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NodePoolNodeConfigTaintArgsDict]]]
    ]
    windows_node_config: NotRequired[
        pulumi.Input[NodePoolNodeConfigWindowsNodeConfigArgsDict]
    ]
    workload_metadata_config: NotRequired[
        pulumi.Input[NodePoolNodeConfigWorkloadMetadataConfigArgsDict]
    ]

@pulumi.input_type
class NodePoolNodeConfigArgs:
    def __init__(
        __self__,
        *,
        advanced_machine_features: Optional[
            pulumi.Input[NodePoolNodeConfigAdvancedMachineFeaturesArgs]
        ] = ...,
        boot_disk: Optional[pulumi.Input[NodePoolNodeConfigBootDiskArgs]] = ...,
        boot_disk_kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        confidential_nodes: Optional[
            pulumi.Input[NodePoolNodeConfigConfidentialNodesArgs]
        ] = ...,
        containerd_config: Optional[
            pulumi.Input[NodePoolNodeConfigContainerdConfigArgs]
        ] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_taints: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodePoolNodeConfigEffectiveTaintArgs]]]
        ] = ...,
        enable_confidential_storage: Optional[pulumi.Input[_builtins.bool]] = ...,
        ephemeral_storage_config: Optional[
            pulumi.Input[NodePoolNodeConfigEphemeralStorageConfigArgs]
        ] = ...,
        ephemeral_storage_local_ssd_config: Optional[
            pulumi.Input[NodePoolNodeConfigEphemeralStorageLocalSsdConfigArgs]
        ] = ...,
        fast_socket: Optional[pulumi.Input[NodePoolNodeConfigFastSocketArgs]] = ...,
        flex_start: Optional[pulumi.Input[_builtins.bool]] = ...,
        gcfs_config: Optional[pulumi.Input[NodePoolNodeConfigGcfsConfigArgs]] = ...,
        guest_accelerators: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodePoolNodeConfigGuestAcceleratorArgs]]]
        ] = ...,
        gvnic: Optional[pulumi.Input[NodePoolNodeConfigGvnicArgs]] = ...,
        host_maintenance_policy: Optional[
            pulumi.Input[NodePoolNodeConfigHostMaintenancePolicyArgs]
        ] = ...,
        image_type: Optional[pulumi.Input[_builtins.str]] = ...,
        kubelet_config: Optional[
            pulumi.Input[NodePoolNodeConfigKubeletConfigArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        linux_node_config: Optional[
            pulumi.Input[NodePoolNodeConfigLinuxNodeConfigArgs]
        ] = ...,
        local_nvme_ssd_block_config: Optional[
            pulumi.Input[NodePoolNodeConfigLocalNvmeSsdBlockConfigArgs]
        ] = ...,
        local_ssd_count: Optional[pulumi.Input[_builtins.int]] = ...,
        local_ssd_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_variant: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        max_run_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        node_group: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        preemptible: Optional[pulumi.Input[_builtins.bool]] = ...,
        reservation_affinity: Optional[
            pulumi.Input[NodePoolNodeConfigReservationAffinityArgs]
        ] = ...,
        resource_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_manager_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        sandbox_config: Optional[
            pulumi.Input[NodePoolNodeConfigSandboxConfigArgs]
        ] = ...,
        secondary_boot_disks: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[NodePoolNodeConfigSecondaryBootDiskArgs]]
            ]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[NodePoolNodeConfigShieldedInstanceConfigArgs]
        ] = ...,
        sole_tenant_config: Optional[
            pulumi.Input[NodePoolNodeConfigSoleTenantConfigArgs]
        ] = ...,
        spot: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_pools: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        taints: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodePoolNodeConfigTaintArgs]]]
        ] = ...,
        windows_node_config: Optional[
            pulumi.Input[NodePoolNodeConfigWindowsNodeConfigArgs]
        ] = ...,
        workload_metadata_config: Optional[
            pulumi.Input[NodePoolNodeConfigWorkloadMetadataConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigAdvancedMachineFeaturesArgs]]: ...
    @advanced_machine_features.setter
    def advanced_machine_features(
        self,
        value: Optional[pulumi.Input[NodePoolNodeConfigAdvancedMachineFeaturesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bootDisk")
    def boot_disk(self) -> Optional[pulumi.Input[NodePoolNodeConfigBootDiskArgs]]: ...
    @boot_disk.setter
    def boot_disk(
        self, value: Optional[pulumi.Input[NodePoolNodeConfigBootDiskArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bootDiskKmsKey")
    def boot_disk_kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @boot_disk_kms_key.setter
    def boot_disk_kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="confidentialNodes")
    def confidential_nodes(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigConfidentialNodesArgs]]: ...
    @confidential_nodes.setter
    def confidential_nodes(
        self, value: Optional[pulumi.Input[NodePoolNodeConfigConfidentialNodesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerdConfig")
    def containerd_config(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigContainerdConfigArgs]]: ...
    @containerd_config.setter
    def containerd_config(
        self, value: Optional[pulumi.Input[NodePoolNodeConfigContainerdConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveTaints")
    def effective_taints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NodePoolNodeConfigEffectiveTaintArgs]]]
    ]: ...
    @effective_taints.setter
    def effective_taints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodePoolNodeConfigEffectiveTaintArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableConfidentialStorage")
    def enable_confidential_storage(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_confidential_storage.setter
    def enable_confidential_storage(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageConfig")
    def ephemeral_storage_config(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigEphemeralStorageConfigArgs]]: ...
    @ephemeral_storage_config.setter
    def ephemeral_storage_config(
        self,
        value: Optional[pulumi.Input[NodePoolNodeConfigEphemeralStorageConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorageLocalSsdConfig")
    def ephemeral_storage_local_ssd_config(
        self,
    ) -> Optional[
        pulumi.Input[NodePoolNodeConfigEphemeralStorageLocalSsdConfigArgs]
    ]: ...
    @ephemeral_storage_local_ssd_config.setter
    def ephemeral_storage_local_ssd_config(
        self,
        value: Optional[
            pulumi.Input[NodePoolNodeConfigEphemeralStorageLocalSsdConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fastSocket")
    def fast_socket(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigFastSocketArgs]]: ...
    @fast_socket.setter
    def fast_socket(
        self, value: Optional[pulumi.Input[NodePoolNodeConfigFastSocketArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="flexStart")
    def flex_start(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @flex_start.setter
    def flex_start(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="gcfsConfig")
    def gcfs_config(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigGcfsConfigArgs]]: ...
    @gcfs_config.setter
    def gcfs_config(
        self, value: Optional[pulumi.Input[NodePoolNodeConfigGcfsConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NodePoolNodeConfigGuestAcceleratorArgs]]]
    ]: ...
    @guest_accelerators.setter
    def guest_accelerators(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodePoolNodeConfigGuestAcceleratorArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def gvnic(self) -> Optional[pulumi.Input[NodePoolNodeConfigGvnicArgs]]: ...
    @gvnic.setter
    def gvnic(self, value: Optional[pulumi.Input[NodePoolNodeConfigGvnicArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="hostMaintenancePolicy")
    def host_maintenance_policy(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigHostMaintenancePolicyArgs]]: ...
    @host_maintenance_policy.setter
    def host_maintenance_policy(
        self, value: Optional[pulumi.Input[NodePoolNodeConfigHostMaintenancePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_type.setter
    def image_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigKubeletConfigArgs]]: ...
    @kubelet_config.setter
    def kubelet_config(
        self, value: Optional[pulumi.Input[NodePoolNodeConfigKubeletConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linuxNodeConfig")
    def linux_node_config(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigLinuxNodeConfigArgs]]: ...
    @linux_node_config.setter
    def linux_node_config(
        self, value: Optional[pulumi.Input[NodePoolNodeConfigLinuxNodeConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="localNvmeSsdBlockConfig")
    def local_nvme_ssd_block_config(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigLocalNvmeSsdBlockConfigArgs]]: ...
    @local_nvme_ssd_block_config.setter
    def local_nvme_ssd_block_config(
        self,
        value: Optional[pulumi.Input[NodePoolNodeConfigLocalNvmeSsdBlockConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @local_ssd_count.setter
    def local_ssd_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="localSsdEncryptionMode")
    def local_ssd_encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_ssd_encryption_mode.setter
    def local_ssd_encryption_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingVariant")
    def logging_variant(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logging_variant.setter
    def logging_variant(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRunDuration")
    def max_run_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_run_duration.setter
    def max_run_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeGroup")
    def node_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_group.setter
    def node_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @oauth_scopes.setter
    def oauth_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def preemptible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preemptible.setter
    def preemptible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigReservationAffinityArgs]]: ...
    @reservation_affinity.setter
    def reservation_affinity(
        self, value: Optional[pulumi.Input[NodePoolNodeConfigReservationAffinityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceLabels")
    def resource_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @resource_labels.setter
    def resource_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @resource_manager_tags.setter
    def resource_manager_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sandboxConfig")
    def sandbox_config(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigSandboxConfigArgs]]: ...
    @sandbox_config.setter
    def sandbox_config(
        self, value: Optional[pulumi.Input[NodePoolNodeConfigSandboxConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secondaryBootDisks")
    def secondary_boot_disks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NodePoolNodeConfigSecondaryBootDiskArgs]]]
    ]: ...
    @secondary_boot_disks.setter
    def secondary_boot_disks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[NodePoolNodeConfigSecondaryBootDiskArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigShieldedInstanceConfigArgs]]: ...
    @shielded_instance_config.setter
    def shielded_instance_config(
        self,
        value: Optional[pulumi.Input[NodePoolNodeConfigShieldedInstanceConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="soleTenantConfig")
    def sole_tenant_config(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigSoleTenantConfigArgs]]: ...
    @sole_tenant_config.setter
    def sole_tenant_config(
        self, value: Optional[pulumi.Input[NodePoolNodeConfigSoleTenantConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def spot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @spot.setter
    def spot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="storagePools")
    def storage_pools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @storage_pools.setter
    def storage_pools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def taints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NodePoolNodeConfigTaintArgs]]]
    ]: ...
    @taints.setter
    def taints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodePoolNodeConfigTaintArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="windowsNodeConfig")
    def windows_node_config(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigWindowsNodeConfigArgs]]: ...
    @windows_node_config.setter
    def windows_node_config(
        self, value: Optional[pulumi.Input[NodePoolNodeConfigWindowsNodeConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workloadMetadataConfig")
    def workload_metadata_config(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigWorkloadMetadataConfigArgs]]: ...
    @workload_metadata_config.setter
    def workload_metadata_config(
        self,
        value: Optional[pulumi.Input[NodePoolNodeConfigWorkloadMetadataConfigArgs]],
    ): ...

class NodePoolNodeConfigAdvancedMachineFeaturesArgsDict(TypedDict):
    threads_per_core: pulumi.Input[_builtins.int]
    enable_nested_virtualization: NotRequired[pulumi.Input[_builtins.bool]]
    performance_monitoring_unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigAdvancedMachineFeaturesArgs:
    def __init__(
        __self__,
        *,
        threads_per_core: pulumi.Input[_builtins.int],
        enable_nested_virtualization: Optional[pulumi.Input[_builtins.bool]] = ...,
        performance_monitoring_unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> pulumi.Input[_builtins.int]: ...
    @threads_per_core.setter
    def threads_per_core(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_nested_virtualization.setter
    def enable_nested_virtualization(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceMonitoringUnit")
    def performance_monitoring_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @performance_monitoring_unit.setter
    def performance_monitoring_unit(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class NodePoolNodeConfigBootDiskArgsDict(TypedDict):
    disk_type: NotRequired[pulumi.Input[_builtins.str]]
    provisioned_iops: NotRequired[pulumi.Input[_builtins.int]]
    provisioned_throughput: NotRequired[pulumi.Input[_builtins.int]]
    size_gb: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class NodePoolNodeConfigBootDiskArgs:
    def __init__(
        __self__,
        *,
        disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_iops: Optional[pulumi.Input[_builtins.int]] = ...,
        provisioned_throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_iops.setter
    def provisioned_iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_throughput.setter
    def provisioned_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size_gb.setter
    def size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class NodePoolNodeConfigConfidentialNodesArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    confidential_instance_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigConfidentialNodesArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        confidential_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceType")
    def confidential_instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @confidential_instance_type.setter
    def confidential_instance_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class NodePoolNodeConfigContainerdConfigArgsDict(TypedDict):
    private_registry_access_config: NotRequired[
        pulumi.Input[
            NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigArgsDict
        ]
    ]
    registry_hosts: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[NodePoolNodeConfigContainerdConfigRegistryHostArgsDict]
            ]
        ]
    ]
    writable_cgroups: NotRequired[
        pulumi.Input[NodePoolNodeConfigContainerdConfigWritableCgroupsArgsDict]
    ]

@pulumi.input_type
class NodePoolNodeConfigContainerdConfigArgs:
    def __init__(
        __self__,
        *,
        private_registry_access_config: Optional[
            pulumi.Input[
                NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigArgs
            ]
        ] = ...,
        registry_hosts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[NodePoolNodeConfigContainerdConfigRegistryHostArgs]
                ]
            ]
        ] = ...,
        writable_cgroups: Optional[
            pulumi.Input[NodePoolNodeConfigContainerdConfigWritableCgroupsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateRegistryAccessConfig")
    def private_registry_access_config(
        self,
    ) -> Optional[
        pulumi.Input[NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigArgs]
    ]: ...
    @private_registry_access_config.setter
    def private_registry_access_config(
        self,
        value: Optional[
            pulumi.Input[
                NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="registryHosts")
    def registry_hosts(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[NodePoolNodeConfigContainerdConfigRegistryHostArgs]]
        ]
    ]: ...
    @registry_hosts.setter
    def registry_hosts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[NodePoolNodeConfigContainerdConfigRegistryHostArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="writableCgroups")
    def writable_cgroups(
        self,
    ) -> Optional[
        pulumi.Input[NodePoolNodeConfigContainerdConfigWritableCgroupsArgs]
    ]: ...
    @writable_cgroups.setter
    def writable_cgroups(
        self,
        value: Optional[
            pulumi.Input[NodePoolNodeConfigContainerdConfigWritableCgroupsArgs]
        ],
    ): ...

class NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    certificate_authority_domain_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        certificate_authority_domain_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityDomainConfigs")
    def certificate_authority_domain_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs
                ]
            ]
        ]
    ]: ...
    @certificate_authority_domain_configs.setter
    def certificate_authority_domain_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgsDict(
    TypedDict
):
    fqdns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    gcp_secret_manager_certificate_config: pulumi.Input[
        NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgsDict
    ]

@pulumi.input_type
class NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigArgs:
    def __init__(
        __self__,
        *,
        fqdns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        gcp_secret_manager_certificate_config: pulumi.Input[
            NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fqdns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @fqdns.setter
    def fqdns(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerCertificateConfig")
    def gcp_secret_manager_certificate_config(
        self,
    ) -> pulumi.Input[
        NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs
    ]: ...
    @gcp_secret_manager_certificate_config.setter
    def gcp_secret_manager_certificate_config(
        self,
        value: pulumi.Input[
            NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs
        ],
    ): ...

class NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgsDict(
    TypedDict
):
    secret_uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class NodePoolNodeConfigContainerdConfigPrivateRegistryAccessConfigCertificateAuthorityDomainConfigGcpSecretManagerCertificateConfigArgs:
    def __init__(__self__, *, secret_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretUri")
    def secret_uri(self) -> pulumi.Input[_builtins.str]: ...
    @secret_uri.setter
    def secret_uri(self, value: pulumi.Input[_builtins.str]): ...

class NodePoolNodeConfigContainerdConfigRegistryHostArgsDict(TypedDict):
    server: pulumi.Input[_builtins.str]
    hosts: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[NodePoolNodeConfigContainerdConfigRegistryHostHostArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class NodePoolNodeConfigContainerdConfigRegistryHostArgs:
    def __init__(
        __self__,
        *,
        server: pulumi.Input[_builtins.str],
        hosts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[NodePoolNodeConfigContainerdConfigRegistryHostHostArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> pulumi.Input[_builtins.str]: ...
    @server.setter
    def server(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def hosts(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[NodePoolNodeConfigContainerdConfigRegistryHostHostArgs]
            ]
        ]
    ]: ...
    @hosts.setter
    def hosts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[NodePoolNodeConfigContainerdConfigRegistryHostHostArgs]
                ]
            ]
        ],
    ): ...

class NodePoolNodeConfigContainerdConfigRegistryHostHostArgsDict(TypedDict):
    host: pulumi.Input[_builtins.str]
    capabilities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    cas: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    NodePoolNodeConfigContainerdConfigRegistryHostHostCaArgsDict
                ]
            ]
        ]
    ]
    clients: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    NodePoolNodeConfigContainerdConfigRegistryHostHostClientArgsDict
                ]
            ]
        ]
    ]
    dial_timeout: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    NodePoolNodeConfigContainerdConfigRegistryHostHostHeaderArgsDict
                ]
            ]
        ]
    ]
    override_path: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class NodePoolNodeConfigContainerdConfigRegistryHostHostArgs:
    def __init__(
        __self__,
        *,
        host: pulumi.Input[_builtins.str],
        capabilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        NodePoolNodeConfigContainerdConfigRegistryHostHostCaArgs
                    ]
                ]
            ]
        ] = ...,
        clients: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        NodePoolNodeConfigContainerdConfigRegistryHostHostClientArgs
                    ]
                ]
            ]
        ] = ...,
        dial_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        headers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        NodePoolNodeConfigContainerdConfigRegistryHostHostHeaderArgs
                    ]
                ]
            ]
        ] = ...,
        override_path: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def capabilities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @capabilities.setter
    def capabilities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def cas(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[NodePoolNodeConfigContainerdConfigRegistryHostHostCaArgs]
            ]
        ]
    ]: ...
    @cas.setter
    def cas(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        NodePoolNodeConfigContainerdConfigRegistryHostHostCaArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def clients(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    NodePoolNodeConfigContainerdConfigRegistryHostHostClientArgs
                ]
            ]
        ]
    ]: ...
    @clients.setter
    def clients(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        NodePoolNodeConfigContainerdConfigRegistryHostHostClientArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dialTimeout")
    def dial_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dial_timeout.setter
    def dial_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    NodePoolNodeConfigContainerdConfigRegistryHostHostHeaderArgs
                ]
            ]
        ]
    ]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        NodePoolNodeConfigContainerdConfigRegistryHostHostHeaderArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="overridePath")
    def override_path(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @override_path.setter
    def override_path(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class NodePoolNodeConfigContainerdConfigRegistryHostHostCaArgsDict(TypedDict):
    gcp_secret_manager_secret_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigContainerdConfigRegistryHostHostCaArgs:
    def __init__(
        __self__,
        *,
        gcp_secret_manager_secret_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_secret_manager_secret_uri.setter
    def gcp_secret_manager_secret_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class NodePoolNodeConfigContainerdConfigRegistryHostHostClientArgsDict(TypedDict):
    cert: pulumi.Input[
        NodePoolNodeConfigContainerdConfigRegistryHostHostClientCertArgsDict
    ]
    key: NotRequired[
        pulumi.Input[
            NodePoolNodeConfigContainerdConfigRegistryHostHostClientKeyArgsDict
        ]
    ]

@pulumi.input_type
class NodePoolNodeConfigContainerdConfigRegistryHostHostClientArgs:
    def __init__(
        __self__,
        *,
        cert: pulumi.Input[
            NodePoolNodeConfigContainerdConfigRegistryHostHostClientCertArgs
        ],
        key: Optional[
            pulumi.Input[
                NodePoolNodeConfigContainerdConfigRegistryHostHostClientKeyArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(
        self,
    ) -> pulumi.Input[
        NodePoolNodeConfigContainerdConfigRegistryHostHostClientCertArgs
    ]: ...
    @cert.setter
    def cert(
        self,
        value: pulumi.Input[
            NodePoolNodeConfigContainerdConfigRegistryHostHostClientCertArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(
        self,
    ) -> Optional[
        pulumi.Input[NodePoolNodeConfigContainerdConfigRegistryHostHostClientKeyArgs]
    ]: ...
    @key.setter
    def key(
        self,
        value: Optional[
            pulumi.Input[
                NodePoolNodeConfigContainerdConfigRegistryHostHostClientKeyArgs
            ]
        ],
    ): ...

class NodePoolNodeConfigContainerdConfigRegistryHostHostClientCertArgsDict(TypedDict):
    gcp_secret_manager_secret_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigContainerdConfigRegistryHostHostClientCertArgs:
    def __init__(
        __self__,
        *,
        gcp_secret_manager_secret_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_secret_manager_secret_uri.setter
    def gcp_secret_manager_secret_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class NodePoolNodeConfigContainerdConfigRegistryHostHostClientKeyArgsDict(TypedDict):
    gcp_secret_manager_secret_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigContainerdConfigRegistryHostHostClientKeyArgs:
    def __init__(
        __self__,
        *,
        gcp_secret_manager_secret_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpSecretManagerSecretUri")
    def gcp_secret_manager_secret_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_secret_manager_secret_uri.setter
    def gcp_secret_manager_secret_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class NodePoolNodeConfigContainerdConfigRegistryHostHostHeaderArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class NodePoolNodeConfigContainerdConfigRegistryHostHostHeaderArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class NodePoolNodeConfigContainerdConfigWritableCgroupsArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class NodePoolNodeConfigContainerdConfigWritableCgroupsArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class NodePoolNodeConfigEffectiveTaintArgsDict(TypedDict):
    effect: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigEffectiveTaintArgs:
    def __init__(
        __self__,
        *,
        effect: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effect.setter
    def effect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolNodeConfigEphemeralStorageConfigArgsDict(TypedDict):
    local_ssd_count: pulumi.Input[_builtins.int]

@pulumi.input_type
class NodePoolNodeConfigEphemeralStorageConfigArgs:
    def __init__(__self__, *, local_ssd_count: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> pulumi.Input[_builtins.int]: ...
    @local_ssd_count.setter
    def local_ssd_count(self, value: pulumi.Input[_builtins.int]): ...

class NodePoolNodeConfigEphemeralStorageLocalSsdConfigArgsDict(TypedDict):
    local_ssd_count: pulumi.Input[_builtins.int]
    data_cache_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class NodePoolNodeConfigEphemeralStorageLocalSsdConfigArgs:
    def __init__(
        __self__,
        *,
        local_ssd_count: pulumi.Input[_builtins.int],
        data_cache_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> pulumi.Input[_builtins.int]: ...
    @local_ssd_count.setter
    def local_ssd_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="dataCacheCount")
    def data_cache_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_cache_count.setter
    def data_cache_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class NodePoolNodeConfigFastSocketArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class NodePoolNodeConfigFastSocketArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class NodePoolNodeConfigGcfsConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class NodePoolNodeConfigGcfsConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class NodePoolNodeConfigGuestAcceleratorArgsDict(TypedDict):
    count: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]
    gpu_driver_installation_config: NotRequired[
        pulumi.Input[
            NodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgsDict
        ]
    ]
    gpu_partition_size: NotRequired[pulumi.Input[_builtins.str]]
    gpu_sharing_config: NotRequired[
        pulumi.Input[NodePoolNodeConfigGuestAcceleratorGpuSharingConfigArgsDict]
    ]

@pulumi.input_type
class NodePoolNodeConfigGuestAcceleratorArgs:
    def __init__(
        __self__,
        *,
        count: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.str],
        gpu_driver_installation_config: Optional[
            pulumi.Input[
                NodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgs
            ]
        ] = ...,
        gpu_partition_size: Optional[pulumi.Input[_builtins.str]] = ...,
        gpu_sharing_config: Optional[
            pulumi.Input[NodePoolNodeConfigGuestAcceleratorGpuSharingConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> pulumi.Input[_builtins.int]: ...
    @count.setter
    def count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverInstallationConfig")
    def gpu_driver_installation_config(
        self,
    ) -> Optional[
        pulumi.Input[NodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgs]
    ]: ...
    @gpu_driver_installation_config.setter
    def gpu_driver_installation_config(
        self,
        value: Optional[
            pulumi.Input[
                NodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gpuPartitionSize")
    def gpu_partition_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gpu_partition_size.setter
    def gpu_partition_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingConfig")
    def gpu_sharing_config(
        self,
    ) -> Optional[
        pulumi.Input[NodePoolNodeConfigGuestAcceleratorGpuSharingConfigArgs]
    ]: ...
    @gpu_sharing_config.setter
    def gpu_sharing_config(
        self,
        value: Optional[
            pulumi.Input[NodePoolNodeConfigGuestAcceleratorGpuSharingConfigArgs]
        ],
    ): ...

class NodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgsDict(TypedDict):
    gpu_driver_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class NodePoolNodeConfigGuestAcceleratorGpuDriverInstallationConfigArgs:
    def __init__(
        __self__, *, gpu_driver_version: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuDriverVersion")
    def gpu_driver_version(self) -> pulumi.Input[_builtins.str]: ...
    @gpu_driver_version.setter
    def gpu_driver_version(self, value: pulumi.Input[_builtins.str]): ...

class NodePoolNodeConfigGuestAcceleratorGpuSharingConfigArgsDict(TypedDict):
    gpu_sharing_strategy: pulumi.Input[_builtins.str]
    max_shared_clients_per_gpu: pulumi.Input[_builtins.int]

@pulumi.input_type
class NodePoolNodeConfigGuestAcceleratorGpuSharingConfigArgs:
    def __init__(
        __self__,
        *,
        gpu_sharing_strategy: pulumi.Input[_builtins.str],
        max_shared_clients_per_gpu: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gpuSharingStrategy")
    def gpu_sharing_strategy(self) -> pulumi.Input[_builtins.str]: ...
    @gpu_sharing_strategy.setter
    def gpu_sharing_strategy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maxSharedClientsPerGpu")
    def max_shared_clients_per_gpu(self) -> pulumi.Input[_builtins.int]: ...
    @max_shared_clients_per_gpu.setter
    def max_shared_clients_per_gpu(self, value: pulumi.Input[_builtins.int]): ...

class NodePoolNodeConfigGvnicArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class NodePoolNodeConfigGvnicArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class NodePoolNodeConfigHostMaintenancePolicyArgsDict(TypedDict):
    maintenance_interval: pulumi.Input[_builtins.str]

@pulumi.input_type
class NodePoolNodeConfigHostMaintenancePolicyArgs:
    def __init__(
        __self__, *, maintenance_interval: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceInterval")
    def maintenance_interval(self) -> pulumi.Input[_builtins.str]: ...
    @maintenance_interval.setter
    def maintenance_interval(self, value: pulumi.Input[_builtins.str]): ...

class NodePoolNodeConfigKubeletConfigArgsDict(TypedDict):
    allowed_unsafe_sysctls: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    container_log_max_files: NotRequired[pulumi.Input[_builtins.int]]
    container_log_max_size: NotRequired[pulumi.Input[_builtins.str]]
    cpu_cfs_quota: NotRequired[pulumi.Input[_builtins.bool]]
    cpu_cfs_quota_period: NotRequired[pulumi.Input[_builtins.str]]
    cpu_manager_policy: NotRequired[pulumi.Input[_builtins.str]]
    eviction_max_pod_grace_period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    eviction_minimum_reclaim: NotRequired[
        pulumi.Input[NodePoolNodeConfigKubeletConfigEvictionMinimumReclaimArgsDict]
    ]
    eviction_soft: NotRequired[
        pulumi.Input[NodePoolNodeConfigKubeletConfigEvictionSoftArgsDict]
    ]
    eviction_soft_grace_period: NotRequired[
        pulumi.Input[NodePoolNodeConfigKubeletConfigEvictionSoftGracePeriodArgsDict]
    ]
    image_gc_high_threshold_percent: NotRequired[pulumi.Input[_builtins.int]]
    image_gc_low_threshold_percent: NotRequired[pulumi.Input[_builtins.int]]
    image_maximum_gc_age: NotRequired[pulumi.Input[_builtins.str]]
    image_minimum_gc_age: NotRequired[pulumi.Input[_builtins.str]]
    insecure_kubelet_readonly_port_enabled: NotRequired[pulumi.Input[_builtins.str]]
    max_parallel_image_pulls: NotRequired[pulumi.Input[_builtins.int]]
    memory_manager: NotRequired[
        pulumi.Input[NodePoolNodeConfigKubeletConfigMemoryManagerArgsDict]
    ]
    pod_pids_limit: NotRequired[pulumi.Input[_builtins.int]]
    single_process_oom_kill: NotRequired[pulumi.Input[_builtins.bool]]
    topology_manager: NotRequired[
        pulumi.Input[NodePoolNodeConfigKubeletConfigTopologyManagerArgsDict]
    ]

@pulumi.input_type
class NodePoolNodeConfigKubeletConfigArgs:
    def __init__(
        __self__,
        *,
        allowed_unsafe_sysctls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        container_log_max_files: Optional[pulumi.Input[_builtins.int]] = ...,
        container_log_max_size: Optional[pulumi.Input[_builtins.str]] = ...,
        cpu_cfs_quota: Optional[pulumi.Input[_builtins.bool]] = ...,
        cpu_cfs_quota_period: Optional[pulumi.Input[_builtins.str]] = ...,
        cpu_manager_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        eviction_max_pod_grace_period_seconds: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        eviction_minimum_reclaim: Optional[
            pulumi.Input[NodePoolNodeConfigKubeletConfigEvictionMinimumReclaimArgs]
        ] = ...,
        eviction_soft: Optional[
            pulumi.Input[NodePoolNodeConfigKubeletConfigEvictionSoftArgs]
        ] = ...,
        eviction_soft_grace_period: Optional[
            pulumi.Input[NodePoolNodeConfigKubeletConfigEvictionSoftGracePeriodArgs]
        ] = ...,
        image_gc_high_threshold_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        image_gc_low_threshold_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        image_maximum_gc_age: Optional[pulumi.Input[_builtins.str]] = ...,
        image_minimum_gc_age: Optional[pulumi.Input[_builtins.str]] = ...,
        insecure_kubelet_readonly_port_enabled: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        max_parallel_image_pulls: Optional[pulumi.Input[_builtins.int]] = ...,
        memory_manager: Optional[
            pulumi.Input[NodePoolNodeConfigKubeletConfigMemoryManagerArgs]
        ] = ...,
        pod_pids_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        single_process_oom_kill: Optional[pulumi.Input[_builtins.bool]] = ...,
        topology_manager: Optional[
            pulumi.Input[NodePoolNodeConfigKubeletConfigTopologyManagerArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedUnsafeSysctls")
    def allowed_unsafe_sysctls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_unsafe_sysctls.setter
    def allowed_unsafe_sysctls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxFiles")
    def container_log_max_files(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @container_log_max_files.setter
    def container_log_max_files(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="containerLogMaxSize")
    def container_log_max_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_log_max_size.setter
    def container_log_max_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuota")
    def cpu_cfs_quota(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cpu_cfs_quota.setter
    def cpu_cfs_quota(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuCfsQuotaPeriod")
    def cpu_cfs_quota_period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu_cfs_quota_period.setter
    def cpu_cfs_quota_period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuManagerPolicy")
    def cpu_manager_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu_manager_policy.setter
    def cpu_manager_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="evictionMaxPodGracePeriodSeconds")
    def eviction_max_pod_grace_period_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @eviction_max_pod_grace_period_seconds.setter
    def eviction_max_pod_grace_period_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="evictionMinimumReclaim")
    def eviction_minimum_reclaim(
        self,
    ) -> Optional[
        pulumi.Input[NodePoolNodeConfigKubeletConfigEvictionMinimumReclaimArgs]
    ]: ...
    @eviction_minimum_reclaim.setter
    def eviction_minimum_reclaim(
        self,
        value: Optional[
            pulumi.Input[NodePoolNodeConfigKubeletConfigEvictionMinimumReclaimArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="evictionSoft")
    def eviction_soft(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigKubeletConfigEvictionSoftArgs]]: ...
    @eviction_soft.setter
    def eviction_soft(
        self,
        value: Optional[pulumi.Input[NodePoolNodeConfigKubeletConfigEvictionSoftArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="evictionSoftGracePeriod")
    def eviction_soft_grace_period(
        self,
    ) -> Optional[
        pulumi.Input[NodePoolNodeConfigKubeletConfigEvictionSoftGracePeriodArgs]
    ]: ...
    @eviction_soft_grace_period.setter
    def eviction_soft_grace_period(
        self,
        value: Optional[
            pulumi.Input[NodePoolNodeConfigKubeletConfigEvictionSoftGracePeriodArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageGcHighThresholdPercent")
    def image_gc_high_threshold_percent(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @image_gc_high_threshold_percent.setter
    def image_gc_high_threshold_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageGcLowThresholdPercent")
    def image_gc_low_threshold_percent(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @image_gc_low_threshold_percent.setter
    def image_gc_low_threshold_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageMaximumGcAge")
    def image_maximum_gc_age(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_maximum_gc_age.setter
    def image_maximum_gc_age(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageMinimumGcAge")
    def image_minimum_gc_age(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_minimum_gc_age.setter
    def image_minimum_gc_age(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="insecureKubeletReadonlyPortEnabled")
    def insecure_kubelet_readonly_port_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @insecure_kubelet_readonly_port_enabled.setter
    def insecure_kubelet_readonly_port_enabled(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxParallelImagePulls")
    def max_parallel_image_pulls(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_parallel_image_pulls.setter
    def max_parallel_image_pulls(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="memoryManager")
    def memory_manager(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigKubeletConfigMemoryManagerArgs]]: ...
    @memory_manager.setter
    def memory_manager(
        self,
        value: Optional[pulumi.Input[NodePoolNodeConfigKubeletConfigMemoryManagerArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="podPidsLimit")
    def pod_pids_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @pod_pids_limit.setter
    def pod_pids_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="singleProcessOomKill")
    def single_process_oom_kill(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @single_process_oom_kill.setter
    def single_process_oom_kill(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="topologyManager")
    def topology_manager(
        self,
    ) -> Optional[pulumi.Input[NodePoolNodeConfigKubeletConfigTopologyManagerArgs]]: ...
    @topology_manager.setter
    def topology_manager(
        self,
        value: Optional[
            pulumi.Input[NodePoolNodeConfigKubeletConfigTopologyManagerArgs]
        ],
    ): ...

class NodePoolNodeConfigKubeletConfigEvictionMinimumReclaimArgsDict(TypedDict):
    imagefs_available: NotRequired[pulumi.Input[_builtins.str]]
    imagefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    memory_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    pid_available: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigKubeletConfigEvictionMinimumReclaimArgs:
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        imagefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        pid_available: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_available.setter
    def imagefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_inodes_free.setter
    def imagefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory_available.setter
    def memory_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_available.setter
    def nodefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_inodes_free.setter
    def nodefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pid_available.setter
    def pid_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolNodeConfigKubeletConfigEvictionSoftArgsDict(TypedDict):
    imagefs_available: NotRequired[pulumi.Input[_builtins.str]]
    imagefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    memory_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    pid_available: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigKubeletConfigEvictionSoftArgs:
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        imagefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        pid_available: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_available.setter
    def imagefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_inodes_free.setter
    def imagefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory_available.setter
    def memory_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_available.setter
    def nodefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_inodes_free.setter
    def nodefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pid_available.setter
    def pid_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolNodeConfigKubeletConfigEvictionSoftGracePeriodArgsDict(TypedDict):
    imagefs_available: NotRequired[pulumi.Input[_builtins.str]]
    imagefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    memory_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_available: NotRequired[pulumi.Input[_builtins.str]]
    nodefs_inodes_free: NotRequired[pulumi.Input[_builtins.str]]
    pid_available: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigKubeletConfigEvictionSoftGracePeriodArgs:
    def __init__(
        __self__,
        *,
        imagefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        imagefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_available: Optional[pulumi.Input[_builtins.str]] = ...,
        nodefs_inodes_free: Optional[pulumi.Input[_builtins.str]] = ...,
        pid_available: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imagefsAvailable")
    def imagefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_available.setter
    def imagefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imagefsInodesFree")
    def imagefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagefs_inodes_free.setter
    def imagefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryAvailable")
    def memory_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory_available.setter
    def memory_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsAvailable")
    def nodefs_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_available.setter
    def nodefs_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodefsInodesFree")
    def nodefs_inodes_free(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nodefs_inodes_free.setter
    def nodefs_inodes_free(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pidAvailable")
    def pid_available(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pid_available.setter
    def pid_available(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolNodeConfigKubeletConfigMemoryManagerArgsDict(TypedDict):
    policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigKubeletConfigMemoryManagerArgs:
    def __init__(
        __self__, *, policy: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolNodeConfigKubeletConfigTopologyManagerArgsDict(TypedDict):
    policy: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigKubeletConfigTopologyManagerArgs:
    def __init__(
        __self__,
        *,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolNodeConfigLinuxNodeConfigArgsDict(TypedDict):
    cgroup_mode: NotRequired[pulumi.Input[_builtins.str]]
    hugepages_config: NotRequired[
        pulumi.Input[NodePoolNodeConfigLinuxNodeConfigHugepagesConfigArgsDict]
    ]
    node_kernel_module_loading: NotRequired[
        pulumi.Input[NodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgsDict]
    ]
    sysctls: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    transparent_hugepage_defrag: NotRequired[pulumi.Input[_builtins.str]]
    transparent_hugepage_enabled: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigLinuxNodeConfigArgs:
    def __init__(
        __self__,
        *,
        cgroup_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        hugepages_config: Optional[
            pulumi.Input[NodePoolNodeConfigLinuxNodeConfigHugepagesConfigArgs]
        ] = ...,
        node_kernel_module_loading: Optional[
            pulumi.Input[NodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgs]
        ] = ...,
        sysctls: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transparent_hugepage_defrag: Optional[pulumi.Input[_builtins.str]] = ...,
        transparent_hugepage_enabled: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cgroupMode")
    def cgroup_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cgroup_mode.setter
    def cgroup_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hugepagesConfig")
    def hugepages_config(
        self,
    ) -> Optional[
        pulumi.Input[NodePoolNodeConfigLinuxNodeConfigHugepagesConfigArgs]
    ]: ...
    @hugepages_config.setter
    def hugepages_config(
        self,
        value: Optional[
            pulumi.Input[NodePoolNodeConfigLinuxNodeConfigHugepagesConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeKernelModuleLoading")
    def node_kernel_module_loading(
        self,
    ) -> Optional[
        pulumi.Input[NodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgs]
    ]: ...
    @node_kernel_module_loading.setter
    def node_kernel_module_loading(
        self,
        value: Optional[
            pulumi.Input[NodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sysctls(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @sysctls.setter
    def sysctls(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageDefrag")
    def transparent_hugepage_defrag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transparent_hugepage_defrag.setter
    def transparent_hugepage_defrag(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transparentHugepageEnabled")
    def transparent_hugepage_enabled(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transparent_hugepage_enabled.setter
    def transparent_hugepage_enabled(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class NodePoolNodeConfigLinuxNodeConfigHugepagesConfigArgsDict(TypedDict):
    hugepage_size1g: NotRequired[pulumi.Input[_builtins.int]]
    hugepage_size2m: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class NodePoolNodeConfigLinuxNodeConfigHugepagesConfigArgs:
    def __init__(
        __self__,
        *,
        hugepage_size1g: Optional[pulumi.Input[_builtins.int]] = ...,
        hugepage_size2m: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize1g")
    def hugepage_size1g(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hugepage_size1g.setter
    def hugepage_size1g(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="hugepageSize2m")
    def hugepage_size2m(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hugepage_size2m.setter
    def hugepage_size2m(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class NodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgsDict(TypedDict):
    policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigLinuxNodeConfigNodeKernelModuleLoadingArgs:
    def __init__(
        __self__, *, policy: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolNodeConfigLocalNvmeSsdBlockConfigArgsDict(TypedDict):
    local_ssd_count: pulumi.Input[_builtins.int]

@pulumi.input_type
class NodePoolNodeConfigLocalNvmeSsdBlockConfigArgs:
    def __init__(__self__, *, local_ssd_count: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> pulumi.Input[_builtins.int]: ...
    @local_ssd_count.setter
    def local_ssd_count(self, value: pulumi.Input[_builtins.int]): ...

class NodePoolNodeConfigReservationAffinityArgsDict(TypedDict):
    consume_reservation_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class NodePoolNodeConfigReservationAffinityArgs:
    def __init__(
        __self__,
        *,
        consume_reservation_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> pulumi.Input[_builtins.str]: ...
    @consume_reservation_type.setter
    def consume_reservation_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class NodePoolNodeConfigSandboxConfigArgsDict(TypedDict):
    sandbox_type: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigSandboxConfigArgs:
    def __init__(
        __self__,
        *,
        sandbox_type: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sandboxType")
    @_utilities.deprecated(...)
    def sandbox_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sandbox_type.setter
    def sandbox_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolNodeConfigSecondaryBootDiskArgsDict(TypedDict):
    disk_image: pulumi.Input[_builtins.str]
    mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigSecondaryBootDiskArgs:
    def __init__(
        __self__,
        *,
        disk_image: pulumi.Input[_builtins.str],
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskImage")
    def disk_image(self) -> pulumi.Input[_builtins.str]: ...
    @disk_image.setter
    def disk_image(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolNodeConfigShieldedInstanceConfigArgsDict(TypedDict):
    enable_integrity_monitoring: NotRequired[pulumi.Input[_builtins.bool]]
    enable_secure_boot: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class NodePoolNodeConfigShieldedInstanceConfigArgs:
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_secure_boot: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_integrity_monitoring.setter
    def enable_integrity_monitoring(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_secure_boot.setter
    def enable_secure_boot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class NodePoolNodeConfigSoleTenantConfigArgsDict(TypedDict):
    node_affinities: pulumi.Input[
        Sequence[pulumi.Input[NodePoolNodeConfigSoleTenantConfigNodeAffinityArgsDict]]
    ]
    min_node_cpus: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class NodePoolNodeConfigSoleTenantConfigArgs:
    def __init__(
        __self__,
        *,
        node_affinities: pulumi.Input[
            Sequence[pulumi.Input[NodePoolNodeConfigSoleTenantConfigNodeAffinityArgs]]
        ],
        min_node_cpus: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeAffinities")
    def node_affinities(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[NodePoolNodeConfigSoleTenantConfigNodeAffinityArgs]]
    ]: ...
    @node_affinities.setter
    def node_affinities(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[NodePoolNodeConfigSoleTenantConfigNodeAffinityArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minNodeCpus")
    def min_node_cpus(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_node_cpus.setter
    def min_node_cpus(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class NodePoolNodeConfigSoleTenantConfigNodeAffinityArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    operator: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class NodePoolNodeConfigSoleTenantConfigNodeAffinityArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        operator: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[_builtins.str]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class NodePoolNodeConfigTaintArgsDict(TypedDict):
    effect: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class NodePoolNodeConfigTaintArgs:
    def __init__(
        __self__,
        *,
        effect: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> pulumi.Input[_builtins.str]: ...
    @effect.setter
    def effect(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class NodePoolNodeConfigWindowsNodeConfigArgsDict(TypedDict):
    osversion: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolNodeConfigWindowsNodeConfigArgs:
    def __init__(
        __self__, *, osversion: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def osversion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @osversion.setter
    def osversion(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolNodeConfigWorkloadMetadataConfigArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class NodePoolNodeConfigWorkloadMetadataConfigArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...

class NodePoolNodeDrainConfigArgsDict(TypedDict):
    respect_pdb_during_node_pool_deletion: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class NodePoolNodeDrainConfigArgs:
    def __init__(
        __self__,
        *,
        respect_pdb_during_node_pool_deletion: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="respectPdbDuringNodePoolDeletion")
    def respect_pdb_during_node_pool_deletion(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @respect_pdb_during_node_pool_deletion.setter
    def respect_pdb_during_node_pool_deletion(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class NodePoolPlacementPolicyArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    policy_name: NotRequired[pulumi.Input[_builtins.str]]
    tpu_topology: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolPlacementPolicyArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tpu_topology: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tpuTopology")
    def tpu_topology(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tpu_topology.setter
    def tpu_topology(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolQueuedProvisioningArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class NodePoolQueuedProvisioningArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class NodePoolUpgradeSettingsArgsDict(TypedDict):
    blue_green_settings: NotRequired[
        pulumi.Input[NodePoolUpgradeSettingsBlueGreenSettingsArgsDict]
    ]
    max_surge: NotRequired[pulumi.Input[_builtins.int]]
    max_unavailable: NotRequired[pulumi.Input[_builtins.int]]
    strategy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolUpgradeSettingsArgs:
    def __init__(
        __self__,
        *,
        blue_green_settings: Optional[
            pulumi.Input[NodePoolUpgradeSettingsBlueGreenSettingsArgs]
        ] = ...,
        max_surge: Optional[pulumi.Input[_builtins.int]] = ...,
        max_unavailable: Optional[pulumi.Input[_builtins.int]] = ...,
        strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blueGreenSettings")
    def blue_green_settings(
        self,
    ) -> Optional[pulumi.Input[NodePoolUpgradeSettingsBlueGreenSettingsArgs]]: ...
    @blue_green_settings.setter
    def blue_green_settings(
        self,
        value: Optional[pulumi.Input[NodePoolUpgradeSettingsBlueGreenSettingsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxSurge")
    def max_surge(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_surge.setter
    def max_surge(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxUnavailable")
    def max_unavailable(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_unavailable.setter
    def max_unavailable(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @strategy.setter
    def strategy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolUpgradeSettingsBlueGreenSettingsArgsDict(TypedDict):
    autoscaled_rollout_policy: NotRequired[
        pulumi.Input[
            NodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicyArgsDict
        ]
    ]
    node_pool_soak_duration: NotRequired[pulumi.Input[_builtins.str]]
    standard_rollout_policy: NotRequired[
        pulumi.Input[
            NodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgsDict
        ]
    ]

@pulumi.input_type
class NodePoolUpgradeSettingsBlueGreenSettingsArgs:
    def __init__(
        __self__,
        *,
        autoscaled_rollout_policy: Optional[
            pulumi.Input[
                NodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicyArgs
            ]
        ] = ...,
        node_pool_soak_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        standard_rollout_policy: Optional[
            pulumi.Input[
                NodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscaledRolloutPolicy")
    def autoscaled_rollout_policy(
        self,
    ) -> Optional[
        pulumi.Input[
            NodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicyArgs
        ]
    ]: ...
    @autoscaled_rollout_policy.setter
    def autoscaled_rollout_policy(
        self,
        value: Optional[
            pulumi.Input[
                NodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodePoolSoakDuration")
    def node_pool_soak_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_pool_soak_duration.setter
    def node_pool_soak_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="standardRolloutPolicy")
    def standard_rollout_policy(
        self,
    ) -> Optional[
        pulumi.Input[NodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgs]
    ]: ...
    @standard_rollout_policy.setter
    def standard_rollout_policy(
        self,
        value: Optional[
            pulumi.Input[
                NodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgs
            ]
        ],
    ): ...

class NodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicyArgsDict(
    TypedDict
):
    wait_for_drain_duration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolUpgradeSettingsBlueGreenSettingsAutoscaledRolloutPolicyArgs:
    def __init__(
        __self__,
        *,
        wait_for_drain_duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="waitForDrainDuration")
    def wait_for_drain_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait_for_drain_duration.setter
    def wait_for_drain_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgsDict(TypedDict):
    batch_node_count: NotRequired[pulumi.Input[_builtins.int]]
    batch_percentage: NotRequired[pulumi.Input[_builtins.float]]
    batch_soak_duration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodePoolUpgradeSettingsBlueGreenSettingsStandardRolloutPolicyArgs:
    def __init__(
        __self__,
        *,
        batch_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        batch_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        batch_soak_duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchNodeCount")
    def batch_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @batch_node_count.setter
    def batch_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="batchPercentage")
    def batch_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @batch_percentage.setter
    def batch_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="batchSoakDuration")
    def batch_soak_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @batch_soak_duration.setter
    def batch_soak_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
