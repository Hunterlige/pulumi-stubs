import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FavoriteProcessArgs", "FavoriteProcess"]

@pulumi.input_type
class FavoriteProcessArgs:
    def __init__(
        __self__,
        *,
        actual_process_name: pulumi.Input[_builtins.str],
        package_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        test_base_account_name: pulumi.Input[_builtins.str],
        favorite_process_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actualProcessName")
    def actual_process_name(self) -> pulumi.Input[_builtins.str]: ...
    @actual_process_name.setter
    def actual_process_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> pulumi.Input[_builtins.str]: ...
    @package_name.setter
    def package_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="testBaseAccountName")
    def test_base_account_name(self) -> pulumi.Input[_builtins.str]: ...
    @test_base_account_name.setter
    def test_base_account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="favoriteProcessResourceName")
    def favorite_process_resource_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @favorite_process_resource_name.setter
    def favorite_process_resource_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("azure-native:testbase:FavoriteProcess")
class FavoriteProcess(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        actual_process_name: Optional[pulumi.Input[_builtins.str]] = ...,
        favorite_process_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        package_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FavoriteProcessArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> FavoriteProcess: ...
    @_builtins.property
    @pulumi.getter(name="actualProcessName")
    def actual_process_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
