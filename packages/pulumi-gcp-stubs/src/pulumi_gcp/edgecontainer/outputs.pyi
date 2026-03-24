

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterAuthorization', 'ClusterAuthorizationAdminUsers', 'ClusterControlPlane', 'ClusterControlPlaneEncryption', 'ClusterControlPlaneEncryptionKmsStatus', 'ClusterControlPlaneLocal', 'ClusterControlPlaneRemote', 'ClusterFleet', 'ClusterMaintenanceEvent', 'ClusterMaintenancePolicy', 'ClusterMaintenancePolicyMaintenanceExclusion', 'ClusterMaintenancePolicyMaintenanceExclusionWindow', 'ClusterMaintenancePolicyWindow', 'ClusterMaintenancePolicyWindowRecurringWindow', ..., 'ClusterNetworking', 'ClusterSystemAddonsConfig', 'ClusterSystemAddonsConfigIngress', 'NodePoolLocalDiskEncryption', 'NodePoolNodeConfig', 'VpnConnectionDetail', 'VpnConnectionDetailCloudRouter', 'VpnConnectionDetailCloudVpn', 'VpnConnectionVpcProject']
@pulumi.output_type
class ClusterAuthorization(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, admin_users: outputs.ClusterAuthorizationAdminUsers) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUsers")
    def admin_users(self) -> outputs.ClusterAuthorizationAdminUsers:
        
        ...
    


@pulumi.output_type
class ClusterAuthorizationAdminUsers(dict):
    def __init__(__self__, *, username: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClusterControlPlane(dict):
    def __init__(__self__, *, local: Optional[outputs.ClusterControlPlaneLocal] = ..., remote: Optional[outputs.ClusterControlPlaneRemote] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def local(self) -> Optional[outputs.ClusterControlPlaneLocal]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def remote(self) -> Optional[outputs.ClusterControlPlaneRemote]:
        
        ...
    


@pulumi.output_type
class ClusterControlPlaneEncryption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key: Optional[_builtins.str] = ..., kms_key_active_version: Optional[_builtins.str] = ..., kms_key_state: Optional[_builtins.str] = ..., kms_statuses: Optional[Sequence[outputs.ClusterControlPlaneEncryptionKmsStatus]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyActiveVersion")
    def kms_key_active_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyState")
    def kms_key_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsStatuses")
    def kms_statuses(self) -> Optional[Sequence[outputs.ClusterControlPlaneEncryptionKmsStatus]]:
        
        ...
    


@pulumi.output_type
class ClusterControlPlaneEncryptionKmsStatus(dict):
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterControlPlaneLocal(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, machine_filter: Optional[_builtins.str] = ..., node_count: Optional[_builtins.int] = ..., node_location: Optional[_builtins.str] = ..., shared_deployment_policy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineFilter")
    def machine_filter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeLocation")
    def node_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedDeploymentPolicy")
    def shared_deployment_policy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterControlPlaneRemote(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, node_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeLocation")
    def node_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterFleet(dict):
    def __init__(__self__, *, project: _builtins.str, membership: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterMaintenanceEvent(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, create_time: Optional[_builtins.str] = ..., end_time: Optional[_builtins.str] = ..., operation: Optional[_builtins.str] = ..., schedule: Optional[_builtins.str] = ..., start_time: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., target_version: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., update_time: Optional[_builtins.str] = ..., uuid: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVersion")
    def target_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterMaintenancePolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, window: outputs.ClusterMaintenancePolicyWindow, maintenance_exclusions: Optional[Sequence[outputs.ClusterMaintenancePolicyMaintenanceExclusion]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def window(self) -> outputs.ClusterMaintenancePolicyWindow:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceExclusions")
    def maintenance_exclusions(self) -> Optional[Sequence[outputs.ClusterMaintenancePolicyMaintenanceExclusion]]:
        
        ...
    


@pulumi.output_type
class ClusterMaintenancePolicyMaintenanceExclusion(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., window: Optional[outputs.ClusterMaintenancePolicyMaintenanceExclusionWindow] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def window(self) -> Optional[outputs.ClusterMaintenancePolicyMaintenanceExclusionWindow]:
        
        ...
    


@pulumi.output_type
class ClusterMaintenancePolicyMaintenanceExclusionWindow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_time: Optional[_builtins.str] = ..., start_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterMaintenancePolicyWindow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, recurring_window: outputs.ClusterMaintenancePolicyWindowRecurringWindow) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recurringWindow")
    def recurring_window(self) -> outputs.ClusterMaintenancePolicyWindowRecurringWindow:
        
        ...
    


@pulumi.output_type
class ClusterMaintenancePolicyWindowRecurringWindow(dict):
    def __init__(__self__, *, recurrence: Optional[_builtins.str] = ..., window: Optional[outputs.ClusterMaintenancePolicyWindowRecurringWindowWindow] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def window(self) -> Optional[outputs.ClusterMaintenancePolicyWindowRecurringWindowWindow]:
        
        ...
    


@pulumi.output_type
class ClusterMaintenancePolicyWindowRecurringWindowWindow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_time: Optional[_builtins.str] = ..., start_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterNetworking(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_ipv4_cidr_blocks: Sequence[_builtins.str], services_ipv4_cidr_blocks: Sequence[_builtins.str], cluster_ipv6_cidr_blocks: Optional[Sequence[_builtins.str]] = ..., network_type: Optional[_builtins.str] = ..., services_ipv6_cidr_blocks: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIpv4CidrBlocks")
    def cluster_ipv4_cidr_blocks(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicesIpv4CidrBlocks")
    def services_ipv4_cidr_blocks(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIpv6CidrBlocks")
    def cluster_ipv6_cidr_blocks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicesIpv6CidrBlocks")
    def services_ipv6_cidr_blocks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ClusterSystemAddonsConfig(dict):
    def __init__(__self__, *, ingress: Optional[outputs.ClusterSystemAddonsConfigIngress] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> Optional[outputs.ClusterSystemAddonsConfigIngress]:
        
        ...
    


@pulumi.output_type
class ClusterSystemAddonsConfigIngress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disabled: Optional[_builtins.bool] = ..., ipv4_vip: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Vip")
    def ipv4_vip(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NodePoolLocalDiskEncryption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key: Optional[_builtins.str] = ..., kms_key_active_version: Optional[_builtins.str] = ..., kms_key_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyActiveVersion")
    def kms_key_active_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyState")
    def kms_key_state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NodePoolNodeConfig(dict):
    def __init__(__self__, *, labels: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class VpnConnectionDetail(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_routers: Optional[Sequence[outputs.VpnConnectionDetailCloudRouter]] = ..., cloud_vpns: Optional[Sequence[outputs.VpnConnectionDetailCloudVpn]] = ..., error: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudRouters")
    def cloud_routers(self) -> Optional[Sequence[outputs.VpnConnectionDetailCloudRouter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudVpns")
    def cloud_vpns(self) -> Optional[Sequence[outputs.VpnConnectionDetailCloudVpn]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpnConnectionDetailCloudRouter(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpnConnectionDetailCloudVpn(dict):
    def __init__(__self__, *, gateway: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpnConnectionVpcProject(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, project_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]:
        
        ...
    


