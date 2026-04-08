import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FileShareArgs", "FileShare"]

@pulumi.input_type
class FileShareArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        access_tier: Optional[
            pulumi.Input[Union[_builtins.str, ShareAccessTier]]
        ] = ...,
        enabled_protocols: Optional[
            pulumi.Input[Union[_builtins.str, EnabledProtocols]]
        ] = ...,
        expand: Optional[pulumi.Input[_builtins.str]] = ...,
        file_share_paid_bursting: Optional[
            pulumi.Input[FileSharePropertiesFileSharePaidBurstingArgs]
        ] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        provisioned_bandwidth_mibps: Optional[pulumi.Input[_builtins.int]] = ...,
        provisioned_iops: Optional[pulumi.Input[_builtins.int]] = ...,
        root_squash: Optional[pulumi.Input[Union[_builtins.str, RootSquashType]]] = ...,
        share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        share_quota: Optional[pulumi.Input[_builtins.int]] = ...,
        signed_identifiers: Optional[
            pulumi.Input[Sequence[pulumi.Input[SignedIdentifierArgs]]]
        ] = ...,
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
    @pulumi.getter(name="accessTier")
    def access_tier(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ShareAccessTier]]]: ...
    @access_tier.setter
    def access_tier(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ShareAccessTier]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enabledProtocols")
    def enabled_protocols(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EnabledProtocols]]]: ...
    @enabled_protocols.setter
    def enabled_protocols(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EnabledProtocols]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def expand(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expand.setter
    def expand(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileSharePaidBursting")
    def file_share_paid_bursting(
        self,
    ) -> Optional[pulumi.Input[FileSharePropertiesFileSharePaidBurstingArgs]]: ...
    @file_share_paid_bursting.setter
    def file_share_paid_bursting(
        self,
        value: Optional[pulumi.Input[FileSharePropertiesFileSharePaidBurstingArgs]],
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
    @pulumi.getter(name="provisionedBandwidthMibps")
    def provisioned_bandwidth_mibps(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_bandwidth_mibps.setter
    def provisioned_bandwidth_mibps(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_iops.setter
    def provisioned_iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="rootSquash")
    def root_squash(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RootSquashType]]]: ...
    @root_squash.setter
    def root_squash(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RootSquashType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @share_name.setter
    def share_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shareQuota")
    def share_quota(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @share_quota.setter
    def share_quota(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="signedIdentifiers")
    def signed_identifiers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SignedIdentifierArgs]]]]: ...
    @signed_identifiers.setter
    def signed_identifiers(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[SignedIdentifierArgs]]]],
    ): ...

@pulumi.type_token("azure-native:storage:FileShare")
class FileShare(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_tier: Optional[
            pulumi.Input[Union[_builtins.str, ShareAccessTier]]
        ] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled_protocols: Optional[
            pulumi.Input[Union[_builtins.str, EnabledProtocols]]
        ] = ...,
        expand: Optional[pulumi.Input[_builtins.str]] = ...,
        file_share_paid_bursting: Optional[
            pulumi.Input[
                Union[
                    FileSharePropertiesFileSharePaidBurstingArgs,
                    FileSharePropertiesFileSharePaidBurstingArgsDict,
                ]
            ]
        ] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        provisioned_bandwidth_mibps: Optional[pulumi.Input[_builtins.int]] = ...,
        provisioned_iops: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        root_squash: Optional[pulumi.Input[Union[_builtins.str, RootSquashType]]] = ...,
        share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        share_quota: Optional[pulumi.Input[_builtins.int]] = ...,
        signed_identifiers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[SignedIdentifierArgs, SignedIdentifierArgsDict]]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FileShareArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> FileShare: ...
    @_builtins.property
    @pulumi.getter(name="accessTier")
    def access_tier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="accessTierChangeTime")
    def access_tier_change_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="accessTierStatus")
    def access_tier_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="deletedTime")
    def deleted_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enabledProtocols")
    def enabled_protocols(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileSharePaidBursting")
    def file_share_paid_bursting(
        self,
    ) -> pulumi.Output[
        Optional[outputs.FileSharePropertiesResponseFileSharePaidBursting]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="includedBurstIops")
    def included_burst_iops(self) -> pulumi.Output[_builtins.int]: ...
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
    @pulumi.getter(name="maxBurstCreditsForIops")
    def max_burst_credits_for_iops(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextAllowedProvisionedBandwidthDowngradeTime")
    def next_allowed_provisioned_bandwidth_downgrade_time(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextAllowedProvisionedIopsDowngradeTime")
    def next_allowed_provisioned_iops_downgrade_time(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextAllowedQuotaDowngradeTime")
    def next_allowed_quota_downgrade_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedBandwidthMibps")
    def provisioned_bandwidth_mibps(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="remainingRetentionDays")
    def remaining_retention_days(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rootSquash")
    def root_squash(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="shareQuota")
    def share_quota(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="shareUsageBytes")
    def share_usage_bytes(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="signedIdentifiers")
    def signed_identifiers(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.SignedIdentifierResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotTime")
    def snapshot_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
