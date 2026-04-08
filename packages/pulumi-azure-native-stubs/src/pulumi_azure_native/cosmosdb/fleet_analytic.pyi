import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FleetAnalyticArgs", "FleetAnalytic"]

@pulumi.input_type
class FleetAnalyticArgs:
    def __init__(
        __self__,
        *,
        fleet_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        fleet_analytics_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_location_type: Optional[
            pulumi.Input[Union[_builtins.str, StorageLocationType]]
        ] = ...,
        storage_location_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fleetName")
    def fleet_name(self) -> pulumi.Input[_builtins.str]: ...
    @fleet_name.setter
    def fleet_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fleetAnalyticsName")
    def fleet_analytics_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fleet_analytics_name.setter
    def fleet_analytics_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageLocationType")
    def storage_location_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StorageLocationType]]]: ...
    @storage_location_type.setter
    def storage_location_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StorageLocationType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageLocationUri")
    def storage_location_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_location_uri.setter
    def storage_location_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:cosmosdb:FleetAnalytic")
class FleetAnalytic(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        fleet_analytics_name: Optional[pulumi.Input[_builtins.str]] = ...,
        fleet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_location_type: Optional[
            pulumi.Input[Union[_builtins.str, StorageLocationType]]
        ] = ...,
        storage_location_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FleetAnalyticArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> FleetAnalytic: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageLocationType")
    def storage_location_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="storageLocationUri")
    def storage_location_uri(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
