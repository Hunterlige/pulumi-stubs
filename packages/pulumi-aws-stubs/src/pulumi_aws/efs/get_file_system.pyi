import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFileSystemResult",
    "AwaitableGetFileSystemResult",
    "get_file_system",
    "get_file_system_output",
]

@pulumi.output_type
class GetFileSystemResult:
    def __init__(
        __self__,
        arn=...,
        availability_zone_id=...,
        availability_zone_name=...,
        creation_token=...,
        dns_name=...,
        encrypted=...,
        file_system_id=...,
        id=...,
        kms_key_id=...,
        lifecycle_policies=...,
        name=...,
        performance_mode=...,
        protections=...,
        provisioned_throughput_in_mibps=...,
        region=...,
        size_in_bytes=...,
        tags=...,
        throughput_mode=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneName")
    def availability_zone_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationToken")
    def creation_token(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lifecyclePolicies")
    def lifecycle_policies(
        self,
    ) -> Sequence[outputs.GetFileSystemLifecyclePolicyResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="performanceMode")
    def performance_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protections(self) -> Sequence[outputs.GetFileSystemProtectionResult]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughputInMibps")
    def provisioned_throughput_in_mibps(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="throughputMode")
    def throughput_mode(self) -> _builtins.str: ...

class AwaitableGetFileSystemResult(GetFileSystemResult):
    def __await__(self): ...

def get_file_system(
    creation_token: Optional[_builtins.str] = ...,
    file_system_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFileSystemResult: ...
def get_file_system_output(
    creation_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    file_system_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFileSystemResult]: ...
