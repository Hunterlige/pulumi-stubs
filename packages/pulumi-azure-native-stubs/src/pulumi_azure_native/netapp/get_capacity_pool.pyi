import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCapacityPoolResult",
    "AwaitableGetCapacityPoolResult",
    "get_capacity_pool",
    "get_capacity_pool_output",
]

@pulumi.output_type
class GetCapacityPoolResult:
    def __init__(
        __self__,
        azure_api_version=...,
        cool_access=...,
        encryption_type=...,
        etag=...,
        id=...,
        location=...,
        name=...,
        pool_id=...,
        provisioning_state=...,
        qos_type=...,
        service_level=...,
        size=...,
        system_data=...,
        tags=...,
        total_throughput_mibps=...,
        type=...,
        utilized_throughput_mibps=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="coolAccess")
    def cool_access(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="poolId")
    def pool_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="qosType")
    def qos_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceLevel")
    def service_level(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="totalThroughputMibps")
    def total_throughput_mibps(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="utilizedThroughputMibps")
    def utilized_throughput_mibps(self) -> _builtins.float: ...

class AwaitableGetCapacityPoolResult(GetCapacityPoolResult):
    def __await__(self): ...

def get_capacity_pool(
    account_name: Optional[_builtins.str] = ...,
    pool_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCapacityPoolResult: ...
def get_capacity_pool_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCapacityPoolResult]: ...
