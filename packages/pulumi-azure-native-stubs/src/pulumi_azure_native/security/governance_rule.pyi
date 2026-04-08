import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GovernanceRuleArgs", "GovernanceRule"]

@pulumi.input_type
class GovernanceRuleArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        owner_source: pulumi.Input[GovernanceRuleOwnerSourceArgs],
        rule_priority: pulumi.Input[_builtins.int],
        rule_type: pulumi.Input[Union[_builtins.str, GovernanceRuleType]],
        scope: pulumi.Input[_builtins.str],
        source_resource_type: pulumi.Input[
            Union[_builtins.str, GovernanceRuleSourceResourceType]
        ],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        excluded_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        governance_email_notification: Optional[
            pulumi.Input[GovernanceRuleEmailNotificationArgs]
        ] = ...,
        include_member_scopes: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_grace_period: Optional[pulumi.Input[_builtins.bool]] = ...,
        remediation_timeframe: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ownerSource")
    def owner_source(self) -> pulumi.Input[GovernanceRuleOwnerSourceArgs]: ...
    @owner_source.setter
    def owner_source(self, value: pulumi.Input[GovernanceRuleOwnerSourceArgs]): ...
    @_builtins.property
    @pulumi.getter(name="rulePriority")
    def rule_priority(self) -> pulumi.Input[_builtins.int]: ...
    @rule_priority.setter
    def rule_priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> pulumi.Input[Union[_builtins.str, GovernanceRuleType]]: ...
    @rule_type.setter
    def rule_type(
        self, value: pulumi.Input[Union[_builtins.str, GovernanceRuleType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceType")
    def source_resource_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, GovernanceRuleSourceResourceType]]: ...
    @source_resource_type.setter
    def source_resource_type(
        self,
        value: pulumi.Input[Union[_builtins.str, GovernanceRuleSourceResourceType]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="excludedScopes")
    def excluded_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_scopes.setter
    def excluded_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="governanceEmailNotification")
    def governance_email_notification(
        self,
    ) -> Optional[pulumi.Input[GovernanceRuleEmailNotificationArgs]]: ...
    @governance_email_notification.setter
    def governance_email_notification(
        self, value: Optional[pulumi.Input[GovernanceRuleEmailNotificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeMemberScopes")
    def include_member_scopes(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_member_scopes.setter
    def include_member_scopes(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_disabled.setter
    def is_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isGracePeriod")
    def is_grace_period(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_grace_period.setter
    def is_grace_period(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="remediationTimeframe")
    def remediation_timeframe(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @remediation_timeframe.setter
    def remediation_timeframe(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_id.setter
    def rule_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:security:GovernanceRule")
class GovernanceRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        excluded_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        governance_email_notification: Optional[
            pulumi.Input[
                Union[
                    GovernanceRuleEmailNotificationArgs,
                    GovernanceRuleEmailNotificationArgsDict,
                ]
            ]
        ] = ...,
        include_member_scopes: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_grace_period: Optional[pulumi.Input[_builtins.bool]] = ...,
        owner_source: Optional[
            pulumi.Input[
                Union[GovernanceRuleOwnerSourceArgs, GovernanceRuleOwnerSourceArgsDict]
            ]
        ] = ...,
        remediation_timeframe: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_priority: Optional[pulumi.Input[_builtins.int]] = ...,
        rule_type: Optional[
            pulumi.Input[Union[_builtins.str, GovernanceRuleType]]
        ] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        source_resource_type: Optional[
            pulumi.Input[Union[_builtins.str, GovernanceRuleSourceResourceType]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GovernanceRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> GovernanceRule: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="excludedScopes")
    def excluded_scopes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="governanceEmailNotification")
    def governance_email_notification(
        self,
    ) -> pulumi.Output[Optional[outputs.GovernanceRuleEmailNotificationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="includeMemberScopes")
    def include_member_scopes(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="isGracePeriod")
    def is_grace_period(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> pulumi.Output[Optional[outputs.GovernanceRuleMetadataResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerSource")
    def owner_source(
        self,
    ) -> pulumi.Output[outputs.GovernanceRuleOwnerSourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="remediationTimeframe")
    def remediation_timeframe(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="rulePriority")
    def rule_priority(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceType")
    def source_resource_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
