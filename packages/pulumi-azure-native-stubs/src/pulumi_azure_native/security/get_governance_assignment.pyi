import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGovernanceAssignmentResult",
    "AwaitableGetGovernanceAssignmentResult",
    "get_governance_assignment",
    "get_governance_assignment_output",
]

@pulumi.output_type
class GetGovernanceAssignmentResult:
    def __init__(
        __self__,
        additional_data=...,
        azure_api_version=...,
        governance_email_notification=...,
        id=...,
        is_grace_period=...,
        name=...,
        owner=...,
        remediation_due_date=...,
        remediation_eta=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalData")
    def additional_data(
        self,
    ) -> Optional[outputs.GovernanceAssignmentAdditionalDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="governanceEmailNotification")
    def governance_email_notification(
        self,
    ) -> Optional[outputs.GovernanceEmailNotificationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isGracePeriod")
    def is_grace_period(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="remediationDueDate")
    def remediation_due_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="remediationEta")
    def remediation_eta(self) -> Optional[outputs.RemediationEtaResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetGovernanceAssignmentResult(GetGovernanceAssignmentResult):
    def __await__(self): ...

def get_governance_assignment(
    assessment_name: Optional[_builtins.str] = ...,
    assignment_key: Optional[_builtins.str] = ...,
    scope: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGovernanceAssignmentResult: ...
def get_governance_assignment_output(
    assessment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    assignment_key: Optional[pulumi.Input[_builtins.str]] = ...,
    scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGovernanceAssignmentResult]: ...
