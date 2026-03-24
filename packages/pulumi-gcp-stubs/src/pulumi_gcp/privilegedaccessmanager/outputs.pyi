import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "SettingsEmailNotificationSettings",
    ...,
    ...,
    ...,
    ...,
    ...,
    "SettingsServiceAccountApproverSettings",
    "EntitlementAdditionalNotificationTargets",
    "EntitlementApprovalWorkflow",
    "EntitlementApprovalWorkflowManualApprovals",
    "EntitlementApprovalWorkflowManualApprovalsStep",
    ...,
    "EntitlementEligibleUser",
    "EntitlementPrivilegedAccess",
    "EntitlementPrivilegedAccessGcpIamAccess",
    "EntitlementPrivilegedAccessGcpIamAccessRoleBinding",
    "EntitlementRequesterJustificationConfig",
    ...,
    ...,
    "GetEntitlementAdditionalNotificationTargetResult",
    "GetEntitlementApprovalWorkflowResult",
    "GetEntitlementApprovalWorkflowManualApprovalResult",
    ...,
    ...,
    "GetEntitlementEligibleUserResult",
    "GetEntitlementPrivilegedAccessResult",
    "GetEntitlementPrivilegedAccessGcpIamAccessResult",
    ...,
    "GetEntitlementRequesterJustificationConfigResult",
    ...,
    ...,
]

@pulumi.output_type
class SettingsEmailNotificationSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_notification_behavior: Optional[
            outputs.SettingsEmailNotificationSettingsCustomNotificationBehavior
        ] = ...,
        disable_all_notifications: Optional[
            outputs.SettingsEmailNotificationSettingsDisableAllNotifications
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customNotificationBehavior")
    def custom_notification_behavior(
        self,
    ) -> Optional[
        outputs.SettingsEmailNotificationSettingsCustomNotificationBehavior
    ]: ...
    @_builtins.property
    @pulumi.getter(name="disableAllNotifications")
    def disable_all_notifications(
        self,
    ) -> Optional[outputs.SettingsEmailNotificationSettingsDisableAllNotifications]: ...

@pulumi.output_type
class SettingsEmailNotificationSettingsCustomNotificationBehavior(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        admin_notifications: Optional[
            outputs.SettingsEmailNotificationSettingsCustomNotificationBehaviorAdminNotifications
        ] = ...,
        approver_notifications: Optional[
            outputs.SettingsEmailNotificationSettingsCustomNotificationBehaviorApproverNotifications
        ] = ...,
        requester_notifications: Optional[
            outputs.SettingsEmailNotificationSettingsCustomNotificationBehaviorRequesterNotifications
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminNotifications")
    def admin_notifications(
        self,
    ) -> Optional[
        outputs.SettingsEmailNotificationSettingsCustomNotificationBehaviorAdminNotifications
    ]: ...
    @_builtins.property
    @pulumi.getter(name="approverNotifications")
    def approver_notifications(
        self,
    ) -> Optional[
        outputs.SettingsEmailNotificationSettingsCustomNotificationBehaviorApproverNotifications
    ]: ...
    @_builtins.property
    @pulumi.getter(name="requesterNotifications")
    def requester_notifications(
        self,
    ) -> Optional[
        outputs.SettingsEmailNotificationSettingsCustomNotificationBehaviorRequesterNotifications
    ]: ...

@pulumi.output_type
class SettingsEmailNotificationSettingsCustomNotificationBehaviorAdminNotifications(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        grant_activated: Optional[_builtins.str] = ...,
        grant_activation_failed: Optional[_builtins.str] = ...,
        grant_ended: Optional[_builtins.str] = ...,
        grant_externally_modified: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="grantActivated")
    def grant_activated(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="grantActivationFailed")
    def grant_activation_failed(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="grantEnded")
    def grant_ended(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="grantExternallyModified")
    def grant_externally_modified(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SettingsEmailNotificationSettingsCustomNotificationBehaviorApproverNotifications(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, pending_approval: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pendingApproval")
    def pending_approval(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SettingsEmailNotificationSettingsCustomNotificationBehaviorRequesterNotifications(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        entitlement_assigned: Optional[_builtins.str] = ...,
        grant_activated: Optional[_builtins.str] = ...,
        grant_activation_failed: Optional[_builtins.str] = ...,
        grant_denied: Optional[_builtins.str] = ...,
        grant_ended: Optional[_builtins.str] = ...,
        grant_expired: Optional[_builtins.str] = ...,
        grant_externally_modified: Optional[_builtins.str] = ...,
        grant_revoked: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entitlementAssigned")
    def entitlement_assigned(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="grantActivated")
    def grant_activated(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="grantActivationFailed")
    def grant_activation_failed(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="grantDenied")
    def grant_denied(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="grantEnded")
    def grant_ended(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="grantExpired")
    def grant_expired(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="grantExternallyModified")
    def grant_externally_modified(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="grantRevoked")
    def grant_revoked(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SettingsEmailNotificationSettingsDisableAllNotifications(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class SettingsServiceAccountApproverSettings(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class EntitlementAdditionalNotificationTargets(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        admin_email_recipients: Optional[Sequence[_builtins.str]] = ...,
        requester_email_recipients: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminEmailRecipients")
    def admin_email_recipients(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="requesterEmailRecipients")
    def requester_email_recipients(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class EntitlementApprovalWorkflow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        manual_approvals: outputs.EntitlementApprovalWorkflowManualApprovals,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="manualApprovals")
    def manual_approvals(
        self,
    ) -> outputs.EntitlementApprovalWorkflowManualApprovals: ...

@pulumi.output_type
class EntitlementApprovalWorkflowManualApprovals(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        steps: Sequence[outputs.EntitlementApprovalWorkflowManualApprovalsStep],
        require_approver_justification: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def steps(
        self,
    ) -> Sequence[outputs.EntitlementApprovalWorkflowManualApprovalsStep]: ...
    @_builtins.property
    @pulumi.getter(name="requireApproverJustification")
    def require_approver_justification(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class EntitlementApprovalWorkflowManualApprovalsStep(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        approvers: outputs.EntitlementApprovalWorkflowManualApprovalsStepApprovers,
        approvals_needed: Optional[_builtins.int] = ...,
        approver_email_recipients: Optional[Sequence[_builtins.str]] = ...,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def approvers(
        self,
    ) -> outputs.EntitlementApprovalWorkflowManualApprovalsStepApprovers: ...
    @_builtins.property
    @pulumi.getter(name="approvalsNeeded")
    def approvals_needed(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="approverEmailRecipients")
    def approver_email_recipients(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EntitlementApprovalWorkflowManualApprovalsStepApprovers(dict):
    def __init__(__self__, *, principals: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class EntitlementEligibleUser(dict):
    def __init__(__self__, *, principals: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class EntitlementPrivilegedAccess(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, gcp_iam_access: outputs.EntitlementPrivilegedAccessGcpIamAccess
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpIamAccess")
    def gcp_iam_access(self) -> outputs.EntitlementPrivilegedAccessGcpIamAccess: ...

@pulumi.output_type
class EntitlementPrivilegedAccessGcpIamAccess(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource: _builtins.str,
        resource_type: _builtins.str,
        role_bindings: Sequence[
            outputs.EntitlementPrivilegedAccessGcpIamAccessRoleBinding
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleBindings")
    def role_bindings(
        self,
    ) -> Sequence[outputs.EntitlementPrivilegedAccessGcpIamAccessRoleBinding]: ...

@pulumi.output_type
class EntitlementPrivilegedAccessGcpIamAccessRoleBinding(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        role: _builtins.str,
        condition_expression: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="conditionExpression")
    def condition_expression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EntitlementRequesterJustificationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        not_mandatory: Optional[
            outputs.EntitlementRequesterJustificationConfigNotMandatory
        ] = ...,
        unstructured: Optional[
            outputs.EntitlementRequesterJustificationConfigUnstructured
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="notMandatory")
    def not_mandatory(
        self,
    ) -> Optional[outputs.EntitlementRequesterJustificationConfigNotMandatory]: ...
    @_builtins.property
    @pulumi.getter
    def unstructured(
        self,
    ) -> Optional[outputs.EntitlementRequesterJustificationConfigUnstructured]: ...

@pulumi.output_type
class EntitlementRequesterJustificationConfigNotMandatory(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class EntitlementRequesterJustificationConfigUnstructured(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class GetEntitlementAdditionalNotificationTargetResult(dict):
    def __init__(
        __self__,
        *,
        admin_email_recipients: Sequence[_builtins.str],
        requester_email_recipients: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminEmailRecipients")
    def admin_email_recipients(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requesterEmailRecipients")
    def requester_email_recipients(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetEntitlementApprovalWorkflowResult(dict):
    def __init__(
        __self__,
        *,
        manual_approvals: Sequence[
            outputs.GetEntitlementApprovalWorkflowManualApprovalResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="manualApprovals")
    def manual_approvals(
        self,
    ) -> Sequence[outputs.GetEntitlementApprovalWorkflowManualApprovalResult]: ...

@pulumi.output_type
class GetEntitlementApprovalWorkflowManualApprovalResult(dict):
    def __init__(
        __self__,
        *,
        require_approver_justification: _builtins.bool,
        steps: Sequence[outputs.GetEntitlementApprovalWorkflowManualApprovalStepResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requireApproverJustification")
    def require_approver_justification(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def steps(
        self,
    ) -> Sequence[outputs.GetEntitlementApprovalWorkflowManualApprovalStepResult]: ...

@pulumi.output_type
class GetEntitlementApprovalWorkflowManualApprovalStepResult(dict):
    def __init__(
        __self__,
        *,
        approvals_needed: _builtins.int,
        approver_email_recipients: Sequence[_builtins.str],
        approvers: Sequence[
            outputs.GetEntitlementApprovalWorkflowManualApprovalStepApproverResult
        ],
        id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approvalsNeeded")
    def approvals_needed(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="approverEmailRecipients")
    def approver_email_recipients(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def approvers(
        self,
    ) -> Sequence[
        outputs.GetEntitlementApprovalWorkflowManualApprovalStepApproverResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class GetEntitlementApprovalWorkflowManualApprovalStepApproverResult(dict):
    def __init__(__self__, *, principals: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetEntitlementEligibleUserResult(dict):
    def __init__(__self__, *, principals: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetEntitlementPrivilegedAccessResult(dict):
    def __init__(
        __self__,
        *,
        gcp_iam_accesses: Sequence[
            outputs.GetEntitlementPrivilegedAccessGcpIamAccessResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpIamAccesses")
    def gcp_iam_accesses(
        self,
    ) -> Sequence[outputs.GetEntitlementPrivilegedAccessGcpIamAccessResult]: ...

@pulumi.output_type
class GetEntitlementPrivilegedAccessGcpIamAccessResult(dict):
    def __init__(
        __self__,
        *,
        resource: _builtins.str,
        resource_type: _builtins.str,
        role_bindings: Sequence[
            outputs.GetEntitlementPrivilegedAccessGcpIamAccessRoleBindingResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleBindings")
    def role_bindings(
        self,
    ) -> Sequence[
        outputs.GetEntitlementPrivilegedAccessGcpIamAccessRoleBindingResult
    ]: ...

@pulumi.output_type
class GetEntitlementPrivilegedAccessGcpIamAccessRoleBindingResult(dict):
    def __init__(
        __self__,
        *,
        condition_expression: _builtins.str,
        id: _builtins.str,
        role: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionExpression")
    def condition_expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...

@pulumi.output_type
class GetEntitlementRequesterJustificationConfigResult(dict):
    def __init__(
        __self__,
        *,
        not_mandatories: Sequence[
            outputs.GetEntitlementRequesterJustificationConfigNotMandatoryResult
        ],
        unstructureds: Sequence[
            outputs.GetEntitlementRequesterJustificationConfigUnstructuredResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="notMandatories")
    def not_mandatories(
        self,
    ) -> Sequence[
        outputs.GetEntitlementRequesterJustificationConfigNotMandatoryResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def unstructureds(
        self,
    ) -> Sequence[
        outputs.GetEntitlementRequesterJustificationConfigUnstructuredResult
    ]: ...

@pulumi.output_type
class GetEntitlementRequesterJustificationConfigNotMandatoryResult(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class GetEntitlementRequesterJustificationConfigUnstructuredResult(dict):
    def __init__(__self__) -> None: ...
