import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConnectedEnvironmentsStorageArgs", "ConnectedEnvironmentsStorage"]

@pulumi.input_type
class ConnectedEnvironmentsStorageArgs:
    def __init__(
        __self__,
        *,
        connected_environment_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        properties: Optional[
            pulumi.Input[ConnectedEnvironmentStoragePropertiesArgs]
        ] = ...,
        storage_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectedEnvironmentName")
    def connected_environment_name(self) -> pulumi.Input[_builtins.str]: ...
    @connected_environment_name.setter
    def connected_environment_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[ConnectedEnvironmentStoragePropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[ConnectedEnvironmentStoragePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageName")
    def storage_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_name.setter
    def storage_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:app:ConnectedEnvironmentsStorage")
class ConnectedEnvironmentsStorage(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        connected_environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    ConnectedEnvironmentStoragePropertiesArgs,
                    ConnectedEnvironmentStoragePropertiesArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConnectedEnvironmentsStorageArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ConnectedEnvironmentsStorage: ...
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
    ) -> pulumi.Output[outputs.ConnectedEnvironmentStorageResponseProperties]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
