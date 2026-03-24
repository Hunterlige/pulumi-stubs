import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetReplicationSubnetGroupResult",
    "AwaitableGetReplicationSubnetGroupResult",
    "get_replication_subnet_group",
    "get_replication_subnet_group_output",
]

@pulumi.output_type
class GetReplicationSubnetGroupResult:
    def __init__(
        __self__,
        id=...,
        region=...,
        replication_subnet_group_arn=...,
        replication_subnet_group_description=...,
        replication_subnet_group_id=...,
        subnet_group_status=...,
        subnet_ids=...,
        tags=...,
        vpc_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupArn")
    def replication_subnet_group_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupDescription")
    def replication_subnet_group_description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetGroupStatus")
    def subnet_group_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

class AwaitableGetReplicationSubnetGroupResult(GetReplicationSubnetGroupResult):
    def __await__(self): ...

def get_replication_subnet_group(
    region: Optional[_builtins.str] = ...,
    replication_subnet_group_id: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetReplicationSubnetGroupResult: ...
def get_replication_subnet_group_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    replication_subnet_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetReplicationSubnetGroupResult]: ...
