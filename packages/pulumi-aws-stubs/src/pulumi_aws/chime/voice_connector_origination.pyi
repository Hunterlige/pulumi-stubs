import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VoiceConnectorOriginationArgs", "VoiceConnectorOrigination"]

@pulumi.input_type
class VoiceConnectorOriginationArgs:
    def __init__(
        __self__,
        *,
        routes: pulumi.Input[
            Sequence[pulumi.Input[VoiceConnectorOriginationRouteArgs]]
        ],
        voice_connector_id: pulumi.Input[_builtins.str],
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def routes(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[VoiceConnectorOriginationRouteArgs]]]: ...
    @routes.setter
    def routes(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[VoiceConnectorOriginationRouteArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="voiceConnectorId")
    def voice_connector_id(self) -> pulumi.Input[_builtins.str]: ...
    @voice_connector_id.setter
    def voice_connector_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _VoiceConnectorOriginationState:
    def __init__(
        __self__,
        *,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routes: Optional[
            pulumi.Input[Sequence[pulumi.Input[VoiceConnectorOriginationRouteArgs]]]
        ] = ...,
        voice_connector_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def routes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VoiceConnectorOriginationRouteArgs]]]
    ]: ...
    @routes.setter
    def routes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VoiceConnectorOriginationRouteArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="voiceConnectorId")
    def voice_connector_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @voice_connector_id.setter
    def voice_connector_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class VoiceConnectorOrigination(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            VoiceConnectorOriginationRouteArgs,
                            VoiceConnectorOriginationRouteArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        voice_connector_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VoiceConnectorOriginationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            VoiceConnectorOriginationRouteArgs,
                            VoiceConnectorOriginationRouteArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        voice_connector_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> VoiceConnectorOrigination: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def routes(
        self,
    ) -> pulumi.Output[Sequence[outputs.VoiceConnectorOriginationRoute]]: ...
    @_builtins.property
    @pulumi.getter(name="voiceConnectorId")
    def voice_connector_id(self) -> pulumi.Output[_builtins.str]: ...
