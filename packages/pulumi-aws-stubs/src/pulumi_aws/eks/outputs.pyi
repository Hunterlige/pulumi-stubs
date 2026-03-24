

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccessPolicyAssociationAccessScope', 'AddonPodIdentityAssociation', 'CapabilityConfiguration', 'CapabilityConfigurationArgoCd', 'CapabilityConfigurationArgoCdAwsIdc', 'CapabilityConfigurationArgoCdNetworkAccess', 'CapabilityConfigurationArgoCdRbacRoleMapping', ..., 'CapabilityTimeouts', 'ClusterAccessConfig', 'ClusterCertificateAuthority', 'ClusterComputeConfig', 'ClusterControlPlaneScalingConfig', 'ClusterEncryptionConfig', 'ClusterEncryptionConfigProvider', 'ClusterIdentity', 'ClusterIdentityOidc', 'ClusterKubernetesNetworkConfig', 'ClusterKubernetesNetworkConfigElasticLoadBalancing', 'ClusterOutpostConfig', 'ClusterOutpostConfigControlPlanePlacement', 'ClusterRemoteNetworkConfig', 'ClusterRemoteNetworkConfigRemoteNodeNetworks', 'ClusterRemoteNetworkConfigRemotePodNetworks', 'ClusterStorageConfig', 'ClusterStorageConfigBlockStorage', 'ClusterUpgradePolicy', 'ClusterVpcConfig', 'ClusterZonalShiftConfig', 'FargateProfileSelector', 'IdentityProviderConfigOidc', 'NodeGroupLaunchTemplate', 'NodeGroupNodeRepairConfig', 'NodeGroupNodeRepairConfigNodeRepairConfigOverride', 'NodeGroupRemoteAccess', 'NodeGroupResource', 'NodeGroupResourceAutoscalingGroup', 'NodeGroupScalingConfig', 'NodeGroupTaint', 'NodeGroupUpdateConfig', 'GetAddonPodIdentityAssociationResult', 'GetClusterAccessConfigResult', 'GetClusterCertificateAuthorityResult', 'GetClusterComputeConfigResult', 'GetClusterControlPlaneScalingConfigResult', 'GetClusterIdentityResult', 'GetClusterIdentityOidcResult', 'GetClusterKubernetesNetworkConfigResult', ..., 'GetClusterOutpostConfigResult', 'GetClusterOutpostConfigControlPlanePlacementResult', 'GetClusterRemoteNetworkConfigResult', ..., ..., 'GetClusterStorageConfigResult', 'GetClusterStorageConfigBlockStorageResult', 'GetClusterUpgradePolicyResult', 'GetClusterVersionsClusterVersionResult', 'GetClusterVpcConfigResult', 'GetClusterZonalShiftConfigResult', 'GetNodeGroupLaunchTemplateResult', 'GetNodeGroupRemoteAccessResult', 'GetNodeGroupResourceResult', 'GetNodeGroupResourceAutoscalingGroupResult', 'GetNodeGroupScalingConfigResult', 'GetNodeGroupTaintResult', 'GetNodeGroupUpdateConfigResult']
@pulumi.output_type
class AccessPolicyAssociationAccessScope(dict):
    def __init__(__self__, *, type: _builtins.str, namespaces: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespaces(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class AddonPodIdentityAssociation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, service_account: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CapabilityConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, argo_cd: Optional[outputs.CapabilityConfigurationArgoCd] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="argoCd")
    def argo_cd(self) -> Optional[outputs.CapabilityConfigurationArgoCd]:
        
        ...
    


@pulumi.output_type
class CapabilityConfigurationArgoCd(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_idc: outputs.CapabilityConfigurationArgoCdAwsIdc, namespace: Optional[_builtins.str] = ..., network_access: Optional[outputs.CapabilityConfigurationArgoCdNetworkAccess] = ..., rbac_role_mappings: Optional[Sequence[outputs.CapabilityConfigurationArgoCdRbacRoleMapping]] = ..., server_url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsIdc")
    def aws_idc(self) -> outputs.CapabilityConfigurationArgoCdAwsIdc:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAccess")
    def network_access(self) -> Optional[outputs.CapabilityConfigurationArgoCdNetworkAccess]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rbacRoleMappings")
    def rbac_role_mappings(self) -> Optional[Sequence[outputs.CapabilityConfigurationArgoCdRbacRoleMapping]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverUrl")
    def server_url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CapabilityConfigurationArgoCdAwsIdc(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, idc_instance_arn: _builtins.str, idc_managed_application_arn: Optional[_builtins.str] = ..., idc_region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idcInstanceArn")
    def idc_instance_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idcManagedApplicationArn")
    def idc_managed_application_arn(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idcRegion")
    def idc_region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CapabilityConfigurationArgoCdNetworkAccess(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, vpce_ids: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpceIds")
    def vpce_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class CapabilityConfigurationArgoCdRbacRoleMapping(dict):
    def __init__(__self__, *, identities: Sequence[outputs.CapabilityConfigurationArgoCdRbacRoleMappingIdentity], role: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Sequence[outputs.CapabilityConfigurationArgoCdRbacRoleMappingIdentity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CapabilityConfigurationArgoCdRbacRoleMappingIdentity(dict):
    def __init__(__self__, *, id: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CapabilityTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterAccessConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authentication_mode: Optional[_builtins.str] = ..., bootstrap_cluster_creator_admin_permissions: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapClusterCreatorAdminPermissions")
    def bootstrap_cluster_creator_admin_permissions(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ClusterCertificateAuthority(dict):
    def __init__(__self__, *, data: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterComputeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., node_pools: Optional[Sequence[_builtins.str]] = ..., node_role_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePools")
    def node_pools(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeRoleArn")
    def node_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterControlPlaneScalingConfig(dict):
    def __init__(__self__, *, tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterEncryptionConfig(dict):
    def __init__(__self__, *, provider: outputs.ClusterEncryptionConfigProvider, resources: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def provider(self) -> outputs.ClusterEncryptionConfigProvider:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterEncryptionConfigProvider(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyArn")
    def key_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClusterIdentity(dict):
    def __init__(__self__, *, oidcs: Optional[Sequence[outputs.ClusterIdentityOidc]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def oidcs(self) -> Optional[Sequence[outputs.ClusterIdentityOidc]]:
        
        ...
    


@pulumi.output_type
class ClusterIdentityOidc(dict):
    def __init__(__self__, *, issuer: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterKubernetesNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, elastic_load_balancing: Optional[outputs.ClusterKubernetesNetworkConfigElasticLoadBalancing] = ..., ip_family: Optional[_builtins.str] = ..., service_ipv4_cidr: Optional[_builtins.str] = ..., service_ipv6_cidr: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticLoadBalancing")
    def elastic_load_balancing(self) -> Optional[outputs.ClusterKubernetesNetworkConfigElasticLoadBalancing]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipFamily")
    def ip_family(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceIpv4Cidr")
    def service_ipv4_cidr(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceIpv6Cidr")
    def service_ipv6_cidr(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterKubernetesNetworkConfigElasticLoadBalancing(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ClusterOutpostConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, control_plane_instance_type: _builtins.str, outpost_arns: Sequence[_builtins.str], control_plane_placement: Optional[outputs.ClusterOutpostConfigControlPlanePlacement] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneInstanceType")
    def control_plane_instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArns")
    def outpost_arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlanePlacement")
    def control_plane_placement(self) -> Optional[outputs.ClusterOutpostConfigControlPlanePlacement]:
        
        ...
    


@pulumi.output_type
class ClusterOutpostConfigControlPlanePlacement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClusterRemoteNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, remote_node_networks: outputs.ClusterRemoteNetworkConfigRemoteNodeNetworks, remote_pod_networks: Optional[outputs.ClusterRemoteNetworkConfigRemotePodNetworks] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteNodeNetworks")
    def remote_node_networks(self) -> outputs.ClusterRemoteNetworkConfigRemoteNodeNetworks:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remotePodNetworks")
    def remote_pod_networks(self) -> Optional[outputs.ClusterRemoteNetworkConfigRemotePodNetworks]:
        
        ...
    


@pulumi.output_type
class ClusterRemoteNetworkConfigRemoteNodeNetworks(dict):
    def __init__(__self__, *, cidrs: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidrs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ClusterRemoteNetworkConfigRemotePodNetworks(dict):
    def __init__(__self__, *, cidrs: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidrs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ClusterStorageConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, block_storage: Optional[outputs.ClusterStorageConfigBlockStorage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockStorage")
    def block_storage(self) -> Optional[outputs.ClusterStorageConfigBlockStorage]:
        
        ...
    


@pulumi.output_type
class ClusterStorageConfigBlockStorage(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ClusterUpgradePolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, support_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportType")
    def support_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterVpcConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnet_ids: Sequence[_builtins.str], cluster_security_group_id: Optional[_builtins.str] = ..., endpoint_private_access: Optional[_builtins.bool] = ..., endpoint_public_access: Optional[_builtins.bool] = ..., public_access_cidrs: Optional[Sequence[_builtins.str]] = ..., security_group_ids: Optional[Sequence[_builtins.str]] = ..., vpc_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterSecurityGroupId")
    def cluster_security_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointPrivateAccess")
    def endpoint_private_access(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointPublicAccess")
    def endpoint_public_access(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicAccessCidrs")
    def public_access_cidrs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterZonalShiftConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class FargateProfileSelector(dict):
    def __init__(__self__, *, namespace: _builtins.str, labels: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class IdentityProviderConfigOidc(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, identity_provider_config_name: _builtins.str, issuer_url: _builtins.str, groups_claim: Optional[_builtins.str] = ..., groups_prefix: Optional[_builtins.str] = ..., required_claims: Optional[Mapping[str, _builtins.str]] = ..., username_claim: Optional[_builtins.str] = ..., username_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityProviderConfigName")
    def identity_provider_config_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuerUrl")
    def issuer_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupsClaim")
    def groups_claim(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupsPrefix")
    def groups_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredClaims")
    def required_claims(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usernameClaim")
    def username_claim(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usernamePrefix")
    def username_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NodeGroupLaunchTemplate(dict):
    def __init__(__self__, *, version: _builtins.str, id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NodeGroupNodeRepairConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., max_parallel_nodes_repaired_count: Optional[_builtins.int] = ..., max_parallel_nodes_repaired_percentage: Optional[_builtins.int] = ..., max_unhealthy_node_threshold_count: Optional[_builtins.int] = ..., max_unhealthy_node_threshold_percentage: Optional[_builtins.int] = ..., node_repair_config_overrides: Optional[Sequence[outputs.NodeGroupNodeRepairConfigNodeRepairConfigOverride]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxParallelNodesRepairedCount")
    def max_parallel_nodes_repaired_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxParallelNodesRepairedPercentage")
    def max_parallel_nodes_repaired_percentage(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUnhealthyNodeThresholdCount")
    def max_unhealthy_node_threshold_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUnhealthyNodeThresholdPercentage")
    def max_unhealthy_node_threshold_percentage(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeRepairConfigOverrides")
    def node_repair_config_overrides(self) -> Optional[Sequence[outputs.NodeGroupNodeRepairConfigNodeRepairConfigOverride]]:
        
        ...
    


@pulumi.output_type
class NodeGroupNodeRepairConfigNodeRepairConfigOverride(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, min_repair_wait_time_mins: _builtins.int, node_monitoring_condition: _builtins.str, node_unhealthy_reason: _builtins.str, repair_action: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minRepairWaitTimeMins")
    def min_repair_wait_time_mins(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeMonitoringCondition")
    def node_monitoring_condition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeUnhealthyReason")
    def node_unhealthy_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repairAction")
    def repair_action(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class NodeGroupRemoteAccess(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ec2_ssh_key: Optional[_builtins.str] = ..., source_security_group_ids: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2SshKey")
    def ec2_ssh_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSecurityGroupIds")
    def source_security_group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class NodeGroupResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscaling_groups: Optional[Sequence[outputs.NodeGroupResourceAutoscalingGroup]] = ..., remote_access_security_group_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroups")
    def autoscaling_groups(self) -> Optional[Sequence[outputs.NodeGroupResourceAutoscalingGroup]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteAccessSecurityGroupId")
    def remote_access_security_group_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NodeGroupResourceAutoscalingGroup(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NodeGroupScalingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, desired_size: _builtins.int, max_size: _builtins.int, min_size: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredSize")
    def desired_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class NodeGroupTaint(dict):
    def __init__(__self__, *, effect: _builtins.str, key: _builtins.str, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def effect(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NodeGroupUpdateConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_unavailable: Optional[_builtins.int] = ..., max_unavailable_percentage: Optional[_builtins.int] = ..., update_strategy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUnavailable")
    def max_unavailable(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUnavailablePercentage")
    def max_unavailable_percentage(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateStrategy")
    def update_strategy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetAddonPodIdentityAssociationResult(dict):
    def __init__(__self__, *, role_arn: _builtins.str, service_account: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetClusterAccessConfigResult(dict):
    def __init__(__self__, *, authentication_mode: _builtins.str, bootstrap_cluster_creator_admin_permissions: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapClusterCreatorAdminPermissions")
    def bootstrap_cluster_creator_admin_permissions(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetClusterCertificateAuthorityResult(dict):
    def __init__(__self__, *, data: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetClusterComputeConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool, node_pools: Sequence[_builtins.str], node_role_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePools")
    def node_pools(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeRoleArn")
    def node_role_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetClusterControlPlaneScalingConfigResult(dict):
    def __init__(__self__, *, tier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetClusterIdentityResult(dict):
    def __init__(__self__, *, oidcs: Sequence[outputs.GetClusterIdentityOidcResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def oidcs(self) -> Sequence[outputs.GetClusterIdentityOidcResult]:
        
        ...
    


@pulumi.output_type
class GetClusterIdentityOidcResult(dict):
    def __init__(__self__, *, issuer: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetClusterKubernetesNetworkConfigResult(dict):
    def __init__(__self__, *, elastic_load_balancings: Sequence[outputs.GetClusterKubernetesNetworkConfigElasticLoadBalancingResult], ip_family: _builtins.str, service_ipv4_cidr: _builtins.str, service_ipv6_cidr: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticLoadBalancings")
    def elastic_load_balancings(self) -> Sequence[outputs.GetClusterKubernetesNetworkConfigElasticLoadBalancingResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipFamily")
    def ip_family(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceIpv4Cidr")
    def service_ipv4_cidr(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceIpv6Cidr")
    def service_ipv6_cidr(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetClusterKubernetesNetworkConfigElasticLoadBalancingResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetClusterOutpostConfigResult(dict):
    def __init__(__self__, *, control_plane_instance_type: _builtins.str, control_plane_placements: Sequence[outputs.GetClusterOutpostConfigControlPlanePlacementResult], outpost_arns: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneInstanceType")
    def control_plane_instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlanePlacements")
    def control_plane_placements(self) -> Sequence[outputs.GetClusterOutpostConfigControlPlanePlacementResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArns")
    def outpost_arns(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetClusterOutpostConfigControlPlanePlacementResult(dict):
    def __init__(__self__, *, group_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetClusterRemoteNetworkConfigResult(dict):
    def __init__(__self__, *, remote_node_networks: Sequence[outputs.GetClusterRemoteNetworkConfigRemoteNodeNetworkResult], remote_pod_networks: Sequence[outputs.GetClusterRemoteNetworkConfigRemotePodNetworkResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteNodeNetworks")
    def remote_node_networks(self) -> Sequence[outputs.GetClusterRemoteNetworkConfigRemoteNodeNetworkResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remotePodNetworks")
    def remote_pod_networks(self) -> Sequence[outputs.GetClusterRemoteNetworkConfigRemotePodNetworkResult]:
        
        ...
    


@pulumi.output_type
class GetClusterRemoteNetworkConfigRemoteNodeNetworkResult(dict):
    def __init__(__self__, *, cidrs: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidrs(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetClusterRemoteNetworkConfigRemotePodNetworkResult(dict):
    def __init__(__self__, *, cidrs: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidrs(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetClusterStorageConfigResult(dict):
    def __init__(__self__, *, block_storages: Sequence[outputs.GetClusterStorageConfigBlockStorageResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockStorages")
    def block_storages(self) -> Sequence[outputs.GetClusterStorageConfigBlockStorageResult]:
        
        ...
    


@pulumi.output_type
class GetClusterStorageConfigBlockStorageResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetClusterUpgradePolicyResult(dict):
    def __init__(__self__, *, support_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportType")
    def support_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetClusterVersionsClusterVersionResult(dict):
    def __init__(__self__, *, cluster_type: _builtins.str, cluster_version: _builtins.str, default_platform_version: _builtins.str, default_version: _builtins.bool, end_of_extended_support_date: _builtins.str, end_of_standard_support_date: _builtins.str, kubernetes_patch_version: _builtins.str, release_date: _builtins.str, version_status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultPlatformVersion")
    def default_platform_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endOfExtendedSupportDate")
    def end_of_extended_support_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endOfStandardSupportDate")
    def end_of_standard_support_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesPatchVersion")
    def kubernetes_patch_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseDate")
    def release_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionStatus")
    def version_status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetClusterVpcConfigResult(dict):
    def __init__(__self__, *, cluster_security_group_id: _builtins.str, endpoint_private_access: _builtins.bool, endpoint_public_access: _builtins.bool, public_access_cidrs: Sequence[_builtins.str], security_group_ids: Sequence[_builtins.str], subnet_ids: Sequence[_builtins.str], vpc_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterSecurityGroupId")
    def cluster_security_group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointPrivateAccess")
    def endpoint_private_access(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointPublicAccess")
    def endpoint_public_access(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicAccessCidrs")
    def public_access_cidrs(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetClusterZonalShiftConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetNodeGroupLaunchTemplateResult(dict):
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, version: _builtins.str) -> None:
        
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
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNodeGroupRemoteAccessResult(dict):
    def __init__(__self__, *, ec2_ssh_key: _builtins.str, source_security_group_ids: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2SshKey")
    def ec2_ssh_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSecurityGroupIds")
    def source_security_group_ids(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetNodeGroupResourceResult(dict):
    def __init__(__self__, *, autoscaling_groups: Sequence[outputs.GetNodeGroupResourceAutoscalingGroupResult], remote_access_security_group_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroups")
    def autoscaling_groups(self) -> Sequence[outputs.GetNodeGroupResourceAutoscalingGroupResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteAccessSecurityGroupId")
    def remote_access_security_group_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNodeGroupResourceAutoscalingGroupResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNodeGroupScalingConfigResult(dict):
    def __init__(__self__, *, desired_size: _builtins.int, max_size: _builtins.int, min_size: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredSize")
    def desired_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetNodeGroupTaintResult(dict):
    def __init__(__self__, *, effect: _builtins.str, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def effect(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNodeGroupUpdateConfigResult(dict):
    def __init__(__self__, *, max_unavailable: _builtins.int, max_unavailable_percentage: _builtins.int, update_strategy: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUnavailable")
    def max_unavailable(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUnavailablePercentage")
    def max_unavailable_percentage(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateStrategy")
    def update_strategy(self) -> _builtins.str:
        ...
    


