import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ArchiveVersionArgs", "ArchiveVersion"]

@pulumi.input_type
class ArchiveVersionArgs:
    def __init__(
        __self__,
        *,
        archive_name: pulumi.Input[_builtins.str],
        package_type: pulumi.Input[_builtins.str],
        registry_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        archive_version_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveName")
    def archive_name(self) -> pulumi.Input[_builtins.str]: ...
    @archive_name.setter
    def archive_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="packageType")
    def package_type(self) -> pulumi.Input[_builtins.str]: ...
    @package_type.setter
    def package_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[_builtins.str]: ...
    @registry_name.setter
    def registry_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="archiveVersionName")
    def archive_version_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @archive_version_name.setter
    def archive_version_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:containerregistry:ArchiveVersion")
class ArchiveVersion(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        archive_name: Optional[pulumi.Input[_builtins.str]] = ...,
        archive_version_name: Optional[pulumi.Input[_builtins.str]] = ...,
        package_type: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ArchiveVersionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ArchiveVersion: ...
    @_builtins.property
    @pulumi.getter(name="archiveVersionErrorMessage")
    def archive_version_error_message(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
