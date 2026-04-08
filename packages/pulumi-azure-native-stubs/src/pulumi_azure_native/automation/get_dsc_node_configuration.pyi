import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDscNodeConfigurationResult",
    "AwaitableGetDscNodeConfigurationResult",
    "get_dsc_node_configuration",
    "get_dsc_node_configuration_output",
]

@pulumi.output_type
class GetDscNodeConfigurationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        configuration=...,
        creation_time=...,
        id=...,
        increment_node_configuration_build=...,
        last_modified_time=...,
        name=...,
        node_count=...,
        source=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.DscConfigurationAssociationPropertyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="incrementNodeConfigurationBuild")
    def increment_node_configuration_build(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDscNodeConfigurationResult(GetDscNodeConfigurationResult):
    def __await__(self): ...

def get_dsc_node_configuration(
    automation_account_name: Optional[_builtins.str] = ...,
    node_configuration_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDscNodeConfigurationResult: ...
def get_dsc_node_configuration_output(
    automation_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    node_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDscNodeConfigurationResult]: ...
