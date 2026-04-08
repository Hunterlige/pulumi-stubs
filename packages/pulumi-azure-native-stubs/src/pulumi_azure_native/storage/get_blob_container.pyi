import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBlobContainerResult",
    "AwaitableGetBlobContainerResult",
    "get_blob_container",
    "get_blob_container_output",
]

@pulumi.output_type
class GetBlobContainerResult:
    def __init__(
        __self__,
        azure_api_version=...,
        default_encryption_scope=...,
        deleted=...,
        deleted_time=...,
        deny_encryption_scope_override=...,
        enable_nfs_v3_all_squash=...,
        enable_nfs_v3_root_squash=...,
        etag=...,
        has_immutability_policy=...,
        has_legal_hold=...,
        id=...,
        immutability_policy=...,
        immutable_storage_with_versioning=...,
        last_modified_time=...,
        lease_duration=...,
        lease_state=...,
        lease_status=...,
        legal_hold=...,
        metadata=...,
        name=...,
        public_access=...,
        remaining_retention_days=...,
        type=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultEncryptionScope")
    def default_encryption_scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="deletedTime")
    def deleted_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="denyEncryptionScopeOverride")
    def deny_encryption_scope_override(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableNfsV3AllSquash")
    def enable_nfs_v3_all_squash(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableNfsV3RootSquash")
    def enable_nfs_v3_root_squash(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hasImmutabilityPolicy")
    def has_immutability_policy(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="hasLegalHold")
    def has_legal_hold(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="immutabilityPolicy")
    def immutability_policy(self) -> outputs.ImmutabilityPolicyPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="immutableStorageWithVersioning")
    def immutable_storage_with_versioning(
        self,
    ) -> Optional[outputs.ImmutableStorageWithVersioningResponse]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="leaseDuration")
    def lease_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="leaseState")
    def lease_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="leaseStatus")
    def lease_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="legalHold")
    def legal_hold(self) -> outputs.LegalHoldPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicAccess")
    def public_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="remainingRetentionDays")
    def remaining_retention_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

class AwaitableGetBlobContainerResult(GetBlobContainerResult):
    def __await__(self): ...

def get_blob_container(
    account_name: Optional[_builtins.str] = ...,
    container_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBlobContainerResult: ...
def get_blob_container_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    container_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBlobContainerResult]: ...
