import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApplicationArgs", "Application"]

@pulumi.input_type
class ApplicationArgs:
    def __init__(
        __self__,
        *,
        application_group_name: pulumi.Input[_builtins.str],
        command_line_setting: pulumi.Input[Union[_builtins.str, CommandLineSetting]],
        resource_group_name: pulumi.Input[_builtins.str],
        application_name: Optional[pulumi.Input[_builtins.str]] = ...,
        application_type: Optional[
            pulumi.Input[Union[_builtins.str, RemoteApplicationType]]
        ] = ...,
        command_line_arguments: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        icon_index: Optional[pulumi.Input[_builtins.int]] = ...,
        icon_path: Optional[pulumi.Input[_builtins.str]] = ...,
        msix_package_application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        msix_package_family_name: Optional[pulumi.Input[_builtins.str]] = ...,
        show_in_portal: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationGroupName")
    def application_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @application_group_name.setter
    def application_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="commandLineSetting")
    def command_line_setting(
        self,
    ) -> pulumi.Input[Union[_builtins.str, CommandLineSetting]]: ...
    @command_line_setting.setter
    def command_line_setting(
        self, value: pulumi.Input[Union[_builtins.str, CommandLineSetting]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_name.setter
    def application_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="applicationType")
    def application_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RemoteApplicationType]]]: ...
    @application_type.setter
    def application_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RemoteApplicationType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="commandLineArguments")
    def command_line_arguments(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @command_line_arguments.setter
    def command_line_arguments(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_path.setter
    def file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iconIndex")
    def icon_index(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @icon_index.setter
    def icon_index(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="iconPath")
    def icon_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @icon_path.setter
    def icon_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="msixPackageApplicationId")
    def msix_package_application_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @msix_package_application_id.setter
    def msix_package_application_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="msixPackageFamilyName")
    def msix_package_family_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @msix_package_family_name.setter
    def msix_package_family_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="showInPortal")
    def show_in_portal(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @show_in_portal.setter
    def show_in_portal(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("azure-native:desktopvirtualization:Application")
class Application(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        application_name: Optional[pulumi.Input[_builtins.str]] = ...,
        application_type: Optional[
            pulumi.Input[Union[_builtins.str, RemoteApplicationType]]
        ] = ...,
        command_line_arguments: Optional[pulumi.Input[_builtins.str]] = ...,
        command_line_setting: Optional[
            pulumi.Input[Union[_builtins.str, CommandLineSetting]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        icon_index: Optional[pulumi.Input[_builtins.int]] = ...,
        icon_path: Optional[pulumi.Input[_builtins.str]] = ...,
        msix_package_application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        msix_package_family_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        show_in_portal: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApplicationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Application: ...
    @_builtins.property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="commandLineArguments")
    def command_line_arguments(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="commandLineSetting")
    def command_line_setting(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="iconContent")
    def icon_content(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iconHash")
    def icon_hash(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iconIndex")
    def icon_index(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="iconPath")
    def icon_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="msixPackageApplicationId")
    def msix_package_application_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="msixPackageFamilyName")
    def msix_package_family_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="showInPortal")
    def show_in_portal(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
