import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RuleArgs", "Rule"]

@pulumi.input_type
class RuleArgs:
    def __init__(
        __self__,
        *,
        namespace_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        subscription_name: pulumi.Input[_builtins.str],
        topic_name: pulumi.Input[_builtins.str],
        action: Optional[pulumi.Input[ActionArgs]] = ...,
        correlation_filter: Optional[pulumi.Input[CorrelationFilterArgs]] = ...,
        filter_type: Optional[pulumi.Input[FilterType]] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sql_filter: Optional[pulumi.Input[SqlFilterArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[_builtins.str]: ...
    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionName")
    def subscription_name(self) -> pulumi.Input[_builtins.str]: ...
    @subscription_name.setter
    def subscription_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> pulumi.Input[_builtins.str]: ...
    @topic_name.setter
    def topic_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[ActionArgs]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[ActionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="correlationFilter")
    def correlation_filter(self) -> Optional[pulumi.Input[CorrelationFilterArgs]]: ...
    @correlation_filter.setter
    def correlation_filter(
        self, value: Optional[pulumi.Input[CorrelationFilterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> Optional[pulumi.Input[FilterType]]: ...
    @filter_type.setter
    def filter_type(self, value: Optional[pulumi.Input[FilterType]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sqlFilter")
    def sql_filter(self) -> Optional[pulumi.Input[SqlFilterArgs]]: ...
    @sql_filter.setter
    def sql_filter(self, value: Optional[pulumi.Input[SqlFilterArgs]]): ...

@pulumi.type_token("azure-native:servicebus:Rule")
class Rule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[Union[ActionArgs, ActionArgsDict]]] = ...,
        correlation_filter: Optional[
            pulumi.Input[Union[CorrelationFilterArgs, CorrelationFilterArgsDict]]
        ] = ...,
        filter_type: Optional[pulumi.Input[FilterType]] = ...,
        namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sql_filter: Optional[
            pulumi.Input[Union[SqlFilterArgs, SqlFilterArgsDict]]
        ] = ...,
        subscription_name: Optional[pulumi.Input[_builtins.str]] = ...,
        topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Rule: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[Optional[outputs.ActionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="correlationFilter")
    def correlation_filter(
        self,
    ) -> pulumi.Output[Optional[outputs.CorrelationFilterResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sqlFilter")
    def sql_filter(self) -> pulumi.Output[Optional[outputs.SqlFilterResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
