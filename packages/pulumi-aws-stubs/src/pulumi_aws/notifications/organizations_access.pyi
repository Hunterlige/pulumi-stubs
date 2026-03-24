import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OrganizationsAccessArgs", "OrganizationsAccess"]

@pulumi.input_type
class OrganizationsAccessArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        timeouts: Optional[pulumi.Input[OrganizationsAccessTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[OrganizationsAccessTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[OrganizationsAccessTimeoutsArgs]]
    ): ...

@pulumi.input_type
class _OrganizationsAccessState:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        timeouts: Optional[pulumi.Input[OrganizationsAccessTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[OrganizationsAccessTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[OrganizationsAccessTimeoutsArgs]]
    ): ...

@pulumi.type_token(...)
class OrganizationsAccess(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    OrganizationsAccessTimeoutsArgs, OrganizationsAccessTimeoutsArgsDict
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OrganizationsAccessArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    OrganizationsAccessTimeoutsArgs, OrganizationsAccessTimeoutsArgsDict
                ]
            ]
        ] = ...,
    ) -> OrganizationsAccess: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.OrganizationsAccessTimeouts]]: ...
