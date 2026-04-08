import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetApplicationPackageResult",
    "AwaitableGetApplicationPackageResult",
    "get_application_package",
    "get_application_package_output",
]

@pulumi.output_type
class GetApplicationPackageResult:
    def __init__(
        __self__,
        azure_api_version=...,
        etag=...,
        format=...,
        id=...,
        last_activation_time=...,
        name=...,
        state=...,
        storage_url=...,
        storage_url_expiry=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastActivationTime")
    def last_activation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageUrl")
    def storage_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageUrlExpiry")
    def storage_url_expiry(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetApplicationPackageResult(GetApplicationPackageResult):
    def __await__(self): ...

def get_application_package(
    account_name: Optional[_builtins.str] = ...,
    application_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    version_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetApplicationPackageResult: ...
def get_application_package_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    application_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    version_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetApplicationPackageResult]: ...
