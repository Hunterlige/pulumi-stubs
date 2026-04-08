import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ScheduledQueryRuleArgs", "ScheduledQueryRule"]

@pulumi.input_type
class ScheduledQueryRuleArgs:
    def __init__(
        __self__,
        *,
        criteria: pulumi.Input[ScheduledQueryRuleCriteriaArgs],
        enabled: pulumi.Input[_builtins.bool],
        resource_group_name: pulumi.Input[_builtins.str],
        scopes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        actions: Optional[pulumi.Input[ActionsArgs]] = ...,
        auto_mitigate: Optional[pulumi.Input[_builtins.bool]] = ...,
        check_workspace_alerts_storage_configured: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        evaluation_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[pulumi.Input[IdentityArgs]] = ...,
        kind: Optional[pulumi.Input[Union[_builtins.str, Kind]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mute_actions_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        override_query_time_range: Optional[pulumi.Input[_builtins.str]] = ...,
        resolve_configuration: Optional[
            pulumi.Input[RuleResolveConfigurationArgs]
        ] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        severity: Optional[pulumi.Input[_builtins.float]] = ...,
        skip_query_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_resource_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        window_size: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def criteria(self) -> pulumi.Input[ScheduledQueryRuleCriteriaArgs]: ...
    @criteria.setter
    def criteria(self, value: pulumi.Input[ScheduledQueryRuleCriteriaArgs]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @scopes.setter
    def scopes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[ActionsArgs]]: ...
    @actions.setter
    def actions(self, value: Optional[pulumi.Input[ActionsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="autoMitigate")
    def auto_mitigate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_mitigate.setter
    def auto_mitigate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="checkWorkspaceAlertsStorageConfigured")
    def check_workspace_alerts_storage_configured(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @check_workspace_alerts_storage_configured.setter
    def check_workspace_alerts_storage_configured(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
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
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @evaluation_frequency.setter
    def evaluation_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, Kind]]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[_builtins.str, Kind]]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="muteActionsDuration")
    def mute_actions_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mute_actions_duration.setter
    def mute_actions_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="overrideQueryTimeRange")
    def override_query_time_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @override_query_time_range.setter
    def override_query_time_range(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resolveConfiguration")
    def resolve_configuration(
        self,
    ) -> Optional[pulumi.Input[RuleResolveConfigurationArgs]]: ...
    @resolve_configuration.setter
    def resolve_configuration(
        self, value: Optional[pulumi.Input[RuleResolveConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="skipQueryValidation")
    def skip_query_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_query_validation.setter
    def skip_query_validation(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceTypes")
    def target_resource_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @target_resource_types.setter
    def target_resource_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @window_size.setter
    def window_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:monitor:ScheduledQueryRule")
class ScheduledQueryRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        actions: Optional[pulumi.Input[Union[ActionsArgs, ActionsArgsDict]]] = ...,
        auto_mitigate: Optional[pulumi.Input[_builtins.bool]] = ...,
        check_workspace_alerts_storage_configured: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        criteria: Optional[
            pulumi.Input[
                Union[
                    ScheduledQueryRuleCriteriaArgs, ScheduledQueryRuleCriteriaArgsDict
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        evaluation_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[pulumi.Input[Union[IdentityArgs, IdentityArgsDict]]] = ...,
        kind: Optional[pulumi.Input[Union[_builtins.str, Kind]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mute_actions_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        override_query_time_range: Optional[pulumi.Input[_builtins.str]] = ...,
        resolve_configuration: Optional[
            pulumi.Input[
                Union[RuleResolveConfigurationArgs, RuleResolveConfigurationArgsDict]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        severity: Optional[pulumi.Input[_builtins.float]] = ...,
        skip_query_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_resource_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        window_size: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ScheduledQueryRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ScheduledQueryRule: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Optional[outputs.ActionsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="autoMitigate")
    def auto_mitigate(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="checkWorkspaceAlertsStorageConfigured")
    def check_workspace_alerts_storage_configured(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="createdWithApiVersion")
    def created_with_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def criteria(self) -> pulumi.Output[outputs.ScheduledQueryRuleCriteriaResponse]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="isLegacyLogAnalyticsRule")
    def is_legacy_log_analytics_rule(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isWorkspaceAlertsStorageConfigured")
    def is_workspace_alerts_storage_configured(
        self,
    ) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="muteActionsDuration")
    def mute_actions_duration(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="overrideQueryTimeRange")
    def override_query_time_range(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resolveConfiguration")
    def resolve_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.RuleResolveConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="skipQueryValidation")
    def skip_query_validation(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceTypes")
    def target_resource_types(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> pulumi.Output[Optional[_builtins.str]]: ...
