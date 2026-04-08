import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConsoleArgs", "Console"]

@pulumi.input_type
class ConsoleArgs:
    def __init__(
        __self__,
        *,
        properties: pulumi.Input[ConsoleCreatePropertiesArgs],
        console_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[ConsoleCreatePropertiesArgs]: ...
    @properties.setter
    def properties(self, value: pulumi.Input[ConsoleCreatePropertiesArgs]): ...
    @_builtins.property
    @pulumi.getter(name="consoleName")
    def console_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @console_name.setter
    def console_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:portal:Console")
class Console(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        console_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[ConsoleCreatePropertiesArgs, ConsoleCreatePropertiesArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConsoleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Console: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.ConsolePropertiesResponse]: ...
