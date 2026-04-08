import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IntegrationServiceEnvironmentArgs", "IntegrationServiceEnvironment"]

@pulumi.input_type
class IntegrationServiceEnvironmentArgs:
    def __init__(
        __self__,
        *,
        resource_group: pulumi.Input[_builtins.str],
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        integration_service_environment_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[IntegrationServiceEnvironmentPropertiesArgs]
        ] = ...,
        sku: Optional[pulumi.Input[IntegrationServiceEnvironmentSkuArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group.setter
    def resource_group(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="integrationServiceEnvironmentName")
    def integration_service_environment_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integration_service_environment_name.setter
    def integration_service_environment_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[IntegrationServiceEnvironmentPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[IntegrationServiceEnvironmentPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[IntegrationServiceEnvironmentSkuArgs]]: ...
    @sku.setter
    def sku(
        self, value: Optional[pulumi.Input[IntegrationServiceEnvironmentSkuArgs]]
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

@pulumi.type_token("azure-native:logic:IntegrationServiceEnvironment")
class IntegrationServiceEnvironment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        integration_service_environment_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    IntegrationServiceEnvironmentPropertiesArgs,
                    IntegrationServiceEnvironmentPropertiesArgsDict,
                ]
            ]
        ] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[
            pulumi.Input[
                Union[
                    IntegrationServiceEnvironmentSkuArgs,
                    IntegrationServiceEnvironmentSkuArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IntegrationServiceEnvironmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> IntegrationServiceEnvironment: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Output[outputs.IntegrationServiceEnvironmentPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def sku(
        self,
    ) -> pulumi.Output[Optional[outputs.IntegrationServiceEnvironmentSkuResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
