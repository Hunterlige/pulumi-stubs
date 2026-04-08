import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RegistrationArgs", "Registration"]

@pulumi.input_type
class RegistrationArgs:
    def __init__(
        __self__,
        *,
        registration_token: pulumi.Input[_builtins.str],
        resource_group: pulumi.Input[_builtins.str],
        location: Optional[pulumi.Input[Union[_builtins.str, Location]]] = ...,
        registration_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="registrationToken")
    def registration_token(self) -> pulumi.Input[_builtins.str]: ...
    @registration_token.setter
    def registration_token(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group.setter
    def resource_group(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[Union[_builtins.str, Location]]]: ...
    @location.setter
    def location(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Location]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="registrationName")
    def registration_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registration_name.setter
    def registration_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:azurestack:Registration")
class Registration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        location: Optional[pulumi.Input[Union[_builtins.str, Location]]] = ...,
        registration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_token: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RegistrationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Registration: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="billingModel")
    def billing_model(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cloudId")
    def cloud_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
