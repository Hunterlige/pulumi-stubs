import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LiteTopicArgs", "LiteTopic"]

@pulumi.input_type
class LiteTopicArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        partition_config: Optional[pulumi.Input[LiteTopicPartitionConfigArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_config: Optional[
            pulumi.Input[LiteTopicReservationConfigArgs]
        ] = ...,
        retention_config: Optional[pulumi.Input[LiteTopicRetentionConfigArgs]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="partitionConfig")
    def partition_config(
        self,
    ) -> Optional[pulumi.Input[LiteTopicPartitionConfigArgs]]: ...
    @partition_config.setter
    def partition_config(
        self, value: Optional[pulumi.Input[LiteTopicPartitionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reservationConfig")
    def reservation_config(
        self,
    ) -> Optional[pulumi.Input[LiteTopicReservationConfigArgs]]: ...
    @reservation_config.setter
    def reservation_config(
        self, value: Optional[pulumi.Input[LiteTopicReservationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionConfig")
    def retention_config(
        self,
    ) -> Optional[pulumi.Input[LiteTopicRetentionConfigArgs]]: ...
    @retention_config.setter
    def retention_config(
        self, value: Optional[pulumi.Input[LiteTopicRetentionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _LiteTopicState:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        partition_config: Optional[pulumi.Input[LiteTopicPartitionConfigArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_config: Optional[
            pulumi.Input[LiteTopicReservationConfigArgs]
        ] = ...,
        retention_config: Optional[pulumi.Input[LiteTopicRetentionConfigArgs]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="partitionConfig")
    def partition_config(
        self,
    ) -> Optional[pulumi.Input[LiteTopicPartitionConfigArgs]]: ...
    @partition_config.setter
    def partition_config(
        self, value: Optional[pulumi.Input[LiteTopicPartitionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reservationConfig")
    def reservation_config(
        self,
    ) -> Optional[pulumi.Input[LiteTopicReservationConfigArgs]]: ...
    @reservation_config.setter
    def reservation_config(
        self, value: Optional[pulumi.Input[LiteTopicReservationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionConfig")
    def retention_config(
        self,
    ) -> Optional[pulumi.Input[LiteTopicRetentionConfigArgs]]: ...
    @retention_config.setter
    def retention_config(
        self, value: Optional[pulumi.Input[LiteTopicRetentionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:pubsub/liteTopic:LiteTopic")
class LiteTopic(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        partition_config: Optional[
            pulumi.Input[
                Union[LiteTopicPartitionConfigArgs, LiteTopicPartitionConfigArgsDict]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_config: Optional[
            pulumi.Input[
                Union[
                    LiteTopicReservationConfigArgs, LiteTopicReservationConfigArgsDict
                ]
            ]
        ] = ...,
        retention_config: Optional[
            pulumi.Input[
                Union[LiteTopicRetentionConfigArgs, LiteTopicRetentionConfigArgsDict]
            ]
        ] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[LiteTopicArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        partition_config: Optional[
            pulumi.Input[
                Union[LiteTopicPartitionConfigArgs, LiteTopicPartitionConfigArgsDict]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_config: Optional[
            pulumi.Input[
                Union[
                    LiteTopicReservationConfigArgs, LiteTopicReservationConfigArgsDict
                ]
            ]
        ] = ...,
        retention_config: Optional[
            pulumi.Input[
                Union[LiteTopicRetentionConfigArgs, LiteTopicRetentionConfigArgsDict]
            ]
        ] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LiteTopic: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partitionConfig")
    def partition_config(
        self,
    ) -> pulumi.Output[Optional[outputs.LiteTopicPartitionConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="reservationConfig")
    def reservation_config(
        self,
    ) -> pulumi.Output[Optional[outputs.LiteTopicReservationConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="retentionConfig")
    def retention_config(
        self,
    ) -> pulumi.Output[Optional[outputs.LiteTopicRetentionConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[Optional[_builtins.str]]: ...
