

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterAutoscalingSettings', 'ClusterAutoscalingSettingsAutoscalingPolicy', ..., ..., ..., 'ClusterDatastoreMountConfig', 'ClusterDatastoreMountConfigDatastoreNetwork', 'ClusterNodeTypeConfig', 'DatastoreNfsDatastore', 'DatastoreNfsDatastoreGoogleFileService', 'DatastoreNfsDatastoreThirdPartyFileService', 'ExternalAccessRuleDestinationIpRange', 'ExternalAccessRuleSourceIpRange', 'NetworkPolicyExternalIp', 'NetworkPolicyInternetAccess', 'NetworkVpcNetwork', 'PrivateCloudHcx', 'PrivateCloudManagementCluster', 'PrivateCloudManagementClusterAutoscalingSettings', ..., ..., ..., ..., 'PrivateCloudManagementClusterNodeTypeConfig', ..., 'PrivateCloudNetworkConfig', 'PrivateCloudNsx', 'PrivateCloudVcenter', 'SubnetDhcpAddressRange', 'GetAnnouncementsAnnouncementResult', 'GetClusterAutoscalingSettingResult', ..., ..., ..., ..., 'GetClusterDatastoreMountConfigResult', ..., 'GetClusterNodeTypeConfigResult', 'GetDatastoreNfsDatastoreResult', 'GetDatastoreNfsDatastoreGoogleFileServiceResult', ..., 'GetExternalAccessRuleDestinationIpRangeResult', 'GetExternalAccessRuleSourceIpRangeResult', 'GetNetworkPolicyExternalIpResult', 'GetNetworkPolicyInternetAccessResult', 'GetNetworkVpcNetworkResult', 'GetPrivateCloudHcxResult', 'GetPrivateCloudManagementClusterResult', ..., ..., ..., ..., ..., ..., ..., 'GetPrivateCloudNetworkConfigResult', 'GetPrivateCloudNsxResult', 'GetPrivateCloudVcenterResult', 'GetSubnetDhcpAddressRangeResult', 'GetUpgradesUpgradeResult', 'GetUpgradesUpgradeComponentUpgradeResult', 'GetUpgradesUpgradeScheduleResult', 'GetUpgradesUpgradeScheduleConstraintsResult', ..., ..., ..., ..., 'GetUpgradesUpgradeScheduleEditWindowResult', 'GetUpgradesUpgradeScheduleWeeklyWindowResult', ...]
@pulumi.output_type
class ClusterAutoscalingSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscaling_policies: Sequence[outputs.ClusterAutoscalingSettingsAutoscalingPolicy], cool_down_period: Optional[_builtins.str] = ..., max_cluster_node_count: Optional[_builtins.int] = ..., min_cluster_node_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingPolicies")
    def autoscaling_policies(self) -> Sequence[outputs.ClusterAutoscalingSettingsAutoscalingPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coolDownPeriod")
    def cool_down_period(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxClusterNodeCount")
    def max_cluster_node_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minClusterNodeCount")
    def min_cluster_node_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterAutoscalingSettingsAutoscalingPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscale_policy_id: _builtins.str, node_type_id: _builtins.str, scale_out_size: _builtins.int, consumed_memory_thresholds: Optional[outputs.ClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholds] = ..., cpu_thresholds: Optional[outputs.ClusterAutoscalingSettingsAutoscalingPolicyCpuThresholds] = ..., storage_thresholds: Optional[outputs.ClusterAutoscalingSettingsAutoscalingPolicyStorageThresholds] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalePolicyId")
    def autoscale_policy_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeId")
    def node_type_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOutSize")
    def scale_out_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumedMemoryThresholds")
    def consumed_memory_thresholds(self) -> Optional[outputs.ClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholds]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuThresholds")
    def cpu_thresholds(self) -> Optional[outputs.ClusterAutoscalingSettingsAutoscalingPolicyCpuThresholds]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageThresholds")
    def storage_thresholds(self) -> Optional[outputs.ClusterAutoscalingSettingsAutoscalingPolicyStorageThresholds]:
        
        ...
    


@pulumi.output_type
class ClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholds(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scale_in: _builtins.int, scale_out: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ClusterAutoscalingSettingsAutoscalingPolicyCpuThresholds(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scale_in: _builtins.int, scale_out: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ClusterAutoscalingSettingsAutoscalingPolicyStorageThresholds(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scale_in: _builtins.int, scale_out: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ClusterDatastoreMountConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, datastore: _builtins.str, datastore_network: outputs.ClusterDatastoreMountConfigDatastoreNetwork, access_mode: Optional[_builtins.str] = ..., file_share: Optional[_builtins.str] = ..., ignore_colocation: Optional[_builtins.bool] = ..., nfs_version: Optional[_builtins.str] = ..., servers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datastore(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datastoreNetwork")
    def datastore_network(self) -> outputs.ClusterDatastoreMountConfigDatastoreNetwork:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileShare")
    def file_share(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreColocation")
    def ignore_colocation(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nfsVersion")
    def nfs_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def servers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ClusterDatastoreMountConfigDatastoreNetwork(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnet: _builtins.str, connection_count: Optional[_builtins.int] = ..., mtu: Optional[_builtins.int] = ..., network_peering: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionCount")
    def connection_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPeering")
    def network_peering(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterNodeTypeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, node_count: _builtins.int, node_type_id: _builtins.str, custom_core_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeId")
    def node_type_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customCoreCount")
    def custom_core_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DatastoreNfsDatastore(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, google_file_service: Optional[outputs.DatastoreNfsDatastoreGoogleFileService] = ..., third_party_file_service: Optional[outputs.DatastoreNfsDatastoreThirdPartyFileService] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleFileService")
    def google_file_service(self) -> Optional[outputs.DatastoreNfsDatastoreGoogleFileService]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thirdPartyFileService")
    def third_party_file_service(self) -> Optional[outputs.DatastoreNfsDatastoreThirdPartyFileService]:
        
        ...
    


@pulumi.output_type
class DatastoreNfsDatastoreGoogleFileService(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, filestore_instance: Optional[_builtins.str] = ..., netapp_volume: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filestoreInstance")
    def filestore_instance(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="netappVolume")
    def netapp_volume(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatastoreNfsDatastoreThirdPartyFileService(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, file_share: _builtins.str, network: _builtins.str, servers: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileShare")
    def file_share(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def servers(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExternalAccessRuleDestinationIpRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, external_address: Optional[_builtins.str] = ..., ip_address_range: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalAddress")
    def external_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressRange")
    def ip_address_range(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExternalAccessRuleSourceIpRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address: Optional[_builtins.str] = ..., ip_address_range: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressRange")
    def ip_address_range(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkPolicyExternalIp(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkPolicyInternetAccess(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkVpcNetwork(dict):
    def __init__(__self__, *, network: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateCloudHcx(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fqdn: Optional[_builtins.str] = ..., internal_ip: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIp")
    def internal_ip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateCloudManagementCluster(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_id: _builtins.str, autoscaling_settings: Optional[outputs.PrivateCloudManagementClusterAutoscalingSettings] = ..., node_type_configs: Optional[Sequence[outputs.PrivateCloudManagementClusterNodeTypeConfig]] = ..., stretched_cluster_config: Optional[outputs.PrivateCloudManagementClusterStretchedClusterConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingSettings")
    def autoscaling_settings(self) -> Optional[outputs.PrivateCloudManagementClusterAutoscalingSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeConfigs")
    def node_type_configs(self) -> Optional[Sequence[outputs.PrivateCloudManagementClusterNodeTypeConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stretchedClusterConfig")
    def stretched_cluster_config(self) -> Optional[outputs.PrivateCloudManagementClusterStretchedClusterConfig]:
        
        ...
    


@pulumi.output_type
class PrivateCloudManagementClusterAutoscalingSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscaling_policies: Sequence[outputs.PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicy], cool_down_period: Optional[_builtins.str] = ..., max_cluster_node_count: Optional[_builtins.int] = ..., min_cluster_node_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingPolicies")
    def autoscaling_policies(self) -> Sequence[outputs.PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coolDownPeriod")
    def cool_down_period(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxClusterNodeCount")
    def max_cluster_node_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minClusterNodeCount")
    def min_cluster_node_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscale_policy_id: _builtins.str, node_type_id: _builtins.str, scale_out_size: _builtins.int, consumed_memory_thresholds: Optional[outputs.PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholds] = ..., cpu_thresholds: Optional[outputs.PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyCpuThresholds] = ..., storage_thresholds: Optional[outputs.PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyStorageThresholds] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalePolicyId")
    def autoscale_policy_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeId")
    def node_type_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOutSize")
    def scale_out_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumedMemoryThresholds")
    def consumed_memory_thresholds(self) -> Optional[outputs.PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholds]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuThresholds")
    def cpu_thresholds(self) -> Optional[outputs.PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyCpuThresholds]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageThresholds")
    def storage_thresholds(self) -> Optional[outputs.PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyStorageThresholds]:
        
        ...
    


@pulumi.output_type
class PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyConsumedMemoryThresholds(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scale_in: _builtins.int, scale_out: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyCpuThresholds(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scale_in: _builtins.int, scale_out: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class PrivateCloudManagementClusterAutoscalingSettingsAutoscalingPolicyStorageThresholds(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scale_in: _builtins.int, scale_out: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class PrivateCloudManagementClusterNodeTypeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, node_count: _builtins.int, node_type_id: _builtins.str, custom_core_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeId")
    def node_type_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customCoreCount")
    def custom_core_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PrivateCloudManagementClusterStretchedClusterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, preferred_location: Optional[_builtins.str] = ..., secondary_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredLocation")
    def preferred_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryLocation")
    def secondary_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateCloudNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, management_cidr: _builtins.str, dns_server_ip: Optional[_builtins.str] = ..., management_ip_address_layout_version: Optional[_builtins.int] = ..., vmware_engine_network: Optional[_builtins.str] = ..., vmware_engine_network_canonical: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementCidr")
    def management_cidr(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsServerIp")
    def dns_server_ip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementIpAddressLayoutVersion")
    def management_ip_address_layout_version(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetwork")
    def vmware_engine_network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetworkCanonical")
    def vmware_engine_network_canonical(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateCloudNsx(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fqdn: Optional[_builtins.str] = ..., internal_ip: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIp")
    def internal_ip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateCloudVcenter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fqdn: Optional[_builtins.str] = ..., internal_ip: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIp")
    def internal_ip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SubnetDhcpAddressRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, first_address: Optional[_builtins.str] = ..., last_address: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstAddress")
    def first_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAddress")
    def last_address(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetAnnouncementsAnnouncementResult(dict):
    def __init__(__self__, *, code: _builtins.str, metadata: Mapping[str, _builtins.str], name: _builtins.str, target_resource_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceType")
    def target_resource_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetClusterAutoscalingSettingResult(dict):
    def __init__(__self__, *, autoscaling_policies: Sequence[outputs.GetClusterAutoscalingSettingAutoscalingPolicyResult], cool_down_period: _builtins.str, max_cluster_node_count: _builtins.int, min_cluster_node_count: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingPolicies")
    def autoscaling_policies(self) -> Sequence[outputs.GetClusterAutoscalingSettingAutoscalingPolicyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coolDownPeriod")
    def cool_down_period(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxClusterNodeCount")
    def max_cluster_node_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minClusterNodeCount")
    def min_cluster_node_count(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetClusterAutoscalingSettingAutoscalingPolicyResult(dict):
    def __init__(__self__, *, autoscale_policy_id: _builtins.str, consumed_memory_thresholds: Sequence[outputs.GetClusterAutoscalingSettingAutoscalingPolicyConsumedMemoryThresholdResult], cpu_thresholds: Sequence[outputs.GetClusterAutoscalingSettingAutoscalingPolicyCpuThresholdResult], node_type_id: _builtins.str, scale_out_size: _builtins.int, storage_thresholds: Sequence[outputs.GetClusterAutoscalingSettingAutoscalingPolicyStorageThresholdResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalePolicyId")
    def autoscale_policy_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumedMemoryThresholds")
    def consumed_memory_thresholds(self) -> Sequence[outputs.GetClusterAutoscalingSettingAutoscalingPolicyConsumedMemoryThresholdResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuThresholds")
    def cpu_thresholds(self) -> Sequence[outputs.GetClusterAutoscalingSettingAutoscalingPolicyCpuThresholdResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeId")
    def node_type_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOutSize")
    def scale_out_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageThresholds")
    def storage_thresholds(self) -> Sequence[outputs.GetClusterAutoscalingSettingAutoscalingPolicyStorageThresholdResult]:
        
        ...
    


@pulumi.output_type
class GetClusterAutoscalingSettingAutoscalingPolicyConsumedMemoryThresholdResult(dict):
    def __init__(__self__, *, scale_in: _builtins.int, scale_out: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetClusterAutoscalingSettingAutoscalingPolicyCpuThresholdResult(dict):
    def __init__(__self__, *, scale_in: _builtins.int, scale_out: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetClusterAutoscalingSettingAutoscalingPolicyStorageThresholdResult(dict):
    def __init__(__self__, *, scale_in: _builtins.int, scale_out: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetClusterDatastoreMountConfigResult(dict):
    def __init__(__self__, *, access_mode: _builtins.str, datastore: _builtins.str, datastore_networks: Sequence[outputs.GetClusterDatastoreMountConfigDatastoreNetworkResult], file_share: _builtins.str, ignore_colocation: _builtins.bool, nfs_version: _builtins.str, servers: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datastore(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datastoreNetworks")
    def datastore_networks(self) -> Sequence[outputs.GetClusterDatastoreMountConfigDatastoreNetworkResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileShare")
    def file_share(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreColocation")
    def ignore_colocation(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nfsVersion")
    def nfs_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def servers(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetClusterDatastoreMountConfigDatastoreNetworkResult(dict):
    def __init__(__self__, *, connection_count: _builtins.int, mtu: _builtins.int, network_peering: _builtins.str, subnet: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionCount")
    def connection_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPeering")
    def network_peering(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetClusterNodeTypeConfigResult(dict):
    def __init__(__self__, *, custom_core_count: _builtins.int, node_count: _builtins.int, node_type_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customCoreCount")
    def custom_core_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeId")
    def node_type_id(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetDatastoreNfsDatastoreResult(dict):
    def __init__(__self__, *, google_file_services: Sequence[outputs.GetDatastoreNfsDatastoreGoogleFileServiceResult], third_party_file_services: Sequence[outputs.GetDatastoreNfsDatastoreThirdPartyFileServiceResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleFileServices")
    def google_file_services(self) -> Sequence[outputs.GetDatastoreNfsDatastoreGoogleFileServiceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thirdPartyFileServices")
    def third_party_file_services(self) -> Sequence[outputs.GetDatastoreNfsDatastoreThirdPartyFileServiceResult]:
        
        ...
    


@pulumi.output_type
class GetDatastoreNfsDatastoreGoogleFileServiceResult(dict):
    def __init__(__self__, *, filestore_instance: _builtins.str, netapp_volume: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filestoreInstance")
    def filestore_instance(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="netappVolume")
    def netapp_volume(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatastoreNfsDatastoreThirdPartyFileServiceResult(dict):
    def __init__(__self__, *, file_share: _builtins.str, network: _builtins.str, servers: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileShare")
    def file_share(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def servers(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetExternalAccessRuleDestinationIpRangeResult(dict):
    def __init__(__self__, *, external_address: _builtins.str, ip_address_range: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalAddress")
    def external_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressRange")
    def ip_address_range(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetExternalAccessRuleSourceIpRangeResult(dict):
    def __init__(__self__, *, ip_address: _builtins.str, ip_address_range: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressRange")
    def ip_address_range(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkPolicyExternalIpResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkPolicyInternetAccessResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNetworkVpcNetworkResult(dict):
    def __init__(__self__, *, network: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPrivateCloudHcxResult(dict):
    def __init__(__self__, *, fqdn: _builtins.str, internal_ip: _builtins.str, state: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIp")
    def internal_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPrivateCloudManagementClusterResult(dict):
    def __init__(__self__, *, autoscaling_settings: Sequence[outputs.GetPrivateCloudManagementClusterAutoscalingSettingResult], cluster_id: _builtins.str, node_type_configs: Sequence[outputs.GetPrivateCloudManagementClusterNodeTypeConfigResult], stretched_cluster_configs: Sequence[outputs.GetPrivateCloudManagementClusterStretchedClusterConfigResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingSettings")
    def autoscaling_settings(self) -> Sequence[outputs.GetPrivateCloudManagementClusterAutoscalingSettingResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeConfigs")
    def node_type_configs(self) -> Sequence[outputs.GetPrivateCloudManagementClusterNodeTypeConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stretchedClusterConfigs")
    def stretched_cluster_configs(self) -> Sequence[outputs.GetPrivateCloudManagementClusterStretchedClusterConfigResult]:
        
        ...
    


@pulumi.output_type
class GetPrivateCloudManagementClusterAutoscalingSettingResult(dict):
    def __init__(__self__, *, autoscaling_policies: Sequence[outputs.GetPrivateCloudManagementClusterAutoscalingSettingAutoscalingPolicyResult], cool_down_period: _builtins.str, max_cluster_node_count: _builtins.int, min_cluster_node_count: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingPolicies")
    def autoscaling_policies(self) -> Sequence[outputs.GetPrivateCloudManagementClusterAutoscalingSettingAutoscalingPolicyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coolDownPeriod")
    def cool_down_period(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxClusterNodeCount")
    def max_cluster_node_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minClusterNodeCount")
    def min_cluster_node_count(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetPrivateCloudManagementClusterAutoscalingSettingAutoscalingPolicyResult(dict):
    def __init__(__self__, *, autoscale_policy_id: _builtins.str, consumed_memory_thresholds: Sequence[outputs.GetPrivateCloudManagementClusterAutoscalingSettingAutoscalingPolicyConsumedMemoryThresholdResult], cpu_thresholds: Sequence[outputs.GetPrivateCloudManagementClusterAutoscalingSettingAutoscalingPolicyCpuThresholdResult], node_type_id: _builtins.str, scale_out_size: _builtins.int, storage_thresholds: Sequence[outputs.GetPrivateCloudManagementClusterAutoscalingSettingAutoscalingPolicyStorageThresholdResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalePolicyId")
    def autoscale_policy_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumedMemoryThresholds")
    def consumed_memory_thresholds(self) -> Sequence[outputs.GetPrivateCloudManagementClusterAutoscalingSettingAutoscalingPolicyConsumedMemoryThresholdResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuThresholds")
    def cpu_thresholds(self) -> Sequence[outputs.GetPrivateCloudManagementClusterAutoscalingSettingAutoscalingPolicyCpuThresholdResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeId")
    def node_type_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOutSize")
    def scale_out_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageThresholds")
    def storage_thresholds(self) -> Sequence[outputs.GetPrivateCloudManagementClusterAutoscalingSettingAutoscalingPolicyStorageThresholdResult]:
        
        ...
    


@pulumi.output_type
class GetPrivateCloudManagementClusterAutoscalingSettingAutoscalingPolicyConsumedMemoryThresholdResult(dict):
    def __init__(__self__, *, scale_in: _builtins.int, scale_out: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetPrivateCloudManagementClusterAutoscalingSettingAutoscalingPolicyCpuThresholdResult(dict):
    def __init__(__self__, *, scale_in: _builtins.int, scale_out: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetPrivateCloudManagementClusterAutoscalingSettingAutoscalingPolicyStorageThresholdResult(dict):
    def __init__(__self__, *, scale_in: _builtins.int, scale_out: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleIn")
    def scale_in(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOut")
    def scale_out(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetPrivateCloudManagementClusterNodeTypeConfigResult(dict):
    def __init__(__self__, *, custom_core_count: _builtins.int, node_count: _builtins.int, node_type_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customCoreCount")
    def custom_core_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeId")
    def node_type_id(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetPrivateCloudManagementClusterStretchedClusterConfigResult(dict):
    def __init__(__self__, *, preferred_location: _builtins.str, secondary_location: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredLocation")
    def preferred_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryLocation")
    def secondary_location(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPrivateCloudNetworkConfigResult(dict):
    def __init__(__self__, *, dns_server_ip: _builtins.str, management_cidr: _builtins.str, management_ip_address_layout_version: _builtins.int, vmware_engine_network: _builtins.str, vmware_engine_network_canonical: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsServerIp")
    def dns_server_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementCidr")
    def management_cidr(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementIpAddressLayoutVersion")
    def management_ip_address_layout_version(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetwork")
    def vmware_engine_network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetworkCanonical")
    def vmware_engine_network_canonical(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPrivateCloudNsxResult(dict):
    def __init__(__self__, *, fqdn: _builtins.str, internal_ip: _builtins.str, state: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIp")
    def internal_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPrivateCloudVcenterResult(dict):
    def __init__(__self__, *, fqdn: _builtins.str, internal_ip: _builtins.str, state: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIp")
    def internal_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSubnetDhcpAddressRangeResult(dict):
    def __init__(__self__, *, first_address: _builtins.str, last_address: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstAddress")
    def first_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAddress")
    def last_address(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUpgradesUpgradeResult(dict):
    def __init__(__self__, *, component_upgrades: Sequence[outputs.GetUpgradesUpgradeComponentUpgradeResult], description: _builtins.str, end_time: _builtins.str, estimated_duration: _builtins.str, name: _builtins.str, schedules: Sequence[outputs.GetUpgradesUpgradeScheduleResult], start_version: _builtins.str, state: _builtins.str, target_version: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentUpgrades")
    def component_upgrades(self) -> Sequence[outputs.GetUpgradesUpgradeComponentUpgradeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="estimatedDuration")
    def estimated_duration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedules(self) -> Sequence[outputs.GetUpgradesUpgradeScheduleResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startVersion")
    def start_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVersion")
    def target_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUpgradesUpgradeComponentUpgradeResult(dict):
    def __init__(__self__, *, component_type: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUpgradesUpgradeScheduleResult(dict):
    def __init__(__self__, *, constraints: outputs.GetUpgradesUpgradeScheduleConstraintsResult, edit_windows: Sequence[outputs.GetUpgradesUpgradeScheduleEditWindowResult], last_editor: _builtins.str, start_time: _builtins.str, weekly_windows: Sequence[outputs.GetUpgradesUpgradeScheduleWeeklyWindowResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def constraints(self) -> outputs.GetUpgradesUpgradeScheduleConstraintsResult:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="editWindows")
    def edit_windows(self) -> Sequence[outputs.GetUpgradesUpgradeScheduleEditWindowResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastEditor")
    def last_editor(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyWindows")
    def weekly_windows(self) -> Sequence[outputs.GetUpgradesUpgradeScheduleWeeklyWindowResult]:
        
        ...
    


@pulumi.output_type
class GetUpgradesUpgradeScheduleConstraintsResult(dict):
    def __init__(__self__, *, disallowed_intervals: outputs.GetUpgradesUpgradeScheduleConstraintsDisallowedIntervalsResult, min_hours_day: _builtins.int, min_hours_week: _builtins.int, reschedule_date_range: outputs.GetUpgradesUpgradeScheduleConstraintsRescheduleDateRangeResult) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disallowedIntervals")
    def disallowed_intervals(self) -> outputs.GetUpgradesUpgradeScheduleConstraintsDisallowedIntervalsResult:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minHoursDay")
    def min_hours_day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minHoursWeek")
    def min_hours_week(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rescheduleDateRange")
    def reschedule_date_range(self) -> outputs.GetUpgradesUpgradeScheduleConstraintsRescheduleDateRangeResult:
        
        ...
    


@pulumi.output_type
class GetUpgradesUpgradeScheduleConstraintsDisallowedIntervalsResult(dict):
    def __init__(__self__, *, end_day: _builtins.str, end_time: outputs.GetUpgradesUpgradeScheduleConstraintsDisallowedIntervalsEndTimeResult, start_day: _builtins.str, start_time: outputs.GetUpgradesUpgradeScheduleConstraintsDisallowedIntervalsStartTimeResult) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDay")
    def end_day(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> outputs.GetUpgradesUpgradeScheduleConstraintsDisallowedIntervalsEndTimeResult:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDay")
    def start_day(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> outputs.GetUpgradesUpgradeScheduleConstraintsDisallowedIntervalsStartTimeResult:
        
        ...
    


@pulumi.output_type
class GetUpgradesUpgradeScheduleConstraintsDisallowedIntervalsEndTimeResult(dict):
    def __init__(__self__, *, hours: _builtins.int, minutes: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetUpgradesUpgradeScheduleConstraintsDisallowedIntervalsStartTimeResult(dict):
    def __init__(__self__, *, hours: _builtins.int, minutes: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetUpgradesUpgradeScheduleConstraintsRescheduleDateRangeResult(dict):
    def __init__(__self__, *, end_time: _builtins.str, start_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUpgradesUpgradeScheduleEditWindowResult(dict):
    def __init__(__self__, *, end_time: _builtins.str, start_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUpgradesUpgradeScheduleWeeklyWindowResult(dict):
    def __init__(__self__, *, day_of_week: _builtins.str, duration: _builtins.str, start_times: Sequence[outputs.GetUpgradesUpgradeScheduleWeeklyWindowStartTimeResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(self) -> Sequence[outputs.GetUpgradesUpgradeScheduleWeeklyWindowStartTimeResult]:
        
        ...
    


@pulumi.output_type
class GetUpgradesUpgradeScheduleWeeklyWindowStartTimeResult(dict):
    def __init__(__self__, *, hours: _builtins.int, minutes: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int:
        ...
    


