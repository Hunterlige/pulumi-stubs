import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessReviewHistoryInstanceArgs",
    "AccessReviewHistoryInstanceArgsDict",
    "AccessReviewInstanceArgs",
    "AccessReviewInstanceArgsDict",
    "AccessReviewRecurrenceRangeArgs",
    "AccessReviewRecurrenceRangeArgsDict",
    "AccessReviewReviewerArgs",
    "AccessReviewReviewerArgsDict",
    "AccessReviewScopeArgs",
    "AccessReviewScopeArgsDict",
    "ApprovalSettingsArgs",
    "ApprovalSettingsArgsDict",
    "ApprovalStageArgs",
    "ApprovalStageArgsDict",
    "IdentityArgs",
    "IdentityArgsDict",
    "ManagementLockOwnerArgs",
    "ManagementLockOwnerArgsDict",
    "NonComplianceMessageArgs",
    "NonComplianceMessageArgsDict",
    "OverrideArgs",
    "OverrideArgsDict",
    "PIMOnlyModeSettingsArgs",
    "PIMOnlyModeSettingsArgsDict",
    "ParameterDefinitionsValueMetadataArgs",
    "ParameterDefinitionsValueMetadataArgsDict",
    "ParameterDefinitionsValueArgs",
    "ParameterDefinitionsValueArgsDict",
    "ParameterValuesValueArgs",
    "ParameterValuesValueArgsDict",
    "PermissionArgs",
    "PermissionArgsDict",
    "PolicyDefinitionGroupArgs",
    "PolicyDefinitionGroupArgsDict",
    "PolicyDefinitionReferenceArgs",
    "PolicyDefinitionReferenceArgsDict",
    "PolicyVariableColumnArgs",
    "PolicyVariableColumnArgsDict",
    "PolicyVariableValueColumnValueArgs",
    "PolicyVariableValueColumnValueArgsDict",
    "PrivateLinkAssociationPropertiesArgs",
    "PrivateLinkAssociationPropertiesArgsDict",
    "ResourceSelectorArgs",
    "ResourceSelectorArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "RoleManagementPolicyApprovalRuleArgs",
    "RoleManagementPolicyApprovalRuleArgsDict",
    "RoleManagementPolicyAuthenticationContextRuleArgs",
    ...,
    "RoleManagementPolicyEnablementRuleArgs",
    "RoleManagementPolicyEnablementRuleArgsDict",
    "RoleManagementPolicyExpirationRuleArgs",
    "RoleManagementPolicyExpirationRuleArgsDict",
    "RoleManagementPolicyNotificationRuleArgs",
    "RoleManagementPolicyNotificationRuleArgsDict",
    "RoleManagementPolicyPimOnlyModeRuleArgs",
    "RoleManagementPolicyPimOnlyModeRuleArgsDict",
    "RoleManagementPolicyRuleTargetArgs",
    "RoleManagementPolicyRuleTargetArgsDict",
    "SelectorArgs",
    "SelectorArgsDict",
    "UserSetArgs",
    "UserSetArgsDict",
    "UsersOrServicePrincipalSetArgs",
    "UsersOrServicePrincipalSetArgsDict",
]

class AccessReviewHistoryInstanceArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    expiration: NotRequired[pulumi.Input[_builtins.str]]
    fulfilled_date_time: NotRequired[pulumi.Input[_builtins.str]]
    review_history_period_end_date_time: NotRequired[pulumi.Input[_builtins.str]]
    review_history_period_start_date_time: NotRequired[pulumi.Input[_builtins.str]]
    run_date_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessReviewHistoryInstanceArgs:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        expiration: Optional[pulumi.Input[_builtins.str]] = ...,
        fulfilled_date_time: Optional[pulumi.Input[_builtins.str]] = ...,
        review_history_period_end_date_time: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        review_history_period_start_date_time: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        run_date_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiration.setter
    def expiration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fulfilledDateTime")
    def fulfilled_date_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fulfilled_date_time.setter
    def fulfilled_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reviewHistoryPeriodEndDateTime")
    def review_history_period_end_date_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @review_history_period_end_date_time.setter
    def review_history_period_end_date_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="reviewHistoryPeriodStartDateTime")
    def review_history_period_start_date_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @review_history_period_start_date_time.setter
    def review_history_period_start_date_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runDateTime")
    def run_date_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @run_date_time.setter
    def run_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessReviewInstanceArgsDict(TypedDict):
    backup_reviewers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AccessReviewReviewerArgsDict]]]
    ]
    end_date_time: NotRequired[pulumi.Input[_builtins.str]]
    reviewers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AccessReviewReviewerArgsDict]]]
    ]
    start_date_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessReviewInstanceArgs:
    def __init__(
        __self__,
        *,
        backup_reviewers: Optional[
            pulumi.Input[Sequence[pulumi.Input[AccessReviewReviewerArgs]]]
        ] = ...,
        end_date_time: Optional[pulumi.Input[_builtins.str]] = ...,
        reviewers: Optional[
            pulumi.Input[Sequence[pulumi.Input[AccessReviewReviewerArgs]]]
        ] = ...,
        start_date_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupReviewers")
    def backup_reviewers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessReviewReviewerArgs]]]]: ...
    @backup_reviewers.setter
    def backup_reviewers(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessReviewReviewerArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="endDateTime")
    def end_date_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_date_time.setter
    def end_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reviewers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessReviewReviewerArgs]]]]: ...
    @reviewers.setter
    def reviewers(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessReviewReviewerArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="startDateTime")
    def start_date_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_date_time.setter
    def start_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessReviewRecurrenceRangeArgsDict(TypedDict):
    end_date: NotRequired[pulumi.Input[_builtins.str]]
    number_of_occurrences: NotRequired[pulumi.Input[_builtins.int]]
    start_date: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[
        pulumi.Input[Union[_builtins.str, AccessReviewRecurrenceRangeType]]
    ]

@pulumi.input_type
class AccessReviewRecurrenceRangeArgs:
    def __init__(
        __self__,
        *,
        end_date: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_occurrences: Optional[pulumi.Input[_builtins.int]] = ...,
        start_date: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[
            pulumi.Input[Union[_builtins.str, AccessReviewRecurrenceRangeType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfOccurrences")
    def number_of_occurrences(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_occurrences.setter
    def number_of_occurrences(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_date.setter
    def start_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, AccessReviewRecurrenceRangeType]]
    ]: ...
    @type.setter
    def type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, AccessReviewRecurrenceRangeType]]
        ],
    ): ...

class AccessReviewReviewerArgsDict(TypedDict):
    principal_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessReviewReviewerArgs:
    def __init__(
        __self__, *, principal_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessReviewScopeArgsDict(TypedDict):
    exclude_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    exclude_role_definition_id: NotRequired[pulumi.Input[_builtins.str]]
    expand_nested_memberships: NotRequired[pulumi.Input[_builtins.bool]]
    inactive_duration: NotRequired[pulumi.Input[_builtins.str]]
    include_access_below_resource: NotRequired[pulumi.Input[_builtins.bool]]
    include_inherited_access: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AccessReviewScopeArgs:
    def __init__(
        __self__,
        *,
        exclude_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        exclude_role_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
        expand_nested_memberships: Optional[pulumi.Input[_builtins.bool]] = ...,
        inactive_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        include_access_below_resource: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_inherited_access: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludeResourceId")
    def exclude_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exclude_resource_id.setter
    def exclude_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="excludeRoleDefinitionId")
    def exclude_role_definition_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exclude_role_definition_id.setter
    def exclude_role_definition_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="expandNestedMemberships")
    def expand_nested_memberships(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @expand_nested_memberships.setter
    def expand_nested_memberships(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inactiveDuration")
    def inactive_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inactive_duration.setter
    def inactive_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="includeAccessBelowResource")
    def include_access_below_resource(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_access_below_resource.setter
    def include_access_below_resource(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeInheritedAccess")
    def include_inherited_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_inherited_access.setter
    def include_inherited_access(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ApprovalSettingsArgsDict(TypedDict):
    approval_mode: NotRequired[pulumi.Input[Union[_builtins.str, ApprovalMode]]]
    approval_stages: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ApprovalStageArgsDict]]]
    ]
    is_approval_required: NotRequired[pulumi.Input[_builtins.bool]]
    is_approval_required_for_extension: NotRequired[pulumi.Input[_builtins.bool]]
    is_requestor_justification_required: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ApprovalSettingsArgs:
    def __init__(
        __self__,
        *,
        approval_mode: Optional[pulumi.Input[Union[_builtins.str, ApprovalMode]]] = ...,
        approval_stages: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApprovalStageArgs]]]
        ] = ...,
        is_approval_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_approval_required_for_extension: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_requestor_justification_required: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approvalMode")
    def approval_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ApprovalMode]]]: ...
    @approval_mode.setter
    def approval_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ApprovalMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="approvalStages")
    def approval_stages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApprovalStageArgs]]]]: ...
    @approval_stages.setter
    def approval_stages(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApprovalStageArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isApprovalRequired")
    def is_approval_required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_approval_required.setter
    def is_approval_required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isApprovalRequiredForExtension")
    def is_approval_required_for_extension(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_approval_required_for_extension.setter
    def is_approval_required_for_extension(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isRequestorJustificationRequired")
    def is_requestor_justification_required(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_requestor_justification_required.setter
    def is_requestor_justification_required(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ApprovalStageArgsDict(TypedDict):
    approval_stage_time_out_in_days: NotRequired[pulumi.Input[_builtins.int]]
    escalation_approvers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[UserSetArgsDict]]]
    ]
    escalation_time_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    is_approver_justification_required: NotRequired[pulumi.Input[_builtins.bool]]
    is_escalation_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    primary_approvers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[UserSetArgsDict]]]
    ]

@pulumi.input_type
class ApprovalStageArgs:
    def __init__(
        __self__,
        *,
        approval_stage_time_out_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        escalation_approvers: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserSetArgs]]]
        ] = ...,
        escalation_time_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        is_approver_justification_required: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_escalation_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        primary_approvers: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserSetArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approvalStageTimeOutInDays")
    def approval_stage_time_out_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @approval_stage_time_out_in_days.setter
    def approval_stage_time_out_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="escalationApprovers")
    def escalation_approvers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserSetArgs]]]]: ...
    @escalation_approvers.setter
    def escalation_approvers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserSetArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="escalationTimeInMinutes")
    def escalation_time_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @escalation_time_in_minutes.setter
    def escalation_time_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isApproverJustificationRequired")
    def is_approver_justification_required(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_approver_justification_required.setter
    def is_approver_justification_required(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isEscalationEnabled")
    def is_escalation_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_escalation_enabled.setter
    def is_escalation_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryApprovers")
    def primary_approvers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserSetArgs]]]]: ...
    @primary_approvers.setter
    def primary_approvers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserSetArgs]]]]
    ): ...

class IdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[ResourceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class IdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[ResourceIdentityType]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ManagementLockOwnerArgsDict(TypedDict):
    application_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagementLockOwnerArgs:
    def __init__(
        __self__, *, application_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NonComplianceMessageArgsDict(TypedDict):
    message: pulumi.Input[_builtins.str]
    policy_definition_reference_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NonComplianceMessageArgs:
    def __init__(
        __self__,
        *,
        message: pulumi.Input[_builtins.str],
        policy_definition_reference_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> pulumi.Input[_builtins.str]: ...
    @message.setter
    def message(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_definition_reference_id.setter
    def policy_definition_reference_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class OverrideArgsDict(TypedDict):
    kind: NotRequired[pulumi.Input[Union[_builtins.str, OverrideKind]]]
    selectors: NotRequired[pulumi.Input[Sequence[pulumi.Input[SelectorArgsDict]]]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OverrideArgs:
    def __init__(
        __self__,
        *,
        kind: Optional[pulumi.Input[Union[_builtins.str, OverrideKind]]] = ...,
        selectors: Optional[pulumi.Input[Sequence[pulumi.Input[SelectorArgs]]]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, OverrideKind]]]: ...
    @kind.setter
    def kind(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OverrideKind]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def selectors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SelectorArgs]]]]: ...
    @selectors.setter
    def selectors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SelectorArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PIMOnlyModeSettingsArgsDict(TypedDict):
    excluded_assignment_types: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, ExcludedPrincipalTypes]]]
        ]
    ]
    excludes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[UsersOrServicePrincipalSetArgsDict]]]
    ]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, PIMOnlyMode]]]

@pulumi.input_type
class PIMOnlyModeSettingsArgs:
    def __init__(
        __self__,
        *,
        excluded_assignment_types: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ExcludedPrincipalTypes]]]
            ]
        ] = ...,
        excludes: Optional[
            pulumi.Input[Sequence[pulumi.Input[UsersOrServicePrincipalSetArgs]]]
        ] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, PIMOnlyMode]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludedAssignmentTypes")
    def excluded_assignment_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, ExcludedPrincipalTypes]]]
        ]
    ]: ...
    @excluded_assignment_types.setter
    def excluded_assignment_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ExcludedPrincipalTypes]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[UsersOrServicePrincipalSetArgs]]]
    ]: ...
    @excludes.setter
    def excludes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[UsersOrServicePrincipalSetArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[_builtins.str, PIMOnlyMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PIMOnlyMode]]]
    ): ...

class ParameterDefinitionsValueMetadataArgsDict(TypedDict):
    assign_permissions: NotRequired[pulumi.Input[_builtins.bool]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    strong_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ParameterDefinitionsValueMetadataArgs:
    def __init__(
        __self__,
        *,
        assign_permissions: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        strong_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assignPermissions")
    def assign_permissions(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @assign_permissions.setter
    def assign_permissions(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="strongType")
    def strong_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @strong_type.setter
    def strong_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ParameterDefinitionsValueArgsDict(TypedDict):
    allowed_values: NotRequired[pulumi.Input[Sequence[Any]]]
    default_value: NotRequired[Any]
    metadata: NotRequired[pulumi.Input[ParameterDefinitionsValueMetadataArgsDict]]
    schema: NotRequired[Any]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ParameterType]]]

@pulumi.input_type
class ParameterDefinitionsValueArgs:
    def __init__(
        __self__,
        *,
        allowed_values: Optional[pulumi.Input[Sequence[Any]]] = ...,
        default_value: Optional[Any] = ...,
        metadata: Optional[pulumi.Input[ParameterDefinitionsValueMetadataArgs]] = ...,
        schema: Optional[Any] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, ParameterType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Optional[pulumi.Input[Sequence[Any]]]: ...
    @allowed_values.setter
    def allowed_values(self, value: Optional[pulumi.Input[Sequence[Any]]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[Any]: ...
    @default_value.setter
    def default_value(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[ParameterDefinitionsValueMetadataArgs]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[ParameterDefinitionsValueMetadataArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[Any]: ...
    @schema.setter
    def schema(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, ParameterType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ParameterType]]]
    ): ...

class ParameterValuesValueArgsDict(TypedDict):
    value: NotRequired[Any]

@pulumi.input_type
class ParameterValuesValueArgs:
    def __init__(__self__, *, value: Optional[Any] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Any]: ...
    @value.setter
    def value(self, value: Optional[Any]): ...

class PermissionArgsDict(TypedDict):
    actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    data_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    not_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    not_data_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class PermissionArgs:
    def __init__(
        __self__,
        *,
        actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        data_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        not_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        not_data_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @actions.setter
    def actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataActions")
    def data_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @data_actions.setter
    def data_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notActions")
    def not_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @not_actions.setter
    def not_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notDataActions")
    def not_data_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @not_data_actions.setter
    def not_data_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PolicyDefinitionGroupArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    additional_metadata_id: NotRequired[pulumi.Input[_builtins.str]]
    category: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyDefinitionGroupArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        additional_metadata_id: Optional[pulumi.Input[_builtins.str]] = ...,
        category: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalMetadataId")
    def additional_metadata_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_metadata_id.setter
    def additional_metadata_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @category.setter
    def category(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyDefinitionReferenceArgsDict(TypedDict):
    policy_definition_id: pulumi.Input[_builtins.str]
    definition_version: NotRequired[pulumi.Input[_builtins.str]]
    group_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    parameters: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[ParameterValuesValueArgsDict]]]
    ]
    policy_definition_reference_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyDefinitionReferenceArgs:
    def __init__(
        __self__,
        *,
        policy_definition_id: pulumi.Input[_builtins.str],
        definition_version: Optional[pulumi.Input[_builtins.str]] = ...,
        group_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ParameterValuesValueArgs]]]
        ] = ...,
        policy_definition_reference_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyDefinitionId")
    def policy_definition_id(self) -> pulumi.Input[_builtins.str]: ...
    @policy_definition_id.setter
    def policy_definition_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="definitionVersion")
    def definition_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @definition_version.setter
    def definition_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="groupNames")
    def group_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @group_names.setter
    def group_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[ParameterValuesValueArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ParameterValuesValueArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_definition_reference_id.setter
    def policy_definition_reference_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class PolicyVariableColumnArgsDict(TypedDict):
    column_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class PolicyVariableColumnArgs:
    def __init__(__self__, *, column_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> pulumi.Input[_builtins.str]: ...
    @column_name.setter
    def column_name(self, value: pulumi.Input[_builtins.str]): ...

class PolicyVariableValueColumnValueArgsDict(TypedDict):
    column_name: pulumi.Input[_builtins.str]
    column_value: Any

@pulumi.input_type
class PolicyVariableValueColumnValueArgs:
    def __init__(
        __self__, *, column_name: pulumi.Input[_builtins.str], column_value: Any
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> pulumi.Input[_builtins.str]: ...
    @column_name.setter
    def column_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="columnValue")
    def column_value(self) -> Any: ...
    @column_value.setter
    def column_value(self, value: Any): ...

class PrivateLinkAssociationPropertiesArgsDict(TypedDict):
    private_link: NotRequired[pulumi.Input[_builtins.str]]
    public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, PublicNetworkAccessOptions]]
    ]

@pulumi.input_type
class PrivateLinkAssociationPropertiesArgs:
    def __init__(
        __self__,
        *,
        private_link: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccessOptions]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateLink")
    def private_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_link.setter
    def private_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessOptions]]]: ...
    @public_network_access.setter
    def public_network_access(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessOptions]]],
    ): ...

class ResourceSelectorArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    selectors: NotRequired[pulumi.Input[Sequence[pulumi.Input[SelectorArgsDict]]]]

@pulumi.input_type
class ResourceSelectorArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        selectors: Optional[pulumi.Input[Sequence[pulumi.Input[SelectorArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def selectors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SelectorArgs]]]]: ...
    @selectors.setter
    def selectors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SelectorArgs]]]]
    ): ...

class RoleEligibilityScheduleRequestPropertiesExpirationArgsDict(TypedDict):
    duration: NotRequired[pulumi.Input[_builtins.str]]
    end_date_time: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, Type]]]

@pulumi.input_type
class RoleEligibilityScheduleRequestPropertiesExpirationArgs:
    def __init__(
        __self__,
        *,
        duration: Optional[pulumi.Input[_builtins.str]] = ...,
        end_date_time: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, Type]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endDateTime")
    def end_date_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_date_time.setter
    def end_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, Type]]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, Type]]]): ...

class RoleEligibilityScheduleRequestPropertiesScheduleInfoArgsDict(TypedDict):
    expiration: NotRequired[
        pulumi.Input[RoleEligibilityScheduleRequestPropertiesExpirationArgsDict]
    ]
    start_date_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RoleEligibilityScheduleRequestPropertiesScheduleInfoArgs:
    def __init__(
        __self__,
        *,
        expiration: Optional[
            pulumi.Input[RoleEligibilityScheduleRequestPropertiesExpirationArgs]
        ] = ...,
        start_date_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expiration(
        self,
    ) -> Optional[
        pulumi.Input[RoleEligibilityScheduleRequestPropertiesExpirationArgs]
    ]: ...
    @expiration.setter
    def expiration(
        self,
        value: Optional[
            pulumi.Input[RoleEligibilityScheduleRequestPropertiesExpirationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="startDateTime")
    def start_date_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_date_time.setter
    def start_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RoleEligibilityScheduleRequestPropertiesTicketInfoArgsDict(TypedDict):
    ticket_number: NotRequired[pulumi.Input[_builtins.str]]
    ticket_system: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RoleEligibilityScheduleRequestPropertiesTicketInfoArgs:
    def __init__(
        __self__,
        *,
        ticket_number: Optional[pulumi.Input[_builtins.str]] = ...,
        ticket_system: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ticketNumber")
    def ticket_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ticket_number.setter
    def ticket_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ticketSystem")
    def ticket_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ticket_system.setter
    def ticket_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RoleManagementPolicyApprovalRuleArgsDict(TypedDict):
    rule_type: pulumi.Input[_builtins.str]
    id: NotRequired[pulumi.Input[_builtins.str]]
    setting: NotRequired[pulumi.Input[ApprovalSettingsArgsDict]]
    target: NotRequired[pulumi.Input[RoleManagementPolicyRuleTargetArgsDict]]

@pulumi.input_type
class RoleManagementPolicyApprovalRuleArgs:
    def __init__(
        __self__,
        *,
        rule_type: pulumi.Input[_builtins.str],
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        setting: Optional[pulumi.Input[ApprovalSettingsArgs]] = ...,
        target: Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> pulumi.Input[_builtins.str]: ...
    @rule_type.setter
    def rule_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def setting(self) -> Optional[pulumi.Input[ApprovalSettingsArgs]]: ...
    @setting.setter
    def setting(self, value: Optional[pulumi.Input[ApprovalSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]]: ...
    @target.setter
    def target(
        self, value: Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]]
    ): ...

class RoleManagementPolicyAuthenticationContextRuleArgsDict(TypedDict):
    rule_type: pulumi.Input[_builtins.str]
    claim_value: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    is_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    target: NotRequired[pulumi.Input[RoleManagementPolicyRuleTargetArgsDict]]

@pulumi.input_type
class RoleManagementPolicyAuthenticationContextRuleArgs:
    def __init__(
        __self__,
        *,
        rule_type: pulumi.Input[_builtins.str],
        claim_value: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        target: Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> pulumi.Input[_builtins.str]: ...
    @rule_type.setter
    def rule_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="claimValue")
    def claim_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @claim_value.setter
    def claim_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]]: ...
    @target.setter
    def target(
        self, value: Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]]
    ): ...

class RoleManagementPolicyEnablementRuleArgsDict(TypedDict):
    rule_type: pulumi.Input[_builtins.str]
    enabled_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, EnablementRules]]]]
    ]
    id: NotRequired[pulumi.Input[_builtins.str]]
    target: NotRequired[pulumi.Input[RoleManagementPolicyRuleTargetArgsDict]]

@pulumi.input_type
class RoleManagementPolicyEnablementRuleArgs:
    def __init__(
        __self__,
        *,
        rule_type: pulumi.Input[_builtins.str],
        enabled_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, EnablementRules]]]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> pulumi.Input[_builtins.str]: ...
    @rule_type.setter
    def rule_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="enabledRules")
    def enabled_rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, EnablementRules]]]]
    ]: ...
    @enabled_rules.setter
    def enabled_rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, EnablementRules]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]]: ...
    @target.setter
    def target(
        self, value: Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]]
    ): ...

class RoleManagementPolicyExpirationRuleArgsDict(TypedDict):
    rule_type: pulumi.Input[_builtins.str]
    exception_members: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[UserSetArgsDict]]]
    ]
    id: NotRequired[pulumi.Input[_builtins.str]]
    is_expiration_required: NotRequired[pulumi.Input[_builtins.bool]]
    maximum_duration: NotRequired[pulumi.Input[_builtins.str]]
    target: NotRequired[pulumi.Input[RoleManagementPolicyRuleTargetArgsDict]]

@pulumi.input_type
class RoleManagementPolicyExpirationRuleArgs:
    def __init__(
        __self__,
        *,
        rule_type: pulumi.Input[_builtins.str],
        exception_members: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserSetArgs]]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        is_expiration_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        maximum_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> pulumi.Input[_builtins.str]: ...
    @rule_type.setter
    def rule_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="exceptionMembers")
    def exception_members(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserSetArgs]]]]: ...
    @exception_members.setter
    def exception_members(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserSetArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isExpirationRequired")
    def is_expiration_required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_expiration_required.setter
    def is_expiration_required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumDuration")
    def maximum_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maximum_duration.setter
    def maximum_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]]: ...
    @target.setter
    def target(
        self, value: Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]]
    ): ...

class RoleManagementPolicyNotificationRuleArgsDict(TypedDict):
    rule_type: pulumi.Input[_builtins.str]
    id: NotRequired[pulumi.Input[_builtins.str]]
    is_default_recipients_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    notification_level: NotRequired[
        pulumi.Input[Union[_builtins.str, NotificationLevel]]
    ]
    notification_recipients: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    notification_type: NotRequired[
        pulumi.Input[Union[_builtins.str, NotificationDeliveryMechanism]]
    ]
    recipient_type: NotRequired[pulumi.Input[Union[_builtins.str, RecipientType]]]
    target: NotRequired[pulumi.Input[RoleManagementPolicyRuleTargetArgsDict]]

@pulumi.input_type
class RoleManagementPolicyNotificationRuleArgs:
    def __init__(
        __self__,
        *,
        rule_type: pulumi.Input[_builtins.str],
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        is_default_recipients_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        notification_level: Optional[
            pulumi.Input[Union[_builtins.str, NotificationLevel]]
        ] = ...,
        notification_recipients: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        notification_type: Optional[
            pulumi.Input[Union[_builtins.str, NotificationDeliveryMechanism]]
        ] = ...,
        recipient_type: Optional[
            pulumi.Input[Union[_builtins.str, RecipientType]]
        ] = ...,
        target: Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> pulumi.Input[_builtins.str]: ...
    @rule_type.setter
    def rule_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isDefaultRecipientsEnabled")
    def is_default_recipients_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_default_recipients_enabled.setter
    def is_default_recipients_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationLevel")
    def notification_level(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NotificationLevel]]]: ...
    @notification_level.setter
    def notification_level(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NotificationLevel]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationRecipients")
    def notification_recipients(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @notification_recipients.setter
    def notification_recipients(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, NotificationDeliveryMechanism]]
    ]: ...
    @notification_type.setter
    def notification_type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, NotificationDeliveryMechanism]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="recipientType")
    def recipient_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RecipientType]]]: ...
    @recipient_type.setter
    def recipient_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RecipientType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]]: ...
    @target.setter
    def target(
        self, value: Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]]
    ): ...

class RoleManagementPolicyPimOnlyModeRuleArgsDict(TypedDict):
    rule_type: pulumi.Input[_builtins.str]
    id: NotRequired[pulumi.Input[_builtins.str]]
    pim_only_mode_settings: NotRequired[pulumi.Input[PIMOnlyModeSettingsArgsDict]]
    target: NotRequired[pulumi.Input[RoleManagementPolicyRuleTargetArgsDict]]

@pulumi.input_type
class RoleManagementPolicyPimOnlyModeRuleArgs:
    def __init__(
        __self__,
        *,
        rule_type: pulumi.Input[_builtins.str],
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        pim_only_mode_settings: Optional[pulumi.Input[PIMOnlyModeSettingsArgs]] = ...,
        target: Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> pulumi.Input[_builtins.str]: ...
    @rule_type.setter
    def rule_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pimOnlyModeSettings")
    def pim_only_mode_settings(
        self,
    ) -> Optional[pulumi.Input[PIMOnlyModeSettingsArgs]]: ...
    @pim_only_mode_settings.setter
    def pim_only_mode_settings(
        self, value: Optional[pulumi.Input[PIMOnlyModeSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]]: ...
    @target.setter
    def target(
        self, value: Optional[pulumi.Input[RoleManagementPolicyRuleTargetArgs]]
    ): ...

class RoleManagementPolicyRuleTargetArgsDict(TypedDict):
    caller: NotRequired[pulumi.Input[_builtins.str]]
    enforced_settings: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    inheritable_settings: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    level: NotRequired[pulumi.Input[_builtins.str]]
    operations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    target_objects: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RoleManagementPolicyRuleTargetArgs:
    def __init__(
        __self__,
        *,
        caller: Optional[pulumi.Input[_builtins.str]] = ...,
        enforced_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        inheritable_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        level: Optional[pulumi.Input[_builtins.str]] = ...,
        operations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        target_objects: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def caller(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @caller.setter
    def caller(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enforcedSettings")
    def enforced_settings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enforced_settings.setter
    def enforced_settings(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inheritableSettings")
    def inheritable_settings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @inheritable_settings.setter
    def inheritable_settings(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @level.setter
    def level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @operations.setter
    def operations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetObjects")
    def target_objects(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @target_objects.setter
    def target_objects(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class SelectorArgsDict(TypedDict):
    in_: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    kind: NotRequired[pulumi.Input[Union[_builtins.str, SelectorKind]]]
    not_in: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class SelectorArgs:
    def __init__(
        __self__,
        *,
        in_: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        kind: Optional[pulumi.Input[Union[_builtins.str, SelectorKind]]] = ...,
        not_in: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="in")
    def in_(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @in_.setter
    def in_(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, SelectorKind]]]: ...
    @kind.setter
    def kind(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SelectorKind]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notIn")
    def not_in(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @not_in.setter
    def not_in(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class UserSetArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    is_backup: NotRequired[pulumi.Input[_builtins.bool]]
    user_type: NotRequired[pulumi.Input[Union[_builtins.str, UserType]]]

@pulumi.input_type
class UserSetArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        is_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        user_type: Optional[pulumi.Input[Union[_builtins.str, UserType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isBackup")
    def is_backup(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_backup.setter
    def is_backup(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="userType")
    def user_type(self) -> Optional[pulumi.Input[Union[_builtins.str, UserType]]]: ...
    @user_type.setter
    def user_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, UserType]]]
    ): ...

class UsersOrServicePrincipalSetArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, UserType]]]

@pulumi.input_type
class UsersOrServicePrincipalSetArgs:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, UserType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, UserType]]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, UserType]]]): ...
