import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EventDataStoreAdvancedEventSelector",
    "EventDataStoreAdvancedEventSelectorFieldSelector",
    "TrailAdvancedEventSelector",
    "TrailAdvancedEventSelectorFieldSelector",
    "TrailEventSelector",
    "TrailEventSelectorDataResource",
    "TrailInsightSelector",
]

@pulumi.output_type
class EventDataStoreAdvancedEventSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        field_selectors: Optional[
            Sequence[outputs.EventDataStoreAdvancedEventSelectorFieldSelector]
        ] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldSelectors")
    def field_selectors(
        self,
    ) -> Optional[
        Sequence[outputs.EventDataStoreAdvancedEventSelectorFieldSelector]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventDataStoreAdvancedEventSelectorFieldSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ends_withs: Optional[Sequence[_builtins.str]] = ...,
        equals: Optional[Sequence[_builtins.str]] = ...,
        field: Optional[_builtins.str] = ...,
        not_ends_withs: Optional[Sequence[_builtins.str]] = ...,
        not_equals: Optional[Sequence[_builtins.str]] = ...,
        not_starts_withs: Optional[Sequence[_builtins.str]] = ...,
        starts_withs: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endsWiths")
    def ends_withs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def equals(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notEndsWiths")
    def not_ends_withs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="notEquals")
    def not_equals(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="notStartsWiths")
    def not_starts_withs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="startsWiths")
    def starts_withs(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class TrailAdvancedEventSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        field_selectors: Sequence[outputs.TrailAdvancedEventSelectorFieldSelector],
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldSelectors")
    def field_selectors(
        self,
    ) -> Sequence[outputs.TrailAdvancedEventSelectorFieldSelector]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TrailAdvancedEventSelectorFieldSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        field: _builtins.str,
        ends_withs: Optional[Sequence[_builtins.str]] = ...,
        equals: Optional[Sequence[_builtins.str]] = ...,
        not_ends_withs: Optional[Sequence[_builtins.str]] = ...,
        not_equals: Optional[Sequence[_builtins.str]] = ...,
        not_starts_withs: Optional[Sequence[_builtins.str]] = ...,
        starts_withs: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endsWiths")
    def ends_withs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def equals(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="notEndsWiths")
    def not_ends_withs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="notEquals")
    def not_equals(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="notStartsWiths")
    def not_starts_withs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="startsWiths")
    def starts_withs(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class TrailEventSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_resources: Optional[
            Sequence[outputs.TrailEventSelectorDataResource]
        ] = ...,
        exclude_management_event_sources: Optional[Sequence[_builtins.str]] = ...,
        include_management_events: Optional[_builtins.bool] = ...,
        read_write_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataResources")
    def data_resources(
        self,
    ) -> Optional[Sequence[outputs.TrailEventSelectorDataResource]]: ...
    @_builtins.property
    @pulumi.getter(name="excludeManagementEventSources")
    def exclude_management_event_sources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="includeManagementEvents")
    def include_management_events(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="readWriteType")
    def read_write_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TrailEventSelectorDataResource(dict):
    def __init__(
        __self__, *, type: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class TrailInsightSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, insight_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="insightType")
    def insight_type(self) -> _builtins.str: ...
