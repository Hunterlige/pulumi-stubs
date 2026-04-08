import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CapacityPoolVolumeArgs", "CapacityPoolVolume"]

@pulumi.input_type
class CapacityPoolVolumeArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        creation_token: pulumi.Input[_builtins.str],
        pool_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        subnet_id: pulumi.Input[_builtins.str],
        usage_threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        avs_data_store: Optional[
            pulumi.Input[Union[_builtins.str, AvsDataStore]]
        ] = ...,
        backup_id: Optional[pulumi.Input[_builtins.str]] = ...,
        capacity_pool_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cool_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        cool_access_retrieval_policy: Optional[
            pulumi.Input[Union[_builtins.str, CoolAccessRetrievalPolicy]]
        ] = ...,
        cool_access_tiering_policy: Optional[
            pulumi.Input[Union[_builtins.str, CoolAccessTieringPolicy]]
        ] = ...,
        coolness_period: Optional[pulumi.Input[_builtins.int]] = ...,
        data_protection: Optional[
            pulumi.Input[VolumePropertiesDataProtectionArgs]
        ] = ...,
        default_group_quota_in_ki_bs: Optional[pulumi.Input[_builtins.float]] = ...,
        default_user_quota_in_ki_bs: Optional[pulumi.Input[_builtins.float]] = ...,
        delete_base_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_subvolumes: Optional[
            pulumi.Input[Union[_builtins.str, EnableSubvolumes]]
        ] = ...,
        encryption_key_source: Optional[
            pulumi.Input[Union[_builtins.str, EncryptionKeySource]]
        ] = ...,
        export_policy: Optional[pulumi.Input[VolumePropertiesExportPolicyArgs]] = ...,
        is_default_quota_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_large_volume: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_restoring: Optional[pulumi.Input[_builtins.bool]] = ...,
        kerberos_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_vault_private_endpoint_resource_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        ldap_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_features: Optional[
            pulumi.Input[Union[_builtins.str, NetworkFeatures]]
        ] = ...,
        placement_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlacementKeyValuePairsArgs]]]
        ] = ...,
        protocol_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        proximity_placement_group: Optional[pulumi.Input[_builtins.str]] = ...,
        security_style: Optional[
            pulumi.Input[Union[_builtins.str, SecurityStyle]]
        ] = ...,
        service_level: Optional[pulumi.Input[Union[_builtins.str, ServiceLevel]]] = ...,
        smb_access_based_enumeration: Optional[
            pulumi.Input[Union[_builtins.str, SmbAccessBasedEnumeration]]
        ] = ...,
        smb_continuously_available: Optional[pulumi.Input[_builtins.bool]] = ...,
        smb_encryption: Optional[pulumi.Input[_builtins.bool]] = ...,
        smb_non_browsable: Optional[
            pulumi.Input[Union[_builtins.str, SmbNonBrowsable]]
        ] = ...,
        snapshot_directory_visible: Optional[pulumi.Input[_builtins.bool]] = ...,
        snapshot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        throughput_mibps: Optional[pulumi.Input[_builtins.float]] = ...,
        unix_permissions: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_name: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_spec_name: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="creationToken")
    def creation_token(self) -> pulumi.Input[_builtins.str]: ...
    @creation_token.setter
    def creation_token(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> pulumi.Input[_builtins.str]: ...
    @pool_name.setter
    def pool_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="usageThreshold")
    def usage_threshold(self) -> pulumi.Input[_builtins.float]: ...
    @usage_threshold.setter
    def usage_threshold(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="avsDataStore")
    def avs_data_store(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AvsDataStore]]]: ...
    @avs_data_store.setter
    def avs_data_store(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AvsDataStore]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_id.setter
    def backup_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="capacityPoolResourceId")
    def capacity_pool_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @capacity_pool_resource_id.setter
    def capacity_pool_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="coolAccess")
    def cool_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cool_access.setter
    def cool_access(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="coolAccessRetrievalPolicy")
    def cool_access_retrieval_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CoolAccessRetrievalPolicy]]]: ...
    @cool_access_retrieval_policy.setter
    def cool_access_retrieval_policy(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, CoolAccessRetrievalPolicy]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="coolAccessTieringPolicy")
    def cool_access_tiering_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CoolAccessTieringPolicy]]]: ...
    @cool_access_tiering_policy.setter
    def cool_access_tiering_policy(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, CoolAccessTieringPolicy]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="coolnessPeriod")
    def coolness_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @coolness_period.setter
    def coolness_period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="dataProtection")
    def data_protection(
        self,
    ) -> Optional[pulumi.Input[VolumePropertiesDataProtectionArgs]]: ...
    @data_protection.setter
    def data_protection(
        self, value: Optional[pulumi.Input[VolumePropertiesDataProtectionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultGroupQuotaInKiBs")
    def default_group_quota_in_ki_bs(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @default_group_quota_in_ki_bs.setter
    def default_group_quota_in_ki_bs(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultUserQuotaInKiBs")
    def default_user_quota_in_ki_bs(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @default_user_quota_in_ki_bs.setter
    def default_user_quota_in_ki_bs(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteBaseSnapshot")
    def delete_base_snapshot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @delete_base_snapshot.setter
    def delete_base_snapshot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableSubvolumes")
    def enable_subvolumes(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EnableSubvolumes]]]: ...
    @enable_subvolumes.setter
    def enable_subvolumes(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EnableSubvolumes]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeySource")
    def encryption_key_source(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EncryptionKeySource]]]: ...
    @encryption_key_source.setter
    def encryption_key_source(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EncryptionKeySource]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exportPolicy")
    def export_policy(
        self,
    ) -> Optional[pulumi.Input[VolumePropertiesExportPolicyArgs]]: ...
    @export_policy.setter
    def export_policy(
        self, value: Optional[pulumi.Input[VolumePropertiesExportPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isDefaultQuotaEnabled")
    def is_default_quota_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_default_quota_enabled.setter
    def is_default_quota_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isLargeVolume")
    def is_large_volume(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_large_volume.setter
    def is_large_volume(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isRestoring")
    def is_restoring(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_restoring.setter
    def is_restoring(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="kerberosEnabled")
    def kerberos_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @kerberos_enabled.setter
    def kerberos_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultPrivateEndpointResourceId")
    def key_vault_private_endpoint_resource_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_private_endpoint_resource_id.setter
    def key_vault_private_endpoint_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ldapEnabled")
    def ldap_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ldap_enabled.setter
    def ldap_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkFeatures")
    def network_features(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NetworkFeatures]]]: ...
    @network_features.setter
    def network_features(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkFeatures]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="placementRules")
    def placement_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlacementKeyValuePairsArgs]]]]: ...
    @placement_rules.setter
    def placement_rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlacementKeyValuePairsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="protocolTypes")
    def protocol_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @protocol_types.setter
    def protocol_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @proximity_placement_group.setter
    def proximity_placement_group(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityStyle")
    def security_style(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SecurityStyle]]]: ...
    @security_style.setter
    def security_style(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SecurityStyle]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceLevel")
    def service_level(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ServiceLevel]]]: ...
    @service_level.setter
    def service_level(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ServiceLevel]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="smbAccessBasedEnumeration")
    def smb_access_based_enumeration(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SmbAccessBasedEnumeration]]]: ...
    @smb_access_based_enumeration.setter
    def smb_access_based_enumeration(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, SmbAccessBasedEnumeration]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="smbContinuouslyAvailable")
    def smb_continuously_available(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @smb_continuously_available.setter
    def smb_continuously_available(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="smbEncryption")
    def smb_encryption(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @smb_encryption.setter
    def smb_encryption(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="smbNonBrowsable")
    def smb_non_browsable(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SmbNonBrowsable]]]: ...
    @smb_non_browsable.setter
    def smb_non_browsable(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SmbNonBrowsable]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotDirectoryVisible")
    def snapshot_directory_visible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @snapshot_directory_visible.setter
    def snapshot_directory_visible(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="throughputMibps")
    def throughput_mibps(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @throughput_mibps.setter
    def throughput_mibps(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="unixPermissions")
    def unix_permissions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unix_permissions.setter
    def unix_permissions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_name.setter
    def volume_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeSpecName")
    def volume_spec_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_spec_name.setter
    def volume_spec_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:netapp:CapacityPoolVolume")
class CapacityPoolVolume(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        avs_data_store: Optional[
            pulumi.Input[Union[_builtins.str, AvsDataStore]]
        ] = ...,
        backup_id: Optional[pulumi.Input[_builtins.str]] = ...,
        capacity_pool_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cool_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        cool_access_retrieval_policy: Optional[
            pulumi.Input[Union[_builtins.str, CoolAccessRetrievalPolicy]]
        ] = ...,
        cool_access_tiering_policy: Optional[
            pulumi.Input[Union[_builtins.str, CoolAccessTieringPolicy]]
        ] = ...,
        coolness_period: Optional[pulumi.Input[_builtins.int]] = ...,
        creation_token: Optional[pulumi.Input[_builtins.str]] = ...,
        data_protection: Optional[
            pulumi.Input[
                Union[
                    VolumePropertiesDataProtectionArgs,
                    VolumePropertiesDataProtectionArgsDict,
                ]
            ]
        ] = ...,
        default_group_quota_in_ki_bs: Optional[pulumi.Input[_builtins.float]] = ...,
        default_user_quota_in_ki_bs: Optional[pulumi.Input[_builtins.float]] = ...,
        delete_base_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_subvolumes: Optional[
            pulumi.Input[Union[_builtins.str, EnableSubvolumes]]
        ] = ...,
        encryption_key_source: Optional[
            pulumi.Input[Union[_builtins.str, EncryptionKeySource]]
        ] = ...,
        export_policy: Optional[
            pulumi.Input[
                Union[
                    VolumePropertiesExportPolicyArgs,
                    VolumePropertiesExportPolicyArgsDict,
                ]
            ]
        ] = ...,
        is_default_quota_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_large_volume: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_restoring: Optional[pulumi.Input[_builtins.bool]] = ...,
        kerberos_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_vault_private_endpoint_resource_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        ldap_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_features: Optional[
            pulumi.Input[Union[_builtins.str, NetworkFeatures]]
        ] = ...,
        placement_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PlacementKeyValuePairsArgs, PlacementKeyValuePairsArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        proximity_placement_group: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        security_style: Optional[
            pulumi.Input[Union[_builtins.str, SecurityStyle]]
        ] = ...,
        service_level: Optional[pulumi.Input[Union[_builtins.str, ServiceLevel]]] = ...,
        smb_access_based_enumeration: Optional[
            pulumi.Input[Union[_builtins.str, SmbAccessBasedEnumeration]]
        ] = ...,
        smb_continuously_available: Optional[pulumi.Input[_builtins.bool]] = ...,
        smb_encryption: Optional[pulumi.Input[_builtins.bool]] = ...,
        smb_non_browsable: Optional[
            pulumi.Input[Union[_builtins.str, SmbNonBrowsable]]
        ] = ...,
        snapshot_directory_visible: Optional[pulumi.Input[_builtins.bool]] = ...,
        snapshot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        throughput_mibps: Optional[pulumi.Input[_builtins.float]] = ...,
        unix_permissions: Optional[pulumi.Input[_builtins.str]] = ...,
        usage_threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        volume_name: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_spec_name: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CapacityPoolVolumeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> CapacityPoolVolume: ...
    @_builtins.property
    @pulumi.getter(name="actualThroughputMibps")
    def actual_throughput_mibps(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="avsDataStore")
    def avs_data_store(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="baremetalTenantId")
    def baremetal_tenant_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="capacityPoolResourceId")
    def capacity_pool_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cloneProgress")
    def clone_progress(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="coolAccess")
    def cool_access(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="coolAccessRetrievalPolicy")
    def cool_access_retrieval_policy(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="coolAccessTieringPolicy")
    def cool_access_tiering_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="coolnessPeriod")
    def coolness_period(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="creationToken")
    def creation_token(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataProtection")
    def data_protection(
        self,
    ) -> pulumi.Output[Optional[outputs.VolumePropertiesResponseDataProtection]]: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreResourceId")
    def data_store_resource_id(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultGroupQuotaInKiBs")
    def default_group_quota_in_ki_bs(
        self,
    ) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultUserQuotaInKiBs")
    def default_user_quota_in_ki_bs(
        self,
    ) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="deleteBaseSnapshot")
    def delete_base_snapshot(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveNetworkFeatures")
    def effective_network_features(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableSubvolumes")
    def enable_subvolumes(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeySource")
    def encryption_key_source(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exportPolicy")
    def export_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.VolumePropertiesResponseExportPolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="fileAccessLogs")
    def file_access_logs(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isDefaultQuotaEnabled")
    def is_default_quota_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="isLargeVolume")
    def is_large_volume(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="isRestoring")
    def is_restoring(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="kerberosEnabled")
    def kerberos_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultPrivateEndpointResourceId")
    def key_vault_private_endpoint_resource_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ldapEnabled")
    def ldap_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maximumNumberOfFiles")
    def maximum_number_of_files(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="mountTargets")
    def mount_targets(
        self,
    ) -> pulumi.Output[Sequence[outputs.MountTargetPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkFeatures")
    def network_features(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="networkSiblingSetId")
    def network_sibling_set_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originatingResourceId")
    def originating_resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="placementRules")
    def placement_rules(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PlacementKeyValuePairsResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="protocolTypes")
    def protocol_types(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedAvailabilityZone")
    def provisioned_availability_zone(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="securityStyle")
    def security_style(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceLevel")
    def service_level(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="smbAccessBasedEnumeration")
    def smb_access_based_enumeration(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="smbContinuouslyAvailable")
    def smb_continuously_available(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="smbEncryption")
    def smb_encryption(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="smbNonBrowsable")
    def smb_non_browsable(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotDirectoryVisible")
    def snapshot_directory_visible(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="storageToNetworkProximity")
    def storage_to_network_proximity(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="t2Network")
    def t2_network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="throughputMibps")
    def throughput_mibps(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="unixPermissions")
    def unix_permissions(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="usageThreshold")
    def usage_threshold(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="volumeGroupName")
    def volume_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="volumeSpecName")
    def volume_spec_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
