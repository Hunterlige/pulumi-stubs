import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DataShareAuthorizationArgs", "DataShareAuthorization"]

@pulumi.input_type
class DataShareAuthorizationArgs:
    def __init__(
        __self__,
        *,
        consumer_identifier: pulumi.Input[_builtins.str],
        data_share_arn: pulumi.Input[_builtins.str],
        allow_writes: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerIdentifier")
    def consumer_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @consumer_identifier.setter
    def consumer_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataShareArn")
    def data_share_arn(self) -> pulumi.Input[_builtins.str]: ...
    @data_share_arn.setter
    def data_share_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowWrites")
    def allow_writes(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_writes.setter
    def allow_writes(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _DataShareAuthorizationState:
    def __init__(
        __self__,
        *,
        allow_writes: Optional[pulumi.Input[_builtins.bool]] = ...,
        consumer_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        data_share_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_by: Optional[pulumi.Input[_builtins.str]] = ...,
        producer_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowWrites")
    def allow_writes(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_writes.setter
    def allow_writes(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="consumerIdentifier")
    def consumer_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_identifier.setter
    def consumer_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataShareArn")
    def data_share_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_share_arn.setter
    def data_share_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_by.setter
    def managed_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="producerArn")
    def producer_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @producer_arn.setter
    def producer_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class DataShareAuthorization(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_writes: Optional[pulumi.Input[_builtins.bool]] = ...,
        consumer_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        data_share_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DataShareAuthorizationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_writes: Optional[pulumi.Input[_builtins.bool]] = ...,
        consumer_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        data_share_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_by: Optional[pulumi.Input[_builtins.str]] = ...,
        producer_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> DataShareAuthorization: ...
    @_builtins.property
    @pulumi.getter(name="allowWrites")
    def allow_writes(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="consumerIdentifier")
    def consumer_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataShareArn")
    def data_share_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="producerArn")
    def producer_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
