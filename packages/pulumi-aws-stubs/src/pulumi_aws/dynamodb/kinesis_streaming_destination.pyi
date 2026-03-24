import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KinesisStreamingDestinationArgs", "KinesisStreamingDestination"]

@pulumi.input_type
class KinesisStreamingDestinationArgs:
    def __init__(
        __self__,
        *,
        stream_arn: pulumi.Input[_builtins.str],
        table_name: pulumi.Input[_builtins.str],
        approximate_creation_date_time_precision: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> pulumi.Input[_builtins.str]: ...
    @stream_arn.setter
    def stream_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="approximateCreationDateTimePrecision")
    def approximate_creation_date_time_precision(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @approximate_creation_date_time_precision.setter
    def approximate_creation_date_time_precision(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _KinesisStreamingDestinationState:
    def __init__(
        __self__,
        *,
        approximate_creation_date_time_precision: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approximateCreationDateTimePrecision")
    def approximate_creation_date_time_precision(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @approximate_creation_date_time_precision.setter
    def approximate_creation_date_time_precision(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream_arn.setter
    def stream_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class KinesisStreamingDestination(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        approximate_creation_date_time_precision: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: KinesisStreamingDestinationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        approximate_creation_date_time_precision: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> KinesisStreamingDestination: ...
    @_builtins.property
    @pulumi.getter(name="approximateCreationDateTimePrecision")
    def approximate_creation_date_time_precision(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[_builtins.str]: ...
