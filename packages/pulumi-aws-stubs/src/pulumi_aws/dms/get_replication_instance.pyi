import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetReplicationInstanceResult",
    "AwaitableGetReplicationInstanceResult",
    "get_replication_instance",
    "get_replication_instance_output",
]

@pulumi.output_type
class GetReplicationInstanceResult:
    def __init__(
        __self__,
        allocated_storage=...,
        auto_minor_version_upgrade=...,
        availability_zone=...,
        engine_version=...,
        id=...,
        kms_key_arn=...,
        multi_az=...,
        network_type=...,
        preferred_maintenance_window=...,
        publicly_accessible=...,
        region=...,
        replication_instance_arn=...,
        replication_instance_class=...,
        replication_instance_id=...,
        replication_instance_private_ips=...,
        replication_instance_public_ips=...,
        replication_subnet_group_id=...,
        tags=...,
        vpc_security_group_ids=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="replicationInstanceArn")
    def replication_instance_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="replicationInstanceClass")
    def replication_instance_class(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="replicationInstanceId")
    def replication_instance_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="replicationInstancePrivateIps")
    def replication_instance_private_ips(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationInstancePublicIps")
    def replication_instance_public_ips(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Sequence[_builtins.str]: ...

class AwaitableGetReplicationInstanceResult(GetReplicationInstanceResult):
    def __await__(self): ...

def get_replication_instance(
    region: Optional[_builtins.str] = ...,
    replication_instance_id: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetReplicationInstanceResult: ...
def get_replication_instance_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    replication_instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetReplicationInstanceResult]: ...
