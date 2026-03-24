import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReplicatorArgs", "Replicator"]

@pulumi.input_type
class ReplicatorArgs:
    def __init__(
        __self__,
        *,
        kafka_clusters: pulumi.Input[
            Sequence[pulumi.Input[ReplicatorKafkaClusterArgs]]
        ],
        replication_info_list: pulumi.Input[ReplicatorReplicationInfoListArgs],
        replicator_name: pulumi.Input[_builtins.str],
        service_execution_role_arn: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kafkaClusters")
    def kafka_clusters(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ReplicatorKafkaClusterArgs]]]: ...
    @kafka_clusters.setter
    def kafka_clusters(
        self, value: pulumi.Input[Sequence[pulumi.Input[ReplicatorKafkaClusterArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicationInfoList")
    def replication_info_list(
        self,
    ) -> pulumi.Input[ReplicatorReplicationInfoListArgs]: ...
    @replication_info_list.setter
    def replication_info_list(
        self, value: pulumi.Input[ReplicatorReplicationInfoListArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicatorName")
    def replicator_name(self) -> pulumi.Input[_builtins.str]: ...
    @replicator_name.setter
    def replicator_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceExecutionRoleArn")
    def service_execution_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @service_execution_role_arn.setter
    def service_execution_role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class _ReplicatorState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        current_version: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        kafka_clusters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReplicatorKafkaClusterArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_info_list: Optional[
            pulumi.Input[ReplicatorReplicationInfoListArgs]
        ] = ...,
        replicator_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @current_version.setter
    def current_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kafkaClusters")
    def kafka_clusters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReplicatorKafkaClusterArgs]]]]: ...
    @kafka_clusters.setter
    def kafka_clusters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReplicatorKafkaClusterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationInfoList")
    def replication_info_list(
        self,
    ) -> Optional[pulumi.Input[ReplicatorReplicationInfoListArgs]]: ...
    @replication_info_list.setter
    def replication_info_list(
        self, value: Optional[pulumi.Input[ReplicatorReplicationInfoListArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicatorName")
    def replicator_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replicator_name.setter
    def replicator_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceExecutionRoleArn")
    def service_execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_execution_role_arn.setter
    def service_execution_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
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

@pulumi.type_token("aws:msk/replicator:Replicator")
class Replicator(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        kafka_clusters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReplicatorKafkaClusterArgs, ReplicatorKafkaClusterArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_info_list: Optional[
            pulumi.Input[
                Union[
                    ReplicatorReplicationInfoListArgs,
                    ReplicatorReplicationInfoListArgsDict,
                ]
            ]
        ] = ...,
        replicator_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReplicatorArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        current_version: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        kafka_clusters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReplicatorKafkaClusterArgs, ReplicatorKafkaClusterArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_info_list: Optional[
            pulumi.Input[
                Union[
                    ReplicatorReplicationInfoListArgs,
                    ReplicatorReplicationInfoListArgsDict,
                ]
            ]
        ] = ...,
        replicator_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Replicator: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="kafkaClusters")
    def kafka_clusters(
        self,
    ) -> pulumi.Output[Sequence[outputs.ReplicatorKafkaCluster]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationInfoList")
    def replication_info_list(
        self,
    ) -> pulumi.Output[outputs.ReplicatorReplicationInfoList]: ...
    @_builtins.property
    @pulumi.getter(name="replicatorName")
    def replicator_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceExecutionRoleArn")
    def service_execution_role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
