import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConfigurationAssignmentParentArgs", "ConfigurationAssignmentParent"]

@pulumi.input_type
class ConfigurationAssignmentParentArgs:
    def __init__(
        __self__,
        *,
        provider_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        resource_name: pulumi.Input[_builtins.str],
        resource_parent_name: pulumi.Input[_builtins.str],
        resource_parent_type: pulumi.Input[_builtins.str],
        resource_type: pulumi.Input[_builtins.str],
        configuration_assignment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[
            pulumi.Input[ConfigurationAssignmentFilterPropertiesArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_configuration_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> pulumi.Input[_builtins.str]: ...
    @provider_name.setter
    def provider_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceParentName")
    def resource_parent_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_parent_name.setter
    def resource_parent_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceParentType")
    def resource_parent_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_parent_type.setter
    def resource_parent_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="configurationAssignmentName")
    def configuration_assignment_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configuration_assignment_name.setter
    def configuration_assignment_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(
        self,
    ) -> Optional[pulumi.Input[ConfigurationAssignmentFilterPropertiesArgs]]: ...
    @filter.setter
    def filter(
        self, value: Optional[pulumi.Input[ConfigurationAssignmentFilterPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceConfigurationId")
    def maintenance_configuration_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_configuration_id.setter
    def maintenance_configuration_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ConfigurationAssignmentParent(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        configuration_assignment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[
            pulumi.Input[
                Union[
                    ConfigurationAssignmentFilterPropertiesArgs,
                    ConfigurationAssignmentFilterPropertiesArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_configuration_id: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_name_: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_parent_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_parent_type: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConfigurationAssignmentParentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ConfigurationAssignmentParent: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filter(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ConfigurationAssignmentFilterPropertiesResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceConfigurationId")
    def maintenance_configuration_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
