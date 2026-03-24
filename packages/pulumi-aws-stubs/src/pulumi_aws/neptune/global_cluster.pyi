import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GlobalClusterArgs", "GlobalCluster"]

@pulumi.input_type
class GlobalClusterArgs:
    def __init__(
        __self__,
        *,
        global_cluster_identifier: pulumi.Input[_builtins.str],
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_db_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @global_cluster_identifier.setter
    def global_cluster_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine.setter
    def engine(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceDbClusterIdentifier")
    def source_db_cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_db_cluster_identifier.setter
    def source_db_cluster_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @storage_encrypted.setter
    def storage_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _GlobalClusterState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        global_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        global_cluster_members: Optional[
            pulumi.Input[Sequence[pulumi.Input[GlobalClusterGlobalClusterMemberArgs]]]
        ] = ...,
        global_cluster_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_db_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine.setter
    def engine(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @global_cluster_identifier.setter
    def global_cluster_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalClusterMembers")
    def global_cluster_members(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GlobalClusterGlobalClusterMemberArgs]]]
    ]: ...
    @global_cluster_members.setter
    def global_cluster_members(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[GlobalClusterGlobalClusterMemberArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalClusterResourceId")
    def global_cluster_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @global_cluster_resource_id.setter
    def global_cluster_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceDbClusterIdentifier")
    def source_db_cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_db_cluster_identifier.setter
    def source_db_cluster_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @storage_encrypted.setter
    def storage_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("aws:neptune/globalCluster:GlobalCluster")
class GlobalCluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        global_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_db_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GlobalClusterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        global_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        global_cluster_members: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            GlobalClusterGlobalClusterMemberArgs,
                            GlobalClusterGlobalClusterMemberArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        global_cluster_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_db_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> GlobalCluster: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="globalClusterMembers")
    def global_cluster_members(
        self,
    ) -> pulumi.Output[Sequence[outputs.GlobalClusterGlobalClusterMember]]: ...
    @_builtins.property
    @pulumi.getter(name="globalClusterResourceId")
    def global_cluster_resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceDbClusterIdentifier")
    def source_db_cluster_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> pulumi.Output[_builtins.bool]: ...
