import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AddonArgs", "Addon"]

@pulumi.input_type
class AddonArgs:
    def __init__(
        __self__,
        *,
        private_cloud_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        addon_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    AddonArcPropertiesArgs,
                    AddonHcxPropertiesArgs,
                    AddonSrmPropertiesArgs,
                    AddonVrPropertiesArgs,
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Input[_builtins.str]: ...
    @private_cloud_name.setter
    def private_cloud_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="addonName")
    def addon_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @addon_name.setter
    def addon_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                AddonArcPropertiesArgs,
                AddonHcxPropertiesArgs,
                AddonSrmPropertiesArgs,
                AddonVrPropertiesArgs,
            ]
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    AddonArcPropertiesArgs,
                    AddonHcxPropertiesArgs,
                    AddonSrmPropertiesArgs,
                    AddonVrPropertiesArgs,
                ]
            ]
        ],
    ): ...

@pulumi.type_token("azure-native:avs:Addon")
class Addon(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        addon_name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    Union[AddonArcPropertiesArgs, AddonArcPropertiesArgsDict],
                    Union[AddonHcxPropertiesArgs, AddonHcxPropertiesArgsDict],
                    Union[AddonSrmPropertiesArgs, AddonSrmPropertiesArgsDict],
                    Union[AddonVrPropertiesArgs, AddonVrPropertiesArgsDict],
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AddonArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Addon: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
