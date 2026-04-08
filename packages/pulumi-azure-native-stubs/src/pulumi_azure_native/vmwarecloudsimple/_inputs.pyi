import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GuestOSCustomizationArgs",
    "GuestOSCustomizationArgsDict",
    "GuestOSNICCustomizationArgs",
    "GuestOSNICCustomizationArgsDict",
    "ResourcePoolArgs",
    "ResourcePoolArgsDict",
    "SkuArgs",
    "SkuArgsDict",
    "VirtualDiskArgs",
    "VirtualDiskArgsDict",
    "VirtualNetworkArgs",
    "VirtualNetworkArgsDict",
    "VirtualNicArgs",
    "VirtualNicArgsDict",
]

class GuestOSCustomizationArgsDict(TypedDict):
    dns_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    host_name: NotRequired[pulumi.Input[_builtins.str]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    policy_id: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GuestOSCustomizationArgs:
    def __init__(
        __self__,
        *,
        dns_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        host_name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_servers.setter
    def dns_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_name.setter
    def host_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuestOSNICCustomizationArgsDict(TypedDict):
    allocation: NotRequired[pulumi.Input[_builtins.str]]
    dns_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    gateway: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    mask: NotRequired[pulumi.Input[_builtins.str]]
    primary_wins_server: NotRequired[pulumi.Input[_builtins.str]]
    secondary_wins_server: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GuestOSNICCustomizationArgs:
    def __init__(
        __self__,
        *,
        allocation: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        gateway: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        mask: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_wins_server: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_wins_server: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def allocation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @allocation.setter
    def allocation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_servers.setter
    def dns_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def gateway(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @gateway.setter
    def gateway(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mask(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mask.setter
    def mask(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryWinsServer")
    def primary_wins_server(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_wins_server.setter
    def primary_wins_server(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryWinsServer")
    def secondary_wins_server(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secondary_wins_server.setter
    def secondary_wins_server(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourcePoolArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ResourcePoolArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...

class SkuArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    capacity: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        capacity: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        family: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualDiskArgsDict(TypedDict):
    controller_id: pulumi.Input[_builtins.str]
    independence_mode: pulumi.Input[DiskIndependenceMode]
    total_size: pulumi.Input[_builtins.int]
    virtual_disk_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualDiskArgs:
    def __init__(
        __self__,
        *,
        controller_id: pulumi.Input[_builtins.str],
        independence_mode: pulumi.Input[DiskIndependenceMode],
        total_size: pulumi.Input[_builtins.int],
        virtual_disk_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controllerId")
    def controller_id(self) -> pulumi.Input[_builtins.str]: ...
    @controller_id.setter
    def controller_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="independenceMode")
    def independence_mode(self) -> pulumi.Input[DiskIndependenceMode]: ...
    @independence_mode.setter
    def independence_mode(self, value: pulumi.Input[DiskIndependenceMode]): ...
    @_builtins.property
    @pulumi.getter(name="totalSize")
    def total_size(self) -> pulumi.Input[_builtins.int]: ...
    @total_size.setter
    def total_size(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="virtualDiskId")
    def virtual_disk_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_disk_id.setter
    def virtual_disk_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualNetworkArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNetworkArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...

class VirtualNicArgsDict(TypedDict):
    network: pulumi.Input[VirtualNetworkArgsDict]
    nic_type: pulumi.Input[NICType]
    customization: NotRequired[pulumi.Input[GuestOSNICCustomizationArgsDict]]
    ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    mac_address: NotRequired[pulumi.Input[_builtins.str]]
    power_on_boot: NotRequired[pulumi.Input[_builtins.bool]]
    virtual_nic_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualNicArgs:
    def __init__(
        __self__,
        *,
        network: pulumi.Input[VirtualNetworkArgs],
        nic_type: pulumi.Input[NICType],
        customization: Optional[pulumi.Input[GuestOSNICCustomizationArgs]] = ...,
        ip_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        mac_address: Optional[pulumi.Input[_builtins.str]] = ...,
        power_on_boot: Optional[pulumi.Input[_builtins.bool]] = ...,
        virtual_nic_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[VirtualNetworkArgs]: ...
    @network.setter
    def network(self, value: pulumi.Input[VirtualNetworkArgs]): ...
    @_builtins.property
    @pulumi.getter(name="nicType")
    def nic_type(self) -> pulumi.Input[NICType]: ...
    @nic_type.setter
    def nic_type(self, value: pulumi.Input[NICType]): ...
    @_builtins.property
    @pulumi.getter
    def customization(self) -> Optional[pulumi.Input[GuestOSNICCustomizationArgs]]: ...
    @customization.setter
    def customization(
        self, value: Optional[pulumi.Input[GuestOSNICCustomizationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ip_addresses.setter
    def ip_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mac_address.setter
    def mac_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="powerOnBoot")
    def power_on_boot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @power_on_boot.setter
    def power_on_boot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualNicId")
    def virtual_nic_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_nic_id.setter
    def virtual_nic_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
