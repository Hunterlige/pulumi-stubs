import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCapacityPoolSubvolumeResult",
    "AwaitableGetCapacityPoolSubvolumeResult",
    "get_capacity_pool_subvolume",
    "get_capacity_pool_subvolume_output",
]

@pulumi.output_type
class GetCapacityPoolSubvolumeResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        parent_path=...,
        path=...,
        provisioning_state=...,
        size=...,
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
    @pulumi.getter(name="parentPath")
    def parent_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetCapacityPoolSubvolumeResult(GetCapacityPoolSubvolumeResult):
    def __await__(self): ...

def get_capacity_pool_subvolume(
    account_name: Optional[_builtins.str] = ...,
    pool_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    subvolume_name: Optional[_builtins.str] = ...,
    volume_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCapacityPoolSubvolumeResult: ...
def get_capacity_pool_subvolume_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    subvolume_name: Optional[pulumi.Input[_builtins.str]] = ...,
    volume_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCapacityPoolSubvolumeResult]: ...
