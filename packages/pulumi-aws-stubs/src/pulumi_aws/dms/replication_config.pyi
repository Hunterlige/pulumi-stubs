import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReplicationConfigArgs", "ReplicationConfig"]

@pulumi.input_type
class ReplicationConfigArgs:
    def __init__(
        __self__,
        *,
        compute_config: pulumi.Input[ReplicationConfigComputeConfigArgs],
        replication_config_identifier: pulumi.Input[_builtins.str],
        replication_type: pulumi.Input[_builtins.str],
        source_endpoint_arn: pulumi.Input[_builtins.str],
        table_mappings: pulumi.Input[_builtins.str],
        target_endpoint_arn: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_settings: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        start_replication: Optional[pulumi.Input[_builtins.bool]] = ...,
        supplemental_settings: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeConfig")
    def compute_config(self) -> pulumi.Input[ReplicationConfigComputeConfigArgs]: ...
    @compute_config.setter
    def compute_config(
        self, value: pulumi.Input[ReplicationConfigComputeConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicationConfigIdentifier")
    def replication_config_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @replication_config_identifier.setter
    def replication_config_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="replicationType")
    def replication_type(self) -> pulumi.Input[_builtins.str]: ...
    @replication_type.setter
    def replication_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceEndpointArn")
    def source_endpoint_arn(self) -> pulumi.Input[_builtins.str]: ...
    @source_endpoint_arn.setter
    def source_endpoint_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableMappings")
    def table_mappings(self) -> pulumi.Input[_builtins.str]: ...
    @table_mappings.setter
    def table_mappings(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetEndpointArn")
    def target_endpoint_arn(self) -> pulumi.Input[_builtins.str]: ...
    @target_endpoint_arn.setter
    def target_endpoint_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationSettings")
    def replication_settings(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_settings.setter
    def replication_settings(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_identifier.setter
    def resource_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startReplication")
    def start_replication(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @start_replication.setter
    def start_replication(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="supplementalSettings")
    def supplemental_settings(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @supplemental_settings.setter
    def supplemental_settings(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class _ReplicationConfigState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_config: Optional[
            pulumi.Input[ReplicationConfigComputeConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_config_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_settings: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_type: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        source_endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        start_replication: Optional[pulumi.Input[_builtins.bool]] = ...,
        supplemental_settings: Optional[pulumi.Input[_builtins.str]] = ...,
        table_mappings: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computeConfig")
    def compute_config(
        self,
    ) -> Optional[pulumi.Input[ReplicationConfigComputeConfigArgs]]: ...
    @compute_config.setter
    def compute_config(
        self, value: Optional[pulumi.Input[ReplicationConfigComputeConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationConfigIdentifier")
    def replication_config_identifier(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_config_identifier.setter
    def replication_config_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicationSettings")
    def replication_settings(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_settings.setter
    def replication_settings(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationType")
    def replication_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_type.setter
    def replication_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_identifier.setter
    def resource_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceEndpointArn")
    def source_endpoint_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_endpoint_arn.setter
    def source_endpoint_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startReplication")
    def start_replication(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @start_replication.setter
    def start_replication(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="supplementalSettings")
    def supplemental_settings(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @supplemental_settings.setter
    def supplemental_settings(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tableMappings")
    def table_mappings(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_mappings.setter
    def table_mappings(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="targetEndpointArn")
    def target_endpoint_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_endpoint_arn.setter
    def target_endpoint_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:dms/replicationConfig:ReplicationConfig")
class ReplicationConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        compute_config: Optional[
            pulumi.Input[
                Union[
                    ReplicationConfigComputeConfigArgs,
                    ReplicationConfigComputeConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_config_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_settings: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_type: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        source_endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        start_replication: Optional[pulumi.Input[_builtins.bool]] = ...,
        supplemental_settings: Optional[pulumi.Input[_builtins.str]] = ...,
        table_mappings: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReplicationConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_config: Optional[
            pulumi.Input[
                Union[
                    ReplicationConfigComputeConfigArgs,
                    ReplicationConfigComputeConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_config_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_settings: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_type: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        source_endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        start_replication: Optional[pulumi.Input[_builtins.bool]] = ...,
        supplemental_settings: Optional[pulumi.Input[_builtins.str]] = ...,
        table_mappings: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ReplicationConfig: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="computeConfig")
    def compute_config(
        self,
    ) -> pulumi.Output[outputs.ReplicationConfigComputeConfig]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationConfigIdentifier")
    def replication_config_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationSettings")
    def replication_settings(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationType")
    def replication_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceEndpointArn")
    def source_endpoint_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startReplication")
    def start_replication(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="supplementalSettings")
    def supplemental_settings(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tableMappings")
    def table_mappings(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetEndpointArn")
    def target_endpoint_arn(self) -> pulumi.Output[_builtins.str]: ...
