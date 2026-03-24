import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KeyArgs", "Key"]

@pulumi.input_type
class KeyArgs:
    def __init__(
        __self__,
        *,
        exportable: pulumi.Input[_builtins.bool],
        deletion_window_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[KeyKeyAttributeArgs]]]
        ] = ...,
        key_check_value_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[KeyTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exportable(self) -> pulumi.Input[_builtins.bool]: ...
    @exportable.setter
    def exportable(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="deletionWindowInDays")
    def deletion_window_in_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @deletion_window_in_days.setter
    def deletion_window_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyAttributes")
    def key_attributes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[KeyKeyAttributeArgs]]]]: ...
    @key_attributes.setter
    def key_attributes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[KeyKeyAttributeArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyCheckValueAlgorithm")
    def key_check_value_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_check_value_algorithm.setter
    def key_check_value_algorithm(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[KeyTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[KeyTimeoutsArgs]]): ...

@pulumi.input_type
class _KeyState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_window_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        exportable: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[KeyKeyAttributeArgs]]]
        ] = ...,
        key_check_value: Optional[pulumi.Input[_builtins.str]] = ...,
        key_check_value_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        key_origin: Optional[pulumi.Input[_builtins.str]] = ...,
        key_state: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[KeyTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionWindowInDays")
    def deletion_window_in_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @deletion_window_in_days.setter
    def deletion_window_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def exportable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @exportable.setter
    def exportable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyAttributes")
    def key_attributes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[KeyKeyAttributeArgs]]]]: ...
    @key_attributes.setter
    def key_attributes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[KeyKeyAttributeArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyCheckValue")
    def key_check_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_check_value.setter
    def key_check_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyCheckValueAlgorithm")
    def key_check_value_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_check_value_algorithm.setter
    def key_check_value_algorithm(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyOrigin")
    def key_origin(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_origin.setter
    def key_origin(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyState")
    def key_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_state.setter
    def key_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[KeyTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[KeyTimeoutsArgs]]): ...

@pulumi.type_token("aws:paymentcryptography/key:Key")
class Key(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        deletion_window_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        exportable: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_attributes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[KeyKeyAttributeArgs, KeyKeyAttributeArgsDict]]
                ]
            ]
        ] = ...,
        key_check_value_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[KeyTimeoutsArgs, KeyTimeoutsArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: KeyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_window_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        exportable: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_attributes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[KeyKeyAttributeArgs, KeyKeyAttributeArgsDict]]
                ]
            ]
        ] = ...,
        key_check_value: Optional[pulumi.Input[_builtins.str]] = ...,
        key_check_value_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        key_origin: Optional[pulumi.Input[_builtins.str]] = ...,
        key_state: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[KeyTimeoutsArgs, KeyTimeoutsArgsDict]]
        ] = ...,
    ) -> Key: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionWindowInDays")
    def deletion_window_in_days(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def exportable(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="keyAttributes")
    def key_attributes(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.KeyKeyAttribute]]]: ...
    @_builtins.property
    @pulumi.getter(name="keyCheckValue")
    def key_check_value(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyCheckValueAlgorithm")
    def key_check_value_algorithm(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyOrigin")
    def key_origin(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyState")
    def key_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.KeyTimeouts]]: ...
