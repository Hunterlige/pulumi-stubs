import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ControlTowerControlArgs", "ControlTowerControl"]

@pulumi.input_type
class ControlTowerControlArgs:
    def __init__(
        __self__,
        *,
        control_identifier: pulumi.Input[_builtins.str],
        target_identifier: pulumi.Input[_builtins.str],
        parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ControlTowerControlParameterArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlIdentifier")
    def control_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @control_identifier.setter
    def control_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetIdentifier")
    def target_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @target_identifier.setter
    def target_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ControlTowerControlParameterArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ControlTowerControlParameterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ControlTowerControlState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        control_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ControlTowerControlParameterArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        target_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="controlIdentifier")
    def control_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @control_identifier.setter
    def control_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ControlTowerControlParameterArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ControlTowerControlParameterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetIdentifier")
    def target_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_identifier.setter
    def target_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ControlTowerControl(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        control_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ControlTowerControlParameterArgs,
                            ControlTowerControlParameterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        target_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ControlTowerControlArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        control_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ControlTowerControlParameterArgs,
                            ControlTowerControlParameterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        target_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ControlTowerControl: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="controlIdentifier")
    def control_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ControlTowerControlParameter]]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetIdentifier")
    def target_identifier(self) -> pulumi.Output[_builtins.str]: ...
