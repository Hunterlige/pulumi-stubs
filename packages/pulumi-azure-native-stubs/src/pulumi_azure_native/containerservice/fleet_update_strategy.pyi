import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FleetUpdateStrategyArgs", "FleetUpdateStrategy"]

@pulumi.input_type
class FleetUpdateStrategyArgs:
    def __init__(
        __self__,
        *,
        fleet_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        strategy: pulumi.Input[UpdateRunStrategyArgs],
        update_strategy_name: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter
    def strategy(self) -> pulumi.Input[UpdateRunStrategyArgs]: ...
    @strategy.setter
    def strategy(self, value: pulumi.Input[UpdateRunStrategyArgs]): ...
    @_builtins.property
    @pulumi.getter(name="updateStrategyName")
    def update_strategy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_strategy_name.setter
    def update_strategy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:containerservice:FleetUpdateStrategy")
class FleetUpdateStrategy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        fleet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        strategy: Optional[
            pulumi.Input[Union[UpdateRunStrategyArgs, UpdateRunStrategyArgsDict]]
        ] = ...,
        update_strategy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FleetUpdateStrategyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> FleetUpdateStrategy: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def strategy(self) -> pulumi.Output[outputs.UpdateRunStrategyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
