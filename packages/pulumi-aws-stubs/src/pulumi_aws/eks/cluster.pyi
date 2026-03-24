

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
    def __init__(__self__, *, role_arn: pulumi.Input[_builtins.str], vpc_config: pulumi.Input[ClusterVpcConfigArgs], access_config: Optional[pulumi.Input[ClusterAccessConfigArgs]] = ..., bootstrap_self_managed_addons: Optional[pulumi.Input[_builtins.bool]] = ..., compute_config: Optional[pulumi.Input[ClusterComputeConfigArgs]] = ..., control_plane_scaling_config: Optional[pulumi.Input[ClusterControlPlaneScalingConfigArgs]] = ..., default_addons_to_removes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., enabled_cluster_log_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., encryption_config: Optional[pulumi.Input[ClusterEncryptionConfigArgs]] = ..., force_update_version: Optional[pulumi.Input[_builtins.bool]] = ..., kubernetes_network_config: Optional[pulumi.Input[ClusterKubernetesNetworkConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., outpost_config: Optional[pulumi.Input[ClusterOutpostConfigArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., remote_network_config: Optional[pulumi.Input[ClusterRemoteNetworkConfigArgs]] = ..., storage_config: Optional[pulumi.Input[ClusterStorageConfigArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., upgrade_policy: Optional[pulumi.Input[ClusterUpgradePolicyArgs]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., zonal_shift_config: Optional[pulumi.Input[ClusterZonalShiftConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Input[ClusterVpcConfigArgs]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: pulumi.Input[ClusterVpcConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessConfig")
    def access_config(self) -> Optional[pulumi.Input[ClusterAccessConfigArgs]]:
        
        ...
    
    @access_config.setter
    def access_config(self, value: Optional[pulumi.Input[ClusterAccessConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapSelfManagedAddons")
    def bootstrap_self_managed_addons(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bootstrap_self_managed_addons.setter
    def bootstrap_self_managed_addons(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeConfig")
    def compute_config(self) -> Optional[pulumi.Input[ClusterComputeConfigArgs]]:
        
        ...
    
    @compute_config.setter
    def compute_config(self, value: Optional[pulumi.Input[ClusterComputeConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneScalingConfig")
    def control_plane_scaling_config(self) -> Optional[pulumi.Input[ClusterControlPlaneScalingConfigArgs]]:
        
        ...
    
    @control_plane_scaling_config.setter
    def control_plane_scaling_config(self, value: Optional[pulumi.Input[ClusterControlPlaneScalingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAddonsToRemoves")
    @_utilities.deprecated(...)
    def default_addons_to_removes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @default_addons_to_removes.setter
    def default_addons_to_removes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledClusterLogTypes")
    def enabled_cluster_log_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @enabled_cluster_log_types.setter
    def enabled_cluster_log_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[pulumi.Input[ClusterEncryptionConfigArgs]]:
        
        ...
    
    @encryption_config.setter
    def encryption_config(self, value: Optional[pulumi.Input[ClusterEncryptionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceUpdateVersion")
    def force_update_version(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_update_version.setter
    def force_update_version(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesNetworkConfig")
    def kubernetes_network_config(self) -> Optional[pulumi.Input[ClusterKubernetesNetworkConfigArgs]]:
        
        ...
    
    @kubernetes_network_config.setter
    def kubernetes_network_config(self, value: Optional[pulumi.Input[ClusterKubernetesNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostConfig")
    def outpost_config(self) -> Optional[pulumi.Input[ClusterOutpostConfigArgs]]:
        
        ...
    
    @outpost_config.setter
    def outpost_config(self, value: Optional[pulumi.Input[ClusterOutpostConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteNetworkConfig")
    def remote_network_config(self) -> Optional[pulumi.Input[ClusterRemoteNetworkConfigArgs]]:
        
        ...
    
    @remote_network_config.setter
    def remote_network_config(self, value: Optional[pulumi.Input[ClusterRemoteNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConfig")
    def storage_config(self) -> Optional[pulumi.Input[ClusterStorageConfigArgs]]:
        
        ...
    
    @storage_config.setter
    def storage_config(self, value: Optional[pulumi.Input[ClusterStorageConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> Optional[pulumi.Input[ClusterUpgradePolicyArgs]]:
        
        ...
    
    @upgrade_policy.setter
    def upgrade_policy(self, value: Optional[pulumi.Input[ClusterUpgradePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zonalShiftConfig")
    def zonal_shift_config(self) -> Optional[pulumi.Input[ClusterZonalShiftConfigArgs]]:
        
        ...
    
    @zonal_shift_config.setter
    def zonal_shift_config(self, value: Optional[pulumi.Input[ClusterZonalShiftConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ClusterState:
    def __init__(__self__, *, access_config: Optional[pulumi.Input[ClusterAccessConfigArgs]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_self_managed_addons: Optional[pulumi.Input[_builtins.bool]] = ..., certificate_authority: Optional[pulumi.Input[ClusterCertificateAuthorityArgs]] = ..., cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., compute_config: Optional[pulumi.Input[ClusterComputeConfigArgs]] = ..., control_plane_scaling_config: Optional[pulumi.Input[ClusterControlPlaneScalingConfigArgs]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., default_addons_to_removes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., enabled_cluster_log_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., encryption_config: Optional[pulumi.Input[ClusterEncryptionConfigArgs]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., force_update_version: Optional[pulumi.Input[_builtins.bool]] = ..., identities: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterIdentityArgs]]]] = ..., kubernetes_network_config: Optional[pulumi.Input[ClusterKubernetesNetworkConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., outpost_config: Optional[pulumi.Input[ClusterOutpostConfigArgs]] = ..., platform_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., remote_network_config: Optional[pulumi.Input[ClusterRemoteNetworkConfigArgs]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., storage_config: Optional[pulumi.Input[ClusterStorageConfigArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., upgrade_policy: Optional[pulumi.Input[ClusterUpgradePolicyArgs]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., vpc_config: Optional[pulumi.Input[ClusterVpcConfigArgs]] = ..., zonal_shift_config: Optional[pulumi.Input[ClusterZonalShiftConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessConfig")
    def access_config(self) -> Optional[pulumi.Input[ClusterAccessConfigArgs]]:
        
        ...
    
    @access_config.setter
    def access_config(self, value: Optional[pulumi.Input[ClusterAccessConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapSelfManagedAddons")
    def bootstrap_self_managed_addons(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bootstrap_self_managed_addons.setter
    def bootstrap_self_managed_addons(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthority")
    def certificate_authority(self) -> Optional[pulumi.Input[ClusterCertificateAuthorityArgs]]:
        
        ...
    
    @certificate_authority.setter
    def certificate_authority(self, value: Optional[pulumi.Input[ClusterCertificateAuthorityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeConfig")
    def compute_config(self) -> Optional[pulumi.Input[ClusterComputeConfigArgs]]:
        
        ...
    
    @compute_config.setter
    def compute_config(self, value: Optional[pulumi.Input[ClusterComputeConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneScalingConfig")
    def control_plane_scaling_config(self) -> Optional[pulumi.Input[ClusterControlPlaneScalingConfigArgs]]:
        
        ...
    
    @control_plane_scaling_config.setter
    def control_plane_scaling_config(self, value: Optional[pulumi.Input[ClusterControlPlaneScalingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAddonsToRemoves")
    @_utilities.deprecated(...)
    def default_addons_to_removes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @default_addons_to_removes.setter
    def default_addons_to_removes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledClusterLogTypes")
    def enabled_cluster_log_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @enabled_cluster_log_types.setter
    def enabled_cluster_log_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[pulumi.Input[ClusterEncryptionConfigArgs]]:
        
        ...
    
    @encryption_config.setter
    def encryption_config(self, value: Optional[pulumi.Input[ClusterEncryptionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceUpdateVersion")
    def force_update_version(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_update_version.setter
    def force_update_version(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterIdentityArgs]]]]:
        
        ...
    
    @identities.setter
    def identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterIdentityArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesNetworkConfig")
    def kubernetes_network_config(self) -> Optional[pulumi.Input[ClusterKubernetesNetworkConfigArgs]]:
        
        ...
    
    @kubernetes_network_config.setter
    def kubernetes_network_config(self, value: Optional[pulumi.Input[ClusterKubernetesNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostConfig")
    def outpost_config(self) -> Optional[pulumi.Input[ClusterOutpostConfigArgs]]:
        
        ...
    
    @outpost_config.setter
    def outpost_config(self, value: Optional[pulumi.Input[ClusterOutpostConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform_version.setter
    def platform_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteNetworkConfig")
    def remote_network_config(self) -> Optional[pulumi.Input[ClusterRemoteNetworkConfigArgs]]:
        
        ...
    
    @remote_network_config.setter
    def remote_network_config(self, value: Optional[pulumi.Input[ClusterRemoteNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConfig")
    def storage_config(self) -> Optional[pulumi.Input[ClusterStorageConfigArgs]]:
        
        ...
    
    @storage_config.setter
    def storage_config(self, value: Optional[pulumi.Input[ClusterStorageConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> Optional[pulumi.Input[ClusterUpgradePolicyArgs]]:
        
        ...
    
    @upgrade_policy.setter
    def upgrade_policy(self, value: Optional[pulumi.Input[ClusterUpgradePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[ClusterVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[ClusterVpcConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zonalShiftConfig")
    def zonal_shift_config(self) -> Optional[pulumi.Input[ClusterZonalShiftConfigArgs]]:
        
        ...
    
    @zonal_shift_config.setter
    def zonal_shift_config(self, value: Optional[pulumi.Input[ClusterZonalShiftConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:eks/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_config: Optional[pulumi.Input[Union[ClusterAccessConfigArgs, ClusterAccessConfigArgsDict]]] = ..., bootstrap_self_managed_addons: Optional[pulumi.Input[_builtins.bool]] = ..., compute_config: Optional[pulumi.Input[Union[ClusterComputeConfigArgs, ClusterComputeConfigArgsDict]]] = ..., control_plane_scaling_config: Optional[pulumi.Input[Union[ClusterControlPlaneScalingConfigArgs, ClusterControlPlaneScalingConfigArgsDict]]] = ..., default_addons_to_removes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., enabled_cluster_log_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., encryption_config: Optional[pulumi.Input[Union[ClusterEncryptionConfigArgs, ClusterEncryptionConfigArgsDict]]] = ..., force_update_version: Optional[pulumi.Input[_builtins.bool]] = ..., kubernetes_network_config: Optional[pulumi.Input[Union[ClusterKubernetesNetworkConfigArgs, ClusterKubernetesNetworkConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., outpost_config: Optional[pulumi.Input[Union[ClusterOutpostConfigArgs, ClusterOutpostConfigArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., remote_network_config: Optional[pulumi.Input[Union[ClusterRemoteNetworkConfigArgs, ClusterRemoteNetworkConfigArgsDict]]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., storage_config: Optional[pulumi.Input[Union[ClusterStorageConfigArgs, ClusterStorageConfigArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., upgrade_policy: Optional[pulumi.Input[Union[ClusterUpgradePolicyArgs, ClusterUpgradePolicyArgsDict]]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., vpc_config: Optional[pulumi.Input[Union[ClusterVpcConfigArgs, ClusterVpcConfigArgsDict]]] = ..., zonal_shift_config: Optional[pulumi.Input[Union[ClusterZonalShiftConfigArgs, ClusterZonalShiftConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_config: Optional[pulumi.Input[Union[ClusterAccessConfigArgs, ClusterAccessConfigArgsDict]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_self_managed_addons: Optional[pulumi.Input[_builtins.bool]] = ..., certificate_authority: Optional[pulumi.Input[Union[ClusterCertificateAuthorityArgs, ClusterCertificateAuthorityArgsDict]]] = ..., cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., compute_config: Optional[pulumi.Input[Union[ClusterComputeConfigArgs, ClusterComputeConfigArgsDict]]] = ..., control_plane_scaling_config: Optional[pulumi.Input[Union[ClusterControlPlaneScalingConfigArgs, ClusterControlPlaneScalingConfigArgsDict]]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., default_addons_to_removes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., enabled_cluster_log_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., encryption_config: Optional[pulumi.Input[Union[ClusterEncryptionConfigArgs, ClusterEncryptionConfigArgsDict]]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., force_update_version: Optional[pulumi.Input[_builtins.bool]] = ..., identities: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterIdentityArgs, ClusterIdentityArgsDict]]]]] = ..., kubernetes_network_config: Optional[pulumi.Input[Union[ClusterKubernetesNetworkConfigArgs, ClusterKubernetesNetworkConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., outpost_config: Optional[pulumi.Input[Union[ClusterOutpostConfigArgs, ClusterOutpostConfigArgsDict]]] = ..., platform_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., remote_network_config: Optional[pulumi.Input[Union[ClusterRemoteNetworkConfigArgs, ClusterRemoteNetworkConfigArgsDict]]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., storage_config: Optional[pulumi.Input[Union[ClusterStorageConfigArgs, ClusterStorageConfigArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., upgrade_policy: Optional[pulumi.Input[Union[ClusterUpgradePolicyArgs, ClusterUpgradePolicyArgsDict]]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., vpc_config: Optional[pulumi.Input[Union[ClusterVpcConfigArgs, ClusterVpcConfigArgsDict]]] = ..., zonal_shift_config: Optional[pulumi.Input[Union[ClusterZonalShiftConfigArgs, ClusterZonalShiftConfigArgsDict]]] = ...) -> Cluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessConfig")
    def access_config(self) -> pulumi.Output[outputs.ClusterAccessConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapSelfManagedAddons")
    def bootstrap_self_managed_addons(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthority")
    def certificate_authority(self) -> pulumi.Output[outputs.ClusterCertificateAuthority]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeConfig")
    def compute_config(self) -> pulumi.Output[outputs.ClusterComputeConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneScalingConfig")
    def control_plane_scaling_config(self) -> pulumi.Output[outputs.ClusterControlPlaneScalingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAddonsToRemoves")
    @_utilities.deprecated(...)
    def default_addons_to_removes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledClusterLogTypes")
    def enabled_cluster_log_types(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> pulumi.Output[Optional[outputs.ClusterEncryptionConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceUpdateVersion")
    def force_update_version(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identities(self) -> pulumi.Output[Sequence[outputs.ClusterIdentity]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesNetworkConfig")
    def kubernetes_network_config(self) -> pulumi.Output[outputs.ClusterKubernetesNetworkConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostConfig")
    def outpost_config(self) -> pulumi.Output[Optional[outputs.ClusterOutpostConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteNetworkConfig")
    def remote_network_config(self) -> pulumi.Output[Optional[outputs.ClusterRemoteNetworkConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConfig")
    def storage_config(self) -> pulumi.Output[outputs.ClusterStorageConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> pulumi.Output[outputs.ClusterUpgradePolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Output[outputs.ClusterVpcConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zonalShiftConfig")
    def zonal_shift_config(self) -> pulumi.Output[Optional[outputs.ClusterZonalShiftConfig]]:
        
        ...
    


