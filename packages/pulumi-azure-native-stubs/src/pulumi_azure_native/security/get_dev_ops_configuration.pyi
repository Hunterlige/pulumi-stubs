import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDevOpsConfigurationResult",
    "AwaitableGetDevOpsConfigurationResult",
    "get_dev_ops_configuration",
    "get_dev_ops_configuration_output",
]

@pulumi.output_type
class GetDevOpsConfigurationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        properties=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.DevOpsConfigurationPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDevOpsConfigurationResult(GetDevOpsConfigurationResult):
    def __await__(self): ...

def get_dev_ops_configuration(
    resource_group_name: Optional[_builtins.str] = ...,
    security_connector_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDevOpsConfigurationResult: ...
def get_dev_ops_configuration_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    security_connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDevOpsConfigurationResult]: ...
