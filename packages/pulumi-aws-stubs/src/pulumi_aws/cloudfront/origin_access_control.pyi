import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OriginAccessControlArgs", "OriginAccessControl"]

@pulumi.input_type
class OriginAccessControlArgs:
    def __init__(
        __self__,
        *,
        origin_access_control_origin_type: pulumi.Input[_builtins.str],
        signing_behavior: pulumi.Input[_builtins.str],
        signing_protocol: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="originAccessControlOriginType")
    def origin_access_control_origin_type(self) -> pulumi.Input[_builtins.str]: ...
    @origin_access_control_origin_type.setter
    def origin_access_control_origin_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="signingBehavior")
    def signing_behavior(self) -> pulumi.Input[_builtins.str]: ...
    @signing_behavior.setter
    def signing_behavior(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="signingProtocol")
    def signing_protocol(self) -> pulumi.Input[_builtins.str]: ...
    @signing_protocol.setter
    def signing_protocol(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _OriginAccessControlState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_access_control_origin_type: Optional[pulumi.Input[_builtins.str]] = ...,
        signing_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        signing_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="originAccessControlOriginType")
    def origin_access_control_origin_type(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @origin_access_control_origin_type.setter
    def origin_access_control_origin_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="signingBehavior")
    def signing_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @signing_behavior.setter
    def signing_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="signingProtocol")
    def signing_protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @signing_protocol.setter
    def signing_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class OriginAccessControl(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_access_control_origin_type: Optional[pulumi.Input[_builtins.str]] = ...,
        signing_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        signing_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OriginAccessControlArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_access_control_origin_type: Optional[pulumi.Input[_builtins.str]] = ...,
        signing_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        signing_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> OriginAccessControl: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originAccessControlOriginType")
    def origin_access_control_origin_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="signingBehavior")
    def signing_behavior(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="signingProtocol")
    def signing_protocol(self) -> pulumi.Output[_builtins.str]: ...
