import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LogDestinationPolicyArgs", "LogDestinationPolicy"]

@pulumi.input_type
class LogDestinationPolicyArgs:
    def __init__(
        __self__,
        *,
        access_policy: pulumi.Input[_builtins.str],
        destination_name: pulumi.Input[_builtins.str],
        force_update: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicy")
    def access_policy(self) -> pulumi.Input[_builtins.str]: ...
    @access_policy.setter
    def access_policy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destinationName")
    def destination_name(self) -> pulumi.Input[_builtins.str]: ...
    @destination_name.setter
    def destination_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="forceUpdate")
    def force_update(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_update.setter
    def force_update(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _LogDestinationPolicyState:
    def __init__(
        __self__,
        *,
        access_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_name: Optional[pulumi.Input[_builtins.str]] = ...,
        force_update: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicy")
    def access_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_policy.setter
    def access_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationName")
    def destination_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_name.setter
    def destination_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceUpdate")
    def force_update(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_update.setter
    def force_update(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class LogDestinationPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_name: Optional[pulumi.Input[_builtins.str]] = ...,
        force_update: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LogDestinationPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_name: Optional[pulumi.Input[_builtins.str]] = ...,
        force_update: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LogDestinationPolicy: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicy")
    def access_policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationName")
    def destination_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="forceUpdate")
    def force_update(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
