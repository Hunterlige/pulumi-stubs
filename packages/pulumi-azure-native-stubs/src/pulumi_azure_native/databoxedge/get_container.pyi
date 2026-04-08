import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetContainerResult",
    "AwaitableGetContainerResult",
    "get_container",
    "get_container_output",
]

@pulumi.output_type
class GetContainerResult:
    def __init__(
        __self__,
        azure_api_version=...,
        container_status=...,
        created_date_time=...,
        data_format=...,
        id=...,
        name=...,
        refresh_details=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="containerStatus")
    def container_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdDateTime")
    def created_date_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="refreshDetails")
    def refresh_details(self) -> outputs.RefreshDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetContainerResult(GetContainerResult):
    def __await__(self): ...

def get_container(
    container_name: Optional[_builtins.str] = ...,
    device_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    storage_account_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetContainerResult: ...
def get_container_output(
    container_name: Optional[pulumi.Input[_builtins.str]] = ...,
    device_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    storage_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetContainerResult]: ...
