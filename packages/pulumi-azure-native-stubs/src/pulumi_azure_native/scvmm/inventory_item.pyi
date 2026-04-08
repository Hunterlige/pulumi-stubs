import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["InventoryItemArgs", "InventoryItem"]

@pulumi.input_type
class InventoryItemArgs:
    def __init__(
        __self__,
        *,
        inventory_type: pulumi.Input[Union[_builtins.str, InventoryType]],
        resource_group_name: pulumi.Input[_builtins.str],
        vmm_server_name: pulumi.Input[_builtins.str],
        inventory_item_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inventoryType")
    def inventory_type(self) -> pulumi.Input[Union[_builtins.str, InventoryType]]: ...
    @inventory_type.setter
    def inventory_type(
        self, value: pulumi.Input[Union[_builtins.str, InventoryType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vmmServerName")
    def vmm_server_name(self) -> pulumi.Input[_builtins.str]: ...
    @vmm_server_name.setter
    def vmm_server_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inventoryItemName")
    def inventory_item_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inventory_item_name.setter
    def inventory_item_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:scvmm:InventoryItem")
class InventoryItem(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        inventory_item_name: Optional[pulumi.Input[_builtins.str]] = ...,
        inventory_type: Optional[
            pulumi.Input[Union[_builtins.str, InventoryType]]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        vmm_server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: InventoryItemArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> InventoryItem: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inventoryItemName")
    def inventory_item_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inventoryType")
    def inventory_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="managedResourceId")
    def managed_resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
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
    @pulumi.getter
    def uuid(self) -> pulumi.Output[_builtins.str]: ...
