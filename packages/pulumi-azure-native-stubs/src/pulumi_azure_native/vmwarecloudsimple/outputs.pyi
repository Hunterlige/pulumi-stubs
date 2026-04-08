import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DedicatedCloudNodePropertiesResponse",
    "GuestOSCustomizationResponse",
    "GuestOSNICCustomizationResponse",
    "ResourcePoolResponse",
    "SkuResponse",
    "VirtualDiskControllerResponse",
    "VirtualDiskResponse",
    "VirtualNetworkResponse",
    "VirtualNicResponse",
]

@pulumi.output_type
class DedicatedCloudNodePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        availability_zone_id: _builtins.str,
        availability_zone_name: _builtins.str,
        cloud_rack_name: _builtins.str,
        created: _builtins.str,
        id: _builtins.str,
        name: _builtins.str,
        nodes_count: _builtins.int,
        placement_group_id: _builtins.str,
        placement_group_name: _builtins.str,
        private_cloud_id: _builtins.str,
        private_cloud_name: _builtins.str,
        provisioning_state: _builtins.str,
        purchase_id: _builtins.str,
        status: _builtins.str,
        vmware_cluster_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneName")
    def availability_zone_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudRackName")
    def cloud_rack_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodesCount")
    def nodes_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="placementGroupId")
    def placement_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="placementGroupName")
    def placement_group_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateCloudId")
    def private_cloud_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="purchaseId")
    def purchase_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vmwareClusterName")
    def vmware_cluster_name(self) -> _builtins.str: ...

@pulumi.output_type
class GuestOSCustomizationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_servers: Optional[Sequence[_builtins.str]] = ...,
        host_name: Optional[_builtins.str] = ...,
        password: Optional[_builtins.str] = ...,
        policy_id: Optional[_builtins.str] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuestOSNICCustomizationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allocation: Optional[_builtins.str] = ...,
        dns_servers: Optional[Sequence[_builtins.str]] = ...,
        gateway: Optional[Sequence[_builtins.str]] = ...,
        ip_address: Optional[_builtins.str] = ...,
        mask: Optional[_builtins.str] = ...,
        primary_wins_server: Optional[_builtins.str] = ...,
        secondary_wins_server: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def allocation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mask(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryWinsServer")
    def primary_wins_server(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryWinsServer")
    def secondary_wins_server(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourcePoolResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        full_name: _builtins.str,
        id: _builtins.str,
        location: _builtins.str,
        name: _builtins.str,
        private_cloud_id: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fullName")
    def full_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateCloudId")
    def private_cloud_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class SkuResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        capacity: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        family: Optional[_builtins.str] = ...,
        tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualDiskControllerResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        sub_type: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subType")
    def sub_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualDiskResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        controller_id: _builtins.str,
        independence_mode: _builtins.str,
        total_size: _builtins.int,
        virtual_disk_name: _builtins.str,
        virtual_disk_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controllerId")
    def controller_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="independenceMode")
    def independence_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="totalSize")
    def total_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="virtualDiskName")
    def virtual_disk_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualDiskId")
    def virtual_disk_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualNetworkResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        assignable: _builtins.bool,
        id: _builtins.str,
        location: _builtins.str,
        name: _builtins.str,
        private_cloud_id: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def assignable(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateCloudId")
    def private_cloud_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNicResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network: outputs.VirtualNetworkResponse,
        nic_type: _builtins.str,
        virtual_nic_name: _builtins.str,
        customization: Optional[outputs.GuestOSNICCustomizationResponse] = ...,
        ip_addresses: Optional[Sequence[_builtins.str]] = ...,
        mac_address: Optional[_builtins.str] = ...,
        power_on_boot: Optional[_builtins.bool] = ...,
        virtual_nic_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> outputs.VirtualNetworkResponse: ...
    @_builtins.property
    @pulumi.getter(name="nicType")
    def nic_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualNicName")
    def virtual_nic_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def customization(self) -> Optional[outputs.GuestOSNICCustomizationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="powerOnBoot")
    def power_on_boot(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="virtualNicId")
    def virtual_nic_id(self) -> Optional[_builtins.str]: ...
