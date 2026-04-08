import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AzureMonitorWorkspacePropertiesArgs",
    "AzureMonitorWorkspacePropertiesArgsDict",
    "ConfigurationProfileResourcePropertiesArgs",
    "ConfigurationProfileResourcePropertiesArgsDict",
    "NotificationSettingsArgs",
    "NotificationSettingsArgsDict",
    "ResourceIdentityArgs",
    "ResourceIdentityArgsDict",
]

class AzureMonitorWorkspacePropertiesArgsDict(TypedDict):
    include_change_details: NotRequired[
        pulumi.Input[Union[_builtins.str, ChangeDetailsMode]]
    ]
    workspace_id: NotRequired[pulumi.Input[_builtins.str]]
    workspace_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureMonitorWorkspacePropertiesArgs:
    def __init__(
        __self__,
        *,
        include_change_details: Optional[
            pulumi.Input[Union[_builtins.str, ChangeDetailsMode]]
        ] = ...,
        workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includeChangeDetails")
    def include_change_details(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ChangeDetailsMode]]]: ...
    @include_change_details.setter
    def include_change_details(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ChangeDetailsMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_resource_id.setter
    def workspace_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConfigurationProfileResourcePropertiesArgsDict(TypedDict):
    notifications: NotRequired[pulumi.Input[NotificationSettingsArgsDict]]

@pulumi.input_type
class ConfigurationProfileResourcePropertiesArgs:
    def __init__(
        __self__,
        *,
        notifications: Optional[pulumi.Input[NotificationSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> Optional[pulumi.Input[NotificationSettingsArgs]]: ...
    @notifications.setter
    def notifications(
        self, value: Optional[pulumi.Input[NotificationSettingsArgs]]
    ): ...

class NotificationSettingsArgsDict(TypedDict):
    activation_state: NotRequired[
        pulumi.Input[Union[_builtins.str, NotificationsState]]
    ]
    azure_monitor_workspace_properties: NotRequired[
        pulumi.Input[AzureMonitorWorkspacePropertiesArgsDict]
    ]

@pulumi.input_type
class NotificationSettingsArgs:
    def __init__(
        __self__,
        *,
        activation_state: Optional[
            pulumi.Input[Union[_builtins.str, NotificationsState]]
        ] = ...,
        azure_monitor_workspace_properties: Optional[
            pulumi.Input[AzureMonitorWorkspacePropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activationState")
    def activation_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NotificationsState]]]: ...
    @activation_state.setter
    def activation_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NotificationsState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorWorkspaceProperties")
    def azure_monitor_workspace_properties(
        self,
    ) -> Optional[pulumi.Input[AzureMonitorWorkspacePropertiesArgs]]: ...
    @azure_monitor_workspace_properties.setter
    def azure_monitor_workspace_properties(
        self, value: Optional[pulumi.Input[AzureMonitorWorkspacePropertiesArgs]]
    ): ...

class ResourceIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, ManagedIdentityTypes]]]

@pulumi.input_type
class ResourceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityTypes]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityTypes]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityTypes]]]
    ): ...
