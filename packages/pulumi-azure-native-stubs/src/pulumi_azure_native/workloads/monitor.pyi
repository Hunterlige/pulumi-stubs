import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MonitorArgs", "Monitor"]

@pulumi.input_type
class MonitorArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        app_location: Optional[pulumi.Input[_builtins.str]] = ...,
        app_service_plan_configuration: Optional[
            pulumi.Input[AppServicePlanConfigurationArgs]
        ] = ...,
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_analytics_workspace_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_resource_group_configuration: Optional[
            pulumi.Input[ManagedResourceGroupConfigurationArgs]
        ] = ...,
        monitor_name: Optional[pulumi.Input[_builtins.str]] = ...,
        monitor_subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_preference: Optional[
            pulumi.Input[Union[_builtins.str, RoutingPreference]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        zone_redundancy_preference: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appLocation")
    def app_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_location.setter
    def app_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="appServicePlanConfiguration")
    def app_service_plan_configuration(
        self,
    ) -> Optional[pulumi.Input[AppServicePlanConfigurationArgs]]: ...
    @app_service_plan_configuration.setter
    def app_service_plan_configuration(
        self, value: Optional[pulumi.Input[AppServicePlanConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logAnalyticsWorkspaceArmId")
    def log_analytics_workspace_arm_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_analytics_workspace_arm_id.setter
    def log_analytics_workspace_arm_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(
        self,
    ) -> Optional[pulumi.Input[ManagedResourceGroupConfigurationArgs]]: ...
    @managed_resource_group_configuration.setter
    def managed_resource_group_configuration(
        self, value: Optional[pulumi.Input[ManagedResourceGroupConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="monitorName")
    def monitor_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @monitor_name.setter
    def monitor_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="monitorSubnet")
    def monitor_subnet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @monitor_subnet.setter
    def monitor_subnet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingPreference")
    def routing_preference(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RoutingPreference]]]: ...
    @routing_preference.setter
    def routing_preference(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RoutingPreference]]]
    ): ...
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
    @pulumi.getter(name="zoneRedundancyPreference")
    def zone_redundancy_preference(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone_redundancy_preference.setter
    def zone_redundancy_preference(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("azure-native:workloads:Monitor")
class Monitor(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_location: Optional[pulumi.Input[_builtins.str]] = ...,
        app_service_plan_configuration: Optional[
            pulumi.Input[
                Union[
                    AppServicePlanConfigurationArgs, AppServicePlanConfigurationArgsDict
                ]
            ]
        ] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_analytics_workspace_arm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_resource_group_configuration: Optional[
            pulumi.Input[
                Union[
                    ManagedResourceGroupConfigurationArgs,
                    ManagedResourceGroupConfigurationArgsDict,
                ]
            ]
        ] = ...,
        monitor_name: Optional[pulumi.Input[_builtins.str]] = ...,
        monitor_subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_preference: Optional[
            pulumi.Input[Union[_builtins.str, RoutingPreference]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        zone_redundancy_preference: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MonitorArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Monitor: ...
    @_builtins.property
    @pulumi.getter(name="appLocation")
    def app_location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="appServicePlanConfiguration")
    def app_service_plan_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.AppServicePlanConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> pulumi.Output[outputs.ErrorDetailResponse]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logAnalyticsWorkspaceArmId")
    def log_analytics_workspace_arm_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedResourceGroupConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="monitorSubnet")
    def monitor_subnet(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="msiArmId")
    def msi_arm_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingPreference")
    def routing_preference(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountArmId")
    def storage_account_arm_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zoneRedundancyPreference")
    def zone_redundancy_preference(self) -> pulumi.Output[Optional[_builtins.str]]: ...
