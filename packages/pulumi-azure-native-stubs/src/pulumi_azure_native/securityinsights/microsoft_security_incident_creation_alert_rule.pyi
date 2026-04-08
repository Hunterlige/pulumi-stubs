import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "MicrosoftSecurityIncidentCreationAlertRuleArgs",
    "MicrosoftSecurityIncidentCreationAlertRule",
]

@pulumi.input_type
class MicrosoftSecurityIncidentCreationAlertRuleArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        enabled: pulumi.Input[_builtins.bool],
        kind: pulumi.Input[_builtins.str],
        product_filter: pulumi.Input[
            Union[_builtins.str, MicrosoftSecurityProductName]
        ],
        resource_group_name: pulumi.Input[_builtins.str],
        workspace_name: pulumi.Input[_builtins.str],
        alert_rule_template_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_names_exclude_filter: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        display_names_filter: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        severities_filter: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AlertSeverity]]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="productFilter")
    def product_filter(
        self,
    ) -> pulumi.Input[Union[_builtins.str, MicrosoftSecurityProductName]]: ...
    @product_filter.setter
    def product_filter(
        self, value: pulumi.Input[Union[_builtins.str, MicrosoftSecurityProductName]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="alertRuleTemplateName")
    def alert_rule_template_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alert_rule_template_name.setter
    def alert_rule_template_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayNamesExcludeFilter")
    def display_names_exclude_filter(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @display_names_exclude_filter.setter
    def display_names_exclude_filter(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayNamesFilter")
    def display_names_filter(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @display_names_filter.setter
    def display_names_filter(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_id.setter
    def rule_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="severitiesFilter")
    def severities_filter(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AlertSeverity]]]]
    ]: ...
    @severities_filter.setter
    def severities_filter(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AlertSeverity]]]]
        ],
    ): ...

@pulumi.type_token(...)
class MicrosoftSecurityIncidentCreationAlertRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        alert_rule_template_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        display_names_exclude_filter: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        display_names_filter: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        product_filter: Optional[
            pulumi.Input[Union[_builtins.str, MicrosoftSecurityProductName]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        severities_filter: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AlertSeverity]]]]
        ] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MicrosoftSecurityIncidentCreationAlertRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> MicrosoftSecurityIncidentCreationAlertRule: ...
    @_builtins.property
    @pulumi.getter(name="alertRuleTemplateName")
    def alert_rule_template_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
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
    @pulumi.getter(name="displayNamesExcludeFilter")
    def display_names_exclude_filter(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="displayNamesFilter")
    def display_names_filter(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedUtc")
    def last_modified_utc(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="productFilter")
    def product_filter(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="severitiesFilter")
    def severities_filter(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
