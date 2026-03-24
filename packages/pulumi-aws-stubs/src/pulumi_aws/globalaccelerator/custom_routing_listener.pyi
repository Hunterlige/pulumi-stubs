import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CustomRoutingListenerArgs", "CustomRoutingListener"]

@pulumi.input_type
class CustomRoutingListenerArgs:
    def __init__(
        __self__,
        *,
        accelerator_arn: pulumi.Input[_builtins.str],
        port_ranges: pulumi.Input[
            Sequence[pulumi.Input[CustomRoutingListenerPortRangeArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorArn")
    def accelerator_arn(self) -> pulumi.Input[_builtins.str]: ...
    @accelerator_arn.setter
    def accelerator_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[CustomRoutingListenerPortRangeArgs]]]: ...
    @port_ranges.setter
    def port_ranges(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[CustomRoutingListenerPortRangeArgs]]],
    ): ...

@pulumi.input_type
class _CustomRoutingListenerState:
    def __init__(
        __self__,
        *,
        accelerator_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        port_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomRoutingListenerPortRangeArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorArn")
    def accelerator_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accelerator_arn.setter
    def accelerator_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CustomRoutingListenerPortRangeArgs]]]
    ]: ...
    @port_ranges.setter
    def port_ranges(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomRoutingListenerPortRangeArgs]]]
        ],
    ): ...

@pulumi.type_token(...)
class CustomRoutingListener(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        accelerator_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        port_ranges: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CustomRoutingListenerPortRangeArgs,
                            CustomRoutingListenerPortRangeArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CustomRoutingListenerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        accelerator_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        port_ranges: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CustomRoutingListenerPortRangeArgs,
                            CustomRoutingListenerPortRangeArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> CustomRoutingListener: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorArn")
    def accelerator_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(
        self,
    ) -> pulumi.Output[Sequence[outputs.CustomRoutingListenerPortRange]]: ...
