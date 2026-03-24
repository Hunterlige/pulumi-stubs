import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "WorkloadComplianceStatus",
    "WorkloadEkmProvisioningResponse",
    "WorkloadKmsSettings",
    "WorkloadPartnerPermissions",
    "WorkloadResource",
    "WorkloadResourceSetting",
    "WorkloadSaaEnrollmentResponse",
    "WorkloadWorkloadOptions",
]

@pulumi.output_type
class WorkloadComplianceStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        acknowledged_violation_counts: Optional[Sequence[_builtins.int]] = ...,
        active_violation_counts: Optional[Sequence[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acknowledgedViolationCounts")
    def acknowledged_violation_counts(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="activeViolationCounts")
    def active_violation_counts(self) -> Optional[Sequence[_builtins.int]]: ...

@pulumi.output_type
class WorkloadEkmProvisioningResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ekm_provisioning_error_domain: Optional[_builtins.str] = ...,
        ekm_provisioning_error_mapping: Optional[_builtins.str] = ...,
        ekm_provisioning_state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ekmProvisioningErrorDomain")
    def ekm_provisioning_error_domain(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ekmProvisioningErrorMapping")
    def ekm_provisioning_error_mapping(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ekmProvisioningState")
    def ekm_provisioning_state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkloadKmsSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, next_rotation_time: _builtins.str, rotation_period: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextRotationTime")
    def next_rotation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> _builtins.str: ...

@pulumi.output_type
class WorkloadPartnerPermissions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        assured_workloads_monitoring: Optional[_builtins.bool] = ...,
        data_logs_viewer: Optional[_builtins.bool] = ...,
        service_access_approver: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assuredWorkloadsMonitoring")
    def assured_workloads_monitoring(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dataLogsViewer")
    def data_logs_viewer(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccessApprover")
    def service_access_approver(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class WorkloadResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_id: Optional[_builtins.int] = ...,
        resource_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkloadResourceSetting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        display_name: Optional[_builtins.str] = ...,
        resource_id: Optional[_builtins.str] = ...,
        resource_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkloadSaaEnrollmentResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        setup_errors: Optional[Sequence[_builtins.str]] = ...,
        setup_status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="setupErrors")
    def setup_errors(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="setupStatus")
    def setup_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkloadWorkloadOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, kaj_enrollment_type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kajEnrollmentType")
    def kaj_enrollment_type(self) -> Optional[_builtins.str]: ...
