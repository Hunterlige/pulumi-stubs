import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FleetDatabaseArgs", "FleetDatabase"]

@pulumi.input_type
class FleetDatabaseArgs:
    def __init__(
        __self__,
        *,
        fleet_name: pulumi.Input[_builtins.str],
        fleetspace_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[FleetDatabasePropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fleetName")
    def fleet_name(self) -> pulumi.Input[_builtins.str]: ...
    @fleet_name.setter
    def fleet_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fleetspaceName")
    def fleetspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @fleetspace_name.setter
    def fleetspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[FleetDatabasePropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[FleetDatabasePropertiesArgs]]
    ): ...

@pulumi.type_token("azure-native:databasefleetmanager:FleetDatabase")
class FleetDatabase(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        fleet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        fleetspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[FleetDatabasePropertiesArgs, FleetDatabasePropertiesArgsDict]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FleetDatabaseArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> FleetDatabase: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.FleetDatabasePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
