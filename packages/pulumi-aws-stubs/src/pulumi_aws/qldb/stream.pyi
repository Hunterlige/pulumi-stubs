import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["StreamArgs", "Stream"]

@pulumi.input_type
class StreamArgs:
    def __init__(
        __self__,
        *,
        inclusive_start_time: pulumi.Input[_builtins.str],
        kinesis_configuration: pulumi.Input[StreamKinesisConfigurationArgs],
        ledger_name: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        stream_name: pulumi.Input[_builtins.str],
        exclusive_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inclusiveStartTime")
    def inclusive_start_time(self) -> pulumi.Input[_builtins.str]: ...
    @inclusive_start_time.setter
    def inclusive_start_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kinesisConfiguration")
    def kinesis_configuration(self) -> pulumi.Input[StreamKinesisConfigurationArgs]: ...
    @kinesis_configuration.setter
    def kinesis_configuration(
        self, value: pulumi.Input[StreamKinesisConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ledgerName")
    def ledger_name(self) -> pulumi.Input[_builtins.str]: ...
    @ledger_name.setter
    def ledger_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> pulumi.Input[_builtins.str]: ...
    @stream_name.setter
    def stream_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="exclusiveEndTime")
    def exclusive_end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exclusive_end_time.setter
    def exclusive_end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class _StreamState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        exclusive_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        inclusive_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        kinesis_configuration: Optional[
            pulumi.Input[StreamKinesisConfigurationArgs]
        ] = ...,
        ledger_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_name: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="exclusiveEndTime")
    def exclusive_end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exclusive_end_time.setter
    def exclusive_end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inclusiveStartTime")
    def inclusive_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inclusive_start_time.setter
    def inclusive_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kinesisConfiguration")
    def kinesis_configuration(
        self,
    ) -> Optional[pulumi.Input[StreamKinesisConfigurationArgs]]: ...
    @kinesis_configuration.setter
    def kinesis_configuration(
        self, value: Optional[pulumi.Input[StreamKinesisConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ledgerName")
    def ledger_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ledger_name.setter
    def ledger_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream_name.setter
    def stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token("aws:qldb/stream:Stream")
class Stream(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        exclusive_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        inclusive_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        kinesis_configuration: Optional[
            pulumi.Input[
                Union[
                    StreamKinesisConfigurationArgs, StreamKinesisConfigurationArgsDict
                ]
            ]
        ] = ...,
        ledger_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: StreamArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        exclusive_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        inclusive_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        kinesis_configuration: Optional[
            pulumi.Input[
                Union[
                    StreamKinesisConfigurationArgs, StreamKinesisConfigurationArgsDict
                ]
            ]
        ] = ...,
        ledger_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Stream: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exclusiveEndTime")
    def exclusive_end_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inclusiveStartTime")
    def inclusive_start_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisConfiguration")
    def kinesis_configuration(
        self,
    ) -> pulumi.Output[outputs.StreamKinesisConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="ledgerName")
    def ledger_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
