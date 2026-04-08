import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDiskPoolResult",
    "AwaitableGetDiskPoolResult",
    "get_disk_pool",
    "get_disk_pool_output",
]

@pulumi.output_type
class GetDiskPoolResult:
    def __init__(
        __self__,
        additional_capabilities=...,
        availability_zones=...,
        azure_api_version=...,
        disks=...,
        id=...,
        location=...,
        managed_by=...,
        managed_by_extended=...,
        name=...,
        provisioning_state=...,
        status=...,
        subnet_id=...,
        system_data=...,
        tags=...,
        tier=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Optional[Sequence[outputs.DiskResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedByExtended")
    def managed_by_extended(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemMetadataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDiskPoolResult(GetDiskPoolResult):
    def __await__(self): ...

def get_disk_pool(
    disk_pool_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDiskPoolResult: ...
def get_disk_pool_output(
    disk_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDiskPoolResult]: ...
