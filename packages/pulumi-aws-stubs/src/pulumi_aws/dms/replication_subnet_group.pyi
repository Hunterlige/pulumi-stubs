import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReplicationSubnetGroupArgs", "ReplicationSubnetGroup"]

@pulumi.input_type
class ReplicationSubnetGroupArgs:
    def __init__(
        __self__,
        *,
        replication_subnet_group_description: pulumi.Input[_builtins.str],
        replication_subnet_group_id: pulumi.Input[_builtins.str],
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupDescription")
    def replication_subnet_group_description(self) -> pulumi.Input[_builtins.str]: ...
    @replication_subnet_group_description.setter
    def replication_subnet_group_description(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @replication_subnet_group_id.setter
    def replication_subnet_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _ReplicationSubnetGroupState:
    def __init__(
        __self__,
        *,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_subnet_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_subnet_group_description: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        replication_subnet_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupArn")
    def replication_subnet_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_subnet_group_arn.setter
    def replication_subnet_group_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupDescription")
    def replication_subnet_group_description(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_subnet_group_description.setter
    def replication_subnet_group_description(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_subnet_group_id.setter
    def replication_subnet_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ReplicationSubnetGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_subnet_group_description: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        replication_subnet_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReplicationSubnetGroupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_subnet_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_subnet_group_description: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        replication_subnet_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ReplicationSubnetGroup: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupArn")
    def replication_subnet_group_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupDescription")
    def replication_subnet_group_description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]: ...
