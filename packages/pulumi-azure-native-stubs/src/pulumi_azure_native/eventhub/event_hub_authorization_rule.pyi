import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EventHubAuthorizationRuleArgs", "EventHubAuthorizationRule"]

@pulumi.input_type
class EventHubAuthorizationRuleArgs:
    def __init__(
        __self__,
        *,
        event_hub_name: pulumi.Input[_builtins.str],
        namespace_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        rights: pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, AccessRights]]]
        ],
        authorization_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> pulumi.Input[_builtins.str]: ...
    @event_hub_name.setter
    def event_hub_name(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter
    def rights(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessRights]]]]: ...
    @rights.setter
    def rights(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessRights]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="authorizationRuleName")
    def authorization_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authorization_rule_name.setter
    def authorization_rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:eventhub:EventHubAuthorizationRule")
class EventHubAuthorizationRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        authorization_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        event_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rights: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessRights]]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EventHubAuthorizationRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> EventHubAuthorizationRule: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rights(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
