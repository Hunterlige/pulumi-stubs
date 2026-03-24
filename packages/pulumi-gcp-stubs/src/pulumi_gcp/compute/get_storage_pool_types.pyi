import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetStoragePoolTypesResult",
    "AwaitableGetStoragePoolTypesResult",
    "get_storage_pool_types",
    "get_storage_pool_types_output",
]

@pulumi.output_type
class GetStoragePoolTypesResult:
    def __init__(
        __self__,
        creation_timestamp=...,
        deprecateds=...,
        description=...,
        id=...,
        kind=...,
        max_pool_provisioned_capacity_gb=...,
        max_pool_provisioned_iops=...,
        max_pool_provisioned_throughput=...,
        min_pool_provisioned_capacity_gb=...,
        min_pool_provisioned_iops=...,
        min_pool_provisioned_throughput=...,
        name=...,
        project=...,
        self_link=...,
        self_link_with_id=...,
        storage_pool_type=...,
        supported_disk_types=...,
        zone=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def deprecateds(self) -> Sequence[outputs.GetStoragePoolTypesDeprecatedResult]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxPoolProvisionedCapacityGb")
    def max_pool_provisioned_capacity_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxPoolProvisionedIops")
    def max_pool_provisioned_iops(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxPoolProvisionedThroughput")
    def max_pool_provisioned_throughput(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minPoolProvisionedCapacityGb")
    def min_pool_provisioned_capacity_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minPoolProvisionedIops")
    def min_pool_provisioned_iops(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minPoolProvisionedThroughput")
    def min_pool_provisioned_throughput(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storagePoolType")
    def storage_pool_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportedDiskTypes")
    def supported_disk_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...

class AwaitableGetStoragePoolTypesResult(GetStoragePoolTypesResult):
    def __await__(self): ...

def get_storage_pool_types(
    project: Optional[_builtins.str] = ...,
    storage_pool_type: Optional[_builtins.str] = ...,
    zone: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetStoragePoolTypesResult: ...
def get_storage_pool_types_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    storage_pool_type: Optional[pulumi.Input[_builtins.str]] = ...,
    zone: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetStoragePoolTypesResult]: ...
