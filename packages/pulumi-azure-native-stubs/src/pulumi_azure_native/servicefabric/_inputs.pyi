import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    ...,
    ...,
    "AdditionalNetworkInterfaceConfigurationArgs",
    "AdditionalNetworkInterfaceConfigurationArgsDict",
    "ApplicationHealthPolicyArgs",
    "ApplicationHealthPolicyArgsDict",
    "ApplicationTypeVersionsCleanupPolicyArgs",
    "ApplicationTypeVersionsCleanupPolicyArgsDict",
    "ApplicationUpgradePolicyArgs",
    "ApplicationUpgradePolicyArgsDict",
    "ApplicationUserAssignedIdentityArgs",
    "ApplicationUserAssignedIdentityArgsDict",
    "AveragePartitionLoadScalingTriggerArgs",
    "AveragePartitionLoadScalingTriggerArgsDict",
    "AverageServiceLoadScalingTriggerArgs",
    "AverageServiceLoadScalingTriggerArgsDict",
    "AzureActiveDirectoryArgs",
    "AzureActiveDirectoryArgsDict",
    "ClientCertificateArgs",
    "ClientCertificateArgsDict",
    "ClusterHealthPolicyArgs",
    "ClusterHealthPolicyArgsDict",
    "ClusterMonitoringPolicyArgs",
    "ClusterMonitoringPolicyArgsDict",
    "ClusterUpgradeDeltaHealthPolicyArgs",
    "ClusterUpgradeDeltaHealthPolicyArgsDict",
    "ClusterUpgradePolicyArgs",
    "ClusterUpgradePolicyArgsDict",
    "EndpointRangeDescriptionArgs",
    "EndpointRangeDescriptionArgsDict",
    "FrontendConfigurationArgs",
    "FrontendConfigurationArgsDict",
    "IpConfigurationPublicIPAddressConfigurationArgs",
    ...,
    "IpConfigurationArgs",
    "IpConfigurationArgsDict",
    "IpTagArgs",
    "IpTagArgsDict",
    "LoadBalancingRuleArgs",
    "LoadBalancingRuleArgsDict",
    "ManagedIdentityArgs",
    "ManagedIdentityArgsDict",
    "NamedPartitionSchemeArgs",
    "NamedPartitionSchemeArgsDict",
    "NetworkSecurityRuleArgs",
    "NetworkSecurityRuleArgsDict",
    "NodeTypeNatConfigArgs",
    "NodeTypeNatConfigArgsDict",
    "NodeTypeSkuArgs",
    "NodeTypeSkuArgsDict",
    "PartitionInstanceCountScaleMechanismArgs",
    "PartitionInstanceCountScaleMechanismArgsDict",
    "RollingUpgradeMonitoringPolicyArgs",
    "RollingUpgradeMonitoringPolicyArgsDict",
    "ScalingPolicyArgs",
    "ScalingPolicyArgsDict",
    "ServiceCorrelationArgs",
    "ServiceCorrelationArgsDict",
    "ServiceEndpointArgs",
    "ServiceEndpointArgsDict",
    "ServiceLoadMetricArgs",
    "ServiceLoadMetricArgsDict",
    "ServicePlacementInvalidDomainPolicyArgs",
    "ServicePlacementInvalidDomainPolicyArgsDict",
    "ServicePlacementNonPartiallyPlaceServicePolicyArgs",
    ...,
    "ServicePlacementPreferPrimaryDomainPolicyArgs",
    "ServicePlacementPreferPrimaryDomainPolicyArgsDict",
    ...,
    ...,
    "ServicePlacementRequiredDomainPolicyArgs",
    "ServicePlacementRequiredDomainPolicyArgsDict",
    "ServiceTypeHealthPolicyArgs",
    "ServiceTypeHealthPolicyArgsDict",
    "SettingsParameterDescriptionArgs",
    "SettingsParameterDescriptionArgsDict",
    "SettingsSectionDescriptionArgs",
    "SettingsSectionDescriptionArgsDict",
    "SingletonPartitionSchemeArgs",
    "SingletonPartitionSchemeArgsDict",
    "SkuArgs",
    "SkuArgsDict",
    "StatefulServicePropertiesArgs",
    "StatefulServicePropertiesArgsDict",
    "StatelessServicePropertiesArgs",
    "StatelessServicePropertiesArgsDict",
    "SubResourceArgs",
    "SubResourceArgsDict",
    "SubnetArgs",
    "SubnetArgsDict",
    "UniformInt64RangePartitionSchemeArgs",
    "UniformInt64RangePartitionSchemeArgsDict",
    "VMSSExtensionArgs",
    "VMSSExtensionArgsDict",
    "VaultCertificateArgs",
    "VaultCertificateArgsDict",
    "VaultSecretGroupArgs",
    "VaultSecretGroupArgsDict",
    "VmImagePlanArgs",
    "VmImagePlanArgsDict",
    "VmManagedIdentityArgs",
    "VmManagedIdentityArgsDict",
    "VmssDataDiskArgs",
    "VmssDataDiskArgsDict",
]

class AddRemoveIncrementalNamedPartitionScalingMechanismArgsDict(TypedDict):
    kind: pulumi.Input[_builtins.str]
    max_partition_count: pulumi.Input[_builtins.int]
    min_partition_count: pulumi.Input[_builtins.int]
    scale_increment: pulumi.Input[_builtins.int]

@pulumi.input_type
class AddRemoveIncrementalNamedPartitionScalingMechanismArgs:
    def __init__(
        __self__,
        *,
        kind: pulumi.Input[_builtins.str],
        max_partition_count: pulumi.Input[_builtins.int],
        min_partition_count: pulumi.Input[_builtins.int],
        scale_increment: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maxPartitionCount")
    def max_partition_count(self) -> pulumi.Input[_builtins.int]: ...
    @max_partition_count.setter
    def max_partition_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minPartitionCount")
    def min_partition_count(self) -> pulumi.Input[_builtins.int]: ...
    @min_partition_count.setter
    def min_partition_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="scaleIncrement")
    def scale_increment(self) -> pulumi.Input[_builtins.int]: ...
    @scale_increment.setter
    def scale_increment(self, value: pulumi.Input[_builtins.int]): ...

class AdditionalNetworkInterfaceConfigurationArgsDict(TypedDict):
    ip_configurations: pulumi.Input[Sequence[pulumi.Input[IpConfigurationArgsDict]]]
    name: pulumi.Input[_builtins.str]
    dscp_configuration: NotRequired[pulumi.Input[SubResourceArgsDict]]
    enable_accelerated_networking: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AdditionalNetworkInterfaceConfigurationArgs:
    def __init__(
        __self__,
        *,
        ip_configurations: pulumi.Input[Sequence[pulumi.Input[IpConfigurationArgs]]],
        name: pulumi.Input[_builtins.str],
        dscp_configuration: Optional[pulumi.Input[SubResourceArgs]] = ...,
        enable_accelerated_networking: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[IpConfigurationArgs]]]: ...
    @ip_configurations.setter
    def ip_configurations(
        self, value: pulumi.Input[Sequence[pulumi.Input[IpConfigurationArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dscpConfiguration")
    def dscp_configuration(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @dscp_configuration.setter
    def dscp_configuration(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_accelerated_networking.setter
    def enable_accelerated_networking(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ApplicationHealthPolicyArgsDict(TypedDict):
    consider_warning_as_error: pulumi.Input[_builtins.bool]
    max_percent_unhealthy_deployed_applications: pulumi.Input[_builtins.int]
    default_service_type_health_policy: NotRequired[
        pulumi.Input[ServiceTypeHealthPolicyArgsDict]
    ]
    service_type_health_policy_map: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[ServiceTypeHealthPolicyArgsDict]]]
    ]

@pulumi.input_type
class ApplicationHealthPolicyArgs:
    def __init__(
        __self__,
        *,
        consider_warning_as_error: pulumi.Input[_builtins.bool],
        max_percent_unhealthy_deployed_applications: pulumi.Input[_builtins.int],
        default_service_type_health_policy: Optional[
            pulumi.Input[ServiceTypeHealthPolicyArgs]
        ] = ...,
        service_type_health_policy_map: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ServiceTypeHealthPolicyArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="considerWarningAsError")
    def consider_warning_as_error(self) -> pulumi.Input[_builtins.bool]: ...
    @consider_warning_as_error.setter
    def consider_warning_as_error(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="maxPercentUnhealthyDeployedApplications")
    def max_percent_unhealthy_deployed_applications(
        self,
    ) -> pulumi.Input[_builtins.int]: ...
    @max_percent_unhealthy_deployed_applications.setter
    def max_percent_unhealthy_deployed_applications(
        self, value: pulumi.Input[_builtins.int]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultServiceTypeHealthPolicy")
    def default_service_type_health_policy(
        self,
    ) -> Optional[pulumi.Input[ServiceTypeHealthPolicyArgs]]: ...
    @default_service_type_health_policy.setter
    def default_service_type_health_policy(
        self, value: Optional[pulumi.Input[ServiceTypeHealthPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceTypeHealthPolicyMap")
    def service_type_health_policy_map(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[ServiceTypeHealthPolicyArgs]]]
    ]: ...
    @service_type_health_policy_map.setter
    def service_type_health_policy_map(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ServiceTypeHealthPolicyArgs]]]
        ],
    ): ...

class ApplicationTypeVersionsCleanupPolicyArgsDict(TypedDict):
    max_unused_versions_to_keep: pulumi.Input[_builtins.int]

@pulumi.input_type
class ApplicationTypeVersionsCleanupPolicyArgs:
    def __init__(
        __self__, *, max_unused_versions_to_keep: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxUnusedVersionsToKeep")
    def max_unused_versions_to_keep(self) -> pulumi.Input[_builtins.int]: ...
    @max_unused_versions_to_keep.setter
    def max_unused_versions_to_keep(self, value: pulumi.Input[_builtins.int]): ...

class ApplicationUpgradePolicyArgsDict(TypedDict):
    application_health_policy: NotRequired[
        pulumi.Input[ApplicationHealthPolicyArgsDict]
    ]
    force_restart: NotRequired[pulumi.Input[_builtins.bool]]
    instance_close_delay_duration: NotRequired[pulumi.Input[_builtins.float]]
    recreate_application: NotRequired[pulumi.Input[_builtins.bool]]
    rolling_upgrade_monitoring_policy: NotRequired[
        pulumi.Input[RollingUpgradeMonitoringPolicyArgsDict]
    ]
    upgrade_mode: NotRequired[pulumi.Input[Union[_builtins.str, RollingUpgradeMode]]]
    upgrade_replica_set_check_timeout: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ApplicationUpgradePolicyArgs:
    def __init__(
        __self__,
        *,
        application_health_policy: Optional[
            pulumi.Input[ApplicationHealthPolicyArgs]
        ] = ...,
        force_restart: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_close_delay_duration: Optional[pulumi.Input[_builtins.float]] = ...,
        recreate_application: Optional[pulumi.Input[_builtins.bool]] = ...,
        rolling_upgrade_monitoring_policy: Optional[
            pulumi.Input[RollingUpgradeMonitoringPolicyArgs]
        ] = ...,
        upgrade_mode: Optional[
            pulumi.Input[Union[_builtins.str, RollingUpgradeMode]]
        ] = ...,
        upgrade_replica_set_check_timeout: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationHealthPolicy")
    def application_health_policy(
        self,
    ) -> Optional[pulumi.Input[ApplicationHealthPolicyArgs]]: ...
    @application_health_policy.setter
    def application_health_policy(
        self, value: Optional[pulumi.Input[ApplicationHealthPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="forceRestart")
    def force_restart(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_restart.setter
    def force_restart(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceCloseDelayDuration")
    def instance_close_delay_duration(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @instance_close_delay_duration.setter
    def instance_close_delay_duration(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recreateApplication")
    def recreate_application(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @recreate_application.setter
    def recreate_application(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="rollingUpgradeMonitoringPolicy")
    def rolling_upgrade_monitoring_policy(
        self,
    ) -> Optional[pulumi.Input[RollingUpgradeMonitoringPolicyArgs]]: ...
    @rolling_upgrade_monitoring_policy.setter
    def rolling_upgrade_monitoring_policy(
        self, value: Optional[pulumi.Input[RollingUpgradeMonitoringPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="upgradeMode")
    def upgrade_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RollingUpgradeMode]]]: ...
    @upgrade_mode.setter
    def upgrade_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RollingUpgradeMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="upgradeReplicaSetCheckTimeout")
    def upgrade_replica_set_check_timeout(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @upgrade_replica_set_check_timeout.setter
    def upgrade_replica_set_check_timeout(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

class ApplicationUserAssignedIdentityArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    principal_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ApplicationUserAssignedIdentityArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        principal_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[_builtins.str]: ...
    @principal_id.setter
    def principal_id(self, value: pulumi.Input[_builtins.str]): ...

class AveragePartitionLoadScalingTriggerArgsDict(TypedDict):
    kind: pulumi.Input[_builtins.str]
    lower_load_threshold: pulumi.Input[_builtins.float]
    metric_name: pulumi.Input[_builtins.str]
    scale_interval: pulumi.Input[_builtins.str]
    upper_load_threshold: pulumi.Input[_builtins.float]

@pulumi.input_type
class AveragePartitionLoadScalingTriggerArgs:
    def __init__(
        __self__,
        *,
        kind: pulumi.Input[_builtins.str],
        lower_load_threshold: pulumi.Input[_builtins.float],
        metric_name: pulumi.Input[_builtins.str],
        scale_interval: pulumi.Input[_builtins.str],
        upper_load_threshold: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lowerLoadThreshold")
    def lower_load_threshold(self) -> pulumi.Input[_builtins.float]: ...
    @lower_load_threshold.setter
    def lower_load_threshold(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scaleInterval")
    def scale_interval(self) -> pulumi.Input[_builtins.str]: ...
    @scale_interval.setter
    def scale_interval(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="upperLoadThreshold")
    def upper_load_threshold(self) -> pulumi.Input[_builtins.float]: ...
    @upper_load_threshold.setter
    def upper_load_threshold(self, value: pulumi.Input[_builtins.float]): ...

class AverageServiceLoadScalingTriggerArgsDict(TypedDict):
    kind: pulumi.Input[_builtins.str]
    lower_load_threshold: pulumi.Input[_builtins.float]
    metric_name: pulumi.Input[_builtins.str]
    scale_interval: pulumi.Input[_builtins.str]
    upper_load_threshold: pulumi.Input[_builtins.float]
    use_only_primary_load: pulumi.Input[_builtins.bool]

@pulumi.input_type
class AverageServiceLoadScalingTriggerArgs:
    def __init__(
        __self__,
        *,
        kind: pulumi.Input[_builtins.str],
        lower_load_threshold: pulumi.Input[_builtins.float],
        metric_name: pulumi.Input[_builtins.str],
        scale_interval: pulumi.Input[_builtins.str],
        upper_load_threshold: pulumi.Input[_builtins.float],
        use_only_primary_load: pulumi.Input[_builtins.bool],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lowerLoadThreshold")
    def lower_load_threshold(self) -> pulumi.Input[_builtins.float]: ...
    @lower_load_threshold.setter
    def lower_load_threshold(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scaleInterval")
    def scale_interval(self) -> pulumi.Input[_builtins.str]: ...
    @scale_interval.setter
    def scale_interval(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="upperLoadThreshold")
    def upper_load_threshold(self) -> pulumi.Input[_builtins.float]: ...
    @upper_load_threshold.setter
    def upper_load_threshold(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="useOnlyPrimaryLoad")
    def use_only_primary_load(self) -> pulumi.Input[_builtins.bool]: ...
    @use_only_primary_load.setter
    def use_only_primary_load(self, value: pulumi.Input[_builtins.bool]): ...

class AzureActiveDirectoryArgsDict(TypedDict):
    client_application: NotRequired[pulumi.Input[_builtins.str]]
    cluster_application: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureActiveDirectoryArgs:
    def __init__(
        __self__,
        *,
        client_application: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_application: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientApplication")
    def client_application(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_application.setter
    def client_application(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterApplication")
    def cluster_application(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_application.setter
    def cluster_application(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClientCertificateArgsDict(TypedDict):
    is_admin: pulumi.Input[_builtins.bool]
    common_name: NotRequired[pulumi.Input[_builtins.str]]
    issuer_thumbprint: NotRequired[pulumi.Input[_builtins.str]]
    thumbprint: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClientCertificateArgs:
    def __init__(
        __self__,
        *,
        is_admin: pulumi.Input[_builtins.bool],
        common_name: Optional[pulumi.Input[_builtins.str]] = ...,
        issuer_thumbprint: Optional[pulumi.Input[_builtins.str]] = ...,
        thumbprint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isAdmin")
    def is_admin(self) -> pulumi.Input[_builtins.bool]: ...
    @is_admin.setter
    def is_admin(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @common_name.setter
    def common_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="issuerThumbprint")
    def issuer_thumbprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @issuer_thumbprint.setter
    def issuer_thumbprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @thumbprint.setter
    def thumbprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterHealthPolicyArgsDict(TypedDict):
    max_percent_unhealthy_applications: pulumi.Input[_builtins.int]
    max_percent_unhealthy_nodes: pulumi.Input[_builtins.int]

@pulumi.input_type
class ClusterHealthPolicyArgs:
    def __init__(
        __self__,
        *,
        max_percent_unhealthy_applications: Optional[pulumi.Input[_builtins.int]] = ...,
        max_percent_unhealthy_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPercentUnhealthyApplications")
    def max_percent_unhealthy_applications(self) -> pulumi.Input[_builtins.int]: ...
    @max_percent_unhealthy_applications.setter
    def max_percent_unhealthy_applications(
        self, value: pulumi.Input[_builtins.int]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxPercentUnhealthyNodes")
    def max_percent_unhealthy_nodes(self) -> pulumi.Input[_builtins.int]: ...
    @max_percent_unhealthy_nodes.setter
    def max_percent_unhealthy_nodes(self, value: pulumi.Input[_builtins.int]): ...

class ClusterMonitoringPolicyArgsDict(TypedDict):
    health_check_retry_timeout: pulumi.Input[_builtins.str]
    health_check_stable_duration: pulumi.Input[_builtins.str]
    health_check_wait_duration: pulumi.Input[_builtins.str]
    upgrade_domain_timeout: pulumi.Input[_builtins.str]
    upgrade_timeout: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterMonitoringPolicyArgs:
    def __init__(
        __self__,
        *,
        health_check_retry_timeout: pulumi.Input[_builtins.str],
        health_check_stable_duration: pulumi.Input[_builtins.str],
        health_check_wait_duration: pulumi.Input[_builtins.str],
        upgrade_domain_timeout: pulumi.Input[_builtins.str],
        upgrade_timeout: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckRetryTimeout")
    def health_check_retry_timeout(self) -> pulumi.Input[_builtins.str]: ...
    @health_check_retry_timeout.setter
    def health_check_retry_timeout(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckStableDuration")
    def health_check_stable_duration(self) -> pulumi.Input[_builtins.str]: ...
    @health_check_stable_duration.setter
    def health_check_stable_duration(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckWaitDuration")
    def health_check_wait_duration(self) -> pulumi.Input[_builtins.str]: ...
    @health_check_wait_duration.setter
    def health_check_wait_duration(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="upgradeDomainTimeout")
    def upgrade_domain_timeout(self) -> pulumi.Input[_builtins.str]: ...
    @upgrade_domain_timeout.setter
    def upgrade_domain_timeout(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="upgradeTimeout")
    def upgrade_timeout(self) -> pulumi.Input[_builtins.str]: ...
    @upgrade_timeout.setter
    def upgrade_timeout(self, value: pulumi.Input[_builtins.str]): ...

class ClusterUpgradeDeltaHealthPolicyArgsDict(TypedDict):
    max_percent_delta_unhealthy_nodes: pulumi.Input[_builtins.int]
    max_percent_delta_unhealthy_applications: NotRequired[pulumi.Input[_builtins.int]]
    max_percent_upgrade_domain_delta_unhealthy_nodes: NotRequired[
        pulumi.Input[_builtins.int]
    ]

@pulumi.input_type
class ClusterUpgradeDeltaHealthPolicyArgs:
    def __init__(
        __self__,
        *,
        max_percent_delta_unhealthy_nodes: pulumi.Input[_builtins.int],
        max_percent_delta_unhealthy_applications: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        max_percent_upgrade_domain_delta_unhealthy_nodes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPercentDeltaUnhealthyNodes")
    def max_percent_delta_unhealthy_nodes(self) -> pulumi.Input[_builtins.int]: ...
    @max_percent_delta_unhealthy_nodes.setter
    def max_percent_delta_unhealthy_nodes(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="maxPercentDeltaUnhealthyApplications")
    def max_percent_delta_unhealthy_applications(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_percent_delta_unhealthy_applications.setter
    def max_percent_delta_unhealthy_applications(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxPercentUpgradeDomainDeltaUnhealthyNodes")
    def max_percent_upgrade_domain_delta_unhealthy_nodes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_percent_upgrade_domain_delta_unhealthy_nodes.setter
    def max_percent_upgrade_domain_delta_unhealthy_nodes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ClusterUpgradePolicyArgsDict(TypedDict):
    delta_health_policy: NotRequired[
        pulumi.Input[ClusterUpgradeDeltaHealthPolicyArgsDict]
    ]
    force_restart: NotRequired[pulumi.Input[_builtins.bool]]
    health_policy: NotRequired[pulumi.Input[ClusterHealthPolicyArgsDict]]
    monitoring_policy: NotRequired[pulumi.Input[ClusterMonitoringPolicyArgsDict]]
    upgrade_replica_set_check_timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterUpgradePolicyArgs:
    def __init__(
        __self__,
        *,
        delta_health_policy: Optional[
            pulumi.Input[ClusterUpgradeDeltaHealthPolicyArgs]
        ] = ...,
        force_restart: Optional[pulumi.Input[_builtins.bool]] = ...,
        health_policy: Optional[pulumi.Input[ClusterHealthPolicyArgs]] = ...,
        monitoring_policy: Optional[pulumi.Input[ClusterMonitoringPolicyArgs]] = ...,
        upgrade_replica_set_check_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deltaHealthPolicy")
    def delta_health_policy(
        self,
    ) -> Optional[pulumi.Input[ClusterUpgradeDeltaHealthPolicyArgs]]: ...
    @delta_health_policy.setter
    def delta_health_policy(
        self, value: Optional[pulumi.Input[ClusterUpgradeDeltaHealthPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="forceRestart")
    def force_restart(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_restart.setter
    def force_restart(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="healthPolicy")
    def health_policy(self) -> Optional[pulumi.Input[ClusterHealthPolicyArgs]]: ...
    @health_policy.setter
    def health_policy(self, value: Optional[pulumi.Input[ClusterHealthPolicyArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringPolicy")
    def monitoring_policy(
        self,
    ) -> Optional[pulumi.Input[ClusterMonitoringPolicyArgs]]: ...
    @monitoring_policy.setter
    def monitoring_policy(
        self, value: Optional[pulumi.Input[ClusterMonitoringPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="upgradeReplicaSetCheckTimeout")
    def upgrade_replica_set_check_timeout(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @upgrade_replica_set_check_timeout.setter
    def upgrade_replica_set_check_timeout(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class EndpointRangeDescriptionArgsDict(TypedDict):
    end_port: pulumi.Input[_builtins.int]
    start_port: pulumi.Input[_builtins.int]

@pulumi.input_type
class EndpointRangeDescriptionArgs:
    def __init__(
        __self__,
        *,
        end_port: pulumi.Input[_builtins.int],
        start_port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endPort")
    def end_port(self) -> pulumi.Input[_builtins.int]: ...
    @end_port.setter
    def end_port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="startPort")
    def start_port(self) -> pulumi.Input[_builtins.int]: ...
    @start_port.setter
    def start_port(self, value: pulumi.Input[_builtins.int]): ...

class FrontendConfigurationArgsDict(TypedDict):
    application_gateway_backend_address_pool_id: NotRequired[
        pulumi.Input[_builtins.str]
    ]
    ip_address_type: NotRequired[pulumi.Input[Union[_builtins.str, IPAddressType]]]
    load_balancer_backend_address_pool_id: NotRequired[pulumi.Input[_builtins.str]]
    load_balancer_inbound_nat_pool_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FrontendConfigurationArgs:
    def __init__(
        __self__,
        *,
        application_gateway_backend_address_pool_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        ip_address_type: Optional[
            pulumi.Input[Union[_builtins.str, IPAddressType]]
        ] = ...,
        load_balancer_backend_address_pool_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        load_balancer_inbound_nat_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationGatewayBackendAddressPoolId")
    def application_gateway_backend_address_pool_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_gateway_backend_address_pool_id.setter
    def application_gateway_backend_address_pool_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IPAddressType]]]: ...
    @ip_address_type.setter
    def ip_address_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IPAddressType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerBackendAddressPoolId")
    def load_balancer_backend_address_pool_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancer_backend_address_pool_id.setter
    def load_balancer_backend_address_pool_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerInboundNatPoolId")
    def load_balancer_inbound_nat_pool_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancer_inbound_nat_pool_id.setter
    def load_balancer_inbound_nat_pool_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class IpConfigurationPublicIPAddressConfigurationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    ip_tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[IpTagArgsDict]]]]
    public_ip_address_version: NotRequired[
        pulumi.Input[Union[_builtins.str, PublicIPAddressVersion]]
    ]

@pulumi.input_type
class IpConfigurationPublicIPAddressConfigurationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        ip_tags: Optional[pulumi.Input[Sequence[pulumi.Input[IpTagArgs]]]] = ...,
        public_ip_address_version: Optional[
            pulumi.Input[Union[_builtins.str, PublicIPAddressVersion]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpTagArgs]]]]: ...
    @ip_tags.setter
    def ip_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpTagArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddressVersion")
    def public_ip_address_version(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicIPAddressVersion]]]: ...
    @public_ip_address_version.setter
    def public_ip_address_version(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PublicIPAddressVersion]]],
    ): ...

class IpConfigurationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    application_gateway_backend_address_pools: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]
    ]
    load_balancer_backend_address_pools: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]
    ]
    load_balancer_inbound_nat_pools: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]
    ]
    private_ip_address_version: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateIPAddressVersion]]
    ]
    public_ip_address_configuration: NotRequired[
        pulumi.Input[IpConfigurationPublicIPAddressConfigurationArgsDict]
    ]
    subnet: NotRequired[pulumi.Input[SubResourceArgsDict]]

@pulumi.input_type
class IpConfigurationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        application_gateway_backend_address_pools: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]
        ] = ...,
        load_balancer_backend_address_pools: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]
        ] = ...,
        load_balancer_inbound_nat_pools: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]
        ] = ...,
        private_ip_address_version: Optional[
            pulumi.Input[Union[_builtins.str, PrivateIPAddressVersion]]
        ] = ...,
        public_ip_address_configuration: Optional[
            pulumi.Input[IpConfigurationPublicIPAddressConfigurationArgs]
        ] = ...,
        subnet: Optional[pulumi.Input[SubResourceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applicationGatewayBackendAddressPools")
    def application_gateway_backend_address_pools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]: ...
    @application_gateway_backend_address_pools.setter
    def application_gateway_backend_address_pools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerBackendAddressPools")
    def load_balancer_backend_address_pools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]: ...
    @load_balancer_backend_address_pools.setter
    def load_balancer_backend_address_pools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerInboundNatPools")
    def load_balancer_inbound_nat_pools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]: ...
    @load_balancer_inbound_nat_pools.setter
    def load_balancer_inbound_nat_pools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateIPAddressVersion")
    def private_ip_address_version(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PrivateIPAddressVersion]]]: ...
    @private_ip_address_version.setter
    def private_ip_address_version(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PrivateIPAddressVersion]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddressConfiguration")
    def public_ip_address_configuration(
        self,
    ) -> Optional[pulumi.Input[IpConfigurationPublicIPAddressConfigurationArgs]]: ...
    @public_ip_address_configuration.setter
    def public_ip_address_configuration(
        self,
        value: Optional[pulumi.Input[IpConfigurationPublicIPAddressConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...

class IpTagArgsDict(TypedDict):
    ip_tag_type: pulumi.Input[_builtins.str]
    tag: pulumi.Input[_builtins.str]

@pulumi.input_type
class IpTagArgs:
    def __init__(
        __self__,
        *,
        ip_tag_type: pulumi.Input[_builtins.str],
        tag: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipTagType")
    def ip_tag_type(self) -> pulumi.Input[_builtins.str]: ...
    @ip_tag_type.setter
    def ip_tag_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> pulumi.Input[_builtins.str]: ...
    @tag.setter
    def tag(self, value: pulumi.Input[_builtins.str]): ...

class LoadBalancingRuleArgsDict(TypedDict):
    backend_port: pulumi.Input[_builtins.int]
    frontend_port: pulumi.Input[_builtins.int]
    probe_protocol: pulumi.Input[Union[_builtins.str, ProbeProtocol]]
    protocol: pulumi.Input[Union[_builtins.str, Protocol]]
    load_distribution: NotRequired[pulumi.Input[_builtins.str]]
    probe_port: NotRequired[pulumi.Input[_builtins.int]]
    probe_request_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LoadBalancingRuleArgs:
    def __init__(
        __self__,
        *,
        backend_port: pulumi.Input[_builtins.int],
        frontend_port: pulumi.Input[_builtins.int],
        probe_protocol: pulumi.Input[Union[_builtins.str, ProbeProtocol]],
        protocol: pulumi.Input[Union[_builtins.str, Protocol]],
        load_distribution: Optional[pulumi.Input[_builtins.str]] = ...,
        probe_port: Optional[pulumi.Input[_builtins.int]] = ...,
        probe_request_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> pulumi.Input[_builtins.int]: ...
    @backend_port.setter
    def backend_port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> pulumi.Input[_builtins.int]: ...
    @frontend_port.setter
    def frontend_port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="probeProtocol")
    def probe_protocol(self) -> pulumi.Input[Union[_builtins.str, ProbeProtocol]]: ...
    @probe_protocol.setter
    def probe_protocol(
        self, value: pulumi.Input[Union[_builtins.str, ProbeProtocol]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[Union[_builtins.str, Protocol]]: ...
    @protocol.setter
    def protocol(self, value: pulumi.Input[Union[_builtins.str, Protocol]]): ...
    @_builtins.property
    @pulumi.getter(name="loadDistribution")
    def load_distribution(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_distribution.setter
    def load_distribution(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="probePort")
    def probe_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @probe_port.setter
    def probe_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="probeRequestPath")
    def probe_request_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @probe_request_path.setter
    def probe_request_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagedIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[ManagedIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ManagedIdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[ManagedIdentityType]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ManagedIdentityType]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[ManagedIdentityType]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class NamedPartitionSchemeArgsDict(TypedDict):
    names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    partition_scheme: pulumi.Input[_builtins.str]

@pulumi.input_type
class NamedPartitionSchemeArgs:
    def __init__(
        __self__,
        *,
        names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        partition_scheme: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def names(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @names.setter
    def names(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="partitionScheme")
    def partition_scheme(self) -> pulumi.Input[_builtins.str]: ...
    @partition_scheme.setter
    def partition_scheme(self, value: pulumi.Input[_builtins.str]): ...

class NetworkSecurityRuleArgsDict(TypedDict):
    access: pulumi.Input[Union[_builtins.str, Access]]
    direction: pulumi.Input[Union[_builtins.str, Direction]]
    name: pulumi.Input[_builtins.str]
    priority: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[Union[_builtins.str, NsgProtocol]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    destination_address_prefix: NotRequired[pulumi.Input[_builtins.str]]
    destination_address_prefixes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    destination_port_range: NotRequired[pulumi.Input[_builtins.str]]
    destination_port_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    source_address_prefix: NotRequired[pulumi.Input[_builtins.str]]
    source_address_prefixes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    source_port_range: NotRequired[pulumi.Input[_builtins.str]]
    source_port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class NetworkSecurityRuleArgs:
    def __init__(
        __self__,
        *,
        access: pulumi.Input[Union[_builtins.str, Access]],
        direction: pulumi.Input[Union[_builtins.str, Direction]],
        name: pulumi.Input[_builtins.str],
        priority: pulumi.Input[_builtins.int],
        protocol: pulumi.Input[Union[_builtins.str, NsgProtocol]],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_address_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_address_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        destination_port_range: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_port_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        source_address_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        source_address_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        source_port_range: Optional[pulumi.Input[_builtins.str]] = ...,
        source_port_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def access(self) -> pulumi.Input[Union[_builtins.str, Access]]: ...
    @access.setter
    def access(self, value: pulumi.Input[Union[_builtins.str, Access]]): ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> pulumi.Input[Union[_builtins.str, Direction]]: ...
    @direction.setter
    def direction(self, value: pulumi.Input[Union[_builtins.str, Direction]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[Union[_builtins.str, NsgProtocol]]: ...
    @protocol.setter
    def protocol(self, value: pulumi.Input[Union[_builtins.str, NsgProtocol]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationAddressPrefix")
    def destination_address_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_address_prefix.setter
    def destination_address_prefix(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationAddressPrefixes")
    def destination_address_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @destination_address_prefixes.setter
    def destination_address_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationPortRange")
    def destination_port_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_port_range.setter
    def destination_port_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @destination_port_ranges.setter
    def destination_port_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceAddressPrefix")
    def source_address_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_address_prefix.setter
    def source_address_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceAddressPrefixes")
    def source_address_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @source_address_prefixes.setter
    def source_address_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_port_range.setter
    def source_port_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @source_port_ranges.setter
    def source_port_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class NodeTypeNatConfigArgsDict(TypedDict):
    backend_port: NotRequired[pulumi.Input[_builtins.int]]
    frontend_port_range_end: NotRequired[pulumi.Input[_builtins.int]]
    frontend_port_range_start: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class NodeTypeNatConfigArgs:
    def __init__(
        __self__,
        *,
        backend_port: Optional[pulumi.Input[_builtins.int]] = ...,
        frontend_port_range_end: Optional[pulumi.Input[_builtins.int]] = ...,
        frontend_port_range_start: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @backend_port.setter
    def backend_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="frontendPortRangeEnd")
    def frontend_port_range_end(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @frontend_port_range_end.setter
    def frontend_port_range_end(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="frontendPortRangeStart")
    def frontend_port_range_start(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @frontend_port_range_start.setter
    def frontend_port_range_start(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class NodeTypeSkuArgsDict(TypedDict):
    capacity: pulumi.Input[_builtins.int]
    name: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NodeTypeSkuArgs:
    def __init__(
        __self__,
        *,
        capacity: pulumi.Input[_builtins.int],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> pulumi.Input[_builtins.int]: ...
    @capacity.setter
    def capacity(self, value: pulumi.Input[_builtins.int]): ...
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

class PartitionInstanceCountScaleMechanismArgsDict(TypedDict):
    kind: pulumi.Input[_builtins.str]
    max_instance_count: pulumi.Input[_builtins.int]
    min_instance_count: pulumi.Input[_builtins.int]
    scale_increment: pulumi.Input[_builtins.int]

@pulumi.input_type
class PartitionInstanceCountScaleMechanismArgs:
    def __init__(
        __self__,
        *,
        kind: pulumi.Input[_builtins.str],
        max_instance_count: pulumi.Input[_builtins.int],
        min_instance_count: pulumi.Input[_builtins.int],
        scale_increment: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> pulumi.Input[_builtins.int]: ...
    @max_instance_count.setter
    def max_instance_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> pulumi.Input[_builtins.int]: ...
    @min_instance_count.setter
    def min_instance_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="scaleIncrement")
    def scale_increment(self) -> pulumi.Input[_builtins.int]: ...
    @scale_increment.setter
    def scale_increment(self, value: pulumi.Input[_builtins.int]): ...

class RollingUpgradeMonitoringPolicyArgsDict(TypedDict):
    failure_action: pulumi.Input[Union[_builtins.str, FailureAction]]
    health_check_retry_timeout: pulumi.Input[_builtins.str]
    health_check_stable_duration: pulumi.Input[_builtins.str]
    health_check_wait_duration: pulumi.Input[_builtins.str]
    upgrade_domain_timeout: pulumi.Input[_builtins.str]
    upgrade_timeout: pulumi.Input[_builtins.str]

@pulumi.input_type
class RollingUpgradeMonitoringPolicyArgs:
    def __init__(
        __self__,
        *,
        failure_action: pulumi.Input[Union[_builtins.str, FailureAction]],
        health_check_retry_timeout: pulumi.Input[_builtins.str],
        health_check_stable_duration: pulumi.Input[_builtins.str],
        health_check_wait_duration: pulumi.Input[_builtins.str],
        upgrade_domain_timeout: pulumi.Input[_builtins.str],
        upgrade_timeout: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureAction")
    def failure_action(self) -> pulumi.Input[Union[_builtins.str, FailureAction]]: ...
    @failure_action.setter
    def failure_action(
        self, value: pulumi.Input[Union[_builtins.str, FailureAction]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckRetryTimeout")
    def health_check_retry_timeout(self) -> pulumi.Input[_builtins.str]: ...
    @health_check_retry_timeout.setter
    def health_check_retry_timeout(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckStableDuration")
    def health_check_stable_duration(self) -> pulumi.Input[_builtins.str]: ...
    @health_check_stable_duration.setter
    def health_check_stable_duration(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckWaitDuration")
    def health_check_wait_duration(self) -> pulumi.Input[_builtins.str]: ...
    @health_check_wait_duration.setter
    def health_check_wait_duration(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="upgradeDomainTimeout")
    def upgrade_domain_timeout(self) -> pulumi.Input[_builtins.str]: ...
    @upgrade_domain_timeout.setter
    def upgrade_domain_timeout(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="upgradeTimeout")
    def upgrade_timeout(self) -> pulumi.Input[_builtins.str]: ...
    @upgrade_timeout.setter
    def upgrade_timeout(self, value: pulumi.Input[_builtins.str]): ...

class ScalingPolicyArgsDict(TypedDict):
    scaling_mechanism: pulumi.Input[
        Union[
            AddRemoveIncrementalNamedPartitionScalingMechanismArgsDict,
            PartitionInstanceCountScaleMechanismArgsDict,
        ]
    ]
    scaling_trigger: pulumi.Input[
        Union[
            AveragePartitionLoadScalingTriggerArgsDict,
            AverageServiceLoadScalingTriggerArgsDict,
        ]
    ]

@pulumi.input_type
class ScalingPolicyArgs:
    def __init__(
        __self__,
        *,
        scaling_mechanism: pulumi.Input[
            Union[
                AddRemoveIncrementalNamedPartitionScalingMechanismArgs,
                PartitionInstanceCountScaleMechanismArgs,
            ]
        ],
        scaling_trigger: pulumi.Input[
            Union[
                AveragePartitionLoadScalingTriggerArgs,
                AverageServiceLoadScalingTriggerArgs,
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scalingMechanism")
    def scaling_mechanism(
        self,
    ) -> pulumi.Input[
        Union[
            AddRemoveIncrementalNamedPartitionScalingMechanismArgs,
            PartitionInstanceCountScaleMechanismArgs,
        ]
    ]: ...
    @scaling_mechanism.setter
    def scaling_mechanism(
        self,
        value: pulumi.Input[
            Union[
                AddRemoveIncrementalNamedPartitionScalingMechanismArgs,
                PartitionInstanceCountScaleMechanismArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scalingTrigger")
    def scaling_trigger(
        self,
    ) -> pulumi.Input[
        Union[
            AveragePartitionLoadScalingTriggerArgs, AverageServiceLoadScalingTriggerArgs
        ]
    ]: ...
    @scaling_trigger.setter
    def scaling_trigger(
        self,
        value: pulumi.Input[
            Union[
                AveragePartitionLoadScalingTriggerArgs,
                AverageServiceLoadScalingTriggerArgs,
            ]
        ],
    ): ...

class ServiceCorrelationArgsDict(TypedDict):
    scheme: pulumi.Input[Union[_builtins.str, ServiceCorrelationScheme]]
    service_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServiceCorrelationArgs:
    def __init__(
        __self__,
        *,
        scheme: pulumi.Input[Union[_builtins.str, ServiceCorrelationScheme]],
        service_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scheme(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ServiceCorrelationScheme]]: ...
    @scheme.setter
    def scheme(
        self, value: pulumi.Input[Union[_builtins.str, ServiceCorrelationScheme]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...

class ServiceEndpointArgsDict(TypedDict):
    service: pulumi.Input[_builtins.str]
    locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServiceEndpointArgs:
    def __init__(
        __self__,
        *,
        service: pulumi.Input[_builtins.str],
        locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @locations.setter
    def locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServiceLoadMetricArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    default_load: NotRequired[pulumi.Input[_builtins.int]]
    primary_default_load: NotRequired[pulumi.Input[_builtins.int]]
    secondary_default_load: NotRequired[pulumi.Input[_builtins.int]]
    weight: NotRequired[pulumi.Input[Union[_builtins.str, ServiceLoadMetricWeight]]]

@pulumi.input_type
class ServiceLoadMetricArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        default_load: Optional[pulumi.Input[_builtins.int]] = ...,
        primary_default_load: Optional[pulumi.Input[_builtins.int]] = ...,
        secondary_default_load: Optional[pulumi.Input[_builtins.int]] = ...,
        weight: Optional[
            pulumi.Input[Union[_builtins.str, ServiceLoadMetricWeight]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultLoad")
    def default_load(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_load.setter
    def default_load(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryDefaultLoad")
    def primary_default_load(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @primary_default_load.setter
    def primary_default_load(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryDefaultLoad")
    def secondary_default_load(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @secondary_default_load.setter
    def secondary_default_load(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ServiceLoadMetricWeight]]]: ...
    @weight.setter
    def weight(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ServiceLoadMetricWeight]]],
    ): ...

class ServicePlacementInvalidDomainPolicyArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServicePlacementInvalidDomainPolicyArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class ServicePlacementNonPartiallyPlaceServicePolicyArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServicePlacementNonPartiallyPlaceServicePolicyArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class ServicePlacementPreferPrimaryDomainPolicyArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServicePlacementPreferPrimaryDomainPolicyArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class ServicePlacementRequireDomainDistributionPolicyArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServicePlacementRequireDomainDistributionPolicyArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class ServicePlacementRequiredDomainPolicyArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServicePlacementRequiredDomainPolicyArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class ServiceTypeHealthPolicyArgsDict(TypedDict):
    max_percent_unhealthy_partitions_per_service: pulumi.Input[_builtins.int]
    max_percent_unhealthy_replicas_per_partition: pulumi.Input[_builtins.int]
    max_percent_unhealthy_services: pulumi.Input[_builtins.int]

@pulumi.input_type
class ServiceTypeHealthPolicyArgs:
    def __init__(
        __self__,
        *,
        max_percent_unhealthy_partitions_per_service: pulumi.Input[_builtins.int],
        max_percent_unhealthy_replicas_per_partition: pulumi.Input[_builtins.int],
        max_percent_unhealthy_services: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPercentUnhealthyPartitionsPerService")
    def max_percent_unhealthy_partitions_per_service(
        self,
    ) -> pulumi.Input[_builtins.int]: ...
    @max_percent_unhealthy_partitions_per_service.setter
    def max_percent_unhealthy_partitions_per_service(
        self, value: pulumi.Input[_builtins.int]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxPercentUnhealthyReplicasPerPartition")
    def max_percent_unhealthy_replicas_per_partition(
        self,
    ) -> pulumi.Input[_builtins.int]: ...
    @max_percent_unhealthy_replicas_per_partition.setter
    def max_percent_unhealthy_replicas_per_partition(
        self, value: pulumi.Input[_builtins.int]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxPercentUnhealthyServices")
    def max_percent_unhealthy_services(self) -> pulumi.Input[_builtins.int]: ...
    @max_percent_unhealthy_services.setter
    def max_percent_unhealthy_services(self, value: pulumi.Input[_builtins.int]): ...

class SettingsParameterDescriptionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class SettingsParameterDescriptionArgs:
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

class SettingsSectionDescriptionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[
        Sequence[pulumi.Input[SettingsParameterDescriptionArgsDict]]
    ]

@pulumi.input_type
class SettingsSectionDescriptionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        parameters: pulumi.Input[
            Sequence[pulumi.Input[SettingsParameterDescriptionArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[SettingsParameterDescriptionArgs]]]: ...
    @parameters.setter
    def parameters(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[SettingsParameterDescriptionArgs]]],
    ): ...

class SingletonPartitionSchemeArgsDict(TypedDict):
    partition_scheme: pulumi.Input[_builtins.str]

@pulumi.input_type
class SingletonPartitionSchemeArgs:
    def __init__(
        __self__, *, partition_scheme: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionScheme")
    def partition_scheme(self) -> pulumi.Input[_builtins.str]: ...
    @partition_scheme.setter
    def partition_scheme(self, value: pulumi.Input[_builtins.str]): ...

class SkuArgsDict(TypedDict):
    name: pulumi.Input[Union[_builtins.str, SkuName]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__, *, name: pulumi.Input[Union[_builtins.str, SkuName]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, SkuName]]: ...
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, SkuName]]): ...

class StatefulServicePropertiesArgsDict(TypedDict):
    partition_description: pulumi.Input[
        Union[
            NamedPartitionSchemeArgsDict,
            SingletonPartitionSchemeArgsDict,
            UniformInt64RangePartitionSchemeArgsDict,
        ]
    ]
    service_kind: pulumi.Input[_builtins.str]
    service_type_name: pulumi.Input[_builtins.str]
    correlation_scheme: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceCorrelationArgsDict]]]
    ]
    default_move_cost: NotRequired[pulumi.Input[Union[_builtins.str, MoveCost]]]
    has_persisted_state: NotRequired[pulumi.Input[_builtins.bool]]
    min_replica_set_size: NotRequired[pulumi.Input[_builtins.int]]
    placement_constraints: NotRequired[pulumi.Input[_builtins.str]]
    quorum_loss_wait_duration: NotRequired[pulumi.Input[_builtins.str]]
    replica_restart_wait_duration: NotRequired[pulumi.Input[_builtins.str]]
    scaling_policies: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ScalingPolicyArgsDict]]]
    ]
    service_dns_name: NotRequired[pulumi.Input[_builtins.str]]
    service_load_metrics: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceLoadMetricArgsDict]]]
    ]
    service_package_activation_mode: NotRequired[
        pulumi.Input[Union[_builtins.str, ServicePackageActivationMode]]
    ]
    service_placement_policies: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        ServicePlacementInvalidDomainPolicyArgsDict,
                        ServicePlacementNonPartiallyPlaceServicePolicyArgsDict,
                        ServicePlacementPreferPrimaryDomainPolicyArgsDict,
                        ServicePlacementRequireDomainDistributionPolicyArgsDict,
                        ServicePlacementRequiredDomainPolicyArgsDict,
                    ]
                ]
            ]
        ]
    ]
    service_placement_time_limit: NotRequired[pulumi.Input[_builtins.str]]
    stand_by_replica_keep_duration: NotRequired[pulumi.Input[_builtins.str]]
    target_replica_set_size: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class StatefulServicePropertiesArgs:
    def __init__(
        __self__,
        *,
        partition_description: pulumi.Input[
            Union[
                NamedPartitionSchemeArgs,
                SingletonPartitionSchemeArgs,
                UniformInt64RangePartitionSchemeArgs,
            ]
        ],
        service_kind: pulumi.Input[_builtins.str],
        service_type_name: pulumi.Input[_builtins.str],
        correlation_scheme: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceCorrelationArgs]]]
        ] = ...,
        default_move_cost: Optional[pulumi.Input[Union[_builtins.str, MoveCost]]] = ...,
        has_persisted_state: Optional[pulumi.Input[_builtins.bool]] = ...,
        min_replica_set_size: Optional[pulumi.Input[_builtins.int]] = ...,
        placement_constraints: Optional[pulumi.Input[_builtins.str]] = ...,
        quorum_loss_wait_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_restart_wait_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[ScalingPolicyArgs]]]
        ] = ...,
        service_dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_load_metrics: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceLoadMetricArgs]]]
        ] = ...,
        service_package_activation_mode: Optional[
            pulumi.Input[Union[_builtins.str, ServicePackageActivationMode]]
        ] = ...,
        service_placement_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ServicePlacementInvalidDomainPolicyArgs,
                            ServicePlacementNonPartiallyPlaceServicePolicyArgs,
                            ServicePlacementPreferPrimaryDomainPolicyArgs,
                            ServicePlacementRequireDomainDistributionPolicyArgs,
                            ServicePlacementRequiredDomainPolicyArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        service_placement_time_limit: Optional[pulumi.Input[_builtins.str]] = ...,
        stand_by_replica_keep_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        target_replica_set_size: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionDescription")
    def partition_description(
        self,
    ) -> pulumi.Input[
        Union[
            NamedPartitionSchemeArgs,
            SingletonPartitionSchemeArgs,
            UniformInt64RangePartitionSchemeArgs,
        ]
    ]: ...
    @partition_description.setter
    def partition_description(
        self,
        value: pulumi.Input[
            Union[
                NamedPartitionSchemeArgs,
                SingletonPartitionSchemeArgs,
                UniformInt64RangePartitionSchemeArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceKind")
    def service_kind(self) -> pulumi.Input[_builtins.str]: ...
    @service_kind.setter
    def service_kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceTypeName")
    def service_type_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_type_name.setter
    def service_type_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="correlationScheme")
    def correlation_scheme(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceCorrelationArgs]]]]: ...
    @correlation_scheme.setter
    def correlation_scheme(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceCorrelationArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultMoveCost")
    def default_move_cost(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MoveCost]]]: ...
    @default_move_cost.setter
    def default_move_cost(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MoveCost]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hasPersistedState")
    def has_persisted_state(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @has_persisted_state.setter
    def has_persisted_state(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="minReplicaSetSize")
    def min_replica_set_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_replica_set_size.setter
    def min_replica_set_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @placement_constraints.setter
    def placement_constraints(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quorumLossWaitDuration")
    def quorum_loss_wait_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quorum_loss_wait_duration.setter
    def quorum_loss_wait_duration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicaRestartWaitDuration")
    def replica_restart_wait_duration(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replica_restart_wait_duration.setter
    def replica_restart_wait_duration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scalingPolicies")
    def scaling_policies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScalingPolicyArgs]]]]: ...
    @scaling_policies.setter
    def scaling_policies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScalingPolicyArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_dns_name.setter
    def service_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceLoadMetrics")
    def service_load_metrics(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceLoadMetricArgs]]]]: ...
    @service_load_metrics.setter
    def service_load_metrics(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceLoadMetricArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="servicePackageActivationMode")
    def service_package_activation_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ServicePackageActivationMode]]]: ...
    @service_package_activation_mode.setter
    def service_package_activation_mode(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ServicePackageActivationMode]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="servicePlacementPolicies")
    def service_placement_policies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        ServicePlacementInvalidDomainPolicyArgs,
                        ServicePlacementNonPartiallyPlaceServicePolicyArgs,
                        ServicePlacementPreferPrimaryDomainPolicyArgs,
                        ServicePlacementRequireDomainDistributionPolicyArgs,
                        ServicePlacementRequiredDomainPolicyArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @service_placement_policies.setter
    def service_placement_policies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ServicePlacementInvalidDomainPolicyArgs,
                            ServicePlacementNonPartiallyPlaceServicePolicyArgs,
                            ServicePlacementPreferPrimaryDomainPolicyArgs,
                            ServicePlacementRequireDomainDistributionPolicyArgs,
                            ServicePlacementRequiredDomainPolicyArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="servicePlacementTimeLimit")
    def service_placement_time_limit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_placement_time_limit.setter
    def service_placement_time_limit(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="standByReplicaKeepDuration")
    def stand_by_replica_keep_duration(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stand_by_replica_keep_duration.setter
    def stand_by_replica_keep_duration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetReplicaSetSize")
    def target_replica_set_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_replica_set_size.setter
    def target_replica_set_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class StatelessServicePropertiesArgsDict(TypedDict):
    instance_count: pulumi.Input[_builtins.int]
    partition_description: pulumi.Input[
        Union[
            NamedPartitionSchemeArgsDict,
            SingletonPartitionSchemeArgsDict,
            UniformInt64RangePartitionSchemeArgsDict,
        ]
    ]
    service_kind: pulumi.Input[_builtins.str]
    service_type_name: pulumi.Input[_builtins.str]
    correlation_scheme: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceCorrelationArgsDict]]]
    ]
    default_move_cost: NotRequired[pulumi.Input[Union[_builtins.str, MoveCost]]]
    min_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    min_instance_percentage: NotRequired[pulumi.Input[_builtins.int]]
    placement_constraints: NotRequired[pulumi.Input[_builtins.str]]
    scaling_policies: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ScalingPolicyArgsDict]]]
    ]
    service_dns_name: NotRequired[pulumi.Input[_builtins.str]]
    service_load_metrics: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceLoadMetricArgsDict]]]
    ]
    service_package_activation_mode: NotRequired[
        pulumi.Input[Union[_builtins.str, ServicePackageActivationMode]]
    ]
    service_placement_policies: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        ServicePlacementInvalidDomainPolicyArgsDict,
                        ServicePlacementNonPartiallyPlaceServicePolicyArgsDict,
                        ServicePlacementPreferPrimaryDomainPolicyArgsDict,
                        ServicePlacementRequireDomainDistributionPolicyArgsDict,
                        ServicePlacementRequiredDomainPolicyArgsDict,
                    ]
                ]
            ]
        ]
    ]

@pulumi.input_type
class StatelessServicePropertiesArgs:
    def __init__(
        __self__,
        *,
        instance_count: pulumi.Input[_builtins.int],
        partition_description: pulumi.Input[
            Union[
                NamedPartitionSchemeArgs,
                SingletonPartitionSchemeArgs,
                UniformInt64RangePartitionSchemeArgs,
            ]
        ],
        service_kind: pulumi.Input[_builtins.str],
        service_type_name: pulumi.Input[_builtins.str],
        correlation_scheme: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceCorrelationArgs]]]
        ] = ...,
        default_move_cost: Optional[pulumi.Input[Union[_builtins.str, MoveCost]]] = ...,
        min_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_instance_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        placement_constraints: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[ScalingPolicyArgs]]]
        ] = ...,
        service_dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_load_metrics: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceLoadMetricArgs]]]
        ] = ...,
        service_package_activation_mode: Optional[
            pulumi.Input[Union[_builtins.str, ServicePackageActivationMode]]
        ] = ...,
        service_placement_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ServicePlacementInvalidDomainPolicyArgs,
                            ServicePlacementNonPartiallyPlaceServicePolicyArgs,
                            ServicePlacementPreferPrimaryDomainPolicyArgs,
                            ServicePlacementRequireDomainDistributionPolicyArgs,
                            ServicePlacementRequiredDomainPolicyArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> pulumi.Input[_builtins.int]: ...
    @instance_count.setter
    def instance_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="partitionDescription")
    def partition_description(
        self,
    ) -> pulumi.Input[
        Union[
            NamedPartitionSchemeArgs,
            SingletonPartitionSchemeArgs,
            UniformInt64RangePartitionSchemeArgs,
        ]
    ]: ...
    @partition_description.setter
    def partition_description(
        self,
        value: pulumi.Input[
            Union[
                NamedPartitionSchemeArgs,
                SingletonPartitionSchemeArgs,
                UniformInt64RangePartitionSchemeArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceKind")
    def service_kind(self) -> pulumi.Input[_builtins.str]: ...
    @service_kind.setter
    def service_kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceTypeName")
    def service_type_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_type_name.setter
    def service_type_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="correlationScheme")
    def correlation_scheme(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceCorrelationArgs]]]]: ...
    @correlation_scheme.setter
    def correlation_scheme(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceCorrelationArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultMoveCost")
    def default_move_cost(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MoveCost]]]: ...
    @default_move_cost.setter
    def default_move_cost(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MoveCost]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_instance_count.setter
    def min_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minInstancePercentage")
    def min_instance_percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_instance_percentage.setter
    def min_instance_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @placement_constraints.setter
    def placement_constraints(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingPolicies")
    def scaling_policies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScalingPolicyArgs]]]]: ...
    @scaling_policies.setter
    def scaling_policies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScalingPolicyArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_dns_name.setter
    def service_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceLoadMetrics")
    def service_load_metrics(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceLoadMetricArgs]]]]: ...
    @service_load_metrics.setter
    def service_load_metrics(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceLoadMetricArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="servicePackageActivationMode")
    def service_package_activation_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ServicePackageActivationMode]]]: ...
    @service_package_activation_mode.setter
    def service_package_activation_mode(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ServicePackageActivationMode]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="servicePlacementPolicies")
    def service_placement_policies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        ServicePlacementInvalidDomainPolicyArgs,
                        ServicePlacementNonPartiallyPlaceServicePolicyArgs,
                        ServicePlacementPreferPrimaryDomainPolicyArgs,
                        ServicePlacementRequireDomainDistributionPolicyArgs,
                        ServicePlacementRequiredDomainPolicyArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @service_placement_policies.setter
    def service_placement_policies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ServicePlacementInvalidDomainPolicyArgs,
                            ServicePlacementNonPartiallyPlaceServicePolicyArgs,
                            ServicePlacementPreferPrimaryDomainPolicyArgs,
                            ServicePlacementRequireDomainDistributionPolicyArgs,
                            ServicePlacementRequiredDomainPolicyArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...

class SubResourceArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SubResourceArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SubnetArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    enable_ipv6: NotRequired[pulumi.Input[_builtins.bool]]
    network_security_group_id: NotRequired[pulumi.Input[_builtins.str]]
    private_endpoint_network_policies: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateEndpointNetworkPolicies]]
    ]
    private_link_service_network_policies: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateLinkServiceNetworkPolicies]]
    ]

@pulumi.input_type
class SubnetArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        enable_ipv6: Optional[pulumi.Input[_builtins.bool]] = ...,
        network_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        private_endpoint_network_policies: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointNetworkPolicies]]
        ] = ...,
        private_link_service_network_policies: Optional[
            pulumi.Input[Union[_builtins.str, PrivateLinkServiceNetworkPolicies]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="enableIpv6")
    def enable_ipv6(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_ipv6.setter
    def enable_ipv6(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroupId")
    def network_security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_security_group_id.setter
    def network_security_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointNetworkPolicies")
    def private_endpoint_network_policies(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, PrivateEndpointNetworkPolicies]]
    ]: ...
    @private_endpoint_network_policies.setter
    def private_endpoint_network_policies(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointNetworkPolicies]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceNetworkPolicies")
    def private_link_service_network_policies(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, PrivateLinkServiceNetworkPolicies]]
    ]: ...
    @private_link_service_network_policies.setter
    def private_link_service_network_policies(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateLinkServiceNetworkPolicies]]
        ],
    ): ...

class UniformInt64RangePartitionSchemeArgsDict(TypedDict):
    count: pulumi.Input[_builtins.int]
    high_key: pulumi.Input[_builtins.float]
    low_key: pulumi.Input[_builtins.float]
    partition_scheme: pulumi.Input[_builtins.str]

@pulumi.input_type
class UniformInt64RangePartitionSchemeArgs:
    def __init__(
        __self__,
        *,
        count: pulumi.Input[_builtins.int],
        high_key: pulumi.Input[_builtins.float],
        low_key: pulumi.Input[_builtins.float],
        partition_scheme: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> pulumi.Input[_builtins.int]: ...
    @count.setter
    def count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="highKey")
    def high_key(self) -> pulumi.Input[_builtins.float]: ...
    @high_key.setter
    def high_key(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="lowKey")
    def low_key(self) -> pulumi.Input[_builtins.float]: ...
    @low_key.setter
    def low_key(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="partitionScheme")
    def partition_scheme(self) -> pulumi.Input[_builtins.str]: ...
    @partition_scheme.setter
    def partition_scheme(self, value: pulumi.Input[_builtins.str]): ...

class VMSSExtensionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    publisher: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    type_handler_version: pulumi.Input[_builtins.str]
    auto_upgrade_minor_version: NotRequired[pulumi.Input[_builtins.bool]]
    enable_automatic_upgrade: NotRequired[pulumi.Input[_builtins.bool]]
    force_update_tag: NotRequired[pulumi.Input[_builtins.str]]
    protected_settings: NotRequired[Any]
    provision_after_extensions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    settings: NotRequired[Any]
    setup_order: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, VmssExtensionSetupOrder]]]
        ]
    ]

@pulumi.input_type
class VMSSExtensionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        publisher: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        type_handler_version: pulumi.Input[_builtins.str],
        auto_upgrade_minor_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_automatic_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        force_update_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_settings: Optional[Any] = ...,
        provision_after_extensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        settings: Optional[Any] = ...,
        setup_order: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, VmssExtensionSetupOrder]]]
            ]
        ] = ...,
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
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> pulumi.Input[_builtins.str]: ...
    @type_handler_version.setter
    def type_handler_version(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @force_update_tag.setter
    def force_update_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="setupOrder")
    def setup_order(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, VmssExtensionSetupOrder]]]
        ]
    ]: ...
    @setup_order.setter
    def setup_order(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, VmssExtensionSetupOrder]]]
            ]
        ],
    ): ...

class VaultCertificateArgsDict(TypedDict):
    certificate_store: pulumi.Input[_builtins.str]
    certificate_url: pulumi.Input[_builtins.str]

@pulumi.input_type
class VaultCertificateArgs:
    def __init__(
        __self__,
        *,
        certificate_store: pulumi.Input[_builtins.str],
        certificate_url: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateStore")
    def certificate_store(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_store.setter
    def certificate_store(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_url.setter
    def certificate_url(self, value: pulumi.Input[_builtins.str]): ...

class VaultSecretGroupArgsDict(TypedDict):
    source_vault: pulumi.Input[SubResourceArgsDict]
    vault_certificates: pulumi.Input[Sequence[pulumi.Input[VaultCertificateArgsDict]]]

@pulumi.input_type
class VaultSecretGroupArgs:
    def __init__(
        __self__,
        *,
        source_vault: pulumi.Input[SubResourceArgs],
        vault_certificates: pulumi.Input[Sequence[pulumi.Input[VaultCertificateArgs]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> pulumi.Input[SubResourceArgs]: ...
    @source_vault.setter
    def source_vault(self, value: pulumi.Input[SubResourceArgs]): ...
    @_builtins.property
    @pulumi.getter(name="vaultCertificates")
    def vault_certificates(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[VaultCertificateArgs]]]: ...
    @vault_certificates.setter
    def vault_certificates(
        self, value: pulumi.Input[Sequence[pulumi.Input[VaultCertificateArgs]]]
    ): ...

class VmImagePlanArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    product: NotRequired[pulumi.Input[_builtins.str]]
    promotion_code: NotRequired[pulumi.Input[_builtins.str]]
    publisher: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VmImagePlanArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        product: Optional[pulumi.Input[_builtins.str]] = ...,
        promotion_code: Optional[pulumi.Input[_builtins.str]] = ...,
        publisher: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def product(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @product.setter
    def product(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @promotion_code.setter
    def promotion_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VmManagedIdentityArgsDict(TypedDict):
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class VmManagedIdentityArgs:
    def __init__(
        __self__,
        *,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class VmssDataDiskArgsDict(TypedDict):
    disk_letter: pulumi.Input[_builtins.str]
    disk_size_gb: pulumi.Input[_builtins.int]
    disk_type: pulumi.Input[Union[_builtins.str, DiskType]]
    lun: pulumi.Input[_builtins.int]

@pulumi.input_type
class VmssDataDiskArgs:
    def __init__(
        __self__,
        *,
        disk_letter: pulumi.Input[_builtins.str],
        disk_size_gb: pulumi.Input[_builtins.int],
        disk_type: pulumi.Input[Union[_builtins.str, DiskType]],
        lun: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskLetter")
    def disk_letter(self) -> pulumi.Input[_builtins.str]: ...
    @disk_letter.setter
    def disk_letter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> pulumi.Input[_builtins.int]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> pulumi.Input[Union[_builtins.str, DiskType]]: ...
    @disk_type.setter
    def disk_type(self, value: pulumi.Input[Union[_builtins.str, DiskType]]): ...
    @_builtins.property
    @pulumi.getter
    def lun(self) -> pulumi.Input[_builtins.int]: ...
    @lun.setter
    def lun(self, value: pulumi.Input[_builtins.int]): ...
