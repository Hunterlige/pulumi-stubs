import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "SettingsEmailNotificationSettingsArgs",
    "SettingsEmailNotificationSettingsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "SettingsServiceAccountApproverSettingsArgs",
    "SettingsServiceAccountApproverSettingsArgsDict",
    "EntitlementAdditionalNotificationTargetsArgs",
    "EntitlementAdditionalNotificationTargetsArgsDict",
    "EntitlementApprovalWorkflowArgs",
    "EntitlementApprovalWorkflowArgsDict",
    "EntitlementApprovalWorkflowManualApprovalsArgs",
    "EntitlementApprovalWorkflowManualApprovalsArgsDict",
    "EntitlementApprovalWorkflowManualApprovalsStepArgs",
    ...,
    ...,
    ...,
    "EntitlementEligibleUserArgs",
    "EntitlementEligibleUserArgsDict",
    "EntitlementPrivilegedAccessArgs",
    "EntitlementPrivilegedAccessArgsDict",
    "EntitlementPrivilegedAccessGcpIamAccessArgs",
    "EntitlementPrivilegedAccessGcpIamAccessArgsDict",
    ...,
    ...,
    "EntitlementRequesterJustificationConfigArgs",
    "EntitlementRequesterJustificationConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
]

class SettingsEmailNotificationSettingsArgsDict(TypedDict):
    custom_notification_behavior: NotRequired[
        pulumi.Input[
            SettingsEmailNotificationSettingsCustomNotificationBehaviorArgsDict
        ]
    ]
    disable_all_notifications: NotRequired[
        pulumi.Input[SettingsEmailNotificationSettingsDisableAllNotificationsArgsDict]
    ]

@pulumi.input_type
class SettingsEmailNotificationSettingsArgs:
    def __init__(
        __self__,
        *,
        custom_notification_behavior: Optional[
            pulumi.Input[
                SettingsEmailNotificationSettingsCustomNotificationBehaviorArgs
            ]
        ] = ...,
        disable_all_notifications: Optional[
            pulumi.Input[SettingsEmailNotificationSettingsDisableAllNotificationsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customNotificationBehavior")
    def custom_notification_behavior(
        self,
    ) -> Optional[
        pulumi.Input[SettingsEmailNotificationSettingsCustomNotificationBehaviorArgs]
    ]: ...
    @custom_notification_behavior.setter
    def custom_notification_behavior(
        self,
        value: Optional[
            pulumi.Input[
                SettingsEmailNotificationSettingsCustomNotificationBehaviorArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableAllNotifications")
    def disable_all_notifications(
        self,
    ) -> Optional[
        pulumi.Input[SettingsEmailNotificationSettingsDisableAllNotificationsArgs]
    ]: ...
    @disable_all_notifications.setter
    def disable_all_notifications(
        self,
        value: Optional[
            pulumi.Input[SettingsEmailNotificationSettingsDisableAllNotificationsArgs]
        ],
    ): ...

class SettingsEmailNotificationSettingsCustomNotificationBehaviorArgsDict(TypedDict):
    admin_notifications: NotRequired[
        pulumi.Input[
            SettingsEmailNotificationSettingsCustomNotificationBehaviorAdminNotificationsArgsDict
        ]
    ]
    approver_notifications: NotRequired[
        pulumi.Input[
            SettingsEmailNotificationSettingsCustomNotificationBehaviorApproverNotificationsArgsDict
        ]
    ]
    requester_notifications: NotRequired[
        pulumi.Input[
            SettingsEmailNotificationSettingsCustomNotificationBehaviorRequesterNotificationsArgsDict
        ]
    ]

@pulumi.input_type
class SettingsEmailNotificationSettingsCustomNotificationBehaviorArgs:
    def __init__(
        __self__,
        *,
        admin_notifications: Optional[
            pulumi.Input[
                SettingsEmailNotificationSettingsCustomNotificationBehaviorAdminNotificationsArgs
            ]
        ] = ...,
        approver_notifications: Optional[
            pulumi.Input[
                SettingsEmailNotificationSettingsCustomNotificationBehaviorApproverNotificationsArgs
            ]
        ] = ...,
        requester_notifications: Optional[
            pulumi.Input[
                SettingsEmailNotificationSettingsCustomNotificationBehaviorRequesterNotificationsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminNotifications")
    def admin_notifications(
        self,
    ) -> Optional[
        pulumi.Input[
            SettingsEmailNotificationSettingsCustomNotificationBehaviorAdminNotificationsArgs
        ]
    ]: ...
    @admin_notifications.setter
    def admin_notifications(
        self,
        value: Optional[
            pulumi.Input[
                SettingsEmailNotificationSettingsCustomNotificationBehaviorAdminNotificationsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="approverNotifications")
    def approver_notifications(
        self,
    ) -> Optional[
        pulumi.Input[
            SettingsEmailNotificationSettingsCustomNotificationBehaviorApproverNotificationsArgs
        ]
    ]: ...
    @approver_notifications.setter
    def approver_notifications(
        self,
        value: Optional[
            pulumi.Input[
                SettingsEmailNotificationSettingsCustomNotificationBehaviorApproverNotificationsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requesterNotifications")
    def requester_notifications(
        self,
    ) -> Optional[
        pulumi.Input[
            SettingsEmailNotificationSettingsCustomNotificationBehaviorRequesterNotificationsArgs
        ]
    ]: ...
    @requester_notifications.setter
    def requester_notifications(
        self,
        value: Optional[
            pulumi.Input[
                SettingsEmailNotificationSettingsCustomNotificationBehaviorRequesterNotificationsArgs
            ]
        ],
    ): ...

class SettingsEmailNotificationSettingsCustomNotificationBehaviorAdminNotificationsArgsDict(
    TypedDict
):
    grant_activated: NotRequired[pulumi.Input[_builtins.str]]
    grant_activation_failed: NotRequired[pulumi.Input[_builtins.str]]
    grant_ended: NotRequired[pulumi.Input[_builtins.str]]
    grant_externally_modified: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SettingsEmailNotificationSettingsCustomNotificationBehaviorAdminNotificationsArgs:
    def __init__(
        __self__,
        *,
        grant_activated: Optional[pulumi.Input[_builtins.str]] = ...,
        grant_activation_failed: Optional[pulumi.Input[_builtins.str]] = ...,
        grant_ended: Optional[pulumi.Input[_builtins.str]] = ...,
        grant_externally_modified: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="grantActivated")
    def grant_activated(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grant_activated.setter
    def grant_activated(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grantActivationFailed")
    def grant_activation_failed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grant_activation_failed.setter
    def grant_activation_failed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grantEnded")
    def grant_ended(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grant_ended.setter
    def grant_ended(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grantExternallyModified")
    def grant_externally_modified(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grant_externally_modified.setter
    def grant_externally_modified(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class SettingsEmailNotificationSettingsCustomNotificationBehaviorApproverNotificationsArgsDict(
    TypedDict
):
    pending_approval: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SettingsEmailNotificationSettingsCustomNotificationBehaviorApproverNotificationsArgs:
    def __init__(
        __self__, *, pending_approval: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pendingApproval")
    def pending_approval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pending_approval.setter
    def pending_approval(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SettingsEmailNotificationSettingsCustomNotificationBehaviorRequesterNotificationsArgsDict(
    TypedDict
):
    entitlement_assigned: NotRequired[pulumi.Input[_builtins.str]]
    grant_activated: NotRequired[pulumi.Input[_builtins.str]]
    grant_activation_failed: NotRequired[pulumi.Input[_builtins.str]]
    grant_denied: NotRequired[pulumi.Input[_builtins.str]]
    grant_ended: NotRequired[pulumi.Input[_builtins.str]]
    grant_expired: NotRequired[pulumi.Input[_builtins.str]]
    grant_externally_modified: NotRequired[pulumi.Input[_builtins.str]]
    grant_revoked: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SettingsEmailNotificationSettingsCustomNotificationBehaviorRequesterNotificationsArgs:
    def __init__(
        __self__,
        *,
        entitlement_assigned: Optional[pulumi.Input[_builtins.str]] = ...,
        grant_activated: Optional[pulumi.Input[_builtins.str]] = ...,
        grant_activation_failed: Optional[pulumi.Input[_builtins.str]] = ...,
        grant_denied: Optional[pulumi.Input[_builtins.str]] = ...,
        grant_ended: Optional[pulumi.Input[_builtins.str]] = ...,
        grant_expired: Optional[pulumi.Input[_builtins.str]] = ...,
        grant_externally_modified: Optional[pulumi.Input[_builtins.str]] = ...,
        grant_revoked: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entitlementAssigned")
    def entitlement_assigned(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entitlement_assigned.setter
    def entitlement_assigned(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grantActivated")
    def grant_activated(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grant_activated.setter
    def grant_activated(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grantActivationFailed")
    def grant_activation_failed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grant_activation_failed.setter
    def grant_activation_failed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grantDenied")
    def grant_denied(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grant_denied.setter
    def grant_denied(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grantEnded")
    def grant_ended(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grant_ended.setter
    def grant_ended(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grantExpired")
    def grant_expired(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grant_expired.setter
    def grant_expired(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grantExternallyModified")
    def grant_externally_modified(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grant_externally_modified.setter
    def grant_externally_modified(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="grantRevoked")
    def grant_revoked(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grant_revoked.setter
    def grant_revoked(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SettingsEmailNotificationSettingsDisableAllNotificationsArgsDict(TypedDict): ...

@pulumi.input_type
class SettingsEmailNotificationSettingsDisableAllNotificationsArgs:
    def __init__(__self__) -> None: ...

class SettingsServiceAccountApproverSettingsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class SettingsServiceAccountApproverSettingsArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EntitlementAdditionalNotificationTargetsArgsDict(TypedDict):
    admin_email_recipients: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    requester_email_recipients: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class EntitlementAdditionalNotificationTargetsArgs:
    def __init__(
        __self__,
        *,
        admin_email_recipients: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        requester_email_recipients: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminEmailRecipients")
    def admin_email_recipients(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @admin_email_recipients.setter
    def admin_email_recipients(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requesterEmailRecipients")
    def requester_email_recipients(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @requester_email_recipients.setter
    def requester_email_recipients(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class EntitlementApprovalWorkflowArgsDict(TypedDict):
    manual_approvals: pulumi.Input[EntitlementApprovalWorkflowManualApprovalsArgsDict]

@pulumi.input_type
class EntitlementApprovalWorkflowArgs:
    def __init__(
        __self__,
        *,
        manual_approvals: pulumi.Input[EntitlementApprovalWorkflowManualApprovalsArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="manualApprovals")
    def manual_approvals(
        self,
    ) -> pulumi.Input[EntitlementApprovalWorkflowManualApprovalsArgs]: ...
    @manual_approvals.setter
    def manual_approvals(
        self, value: pulumi.Input[EntitlementApprovalWorkflowManualApprovalsArgs]
    ): ...

class EntitlementApprovalWorkflowManualApprovalsArgsDict(TypedDict):
    steps: pulumi.Input[
        Sequence[pulumi.Input[EntitlementApprovalWorkflowManualApprovalsStepArgsDict]]
    ]
    require_approver_justification: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class EntitlementApprovalWorkflowManualApprovalsArgs:
    def __init__(
        __self__,
        *,
        steps: pulumi.Input[
            Sequence[pulumi.Input[EntitlementApprovalWorkflowManualApprovalsStepArgs]]
        ],
        require_approver_justification: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def steps(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[EntitlementApprovalWorkflowManualApprovalsStepArgs]]
    ]: ...
    @steps.setter
    def steps(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[EntitlementApprovalWorkflowManualApprovalsStepArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requireApproverJustification")
    def require_approver_justification(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_approver_justification.setter
    def require_approver_justification(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class EntitlementApprovalWorkflowManualApprovalsStepArgsDict(TypedDict):
    approvers: pulumi.Input[
        EntitlementApprovalWorkflowManualApprovalsStepApproversArgsDict
    ]
    approvals_needed: NotRequired[pulumi.Input[_builtins.int]]
    approver_email_recipients: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EntitlementApprovalWorkflowManualApprovalsStepArgs:
    def __init__(
        __self__,
        *,
        approvers: pulumi.Input[
            EntitlementApprovalWorkflowManualApprovalsStepApproversArgs
        ],
        approvals_needed: Optional[pulumi.Input[_builtins.int]] = ...,
        approver_email_recipients: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def approvers(
        self,
    ) -> pulumi.Input[EntitlementApprovalWorkflowManualApprovalsStepApproversArgs]: ...
    @approvers.setter
    def approvers(
        self,
        value: pulumi.Input[
            EntitlementApprovalWorkflowManualApprovalsStepApproversArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="approvalsNeeded")
    def approvals_needed(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @approvals_needed.setter
    def approvals_needed(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="approverEmailRecipients")
    def approver_email_recipients(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @approver_email_recipients.setter
    def approver_email_recipients(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EntitlementApprovalWorkflowManualApprovalsStepApproversArgsDict(TypedDict):
    principals: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class EntitlementApprovalWorkflowManualApprovalsStepApproversArgs:
    def __init__(
        __self__, *, principals: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def principals(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @principals.setter
    def principals(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class EntitlementEligibleUserArgsDict(TypedDict):
    principals: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class EntitlementEligibleUserArgs:
    def __init__(
        __self__, *, principals: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def principals(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @principals.setter
    def principals(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class EntitlementPrivilegedAccessArgsDict(TypedDict):
    gcp_iam_access: pulumi.Input[EntitlementPrivilegedAccessGcpIamAccessArgsDict]

@pulumi.input_type
class EntitlementPrivilegedAccessArgs:
    def __init__(
        __self__,
        *,
        gcp_iam_access: pulumi.Input[EntitlementPrivilegedAccessGcpIamAccessArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpIamAccess")
    def gcp_iam_access(
        self,
    ) -> pulumi.Input[EntitlementPrivilegedAccessGcpIamAccessArgs]: ...
    @gcp_iam_access.setter
    def gcp_iam_access(
        self, value: pulumi.Input[EntitlementPrivilegedAccessGcpIamAccessArgs]
    ): ...

class EntitlementPrivilegedAccessGcpIamAccessArgsDict(TypedDict):
    resource: pulumi.Input[_builtins.str]
    resource_type: pulumi.Input[_builtins.str]
    role_bindings: pulumi.Input[
        Sequence[
            pulumi.Input[EntitlementPrivilegedAccessGcpIamAccessRoleBindingArgsDict]
        ]
    ]

@pulumi.input_type
class EntitlementPrivilegedAccessGcpIamAccessArgs:
    def __init__(
        __self__,
        *,
        resource: pulumi.Input[_builtins.str],
        resource_type: pulumi.Input[_builtins.str],
        role_bindings: pulumi.Input[
            Sequence[
                pulumi.Input[EntitlementPrivilegedAccessGcpIamAccessRoleBindingArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Input[_builtins.str]: ...
    @resource.setter
    def resource(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleBindings")
    def role_bindings(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[EntitlementPrivilegedAccessGcpIamAccessRoleBindingArgs]]
    ]: ...
    @role_bindings.setter
    def role_bindings(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[EntitlementPrivilegedAccessGcpIamAccessRoleBindingArgs]
            ]
        ],
    ): ...

class EntitlementPrivilegedAccessGcpIamAccessRoleBindingArgsDict(TypedDict):
    role: pulumi.Input[_builtins.str]
    condition_expression: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EntitlementPrivilegedAccessGcpIamAccessRoleBindingArgs:
    def __init__(
        __self__,
        *,
        role: pulumi.Input[_builtins.str],
        condition_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]: ...
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="conditionExpression")
    def condition_expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @condition_expression.setter
    def condition_expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EntitlementRequesterJustificationConfigArgsDict(TypedDict):
    not_mandatory: NotRequired[
        pulumi.Input[EntitlementRequesterJustificationConfigNotMandatoryArgsDict]
    ]
    unstructured: NotRequired[
        pulumi.Input[EntitlementRequesterJustificationConfigUnstructuredArgsDict]
    ]

@pulumi.input_type
class EntitlementRequesterJustificationConfigArgs:
    def __init__(
        __self__,
        *,
        not_mandatory: Optional[
            pulumi.Input[EntitlementRequesterJustificationConfigNotMandatoryArgs]
        ] = ...,
        unstructured: Optional[
            pulumi.Input[EntitlementRequesterJustificationConfigUnstructuredArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="notMandatory")
    def not_mandatory(
        self,
    ) -> Optional[
        pulumi.Input[EntitlementRequesterJustificationConfigNotMandatoryArgs]
    ]: ...
    @not_mandatory.setter
    def not_mandatory(
        self,
        value: Optional[
            pulumi.Input[EntitlementRequesterJustificationConfigNotMandatoryArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def unstructured(
        self,
    ) -> Optional[
        pulumi.Input[EntitlementRequesterJustificationConfigUnstructuredArgs]
    ]: ...
    @unstructured.setter
    def unstructured(
        self,
        value: Optional[
            pulumi.Input[EntitlementRequesterJustificationConfigUnstructuredArgs]
        ],
    ): ...

class EntitlementRequesterJustificationConfigNotMandatoryArgsDict(TypedDict): ...

@pulumi.input_type
class EntitlementRequesterJustificationConfigNotMandatoryArgs:
    def __init__(__self__) -> None: ...

class EntitlementRequesterJustificationConfigUnstructuredArgsDict(TypedDict): ...

@pulumi.input_type
class EntitlementRequesterJustificationConfigUnstructuredArgs:
    def __init__(__self__) -> None: ...
