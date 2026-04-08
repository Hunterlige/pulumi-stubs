import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AssignmentInfoResponse",
    "AssignmentReportResourceComplianceReasonResponse",
    "AssignmentReportResourceResponse",
    "AssignmentReportResponse",
    "ConfigurationInfoResponse",
    "ConfigurationParameterResponse",
    "ConfigurationSettingResponse",
    "GuestConfigurationAssignmentPropertiesResponse",
    "GuestConfigurationNavigationResponse",
    "SystemDataResponse",
    "VMInfoResponse",
    "VMSSVMInfoResponse",
]

@pulumi.output_type
class AssignmentInfoResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        configuration: Optional[outputs.ConfigurationInfoResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[outputs.ConfigurationInfoResponse]: ...

@pulumi.output_type
class AssignmentReportResourceComplianceReasonResponse(dict):
    def __init__(__self__, *, code: _builtins.str, phrase: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def phrase(self) -> _builtins.str: ...

@pulumi.output_type
class AssignmentReportResourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compliance_status: _builtins.str,
        properties: Any,
        resource_id: _builtins.str,
        reasons: Optional[
            Sequence[outputs.AssignmentReportResourceComplianceReasonResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="complianceStatus")
    def compliance_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def reasons(
        self,
    ) -> Optional[
        Sequence[outputs.AssignmentReportResourceComplianceReasonResponse]
    ]: ...

@pulumi.output_type
class AssignmentReportResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compliance_status: _builtins.str,
        end_time: _builtins.str,
        id: _builtins.str,
        operation_type: _builtins.str,
        report_id: _builtins.str,
        start_time: _builtins.str,
        assignment: Optional[outputs.AssignmentInfoResponse] = ...,
        resources: Optional[Sequence[outputs.AssignmentReportResourceResponse]] = ...,
        vm: Optional[outputs.VMInfoResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="complianceStatus")
    def compliance_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reportId")
    def report_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def assignment(self) -> Optional[outputs.AssignmentInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[Sequence[outputs.AssignmentReportResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def vm(self) -> Optional[outputs.VMInfoResponse]: ...

@pulumi.output_type
class ConfigurationInfoResponse(dict):
    def __init__(__self__, *, name: _builtins.str, version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class ConfigurationParameterResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConfigurationSettingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_after_reboot: _builtins.str,
        allow_module_overwrite: _builtins.bool,
        configuration_mode: _builtins.str,
        configuration_mode_frequency_mins: Optional[_builtins.float] = ...,
        reboot_if_needed: _builtins.bool,
        refresh_frequency_mins: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionAfterReboot")
    def action_after_reboot(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowModuleOverwrite")
    def allow_module_overwrite(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="configurationMode")
    def configuration_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="configurationModeFrequencyMins")
    def configuration_mode_frequency_mins(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="rebootIfNeeded")
    def reboot_if_needed(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="refreshFrequencyMins")
    def refresh_frequency_mins(self) -> _builtins.float: ...

@pulumi.output_type
class GuestConfigurationAssignmentPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        assignment_hash: _builtins.str,
        compliance_status: _builtins.str,
        last_compliance_status_checked: _builtins.str,
        latest_report_id: _builtins.str,
        parameter_hash: _builtins.str,
        provisioning_state: _builtins.str,
        resource_type: _builtins.str,
        target_resource_id: _builtins.str,
        context: Optional[_builtins.str] = ...,
        guest_configuration: Optional[
            outputs.GuestConfigurationNavigationResponse
        ] = ...,
        latest_assignment_report: Optional[outputs.AssignmentReportResponse] = ...,
        vmss_vm_list: Optional[Sequence[outputs.VMSSVMInfoResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assignmentHash")
    def assignment_hash(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="complianceStatus")
    def compliance_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastComplianceStatusChecked")
    def last_compliance_status_checked(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="latestReportId")
    def latest_report_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterHash")
    def parameter_hash(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="guestConfiguration")
    def guest_configuration(
        self,
    ) -> Optional[outputs.GuestConfigurationNavigationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="latestAssignmentReport")
    def latest_assignment_report(
        self,
    ) -> Optional[outputs.AssignmentReportResponse]: ...
    @_builtins.property
    @pulumi.getter(name="vmssVMList")
    def vmss_vm_list(self) -> Optional[Sequence[outputs.VMSSVMInfoResponse]]: ...

@pulumi.output_type
class GuestConfigurationNavigationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        assignment_source: _builtins.str,
        configuration_setting: outputs.ConfigurationSettingResponse,
        content_type: _builtins.str,
        assignment_type: Optional[_builtins.str] = ...,
        configuration_parameter: Optional[
            Sequence[outputs.ConfigurationParameterResponse]
        ] = ...,
        configuration_protected_parameter: Optional[
            Sequence[outputs.ConfigurationParameterResponse]
        ] = ...,
        content_hash: Optional[_builtins.str] = ...,
        content_managed_identity: Optional[_builtins.str] = ...,
        content_uri: Optional[_builtins.str] = ...,
        kind: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assignmentSource")
    def assignment_source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="configurationSetting")
    def configuration_setting(self) -> outputs.ConfigurationSettingResponse: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="assignmentType")
    def assignment_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="configurationParameter")
    def configuration_parameter(
        self,
    ) -> Optional[Sequence[outputs.ConfigurationParameterResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="configurationProtectedParameter")
    def configuration_protected_parameter(
        self,
    ) -> Optional[Sequence[outputs.ConfigurationParameterResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="contentHash")
    def content_hash(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentManagedIdentity")
    def content_managed_identity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentUri")
    def content_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

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
class VMInfoResponse(dict):
    def __init__(__self__, *, id: _builtins.str, uuid: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> _builtins.str: ...

@pulumi.output_type
class VMSSVMInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compliance_status: _builtins.str,
        last_compliance_checked: _builtins.str,
        latest_report_id: _builtins.str,
        vm_id: _builtins.str,
        vm_resource_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="complianceStatus")
    def compliance_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastComplianceChecked")
    def last_compliance_checked(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="latestReportId")
    def latest_report_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vmResourceId")
    def vm_resource_id(self) -> _builtins.str: ...
