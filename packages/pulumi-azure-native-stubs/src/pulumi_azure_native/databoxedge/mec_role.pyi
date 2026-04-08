import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MECRoleArgs", "MECRole"]

@pulumi.input_type
class MECRoleArgs:
    def __init__(
        __self__,
        *,
        device_name: pulumi.Input[_builtins.str],
        kind: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        role_status: pulumi.Input[Union[_builtins.str, RoleStatus]],
        connection_string: Optional[pulumi.Input[AsymmetricEncryptedSecretArgs]] = ...,
        controller_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_unique_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]: ...
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleStatus")
    def role_status(self) -> pulumi.Input[Union[_builtins.str, RoleStatus]]: ...
    @role_status.setter
    def role_status(self, value: pulumi.Input[Union[_builtins.str, RoleStatus]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(
        self,
    ) -> Optional[pulumi.Input[AsymmetricEncryptedSecretArgs]]: ...
    @connection_string.setter
    def connection_string(
        self, value: Optional[pulumi.Input[AsymmetricEncryptedSecretArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="controllerEndpoint")
    def controller_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @controller_endpoint.setter
    def controller_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceUniqueId")
    def resource_unique_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_unique_id.setter
    def resource_unique_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:databoxedge:MECRole")
class MECRole(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        connection_string: Optional[
            pulumi.Input[
                Union[AsymmetricEncryptedSecretArgs, AsymmetricEncryptedSecretArgsDict]
            ]
        ] = ...,
        controller_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_unique_id: Optional[pulumi.Input[_builtins.str]] = ...,
        role_status: Optional[pulumi.Input[Union[_builtins.str, RoleStatus]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MECRoleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> MECRole: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(
        self,
    ) -> pulumi.Output[Optional[outputs.AsymmetricEncryptedSecretResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="controllerEndpoint")
    def controller_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceUniqueId")
    def resource_unique_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="roleStatus")
    def role_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
