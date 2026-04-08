import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AdministratorArgs", "Administrator"]

@pulumi.input_type
class AdministratorArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        server_name: pulumi.Input[_builtins.str],
        object_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_name: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_type: Optional[
            pulumi.Input[Union[_builtins.str, PrincipalType]]
        ] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]: ...
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalName")
    def principal_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_name.setter
    def principal_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PrincipalType]]]: ...
    @principal_type.setter
    def principal_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PrincipalType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:dbforpostgresql:Administrator")
class Administrator(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        object_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_name: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_type: Optional[
            pulumi.Input[Union[_builtins.str, PrincipalType]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AdministratorArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Administrator: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="principalName")
    def principal_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
