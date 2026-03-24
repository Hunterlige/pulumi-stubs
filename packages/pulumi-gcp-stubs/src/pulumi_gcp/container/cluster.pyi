

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterArgs', 'Cluster']
@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *, addons_config: Optional[pulumi.Input[ClusterAddonsConfigArgs]] = ..., allow_net_admin: Optional[pulumi.Input[_builtins.bool]] = ..., anonymous_authentication_config: Optional[pulumi.Input[ClusterAnonymousAuthenticationConfigArgs]] = ..., authenticator_groups_config: Optional[pulumi.Input[ClusterAuthenticatorGroupsConfigArgs]] = ..., binary_authorization: Optional[pulumi.Input[ClusterBinaryAuthorizationArgs]] = ..., cluster_autoscaling: Optional[pulumi.Input[ClusterClusterAutoscalingArgs]] = ..., cluster_ipv4_cidr: Optional[pulumi.Input[_builtins.str]] = ..., cluster_telemetry: Optional[pulumi.Input[ClusterClusterTelemetryArgs]] = ..., confidential_nodes: Optional[pulumi.Input[ClusterConfidentialNodesArgs]] = ..., control_plane_endpoints_config: Optional[pulumi.Input[ClusterControlPlaneEndpointsConfigArgs]] = ..., cost_management_config: Optional[pulumi.Input[ClusterCostManagementConfigArgs]] = ..., database_encryption: Optional[pulumi.Input[ClusterDatabaseEncryptionArgs]] = ..., datapath_provider: Optional[pulumi.Input[_builtins.str]] = ..., default_max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ..., default_snat_status: Optional[pulumi.Input[ClusterDefaultSnatStatusArgs]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_l4_lb_firewall_reconciliation: Optional[pulumi.Input[_builtins.bool]] = ..., dns_config: Optional[pulumi.Input[ClusterDnsConfigArgs]] = ..., enable_autopilot: Optional[pulumi.Input[_builtins.bool]] = ..., enable_cilium_clusterwide_network_policy: Optional[pulumi.Input[_builtins.bool]] = ..., enable_fqdn_network_policy: Optional[pulumi.Input[_builtins.bool]] = ..., enable_intranode_visibility: Optional[pulumi.Input[_builtins.bool]] = ..., enable_k8s_beta_apis: Optional[pulumi.Input[ClusterEnableK8sBetaApisArgs]] = ..., enable_kubernetes_alpha: Optional[pulumi.Input[_builtins.bool]] = ..., enable_l4_ilb_subsetting: Optional[pulumi.Input[_builtins.bool]] = ..., enable_legacy_abac: Optional[pulumi.Input[_builtins.bool]] = ..., enable_multi_networking: Optional[pulumi.Input[_builtins.bool]] = ..., enable_shielded_nodes: Optional[pulumi.Input[_builtins.bool]] = ..., enable_tpu: Optional[pulumi.Input[_builtins.bool]] = ..., enterprise_config: Optional[pulumi.Input[ClusterEnterpriseConfigArgs]] = ..., fleet: Optional[pulumi.Input[ClusterFleetArgs]] = ..., gateway_api_config: Optional[pulumi.Input[ClusterGatewayApiConfigArgs]] = ..., gke_auto_upgrade_config: Optional[pulumi.Input[ClusterGkeAutoUpgradeConfigArgs]] = ..., identity_service_config: Optional[pulumi.Input[ClusterIdentityServiceConfigArgs]] = ..., in_transit_encryption_config: Optional[pulumi.Input[_builtins.str]] = ..., initial_node_count: Optional[pulumi.Input[_builtins.int]] = ..., ip_allocation_policy: Optional[pulumi.Input[ClusterIpAllocationPolicyArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[ClusterLoggingConfigArgs]] = ..., logging_service: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_policy: Optional[pulumi.Input[ClusterMaintenancePolicyArgs]] = ..., managed_opentelemetry_config: Optional[pulumi.Input[ClusterManagedOpentelemetryConfigArgs]] = ..., master_auth: Optional[pulumi.Input[ClusterMasterAuthArgs]] = ..., master_authorized_networks_config: Optional[pulumi.Input[ClusterMasterAuthorizedNetworksConfigArgs]] = ..., mesh_certificates: Optional[pulumi.Input[ClusterMeshCertificatesArgs]] = ..., min_master_version: Optional[pulumi.Input[_builtins.str]] = ..., monitoring_config: Optional[pulumi.Input[ClusterMonitoringConfigArgs]] = ..., monitoring_service: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., network_performance_config: Optional[pulumi.Input[ClusterNetworkPerformanceConfigArgs]] = ..., network_policy: Optional[pulumi.Input[ClusterNetworkPolicyArgs]] = ..., networking_mode: Optional[pulumi.Input[_builtins.str]] = ..., node_config: Optional[pulumi.Input[ClusterNodeConfigArgs]] = ..., node_locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., node_pool_auto_config: Optional[pulumi.Input[ClusterNodePoolAutoConfigArgs]] = ..., node_pool_defaults: Optional[pulumi.Input[ClusterNodePoolDefaultsArgs]] = ..., node_pools: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodePoolArgs]]]] = ..., node_version: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[ClusterNotificationConfigArgs]] = ..., pod_autoscaling: Optional[pulumi.Input[ClusterPodAutoscalingArgs]] = ..., pod_security_policy_config: Optional[pulumi.Input[ClusterPodSecurityPolicyConfigArgs]] = ..., private_cluster_config: Optional[pulumi.Input[ClusterPrivateClusterConfigArgs]] = ..., private_ipv6_google_access: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protect_config: Optional[pulumi.Input[ClusterProtectConfigArgs]] = ..., rbac_binding_config: Optional[pulumi.Input[ClusterRbacBindingConfigArgs]] = ..., release_channel: Optional[pulumi.Input[ClusterReleaseChannelArgs]] = ..., remove_default_node_pool: Optional[pulumi.Input[_builtins.bool]] = ..., resource_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_usage_export_config: Optional[pulumi.Input[ClusterResourceUsageExportConfigArgs]] = ..., secret_manager_config: Optional[pulumi.Input[ClusterSecretManagerConfigArgs]] = ..., secret_sync_config: Optional[pulumi.Input[ClusterSecretSyncConfigArgs]] = ..., security_posture_config: Optional[pulumi.Input[ClusterSecurityPostureConfigArgs]] = ..., service_external_ips_config: Optional[pulumi.Input[ClusterServiceExternalIpsConfigArgs]] = ..., subnetwork: Optional[pulumi.Input[_builtins.str]] = ..., tpu_config: Optional[pulumi.Input[ClusterTpuConfigArgs]] = ..., user_managed_keys_config: Optional[pulumi.Input[ClusterUserManagedKeysConfigArgs]] = ..., vertical_pod_autoscaling: Optional[pulumi.Input[ClusterVerticalPodAutoscalingArgs]] = ..., workload_alts_config: Optional[pulumi.Input[ClusterWorkloadAltsConfigArgs]] = ..., workload_identity_config: Optional[pulumi.Input[ClusterWorkloadIdentityConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonsConfig")
    def addons_config(self) -> Optional[pulumi.Input[ClusterAddonsConfigArgs]]:
        
        ...
    
    @addons_config.setter
    def addons_config(self, value: Optional[pulumi.Input[ClusterAddonsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowNetAdmin")
    def allow_net_admin(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_net_admin.setter
    def allow_net_admin(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="anonymousAuthenticationConfig")
    def anonymous_authentication_config(self) -> Optional[pulumi.Input[ClusterAnonymousAuthenticationConfigArgs]]:
        
        ...
    
    @anonymous_authentication_config.setter
    def anonymous_authentication_config(self, value: Optional[pulumi.Input[ClusterAnonymousAuthenticationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticatorGroupsConfig")
    def authenticator_groups_config(self) -> Optional[pulumi.Input[ClusterAuthenticatorGroupsConfigArgs]]:
        
        ...
    
    @authenticator_groups_config.setter
    def authenticator_groups_config(self, value: Optional[pulumi.Input[ClusterAuthenticatorGroupsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(self) -> Optional[pulumi.Input[ClusterBinaryAuthorizationArgs]]:
        
        ...
    
    @binary_authorization.setter
    def binary_authorization(self, value: Optional[pulumi.Input[ClusterBinaryAuthorizationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterAutoscaling")
    def cluster_autoscaling(self) -> Optional[pulumi.Input[ClusterClusterAutoscalingArgs]]:
        
        ...
    
    @cluster_autoscaling.setter
    def cluster_autoscaling(self, value: Optional[pulumi.Input[ClusterClusterAutoscalingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIpv4Cidr")
    def cluster_ipv4_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_ipv4_cidr.setter
    def cluster_ipv4_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterTelemetry")
    def cluster_telemetry(self) -> Optional[pulumi.Input[ClusterClusterTelemetryArgs]]:
        
        ...
    
    @cluster_telemetry.setter
    def cluster_telemetry(self, value: Optional[pulumi.Input[ClusterClusterTelemetryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialNodes")
    def confidential_nodes(self) -> Optional[pulumi.Input[ClusterConfidentialNodesArgs]]:
        
        ...
    
    @confidential_nodes.setter
    def confidential_nodes(self, value: Optional[pulumi.Input[ClusterConfidentialNodesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneEndpointsConfig")
    def control_plane_endpoints_config(self) -> Optional[pulumi.Input[ClusterControlPlaneEndpointsConfigArgs]]:
        
        ...
    
    @control_plane_endpoints_config.setter
    def control_plane_endpoints_config(self, value: Optional[pulumi.Input[ClusterControlPlaneEndpointsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="costManagementConfig")
    def cost_management_config(self) -> Optional[pulumi.Input[ClusterCostManagementConfigArgs]]:
        
        ...
    
    @cost_management_config.setter
    def cost_management_config(self, value: Optional[pulumi.Input[ClusterCostManagementConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseEncryption")
    def database_encryption(self) -> Optional[pulumi.Input[ClusterDatabaseEncryptionArgs]]:
        
        ...
    
    @database_encryption.setter
    def database_encryption(self, value: Optional[pulumi.Input[ClusterDatabaseEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datapathProvider")
    def datapath_provider(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @datapath_provider.setter
    def datapath_provider(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultMaxPodsPerNode")
    def default_max_pods_per_node(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_max_pods_per_node.setter
    def default_max_pods_per_node(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSnatStatus")
    def default_snat_status(self) -> Optional[pulumi.Input[ClusterDefaultSnatStatusArgs]]:
        
        ...
    
    @default_snat_status.setter
    def default_snat_status(self, value: Optional[pulumi.Input[ClusterDefaultSnatStatusArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableL4LbFirewallReconciliation")
    def disable_l4_lb_firewall_reconciliation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_l4_lb_firewall_reconciliation.setter
    def disable_l4_lb_firewall_reconciliation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> Optional[pulumi.Input[ClusterDnsConfigArgs]]:
        
        ...
    
    @dns_config.setter
    def dns_config(self, value: Optional[pulumi.Input[ClusterDnsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutopilot")
    def enable_autopilot(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_autopilot.setter
    def enable_autopilot(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCiliumClusterwideNetworkPolicy")
    def enable_cilium_clusterwide_network_policy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_cilium_clusterwide_network_policy.setter
    def enable_cilium_clusterwide_network_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableFqdnNetworkPolicy")
    def enable_fqdn_network_policy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_fqdn_network_policy.setter
    def enable_fqdn_network_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIntranodeVisibility")
    def enable_intranode_visibility(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_intranode_visibility.setter
    def enable_intranode_visibility(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableK8sBetaApis")
    def enable_k8s_beta_apis(self) -> Optional[pulumi.Input[ClusterEnableK8sBetaApisArgs]]:
        
        ...
    
    @enable_k8s_beta_apis.setter
    def enable_k8s_beta_apis(self, value: Optional[pulumi.Input[ClusterEnableK8sBetaApisArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableKubernetesAlpha")
    def enable_kubernetes_alpha(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_kubernetes_alpha.setter
    def enable_kubernetes_alpha(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableL4IlbSubsetting")
    def enable_l4_ilb_subsetting(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_l4_ilb_subsetting.setter
    def enable_l4_ilb_subsetting(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLegacyAbac")
    def enable_legacy_abac(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_legacy_abac.setter
    def enable_legacy_abac(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMultiNetworking")
    def enable_multi_networking(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_multi_networking.setter
    def enable_multi_networking(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableShieldedNodes")
    def enable_shielded_nodes(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_shielded_nodes.setter
    def enable_shielded_nodes(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableTpu")
    def enable_tpu(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_tpu.setter
    def enable_tpu(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enterpriseConfig")
    @_utilities.deprecated(...)
    def enterprise_config(self) -> Optional[pulumi.Input[ClusterEnterpriseConfigArgs]]:
        
        ...
    
    @enterprise_config.setter
    def enterprise_config(self, value: Optional[pulumi.Input[ClusterEnterpriseConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fleet(self) -> Optional[pulumi.Input[ClusterFleetArgs]]:
        
        ...
    
    @fleet.setter
    def fleet(self, value: Optional[pulumi.Input[ClusterFleetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayApiConfig")
    def gateway_api_config(self) -> Optional[pulumi.Input[ClusterGatewayApiConfigArgs]]:
        
        ...
    
    @gateway_api_config.setter
    def gateway_api_config(self, value: Optional[pulumi.Input[ClusterGatewayApiConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeAutoUpgradeConfig")
    def gke_auto_upgrade_config(self) -> Optional[pulumi.Input[ClusterGkeAutoUpgradeConfigArgs]]:
        
        ...
    
    @gke_auto_upgrade_config.setter
    def gke_auto_upgrade_config(self, value: Optional[pulumi.Input[ClusterGkeAutoUpgradeConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityServiceConfig")
    def identity_service_config(self) -> Optional[pulumi.Input[ClusterIdentityServiceConfigArgs]]:
        
        ...
    
    @identity_service_config.setter
    def identity_service_config(self, value: Optional[pulumi.Input[ClusterIdentityServiceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inTransitEncryptionConfig")
    def in_transit_encryption_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @in_transit_encryption_config.setter
    def in_transit_encryption_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialNodeCount")
    def initial_node_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @initial_node_count.setter
    def initial_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAllocationPolicy")
    def ip_allocation_policy(self) -> Optional[pulumi.Input[ClusterIpAllocationPolicyArgs]]:
        
        ...
    
    @ip_allocation_policy.setter
    def ip_allocation_policy(self, value: Optional[pulumi.Input[ClusterIpAllocationPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input[ClusterLoggingConfigArgs]]:
        
        ...
    
    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input[ClusterLoggingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingService")
    def logging_service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @logging_service.setter
    def logging_service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(self) -> Optional[pulumi.Input[ClusterMaintenancePolicyArgs]]:
        
        ...
    
    @maintenance_policy.setter
    def maintenance_policy(self, value: Optional[pulumi.Input[ClusterMaintenancePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedOpentelemetryConfig")
    def managed_opentelemetry_config(self) -> Optional[pulumi.Input[ClusterManagedOpentelemetryConfigArgs]]:
        
        ...
    
    @managed_opentelemetry_config.setter
    def managed_opentelemetry_config(self, value: Optional[pulumi.Input[ClusterManagedOpentelemetryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAuth")
    def master_auth(self) -> Optional[pulumi.Input[ClusterMasterAuthArgs]]:
        
        ...
    
    @master_auth.setter
    def master_auth(self, value: Optional[pulumi.Input[ClusterMasterAuthArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAuthorizedNetworksConfig")
    def master_authorized_networks_config(self) -> Optional[pulumi.Input[ClusterMasterAuthorizedNetworksConfigArgs]]:
        
        ...
    
    @master_authorized_networks_config.setter
    def master_authorized_networks_config(self, value: Optional[pulumi.Input[ClusterMasterAuthorizedNetworksConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="meshCertificates")
    def mesh_certificates(self) -> Optional[pulumi.Input[ClusterMeshCertificatesArgs]]:
        
        ...
    
    @mesh_certificates.setter
    def mesh_certificates(self, value: Optional[pulumi.Input[ClusterMeshCertificatesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minMasterVersion")
    def min_master_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @min_master_version.setter
    def min_master_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringConfig")
    def monitoring_config(self) -> Optional[pulumi.Input[ClusterMonitoringConfigArgs]]:
        
        ...
    
    @monitoring_config.setter
    def monitoring_config(self, value: Optional[pulumi.Input[ClusterMonitoringConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringService")
    def monitoring_service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @monitoring_service.setter
    def monitoring_service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfig")
    def network_performance_config(self) -> Optional[pulumi.Input[ClusterNetworkPerformanceConfigArgs]]:
        
        ...
    
    @network_performance_config.setter
    def network_performance_config(self, value: Optional[pulumi.Input[ClusterNetworkPerformanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPolicy")
    def network_policy(self) -> Optional[pulumi.Input[ClusterNetworkPolicyArgs]]:
        
        ...
    
    @network_policy.setter
    def network_policy(self, value: Optional[pulumi.Input[ClusterNetworkPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkingMode")
    def networking_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @networking_mode.setter
    def networking_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[ClusterNodeConfigArgs]]:
        
        ...
    
    @node_config.setter
    def node_config(self, value: Optional[pulumi.Input[ClusterNodeConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeLocations")
    def node_locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @node_locations.setter
    def node_locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePoolAutoConfig")
    def node_pool_auto_config(self) -> Optional[pulumi.Input[ClusterNodePoolAutoConfigArgs]]:
        
        ...
    
    @node_pool_auto_config.setter
    def node_pool_auto_config(self, value: Optional[pulumi.Input[ClusterNodePoolAutoConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePoolDefaults")
    def node_pool_defaults(self) -> Optional[pulumi.Input[ClusterNodePoolDefaultsArgs]]:
        
        ...
    
    @node_pool_defaults.setter
    def node_pool_defaults(self, value: Optional[pulumi.Input[ClusterNodePoolDefaultsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePools")
    def node_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodePoolArgs]]]]:
        
        ...
    
    @node_pools.setter
    def node_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodePoolArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeVersion")
    def node_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_version.setter
    def node_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> Optional[pulumi.Input[ClusterNotificationConfigArgs]]:
        
        ...
    
    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input[ClusterNotificationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="podAutoscaling")
    def pod_autoscaling(self) -> Optional[pulumi.Input[ClusterPodAutoscalingArgs]]:
        
        ...
    
    @pod_autoscaling.setter
    def pod_autoscaling(self, value: Optional[pulumi.Input[ClusterPodAutoscalingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="podSecurityPolicyConfig")
    def pod_security_policy_config(self) -> Optional[pulumi.Input[ClusterPodSecurityPolicyConfigArgs]]:
        
        ...
    
    @pod_security_policy_config.setter
    def pod_security_policy_config(self, value: Optional[pulumi.Input[ClusterPodSecurityPolicyConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateClusterConfig")
    def private_cluster_config(self) -> Optional[pulumi.Input[ClusterPrivateClusterConfigArgs]]:
        
        ...
    
    @private_cluster_config.setter
    def private_cluster_config(self, value: Optional[pulumi.Input[ClusterPrivateClusterConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ipv6_google_access.setter
    def private_ipv6_google_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectConfig")
    def protect_config(self) -> Optional[pulumi.Input[ClusterProtectConfigArgs]]:
        
        ...
    
    @protect_config.setter
    def protect_config(self, value: Optional[pulumi.Input[ClusterProtectConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rbacBindingConfig")
    def rbac_binding_config(self) -> Optional[pulumi.Input[ClusterRbacBindingConfigArgs]]:
        
        ...
    
    @rbac_binding_config.setter
    def rbac_binding_config(self, value: Optional[pulumi.Input[ClusterRbacBindingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseChannel")
    def release_channel(self) -> Optional[pulumi.Input[ClusterReleaseChannelArgs]]:
        
        ...
    
    @release_channel.setter
    def release_channel(self, value: Optional[pulumi.Input[ClusterReleaseChannelArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="removeDefaultNodePool")
    def remove_default_node_pool(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @remove_default_node_pool.setter
    def remove_default_node_pool(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceLabels")
    def resource_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_labels.setter
    def resource_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceUsageExportConfig")
    def resource_usage_export_config(self) -> Optional[pulumi.Input[ClusterResourceUsageExportConfigArgs]]:
        
        ...
    
    @resource_usage_export_config.setter
    def resource_usage_export_config(self, value: Optional[pulumi.Input[ClusterResourceUsageExportConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretManagerConfig")
    def secret_manager_config(self) -> Optional[pulumi.Input[ClusterSecretManagerConfigArgs]]:
        
        ...
    
    @secret_manager_config.setter
    def secret_manager_config(self, value: Optional[pulumi.Input[ClusterSecretManagerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretSyncConfig")
    def secret_sync_config(self) -> Optional[pulumi.Input[ClusterSecretSyncConfigArgs]]:
        
        ...
    
    @secret_sync_config.setter
    def secret_sync_config(self, value: Optional[pulumi.Input[ClusterSecretSyncConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPostureConfig")
    def security_posture_config(self) -> Optional[pulumi.Input[ClusterSecurityPostureConfigArgs]]:
        
        ...
    
    @security_posture_config.setter
    def security_posture_config(self, value: Optional[pulumi.Input[ClusterSecurityPostureConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceExternalIpsConfig")
    def service_external_ips_config(self) -> Optional[pulumi.Input[ClusterServiceExternalIpsConfigArgs]]:
        
        ...
    
    @service_external_ips_config.setter
    def service_external_ips_config(self, value: Optional[pulumi.Input[ClusterServiceExternalIpsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tpuConfig")
    def tpu_config(self) -> Optional[pulumi.Input[ClusterTpuConfigArgs]]:
        
        ...
    
    @tpu_config.setter
    def tpu_config(self, value: Optional[pulumi.Input[ClusterTpuConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userManagedKeysConfig")
    def user_managed_keys_config(self) -> Optional[pulumi.Input[ClusterUserManagedKeysConfigArgs]]:
        
        ...
    
    @user_managed_keys_config.setter
    def user_managed_keys_config(self, value: Optional[pulumi.Input[ClusterUserManagedKeysConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verticalPodAutoscaling")
    def vertical_pod_autoscaling(self) -> Optional[pulumi.Input[ClusterVerticalPodAutoscalingArgs]]:
        
        ...
    
    @vertical_pod_autoscaling.setter
    def vertical_pod_autoscaling(self, value: Optional[pulumi.Input[ClusterVerticalPodAutoscalingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadAltsConfig")
    def workload_alts_config(self) -> Optional[pulumi.Input[ClusterWorkloadAltsConfigArgs]]:
        
        ...
    
    @workload_alts_config.setter
    def workload_alts_config(self, value: Optional[pulumi.Input[ClusterWorkloadAltsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityConfig")
    def workload_identity_config(self) -> Optional[pulumi.Input[ClusterWorkloadIdentityConfigArgs]]:
        
        ...
    
    @workload_identity_config.setter
    def workload_identity_config(self, value: Optional[pulumi.Input[ClusterWorkloadIdentityConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ClusterState:
    def __init__(__self__, *, addons_config: Optional[pulumi.Input[ClusterAddonsConfigArgs]] = ..., allow_net_admin: Optional[pulumi.Input[_builtins.bool]] = ..., anonymous_authentication_config: Optional[pulumi.Input[ClusterAnonymousAuthenticationConfigArgs]] = ..., authenticator_groups_config: Optional[pulumi.Input[ClusterAuthenticatorGroupsConfigArgs]] = ..., binary_authorization: Optional[pulumi.Input[ClusterBinaryAuthorizationArgs]] = ..., cluster_autoscaling: Optional[pulumi.Input[ClusterClusterAutoscalingArgs]] = ..., cluster_ipv4_cidr: Optional[pulumi.Input[_builtins.str]] = ..., cluster_telemetry: Optional[pulumi.Input[ClusterClusterTelemetryArgs]] = ..., confidential_nodes: Optional[pulumi.Input[ClusterConfidentialNodesArgs]] = ..., control_plane_endpoints_config: Optional[pulumi.Input[ClusterControlPlaneEndpointsConfigArgs]] = ..., cost_management_config: Optional[pulumi.Input[ClusterCostManagementConfigArgs]] = ..., database_encryption: Optional[pulumi.Input[ClusterDatabaseEncryptionArgs]] = ..., datapath_provider: Optional[pulumi.Input[_builtins.str]] = ..., default_max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ..., default_snat_status: Optional[pulumi.Input[ClusterDefaultSnatStatusArgs]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_l4_lb_firewall_reconciliation: Optional[pulumi.Input[_builtins.bool]] = ..., dns_config: Optional[pulumi.Input[ClusterDnsConfigArgs]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_autopilot: Optional[pulumi.Input[_builtins.bool]] = ..., enable_cilium_clusterwide_network_policy: Optional[pulumi.Input[_builtins.bool]] = ..., enable_fqdn_network_policy: Optional[pulumi.Input[_builtins.bool]] = ..., enable_intranode_visibility: Optional[pulumi.Input[_builtins.bool]] = ..., enable_k8s_beta_apis: Optional[pulumi.Input[ClusterEnableK8sBetaApisArgs]] = ..., enable_kubernetes_alpha: Optional[pulumi.Input[_builtins.bool]] = ..., enable_l4_ilb_subsetting: Optional[pulumi.Input[_builtins.bool]] = ..., enable_legacy_abac: Optional[pulumi.Input[_builtins.bool]] = ..., enable_multi_networking: Optional[pulumi.Input[_builtins.bool]] = ..., enable_shielded_nodes: Optional[pulumi.Input[_builtins.bool]] = ..., enable_tpu: Optional[pulumi.Input[_builtins.bool]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., enterprise_config: Optional[pulumi.Input[ClusterEnterpriseConfigArgs]] = ..., fleet: Optional[pulumi.Input[ClusterFleetArgs]] = ..., gateway_api_config: Optional[pulumi.Input[ClusterGatewayApiConfigArgs]] = ..., gke_auto_upgrade_config: Optional[pulumi.Input[ClusterGkeAutoUpgradeConfigArgs]] = ..., identity_service_config: Optional[pulumi.Input[ClusterIdentityServiceConfigArgs]] = ..., in_transit_encryption_config: Optional[pulumi.Input[_builtins.str]] = ..., initial_node_count: Optional[pulumi.Input[_builtins.int]] = ..., ip_allocation_policy: Optional[pulumi.Input[ClusterIpAllocationPolicyArgs]] = ..., label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[ClusterLoggingConfigArgs]] = ..., logging_service: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_policy: Optional[pulumi.Input[ClusterMaintenancePolicyArgs]] = ..., managed_opentelemetry_config: Optional[pulumi.Input[ClusterManagedOpentelemetryConfigArgs]] = ..., master_auth: Optional[pulumi.Input[ClusterMasterAuthArgs]] = ..., master_authorized_networks_config: Optional[pulumi.Input[ClusterMasterAuthorizedNetworksConfigArgs]] = ..., master_version: Optional[pulumi.Input[_builtins.str]] = ..., mesh_certificates: Optional[pulumi.Input[ClusterMeshCertificatesArgs]] = ..., min_master_version: Optional[pulumi.Input[_builtins.str]] = ..., monitoring_config: Optional[pulumi.Input[ClusterMonitoringConfigArgs]] = ..., monitoring_service: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., network_performance_config: Optional[pulumi.Input[ClusterNetworkPerformanceConfigArgs]] = ..., network_policy: Optional[pulumi.Input[ClusterNetworkPolicyArgs]] = ..., networking_mode: Optional[pulumi.Input[_builtins.str]] = ..., node_config: Optional[pulumi.Input[ClusterNodeConfigArgs]] = ..., node_locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., node_pool_auto_config: Optional[pulumi.Input[ClusterNodePoolAutoConfigArgs]] = ..., node_pool_defaults: Optional[pulumi.Input[ClusterNodePoolDefaultsArgs]] = ..., node_pools: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodePoolArgs]]]] = ..., node_version: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[ClusterNotificationConfigArgs]] = ..., operation: Optional[pulumi.Input[_builtins.str]] = ..., pod_autoscaling: Optional[pulumi.Input[ClusterPodAutoscalingArgs]] = ..., pod_security_policy_config: Optional[pulumi.Input[ClusterPodSecurityPolicyConfigArgs]] = ..., private_cluster_config: Optional[pulumi.Input[ClusterPrivateClusterConfigArgs]] = ..., private_ipv6_google_access: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protect_config: Optional[pulumi.Input[ClusterProtectConfigArgs]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., rbac_binding_config: Optional[pulumi.Input[ClusterRbacBindingConfigArgs]] = ..., release_channel: Optional[pulumi.Input[ClusterReleaseChannelArgs]] = ..., remove_default_node_pool: Optional[pulumi.Input[_builtins.bool]] = ..., resource_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_usage_export_config: Optional[pulumi.Input[ClusterResourceUsageExportConfigArgs]] = ..., secret_manager_config: Optional[pulumi.Input[ClusterSecretManagerConfigArgs]] = ..., secret_sync_config: Optional[pulumi.Input[ClusterSecretSyncConfigArgs]] = ..., security_posture_config: Optional[pulumi.Input[ClusterSecurityPostureConfigArgs]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., service_external_ips_config: Optional[pulumi.Input[ClusterServiceExternalIpsConfigArgs]] = ..., services_ipv4_cidr: Optional[pulumi.Input[_builtins.str]] = ..., subnetwork: Optional[pulumi.Input[_builtins.str]] = ..., tpu_config: Optional[pulumi.Input[ClusterTpuConfigArgs]] = ..., tpu_ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., user_managed_keys_config: Optional[pulumi.Input[ClusterUserManagedKeysConfigArgs]] = ..., vertical_pod_autoscaling: Optional[pulumi.Input[ClusterVerticalPodAutoscalingArgs]] = ..., workload_alts_config: Optional[pulumi.Input[ClusterWorkloadAltsConfigArgs]] = ..., workload_identity_config: Optional[pulumi.Input[ClusterWorkloadIdentityConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonsConfig")
    def addons_config(self) -> Optional[pulumi.Input[ClusterAddonsConfigArgs]]:
        
        ...
    
    @addons_config.setter
    def addons_config(self, value: Optional[pulumi.Input[ClusterAddonsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowNetAdmin")
    def allow_net_admin(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_net_admin.setter
    def allow_net_admin(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="anonymousAuthenticationConfig")
    def anonymous_authentication_config(self) -> Optional[pulumi.Input[ClusterAnonymousAuthenticationConfigArgs]]:
        
        ...
    
    @anonymous_authentication_config.setter
    def anonymous_authentication_config(self, value: Optional[pulumi.Input[ClusterAnonymousAuthenticationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticatorGroupsConfig")
    def authenticator_groups_config(self) -> Optional[pulumi.Input[ClusterAuthenticatorGroupsConfigArgs]]:
        
        ...
    
    @authenticator_groups_config.setter
    def authenticator_groups_config(self, value: Optional[pulumi.Input[ClusterAuthenticatorGroupsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(self) -> Optional[pulumi.Input[ClusterBinaryAuthorizationArgs]]:
        
        ...
    
    @binary_authorization.setter
    def binary_authorization(self, value: Optional[pulumi.Input[ClusterBinaryAuthorizationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterAutoscaling")
    def cluster_autoscaling(self) -> Optional[pulumi.Input[ClusterClusterAutoscalingArgs]]:
        
        ...
    
    @cluster_autoscaling.setter
    def cluster_autoscaling(self, value: Optional[pulumi.Input[ClusterClusterAutoscalingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIpv4Cidr")
    def cluster_ipv4_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_ipv4_cidr.setter
    def cluster_ipv4_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterTelemetry")
    def cluster_telemetry(self) -> Optional[pulumi.Input[ClusterClusterTelemetryArgs]]:
        
        ...
    
    @cluster_telemetry.setter
    def cluster_telemetry(self, value: Optional[pulumi.Input[ClusterClusterTelemetryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialNodes")
    def confidential_nodes(self) -> Optional[pulumi.Input[ClusterConfidentialNodesArgs]]:
        
        ...
    
    @confidential_nodes.setter
    def confidential_nodes(self, value: Optional[pulumi.Input[ClusterConfidentialNodesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneEndpointsConfig")
    def control_plane_endpoints_config(self) -> Optional[pulumi.Input[ClusterControlPlaneEndpointsConfigArgs]]:
        
        ...
    
    @control_plane_endpoints_config.setter
    def control_plane_endpoints_config(self, value: Optional[pulumi.Input[ClusterControlPlaneEndpointsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="costManagementConfig")
    def cost_management_config(self) -> Optional[pulumi.Input[ClusterCostManagementConfigArgs]]:
        
        ...
    
    @cost_management_config.setter
    def cost_management_config(self, value: Optional[pulumi.Input[ClusterCostManagementConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseEncryption")
    def database_encryption(self) -> Optional[pulumi.Input[ClusterDatabaseEncryptionArgs]]:
        
        ...
    
    @database_encryption.setter
    def database_encryption(self, value: Optional[pulumi.Input[ClusterDatabaseEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datapathProvider")
    def datapath_provider(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @datapath_provider.setter
    def datapath_provider(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultMaxPodsPerNode")
    def default_max_pods_per_node(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_max_pods_per_node.setter
    def default_max_pods_per_node(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSnatStatus")
    def default_snat_status(self) -> Optional[pulumi.Input[ClusterDefaultSnatStatusArgs]]:
        
        ...
    
    @default_snat_status.setter
    def default_snat_status(self, value: Optional[pulumi.Input[ClusterDefaultSnatStatusArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableL4LbFirewallReconciliation")
    def disable_l4_lb_firewall_reconciliation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_l4_lb_firewall_reconciliation.setter
    def disable_l4_lb_firewall_reconciliation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> Optional[pulumi.Input[ClusterDnsConfigArgs]]:
        
        ...
    
    @dns_config.setter
    def dns_config(self, value: Optional[pulumi.Input[ClusterDnsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutopilot")
    def enable_autopilot(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_autopilot.setter
    def enable_autopilot(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCiliumClusterwideNetworkPolicy")
    def enable_cilium_clusterwide_network_policy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_cilium_clusterwide_network_policy.setter
    def enable_cilium_clusterwide_network_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableFqdnNetworkPolicy")
    def enable_fqdn_network_policy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_fqdn_network_policy.setter
    def enable_fqdn_network_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIntranodeVisibility")
    def enable_intranode_visibility(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_intranode_visibility.setter
    def enable_intranode_visibility(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableK8sBetaApis")
    def enable_k8s_beta_apis(self) -> Optional[pulumi.Input[ClusterEnableK8sBetaApisArgs]]:
        
        ...
    
    @enable_k8s_beta_apis.setter
    def enable_k8s_beta_apis(self, value: Optional[pulumi.Input[ClusterEnableK8sBetaApisArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableKubernetesAlpha")
    def enable_kubernetes_alpha(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_kubernetes_alpha.setter
    def enable_kubernetes_alpha(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableL4IlbSubsetting")
    def enable_l4_ilb_subsetting(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_l4_ilb_subsetting.setter
    def enable_l4_ilb_subsetting(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLegacyAbac")
    def enable_legacy_abac(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_legacy_abac.setter
    def enable_legacy_abac(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMultiNetworking")
    def enable_multi_networking(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_multi_networking.setter
    def enable_multi_networking(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableShieldedNodes")
    def enable_shielded_nodes(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_shielded_nodes.setter
    def enable_shielded_nodes(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableTpu")
    def enable_tpu(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_tpu.setter
    def enable_tpu(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enterpriseConfig")
    @_utilities.deprecated(...)
    def enterprise_config(self) -> Optional[pulumi.Input[ClusterEnterpriseConfigArgs]]:
        
        ...
    
    @enterprise_config.setter
    def enterprise_config(self, value: Optional[pulumi.Input[ClusterEnterpriseConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fleet(self) -> Optional[pulumi.Input[ClusterFleetArgs]]:
        
        ...
    
    @fleet.setter
    def fleet(self, value: Optional[pulumi.Input[ClusterFleetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayApiConfig")
    def gateway_api_config(self) -> Optional[pulumi.Input[ClusterGatewayApiConfigArgs]]:
        
        ...
    
    @gateway_api_config.setter
    def gateway_api_config(self, value: Optional[pulumi.Input[ClusterGatewayApiConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeAutoUpgradeConfig")
    def gke_auto_upgrade_config(self) -> Optional[pulumi.Input[ClusterGkeAutoUpgradeConfigArgs]]:
        
        ...
    
    @gke_auto_upgrade_config.setter
    def gke_auto_upgrade_config(self, value: Optional[pulumi.Input[ClusterGkeAutoUpgradeConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityServiceConfig")
    def identity_service_config(self) -> Optional[pulumi.Input[ClusterIdentityServiceConfigArgs]]:
        
        ...
    
    @identity_service_config.setter
    def identity_service_config(self, value: Optional[pulumi.Input[ClusterIdentityServiceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inTransitEncryptionConfig")
    def in_transit_encryption_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @in_transit_encryption_config.setter
    def in_transit_encryption_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialNodeCount")
    def initial_node_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @initial_node_count.setter
    def initial_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAllocationPolicy")
    def ip_allocation_policy(self) -> Optional[pulumi.Input[ClusterIpAllocationPolicyArgs]]:
        
        ...
    
    @ip_allocation_policy.setter
    def ip_allocation_policy(self, value: Optional[pulumi.Input[ClusterIpAllocationPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @label_fingerprint.setter
    def label_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input[ClusterLoggingConfigArgs]]:
        
        ...
    
    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input[ClusterLoggingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingService")
    def logging_service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @logging_service.setter
    def logging_service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(self) -> Optional[pulumi.Input[ClusterMaintenancePolicyArgs]]:
        
        ...
    
    @maintenance_policy.setter
    def maintenance_policy(self, value: Optional[pulumi.Input[ClusterMaintenancePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedOpentelemetryConfig")
    def managed_opentelemetry_config(self) -> Optional[pulumi.Input[ClusterManagedOpentelemetryConfigArgs]]:
        
        ...
    
    @managed_opentelemetry_config.setter
    def managed_opentelemetry_config(self, value: Optional[pulumi.Input[ClusterManagedOpentelemetryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAuth")
    def master_auth(self) -> Optional[pulumi.Input[ClusterMasterAuthArgs]]:
        
        ...
    
    @master_auth.setter
    def master_auth(self, value: Optional[pulumi.Input[ClusterMasterAuthArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAuthorizedNetworksConfig")
    def master_authorized_networks_config(self) -> Optional[pulumi.Input[ClusterMasterAuthorizedNetworksConfigArgs]]:
        
        ...
    
    @master_authorized_networks_config.setter
    def master_authorized_networks_config(self, value: Optional[pulumi.Input[ClusterMasterAuthorizedNetworksConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterVersion")
    def master_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_version.setter
    def master_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="meshCertificates")
    def mesh_certificates(self) -> Optional[pulumi.Input[ClusterMeshCertificatesArgs]]:
        
        ...
    
    @mesh_certificates.setter
    def mesh_certificates(self, value: Optional[pulumi.Input[ClusterMeshCertificatesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minMasterVersion")
    def min_master_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @min_master_version.setter
    def min_master_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringConfig")
    def monitoring_config(self) -> Optional[pulumi.Input[ClusterMonitoringConfigArgs]]:
        
        ...
    
    @monitoring_config.setter
    def monitoring_config(self, value: Optional[pulumi.Input[ClusterMonitoringConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringService")
    def monitoring_service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @monitoring_service.setter
    def monitoring_service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfig")
    def network_performance_config(self) -> Optional[pulumi.Input[ClusterNetworkPerformanceConfigArgs]]:
        
        ...
    
    @network_performance_config.setter
    def network_performance_config(self, value: Optional[pulumi.Input[ClusterNetworkPerformanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPolicy")
    def network_policy(self) -> Optional[pulumi.Input[ClusterNetworkPolicyArgs]]:
        
        ...
    
    @network_policy.setter
    def network_policy(self, value: Optional[pulumi.Input[ClusterNetworkPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkingMode")
    def networking_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @networking_mode.setter
    def networking_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[ClusterNodeConfigArgs]]:
        
        ...
    
    @node_config.setter
    def node_config(self, value: Optional[pulumi.Input[ClusterNodeConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeLocations")
    def node_locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @node_locations.setter
    def node_locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePoolAutoConfig")
    def node_pool_auto_config(self) -> Optional[pulumi.Input[ClusterNodePoolAutoConfigArgs]]:
        
        ...
    
    @node_pool_auto_config.setter
    def node_pool_auto_config(self, value: Optional[pulumi.Input[ClusterNodePoolAutoConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePoolDefaults")
    def node_pool_defaults(self) -> Optional[pulumi.Input[ClusterNodePoolDefaultsArgs]]:
        
        ...
    
    @node_pool_defaults.setter
    def node_pool_defaults(self, value: Optional[pulumi.Input[ClusterNodePoolDefaultsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePools")
    def node_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodePoolArgs]]]]:
        
        ...
    
    @node_pools.setter
    def node_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodePoolArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeVersion")
    def node_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_version.setter
    def node_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> Optional[pulumi.Input[ClusterNotificationConfigArgs]]:
        
        ...
    
    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input[ClusterNotificationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operation(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @operation.setter
    def operation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="podAutoscaling")
    def pod_autoscaling(self) -> Optional[pulumi.Input[ClusterPodAutoscalingArgs]]:
        
        ...
    
    @pod_autoscaling.setter
    def pod_autoscaling(self, value: Optional[pulumi.Input[ClusterPodAutoscalingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="podSecurityPolicyConfig")
    def pod_security_policy_config(self) -> Optional[pulumi.Input[ClusterPodSecurityPolicyConfigArgs]]:
        
        ...
    
    @pod_security_policy_config.setter
    def pod_security_policy_config(self, value: Optional[pulumi.Input[ClusterPodSecurityPolicyConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateClusterConfig")
    def private_cluster_config(self) -> Optional[pulumi.Input[ClusterPrivateClusterConfigArgs]]:
        
        ...
    
    @private_cluster_config.setter
    def private_cluster_config(self, value: Optional[pulumi.Input[ClusterPrivateClusterConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ipv6_google_access.setter
    def private_ipv6_google_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectConfig")
    def protect_config(self) -> Optional[pulumi.Input[ClusterProtectConfigArgs]]:
        
        ...
    
    @protect_config.setter
    def protect_config(self, value: Optional[pulumi.Input[ClusterProtectConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rbacBindingConfig")
    def rbac_binding_config(self) -> Optional[pulumi.Input[ClusterRbacBindingConfigArgs]]:
        
        ...
    
    @rbac_binding_config.setter
    def rbac_binding_config(self, value: Optional[pulumi.Input[ClusterRbacBindingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseChannel")
    def release_channel(self) -> Optional[pulumi.Input[ClusterReleaseChannelArgs]]:
        
        ...
    
    @release_channel.setter
    def release_channel(self, value: Optional[pulumi.Input[ClusterReleaseChannelArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="removeDefaultNodePool")
    def remove_default_node_pool(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @remove_default_node_pool.setter
    def remove_default_node_pool(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceLabels")
    def resource_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_labels.setter
    def resource_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceUsageExportConfig")
    def resource_usage_export_config(self) -> Optional[pulumi.Input[ClusterResourceUsageExportConfigArgs]]:
        
        ...
    
    @resource_usage_export_config.setter
    def resource_usage_export_config(self, value: Optional[pulumi.Input[ClusterResourceUsageExportConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretManagerConfig")
    def secret_manager_config(self) -> Optional[pulumi.Input[ClusterSecretManagerConfigArgs]]:
        
        ...
    
    @secret_manager_config.setter
    def secret_manager_config(self, value: Optional[pulumi.Input[ClusterSecretManagerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretSyncConfig")
    def secret_sync_config(self) -> Optional[pulumi.Input[ClusterSecretSyncConfigArgs]]:
        
        ...
    
    @secret_sync_config.setter
    def secret_sync_config(self, value: Optional[pulumi.Input[ClusterSecretSyncConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPostureConfig")
    def security_posture_config(self) -> Optional[pulumi.Input[ClusterSecurityPostureConfigArgs]]:
        
        ...
    
    @security_posture_config.setter
    def security_posture_config(self, value: Optional[pulumi.Input[ClusterSecurityPostureConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceExternalIpsConfig")
    def service_external_ips_config(self) -> Optional[pulumi.Input[ClusterServiceExternalIpsConfigArgs]]:
        
        ...
    
    @service_external_ips_config.setter
    def service_external_ips_config(self, value: Optional[pulumi.Input[ClusterServiceExternalIpsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicesIpv4Cidr")
    def services_ipv4_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @services_ipv4_cidr.setter
    def services_ipv4_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tpuConfig")
    def tpu_config(self) -> Optional[pulumi.Input[ClusterTpuConfigArgs]]:
        
        ...
    
    @tpu_config.setter
    def tpu_config(self, value: Optional[pulumi.Input[ClusterTpuConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tpuIpv4CidrBlock")
    def tpu_ipv4_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tpu_ipv4_cidr_block.setter
    def tpu_ipv4_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userManagedKeysConfig")
    def user_managed_keys_config(self) -> Optional[pulumi.Input[ClusterUserManagedKeysConfigArgs]]:
        
        ...
    
    @user_managed_keys_config.setter
    def user_managed_keys_config(self, value: Optional[pulumi.Input[ClusterUserManagedKeysConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verticalPodAutoscaling")
    def vertical_pod_autoscaling(self) -> Optional[pulumi.Input[ClusterVerticalPodAutoscalingArgs]]:
        
        ...
    
    @vertical_pod_autoscaling.setter
    def vertical_pod_autoscaling(self, value: Optional[pulumi.Input[ClusterVerticalPodAutoscalingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadAltsConfig")
    def workload_alts_config(self) -> Optional[pulumi.Input[ClusterWorkloadAltsConfigArgs]]:
        
        ...
    
    @workload_alts_config.setter
    def workload_alts_config(self, value: Optional[pulumi.Input[ClusterWorkloadAltsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityConfig")
    def workload_identity_config(self) -> Optional[pulumi.Input[ClusterWorkloadIdentityConfigArgs]]:
        
        ...
    
    @workload_identity_config.setter
    def workload_identity_config(self, value: Optional[pulumi.Input[ClusterWorkloadIdentityConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:container/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., addons_config: Optional[pulumi.Input[Union[ClusterAddonsConfigArgs, ClusterAddonsConfigArgsDict]]] = ..., allow_net_admin: Optional[pulumi.Input[_builtins.bool]] = ..., anonymous_authentication_config: Optional[pulumi.Input[Union[ClusterAnonymousAuthenticationConfigArgs, ClusterAnonymousAuthenticationConfigArgsDict]]] = ..., authenticator_groups_config: Optional[pulumi.Input[Union[ClusterAuthenticatorGroupsConfigArgs, ClusterAuthenticatorGroupsConfigArgsDict]]] = ..., binary_authorization: Optional[pulumi.Input[Union[ClusterBinaryAuthorizationArgs, ClusterBinaryAuthorizationArgsDict]]] = ..., cluster_autoscaling: Optional[pulumi.Input[Union[ClusterClusterAutoscalingArgs, ClusterClusterAutoscalingArgsDict]]] = ..., cluster_ipv4_cidr: Optional[pulumi.Input[_builtins.str]] = ..., cluster_telemetry: Optional[pulumi.Input[Union[ClusterClusterTelemetryArgs, ClusterClusterTelemetryArgsDict]]] = ..., confidential_nodes: Optional[pulumi.Input[Union[ClusterConfidentialNodesArgs, ClusterConfidentialNodesArgsDict]]] = ..., control_plane_endpoints_config: Optional[pulumi.Input[Union[ClusterControlPlaneEndpointsConfigArgs, ClusterControlPlaneEndpointsConfigArgsDict]]] = ..., cost_management_config: Optional[pulumi.Input[Union[ClusterCostManagementConfigArgs, ClusterCostManagementConfigArgsDict]]] = ..., database_encryption: Optional[pulumi.Input[Union[ClusterDatabaseEncryptionArgs, ClusterDatabaseEncryptionArgsDict]]] = ..., datapath_provider: Optional[pulumi.Input[_builtins.str]] = ..., default_max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ..., default_snat_status: Optional[pulumi.Input[Union[ClusterDefaultSnatStatusArgs, ClusterDefaultSnatStatusArgsDict]]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_l4_lb_firewall_reconciliation: Optional[pulumi.Input[_builtins.bool]] = ..., dns_config: Optional[pulumi.Input[Union[ClusterDnsConfigArgs, ClusterDnsConfigArgsDict]]] = ..., enable_autopilot: Optional[pulumi.Input[_builtins.bool]] = ..., enable_cilium_clusterwide_network_policy: Optional[pulumi.Input[_builtins.bool]] = ..., enable_fqdn_network_policy: Optional[pulumi.Input[_builtins.bool]] = ..., enable_intranode_visibility: Optional[pulumi.Input[_builtins.bool]] = ..., enable_k8s_beta_apis: Optional[pulumi.Input[Union[ClusterEnableK8sBetaApisArgs, ClusterEnableK8sBetaApisArgsDict]]] = ..., enable_kubernetes_alpha: Optional[pulumi.Input[_builtins.bool]] = ..., enable_l4_ilb_subsetting: Optional[pulumi.Input[_builtins.bool]] = ..., enable_legacy_abac: Optional[pulumi.Input[_builtins.bool]] = ..., enable_multi_networking: Optional[pulumi.Input[_builtins.bool]] = ..., enable_shielded_nodes: Optional[pulumi.Input[_builtins.bool]] = ..., enable_tpu: Optional[pulumi.Input[_builtins.bool]] = ..., enterprise_config: Optional[pulumi.Input[Union[ClusterEnterpriseConfigArgs, ClusterEnterpriseConfigArgsDict]]] = ..., fleet: Optional[pulumi.Input[Union[ClusterFleetArgs, ClusterFleetArgsDict]]] = ..., gateway_api_config: Optional[pulumi.Input[Union[ClusterGatewayApiConfigArgs, ClusterGatewayApiConfigArgsDict]]] = ..., gke_auto_upgrade_config: Optional[pulumi.Input[Union[ClusterGkeAutoUpgradeConfigArgs, ClusterGkeAutoUpgradeConfigArgsDict]]] = ..., identity_service_config: Optional[pulumi.Input[Union[ClusterIdentityServiceConfigArgs, ClusterIdentityServiceConfigArgsDict]]] = ..., in_transit_encryption_config: Optional[pulumi.Input[_builtins.str]] = ..., initial_node_count: Optional[pulumi.Input[_builtins.int]] = ..., ip_allocation_policy: Optional[pulumi.Input[Union[ClusterIpAllocationPolicyArgs, ClusterIpAllocationPolicyArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[Union[ClusterLoggingConfigArgs, ClusterLoggingConfigArgsDict]]] = ..., logging_service: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_policy: Optional[pulumi.Input[Union[ClusterMaintenancePolicyArgs, ClusterMaintenancePolicyArgsDict]]] = ..., managed_opentelemetry_config: Optional[pulumi.Input[Union[ClusterManagedOpentelemetryConfigArgs, ClusterManagedOpentelemetryConfigArgsDict]]] = ..., master_auth: Optional[pulumi.Input[Union[ClusterMasterAuthArgs, ClusterMasterAuthArgsDict]]] = ..., master_authorized_networks_config: Optional[pulumi.Input[Union[ClusterMasterAuthorizedNetworksConfigArgs, ClusterMasterAuthorizedNetworksConfigArgsDict]]] = ..., mesh_certificates: Optional[pulumi.Input[Union[ClusterMeshCertificatesArgs, ClusterMeshCertificatesArgsDict]]] = ..., min_master_version: Optional[pulumi.Input[_builtins.str]] = ..., monitoring_config: Optional[pulumi.Input[Union[ClusterMonitoringConfigArgs, ClusterMonitoringConfigArgsDict]]] = ..., monitoring_service: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., network_performance_config: Optional[pulumi.Input[Union[ClusterNetworkPerformanceConfigArgs, ClusterNetworkPerformanceConfigArgsDict]]] = ..., network_policy: Optional[pulumi.Input[Union[ClusterNetworkPolicyArgs, ClusterNetworkPolicyArgsDict]]] = ..., networking_mode: Optional[pulumi.Input[_builtins.str]] = ..., node_config: Optional[pulumi.Input[Union[ClusterNodeConfigArgs, ClusterNodeConfigArgsDict]]] = ..., node_locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., node_pool_auto_config: Optional[pulumi.Input[Union[ClusterNodePoolAutoConfigArgs, ClusterNodePoolAutoConfigArgsDict]]] = ..., node_pool_defaults: Optional[pulumi.Input[Union[ClusterNodePoolDefaultsArgs, ClusterNodePoolDefaultsArgsDict]]] = ..., node_pools: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterNodePoolArgs, ClusterNodePoolArgsDict]]]]] = ..., node_version: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[Union[ClusterNotificationConfigArgs, ClusterNotificationConfigArgsDict]]] = ..., pod_autoscaling: Optional[pulumi.Input[Union[ClusterPodAutoscalingArgs, ClusterPodAutoscalingArgsDict]]] = ..., pod_security_policy_config: Optional[pulumi.Input[Union[ClusterPodSecurityPolicyConfigArgs, ClusterPodSecurityPolicyConfigArgsDict]]] = ..., private_cluster_config: Optional[pulumi.Input[Union[ClusterPrivateClusterConfigArgs, ClusterPrivateClusterConfigArgsDict]]] = ..., private_ipv6_google_access: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protect_config: Optional[pulumi.Input[Union[ClusterProtectConfigArgs, ClusterProtectConfigArgsDict]]] = ..., rbac_binding_config: Optional[pulumi.Input[Union[ClusterRbacBindingConfigArgs, ClusterRbacBindingConfigArgsDict]]] = ..., release_channel: Optional[pulumi.Input[Union[ClusterReleaseChannelArgs, ClusterReleaseChannelArgsDict]]] = ..., remove_default_node_pool: Optional[pulumi.Input[_builtins.bool]] = ..., resource_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_usage_export_config: Optional[pulumi.Input[Union[ClusterResourceUsageExportConfigArgs, ClusterResourceUsageExportConfigArgsDict]]] = ..., secret_manager_config: Optional[pulumi.Input[Union[ClusterSecretManagerConfigArgs, ClusterSecretManagerConfigArgsDict]]] = ..., secret_sync_config: Optional[pulumi.Input[Union[ClusterSecretSyncConfigArgs, ClusterSecretSyncConfigArgsDict]]] = ..., security_posture_config: Optional[pulumi.Input[Union[ClusterSecurityPostureConfigArgs, ClusterSecurityPostureConfigArgsDict]]] = ..., service_external_ips_config: Optional[pulumi.Input[Union[ClusterServiceExternalIpsConfigArgs, ClusterServiceExternalIpsConfigArgsDict]]] = ..., subnetwork: Optional[pulumi.Input[_builtins.str]] = ..., tpu_config: Optional[pulumi.Input[Union[ClusterTpuConfigArgs, ClusterTpuConfigArgsDict]]] = ..., user_managed_keys_config: Optional[pulumi.Input[Union[ClusterUserManagedKeysConfigArgs, ClusterUserManagedKeysConfigArgsDict]]] = ..., vertical_pod_autoscaling: Optional[pulumi.Input[Union[ClusterVerticalPodAutoscalingArgs, ClusterVerticalPodAutoscalingArgsDict]]] = ..., workload_alts_config: Optional[pulumi.Input[Union[ClusterWorkloadAltsConfigArgs, ClusterWorkloadAltsConfigArgsDict]]] = ..., workload_identity_config: Optional[pulumi.Input[Union[ClusterWorkloadIdentityConfigArgs, ClusterWorkloadIdentityConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ClusterArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., addons_config: Optional[pulumi.Input[Union[ClusterAddonsConfigArgs, ClusterAddonsConfigArgsDict]]] = ..., allow_net_admin: Optional[pulumi.Input[_builtins.bool]] = ..., anonymous_authentication_config: Optional[pulumi.Input[Union[ClusterAnonymousAuthenticationConfigArgs, ClusterAnonymousAuthenticationConfigArgsDict]]] = ..., authenticator_groups_config: Optional[pulumi.Input[Union[ClusterAuthenticatorGroupsConfigArgs, ClusterAuthenticatorGroupsConfigArgsDict]]] = ..., binary_authorization: Optional[pulumi.Input[Union[ClusterBinaryAuthorizationArgs, ClusterBinaryAuthorizationArgsDict]]] = ..., cluster_autoscaling: Optional[pulumi.Input[Union[ClusterClusterAutoscalingArgs, ClusterClusterAutoscalingArgsDict]]] = ..., cluster_ipv4_cidr: Optional[pulumi.Input[_builtins.str]] = ..., cluster_telemetry: Optional[pulumi.Input[Union[ClusterClusterTelemetryArgs, ClusterClusterTelemetryArgsDict]]] = ..., confidential_nodes: Optional[pulumi.Input[Union[ClusterConfidentialNodesArgs, ClusterConfidentialNodesArgsDict]]] = ..., control_plane_endpoints_config: Optional[pulumi.Input[Union[ClusterControlPlaneEndpointsConfigArgs, ClusterControlPlaneEndpointsConfigArgsDict]]] = ..., cost_management_config: Optional[pulumi.Input[Union[ClusterCostManagementConfigArgs, ClusterCostManagementConfigArgsDict]]] = ..., database_encryption: Optional[pulumi.Input[Union[ClusterDatabaseEncryptionArgs, ClusterDatabaseEncryptionArgsDict]]] = ..., datapath_provider: Optional[pulumi.Input[_builtins.str]] = ..., default_max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ..., default_snat_status: Optional[pulumi.Input[Union[ClusterDefaultSnatStatusArgs, ClusterDefaultSnatStatusArgsDict]]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_l4_lb_firewall_reconciliation: Optional[pulumi.Input[_builtins.bool]] = ..., dns_config: Optional[pulumi.Input[Union[ClusterDnsConfigArgs, ClusterDnsConfigArgsDict]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_autopilot: Optional[pulumi.Input[_builtins.bool]] = ..., enable_cilium_clusterwide_network_policy: Optional[pulumi.Input[_builtins.bool]] = ..., enable_fqdn_network_policy: Optional[pulumi.Input[_builtins.bool]] = ..., enable_intranode_visibility: Optional[pulumi.Input[_builtins.bool]] = ..., enable_k8s_beta_apis: Optional[pulumi.Input[Union[ClusterEnableK8sBetaApisArgs, ClusterEnableK8sBetaApisArgsDict]]] = ..., enable_kubernetes_alpha: Optional[pulumi.Input[_builtins.bool]] = ..., enable_l4_ilb_subsetting: Optional[pulumi.Input[_builtins.bool]] = ..., enable_legacy_abac: Optional[pulumi.Input[_builtins.bool]] = ..., enable_multi_networking: Optional[pulumi.Input[_builtins.bool]] = ..., enable_shielded_nodes: Optional[pulumi.Input[_builtins.bool]] = ..., enable_tpu: Optional[pulumi.Input[_builtins.bool]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., enterprise_config: Optional[pulumi.Input[Union[ClusterEnterpriseConfigArgs, ClusterEnterpriseConfigArgsDict]]] = ..., fleet: Optional[pulumi.Input[Union[ClusterFleetArgs, ClusterFleetArgsDict]]] = ..., gateway_api_config: Optional[pulumi.Input[Union[ClusterGatewayApiConfigArgs, ClusterGatewayApiConfigArgsDict]]] = ..., gke_auto_upgrade_config: Optional[pulumi.Input[Union[ClusterGkeAutoUpgradeConfigArgs, ClusterGkeAutoUpgradeConfigArgsDict]]] = ..., identity_service_config: Optional[pulumi.Input[Union[ClusterIdentityServiceConfigArgs, ClusterIdentityServiceConfigArgsDict]]] = ..., in_transit_encryption_config: Optional[pulumi.Input[_builtins.str]] = ..., initial_node_count: Optional[pulumi.Input[_builtins.int]] = ..., ip_allocation_policy: Optional[pulumi.Input[Union[ClusterIpAllocationPolicyArgs, ClusterIpAllocationPolicyArgsDict]]] = ..., label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[Union[ClusterLoggingConfigArgs, ClusterLoggingConfigArgsDict]]] = ..., logging_service: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_policy: Optional[pulumi.Input[Union[ClusterMaintenancePolicyArgs, ClusterMaintenancePolicyArgsDict]]] = ..., managed_opentelemetry_config: Optional[pulumi.Input[Union[ClusterManagedOpentelemetryConfigArgs, ClusterManagedOpentelemetryConfigArgsDict]]] = ..., master_auth: Optional[pulumi.Input[Union[ClusterMasterAuthArgs, ClusterMasterAuthArgsDict]]] = ..., master_authorized_networks_config: Optional[pulumi.Input[Union[ClusterMasterAuthorizedNetworksConfigArgs, ClusterMasterAuthorizedNetworksConfigArgsDict]]] = ..., master_version: Optional[pulumi.Input[_builtins.str]] = ..., mesh_certificates: Optional[pulumi.Input[Union[ClusterMeshCertificatesArgs, ClusterMeshCertificatesArgsDict]]] = ..., min_master_version: Optional[pulumi.Input[_builtins.str]] = ..., monitoring_config: Optional[pulumi.Input[Union[ClusterMonitoringConfigArgs, ClusterMonitoringConfigArgsDict]]] = ..., monitoring_service: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., network_performance_config: Optional[pulumi.Input[Union[ClusterNetworkPerformanceConfigArgs, ClusterNetworkPerformanceConfigArgsDict]]] = ..., network_policy: Optional[pulumi.Input[Union[ClusterNetworkPolicyArgs, ClusterNetworkPolicyArgsDict]]] = ..., networking_mode: Optional[pulumi.Input[_builtins.str]] = ..., node_config: Optional[pulumi.Input[Union[ClusterNodeConfigArgs, ClusterNodeConfigArgsDict]]] = ..., node_locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., node_pool_auto_config: Optional[pulumi.Input[Union[ClusterNodePoolAutoConfigArgs, ClusterNodePoolAutoConfigArgsDict]]] = ..., node_pool_defaults: Optional[pulumi.Input[Union[ClusterNodePoolDefaultsArgs, ClusterNodePoolDefaultsArgsDict]]] = ..., node_pools: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterNodePoolArgs, ClusterNodePoolArgsDict]]]]] = ..., node_version: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[Union[ClusterNotificationConfigArgs, ClusterNotificationConfigArgsDict]]] = ..., operation: Optional[pulumi.Input[_builtins.str]] = ..., pod_autoscaling: Optional[pulumi.Input[Union[ClusterPodAutoscalingArgs, ClusterPodAutoscalingArgsDict]]] = ..., pod_security_policy_config: Optional[pulumi.Input[Union[ClusterPodSecurityPolicyConfigArgs, ClusterPodSecurityPolicyConfigArgsDict]]] = ..., private_cluster_config: Optional[pulumi.Input[Union[ClusterPrivateClusterConfigArgs, ClusterPrivateClusterConfigArgsDict]]] = ..., private_ipv6_google_access: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protect_config: Optional[pulumi.Input[Union[ClusterProtectConfigArgs, ClusterProtectConfigArgsDict]]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., rbac_binding_config: Optional[pulumi.Input[Union[ClusterRbacBindingConfigArgs, ClusterRbacBindingConfigArgsDict]]] = ..., release_channel: Optional[pulumi.Input[Union[ClusterReleaseChannelArgs, ClusterReleaseChannelArgsDict]]] = ..., remove_default_node_pool: Optional[pulumi.Input[_builtins.bool]] = ..., resource_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_usage_export_config: Optional[pulumi.Input[Union[ClusterResourceUsageExportConfigArgs, ClusterResourceUsageExportConfigArgsDict]]] = ..., secret_manager_config: Optional[pulumi.Input[Union[ClusterSecretManagerConfigArgs, ClusterSecretManagerConfigArgsDict]]] = ..., secret_sync_config: Optional[pulumi.Input[Union[ClusterSecretSyncConfigArgs, ClusterSecretSyncConfigArgsDict]]] = ..., security_posture_config: Optional[pulumi.Input[Union[ClusterSecurityPostureConfigArgs, ClusterSecurityPostureConfigArgsDict]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., service_external_ips_config: Optional[pulumi.Input[Union[ClusterServiceExternalIpsConfigArgs, ClusterServiceExternalIpsConfigArgsDict]]] = ..., services_ipv4_cidr: Optional[pulumi.Input[_builtins.str]] = ..., subnetwork: Optional[pulumi.Input[_builtins.str]] = ..., tpu_config: Optional[pulumi.Input[Union[ClusterTpuConfigArgs, ClusterTpuConfigArgsDict]]] = ..., tpu_ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., user_managed_keys_config: Optional[pulumi.Input[Union[ClusterUserManagedKeysConfigArgs, ClusterUserManagedKeysConfigArgsDict]]] = ..., vertical_pod_autoscaling: Optional[pulumi.Input[Union[ClusterVerticalPodAutoscalingArgs, ClusterVerticalPodAutoscalingArgsDict]]] = ..., workload_alts_config: Optional[pulumi.Input[Union[ClusterWorkloadAltsConfigArgs, ClusterWorkloadAltsConfigArgsDict]]] = ..., workload_identity_config: Optional[pulumi.Input[Union[ClusterWorkloadIdentityConfigArgs, ClusterWorkloadIdentityConfigArgsDict]]] = ...) -> Cluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonsConfig")
    def addons_config(self) -> pulumi.Output[outputs.ClusterAddonsConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowNetAdmin")
    def allow_net_admin(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anonymousAuthenticationConfig")
    def anonymous_authentication_config(self) -> pulumi.Output[outputs.ClusterAnonymousAuthenticationConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticatorGroupsConfig")
    def authenticator_groups_config(self) -> pulumi.Output[outputs.ClusterAuthenticatorGroupsConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(self) -> pulumi.Output[Optional[outputs.ClusterBinaryAuthorization]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterAutoscaling")
    def cluster_autoscaling(self) -> pulumi.Output[outputs.ClusterClusterAutoscaling]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIpv4Cidr")
    def cluster_ipv4_cidr(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterTelemetry")
    def cluster_telemetry(self) -> pulumi.Output[outputs.ClusterClusterTelemetry]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialNodes")
    def confidential_nodes(self) -> pulumi.Output[outputs.ClusterConfidentialNodes]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneEndpointsConfig")
    def control_plane_endpoints_config(self) -> pulumi.Output[outputs.ClusterControlPlaneEndpointsConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="costManagementConfig")
    def cost_management_config(self) -> pulumi.Output[outputs.ClusterCostManagementConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseEncryption")
    def database_encryption(self) -> pulumi.Output[outputs.ClusterDatabaseEncryption]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datapathProvider")
    def datapath_provider(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultMaxPodsPerNode")
    def default_max_pods_per_node(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSnatStatus")
    def default_snat_status(self) -> pulumi.Output[outputs.ClusterDefaultSnatStatus]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableL4LbFirewallReconciliation")
    def disable_l4_lb_firewall_reconciliation(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> pulumi.Output[Optional[outputs.ClusterDnsConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutopilot")
    def enable_autopilot(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCiliumClusterwideNetworkPolicy")
    def enable_cilium_clusterwide_network_policy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableFqdnNetworkPolicy")
    def enable_fqdn_network_policy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIntranodeVisibility")
    def enable_intranode_visibility(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableK8sBetaApis")
    def enable_k8s_beta_apis(self) -> pulumi.Output[Optional[outputs.ClusterEnableK8sBetaApis]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableKubernetesAlpha")
    def enable_kubernetes_alpha(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableL4IlbSubsetting")
    def enable_l4_ilb_subsetting(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLegacyAbac")
    def enable_legacy_abac(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMultiNetworking")
    def enable_multi_networking(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableShieldedNodes")
    def enable_shielded_nodes(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableTpu")
    def enable_tpu(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enterpriseConfig")
    @_utilities.deprecated(...)
    def enterprise_config(self) -> pulumi.Output[outputs.ClusterEnterpriseConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fleet(self) -> pulumi.Output[Optional[outputs.ClusterFleet]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayApiConfig")
    def gateway_api_config(self) -> pulumi.Output[outputs.ClusterGatewayApiConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeAutoUpgradeConfig")
    def gke_auto_upgrade_config(self) -> pulumi.Output[outputs.ClusterGkeAutoUpgradeConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityServiceConfig")
    def identity_service_config(self) -> pulumi.Output[outputs.ClusterIdentityServiceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inTransitEncryptionConfig")
    def in_transit_encryption_config(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialNodeCount")
    def initial_node_count(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAllocationPolicy")
    def ip_allocation_policy(self) -> pulumi.Output[outputs.ClusterIpAllocationPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> pulumi.Output[outputs.ClusterLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingService")
    def logging_service(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(self) -> pulumi.Output[Optional[outputs.ClusterMaintenancePolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedOpentelemetryConfig")
    def managed_opentelemetry_config(self) -> pulumi.Output[outputs.ClusterManagedOpentelemetryConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAuth")
    def master_auth(self) -> pulumi.Output[outputs.ClusterMasterAuth]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAuthorizedNetworksConfig")
    def master_authorized_networks_config(self) -> pulumi.Output[outputs.ClusterMasterAuthorizedNetworksConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterVersion")
    def master_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="meshCertificates")
    def mesh_certificates(self) -> pulumi.Output[outputs.ClusterMeshCertificates]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minMasterVersion")
    def min_master_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringConfig")
    def monitoring_config(self) -> pulumi.Output[outputs.ClusterMonitoringConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringService")
    def monitoring_service(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfig")
    def network_performance_config(self) -> pulumi.Output[Optional[outputs.ClusterNetworkPerformanceConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPolicy")
    def network_policy(self) -> pulumi.Output[Optional[outputs.ClusterNetworkPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkingMode")
    def networking_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> pulumi.Output[outputs.ClusterNodeConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeLocations")
    def node_locations(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePoolAutoConfig")
    def node_pool_auto_config(self) -> pulumi.Output[outputs.ClusterNodePoolAutoConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePoolDefaults")
    def node_pool_defaults(self) -> pulumi.Output[outputs.ClusterNodePoolDefaults]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePools")
    def node_pools(self) -> pulumi.Output[Sequence[outputs.ClusterNodePool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeVersion")
    def node_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> pulumi.Output[outputs.ClusterNotificationConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operation(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="podAutoscaling")
    def pod_autoscaling(self) -> pulumi.Output[outputs.ClusterPodAutoscaling]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="podSecurityPolicyConfig")
    def pod_security_policy_config(self) -> pulumi.Output[Optional[outputs.ClusterPodSecurityPolicyConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateClusterConfig")
    def private_cluster_config(self) -> pulumi.Output[outputs.ClusterPrivateClusterConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectConfig")
    def protect_config(self) -> pulumi.Output[outputs.ClusterProtectConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rbacBindingConfig")
    def rbac_binding_config(self) -> pulumi.Output[outputs.ClusterRbacBindingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseChannel")
    def release_channel(self) -> pulumi.Output[outputs.ClusterReleaseChannel]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="removeDefaultNodePool")
    def remove_default_node_pool(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceLabels")
    def resource_labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceUsageExportConfig")
    def resource_usage_export_config(self) -> pulumi.Output[Optional[outputs.ClusterResourceUsageExportConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretManagerConfig")
    def secret_manager_config(self) -> pulumi.Output[Optional[outputs.ClusterSecretManagerConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretSyncConfig")
    def secret_sync_config(self) -> pulumi.Output[Optional[outputs.ClusterSecretSyncConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPostureConfig")
    def security_posture_config(self) -> pulumi.Output[outputs.ClusterSecurityPostureConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceExternalIpsConfig")
    def service_external_ips_config(self) -> pulumi.Output[outputs.ClusterServiceExternalIpsConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicesIpv4Cidr")
    def services_ipv4_cidr(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tpuConfig")
    def tpu_config(self) -> pulumi.Output[outputs.ClusterTpuConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tpuIpv4CidrBlock")
    def tpu_ipv4_cidr_block(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userManagedKeysConfig")
    def user_managed_keys_config(self) -> pulumi.Output[Optional[outputs.ClusterUserManagedKeysConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verticalPodAutoscaling")
    def vertical_pod_autoscaling(self) -> pulumi.Output[outputs.ClusterVerticalPodAutoscaling]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadAltsConfig")
    def workload_alts_config(self) -> pulumi.Output[outputs.ClusterWorkloadAltsConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityConfig")
    def workload_identity_config(self) -> pulumi.Output[outputs.ClusterWorkloadIdentityConfig]:
        
        ...
    


