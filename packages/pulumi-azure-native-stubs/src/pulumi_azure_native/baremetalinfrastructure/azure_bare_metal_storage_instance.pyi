import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AzureBareMetalStorageInstanceArgs", "AzureBareMetalStorageInstance"]

@pulumi.input_type
class AzureBareMetalStorageInstanceArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        azure_bare_metal_storage_instance_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        azure_bare_metal_storage_instance_unique_identifier: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        identity: Optional[
            pulumi.Input[AzureBareMetalStorageInstanceIdentityArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_properties: Optional[pulumi.Input[StoragePropertiesArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="azureBareMetalStorageInstanceName")
    def azure_bare_metal_storage_instance_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_bare_metal_storage_instance_name.setter
    def azure_bare_metal_storage_instance_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureBareMetalStorageInstanceUniqueIdentifier")
    def azure_bare_metal_storage_instance_unique_identifier(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_bare_metal_storage_instance_unique_identifier.setter
    def azure_bare_metal_storage_instance_unique_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[pulumi.Input[AzureBareMetalStorageInstanceIdentityArgs]]: ...
    @identity.setter
    def identity(
        self, value: Optional[pulumi.Input[AzureBareMetalStorageInstanceIdentityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageProperties")
    def storage_properties(self) -> Optional[pulumi.Input[StoragePropertiesArgs]]: ...
    @storage_properties.setter
    def storage_properties(
        self, value: Optional[pulumi.Input[StoragePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class AzureBareMetalStorageInstance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        azure_bare_metal_storage_instance_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        azure_bare_metal_storage_instance_unique_identifier: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        identity: Optional[
            pulumi.Input[
                Union[
                    AzureBareMetalStorageInstanceIdentityArgs,
                    AzureBareMetalStorageInstanceIdentityArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_properties: Optional[
            pulumi.Input[Union[StoragePropertiesArgs, StoragePropertiesArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AzureBareMetalStorageInstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> AzureBareMetalStorageInstance: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureBareMetalStorageInstanceUniqueIdentifier")
    def azure_bare_metal_storage_instance_unique_identifier(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AzureBareMetalStorageInstanceIdentityResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageProperties")
    def storage_properties(
        self,
    ) -> pulumi.Output[Optional[outputs.StoragePropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
