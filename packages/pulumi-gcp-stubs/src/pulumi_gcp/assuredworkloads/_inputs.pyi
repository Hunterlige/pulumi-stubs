import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "WorkloadComplianceStatusArgs",
    "WorkloadComplianceStatusArgsDict",
    "WorkloadEkmProvisioningResponseArgs",
    "WorkloadEkmProvisioningResponseArgsDict",
    "WorkloadKmsSettingsArgs",
    "WorkloadKmsSettingsArgsDict",
    "WorkloadPartnerPermissionsArgs",
    "WorkloadPartnerPermissionsArgsDict",
    "WorkloadResourceArgs",
    "WorkloadResourceArgsDict",
    "WorkloadResourceSettingArgs",
    "WorkloadResourceSettingArgsDict",
    "WorkloadSaaEnrollmentResponseArgs",
    "WorkloadSaaEnrollmentResponseArgsDict",
    "WorkloadWorkloadOptionsArgs",
    "WorkloadWorkloadOptionsArgsDict",
]

class WorkloadComplianceStatusArgsDict(TypedDict):
    acknowledged_violation_counts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ]
    active_violation_counts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ]

@pulumi.input_type
class WorkloadComplianceStatusArgs:
    def __init__(
        __self__,
        *,
        acknowledged_violation_counts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        active_violation_counts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acknowledgedViolationCounts")
    def acknowledged_violation_counts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @acknowledged_violation_counts.setter
    def acknowledged_violation_counts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="activeViolationCounts")
    def active_violation_counts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @active_violation_counts.setter
    def active_violation_counts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class WorkloadEkmProvisioningResponseArgsDict(TypedDict):
    ekm_provisioning_error_domain: NotRequired[pulumi.Input[_builtins.str]]
    ekm_provisioning_error_mapping: NotRequired[pulumi.Input[_builtins.str]]
    ekm_provisioning_state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkloadEkmProvisioningResponseArgs:
    def __init__(
        __self__,
        *,
        ekm_provisioning_error_domain: Optional[pulumi.Input[_builtins.str]] = ...,
        ekm_provisioning_error_mapping: Optional[pulumi.Input[_builtins.str]] = ...,
        ekm_provisioning_state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ekmProvisioningErrorDomain")
    def ekm_provisioning_error_domain(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ekm_provisioning_error_domain.setter
    def ekm_provisioning_error_domain(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ekmProvisioningErrorMapping")
    def ekm_provisioning_error_mapping(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ekm_provisioning_error_mapping.setter
    def ekm_provisioning_error_mapping(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ekmProvisioningState")
    def ekm_provisioning_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ekm_provisioning_state.setter
    def ekm_provisioning_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkloadKmsSettingsArgsDict(TypedDict):
    next_rotation_time: pulumi.Input[_builtins.str]
    rotation_period: pulumi.Input[_builtins.str]

@pulumi.input_type
class WorkloadKmsSettingsArgs:
    def __init__(
        __self__,
        *,
        next_rotation_time: pulumi.Input[_builtins.str],
        rotation_period: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextRotationTime")
    def next_rotation_time(self) -> pulumi.Input[_builtins.str]: ...
    @next_rotation_time.setter
    def next_rotation_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> pulumi.Input[_builtins.str]: ...
    @rotation_period.setter
    def rotation_period(self, value: pulumi.Input[_builtins.str]): ...

class WorkloadPartnerPermissionsArgsDict(TypedDict):
    assured_workloads_monitoring: NotRequired[pulumi.Input[_builtins.bool]]
    data_logs_viewer: NotRequired[pulumi.Input[_builtins.bool]]
    service_access_approver: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class WorkloadPartnerPermissionsArgs:
    def __init__(
        __self__,
        *,
        assured_workloads_monitoring: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_logs_viewer: Optional[pulumi.Input[_builtins.bool]] = ...,
        service_access_approver: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assuredWorkloadsMonitoring")
    def assured_workloads_monitoring(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @assured_workloads_monitoring.setter
    def assured_workloads_monitoring(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataLogsViewer")
    def data_logs_viewer(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @data_logs_viewer.setter
    def data_logs_viewer(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccessApprover")
    def service_access_approver(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @service_access_approver.setter
    def service_access_approver(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class WorkloadResourceArgsDict(TypedDict):
    resource_id: NotRequired[pulumi.Input[_builtins.int]]
    resource_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkloadResourceArgs:
    def __init__(
        __self__,
        *,
        resource_id: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkloadResourceSettingArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]
    resource_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkloadResourceSettingArgs:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkloadSaaEnrollmentResponseArgsDict(TypedDict):
    setup_errors: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    setup_status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkloadSaaEnrollmentResponseArgs:
    def __init__(
        __self__,
        *,
        setup_errors: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        setup_status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="setupErrors")
    def setup_errors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @setup_errors.setter
    def setup_errors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="setupStatus")
    def setup_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @setup_status.setter
    def setup_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkloadWorkloadOptionsArgsDict(TypedDict):
    kaj_enrollment_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkloadWorkloadOptionsArgs:
    def __init__(
        __self__, *, kaj_enrollment_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kajEnrollmentType")
    def kaj_enrollment_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kaj_enrollment_type.setter
    def kaj_enrollment_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
