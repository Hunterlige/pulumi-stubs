import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TrackerAssociationArgs", "TrackerAssociation"]

@pulumi.input_type
class TrackerAssociationArgs:
    def __init__(
        __self__,
        *,
        consumer_arn: pulumi.Input[_builtins.str],
        tracker_name: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerArn")
    def consumer_arn(self) -> pulumi.Input[_builtins.str]: ...
    @consumer_arn.setter
    def consumer_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trackerName")
    def tracker_name(self) -> pulumi.Input[_builtins.str]: ...
    @tracker_name.setter
    def tracker_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _TrackerAssociationState:
    def __init__(
        __self__,
        *,
        consumer_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tracker_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerArn")
    def consumer_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_arn.setter
    def consumer_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trackerName")
    def tracker_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tracker_name.setter
    def tracker_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:location/trackerAssociation:TrackerAssociation")
class TrackerAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        consumer_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tracker_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TrackerAssociationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        consumer_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tracker_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> TrackerAssociation: ...
    @_builtins.property
    @pulumi.getter(name="consumerArn")
    def consumer_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trackerName")
    def tracker_name(self) -> pulumi.Output[_builtins.str]: ...
