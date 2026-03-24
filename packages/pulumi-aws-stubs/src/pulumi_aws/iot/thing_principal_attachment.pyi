import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ThingPrincipalAttachmentArgs", "ThingPrincipalAttachment"]

@pulumi.input_type
class ThingPrincipalAttachmentArgs:
    def __init__(
        __self__,
        *,
        principal: pulumi.Input[_builtins.str],
        thing: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        thing_principal_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]: ...
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def thing(self) -> pulumi.Input[_builtins.str]: ...
    @thing.setter
    def thing(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="thingPrincipalType")
    def thing_principal_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @thing_principal_type.setter
    def thing_principal_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ThingPrincipalAttachmentState:
    def __init__(
        __self__,
        *,
        principal: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        thing: Optional[pulumi.Input[_builtins.str]] = ...,
        thing_principal_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal.setter
    def principal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def thing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @thing.setter
    def thing(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="thingPrincipalType")
    def thing_principal_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @thing_principal_type.setter
    def thing_principal_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ThingPrincipalAttachment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        principal: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        thing: Optional[pulumi.Input[_builtins.str]] = ...,
        thing_principal_type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ThingPrincipalAttachmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        principal: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        thing: Optional[pulumi.Input[_builtins.str]] = ...,
        thing_principal_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ThingPrincipalAttachment: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def thing(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="thingPrincipalType")
    def thing_principal_type(self) -> pulumi.Output[_builtins.str]: ...
