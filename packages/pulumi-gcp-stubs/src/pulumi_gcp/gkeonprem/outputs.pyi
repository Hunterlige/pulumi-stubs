

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BareMetalAdminClusterClusterOperations', 'BareMetalAdminClusterControlPlane', 'BareMetalAdminClusterControlPlaneApiServerArg', ..., ..., ..., ..., 'BareMetalAdminClusterFleet', 'BareMetalAdminClusterLoadBalancer', 'BareMetalAdminClusterLoadBalancerBgpLbConfig', ..., ..., ..., ..., ..., ..., ..., 'BareMetalAdminClusterLoadBalancerManualLbConfig', 'BareMetalAdminClusterLoadBalancerPortConfig', 'BareMetalAdminClusterLoadBalancerVipConfig', 'BareMetalAdminClusterMaintenanceConfig', 'BareMetalAdminClusterNetworkConfig', 'BareMetalAdminClusterNetworkConfigIslandModeCidr', ..., 'BareMetalAdminClusterNodeAccessConfig', 'BareMetalAdminClusterNodeConfig', 'BareMetalAdminClusterProxy', 'BareMetalAdminClusterSecurityConfig', 'BareMetalAdminClusterSecurityConfigAuthorization', ..., 'BareMetalAdminClusterStatus', 'BareMetalAdminClusterStatusCondition', 'BareMetalAdminClusterStorage', 'BareMetalAdminClusterStorageLvpNodeMountsConfig', 'BareMetalAdminClusterStorageLvpShareConfig', ..., 'BareMetalAdminClusterValidationCheck', 'BareMetalAdminClusterValidationCheckStatus', 'BareMetalAdminClusterValidationCheckStatusResult', 'BareMetalClusterBinaryAuthorization', 'BareMetalClusterClusterOperations', 'BareMetalClusterControlPlane', 'BareMetalClusterControlPlaneApiServerArg', ..., ..., ..., ..., 'BareMetalClusterFleet', 'BareMetalClusterLoadBalancer', 'BareMetalClusterLoadBalancerBgpLbConfig', 'BareMetalClusterLoadBalancerBgpLbConfigAddressPool', ..., ..., ..., ..., ..., ..., 'BareMetalClusterLoadBalancerManualLbConfig', 'BareMetalClusterLoadBalancerMetalLbConfig', ..., ..., ..., ..., ..., 'BareMetalClusterLoadBalancerPortConfig', 'BareMetalClusterLoadBalancerVipConfig', 'BareMetalClusterMaintenanceConfig', 'BareMetalClusterNetworkConfig', 'BareMetalClusterNetworkConfigIslandModeCidr', ..., 'BareMetalClusterNetworkConfigSrIovConfig', 'BareMetalClusterNodeAccessConfig', 'BareMetalClusterNodeConfig', 'BareMetalClusterOsEnvironmentConfig', 'BareMetalClusterProxy', 'BareMetalClusterSecurityConfig', 'BareMetalClusterSecurityConfigAuthorization', ..., 'BareMetalClusterStatus', 'BareMetalClusterStatusCondition', 'BareMetalClusterStorage', 'BareMetalClusterStorageLvpNodeMountsConfig', 'BareMetalClusterStorageLvpShareConfig', 'BareMetalClusterStorageLvpShareConfigLvpConfig', 'BareMetalClusterUpgradePolicy', 'BareMetalClusterValidationCheck', 'BareMetalClusterValidationCheckStatus', 'BareMetalClusterValidationCheckStatusResult', 'BareMetalNodePoolNodePoolConfig', 'BareMetalNodePoolNodePoolConfigNodeConfig', 'BareMetalNodePoolNodePoolConfigTaint', 'BareMetalNodePoolStatus', 'BareMetalNodePoolStatusCondition', 'VMwareClusterAntiAffinityGroups', 'VMwareClusterAuthorization', 'VMwareClusterAuthorizationAdminUser', 'VMwareClusterAutoRepairConfig', 'VMwareClusterControlPlaneNode', 'VMwareClusterControlPlaneNodeAutoResizeConfig', 'VMwareClusterControlPlaneNodeVsphereConfig', 'VMwareClusterDataplaneV2', 'VMwareClusterFleet', 'VMwareClusterLoadBalancer', 'VMwareClusterLoadBalancerF5Config', 'VMwareClusterLoadBalancerManualLbConfig', 'VMwareClusterLoadBalancerMetalLbConfig', 'VMwareClusterLoadBalancerMetalLbConfigAddressPool', 'VMwareClusterLoadBalancerVipConfig', 'VMwareClusterNetworkConfig', 'VMwareClusterNetworkConfigControlPlaneV2Config', ..., ..., 'VMwareClusterNetworkConfigDhcpIpConfig', 'VMwareClusterNetworkConfigHostConfig', 'VMwareClusterNetworkConfigStaticIpConfig', 'VMwareClusterNetworkConfigStaticIpConfigIpBlock', 'VMwareClusterNetworkConfigStaticIpConfigIpBlockIp', 'VMwareClusterStatus', 'VMwareClusterStatusCondition', 'VMwareClusterStorage', 'VMwareClusterUpgradePolicy', 'VMwareClusterValidationCheck', 'VMwareClusterValidationCheckStatus', 'VMwareClusterValidationCheckStatusResult', 'VMwareClusterVcenter', 'VMwareNodePoolConfig', 'VMwareNodePoolConfigTaint', 'VMwareNodePoolConfigVsphereConfig', 'VMwareNodePoolConfigVsphereConfigTag', 'VMwareNodePoolNodePoolAutoscaling', 'VMwareNodePoolStatus', 'VMwareNodePoolStatusCondition', 'VmwareAdminClusterAddonNode', 'VmwareAdminClusterAddonNodeAutoResizeConfig', 'VmwareAdminClusterAntiAffinityGroups', 'VmwareAdminClusterAuthorization', 'VmwareAdminClusterAuthorizationViewerUser', 'VmwareAdminClusterAutoRepairConfig', 'VmwareAdminClusterControlPlaneNode', 'VmwareAdminClusterFleet', 'VmwareAdminClusterLoadBalancer', 'VmwareAdminClusterLoadBalancerF5Config', 'VmwareAdminClusterLoadBalancerManualLbConfig', 'VmwareAdminClusterLoadBalancerMetalLbConfig', 'VmwareAdminClusterLoadBalancerVipConfig', 'VmwareAdminClusterNetworkConfig', 'VmwareAdminClusterNetworkConfigDhcpIpConfig', ..., ..., ..., 'VmwareAdminClusterNetworkConfigHostConfig', 'VmwareAdminClusterNetworkConfigStaticIpConfig', ..., ..., 'VmwareAdminClusterPlatformConfig', 'VmwareAdminClusterPlatformConfigBundle', 'VmwareAdminClusterPlatformConfigBundleStatus', ..., 'VmwareAdminClusterPlatformConfigStatus', 'VmwareAdminClusterPlatformConfigStatusCondition', 'VmwareAdminClusterPrivateRegistryConfig', 'VmwareAdminClusterProxy', 'VmwareAdminClusterStatus', 'VmwareAdminClusterStatusCondition', 'VmwareAdminClusterVcenter']
@pulumi.output_type
class BareMetalAdminClusterClusterOperations(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_application_logs: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableApplicationLogs")
    def enable_application_logs(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterControlPlane(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, control_plane_node_pool_config: outputs.BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfig, api_server_args: Optional[Sequence[outputs.BareMetalAdminClusterControlPlaneApiServerArg]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneNodePoolConfig")
    def control_plane_node_pool_config(self) -> outputs.BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiServerArgs")
    def api_server_args(self) -> Optional[Sequence[outputs.BareMetalAdminClusterControlPlaneApiServerArg]]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterControlPlaneApiServerArg(dict):
    def __init__(__self__, *, argument: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def argument(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, node_pool_config: outputs.BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfig) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePoolConfig")
    def node_pool_config(self) -> outputs.BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfig:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, labels: Optional[Mapping[str, _builtins.str]] = ..., node_configs: Optional[Sequence[outputs.BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfig]] = ..., operating_system: Optional[_builtins.str] = ..., taints: Optional[Sequence[outputs.BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaint]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(self) -> Optional[Sequence[outputs.BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def taints(self) -> Optional[Sequence[outputs.BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaint]]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, labels: Optional[Mapping[str, _builtins.str]] = ..., node_ip: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeIp")
    def node_ip(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaint(dict):
    def __init__(__self__, *, effect: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterFleet(dict):
    def __init__(__self__, *, membership: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterLoadBalancer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, port_config: outputs.BareMetalAdminClusterLoadBalancerPortConfig, vip_config: outputs.BareMetalAdminClusterLoadBalancerVipConfig, bgp_lb_config: Optional[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfig] = ..., manual_lb_config: Optional[outputs.BareMetalAdminClusterLoadBalancerManualLbConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portConfig")
    def port_config(self) -> outputs.BareMetalAdminClusterLoadBalancerPortConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vipConfig")
    def vip_config(self) -> outputs.BareMetalAdminClusterLoadBalancerVipConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpLbConfig")
    def bgp_lb_config(self) -> Optional[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualLbConfig")
    def manual_lb_config(self) -> Optional[outputs.BareMetalAdminClusterLoadBalancerManualLbConfig]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterLoadBalancerBgpLbConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address_pools: Optional[Sequence[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfigAddressPool]] = ..., asn: Optional[_builtins.int] = ..., bgp_peer_configs: Optional[Sequence[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfigBgpPeerConfig]] = ..., load_balancer_node_pool_config: Optional[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPools")
    def address_pools(self) -> Optional[Sequence[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfigAddressPool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def asn(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpPeerConfigs")
    def bgp_peer_configs(self) -> Optional[Sequence[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfigBgpPeerConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerNodePoolConfig")
    def load_balancer_node_pool_config(self) -> Optional[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfig]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterLoadBalancerBgpLbConfigAddressPool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, addresses: Optional[Sequence[_builtins.str]] = ..., avoid_buggy_ips: Optional[_builtins.bool] = ..., manual_assign: Optional[_builtins.bool] = ..., pool: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avoidBuggyIps")
    def avoid_buggy_ips(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualAssign")
    def manual_assign(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pool(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterLoadBalancerBgpLbConfigBgpPeerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, asn: Optional[_builtins.int] = ..., control_plane_nodes: Optional[Sequence[_builtins.str]] = ..., ip_address: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def asn(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneNodes")
    def control_plane_nodes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, node_pool_config: Optional[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePoolConfig")
    def node_pool_config(self) -> Optional[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfig]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kubelet_config: Optional[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfig] = ..., labels: Optional[Mapping[str, _builtins.str]] = ..., node_configs: Optional[Sequence[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfig]] = ..., operating_system: Optional[_builtins.str] = ..., taints: Optional[Sequence[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaint]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(self) -> Optional[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(self) -> Optional[Sequence[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def taints(self) -> Optional[Sequence[outputs.BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaint]]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, registry_burst: Optional[_builtins.int] = ..., registry_pull_qps: Optional[_builtins.int] = ..., serialize_image_pulls_disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryBurst")
    def registry_burst(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryPullQps")
    def registry_pull_qps(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serializeImagePullsDisabled")
    def serialize_image_pulls_disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, labels: Optional[Mapping[str, _builtins.str]] = ..., node_ip: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeIp")
    def node_ip(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaint(dict):
    def __init__(__self__, *, effect: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterLoadBalancerManualLbConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterLoadBalancerPortConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, control_plane_load_balancer_port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneLoadBalancerPort")
    def control_plane_load_balancer_port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterLoadBalancerVipConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, control_plane_vip: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneVip")
    def control_plane_vip(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterMaintenanceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, maintenance_address_cidr_blocks: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceAddressCidrBlocks")
    def maintenance_address_cidr_blocks(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, advanced_networking: Optional[_builtins.bool] = ..., island_mode_cidr: Optional[outputs.BareMetalAdminClusterNetworkConfigIslandModeCidr] = ..., multiple_network_interfaces_config: Optional[outputs.BareMetalAdminClusterNetworkConfigMultipleNetworkInterfacesConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedNetworking")
    def advanced_networking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="islandModeCidr")
    def island_mode_cidr(self) -> Optional[outputs.BareMetalAdminClusterNetworkConfigIslandModeCidr]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multipleNetworkInterfacesConfig")
    def multiple_network_interfaces_config(self) -> Optional[outputs.BareMetalAdminClusterNetworkConfigMultipleNetworkInterfacesConfig]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterNetworkConfigIslandModeCidr(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pod_address_cidr_blocks: Sequence[_builtins.str], service_address_cidr_blocks: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="podAddressCidrBlocks")
    def pod_address_cidr_blocks(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAddressCidrBlocks")
    def service_address_cidr_blocks(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterNetworkConfigMultipleNetworkInterfacesConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterNodeAccessConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, login_user: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginUser")
    def login_user(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterNodeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_pods_per_node: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterProxy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, uri: _builtins.str, no_proxies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noProxies")
    def no_proxies(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterSecurityConfig(dict):
    def __init__(__self__, *, authorization: Optional[outputs.BareMetalAdminClusterSecurityConfigAuthorization] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> Optional[outputs.BareMetalAdminClusterSecurityConfigAuthorization]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterSecurityConfigAuthorization(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, admin_users: Sequence[outputs.BareMetalAdminClusterSecurityConfigAuthorizationAdminUser]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUsers")
    def admin_users(self) -> Sequence[outputs.BareMetalAdminClusterSecurityConfigAuthorizationAdminUser]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterSecurityConfigAuthorizationAdminUser(dict):
    def __init__(__self__, *, username: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterStatus(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conditions: Optional[Sequence[outputs.BareMetalAdminClusterStatusCondition]] = ..., error_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.BareMetalAdminClusterStatusCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterStatusCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterStorage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lvp_node_mounts_config: outputs.BareMetalAdminClusterStorageLvpNodeMountsConfig, lvp_share_config: outputs.BareMetalAdminClusterStorageLvpShareConfig) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lvpNodeMountsConfig")
    def lvp_node_mounts_config(self) -> outputs.BareMetalAdminClusterStorageLvpNodeMountsConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lvpShareConfig")
    def lvp_share_config(self) -> outputs.BareMetalAdminClusterStorageLvpShareConfig:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterStorageLvpNodeMountsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, path: _builtins.str, storage_class: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterStorageLvpShareConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lvp_config: outputs.BareMetalAdminClusterStorageLvpShareConfigLvpConfig, shared_path_pv_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lvpConfig")
    def lvp_config(self) -> outputs.BareMetalAdminClusterStorageLvpShareConfigLvpConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedPathPvCount")
    def shared_path_pv_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterStorageLvpShareConfigLvpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, path: _builtins.str, storage_class: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterValidationCheck(dict):
    def __init__(__self__, *, options: Optional[_builtins.str] = ..., scenario: Optional[_builtins.str] = ..., statuses: Optional[Sequence[outputs.BareMetalAdminClusterValidationCheckStatus]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scenario(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Optional[Sequence[outputs.BareMetalAdminClusterValidationCheckStatus]]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterValidationCheckStatus(dict):
    def __init__(__self__, *, results: Optional[Sequence[outputs.BareMetalAdminClusterValidationCheckStatusResult]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def results(self) -> Optional[Sequence[outputs.BareMetalAdminClusterValidationCheckStatusResult]]:
        
        ...
    


@pulumi.output_type
class BareMetalAdminClusterValidationCheckStatusResult(dict):
    def __init__(__self__, *, category: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., details: Optional[_builtins.str] = ..., options: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterBinaryAuthorization(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, evaluation_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationMode")
    def evaluation_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterClusterOperations(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_application_logs: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableApplicationLogs")
    def enable_application_logs(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterControlPlane(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, control_plane_node_pool_config: outputs.BareMetalClusterControlPlaneControlPlaneNodePoolConfig, api_server_args: Optional[Sequence[outputs.BareMetalClusterControlPlaneApiServerArg]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneNodePoolConfig")
    def control_plane_node_pool_config(self) -> outputs.BareMetalClusterControlPlaneControlPlaneNodePoolConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiServerArgs")
    def api_server_args(self) -> Optional[Sequence[outputs.BareMetalClusterControlPlaneApiServerArg]]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterControlPlaneApiServerArg(dict):
    def __init__(__self__, *, argument: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def argument(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BareMetalClusterControlPlaneControlPlaneNodePoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, node_pool_config: outputs.BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfig) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePoolConfig")
    def node_pool_config(self) -> outputs.BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfig:
        
        ...
    


@pulumi.output_type
class BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, labels: Optional[Mapping[str, _builtins.str]] = ..., node_configs: Optional[Sequence[outputs.BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfig]] = ..., operating_system: Optional[_builtins.str] = ..., taints: Optional[Sequence[outputs.BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaint]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(self) -> Optional[Sequence[outputs.BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def taints(self) -> Optional[Sequence[outputs.BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaint]]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigNodeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, labels: Optional[Mapping[str, _builtins.str]] = ..., node_ip: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeIp")
    def node_ip(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterControlPlaneControlPlaneNodePoolConfigNodePoolConfigTaint(dict):
    def __init__(__self__, *, effect: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterFleet(dict):
    def __init__(__self__, *, membership: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, port_config: outputs.BareMetalClusterLoadBalancerPortConfig, vip_config: outputs.BareMetalClusterLoadBalancerVipConfig, bgp_lb_config: Optional[outputs.BareMetalClusterLoadBalancerBgpLbConfig] = ..., manual_lb_config: Optional[outputs.BareMetalClusterLoadBalancerManualLbConfig] = ..., metal_lb_config: Optional[outputs.BareMetalClusterLoadBalancerMetalLbConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portConfig")
    def port_config(self) -> outputs.BareMetalClusterLoadBalancerPortConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vipConfig")
    def vip_config(self) -> outputs.BareMetalClusterLoadBalancerVipConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpLbConfig")
    def bgp_lb_config(self) -> Optional[outputs.BareMetalClusterLoadBalancerBgpLbConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualLbConfig")
    def manual_lb_config(self) -> Optional[outputs.BareMetalClusterLoadBalancerManualLbConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metalLbConfig")
    def metal_lb_config(self) -> Optional[outputs.BareMetalClusterLoadBalancerMetalLbConfig]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerBgpLbConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address_pools: Sequence[outputs.BareMetalClusterLoadBalancerBgpLbConfigAddressPool], asn: _builtins.int, bgp_peer_configs: Sequence[outputs.BareMetalClusterLoadBalancerBgpLbConfigBgpPeerConfig], load_balancer_node_pool_config: Optional[outputs.BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPools")
    def address_pools(self) -> Sequence[outputs.BareMetalClusterLoadBalancerBgpLbConfigAddressPool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def asn(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpPeerConfigs")
    def bgp_peer_configs(self) -> Sequence[outputs.BareMetalClusterLoadBalancerBgpLbConfigBgpPeerConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerNodePoolConfig")
    def load_balancer_node_pool_config(self) -> Optional[outputs.BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfig]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerBgpLbConfigAddressPool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, addresses: Sequence[_builtins.str], pool: _builtins.str, avoid_buggy_ips: Optional[_builtins.bool] = ..., manual_assign: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pool(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avoidBuggyIps")
    def avoid_buggy_ips(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualAssign")
    def manual_assign(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerBgpLbConfigBgpPeerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, asn: _builtins.int, ip_address: _builtins.str, control_plane_nodes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def asn(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneNodes")
    def control_plane_nodes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, node_pool_config: Optional[outputs.BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePoolConfig")
    def node_pool_config(self) -> Optional[outputs.BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfig]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kubelet_config: Optional[outputs.BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfig] = ..., labels: Optional[Mapping[str, _builtins.str]] = ..., node_configs: Optional[Sequence[outputs.BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfig]] = ..., operating_system: Optional[_builtins.str] = ..., taints: Optional[Sequence[outputs.BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaint]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(self) -> Optional[outputs.BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(self) -> Optional[Sequence[outputs.BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def taints(self) -> Optional[Sequence[outputs.BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaint]]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigKubeletConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, registry_burst: Optional[_builtins.int] = ..., registry_pull_qps: Optional[_builtins.int] = ..., serialize_image_pulls_disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryBurst")
    def registry_burst(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryPullQps")
    def registry_pull_qps(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serializeImagePullsDisabled")
    def serialize_image_pulls_disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, labels: Optional[Mapping[str, _builtins.str]] = ..., node_ip: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeIp")
    def node_ip(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerBgpLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaint(dict):
    def __init__(__self__, *, effect: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerManualLbConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerMetalLbConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address_pools: Sequence[outputs.BareMetalClusterLoadBalancerMetalLbConfigAddressPool], load_balancer_node_pool_config: Optional[outputs.BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPools")
    def address_pools(self) -> Sequence[outputs.BareMetalClusterLoadBalancerMetalLbConfigAddressPool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerNodePoolConfig")
    def load_balancer_node_pool_config(self) -> Optional[outputs.BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfig]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerMetalLbConfigAddressPool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, addresses: Sequence[_builtins.str], pool: _builtins.str, avoid_buggy_ips: Optional[_builtins.bool] = ..., manual_assign: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pool(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avoidBuggyIps")
    def avoid_buggy_ips(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualAssign")
    def manual_assign(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, node_pool_config: Optional[outputs.BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePoolConfig")
    def node_pool_config(self) -> Optional[outputs.BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfig]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, labels: Optional[Mapping[str, _builtins.str]] = ..., node_configs: Optional[Sequence[outputs.BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfig]] = ..., operating_system: Optional[_builtins.str] = ..., taints: Optional[Sequence[outputs.BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaint]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(self) -> Optional[Sequence[outputs.BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def taints(self) -> Optional[Sequence[outputs.BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaint]]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigNodeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, labels: Optional[Mapping[str, _builtins.str]] = ..., node_ip: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeIp")
    def node_ip(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerMetalLbConfigLoadBalancerNodePoolConfigNodePoolConfigTaint(dict):
    def __init__(__self__, *, effect: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerPortConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, control_plane_load_balancer_port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneLoadBalancerPort")
    def control_plane_load_balancer_port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class BareMetalClusterLoadBalancerVipConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, control_plane_vip: _builtins.str, ingress_vip: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneVip")
    def control_plane_vip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressVip")
    def ingress_vip(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BareMetalClusterMaintenanceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, maintenance_address_cidr_blocks: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceAddressCidrBlocks")
    def maintenance_address_cidr_blocks(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, advanced_networking: Optional[_builtins.bool] = ..., island_mode_cidr: Optional[outputs.BareMetalClusterNetworkConfigIslandModeCidr] = ..., multiple_network_interfaces_config: Optional[outputs.BareMetalClusterNetworkConfigMultipleNetworkInterfacesConfig] = ..., sr_iov_config: Optional[outputs.BareMetalClusterNetworkConfigSrIovConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedNetworking")
    def advanced_networking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="islandModeCidr")
    def island_mode_cidr(self) -> Optional[outputs.BareMetalClusterNetworkConfigIslandModeCidr]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multipleNetworkInterfacesConfig")
    def multiple_network_interfaces_config(self) -> Optional[outputs.BareMetalClusterNetworkConfigMultipleNetworkInterfacesConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="srIovConfig")
    def sr_iov_config(self) -> Optional[outputs.BareMetalClusterNetworkConfigSrIovConfig]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterNetworkConfigIslandModeCidr(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pod_address_cidr_blocks: Sequence[_builtins.str], service_address_cidr_blocks: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="podAddressCidrBlocks")
    def pod_address_cidr_blocks(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAddressCidrBlocks")
    def service_address_cidr_blocks(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterNetworkConfigMultipleNetworkInterfacesConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterNetworkConfigSrIovConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterNodeAccessConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, login_user: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginUser")
    def login_user(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterNodeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_runtime: Optional[_builtins.str] = ..., max_pods_per_node: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerRuntime")
    def container_runtime(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterOsEnvironmentConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, package_repo_excluded: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageRepoExcluded")
    def package_repo_excluded(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class BareMetalClusterProxy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, uri: _builtins.str, no_proxies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noProxies")
    def no_proxies(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterSecurityConfig(dict):
    def __init__(__self__, *, authorization: Optional[outputs.BareMetalClusterSecurityConfigAuthorization] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> Optional[outputs.BareMetalClusterSecurityConfigAuthorization]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterSecurityConfigAuthorization(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, admin_users: Sequence[outputs.BareMetalClusterSecurityConfigAuthorizationAdminUser]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUsers")
    def admin_users(self) -> Sequence[outputs.BareMetalClusterSecurityConfigAuthorizationAdminUser]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterSecurityConfigAuthorizationAdminUser(dict):
    def __init__(__self__, *, username: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BareMetalClusterStatus(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conditions: Optional[Sequence[outputs.BareMetalClusterStatusCondition]] = ..., error_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.BareMetalClusterStatusCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterStatusCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterStorage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lvp_node_mounts_config: outputs.BareMetalClusterStorageLvpNodeMountsConfig, lvp_share_config: outputs.BareMetalClusterStorageLvpShareConfig) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lvpNodeMountsConfig")
    def lvp_node_mounts_config(self) -> outputs.BareMetalClusterStorageLvpNodeMountsConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lvpShareConfig")
    def lvp_share_config(self) -> outputs.BareMetalClusterStorageLvpShareConfig:
        
        ...
    


@pulumi.output_type
class BareMetalClusterStorageLvpNodeMountsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, path: _builtins.str, storage_class: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BareMetalClusterStorageLvpShareConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lvp_config: outputs.BareMetalClusterStorageLvpShareConfigLvpConfig, shared_path_pv_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lvpConfig")
    def lvp_config(self) -> outputs.BareMetalClusterStorageLvpShareConfigLvpConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedPathPvCount")
    def shared_path_pv_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterStorageLvpShareConfigLvpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, path: _builtins.str, storage_class: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BareMetalClusterUpgradePolicy(dict):
    def __init__(__self__, *, policy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterValidationCheck(dict):
    def __init__(__self__, *, options: Optional[_builtins.str] = ..., scenario: Optional[_builtins.str] = ..., statuses: Optional[Sequence[outputs.BareMetalClusterValidationCheckStatus]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scenario(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Optional[Sequence[outputs.BareMetalClusterValidationCheckStatus]]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterValidationCheckStatus(dict):
    def __init__(__self__, *, results: Optional[Sequence[outputs.BareMetalClusterValidationCheckStatusResult]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def results(self) -> Optional[Sequence[outputs.BareMetalClusterValidationCheckStatusResult]]:
        
        ...
    


@pulumi.output_type
class BareMetalClusterValidationCheckStatusResult(dict):
    def __init__(__self__, *, category: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., details: Optional[_builtins.str] = ..., options: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalNodePoolNodePoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, node_configs: Sequence[outputs.BareMetalNodePoolNodePoolConfigNodeConfig], labels: Optional[Mapping[str, _builtins.str]] = ..., operating_system: Optional[_builtins.str] = ..., taints: Optional[Sequence[outputs.BareMetalNodePoolNodePoolConfigTaint]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(self) -> Sequence[outputs.BareMetalNodePoolNodePoolConfigNodeConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def taints(self) -> Optional[Sequence[outputs.BareMetalNodePoolNodePoolConfigTaint]]:
        
        ...
    


@pulumi.output_type
class BareMetalNodePoolNodePoolConfigNodeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, labels: Optional[Mapping[str, _builtins.str]] = ..., node_ip: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeIp")
    def node_ip(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalNodePoolNodePoolConfigTaint(dict):
    def __init__(__self__, *, effect: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalNodePoolStatus(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conditions: Optional[Sequence[outputs.BareMetalNodePoolStatusCondition]] = ..., error_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.BareMetalNodePoolStatusCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BareMetalNodePoolStatusCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareClusterAntiAffinityGroups(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aag_config_disabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aagConfigDisabled")
    def aag_config_disabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class VMwareClusterAuthorization(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, admin_users: Optional[Sequence[outputs.VMwareClusterAuthorizationAdminUser]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUsers")
    def admin_users(self) -> Optional[Sequence[outputs.VMwareClusterAuthorizationAdminUser]]:
        
        ...
    


@pulumi.output_type
class VMwareClusterAuthorizationAdminUser(dict):
    def __init__(__self__, *, username: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VMwareClusterAutoRepairConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class VMwareClusterControlPlaneNode(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_resize_config: Optional[outputs.VMwareClusterControlPlaneNodeAutoResizeConfig] = ..., cpus: Optional[_builtins.int] = ..., memory: Optional[_builtins.int] = ..., replicas: Optional[_builtins.int] = ..., vsphere_configs: Optional[Sequence[outputs.VMwareClusterControlPlaneNodeVsphereConfig]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoResizeConfig")
    def auto_resize_config(self) -> Optional[outputs.VMwareClusterControlPlaneNodeAutoResizeConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpus(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vsphereConfigs")
    def vsphere_configs(self) -> Optional[Sequence[outputs.VMwareClusterControlPlaneNodeVsphereConfig]]:
        
        ...
    


@pulumi.output_type
class VMwareClusterControlPlaneNodeAutoResizeConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class VMwareClusterControlPlaneNodeVsphereConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, datastore: Optional[_builtins.str] = ..., storage_policy_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datastore(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storagePolicyName")
    def storage_policy_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareClusterDataplaneV2(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, advanced_networking: Optional[_builtins.bool] = ..., dataplane_v2_enabled: Optional[_builtins.bool] = ..., windows_dataplane_v2_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedNetworking")
    def advanced_networking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataplaneV2Enabled")
    def dataplane_v2_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsDataplaneV2Enabled")
    def windows_dataplane_v2_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VMwareClusterFleet(dict):
    def __init__(__self__, *, membership: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareClusterLoadBalancer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, f5_config: Optional[outputs.VMwareClusterLoadBalancerF5Config] = ..., manual_lb_config: Optional[outputs.VMwareClusterLoadBalancerManualLbConfig] = ..., metal_lb_config: Optional[outputs.VMwareClusterLoadBalancerMetalLbConfig] = ..., vip_config: Optional[outputs.VMwareClusterLoadBalancerVipConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="f5Config")
    def f5_config(self) -> Optional[outputs.VMwareClusterLoadBalancerF5Config]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualLbConfig")
    def manual_lb_config(self) -> Optional[outputs.VMwareClusterLoadBalancerManualLbConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metalLbConfig")
    def metal_lb_config(self) -> Optional[outputs.VMwareClusterLoadBalancerMetalLbConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vipConfig")
    def vip_config(self) -> Optional[outputs.VMwareClusterLoadBalancerVipConfig]:
        
        ...
    


@pulumi.output_type
class VMwareClusterLoadBalancerF5Config(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address: Optional[_builtins.str] = ..., partition: Optional[_builtins.str] = ..., snat_pool: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def partition(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snatPool")
    def snat_pool(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareClusterLoadBalancerManualLbConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, control_plane_node_port: Optional[_builtins.int] = ..., ingress_http_node_port: Optional[_builtins.int] = ..., ingress_https_node_port: Optional[_builtins.int] = ..., konnectivity_server_node_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneNodePort")
    def control_plane_node_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressHttpNodePort")
    def ingress_http_node_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressHttpsNodePort")
    def ingress_https_node_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="konnectivityServerNodePort")
    def konnectivity_server_node_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class VMwareClusterLoadBalancerMetalLbConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address_pools: Sequence[outputs.VMwareClusterLoadBalancerMetalLbConfigAddressPool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPools")
    def address_pools(self) -> Sequence[outputs.VMwareClusterLoadBalancerMetalLbConfigAddressPool]:
        
        ...
    


@pulumi.output_type
class VMwareClusterLoadBalancerMetalLbConfigAddressPool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, addresses: Sequence[_builtins.str], pool: _builtins.str, avoid_buggy_ips: Optional[_builtins.bool] = ..., manual_assign: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pool(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avoidBuggyIps")
    def avoid_buggy_ips(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualAssign")
    def manual_assign(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VMwareClusterLoadBalancerVipConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, control_plane_vip: Optional[_builtins.str] = ..., ingress_vip: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneVip")
    def control_plane_vip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressVip")
    def ingress_vip(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareClusterNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pod_address_cidr_blocks: Sequence[_builtins.str], service_address_cidr_blocks: Sequence[_builtins.str], control_plane_v2_config: Optional[outputs.VMwareClusterNetworkConfigControlPlaneV2Config] = ..., dhcp_ip_config: Optional[outputs.VMwareClusterNetworkConfigDhcpIpConfig] = ..., host_config: Optional[outputs.VMwareClusterNetworkConfigHostConfig] = ..., static_ip_config: Optional[outputs.VMwareClusterNetworkConfigStaticIpConfig] = ..., vcenter_network: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="podAddressCidrBlocks")
    def pod_address_cidr_blocks(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAddressCidrBlocks")
    def service_address_cidr_blocks(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneV2Config")
    def control_plane_v2_config(self) -> Optional[outputs.VMwareClusterNetworkConfigControlPlaneV2Config]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dhcpIpConfig")
    def dhcp_ip_config(self) -> Optional[outputs.VMwareClusterNetworkConfigDhcpIpConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostConfig")
    def host_config(self) -> Optional[outputs.VMwareClusterNetworkConfigHostConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIpConfig")
    def static_ip_config(self) -> Optional[outputs.VMwareClusterNetworkConfigStaticIpConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcenterNetwork")
    def vcenter_network(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareClusterNetworkConfigControlPlaneV2Config(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, control_plane_ip_block: Optional[outputs.VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlock] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneIpBlock")
    def control_plane_ip_block(self) -> Optional[outputs.VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlock]:
        
        ...
    


@pulumi.output_type
class VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlock(dict):
    def __init__(__self__, *, gateway: Optional[_builtins.str] = ..., ips: Optional[Sequence[outputs.VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlockIp]] = ..., netmask: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ips(self) -> Optional[Sequence[outputs.VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlockIp]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def netmask(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareClusterNetworkConfigControlPlaneV2ConfigControlPlaneIpBlockIp(dict):
    def __init__(__self__, *, hostname: Optional[_builtins.str] = ..., ip: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ip(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareClusterNetworkConfigDhcpIpConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class VMwareClusterNetworkConfigHostConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dns_search_domains: Optional[Sequence[_builtins.str]] = ..., dns_servers: Optional[Sequence[_builtins.str]] = ..., ntp_servers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSearchDomains")
    def dns_search_domains(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ntpServers")
    def ntp_servers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class VMwareClusterNetworkConfigStaticIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_blocks: Sequence[outputs.VMwareClusterNetworkConfigStaticIpConfigIpBlock]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipBlocks")
    def ip_blocks(self) -> Sequence[outputs.VMwareClusterNetworkConfigStaticIpConfigIpBlock]:
        
        ...
    


@pulumi.output_type
class VMwareClusterNetworkConfigStaticIpConfigIpBlock(dict):
    def __init__(__self__, *, gateway: _builtins.str, ips: Sequence[outputs.VMwareClusterNetworkConfigStaticIpConfigIpBlockIp], netmask: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ips(self) -> Sequence[outputs.VMwareClusterNetworkConfigStaticIpConfigIpBlockIp]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def netmask(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VMwareClusterNetworkConfigStaticIpConfigIpBlockIp(dict):
    def __init__(__self__, *, ip: _builtins.str, hostname: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareClusterStatus(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conditions: Optional[Sequence[outputs.VMwareClusterStatusCondition]] = ..., error_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.VMwareClusterStatusCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareClusterStatusCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareClusterStorage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, vsphere_csi_disabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vsphereCsiDisabled")
    def vsphere_csi_disabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class VMwareClusterUpgradePolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, control_plane_only: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneOnly")
    def control_plane_only(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VMwareClusterValidationCheck(dict):
    def __init__(__self__, *, options: Optional[_builtins.str] = ..., scenario: Optional[_builtins.str] = ..., statuses: Optional[Sequence[outputs.VMwareClusterValidationCheckStatus]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scenario(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Optional[Sequence[outputs.VMwareClusterValidationCheckStatus]]:
        
        ...
    


@pulumi.output_type
class VMwareClusterValidationCheckStatus(dict):
    def __init__(__self__, *, results: Optional[Sequence[outputs.VMwareClusterValidationCheckStatusResult]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def results(self) -> Optional[Sequence[outputs.VMwareClusterValidationCheckStatusResult]]:
        
        ...
    


@pulumi.output_type
class VMwareClusterValidationCheckStatusResult(dict):
    def __init__(__self__, *, category: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., details: Optional[_builtins.str] = ..., options: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareClusterVcenter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address: Optional[_builtins.str] = ..., ca_cert_data: Optional[_builtins.str] = ..., cluster: Optional[_builtins.str] = ..., datacenter: Optional[_builtins.str] = ..., datastore: Optional[_builtins.str] = ..., folder: Optional[_builtins.str] = ..., resource_pool: Optional[_builtins.str] = ..., storage_policy_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCertData")
    def ca_cert_data(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datacenter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datastore(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePool")
    def resource_pool(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storagePolicyName")
    def storage_policy_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareNodePoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, image_type: _builtins.str, boot_disk_size_gb: Optional[_builtins.int] = ..., cpus: Optional[_builtins.int] = ..., enable_load_balancer: Optional[_builtins.bool] = ..., image: Optional[_builtins.str] = ..., labels: Optional[Mapping[str, _builtins.str]] = ..., memory_mb: Optional[_builtins.int] = ..., replicas: Optional[_builtins.int] = ..., taints: Optional[Sequence[outputs.VMwareNodePoolConfigTaint]] = ..., vsphere_config: Optional[outputs.VMwareNodePoolConfigVsphereConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpus(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLoadBalancer")
    def enable_load_balancer(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryMb")
    def memory_mb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def taints(self) -> Optional[Sequence[outputs.VMwareNodePoolConfigTaint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vsphereConfig")
    def vsphere_config(self) -> Optional[outputs.VMwareNodePoolConfigVsphereConfig]:
        
        ...
    


@pulumi.output_type
class VMwareNodePoolConfigTaint(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str, effect: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def effect(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareNodePoolConfigVsphereConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, datastore: Optional[_builtins.str] = ..., host_groups: Optional[Sequence[_builtins.str]] = ..., tags: Optional[Sequence[outputs.VMwareNodePoolConfigVsphereConfigTag]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datastore(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostGroups")
    def host_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[outputs.VMwareNodePoolConfigVsphereConfigTag]]:
        
        ...
    


@pulumi.output_type
class VMwareNodePoolConfigVsphereConfigTag(dict):
    def __init__(__self__, *, category: Optional[_builtins.str] = ..., tag: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareNodePoolNodePoolAutoscaling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_replicas: _builtins.int, min_replicas: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxReplicas")
    def max_replicas(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minReplicas")
    def min_replicas(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class VMwareNodePoolStatus(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conditions: Optional[Sequence[outputs.VMwareNodePoolStatusCondition]] = ..., error_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.VMwareNodePoolStatusCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareNodePoolStatusCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterAddonNode(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_resize_config: Optional[outputs.VmwareAdminClusterAddonNodeAutoResizeConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoResizeConfig")
    def auto_resize_config(self) -> Optional[outputs.VmwareAdminClusterAddonNodeAutoResizeConfig]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterAddonNodeAutoResizeConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterAntiAffinityGroups(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aag_config_disabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aagConfigDisabled")
    def aag_config_disabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterAuthorization(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, viewer_users: Optional[Sequence[outputs.VmwareAdminClusterAuthorizationViewerUser]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewerUsers")
    def viewer_users(self) -> Optional[Sequence[outputs.VmwareAdminClusterAuthorizationViewerUser]]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterAuthorizationViewerUser(dict):
    def __init__(__self__, *, username: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterAutoRepairConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterControlPlaneNode(dict):
    def __init__(__self__, *, cpus: Optional[_builtins.int] = ..., memory: Optional[_builtins.int] = ..., replicas: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpus(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterFleet(dict):
    def __init__(__self__, *, membership: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterLoadBalancer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, vip_config: outputs.VmwareAdminClusterLoadBalancerVipConfig, f5_config: Optional[outputs.VmwareAdminClusterLoadBalancerF5Config] = ..., manual_lb_config: Optional[outputs.VmwareAdminClusterLoadBalancerManualLbConfig] = ..., metal_lb_config: Optional[outputs.VmwareAdminClusterLoadBalancerMetalLbConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vipConfig")
    def vip_config(self) -> outputs.VmwareAdminClusterLoadBalancerVipConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="f5Config")
    def f5_config(self) -> Optional[outputs.VmwareAdminClusterLoadBalancerF5Config]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualLbConfig")
    def manual_lb_config(self) -> Optional[outputs.VmwareAdminClusterLoadBalancerManualLbConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metalLbConfig")
    def metal_lb_config(self) -> Optional[outputs.VmwareAdminClusterLoadBalancerMetalLbConfig]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterLoadBalancerF5Config(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address: Optional[_builtins.str] = ..., partition: Optional[_builtins.str] = ..., snat_pool: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def partition(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snatPool")
    def snat_pool(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterLoadBalancerManualLbConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, addons_node_port: Optional[_builtins.int] = ..., control_plane_node_port: Optional[_builtins.int] = ..., ingress_http_node_port: Optional[_builtins.int] = ..., ingress_https_node_port: Optional[_builtins.int] = ..., konnectivity_server_node_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonsNodePort")
    def addons_node_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneNodePort")
    def control_plane_node_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressHttpNodePort")
    def ingress_http_node_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressHttpsNodePort")
    def ingress_https_node_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="konnectivityServerNodePort")
    def konnectivity_server_node_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterLoadBalancerMetalLbConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterLoadBalancerVipConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, control_plane_vip: _builtins.str, addons_vip: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneVip")
    def control_plane_vip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonsVip")
    def addons_vip(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pod_address_cidr_blocks: Sequence[_builtins.str], service_address_cidr_blocks: Sequence[_builtins.str], dhcp_ip_config: Optional[outputs.VmwareAdminClusterNetworkConfigDhcpIpConfig] = ..., ha_control_plane_config: Optional[outputs.VmwareAdminClusterNetworkConfigHaControlPlaneConfig] = ..., host_config: Optional[outputs.VmwareAdminClusterNetworkConfigHostConfig] = ..., static_ip_config: Optional[outputs.VmwareAdminClusterNetworkConfigStaticIpConfig] = ..., vcenter_network: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="podAddressCidrBlocks")
    def pod_address_cidr_blocks(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAddressCidrBlocks")
    def service_address_cidr_blocks(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dhcpIpConfig")
    def dhcp_ip_config(self) -> Optional[outputs.VmwareAdminClusterNetworkConfigDhcpIpConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="haControlPlaneConfig")
    def ha_control_plane_config(self) -> Optional[outputs.VmwareAdminClusterNetworkConfigHaControlPlaneConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostConfig")
    def host_config(self) -> Optional[outputs.VmwareAdminClusterNetworkConfigHostConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIpConfig")
    def static_ip_config(self) -> Optional[outputs.VmwareAdminClusterNetworkConfigStaticIpConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcenterNetwork")
    def vcenter_network(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterNetworkConfigDhcpIpConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterNetworkConfigHaControlPlaneConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, control_plane_ip_block: Optional[outputs.VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlock] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneIpBlock")
    def control_plane_ip_block(self) -> Optional[outputs.VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlock]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlock(dict):
    def __init__(__self__, *, gateway: _builtins.str, ips: Sequence[outputs.VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlockIp], netmask: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ips(self) -> Sequence[outputs.VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlockIp]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def netmask(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterNetworkConfigHaControlPlaneConfigControlPlaneIpBlockIp(dict):
    def __init__(__self__, *, ip: _builtins.str, hostname: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterNetworkConfigHostConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dns_search_domains: Optional[Sequence[_builtins.str]] = ..., dns_servers: Optional[Sequence[_builtins.str]] = ..., ntp_servers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSearchDomains")
    def dns_search_domains(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ntpServers")
    def ntp_servers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterNetworkConfigStaticIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_blocks: Optional[Sequence[outputs.VmwareAdminClusterNetworkConfigStaticIpConfigIpBlock]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipBlocks")
    def ip_blocks(self) -> Optional[Sequence[outputs.VmwareAdminClusterNetworkConfigStaticIpConfigIpBlock]]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterNetworkConfigStaticIpConfigIpBlock(dict):
    def __init__(__self__, *, gateway: _builtins.str, ips: Sequence[outputs.VmwareAdminClusterNetworkConfigStaticIpConfigIpBlockIp], netmask: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ips(self) -> Sequence[outputs.VmwareAdminClusterNetworkConfigStaticIpConfigIpBlockIp]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def netmask(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterNetworkConfigStaticIpConfigIpBlockIp(dict):
    def __init__(__self__, *, ip: _builtins.str, hostname: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterPlatformConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bundles: Optional[Sequence[outputs.VmwareAdminClusterPlatformConfigBundle]] = ..., platform_version: Optional[_builtins.str] = ..., required_platform_version: Optional[_builtins.str] = ..., statuses: Optional[Sequence[outputs.VmwareAdminClusterPlatformConfigStatus]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bundles(self) -> Optional[Sequence[outputs.VmwareAdminClusterPlatformConfigBundle]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredPlatformVersion")
    def required_platform_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Optional[Sequence[outputs.VmwareAdminClusterPlatformConfigStatus]]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterPlatformConfigBundle(dict):
    def __init__(__self__, *, statuses: Optional[Sequence[outputs.VmwareAdminClusterPlatformConfigBundleStatus]] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Optional[Sequence[outputs.VmwareAdminClusterPlatformConfigBundleStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterPlatformConfigBundleStatus(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conditions: Optional[Sequence[outputs.VmwareAdminClusterPlatformConfigBundleStatusCondition]] = ..., error_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.VmwareAdminClusterPlatformConfigBundleStatusCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterPlatformConfigBundleStatusCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterPlatformConfigStatus(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conditions: Optional[Sequence[outputs.VmwareAdminClusterPlatformConfigStatusCondition]] = ..., error_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.VmwareAdminClusterPlatformConfigStatusCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterPlatformConfigStatusCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterPrivateRegistryConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address: Optional[_builtins.str] = ..., ca_cert: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCert")
    def ca_cert(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterProxy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, url: _builtins.str, no_proxy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noProxy")
    def no_proxy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterStatus(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conditions: Optional[Sequence[outputs.VmwareAdminClusterStatusCondition]] = ..., error_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.VmwareAdminClusterStatusCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterStatusCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VmwareAdminClusterVcenter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address: Optional[_builtins.str] = ..., ca_cert_data: Optional[_builtins.str] = ..., cluster: Optional[_builtins.str] = ..., data_disk: Optional[_builtins.str] = ..., datacenter: Optional[_builtins.str] = ..., datastore: Optional[_builtins.str] = ..., folder: Optional[_builtins.str] = ..., resource_pool: Optional[_builtins.str] = ..., storage_policy_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCertData")
    def ca_cert_data(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDisk")
    def data_disk(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datacenter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datastore(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePool")
    def resource_pool(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storagePolicyName")
    def storage_policy_name(self) -> Optional[_builtins.str]:
        
        ...
    


