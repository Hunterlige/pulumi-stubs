import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OrganizationsFeaturesArgs", "OrganizationsFeatures"]

@pulumi.input_type
class OrganizationsFeaturesArgs:
    def __init__(
        __self__,
        *,
        enabled_features: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledFeatures")
    def enabled_features(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @enabled_features.setter
    def enabled_features(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

@pulumi.input_type
class _OrganizationsFeaturesState:
    def __init__(
        __self__,
        *,
        enabled_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledFeatures")
    def enabled_features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enabled_features.setter
    def enabled_features(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class OrganizationsFeatures(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        enabled_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OrganizationsFeaturesArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        enabled_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> OrganizationsFeatures: ...
    @_builtins.property
    @pulumi.getter(name="enabledFeatures")
    def enabled_features(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
