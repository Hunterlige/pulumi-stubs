import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DynamicConfigurationArgs", "DynamicConfiguration"]

@pulumi.input_type
class DynamicConfigurationArgs:
    def __init__(
        __self__,
        *,
        configuration_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        dynamic_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[DynamicConfigurationPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> pulumi.Input[_builtins.str]: ...
    @configuration_name.setter
    def configuration_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dynamicConfigurationName")
    def dynamic_configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dynamic_configuration_name.setter
    def dynamic_configuration_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[DynamicConfigurationPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[DynamicConfigurationPropertiesArgs]]
    ): ...

@pulumi.type_token("azure-native:edge:DynamicConfiguration")
class DynamicConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamic_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    DynamicConfigurationPropertiesArgs,
                    DynamicConfigurationPropertiesArgsDict,
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
        args: DynamicConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> DynamicConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Output[outputs.DynamicConfigurationPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
