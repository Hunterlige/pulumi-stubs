import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AzureMonitorConfigurationArgs",
    "AzureMonitorConfigurationArgsDict",
    "ChangeTrackingConfigurationArgs",
    "ChangeTrackingConfigurationArgsDict",
    "DesiredConfigurationArgs",
    "DesiredConfigurationArgsDict",
    "ManagedOpsPropertiesArgs",
    "ManagedOpsPropertiesArgsDict",
]

class AzureMonitorConfigurationArgsDict(TypedDict):
    azure_monitor_workspace_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureMonitorConfigurationArgs:
    def __init__(
        __self__, *, azure_monitor_workspace_id: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorWorkspaceId")
    def azure_monitor_workspace_id(self) -> pulumi.Input[_builtins.str]: ...
    @azure_monitor_workspace_id.setter
    def azure_monitor_workspace_id(self, value: pulumi.Input[_builtins.str]): ...

class ChangeTrackingConfigurationArgsDict(TypedDict):
    log_analytics_workspace_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChangeTrackingConfigurationArgs:
    def __init__(
        __self__, *, log_analytics_workspace_id: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> pulumi.Input[_builtins.str]: ...
    @log_analytics_workspace_id.setter
    def log_analytics_workspace_id(self, value: pulumi.Input[_builtins.str]): ...

class DesiredConfigurationArgsDict(TypedDict):
    azure_monitor_insights: pulumi.Input[AzureMonitorConfigurationArgsDict]
    change_tracking_and_inventory: pulumi.Input[ChangeTrackingConfigurationArgsDict]
    user_assigned_managed_identity_id: pulumi.Input[_builtins.str]
    defender_cspm: NotRequired[
        pulumi.Input[Union[_builtins.str, DesiredEnablementState]]
    ]
    defender_for_servers: NotRequired[
        pulumi.Input[Union[_builtins.str, DesiredEnablementState]]
    ]

@pulumi.input_type
class DesiredConfigurationArgs:
    def __init__(
        __self__,
        *,
        azure_monitor_insights: pulumi.Input[AzureMonitorConfigurationArgs],
        change_tracking_and_inventory: pulumi.Input[ChangeTrackingConfigurationArgs],
        user_assigned_managed_identity_id: pulumi.Input[_builtins.str],
        defender_cspm: Optional[
            pulumi.Input[Union[_builtins.str, DesiredEnablementState]]
        ] = ...,
        defender_for_servers: Optional[
            pulumi.Input[Union[_builtins.str, DesiredEnablementState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorInsights")
    def azure_monitor_insights(self) -> pulumi.Input[AzureMonitorConfigurationArgs]: ...
    @azure_monitor_insights.setter
    def azure_monitor_insights(
        self, value: pulumi.Input[AzureMonitorConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="changeTrackingAndInventory")
    def change_tracking_and_inventory(
        self,
    ) -> pulumi.Input[ChangeTrackingConfigurationArgs]: ...
    @change_tracking_and_inventory.setter
    def change_tracking_and_inventory(
        self, value: pulumi.Input[ChangeTrackingConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedManagedIdentityId")
    def user_assigned_managed_identity_id(self) -> pulumi.Input[_builtins.str]: ...
    @user_assigned_managed_identity_id.setter
    def user_assigned_managed_identity_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defenderCspm")
    def defender_cspm(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DesiredEnablementState]]]: ...
    @defender_cspm.setter
    def defender_cspm(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DesiredEnablementState]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defenderForServers")
    def defender_for_servers(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DesiredEnablementState]]]: ...
    @defender_for_servers.setter
    def defender_for_servers(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DesiredEnablementState]]],
    ): ...

class ManagedOpsPropertiesArgsDict(TypedDict):
    desired_configuration: pulumi.Input[DesiredConfigurationArgsDict]

@pulumi.input_type
class ManagedOpsPropertiesArgs:
    def __init__(
        __self__, *, desired_configuration: pulumi.Input[DesiredConfigurationArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredConfiguration")
    def desired_configuration(self) -> pulumi.Input[DesiredConfigurationArgs]: ...
    @desired_configuration.setter
    def desired_configuration(self, value: pulumi.Input[DesiredConfigurationArgs]): ...
