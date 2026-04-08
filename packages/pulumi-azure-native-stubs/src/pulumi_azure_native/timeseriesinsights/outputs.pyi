import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EnvironmentStateDetailsResponse",
    "EnvironmentStatusResponse",
    "Gen2StorageConfigurationOutputResponse",
    "IngressEnvironmentStatusResponse",
    "LocalTimestampResponse",
    "LocalTimestampResponseTimeZoneOffset",
    "ReferenceDataSetKeyPropertyResponse",
    "SkuResponse",
    "TimeSeriesIdPropertyResponse",
    "WarmStorageEnvironmentStatusResponse",
    "WarmStoreConfigurationPropertiesResponse",
]

@pulumi.output_type
class EnvironmentStateDetailsResponse(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnvironmentStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ingress: outputs.IngressEnvironmentStatusResponse,
        warm_storage: outputs.WarmStorageEnvironmentStatusResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> outputs.IngressEnvironmentStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="warmStorage")
    def warm_storage(self) -> outputs.WarmStorageEnvironmentStatusResponse: ...

@pulumi.output_type
class Gen2StorageConfigurationOutputResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, account_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> _builtins.str: ...

@pulumi.output_type
class IngressEnvironmentStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        state_details: outputs.EnvironmentStateDetailsResponse,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stateDetails")
    def state_details(self) -> outputs.EnvironmentStateDetailsResponse: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LocalTimestampResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        format: Optional[_builtins.str] = ...,
        time_zone_offset: Optional[outputs.LocalTimestampResponseTimeZoneOffset] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeZoneOffset")
    def time_zone_offset(
        self,
    ) -> Optional[outputs.LocalTimestampResponseTimeZoneOffset]: ...

@pulumi.output_type
class LocalTimestampResponseTimeZoneOffset(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, property_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ReferenceDataSetKeyPropertyResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SkuResponse(dict):
    def __init__(__self__, *, capacity: _builtins.int, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class TimeSeriesIdPropertyResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WarmStorageEnvironmentStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        current_count: Optional[_builtins.int] = ...,
        max_count: Optional[_builtins.int] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentCount")
    def current_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WarmStoreConfigurationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, data_retention: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataRetention")
    def data_retention(self) -> _builtins.str: ...
