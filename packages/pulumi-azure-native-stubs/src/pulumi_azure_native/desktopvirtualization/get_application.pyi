import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetApplicationResult",
    "AwaitableGetApplicationResult",
    "get_application",
    "get_application_output",
]

@pulumi.output_type
class GetApplicationResult:
    def __init__(
        __self__,
        application_type=...,
        azure_api_version=...,
        command_line_arguments=...,
        command_line_setting=...,
        description=...,
        file_path=...,
        friendly_name=...,
        icon_content=...,
        icon_hash=...,
        icon_index=...,
        icon_path=...,
        id=...,
        msix_package_application_id=...,
        msix_package_family_name=...,
        name=...,
        object_id=...,
        show_in_portal=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="commandLineArguments")
    def command_line_arguments(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="commandLineSetting")
    def command_line_setting(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iconContent")
    def icon_content(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iconHash")
    def icon_hash(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iconIndex")
    def icon_index(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="iconPath")
    def icon_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="msixPackageApplicationId")
    def msix_package_application_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="msixPackageFamilyName")
    def msix_package_family_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="showInPortal")
    def show_in_portal(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetApplicationResult(GetApplicationResult):
    def __await__(self): ...

def get_application(
    application_group_name: Optional[_builtins.str] = ...,
    application_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetApplicationResult: ...
def get_application_output(
    application_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    application_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetApplicationResult]: ...
