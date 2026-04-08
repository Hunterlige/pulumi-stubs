import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCapacityPoolBucketResult",
    "AwaitableGetCapacityPoolBucketResult",
    "get_capacity_pool_bucket",
    "get_capacity_pool_bucket_output",
]

@pulumi.output_type
class GetCapacityPoolBucketResult:
    def __init__(
        __self__,
        azure_api_version=...,
        file_system_user=...,
        id=...,
        name=...,
        path=...,
        provisioning_state=...,
        server=...,
        status=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemUser")
    def file_system_user(self) -> Optional[outputs.FileSystemUserResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> Optional[outputs.BucketServerPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetCapacityPoolBucketResult(GetCapacityPoolBucketResult):
    def __await__(self): ...

def get_capacity_pool_bucket(
    account_name: Optional[_builtins.str] = ...,
    bucket_name: Optional[_builtins.str] = ...,
    pool_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    volume_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCapacityPoolBucketResult: ...
def get_capacity_pool_bucket_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
    pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    volume_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCapacityPoolBucketResult]: ...
