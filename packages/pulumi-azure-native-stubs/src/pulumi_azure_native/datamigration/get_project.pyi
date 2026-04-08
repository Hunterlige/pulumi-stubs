import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetProjectResult",
    "AwaitableGetProjectResult",
    "get_project",
    "get_project_output",
]

@pulumi.output_type
class GetProjectResult:
    def __init__(
        __self__,
        azure_api_version=...,
        azure_authentication_info=...,
        creation_time=...,
        databases_info=...,
        etag=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        source_connection_info=...,
        source_platform=...,
        system_data=...,
        tags=...,
        target_connection_info=...,
        target_platform=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureAuthenticationInfo")
    def azure_authentication_info(
        self,
    ) -> Optional[outputs.AzureActiveDirectoryAppResponse]: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databasesInfo")
    def databases_info(self) -> Optional[Sequence[outputs.DatabaseInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="sourcePlatform")
    def source_platform(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="targetPlatform")
    def target_platform(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetProjectResult(GetProjectResult):
    def __await__(self): ...

def get_project(
    group_name: Optional[_builtins.str] = ...,
    project_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetProjectResult: ...
def get_project_output(
    group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    project_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetProjectResult]: ...
