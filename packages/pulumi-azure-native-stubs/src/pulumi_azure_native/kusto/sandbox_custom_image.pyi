import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SandboxCustomImageArgs", "SandboxCustomImage"]

@pulumi.input_type
class SandboxCustomImageArgs:
    def __init__(
        __self__,
        *,
        cluster_name: pulumi.Input[_builtins.str],
        language: pulumi.Input[Union[_builtins.str, Language]],
        resource_group_name: pulumi.Input[_builtins.str],
        base_image_name: Optional[pulumi.Input[_builtins.str]] = ...,
        language_version: Optional[pulumi.Input[_builtins.str]] = ...,
        requirements_file_content: Optional[pulumi.Input[_builtins.str]] = ...,
        sandbox_custom_image_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def language(self) -> pulumi.Input[Union[_builtins.str, Language]]: ...
    @language.setter
    def language(self, value: pulumi.Input[Union[_builtins.str, Language]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="baseImageName")
    def base_image_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @base_image_name.setter
    def base_image_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="languageVersion")
    def language_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_version.setter
    def language_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requirementsFileContent")
    def requirements_file_content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @requirements_file_content.setter
    def requirements_file_content(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sandboxCustomImageName")
    def sandbox_custom_image_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sandbox_custom_image_name.setter
    def sandbox_custom_image_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("azure-native:kusto:SandboxCustomImage")
class SandboxCustomImage(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        base_image_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        language: Optional[pulumi.Input[Union[_builtins.str, Language]]] = ...,
        language_version: Optional[pulumi.Input[_builtins.str]] = ...,
        requirements_file_content: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sandbox_custom_image_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SandboxCustomImageArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> SandboxCustomImage: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="baseImageName")
    def base_image_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def language(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="languageVersion")
    def language_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requirementsFileContent")
    def requirements_file_content(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
