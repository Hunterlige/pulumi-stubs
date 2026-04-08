import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EventDataStoreAdvancedEventSelectorArgs",
    "EventDataStoreAdvancedEventSelectorArgsDict",
    ...,
    ...,
    "TrailAdvancedEventSelectorArgs",
    "TrailAdvancedEventSelectorArgsDict",
    "TrailAdvancedEventSelectorFieldSelectorArgs",
    "TrailAdvancedEventSelectorFieldSelectorArgsDict",
    "TrailEventSelectorArgs",
    "TrailEventSelectorArgsDict",
    "TrailEventSelectorDataResourceArgs",
    "TrailEventSelectorDataResourceArgsDict",
    "TrailInsightSelectorArgs",
    "TrailInsightSelectorArgsDict",
]

class EventDataStoreAdvancedEventSelectorArgsDict(TypedDict):
    field_selectors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[EventDataStoreAdvancedEventSelectorFieldSelectorArgsDict]
            ]
        ]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventDataStoreAdvancedEventSelectorArgs:
    def __init__(
        __self__,
        *,
        field_selectors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[EventDataStoreAdvancedEventSelectorFieldSelectorArgs]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldSelectors")
    def field_selectors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[EventDataStoreAdvancedEventSelectorFieldSelectorArgs]]
        ]
    ]: ...
    @field_selectors.setter
    def field_selectors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[EventDataStoreAdvancedEventSelectorFieldSelectorArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventDataStoreAdvancedEventSelectorFieldSelectorArgsDict(TypedDict):
    ends_withs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    equals: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    field: NotRequired[pulumi.Input[_builtins.str]]
    not_ends_withs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    not_equals: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    not_starts_withs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    starts_withs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class EventDataStoreAdvancedEventSelectorFieldSelectorArgs:
    def __init__(
        __self__,
        *,
        ends_withs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        equals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        field: Optional[pulumi.Input[_builtins.str]] = ...,
        not_ends_withs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        not_equals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        not_starts_withs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        starts_withs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endsWiths")
    def ends_withs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ends_withs.setter
    def ends_withs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def equals(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @equals.setter
    def equals(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notEndsWiths")
    def not_ends_withs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @not_ends_withs.setter
    def not_ends_withs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notEquals")
    def not_equals(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @not_equals.setter
    def not_equals(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notStartsWiths")
    def not_starts_withs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @not_starts_withs.setter
    def not_starts_withs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startsWiths")
    def starts_withs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @starts_withs.setter
    def starts_withs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class TrailAdvancedEventSelectorArgsDict(TypedDict):
    field_selectors: pulumi.Input[
        Sequence[pulumi.Input[TrailAdvancedEventSelectorFieldSelectorArgsDict]]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TrailAdvancedEventSelectorArgs:
    def __init__(
        __self__,
        *,
        field_selectors: pulumi.Input[
            Sequence[pulumi.Input[TrailAdvancedEventSelectorFieldSelectorArgs]]
        ],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldSelectors")
    def field_selectors(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[TrailAdvancedEventSelectorFieldSelectorArgs]]
    ]: ...
    @field_selectors.setter
    def field_selectors(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[TrailAdvancedEventSelectorFieldSelectorArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TrailAdvancedEventSelectorFieldSelectorArgsDict(TypedDict):
    field: pulumi.Input[_builtins.str]
    ends_withs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    equals: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    not_ends_withs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    not_equals: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    not_starts_withs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    starts_withs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class TrailAdvancedEventSelectorFieldSelectorArgs:
    def __init__(
        __self__,
        *,
        field: pulumi.Input[_builtins.str],
        ends_withs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        equals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        not_ends_withs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        not_equals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        not_starts_withs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        starts_withs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> pulumi.Input[_builtins.str]: ...
    @field.setter
    def field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endsWiths")
    def ends_withs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ends_withs.setter
    def ends_withs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def equals(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @equals.setter
    def equals(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notEndsWiths")
    def not_ends_withs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @not_ends_withs.setter
    def not_ends_withs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notEquals")
    def not_equals(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @not_equals.setter
    def not_equals(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notStartsWiths")
    def not_starts_withs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @not_starts_withs.setter
    def not_starts_withs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startsWiths")
    def starts_withs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @starts_withs.setter
    def starts_withs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class TrailEventSelectorArgsDict(TypedDict):
    data_resources: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TrailEventSelectorDataResourceArgsDict]]]
    ]
    exclude_management_event_sources: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    include_management_events: NotRequired[pulumi.Input[_builtins.bool]]
    read_write_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TrailEventSelectorArgs:
    def __init__(
        __self__,
        *,
        data_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrailEventSelectorDataResourceArgs]]]
        ] = ...,
        exclude_management_event_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        include_management_events: Optional[pulumi.Input[_builtins.bool]] = ...,
        read_write_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataResources")
    def data_resources(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TrailEventSelectorDataResourceArgs]]]
    ]: ...
    @data_resources.setter
    def data_resources(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrailEventSelectorDataResourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeManagementEventSources")
    def exclude_management_event_sources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_management_event_sources.setter
    def exclude_management_event_sources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeManagementEvents")
    def include_management_events(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_management_events.setter
    def include_management_events(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="readWriteType")
    def read_write_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @read_write_type.setter
    def read_write_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TrailEventSelectorDataResourceArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class TrailEventSelectorDataResourceArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class TrailInsightSelectorArgsDict(TypedDict):
    insight_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class TrailInsightSelectorArgs:
    def __init__(__self__, *, insight_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="insightType")
    def insight_type(self) -> pulumi.Input[_builtins.str]: ...
    @insight_type.setter
    def insight_type(self, value: pulumi.Input[_builtins.str]): ...
