import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CustomImageArgs", "CustomImage"]

@pulumi.input_type
class CustomImageArgs:
    def __init__(
        __self__,
        *,
        definition_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        source: Optional[pulumi.Input[Union[_builtins.str, ImageSource]]] = ...,
        test_base_account_name: pulumi.Input[_builtins.str],
        version_name: pulumi.Input[_builtins.str],
        custom_image_name: Optional[pulumi.Input[_builtins.str]] = ...,
        vhd_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="definitionName")
    def definition_name(self) -> pulumi.Input[_builtins.str]: ...
    @definition_name.setter
    def definition_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[Union[_builtins.str, ImageSource]]: ...
    @source.setter
    def source(self, value: pulumi.Input[Union[_builtins.str, ImageSource]]): ...
    @_builtins.property
    @pulumi.getter(name="testBaseAccountName")
    def test_base_account_name(self) -> pulumi.Input[_builtins.str]: ...
    @test_base_account_name.setter
    def test_base_account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> pulumi.Input[_builtins.str]: ...
    @version_name.setter
    def version_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customImageName")
    def custom_image_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_image_name.setter
    def custom_image_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vhdId")
    def vhd_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vhd_id.setter
    def vhd_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:testbase:CustomImage")
class CustomImage(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        custom_image_name: Optional[pulumi.Input[_builtins.str]] = ...,
        definition_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[Union[_builtins.str, ImageSource]]] = ...,
        test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        version_name: Optional[pulumi.Input[_builtins.str]] = ...,
        vhd_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CustomImageArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> CustomImage: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="definitionName")
    def definition_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osDiskImageSizeInGB")
    def os_disk_image_size_in_gb(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def product(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def release(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="releaseVersionDate")
    def release_version_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validationResults")
    def validation_results(
        self,
    ) -> pulumi.Output[outputs.ImageValidationResultsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vhdFileName")
    def vhd_file_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vhdId")
    def vhd_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
