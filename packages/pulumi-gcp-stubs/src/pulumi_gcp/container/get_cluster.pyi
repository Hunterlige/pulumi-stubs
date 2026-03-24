

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetClusterResult', 'AwaitableGetClusterResult', 'get_cluster', 'get_cluster_output']
@pulumi.output_type
class GetClusterResult:
    
    def __init__(__self__, addons_configs=..., allow_net_admin=..., anonymous_authentication_configs=..., authenticator_groups_configs=..., binary_authorizations=..., cluster_autoscalings=..., cluster_ipv4_cidr=..., cluster_telemetries=..., confidential_nodes=..., control_plane_endpoints_configs=..., cost_management_configs=..., database_encryptions=..., datapath_provider=..., default_max_pods_per_node=..., default_snat_statuses=..., deletion_protection=..., description=..., disable_l4_lb_firewall_reconciliation=..., dns_configs=..., effective_labels=..., enable_autopilot=..., enable_cilium_clusterwide_network_policy=..., enable_fqdn_network_policy=..., enable_intranode_visibility=..., enable_k8s_beta_apis=..., enable_kubernetes_alpha=..., enable_l4_ilb_subsetting=..., enable_legacy_abac=..., enable_multi_networking=..., enable_shielded_nodes=..., enable_tpu=..., endpoint=..., enterprise_configs=..., fleets=..., gateway_api_configs=..., gke_auto_upgrade_configs=..., id=..., identity_service_configs=..., in_transit_encryption_config=..., initial_node_count=..., ip_allocation_policies=..., label_fingerprint=..., location=..., logging_configs=..., logging_service=..., maintenance_policies=..., managed_opentelemetry_configs=..., master_authorized_networks_configs=..., master_auths=..., master_version=..., mesh_certificates=..., min_master_version=..., monitoring_configs=..., monitoring_service=..., name=..., network=..., network_performance_configs=..., network_policies=..., networking_mode=..., node_configs=..., node_locations=..., node_pool_auto_configs=..., node_pool_defaults=..., node_pools=..., node_version=..., notification_configs=..., operation=..., pod_autoscalings=..., pod_security_policy_configs=..., private_cluster_configs=..., private_ipv6_google_access=..., project=..., protect_configs=..., pulumi_labels=..., rbac_binding_configs=..., release_channels=..., remove_default_node_pool=..., resource_labels=..., resource_usage_export_configs=..., secret_manager_configs=..., secret_sync_configs=..., security_posture_configs=..., self_link=..., service_external_ips_configs=..., services_ipv4_cidr=..., subnetwork=..., tpu_configs=..., tpu_ipv4_cidr_block=..., user_managed_keys_configs=..., vertical_pod_autoscalings=..., workload_alts_configs=..., workload_identity_configs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonsConfigs")
    def addons_configs(self) -> Sequence[outputs.GetClusterAddonsConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowNetAdmin")
    def allow_net_admin(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="anonymousAuthenticationConfigs")
    def anonymous_authentication_configs(self) -> Sequence[outputs.GetClusterAnonymousAuthenticationConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticatorGroupsConfigs")
    def authenticator_groups_configs(self) -> Sequence[outputs.GetClusterAuthenticatorGroupsConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorizations")
    def binary_authorizations(self) -> Sequence[outputs.GetClusterBinaryAuthorizationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterAutoscalings")
    def cluster_autoscalings(self) -> Sequence[outputs.GetClusterClusterAutoscalingResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIpv4Cidr")
    def cluster_ipv4_cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterTelemetries")
    def cluster_telemetries(self) -> Sequence[outputs.GetClusterClusterTelemetryResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialNodes")
    def confidential_nodes(self) -> Sequence[outputs.GetClusterConfidentialNodeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneEndpointsConfigs")
    def control_plane_endpoints_configs(self) -> Sequence[outputs.GetClusterControlPlaneEndpointsConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="costManagementConfigs")
    def cost_management_configs(self) -> Sequence[outputs.GetClusterCostManagementConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseEncryptions")
    def database_encryptions(self) -> Sequence[outputs.GetClusterDatabaseEncryptionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datapathProvider")
    def datapath_provider(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultMaxPodsPerNode")
    def default_max_pods_per_node(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSnatStatuses")
    def default_snat_statuses(self) -> Sequence[outputs.GetClusterDefaultSnatStatusResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableL4LbFirewallReconciliation")
    def disable_l4_lb_firewall_reconciliation(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsConfigs")
    def dns_configs(self) -> Sequence[outputs.GetClusterDnsConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutopilot")
    def enable_autopilot(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCiliumClusterwideNetworkPolicy")
    def enable_cilium_clusterwide_network_policy(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableFqdnNetworkPolicy")
    def enable_fqdn_network_policy(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIntranodeVisibility")
    def enable_intranode_visibility(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableK8sBetaApis")
    def enable_k8s_beta_apis(self) -> Sequence[outputs.GetClusterEnableK8sBetaApiResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableKubernetesAlpha")
    def enable_kubernetes_alpha(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableL4IlbSubsetting")
    def enable_l4_ilb_subsetting(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLegacyAbac")
    def enable_legacy_abac(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMultiNetworking")
    def enable_multi_networking(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableShieldedNodes")
    def enable_shielded_nodes(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableTpu")
    def enable_tpu(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enterpriseConfigs")
    def enterprise_configs(self) -> Sequence[outputs.GetClusterEnterpriseConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fleets(self) -> Sequence[outputs.GetClusterFleetResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayApiConfigs")
    def gateway_api_configs(self) -> Sequence[outputs.GetClusterGatewayApiConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeAutoUpgradeConfigs")
    def gke_auto_upgrade_configs(self) -> Sequence[outputs.GetClusterGkeAutoUpgradeConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityServiceConfigs")
    def identity_service_configs(self) -> Sequence[outputs.GetClusterIdentityServiceConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inTransitEncryptionConfig")
    def in_transit_encryption_config(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialNodeCount")
    def initial_node_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAllocationPolicies")
    def ip_allocation_policies(self) -> Sequence[outputs.GetClusterIpAllocationPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfigs")
    def logging_configs(self) -> Sequence[outputs.GetClusterLoggingConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingService")
    def logging_service(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenancePolicies")
    def maintenance_policies(self) -> Sequence[outputs.GetClusterMaintenancePolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedOpentelemetryConfigs")
    def managed_opentelemetry_configs(self) -> Sequence[outputs.GetClusterManagedOpentelemetryConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAuthorizedNetworksConfigs")
    def master_authorized_networks_configs(self) -> Sequence[outputs.GetClusterMasterAuthorizedNetworksConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAuths")
    def master_auths(self) -> Sequence[outputs.GetClusterMasterAuthResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterVersion")
    def master_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="meshCertificates")
    def mesh_certificates(self) -> Sequence[outputs.GetClusterMeshCertificateResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minMasterVersion")
    def min_master_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringConfigs")
    def monitoring_configs(self) -> Sequence[outputs.GetClusterMonitoringConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringService")
    def monitoring_service(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfigs")
    def network_performance_configs(self) -> Sequence[outputs.GetClusterNetworkPerformanceConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPolicies")
    def network_policies(self) -> Sequence[outputs.GetClusterNetworkPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkingMode")
    def networking_mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(self) -> Sequence[outputs.GetClusterNodeConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeLocations")
    def node_locations(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePoolAutoConfigs")
    def node_pool_auto_configs(self) -> Sequence[outputs.GetClusterNodePoolAutoConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePoolDefaults")
    def node_pool_defaults(self) -> Sequence[outputs.GetClusterNodePoolDefaultResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePools")
    def node_pools(self) -> Sequence[outputs.GetClusterNodePoolResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeVersion")
    def node_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfigs")
    def notification_configs(self) -> Sequence[outputs.GetClusterNotificationConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operation(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="podAutoscalings")
    def pod_autoscalings(self) -> Sequence[outputs.GetClusterPodAutoscalingResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="podSecurityPolicyConfigs")
    def pod_security_policy_configs(self) -> Sequence[outputs.GetClusterPodSecurityPolicyConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateClusterConfigs")
    def private_cluster_configs(self) -> Sequence[outputs.GetClusterPrivateClusterConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectConfigs")
    def protect_configs(self) -> Sequence[outputs.GetClusterProtectConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rbacBindingConfigs")
    def rbac_binding_configs(self) -> Sequence[outputs.GetClusterRbacBindingConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseChannels")
    def release_channels(self) -> Sequence[outputs.GetClusterReleaseChannelResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="removeDefaultNodePool")
    def remove_default_node_pool(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceLabels")
    def resource_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceUsageExportConfigs")
    def resource_usage_export_configs(self) -> Sequence[outputs.GetClusterResourceUsageExportConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretManagerConfigs")
    def secret_manager_configs(self) -> Sequence[outputs.GetClusterSecretManagerConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretSyncConfigs")
    def secret_sync_configs(self) -> Sequence[outputs.GetClusterSecretSyncConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPostureConfigs")
    def security_posture_configs(self) -> Sequence[outputs.GetClusterSecurityPostureConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceExternalIpsConfigs")
    def service_external_ips_configs(self) -> Sequence[outputs.GetClusterServiceExternalIpsConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicesIpv4Cidr")
    def services_ipv4_cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tpuConfigs")
    def tpu_configs(self) -> Sequence[outputs.GetClusterTpuConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tpuIpv4CidrBlock")
    def tpu_ipv4_cidr_block(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userManagedKeysConfigs")
    def user_managed_keys_configs(self) -> Sequence[outputs.GetClusterUserManagedKeysConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verticalPodAutoscalings")
    def vertical_pod_autoscalings(self) -> Sequence[outputs.GetClusterVerticalPodAutoscalingResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadAltsConfigs")
    def workload_alts_configs(self) -> Sequence[outputs.GetClusterWorkloadAltsConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityConfigs")
    def workload_identity_configs(self) -> Sequence[outputs.GetClusterWorkloadIdentityConfigResult]:
        ...
    


class AwaitableGetClusterResult(GetClusterResult):
    def __await__(self): # -> Generator[Never, Any, GetClusterResult]:
        ...
    


def get_cluster(location: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetClusterResult:
    
    ...

def get_cluster_output(location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetClusterResult]:
    
    ...

