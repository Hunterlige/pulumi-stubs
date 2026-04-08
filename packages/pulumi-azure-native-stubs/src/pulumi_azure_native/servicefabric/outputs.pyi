import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    ...,
    "AdditionalNetworkInterfaceConfigurationResponse",
    "ApplicationHealthPolicyResponse",
    "ApplicationTypeVersionsCleanupPolicyResponse",
    "ApplicationUpgradePolicyResponse",
    "ApplicationUserAssignedIdentityResponse",
    "AveragePartitionLoadScalingTriggerResponse",
    "AverageServiceLoadScalingTriggerResponse",
    "AzureActiveDirectoryResponse",
    "ClientCertificateResponse",
    "ClusterHealthPolicyResponse",
    "ClusterMonitoringPolicyResponse",
    "ClusterUpgradeDeltaHealthPolicyResponse",
    "ClusterUpgradePolicyResponse",
    "EndpointRangeDescriptionResponse",
    "FaultSimulationConstraintsResponse",
    "FaultSimulationDetailsResponse",
    "FaultSimulationResponse",
    "FrontendConfigurationResponse",
    "IpConfigurationResponse",
    ...,
    "IpTagResponse",
    "LoadBalancingRuleResponse",
    "ManagedIdentityResponse",
    "NamedPartitionSchemeResponse",
    "NetworkSecurityRuleResponse",
    "NodeTypeFaultSimulationResponse",
    "NodeTypeNatConfigResponse",
    "NodeTypeSkuResponse",
    "PartitionInstanceCountScaleMechanismResponse",
    "ResourceAzStatusResponse",
    "RollingUpgradeMonitoringPolicyResponse",
    "ScalingPolicyResponse",
    "ServiceCorrelationResponse",
    "ServiceEndpointResponse",
    "ServiceLoadMetricResponse",
    "ServicePlacementInvalidDomainPolicyResponse",
    ...,
    "ServicePlacementPreferPrimaryDomainPolicyResponse",
    ...,
    "ServicePlacementRequiredDomainPolicyResponse",
    "ServiceTypeHealthPolicyResponse",
    "SettingsParameterDescriptionResponse",
    "SettingsSectionDescriptionResponse",
    "SingletonPartitionSchemeResponse",
    "SkuResponse",
    "StatefulServicePropertiesResponse",
    "StatelessServicePropertiesResponse",
    "SubResourceResponse",
    "SubnetResponse",
    "SystemDataResponse",
    "UniformInt64RangePartitionSchemeResponse",
    "UserAssignedIdentityResponse",
    "VMSSExtensionResponse",
    "VaultCertificateResponse",
    "VaultSecretGroupResponse",
    "VmImagePlanResponse",
    "VmManagedIdentityResponse",
    "VmssDataDiskResponse",
    "ZoneFaultSimulationContentResponse",
]

@pulumi.output_type
class AddRemoveIncrementalNamedPartitionScalingMechanismResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kind: _builtins.str,
        max_partition_count: _builtins.int,
        min_partition_count: _builtins.int,
        scale_increment: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxPartitionCount")
    def max_partition_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minPartitionCount")
    def min_partition_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="scaleIncrement")
    def scale_increment(self) -> _builtins.int: ...

@pulumi.output_type
class AdditionalNetworkInterfaceConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ip_configurations: Sequence[outputs.IpConfigurationResponse],
        name: _builtins.str,
        dscp_configuration: Optional[outputs.SubResourceResponse] = ...,
        enable_accelerated_networking: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Sequence[outputs.IpConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dscpConfiguration")
    def dscp_configuration(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ApplicationHealthPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        consider_warning_as_error: _builtins.bool,
        max_percent_unhealthy_deployed_applications: _builtins.int,
        default_service_type_health_policy: Optional[
            outputs.ServiceTypeHealthPolicyResponse
        ] = ...,
        service_type_health_policy_map: Optional[
            Mapping[str, outputs.ServiceTypeHealthPolicyResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="considerWarningAsError")
    def consider_warning_as_error(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="maxPercentUnhealthyDeployedApplications")
    def max_percent_unhealthy_deployed_applications(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="defaultServiceTypeHealthPolicy")
    def default_service_type_health_policy(
        self,
    ) -> Optional[outputs.ServiceTypeHealthPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="serviceTypeHealthPolicyMap")
    def service_type_health_policy_map(
        self,
    ) -> Optional[Mapping[str, outputs.ServiceTypeHealthPolicyResponse]]: ...

@pulumi.output_type
class ApplicationTypeVersionsCleanupPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, max_unused_versions_to_keep: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxUnusedVersionsToKeep")
    def max_unused_versions_to_keep(self) -> _builtins.int: ...

@pulumi.output_type
class ApplicationUpgradePolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        application_health_policy: Optional[
            outputs.ApplicationHealthPolicyResponse
        ] = ...,
        force_restart: Optional[_builtins.bool] = ...,
        instance_close_delay_duration: Optional[_builtins.float] = ...,
        recreate_application: Optional[_builtins.bool] = ...,
        rolling_upgrade_monitoring_policy: Optional[
            outputs.RollingUpgradeMonitoringPolicyResponse
        ] = ...,
        upgrade_mode: Optional[_builtins.str] = ...,
        upgrade_replica_set_check_timeout: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationHealthPolicy")
    def application_health_policy(
        self,
    ) -> Optional[outputs.ApplicationHealthPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="forceRestart")
    def force_restart(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="instanceCloseDelayDuration")
    def instance_close_delay_duration(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="recreateApplication")
    def recreate_application(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="rollingUpgradeMonitoringPolicy")
    def rolling_upgrade_monitoring_policy(
        self,
    ) -> Optional[outputs.RollingUpgradeMonitoringPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="upgradeMode")
    def upgrade_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="upgradeReplicaSetCheckTimeout")
    def upgrade_replica_set_check_timeout(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class ApplicationUserAssignedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, name: _builtins.str, principal_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...

@pulumi.output_type
class AveragePartitionLoadScalingTriggerResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kind: _builtins.str,
        lower_load_threshold: _builtins.float,
        metric_name: _builtins.str,
        scale_interval: _builtins.str,
        upper_load_threshold: _builtins.float,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lowerLoadThreshold")
    def lower_load_threshold(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scaleInterval")
    def scale_interval(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="upperLoadThreshold")
    def upper_load_threshold(self) -> _builtins.float: ...

@pulumi.output_type
class AverageServiceLoadScalingTriggerResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kind: _builtins.str,
        lower_load_threshold: _builtins.float,
        metric_name: _builtins.str,
        scale_interval: _builtins.str,
        upper_load_threshold: _builtins.float,
        use_only_primary_load: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lowerLoadThreshold")
    def lower_load_threshold(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scaleInterval")
    def scale_interval(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="upperLoadThreshold")
    def upper_load_threshold(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="useOnlyPrimaryLoad")
    def use_only_primary_load(self) -> _builtins.bool: ...

@pulumi.output_type
class AzureActiveDirectoryResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_application: Optional[_builtins.str] = ...,
        cluster_application: Optional[_builtins.str] = ...,
        tenant_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientApplication")
    def client_application(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterApplication")
    def cluster_application(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClientCertificateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_admin: _builtins.bool,
        common_name: Optional[_builtins.str] = ...,
        issuer_thumbprint: Optional[_builtins.str] = ...,
        thumbprint: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isAdmin")
    def is_admin(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="issuerThumbprint")
    def issuer_thumbprint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterHealthPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_percent_unhealthy_applications: Optional[_builtins.int] = ...,
        max_percent_unhealthy_nodes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPercentUnhealthyApplications")
    def max_percent_unhealthy_applications(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxPercentUnhealthyNodes")
    def max_percent_unhealthy_nodes(self) -> _builtins.int: ...

@pulumi.output_type
class ClusterMonitoringPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        health_check_retry_timeout: _builtins.str,
        health_check_stable_duration: _builtins.str,
        health_check_wait_duration: _builtins.str,
        upgrade_domain_timeout: _builtins.str,
        upgrade_timeout: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckRetryTimeout")
    def health_check_retry_timeout(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckStableDuration")
    def health_check_stable_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckWaitDuration")
    def health_check_wait_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="upgradeDomainTimeout")
    def upgrade_domain_timeout(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="upgradeTimeout")
    def upgrade_timeout(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterUpgradeDeltaHealthPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_percent_delta_unhealthy_nodes: _builtins.int,
        max_percent_delta_unhealthy_applications: Optional[_builtins.int] = ...,
        max_percent_upgrade_domain_delta_unhealthy_nodes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPercentDeltaUnhealthyNodes")
    def max_percent_delta_unhealthy_nodes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxPercentDeltaUnhealthyApplications")
    def max_percent_delta_unhealthy_applications(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxPercentUpgradeDomainDeltaUnhealthyNodes")
    def max_percent_upgrade_domain_delta_unhealthy_nodes(
        self,
    ) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterUpgradePolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        delta_health_policy: Optional[
            outputs.ClusterUpgradeDeltaHealthPolicyResponse
        ] = ...,
        force_restart: Optional[_builtins.bool] = ...,
        health_policy: Optional[outputs.ClusterHealthPolicyResponse] = ...,
        monitoring_policy: Optional[outputs.ClusterMonitoringPolicyResponse] = ...,
        upgrade_replica_set_check_timeout: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deltaHealthPolicy")
    def delta_health_policy(
        self,
    ) -> Optional[outputs.ClusterUpgradeDeltaHealthPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="forceRestart")
    def force_restart(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="healthPolicy")
    def health_policy(self) -> Optional[outputs.ClusterHealthPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringPolicy")
    def monitoring_policy(
        self,
    ) -> Optional[outputs.ClusterMonitoringPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="upgradeReplicaSetCheckTimeout")
    def upgrade_replica_set_check_timeout(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EndpointRangeDescriptionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, end_port: _builtins.int, start_port: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endPort")
    def end_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="startPort")
    def start_port(self) -> _builtins.int: ...

@pulumi.output_type
class FaultSimulationConstraintsResponse(dict):
    def __init__(
        __self__, *, expiration_time: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FaultSimulationDetailsResponse(dict):
    def __init__(
        __self__,
        *,
        cluster_id: Optional[_builtins.str] = ...,
        node_type_fault_simulation: Optional[
            Sequence[outputs.NodeTypeFaultSimulationResponse]
        ] = ...,
        operation_id: Optional[_builtins.str] = ...,
        parameters: Optional[outputs.ZoneFaultSimulationContentResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeTypeFaultSimulation")
    def node_type_fault_simulation(
        self,
    ) -> Optional[Sequence[outputs.NodeTypeFaultSimulationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[outputs.ZoneFaultSimulationContentResponse]: ...

@pulumi.output_type
class FaultSimulationResponse(dict):
    def __init__(
        __self__,
        *,
        details: Optional[outputs.FaultSimulationDetailsResponse] = ...,
        end_time: Optional[_builtins.str] = ...,
        simulation_id: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[outputs.FaultSimulationDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="simulationId")
    def simulation_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FrontendConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        application_gateway_backend_address_pool_id: Optional[_builtins.str] = ...,
        ip_address_type: Optional[_builtins.str] = ...,
        load_balancer_backend_address_pool_id: Optional[_builtins.str] = ...,
        load_balancer_inbound_nat_pool_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationGatewayBackendAddressPoolId")
    def application_gateway_backend_address_pool_id(
        self,
    ) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerBackendAddressPoolId")
    def load_balancer_backend_address_pool_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerInboundNatPoolId")
    def load_balancer_inbound_nat_pool_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IpConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        application_gateway_backend_address_pools: Optional[
            Sequence[outputs.SubResourceResponse]
        ] = ...,
        load_balancer_backend_address_pools: Optional[
            Sequence[outputs.SubResourceResponse]
        ] = ...,
        load_balancer_inbound_nat_pools: Optional[
            Sequence[outputs.SubResourceResponse]
        ] = ...,
        private_ip_address_version: Optional[_builtins.str] = ...,
        public_ip_address_configuration: Optional[
            outputs.IpConfigurationResponsePublicIPAddressConfiguration
        ] = ...,
        subnet: Optional[outputs.SubResourceResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="applicationGatewayBackendAddressPools")
    def application_gateway_backend_address_pools(
        self,
    ) -> Optional[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerBackendAddressPools")
    def load_balancer_backend_address_pools(
        self,
    ) -> Optional[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerInboundNatPools")
    def load_balancer_inbound_nat_pools(
        self,
    ) -> Optional[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="privateIPAddressVersion")
    def private_ip_address_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddressConfiguration")
    def public_ip_address_configuration(
        self,
    ) -> Optional[outputs.IpConfigurationResponsePublicIPAddressConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[outputs.SubResourceResponse]: ...

@pulumi.output_type
class IpConfigurationResponsePublicIPAddressConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        ip_tags: Optional[Sequence[outputs.IpTagResponse]] = ...,
        public_ip_address_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipTags")
    def ip_tags(self) -> Optional[Sequence[outputs.IpTagResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddressVersion")
    def public_ip_address_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IpTagResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, ip_tag_type: _builtins.str, tag: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipTagType")
    def ip_tag_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> _builtins.str: ...

@pulumi.output_type
class LoadBalancingRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backend_port: _builtins.int,
        frontend_port: _builtins.int,
        probe_protocol: _builtins.str,
        protocol: _builtins.str,
        load_distribution: Optional[_builtins.str] = ...,
        probe_port: Optional[_builtins.int] = ...,
        probe_request_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="probeProtocol")
    def probe_protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="loadDistribution")
    def load_distribution(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="probePort")
    def probe_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="probeRequestPath")
    def probe_request_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class NamedPartitionSchemeResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, names: Sequence[_builtins.str], partition_scheme: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partitionScheme")
    def partition_scheme(self) -> _builtins.str: ...

@pulumi.output_type
class NetworkSecurityRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access: _builtins.str,
        direction: _builtins.str,
        name: _builtins.str,
        priority: _builtins.int,
        protocol: _builtins.str,
        description: Optional[_builtins.str] = ...,
        destination_address_prefix: Optional[_builtins.str] = ...,
        destination_address_prefixes: Optional[Sequence[_builtins.str]] = ...,
        destination_port_range: Optional[_builtins.str] = ...,
        destination_port_ranges: Optional[Sequence[_builtins.str]] = ...,
        source_address_prefix: Optional[_builtins.str] = ...,
        source_address_prefixes: Optional[Sequence[_builtins.str]] = ...,
        source_port_range: Optional[_builtins.str] = ...,
        source_port_ranges: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def access(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationAddressPrefix")
    def destination_address_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationAddressPrefixes")
    def destination_address_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationPortRange")
    def destination_port_range(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceAddressPrefix")
    def source_address_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceAddressPrefixes")
    def source_address_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class NodeTypeFaultSimulationResponse(dict):
    def __init__(
        __self__,
        *,
        operation_status: _builtins.str,
        node_type_name: Optional[_builtins.str] = ...,
        operation_id: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operationStatus")
    def operation_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeTypeName")
    def node_type_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NodeTypeNatConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backend_port: Optional[_builtins.int] = ...,
        frontend_port_range_end: Optional[_builtins.int] = ...,
        frontend_port_range_start: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="frontendPortRangeEnd")
    def frontend_port_range_end(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="frontendPortRangeStart")
    def frontend_port_range_start(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class NodeTypeSkuResponse(dict):
    def __init__(
        __self__,
        *,
        capacity: _builtins.int,
        name: Optional[_builtins.str] = ...,
        tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PartitionInstanceCountScaleMechanismResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kind: _builtins.str,
        max_instance_count: _builtins.int,
        min_instance_count: _builtins.int,
        scale_increment: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="scaleIncrement")
    def scale_increment(self) -> _builtins.int: ...

@pulumi.output_type
class ResourceAzStatusResponse(dict):
    def __init__(
        __self__,
        *,
        details: _builtins.str,
        is_zone_resilient: _builtins.bool,
        resource_name: _builtins.str,
        resource_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isZoneResilient")
    def is_zone_resilient(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...

@pulumi.output_type
class RollingUpgradeMonitoringPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        failure_action: _builtins.str,
        health_check_retry_timeout: _builtins.str,
        health_check_stable_duration: _builtins.str,
        health_check_wait_duration: _builtins.str,
        upgrade_domain_timeout: _builtins.str,
        upgrade_timeout: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureAction")
    def failure_action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckRetryTimeout")
    def health_check_retry_timeout(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckStableDuration")
    def health_check_stable_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckWaitDuration")
    def health_check_wait_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="upgradeDomainTimeout")
    def upgrade_domain_timeout(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="upgradeTimeout")
    def upgrade_timeout(self) -> _builtins.str: ...

@pulumi.output_type
class ScalingPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, scaling_mechanism: Any, scaling_trigger: Any) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scalingMechanism")
    def scaling_mechanism(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="scalingTrigger")
    def scaling_trigger(self) -> Any: ...

@pulumi.output_type
class ServiceCorrelationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, scheme: _builtins.str, service_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...

@pulumi.output_type
class ServiceEndpointResponse(dict):
    def __init__(
        __self__,
        *,
        service: _builtins.str,
        locations: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServiceLoadMetricResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        default_load: Optional[_builtins.int] = ...,
        primary_default_load: Optional[_builtins.int] = ...,
        secondary_default_load: Optional[_builtins.int] = ...,
        weight: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultLoad")
    def default_load(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="primaryDefaultLoad")
    def primary_default_load(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryDefaultLoad")
    def secondary_default_load(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicePlacementInvalidDomainPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, domain_name: _builtins.str, type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ServicePlacementNonPartiallyPlaceServicePolicyResponse(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ServicePlacementPreferPrimaryDomainPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, domain_name: _builtins.str, type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ServicePlacementRequireDomainDistributionPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, domain_name: _builtins.str, type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ServicePlacementRequiredDomainPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, domain_name: _builtins.str, type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ServiceTypeHealthPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_percent_unhealthy_partitions_per_service: _builtins.int,
        max_percent_unhealthy_replicas_per_partition: _builtins.int,
        max_percent_unhealthy_services: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPercentUnhealthyPartitionsPerService")
    def max_percent_unhealthy_partitions_per_service(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxPercentUnhealthyReplicasPerPartition")
    def max_percent_unhealthy_replicas_per_partition(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxPercentUnhealthyServices")
    def max_percent_unhealthy_services(self) -> _builtins.int: ...

@pulumi.output_type
class SettingsParameterDescriptionResponse(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class SettingsSectionDescriptionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: Sequence[outputs.SettingsParameterDescriptionResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Sequence[outputs.SettingsParameterDescriptionResponse]: ...

@pulumi.output_type
class SingletonPartitionSchemeResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, partition_scheme: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionScheme")
    def partition_scheme(self) -> _builtins.str: ...

@pulumi.output_type
class SkuResponse(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class StatefulServicePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        partition_description: Any,
        provisioning_state: _builtins.str,
        service_kind: _builtins.str,
        service_type_name: _builtins.str,
        correlation_scheme: Optional[
            Sequence[outputs.ServiceCorrelationResponse]
        ] = ...,
        default_move_cost: Optional[_builtins.str] = ...,
        has_persisted_state: Optional[_builtins.bool] = ...,
        min_replica_set_size: Optional[_builtins.int] = ...,
        placement_constraints: Optional[_builtins.str] = ...,
        quorum_loss_wait_duration: Optional[_builtins.str] = ...,
        replica_restart_wait_duration: Optional[_builtins.str] = ...,
        scaling_policies: Optional[Sequence[outputs.ScalingPolicyResponse]] = ...,
        service_dns_name: Optional[_builtins.str] = ...,
        service_load_metrics: Optional[
            Sequence[outputs.ServiceLoadMetricResponse]
        ] = ...,
        service_package_activation_mode: Optional[_builtins.str] = ...,
        service_placement_policies: Optional[Sequence[Any]] = ...,
        service_placement_time_limit: Optional[_builtins.str] = ...,
        stand_by_replica_keep_duration: Optional[_builtins.str] = ...,
        target_replica_set_size: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionDescription")
    def partition_description(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceKind")
    def service_kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceTypeName")
    def service_type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="correlationScheme")
    def correlation_scheme(
        self,
    ) -> Optional[Sequence[outputs.ServiceCorrelationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultMoveCost")
    def default_move_cost(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hasPersistedState")
    def has_persisted_state(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="minReplicaSetSize")
    def min_replica_set_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="quorumLossWaitDuration")
    def quorum_loss_wait_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicaRestartWaitDuration")
    def replica_restart_wait_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scalingPolicies")
    def scaling_policies(self) -> Optional[Sequence[outputs.ScalingPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceLoadMetrics")
    def service_load_metrics(
        self,
    ) -> Optional[Sequence[outputs.ServiceLoadMetricResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="servicePackageActivationMode")
    def service_package_activation_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="servicePlacementPolicies")
    def service_placement_policies(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="servicePlacementTimeLimit")
    def service_placement_time_limit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="standByReplicaKeepDuration")
    def stand_by_replica_keep_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetReplicaSetSize")
    def target_replica_set_size(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StatelessServicePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_count: _builtins.int,
        partition_description: Any,
        provisioning_state: _builtins.str,
        service_kind: _builtins.str,
        service_type_name: _builtins.str,
        correlation_scheme: Optional[
            Sequence[outputs.ServiceCorrelationResponse]
        ] = ...,
        default_move_cost: Optional[_builtins.str] = ...,
        min_instance_count: Optional[_builtins.int] = ...,
        min_instance_percentage: Optional[_builtins.int] = ...,
        placement_constraints: Optional[_builtins.str] = ...,
        scaling_policies: Optional[Sequence[outputs.ScalingPolicyResponse]] = ...,
        service_dns_name: Optional[_builtins.str] = ...,
        service_load_metrics: Optional[
            Sequence[outputs.ServiceLoadMetricResponse]
        ] = ...,
        service_package_activation_mode: Optional[_builtins.str] = ...,
        service_placement_policies: Optional[Sequence[Any]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="partitionDescription")
    def partition_description(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceKind")
    def service_kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceTypeName")
    def service_type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="correlationScheme")
    def correlation_scheme(
        self,
    ) -> Optional[Sequence[outputs.ServiceCorrelationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultMoveCost")
    def default_move_cost(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minInstancePercentage")
    def min_instance_percentage(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scalingPolicies")
    def scaling_policies(self) -> Optional[Sequence[outputs.ScalingPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceLoadMetrics")
    def service_load_metrics(
        self,
    ) -> Optional[Sequence[outputs.ServiceLoadMetricResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="servicePackageActivationMode")
    def service_package_activation_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="servicePlacementPolicies")
    def service_placement_policies(self) -> Optional[Sequence[Any]]: ...

@pulumi.output_type
class SubResourceResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SubnetResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        enable_ipv6: Optional[_builtins.bool] = ...,
        network_security_group_id: Optional[_builtins.str] = ...,
        private_endpoint_network_policies: Optional[_builtins.str] = ...,
        private_link_service_network_policies: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enableIpv6")
    def enable_ipv6(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroupId")
    def network_security_group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointNetworkPolicies")
    def private_endpoint_network_policies(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceNetworkPolicies")
    def private_link_service_network_policies(self) -> Optional[_builtins.str]: ...

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
class UniformInt64RangePartitionSchemeResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        count: _builtins.int,
        high_key: _builtins.float,
        low_key: _builtins.float,
        partition_scheme: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="highKey")
    def high_key(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="lowKey")
    def low_key(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="partitionScheme")
    def partition_scheme(self) -> _builtins.str: ...

@pulumi.output_type
class UserAssignedIdentityResponse(dict):
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
class VMSSExtensionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        provisioning_state: _builtins.str,
        publisher: _builtins.str,
        type: _builtins.str,
        type_handler_version: _builtins.str,
        auto_upgrade_minor_version: Optional[_builtins.bool] = ...,
        enable_automatic_upgrade: Optional[_builtins.bool] = ...,
        force_update_tag: Optional[_builtins.str] = ...,
        protected_settings: Optional[Any] = ...,
        provision_after_extensions: Optional[Sequence[_builtins.str]] = ...,
        settings: Optional[Any] = ...,
        setup_order: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="provisionAfterExtensions")
    def provision_after_extensions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="setupOrder")
    def setup_order(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class VaultCertificateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, certificate_store: _builtins.str, certificate_url: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateStore")
    def certificate_store(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> _builtins.str: ...

@pulumi.output_type
class VaultSecretGroupResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_vault: outputs.SubResourceResponse,
        vault_certificates: Sequence[outputs.VaultCertificateResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceVault")
    def source_vault(self) -> outputs.SubResourceResponse: ...
    @_builtins.property
    @pulumi.getter(name="vaultCertificates")
    def vault_certificates(self) -> Sequence[outputs.VaultCertificateResponse]: ...

@pulumi.output_type
class VmImagePlanResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        product: Optional[_builtins.str] = ...,
        promotion_code: Optional[_builtins.str] = ...,
        publisher: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def product(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VmManagedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, user_assigned_identities: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class VmssDataDiskResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_letter: _builtins.str,
        disk_size_gb: _builtins.int,
        disk_type: _builtins.str,
        lun: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskLetter")
    def disk_letter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def lun(self) -> _builtins.int: ...

@pulumi.output_type
class ZoneFaultSimulationContentResponse(dict):
    def __init__(
        __self__,
        *,
        fault_kind: _builtins.str,
        constraints: Optional[outputs.FaultSimulationConstraintsResponse] = ...,
        force: Optional[_builtins.bool] = ...,
        zones: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="faultKind")
    def fault_kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def constraints(self) -> Optional[outputs.FaultSimulationConstraintsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def force(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...
