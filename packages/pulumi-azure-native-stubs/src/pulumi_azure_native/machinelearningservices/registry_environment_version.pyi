import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RegistryEnvironmentVersionArgs", "RegistryEnvironmentVersion"]

@pulumi.input_type
class RegistryEnvironmentVersionArgs:
    def __init__(
        __self__,
        *,
        environment_name: pulumi.Input[_builtins.str],
        properties: pulumi.Input[EnvironmentVersionPropertiesArgs],
        registry_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Input[_builtins.str]: ...
    @environment_name.setter
    def environment_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[EnvironmentVersionPropertiesArgs]: ...
    @properties.setter
    def properties(self, value: pulumi.Input[EnvironmentVersionPropertiesArgs]): ...
    @_builtins.property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[_builtins.str]: ...
    @registry_name.setter
    def registry_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class RegistryEnvironmentVersion(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    EnvironmentVersionPropertiesArgs,
                    EnvironmentVersionPropertiesArgsDict,
                ]
            ]
        ] = ...,
        registry_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RegistryEnvironmentVersionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> RegistryEnvironmentVersion: ...
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
    ) -> pulumi.Output[outputs.EnvironmentVersionPropertiesResponseV1]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
