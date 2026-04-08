import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["StorageAccountArgs", "StorageAccount"]

@pulumi.input_type
class StorageAccountArgs:
    def __init__(
        __self__,
        *,
        data_policy: pulumi.Input[Union[_builtins.str, DataPolicy]],
        device_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_credential_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_status: Optional[
            pulumi.Input[Union[_builtins.str, StorageAccountStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataPolicy")
    def data_policy(self) -> pulumi.Input[Union[_builtins.str, DataPolicy]]: ...
    @data_policy.setter
    def data_policy(self, value: pulumi.Input[Union[_builtins.str, DataPolicy]]): ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]: ...
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountCredentialId")
    def storage_account_credential_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_credential_id.setter
    def storage_account_credential_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_name.setter
    def storage_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountStatus")
    def storage_account_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StorageAccountStatus]]]: ...
    @storage_account_status.setter
    def storage_account_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StorageAccountStatus]]]
    ): ...

@pulumi.type_token("azure-native:databoxedge:StorageAccount")
class StorageAccount(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        data_policy: Optional[pulumi.Input[Union[_builtins.str, DataPolicy]]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_credential_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_status: Optional[
            pulumi.Input[Union[_builtins.str, StorageAccountStatus]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: StorageAccountArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> StorageAccount: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="blobEndpoint")
    def blob_endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="containerCount")
    def container_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dataPolicy")
    def data_policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountCredentialId")
    def storage_account_credential_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountStatus")
    def storage_account_status(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
