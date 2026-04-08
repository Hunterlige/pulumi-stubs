import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NotificationHubAuthorizationRuleArgs", "NotificationHubAuthorizationRule"]

@pulumi.input_type
class NotificationHubAuthorizationRuleArgs:
    def __init__(
        __self__,
        *,
        namespace_name: pulumi.Input[_builtins.str],
        notification_hub_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        rights: pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, AccessRights]]]
        ],
        authorization_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_key: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[_builtins.str]: ...
    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="notificationHubName")
    def notification_hub_name(self) -> pulumi.Input[_builtins.str]: ...
    @notification_hub_name.setter
    def notification_hub_name(self, value: pulumi.Input[_builtins.str]): ...
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
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secondary_key.setter
    def secondary_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class NotificationHubAuthorizationRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        authorization_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rights: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessRights]]]]
        ] = ...,
        secondary_key: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NotificationHubAuthorizationRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> NotificationHubAuthorizationRule: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="claimType")
    def claim_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="claimValue")
    def claim_value(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="modifiedTime")
    def modified_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def rights(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
