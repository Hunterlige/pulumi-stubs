import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetArchifeResult",
    "AwaitableGetArchifeResult",
    "get_archife",
    "get_archife_output",
]

@pulumi.output_type
class GetArchifeResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        package_source=...,
        provisioning_state=...,
        published_version=...,
        repository_endpoint=...,
        repository_endpoint_prefix=...,
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
    @pulumi.getter(name="packageSource")
    def package_source(
        self,
    ) -> Optional[outputs.ArchivePackageSourcePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publishedVersion")
    def published_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryEndpoint")
    def repository_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="repositoryEndpointPrefix")
    def repository_endpoint_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetArchifeResult(GetArchifeResult):
    def __await__(self): ...

def get_archife(
    archive_name: Optional[_builtins.str] = ...,
    package_type: Optional[_builtins.str] = ...,
    registry_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetArchifeResult: ...
def get_archife_output(
    archive_name: Optional[pulumi.Input[_builtins.str]] = ...,
    package_type: Optional[pulumi.Input[_builtins.str]] = ...,
    registry_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetArchifeResult]: ...
