import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetDiskResult", "AwaitableGetDiskResult", "get_disk", "get_disk_output"]

@pulumi.output_type
class GetDiskResult:
    def __init__(
        __self__,
        azure_api_version=...,
        created_date=...,
        disk_blob_name=...,
        disk_size_gi_b=...,
        disk_type=...,
        disk_uri=...,
        host_caching=...,
        id=...,
        leased_by_lab_vm_id=...,
        location=...,
        managed_disk_id=...,
        name=...,
        provisioning_state=...,
        storage_account_id=...,
        system_data=...,
        tags=...,
        type=...,
        unique_identifier=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="diskBlobName")
    def disk_blob_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGiB")
    def disk_size_gi_b(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskUri")
    def disk_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostCaching")
    def host_caching(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="leasedByLabVmId")
    def leased_by_lab_vm_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedDiskId")
    def managed_disk_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> _builtins.str: ...

class AwaitableGetDiskResult(GetDiskResult):
    def __await__(self): ...

def get_disk(
    expand: Optional[_builtins.str] = ...,
    lab_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    user_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDiskResult: ...
def get_disk_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    lab_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    user_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDiskResult]: ...
