import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EventSourcesConfigArgs", "EventSourcesConfig"]

@pulumi.input_type
class EventSourcesConfigArgs:
    def __init__(
        __self__,
        *,
        event_sources: pulumi.Input[
            Sequence[pulumi.Input[EventSourcesConfigEventSourceArgs]]
        ],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventSources")
    def event_sources(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[EventSourcesConfigEventSourceArgs]]]: ...
    @event_sources.setter
    def event_sources(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[EventSourcesConfigEventSourceArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _EventSourcesConfigState:
    def __init__(
        __self__,
        *,
        event_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[EventSourcesConfigEventSourceArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventSources")
    def event_sources(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EventSourcesConfigEventSourceArgs]]]
    ]: ...
    @event_sources.setter
    def event_sources(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EventSourcesConfigEventSourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class EventSourcesConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        event_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EventSourcesConfigEventSourceArgs,
                            EventSourcesConfigEventSourceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EventSourcesConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        event_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EventSourcesConfigEventSourceArgs,
                            EventSourcesConfigEventSourceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> EventSourcesConfig: ...
    @_builtins.property
    @pulumi.getter(name="eventSources")
    def event_sources(
        self,
    ) -> pulumi.Output[Sequence[outputs.EventSourcesConfigEventSource]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
