import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ExtensionAzureMonitorStatusArgs", "ExtensionAzureMonitorStatus"]

@pulumi.input_type
class ExtensionAzureMonitorStatusArgs:
    def __init__(
        __self__,
        *,
        cluster_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        primary_key: Optional[pulumi.Input[_builtins.str]] = ...,
        selected_configurations: Optional[
            pulumi.Input[AzureMonitorSelectedConfigurationsArgs]
        ] = ...,
        workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selectedConfigurations")
    def selected_configurations(
        self,
    ) -> Optional[pulumi.Input[AzureMonitorSelectedConfigurationsArgs]]: ...
    @selected_configurations.setter
    def selected_configurations(
        self, value: Optional[pulumi.Input[AzureMonitorSelectedConfigurationsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:hdinsight:ExtensionAzureMonitorStatus")
class ExtensionAzureMonitorStatus(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        selected_configurations: Optional[
            pulumi.Input[
                Union[
                    AzureMonitorSelectedConfigurationsArgs,
                    AzureMonitorSelectedConfigurationsArgsDict,
                ]
            ]
        ] = ...,
        workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ExtensionAzureMonitorStatusArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ExtensionAzureMonitorStatus: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterMonitoringEnabled")
    def cluster_monitoring_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="selectedConfigurations")
    def selected_configurations(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AzureMonitorSelectedConfigurationsResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
