import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApplianceArgs", "Appliance"]

@pulumi.input_type
class ApplianceArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        distro: Optional[pulumi.Input[Union[_builtins.str, Distro]]] = ...,
        identity: Optional[pulumi.Input[IdentityArgs]] = ...,
        infrastructure_config: Optional[
            pulumi.Input[AppliancePropertiesInfrastructureConfigArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def distro(self) -> Optional[pulumi.Input[Union[_builtins.str, Distro]]]: ...
    @distro.setter
    def distro(self, value: Optional[pulumi.Input[Union[_builtins.str, Distro]]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="infrastructureConfig")
    def infrastructure_config(
        self,
    ) -> Optional[pulumi.Input[AppliancePropertiesInfrastructureConfigArgs]]: ...
    @infrastructure_config.setter
    def infrastructure_config(
        self, value: Optional[pulumi.Input[AppliancePropertiesInfrastructureConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:resourceconnector:Appliance")
class Appliance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        distro: Optional[pulumi.Input[Union[_builtins.str, Distro]]] = ...,
        identity: Optional[pulumi.Input[Union[IdentityArgs, IdentityArgsDict]]] = ...,
        infrastructure_config: Optional[
            pulumi.Input[
                Union[
                    AppliancePropertiesInfrastructureConfigArgs,
                    AppliancePropertiesInfrastructureConfigArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_name_: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApplianceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Appliance: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def distro(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureConfig")
    def infrastructure_config(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AppliancePropertiesInfrastructureConfigResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
