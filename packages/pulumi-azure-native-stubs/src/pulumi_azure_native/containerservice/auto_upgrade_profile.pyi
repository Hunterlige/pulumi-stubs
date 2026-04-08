import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AutoUpgradeProfileArgs", "AutoUpgradeProfile"]

@pulumi.input_type
class AutoUpgradeProfileArgs:
    def __init__(
        __self__,
        *,
        channel: pulumi.Input[Union[_builtins.str, UpgradeChannel]],
        fleet_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        auto_upgrade_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        node_image_selection: Optional[
            pulumi.Input[AutoUpgradeNodeImageSelectionArgs]
        ] = ...,
        update_strategy_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> pulumi.Input[Union[_builtins.str, UpgradeChannel]]: ...
    @channel.setter
    def channel(self, value: pulumi.Input[Union[_builtins.str, UpgradeChannel]]): ...
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
    @pulumi.getter(name="autoUpgradeProfileName")
    def auto_upgrade_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_upgrade_profile_name.setter
    def auto_upgrade_profile_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeImageSelection")
    def node_image_selection(
        self,
    ) -> Optional[pulumi.Input[AutoUpgradeNodeImageSelectionArgs]]: ...
    @node_image_selection.setter
    def node_image_selection(
        self, value: Optional[pulumi.Input[AutoUpgradeNodeImageSelectionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateStrategyId")
    def update_strategy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_strategy_id.setter
    def update_strategy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:containerservice:AutoUpgradeProfile")
class AutoUpgradeProfile(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_upgrade_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        channel: Optional[pulumi.Input[Union[_builtins.str, UpgradeChannel]]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        fleet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_image_selection: Optional[
            pulumi.Input[
                Union[
                    AutoUpgradeNodeImageSelectionArgs,
                    AutoUpgradeNodeImageSelectionArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        update_strategy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AutoUpgradeProfileArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> AutoUpgradeProfile: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeImageSelection")
    def node_image_selection(
        self,
    ) -> pulumi.Output[Optional[outputs.AutoUpgradeNodeImageSelectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateStrategyId")
    def update_strategy_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
