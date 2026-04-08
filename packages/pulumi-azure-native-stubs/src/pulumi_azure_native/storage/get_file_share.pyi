import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFileShareResult",
    "AwaitableGetFileShareResult",
    "get_file_share",
    "get_file_share_output",
]

@pulumi.output_type
class GetFileShareResult:
    def __init__(
        __self__,
        access_tier=...,
        access_tier_change_time=...,
        access_tier_status=...,
        azure_api_version=...,
        deleted=...,
        deleted_time=...,
        enabled_protocols=...,
        etag=...,
        file_share_paid_bursting=...,
        id=...,
        included_burst_iops=...,
        last_modified_time=...,
        lease_duration=...,
        lease_state=...,
        lease_status=...,
        max_burst_credits_for_iops=...,
        metadata=...,
        name=...,
        next_allowed_provisioned_bandwidth_downgrade_time=...,
        next_allowed_provisioned_iops_downgrade_time=...,
        next_allowed_quota_downgrade_time=...,
        provisioned_bandwidth_mibps=...,
        provisioned_iops=...,
        remaining_retention_days=...,
        root_squash=...,
        share_quota=...,
        share_usage_bytes=...,
        signed_identifiers=...,
        snapshot_time=...,
        type=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessTier")
    def access_tier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="accessTierChangeTime")
    def access_tier_change_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessTierStatus")
    def access_tier_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="deletedTime")
    def deleted_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enabledProtocols")
    def enabled_protocols(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileSharePaidBursting")
    def file_share_paid_bursting(
        self,
    ) -> Optional[outputs.FileSharePropertiesResponseFileSharePaidBursting]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includedBurstIops")
    def included_burst_iops(self) -> _builtins.int: ...
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
    @pulumi.getter(name="maxBurstCreditsForIops")
    def max_burst_credits_for_iops(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextAllowedProvisionedBandwidthDowngradeTime")
    def next_allowed_provisioned_bandwidth_downgrade_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextAllowedProvisionedIopsDowngradeTime")
    def next_allowed_provisioned_iops_downgrade_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextAllowedQuotaDowngradeTime")
    def next_allowed_quota_downgrade_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisionedBandwidthMibps")
    def provisioned_bandwidth_mibps(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="remainingRetentionDays")
    def remaining_retention_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="rootSquash")
    def root_squash(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shareQuota")
    def share_quota(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="shareUsageBytes")
    def share_usage_bytes(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="signedIdentifiers")
    def signed_identifiers(
        self,
    ) -> Optional[Sequence[outputs.SignedIdentifierResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotTime")
    def snapshot_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

class AwaitableGetFileShareResult(GetFileShareResult):
    def __await__(self): ...

def get_file_share(
    account_name: Optional[_builtins.str] = ...,
    expand: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    share_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFileShareResult: ...
def get_file_share_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    share_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFileShareResult]: ...
