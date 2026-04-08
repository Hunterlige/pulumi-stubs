import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ErrorAdditionalInfoResponse",
    "ErrorDetailResponse",
    ...,
    "OffAzureDiscoverySourceResourcePropertiesResponse",
    "SystemDataResponse",
]

@pulumi.output_type
class ErrorAdditionalInfoResponse(dict):
    def __init__(__self__, *, info: Any, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def info(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ErrorDetailResponse(dict):
    def __init__(
        __self__,
        *,
        additional_info: Sequence[outputs.ErrorAdditionalInfoResponse],
        code: _builtins.str,
        details: Sequence[outputs.ErrorDetailResponse],
        message: _builtins.str,
        target: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence[outputs.ErrorAdditionalInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDetailResponse]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

@pulumi.output_type
class GetDependencyViewForAllMachinesResultPropertiesResponse(dict):
    def __init__(__self__, *, layout_file_sas_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="layoutFileSasUrl")
    def layout_file_sas_url(self) -> _builtins.str: ...

@pulumi.output_type
class OffAzureDiscoverySourceResourcePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        source_id: _builtins.str,
        source_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> _builtins.str: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
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
