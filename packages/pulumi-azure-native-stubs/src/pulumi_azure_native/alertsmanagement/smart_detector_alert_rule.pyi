import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SmartDetectorAlertRuleArgs", "SmartDetectorAlertRule"]

@pulumi.input_type
class SmartDetectorAlertRuleArgs:
    def __init__(
        __self__,
        *,
        action_groups: pulumi.Input[ActionGroupsInformationArgs],
        detector: pulumi.Input[DetectorArgs],
        frequency: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        scope: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        severity: pulumi.Input[Union[_builtins.str, Severity]],
        state: pulumi.Input[Union[_builtins.str, AlertRuleState]],
        alert_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        throttling: Optional[pulumi.Input[ThrottlingInformationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionGroups")
    def action_groups(self) -> pulumi.Input[ActionGroupsInformationArgs]: ...
    @action_groups.setter
    def action_groups(self, value: pulumi.Input[ActionGroupsInformationArgs]): ...
    @_builtins.property
    @pulumi.getter
    def detector(self) -> pulumi.Input[DetectorArgs]: ...
    @detector.setter
    def detector(self, value: pulumi.Input[DetectorArgs]): ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[_builtins.str]: ...
    @frequency.setter
    def frequency(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Input[Union[_builtins.str, Severity]]: ...
    @severity.setter
    def severity(self, value: pulumi.Input[Union[_builtins.str, Severity]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[Union[_builtins.str, AlertRuleState]]: ...
    @state.setter
    def state(self, value: pulumi.Input[Union[_builtins.str, AlertRuleState]]): ...
    @_builtins.property
    @pulumi.getter(name="alertRuleName")
    def alert_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alert_rule_name.setter
    def alert_rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def throttling(self) -> Optional[pulumi.Input[ThrottlingInformationArgs]]: ...
    @throttling.setter
    def throttling(self, value: Optional[pulumi.Input[ThrottlingInformationArgs]]): ...

@pulumi.type_token(...)
class SmartDetectorAlertRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        action_groups: Optional[
            pulumi.Input[
                Union[ActionGroupsInformationArgs, ActionGroupsInformationArgsDict]
            ]
        ] = ...,
        alert_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        detector: Optional[pulumi.Input[Union[DetectorArgs, DetectorArgsDict]]] = ...,
        frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        severity: Optional[pulumi.Input[Union[_builtins.str, Severity]]] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, AlertRuleState]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        throttling: Optional[
            pulumi.Input[
                Union[ThrottlingInformationArgs, ThrottlingInformationArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SmartDetectorAlertRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> SmartDetectorAlertRule: ...
    @_builtins.property
    @pulumi.getter(name="actionGroups")
    def action_groups(
        self,
    ) -> pulumi.Output[outputs.ActionGroupsInformationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def detector(self) -> pulumi.Output[outputs.DetectorResponse]: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def throttling(
        self,
    ) -> pulumi.Output[Optional[outputs.ThrottlingInformationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
