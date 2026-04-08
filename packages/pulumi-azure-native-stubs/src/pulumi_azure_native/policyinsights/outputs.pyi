import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AttestationEvidenceResponse",
    "ErrorDefinitionResponse",
    "RemediationDeploymentResponse",
    "RemediationDeploymentSummaryResponse",
    "RemediationFiltersResponse",
    "RemediationPropertiesResponseFailureThreshold",
    "SystemDataResponse",
    "TypedErrorInfoResponse",
]

@pulumi.output_type
class AttestationEvidenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        source_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceUri")
    def source_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ErrorDefinitionResponse(dict):
    def __init__(
        __self__,
        *,
        additional_info: Sequence[outputs.TypedErrorInfoResponse],
        code: _builtins.str,
        details: Sequence[outputs.ErrorDefinitionResponse],
        message: _builtins.str,
        target: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence[outputs.TypedErrorInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDefinitionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

@pulumi.output_type
class RemediationDeploymentResponse(dict):
    def __init__(
        __self__,
        *,
        created_on: _builtins.str,
        deployment_id: _builtins.str,
        error: outputs.ErrorDefinitionResponse,
        last_updated_on: _builtins.str,
        remediated_resource_id: _builtins.str,
        resource_location: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ErrorDefinitionResponse: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="remediatedResourceId")
    def remediated_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceLocation")
    def resource_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class RemediationDeploymentSummaryResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        failed_deployments: _builtins.int,
        successful_deployments: _builtins.int,
        total_deployments: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failedDeployments")
    def failed_deployments(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="successfulDeployments")
    def successful_deployments(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="totalDeployments")
    def total_deployments(self) -> _builtins.int: ...

@pulumi.output_type
class RemediationFiltersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        locations: Optional[Sequence[_builtins.str]] = ...,
        resource_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceIds")
    def resource_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RemediationPropertiesResponseFailureThreshold(dict):
    def __init__(__self__, *, percentage: Optional[_builtins.float] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[_builtins.float]: ...

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

@pulumi.output_type
class TypedErrorInfoResponse(dict):
    def __init__(__self__, *, info: Any, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def info(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
