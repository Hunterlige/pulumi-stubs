import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccountSuppressionAttributesArgs", "AccountSuppressionAttributes"]

@pulumi.input_type
class AccountSuppressionAttributesArgs:
    def __init__(
        __self__,
        *,
        suppressed_reasons: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="suppressedReasons")
    def suppressed_reasons(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @suppressed_reasons.setter
    def suppressed_reasons(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AccountSuppressionAttributesState:
    def __init__(
        __self__,
        *,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        suppressed_reasons: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="suppressedReasons")
    def suppressed_reasons(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @suppressed_reasons.setter
    def suppressed_reasons(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class AccountSuppressionAttributes(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        suppressed_reasons: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AccountSuppressionAttributesArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        suppressed_reasons: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> AccountSuppressionAttributes: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="suppressedReasons")
    def suppressed_reasons(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
