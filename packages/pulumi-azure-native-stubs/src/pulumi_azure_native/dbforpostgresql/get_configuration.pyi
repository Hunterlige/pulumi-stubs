import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConfigurationResult",
    "AwaitableGetConfigurationResult",
    "get_configuration",
    "get_configuration_output",
]

@pulumi.output_type
class GetConfigurationResult:
    def __init__(
        __self__,
        allowed_values=...,
        azure_api_version=...,
        data_type=...,
        default_value=...,
        description=...,
        documentation_link=...,
        id=...,
        is_config_pending_restart=...,
        is_dynamic_config=...,
        is_read_only=...,
        name=...,
        source=...,
        system_data=...,
        type=...,
        unit=...,
        value=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="documentationLink")
    def documentation_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isConfigPendingRestart")
    def is_config_pending_restart(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isDynamicConfig")
    def is_dynamic_config(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isReadOnly")
    def is_read_only(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

class AwaitableGetConfigurationResult(GetConfigurationResult):
    def __await__(self): ...

def get_configuration(
    configuration_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConfigurationResult: ...
def get_configuration_output(
    configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConfigurationResult]: ...
