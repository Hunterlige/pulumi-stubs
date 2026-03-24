import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RealtimeLogConfigArgs", "RealtimeLogConfig"]

@pulumi.input_type
class RealtimeLogConfigArgs:
    def __init__(
        __self__,
        *,
        endpoint: pulumi.Input[RealtimeLogConfigEndpointArgs],
        fields: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        sampling_rate: pulumi.Input[_builtins.int],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[RealtimeLogConfigEndpointArgs]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[RealtimeLogConfigEndpointArgs]): ...
    @_builtins.property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> pulumi.Input[_builtins.int]: ...
    @sampling_rate.setter
    def sampling_rate(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _RealtimeLogConfigState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[RealtimeLogConfigEndpointArgs]] = ...,
        fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        sampling_rate: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[RealtimeLogConfigEndpointArgs]]: ...
    @endpoint.setter
    def endpoint(
        self, value: Optional[pulumi.Input[RealtimeLogConfigEndpointArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @fields.setter
    def fields(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @sampling_rate.setter
    def sampling_rate(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token("aws:cloudfront/realtimeLogConfig:RealtimeLogConfig")
class RealtimeLogConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        endpoint: Optional[
            pulumi.Input[
                Union[RealtimeLogConfigEndpointArgs, RealtimeLogConfigEndpointArgsDict]
            ]
        ] = ...,
        fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        sampling_rate: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RealtimeLogConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[
            pulumi.Input[
                Union[RealtimeLogConfigEndpointArgs, RealtimeLogConfigEndpointArgsDict]
            ]
        ] = ...,
        fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        sampling_rate: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> RealtimeLogConfig: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[outputs.RealtimeLogConfigEndpoint]: ...
    @_builtins.property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> pulumi.Output[_builtins.int]: ...
