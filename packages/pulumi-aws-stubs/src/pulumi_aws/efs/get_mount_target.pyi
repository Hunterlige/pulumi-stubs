import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMountTargetResult",
    "AwaitableGetMountTargetResult",
    "get_mount_target",
    "get_mount_target_output",
]

@pulumi.output_type
class GetMountTargetResult:
    def __init__(
        __self__,
        access_point_id=...,
        availability_zone_id=...,
        availability_zone_name=...,
        dns_name=...,
        file_system_arn=...,
        file_system_id=...,
        id=...,
        ip_address=...,
        ip_address_type=...,
        ipv6_address=...,
        mount_target_dns_name=...,
        mount_target_id=...,
        network_interface_id=...,
        owner_id=...,
        region=...,
        security_groups=...,
        subnet_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPointId")
    def access_point_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneName")
    def availability_zone_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemArn")
    def file_system_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mountTargetDnsName")
    def mount_target_dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mountTargetId")
    def mount_target_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...

class AwaitableGetMountTargetResult(GetMountTargetResult):
    def __await__(self): ...

def get_mount_target(
    access_point_id: Optional[_builtins.str] = ...,
    file_system_id: Optional[_builtins.str] = ...,
    mount_target_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMountTargetResult: ...
def get_mount_target_output(
    access_point_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    file_system_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    mount_target_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMountTargetResult]: ...
