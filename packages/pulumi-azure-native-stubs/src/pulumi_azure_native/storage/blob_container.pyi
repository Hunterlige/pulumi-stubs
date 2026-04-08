import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BlobContainerArgs", "BlobContainer"]

@pulumi.input_type
class BlobContainerArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        default_encryption_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        deny_encryption_scope_override: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_nfs_v3_all_squash: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_nfs_v3_root_squash: Optional[pulumi.Input[_builtins.bool]] = ...,
        immutable_storage_with_versioning: Optional[
            pulumi.Input[ImmutableStorageWithVersioningArgs]
        ] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        public_access: Optional[pulumi.Input[PublicAccess]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultEncryptionScope")
    def default_encryption_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_encryption_scope.setter
    def default_encryption_scope(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="denyEncryptionScopeOverride")
    def deny_encryption_scope_override(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deny_encryption_scope_override.setter
    def deny_encryption_scope_override(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableNfsV3AllSquash")
    def enable_nfs_v3_all_squash(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_nfs_v3_all_squash.setter
    def enable_nfs_v3_all_squash(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableNfsV3RootSquash")
    def enable_nfs_v3_root_squash(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_nfs_v3_root_squash.setter
    def enable_nfs_v3_root_squash(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="immutableStorageWithVersioning")
    def immutable_storage_with_versioning(
        self,
    ) -> Optional[pulumi.Input[ImmutableStorageWithVersioningArgs]]: ...
    @immutable_storage_with_versioning.setter
    def immutable_storage_with_versioning(
        self, value: Optional[pulumi.Input[ImmutableStorageWithVersioningArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicAccess")
    def public_access(self) -> Optional[pulumi.Input[PublicAccess]]: ...
    @public_access.setter
    def public_access(self, value: Optional[pulumi.Input[PublicAccess]]): ...

@pulumi.type_token("azure-native:storage:BlobContainer")
class BlobContainer(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        default_encryption_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        deny_encryption_scope_override: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_nfs_v3_all_squash: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_nfs_v3_root_squash: Optional[pulumi.Input[_builtins.bool]] = ...,
        immutable_storage_with_versioning: Optional[
            pulumi.Input[
                Union[
                    ImmutableStorageWithVersioningArgs,
                    ImmutableStorageWithVersioningArgsDict,
                ]
            ]
        ] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        public_access: Optional[pulumi.Input[PublicAccess]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BlobContainerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> BlobContainer: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultEncryptionScope")
    def default_encryption_scope(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="deletedTime")
    def deleted_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="denyEncryptionScopeOverride")
    def deny_encryption_scope_override(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableNfsV3AllSquash")
    def enable_nfs_v3_all_squash(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableNfsV3RootSquash")
    def enable_nfs_v3_root_squash(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hasImmutabilityPolicy")
    def has_immutability_policy(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="hasLegalHold")
    def has_legal_hold(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="immutabilityPolicy")
    def immutability_policy(
        self,
    ) -> pulumi.Output[outputs.ImmutabilityPolicyPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="immutableStorageWithVersioning")
    def immutable_storage_with_versioning(
        self,
    ) -> pulumi.Output[Optional[outputs.ImmutableStorageWithVersioningResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="leaseDuration")
    def lease_duration(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="leaseState")
    def lease_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="leaseStatus")
    def lease_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="legalHold")
    def legal_hold(self) -> pulumi.Output[outputs.LegalHoldPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicAccess")
    def public_access(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="remainingRetentionDays")
    def remaining_retention_days(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
