import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkspaceSubscriptionArgs", "WorkspaceSubscription"]

@pulumi.input_type
class WorkspaceSubscriptionArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        scope: pulumi.Input[_builtins.str],
        service_name: pulumi.Input[_builtins.str],
        workspace_id: pulumi.Input[_builtins.str],
        allow_tracing: Optional[pulumi.Input[_builtins.bool]] = ...,
        app_type: Optional[pulumi.Input[_builtins.str]] = ...,
        notify: Optional[pulumi.Input[_builtins.bool]] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_key: Optional[pulumi.Input[_builtins.str]] = ...,
        sid: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[SubscriptionState]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowTracing")
    def allow_tracing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_tracing.setter
    def allow_tracing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="appType")
    def app_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_type.setter
    def app_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def notify(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @notify.setter
    def notify(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def sid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sid.setter
    def sid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[SubscriptionState]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[SubscriptionState]]): ...

@pulumi.type_token("azure-native:apimanagement:WorkspaceSubscription")
class WorkspaceSubscription(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_tracing: Optional[pulumi.Input[_builtins.bool]] = ...,
        app_type: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        notify: Optional[pulumi.Input[_builtins.bool]] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_key: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sid: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[SubscriptionState]] = ...,
        workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkspaceSubscriptionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> WorkspaceSubscription: ...
    @_builtins.property
    @pulumi.getter(name="allowTracing")
    def allow_tracing(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationDate")
    def notification_date(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stateComment")
    def state_comment(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
