import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApplicationLayerAutomaticResponseArgs", "ApplicationLayerAutomaticResponse"]

@pulumi.input_type
class ApplicationLayerAutomaticResponseArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[_builtins.str],
        resource_arn: pulumi.Input[_builtins.str],
        timeouts: Optional[
            pulumi.Input[ApplicationLayerAutomaticResponseTimeoutsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]: ...
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]: ...
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[ApplicationLayerAutomaticResponseTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self,
        value: Optional[pulumi.Input[ApplicationLayerAutomaticResponseTimeoutsArgs]],
    ): ...

@pulumi.input_type
class _ApplicationLayerAutomaticResponseState:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[ApplicationLayerAutomaticResponseTimeoutsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[ApplicationLayerAutomaticResponseTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self,
        value: Optional[pulumi.Input[ApplicationLayerAutomaticResponseTimeoutsArgs]],
    ): ...

@pulumi.type_token(...)
class ApplicationLayerAutomaticResponse(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    ApplicationLayerAutomaticResponseTimeoutsArgs,
                    ApplicationLayerAutomaticResponseTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApplicationLayerAutomaticResponseArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    ApplicationLayerAutomaticResponseTimeoutsArgs,
                    ApplicationLayerAutomaticResponseTimeoutsArgsDict,
                ]
            ]
        ] = ...,
    ) -> ApplicationLayerAutomaticResponse: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.ApplicationLayerAutomaticResponseTimeouts]]: ...
