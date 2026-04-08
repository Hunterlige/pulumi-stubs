import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EventImpactedResourceResponse",
    "KeyValueItemResponse",
    "SystemDataResponse",
]

@pulumi.output_type
class EventImpactedResourceResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        system_data: outputs.SystemDataResponse,
        target_region: _builtins.str,
        target_resource_id: _builtins.str,
        target_resource_type: _builtins.str,
        type: _builtins.str,
        info: Optional[Sequence[outputs.KeyValueItemResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="targetRegion")
    def target_region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceType")
    def target_resource_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def info(self) -> Optional[Sequence[outputs.KeyValueItemResponse]]: ...

@pulumi.output_type
class KeyValueItemResponse(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...
