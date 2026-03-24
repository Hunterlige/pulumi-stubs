

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccessReviewHistoryInstanceResponse', 'AccessReviewInstanceResponse', 'AccessReviewRecurrenceRangeResponse', 'AccessReviewReviewerResponse', 'AccessReviewScopeResponse', 'ApprovalSettingsResponse', 'ApprovalStageResponse', 'ExpandedPropertiesResponse', 'ExpandedPropertiesResponsePrincipal', 'ExpandedPropertiesResponseRoleDefinition', 'ExpandedPropertiesResponseScope', 'IdentityResponse', 'IdentityResponseUserAssignedIdentities', 'ManagedByTenantResponse', 'ManagementLockOwnerResponse', 'NonComplianceMessageResponse', 'OverrideResponse', 'PIMOnlyModeSettingsResponse', 'ParameterDefinitionsValueResponse', 'ParameterDefinitionsValueResponseMetadata', 'ParameterValuesValueResponse', 'PermissionResponse', 'PolicyAssignmentPropertiesResponse', 'PolicyAssignmentPropertiesResponsePolicy', 'PolicyAssignmentPropertiesResponseRoleDefinition', 'PolicyAssignmentPropertiesResponseScope', 'PolicyDefinitionGroupResponse', 'PolicyDefinitionReferenceResponse', 'PolicyDefinitionVersionResponse', 'PolicyPropertiesResponse', 'PolicyPropertiesResponseScope', 'PolicySetDefinitionVersionResponse', 'PolicyVariableColumnResponse', 'PolicyVariableValueColumnValueResponse', 'PrincipalResponse', 'PrivateLinkAssociationPropertiesExpandedResponse', ..., 'ResourceSelectorResponse', ..., ..., ..., 'RoleManagementPolicyApprovalRuleResponse', ..., 'RoleManagementPolicyEnablementRuleResponse', 'RoleManagementPolicyExpirationRuleResponse', 'RoleManagementPolicyNotificationRuleResponse', 'RoleManagementPolicyPimOnlyModeRuleResponse', 'RoleManagementPolicyRuleTargetResponse', 'SelectorResponse', 'SubscriptionPoliciesResponse', 'SubscriptionResponse', 'SystemDataResponse', 'UserSetResponse', 'UsersOrServicePrincipalSetResponse']
@pulumi.output_type
class AccessReviewHistoryInstanceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, download_uri: _builtins.str, id: _builtins.str, name: _builtins.str, status: _builtins.str, type: _builtins.str, display_name: Optional[_builtins.str] = ..., expiration: Optional[_builtins.str] = ..., fulfilled_date_time: Optional[_builtins.str] = ..., review_history_period_end_date_time: Optional[_builtins.str] = ..., review_history_period_start_date_time: Optional[_builtins.str] = ..., run_date_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="downloadUri")
    def download_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fulfilledDateTime")
    def fulfilled_date_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reviewHistoryPeriodEndDateTime")
    def review_history_period_end_date_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reviewHistoryPeriodStartDateTime")
    def review_history_period_start_date_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runDateTime")
    def run_date_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AccessReviewInstanceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, reviewers_type: _builtins.str, status: _builtins.str, type: _builtins.str, backup_reviewers: Optional[Sequence[outputs.AccessReviewReviewerResponse]] = ..., end_date_time: Optional[_builtins.str] = ..., reviewers: Optional[Sequence[outputs.AccessReviewReviewerResponse]] = ..., start_date_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reviewersType")
    def reviewers_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupReviewers")
    def backup_reviewers(self) -> Optional[Sequence[outputs.AccessReviewReviewerResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDateTime")
    def end_date_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reviewers(self) -> Optional[Sequence[outputs.AccessReviewReviewerResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDateTime")
    def start_date_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AccessReviewRecurrenceRangeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_date: Optional[_builtins.str] = ..., number_of_occurrences: Optional[_builtins.int] = ..., start_date: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfOccurrences")
    def number_of_occurrences(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AccessReviewReviewerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_type: _builtins.str, principal_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AccessReviewScopeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assignment_state: _builtins.str, principal_type: _builtins.str, resource_id: _builtins.str, role_definition_id: _builtins.str, exclude_resource_id: Optional[_builtins.str] = ..., exclude_role_definition_id: Optional[_builtins.str] = ..., expand_nested_memberships: Optional[_builtins.bool] = ..., inactive_duration: Optional[_builtins.str] = ..., include_access_below_resource: Optional[_builtins.bool] = ..., include_inherited_access: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignmentState")
    def assignment_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeResourceId")
    def exclude_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeRoleDefinitionId")
    def exclude_role_definition_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expandNestedMemberships")
    def expand_nested_memberships(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inactiveDuration")
    def inactive_duration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeAccessBelowResource")
    def include_access_below_resource(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeInheritedAccess")
    def include_inherited_access(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ApprovalSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, approval_mode: Optional[_builtins.str] = ..., approval_stages: Optional[Sequence[outputs.ApprovalStageResponse]] = ..., is_approval_required: Optional[_builtins.bool] = ..., is_approval_required_for_extension: Optional[_builtins.bool] = ..., is_requestor_justification_required: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalMode")
    def approval_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalStages")
    def approval_stages(self) -> Optional[Sequence[outputs.ApprovalStageResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isApprovalRequired")
    def is_approval_required(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isApprovalRequiredForExtension")
    def is_approval_required_for_extension(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRequestorJustificationRequired")
    def is_requestor_justification_required(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ApprovalStageResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, approval_stage_time_out_in_days: Optional[_builtins.int] = ..., escalation_approvers: Optional[Sequence[outputs.UserSetResponse]] = ..., escalation_time_in_minutes: Optional[_builtins.int] = ..., is_approver_justification_required: Optional[_builtins.bool] = ..., is_escalation_enabled: Optional[_builtins.bool] = ..., primary_approvers: Optional[Sequence[outputs.UserSetResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalStageTimeOutInDays")
    def approval_stage_time_out_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="escalationApprovers")
    def escalation_approvers(self) -> Optional[Sequence[outputs.UserSetResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="escalationTimeInMinutes")
    def escalation_time_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isApproverJustificationRequired")
    def is_approver_justification_required(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEscalationEnabled")
    def is_escalation_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryApprovers")
    def primary_approvers(self) -> Optional[Sequence[outputs.UserSetResponse]]:
        
        ...
    


@pulumi.output_type
class ExpandedPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal: Optional[outputs.ExpandedPropertiesResponsePrincipal] = ..., role_definition: Optional[outputs.ExpandedPropertiesResponseRoleDefinition] = ..., scope: Optional[outputs.ExpandedPropertiesResponseScope] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[outputs.ExpandedPropertiesResponsePrincipal]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleDefinition")
    def role_definition(self) -> Optional[outputs.ExpandedPropertiesResponseRoleDefinition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[outputs.ExpandedPropertiesResponseScope]:
        
        ...
    


@pulumi.output_type
class ExpandedPropertiesResponsePrincipal(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., email: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExpandedPropertiesResponseRoleDefinition(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExpandedPropertiesResponseScope(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ..., user_assigned_identities: Optional[Mapping[str, outputs.IdentityResponseUserAssignedIdentities]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.IdentityResponseUserAssignedIdentities]]:
        
        ...
    


@pulumi.output_type
class IdentityResponseUserAssignedIdentities(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, principal_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ManagedByTenantResponse(dict):
    
    def __init__(__self__, *, tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagementLockOwnerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, application_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NonComplianceMessageResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, message: _builtins.str, policy_definition_reference_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OverrideResponse(dict):
    
    def __init__(__self__, *, kind: Optional[_builtins.str] = ..., selectors: Optional[Sequence[outputs.SelectorResponse]] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def selectors(self) -> Optional[Sequence[outputs.SelectorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PIMOnlyModeSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, excluded_assignment_types: Optional[Sequence[_builtins.str]] = ..., excludes: Optional[Sequence[outputs.UsersOrServicePrincipalSetResponse]] = ..., mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedAssignmentTypes")
    def excluded_assignment_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def excludes(self) -> Optional[Sequence[outputs.UsersOrServicePrincipalSetResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ParameterDefinitionsValueResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_values: Optional[Sequence[Any]] = ..., default_value: Optional[Any] = ..., metadata: Optional[outputs.ParameterDefinitionsValueResponseMetadata] = ..., schema: Optional[Any] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Optional[Sequence[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.ParameterDefinitionsValueResponseMetadata]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ParameterDefinitionsValueResponseMetadata(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assign_permissions: Optional[_builtins.bool] = ..., description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., strong_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignPermissions")
    def assign_permissions(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="strongType")
    def strong_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ParameterValuesValueResponse(dict):
    
    def __init__(__self__, *, value: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Any]:
        
        ...
    


@pulumi.output_type
class PermissionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, condition: _builtins.str, condition_version: _builtins.str, actions: Optional[Sequence[_builtins.str]] = ..., data_actions: Optional[Sequence[_builtins.str]] = ..., not_actions: Optional[Sequence[_builtins.str]] = ..., not_data_actions: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionVersion")
    def condition_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataActions")
    def data_actions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notActions")
    def not_actions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notDataActions")
    def not_data_actions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PolicyAssignmentPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, policy: Optional[outputs.PolicyAssignmentPropertiesResponsePolicy] = ..., role_definition: Optional[outputs.PolicyAssignmentPropertiesResponseRoleDefinition] = ..., scope: Optional[outputs.PolicyAssignmentPropertiesResponseScope] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[outputs.PolicyAssignmentPropertiesResponsePolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleDefinition")
    def role_definition(self) -> Optional[outputs.PolicyAssignmentPropertiesResponseRoleDefinition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[outputs.PolicyAssignmentPropertiesResponseScope]:
        
        ...
    


@pulumi.output_type
class PolicyAssignmentPropertiesResponsePolicy(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_modified_by: outputs.PrincipalResponse, id: Optional[_builtins.str] = ..., last_modified_date_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> outputs.PrincipalResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedDateTime")
    def last_modified_date_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyAssignmentPropertiesResponseRoleDefinition(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyAssignmentPropertiesResponseScope(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyDefinitionGroupResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, additional_metadata_id: Optional[_builtins.str] = ..., category: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalMetadataId")
    def additional_metadata_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyDefinitionReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, effective_definition_version: _builtins.str, latest_definition_version: _builtins.str, policy_definition_id: _builtins.str, definition_version: Optional[_builtins.str] = ..., group_names: Optional[Sequence[_builtins.str]] = ..., parameters: Optional[Mapping[str, outputs.ParameterValuesValueResponse]] = ..., policy_definition_reference_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveDefinitionVersion")
    def effective_definition_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestDefinitionVersion")
    def latest_definition_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDefinitionId")
    def policy_definition_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="definitionVersion")
    def definition_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupNames")
    def group_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, outputs.ParameterValuesValueResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyDefinitionVersionResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., metadata: Optional[Any] = ..., mode: Optional[_builtins.str] = ..., parameters: Optional[Mapping[str, outputs.ParameterDefinitionsValueResponse]] = ..., policy_rule: Optional[Any] = ..., policy_type: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, outputs.ParameterDefinitionsValueResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyRule")
    def policy_rule(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyPropertiesResponse(dict):
    
    def __init__(__self__, *, scope: outputs.PolicyPropertiesResponseScope) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> outputs.PolicyPropertiesResponseScope:
        
        ...
    


@pulumi.output_type
class PolicyPropertiesResponseScope(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicySetDefinitionVersionResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, policy_definitions: Sequence[outputs.PolicyDefinitionReferenceResponse], system_data: outputs.SystemDataResponse, type: _builtins.str, description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., metadata: Optional[Any] = ..., parameters: Optional[Mapping[str, outputs.ParameterDefinitionsValueResponse]] = ..., policy_definition_groups: Optional[Sequence[outputs.PolicyDefinitionGroupResponse]] = ..., policy_type: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDefinitions")
    def policy_definitions(self) -> Sequence[outputs.PolicyDefinitionReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, outputs.ParameterDefinitionsValueResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDefinitionGroups")
    def policy_definition_groups(self) -> Optional[Sequence[outputs.PolicyDefinitionGroupResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyVariableColumnResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, column_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PolicyVariableValueColumnValueResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, column_name: _builtins.str, column_value: Any) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnValue")
    def column_value(self) -> Any:
        
        ...
    


@pulumi.output_type
class PrincipalResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., email: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateLinkAssociationPropertiesExpandedResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, private_link: Optional[_builtins.str] = ..., public_network_access: Optional[_builtins.str] = ..., scope: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLink")
    def private_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantID")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceManagementPrivateLinkEndpointConnectionsResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, private_endpoint_connections: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ResourceSelectorResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., selectors: Optional[Sequence[outputs.SelectorResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def selectors(self) -> Optional[Sequence[outputs.SelectorResponse]]:
        
        ...
    


@pulumi.output_type
class RoleEligibilityScheduleRequestPropertiesResponseExpiration(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, duration: Optional[_builtins.str] = ..., end_date_time: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDateTime")
    def end_date_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RoleEligibilityScheduleRequestPropertiesResponseScheduleInfo(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expiration: Optional[outputs.RoleEligibilityScheduleRequestPropertiesResponseExpiration] = ..., start_date_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[outputs.RoleEligibilityScheduleRequestPropertiesResponseExpiration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDateTime")
    def start_date_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RoleEligibilityScheduleRequestPropertiesResponseTicketInfo(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ticket_number: Optional[_builtins.str] = ..., ticket_system: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ticketNumber")
    def ticket_number(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ticketSystem")
    def ticket_system(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RoleManagementPolicyApprovalRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, rule_type: _builtins.str, id: Optional[_builtins.str] = ..., setting: Optional[outputs.ApprovalSettingsResponse] = ..., target: Optional[outputs.RoleManagementPolicyRuleTargetResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def setting(self) -> Optional[outputs.ApprovalSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[outputs.RoleManagementPolicyRuleTargetResponse]:
        
        ...
    


@pulumi.output_type
class RoleManagementPolicyAuthenticationContextRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, rule_type: _builtins.str, claim_value: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., is_enabled: Optional[_builtins.bool] = ..., target: Optional[outputs.RoleManagementPolicyRuleTargetResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="claimValue")
    def claim_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[outputs.RoleManagementPolicyRuleTargetResponse]:
        
        ...
    


@pulumi.output_type
class RoleManagementPolicyEnablementRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, rule_type: _builtins.str, enabled_rules: Optional[Sequence[_builtins.str]] = ..., id: Optional[_builtins.str] = ..., target: Optional[outputs.RoleManagementPolicyRuleTargetResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledRules")
    def enabled_rules(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[outputs.RoleManagementPolicyRuleTargetResponse]:
        
        ...
    


@pulumi.output_type
class RoleManagementPolicyExpirationRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, rule_type: _builtins.str, exception_members: Optional[Sequence[outputs.UserSetResponse]] = ..., id: Optional[_builtins.str] = ..., is_expiration_required: Optional[_builtins.bool] = ..., maximum_duration: Optional[_builtins.str] = ..., target: Optional[outputs.RoleManagementPolicyRuleTargetResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exceptionMembers")
    def exception_members(self) -> Optional[Sequence[outputs.UserSetResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isExpirationRequired")
    def is_expiration_required(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumDuration")
    def maximum_duration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[outputs.RoleManagementPolicyRuleTargetResponse]:
        
        ...
    


@pulumi.output_type
class RoleManagementPolicyNotificationRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, rule_type: _builtins.str, id: Optional[_builtins.str] = ..., is_default_recipients_enabled: Optional[_builtins.bool] = ..., notification_level: Optional[_builtins.str] = ..., notification_recipients: Optional[Sequence[_builtins.str]] = ..., notification_type: Optional[_builtins.str] = ..., recipient_type: Optional[_builtins.str] = ..., target: Optional[outputs.RoleManagementPolicyRuleTargetResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefaultRecipientsEnabled")
    def is_default_recipients_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationLevel")
    def notification_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationRecipients")
    def notification_recipients(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recipientType")
    def recipient_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[outputs.RoleManagementPolicyRuleTargetResponse]:
        
        ...
    


@pulumi.output_type
class RoleManagementPolicyPimOnlyModeRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, rule_type: _builtins.str, id: Optional[_builtins.str] = ..., pim_only_mode_settings: Optional[outputs.PIMOnlyModeSettingsResponse] = ..., target: Optional[outputs.RoleManagementPolicyRuleTargetResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pimOnlyModeSettings")
    def pim_only_mode_settings(self) -> Optional[outputs.PIMOnlyModeSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[outputs.RoleManagementPolicyRuleTargetResponse]:
        
        ...
    


@pulumi.output_type
class RoleManagementPolicyRuleTargetResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, caller: Optional[_builtins.str] = ..., enforced_settings: Optional[Sequence[_builtins.str]] = ..., inheritable_settings: Optional[Sequence[_builtins.str]] = ..., level: Optional[_builtins.str] = ..., operations: Optional[Sequence[_builtins.str]] = ..., target_objects: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def caller(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforcedSettings")
    def enforced_settings(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inheritableSettings")
    def inheritable_settings(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetObjects")
    def target_objects(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class SelectorResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, in_: Optional[Sequence[_builtins.str]] = ..., kind: Optional[_builtins.str] = ..., not_in: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="in")
    def in_(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notIn")
    def not_in(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class SubscriptionPoliciesResponse(dict):
    
    def __init__(__self__, *, location_placement_id: Optional[_builtins.str] = ..., quota_id: Optional[_builtins.str] = ..., spending_limit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationPlacementId")
    def location_placement_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaId")
    def quota_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spendingLimit")
    def spending_limit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SubscriptionResponse(dict):
    
    def __init__(__self__, *, authorization_source: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., managed_by_tenants: Optional[Sequence[outputs.ManagedByTenantResponse]] = ..., state: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ..., subscription_policies: Optional[outputs.SubscriptionPoliciesResponse] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationSource")
    def authorization_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedByTenants")
    def managed_by_tenants(self) -> Optional[Sequence[outputs.ManagedByTenantResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionPolicies")
    def subscription_policies(self) -> Optional[outputs.SubscriptionPoliciesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserSetResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., is_backup: Optional[_builtins.bool] = ..., user_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isBackup")
    def is_backup(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userType")
    def user_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UsersOrServicePrincipalSetResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


