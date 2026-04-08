import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetScopeAccessReviewScheduleDefinitionByIdResult",
    ...,
    "get_scope_access_review_schedule_definition_by_id",
    ...,
]

@pulumi.output_type
class GetScopeAccessReviewScheduleDefinitionByIdResult:
    def __init__(
        __self__,
        auto_apply_decisions_enabled=...,
        azure_api_version=...,
        backup_reviewers=...,
        default_decision=...,
        default_decision_enabled=...,
        description_for_admins=...,
        description_for_reviewers=...,
        display_name=...,
        id=...,
        instance_duration_in_days=...,
        instances=...,
        interval=...,
        justification_required_on_approval=...,
        mail_notifications_enabled=...,
        name=...,
        principal_id=...,
        principal_name=...,
        principal_type=...,
        range=...,
        recommendation_look_back_duration=...,
        recommendations_enabled=...,
        reminder_notifications_enabled=...,
        reviewers=...,
        reviewers_type=...,
        scope=...,
        status=...,
        type=...,
        user_principal_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoApplyDecisionsEnabled")
    def auto_apply_decisions_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backupReviewers")
    def backup_reviewers(
        self,
    ) -> Optional[Sequence[outputs.AccessReviewReviewerResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultDecision")
    def default_decision(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultDecisionEnabled")
    def default_decision_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="descriptionForAdmins")
    def description_for_admins(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="descriptionForReviewers")
    def description_for_reviewers(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceDurationInDays")
    def instance_duration_in_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Optional[Sequence[outputs.AccessReviewInstanceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="justificationRequiredOnApproval")
    def justification_required_on_approval(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="mailNotificationsEnabled")
    def mail_notifications_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalName")
    def principal_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def range(self) -> Optional[outputs.AccessReviewRecurrenceRangeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="recommendationLookBackDuration")
    def recommendation_look_back_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recommendationsEnabled")
    def recommendations_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="reminderNotificationsEnabled")
    def reminder_notifications_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def reviewers(self) -> Optional[Sequence[outputs.AccessReviewReviewerResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="reviewersType")
    def reviewers_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> outputs.AccessReviewScopeResponse: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPrincipalName")
    def user_principal_name(self) -> _builtins.str: ...

class AwaitableGetScopeAccessReviewScheduleDefinitionByIdResult(
    GetScopeAccessReviewScheduleDefinitionByIdResult
):
    def __await__(self): ...

def get_scope_access_review_schedule_definition_by_id(
    schedule_definition_id: Optional[_builtins.str] = ...,
    scope: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetScopeAccessReviewScheduleDefinitionByIdResult: ...
def get_scope_access_review_schedule_definition_by_id_output(
    schedule_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
    scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetScopeAccessReviewScheduleDefinitionByIdResult]: ...
