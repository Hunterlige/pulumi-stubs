import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DiskArgs", "Disk"]

@pulumi.input_type
class DiskArgs:
    def __init__(
        __self__,
        *,
        creation_data: pulumi.Input[CreationDataArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        bursting_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        completion_percent: Optional[pulumi.Input[_builtins.float]] = ...,
        data_access_auth_mode: Optional[
            pulumi.Input[Union[_builtins.str, DataAccessAuthMode]]
        ] = ...,
        disk_access_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_iops_read_only: Optional[pulumi.Input[_builtins.float]] = ...,
        disk_iops_read_write: Optional[pulumi.Input[_builtins.float]] = ...,
        disk_m_bps_read_only: Optional[pulumi.Input[_builtins.float]] = ...,
        disk_m_bps_read_write: Optional[pulumi.Input[_builtins.float]] = ...,
        disk_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        encryption: Optional[pulumi.Input[EncryptionArgs]] = ...,
        encryption_settings_collection: Optional[
            pulumi.Input[EncryptionSettingsCollectionArgs]
        ] = ...,
        extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ...,
        hyper_v_generation: Optional[
            pulumi.Input[Union[_builtins.str, HyperVGeneration]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_shares: Optional[pulumi.Input[_builtins.int]] = ...,
        network_access_policy: Optional[
            pulumi.Input[Union[_builtins.str, NetworkAccessPolicy]]
        ] = ...,
        optimized_for_frequent_attach: Optional[pulumi.Input[_builtins.bool]] = ...,
        os_type: Optional[pulumi.Input[OperatingSystemTypes]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        purchase_plan: Optional[pulumi.Input[DiskPurchasePlanArgs]] = ...,
        security_profile: Optional[pulumi.Input[DiskSecurityProfileArgs]] = ...,
        sku: Optional[pulumi.Input[DiskSkuArgs]] = ...,
        supported_capabilities: Optional[pulumi.Input[SupportedCapabilitiesArgs]] = ...,
        supports_hibernation: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> pulumi.Input[CreationDataArgs]: ...
    @creation_data.setter
    def creation_data(self, value: pulumi.Input[CreationDataArgs]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="burstingEnabled")
    def bursting_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bursting_enabled.setter
    def bursting_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="completionPercent")
    def completion_percent(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @completion_percent.setter
    def completion_percent(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="dataAccessAuthMode")
    def data_access_auth_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DataAccessAuthMode]]]: ...
    @data_access_auth_mode.setter
    def data_access_auth_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DataAccessAuthMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskAccessId")
    def disk_access_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_access_id.setter
    def disk_access_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskIOPSReadOnly")
    def disk_iops_read_only(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @disk_iops_read_only.setter
    def disk_iops_read_only(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="diskIOPSReadWrite")
    def disk_iops_read_write(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @disk_iops_read_write.setter
    def disk_iops_read_write(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="diskMBpsReadOnly")
    def disk_m_bps_read_only(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @disk_m_bps_read_only.setter
    def disk_m_bps_read_only(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="diskMBpsReadWrite")
    def disk_m_bps_read_write(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @disk_m_bps_read_write.setter
    def disk_m_bps_read_write(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_name.setter
    def disk_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[EncryptionArgs]]: ...
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[EncryptionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionSettingsCollection")
    def encryption_settings_collection(
        self,
    ) -> Optional[pulumi.Input[EncryptionSettingsCollectionArgs]]: ...
    @encryption_settings_collection.setter
    def encryption_settings_collection(
        self, value: Optional[pulumi.Input[EncryptionSettingsCollectionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @extended_location.setter
    def extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, HyperVGeneration]]]: ...
    @hyper_v_generation.setter
    def hyper_v_generation(
        self, value: Optional[pulumi.Input[Union[_builtins.str, HyperVGeneration]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxShares")
    def max_shares(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_shares.setter
    def max_shares(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="networkAccessPolicy")
    def network_access_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NetworkAccessPolicy]]]: ...
    @network_access_policy.setter
    def network_access_policy(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkAccessPolicy]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="optimizedForFrequentAttach")
    def optimized_for_frequent_attach(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @optimized_for_frequent_attach.setter
    def optimized_for_frequent_attach(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[OperatingSystemTypes]]: ...
    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[OperatingSystemTypes]]): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]: ...
    @public_network_access.setter
    def public_network_access(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="purchasePlan")
    def purchase_plan(self) -> Optional[pulumi.Input[DiskPurchasePlanArgs]]: ...
    @purchase_plan.setter
    def purchase_plan(self, value: Optional[pulumi.Input[DiskPurchasePlanArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input[DiskSecurityProfileArgs]]: ...
    @security_profile.setter
    def security_profile(
        self, value: Optional[pulumi.Input[DiskSecurityProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[DiskSkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[DiskSkuArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="supportedCapabilities")
    def supported_capabilities(
        self,
    ) -> Optional[pulumi.Input[SupportedCapabilitiesArgs]]: ...
    @supported_capabilities.setter
    def supported_capabilities(
        self, value: Optional[pulumi.Input[SupportedCapabilitiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="supportsHibernation")
    def supports_hibernation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @supports_hibernation.setter
    def supports_hibernation(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:compute:Disk")
class Disk(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bursting_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        completion_percent: Optional[pulumi.Input[_builtins.float]] = ...,
        creation_data: Optional[
            pulumi.Input[Union[CreationDataArgs, CreationDataArgsDict]]
        ] = ...,
        data_access_auth_mode: Optional[
            pulumi.Input[Union[_builtins.str, DataAccessAuthMode]]
        ] = ...,
        disk_access_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_iops_read_only: Optional[pulumi.Input[_builtins.float]] = ...,
        disk_iops_read_write: Optional[pulumi.Input[_builtins.float]] = ...,
        disk_m_bps_read_only: Optional[pulumi.Input[_builtins.float]] = ...,
        disk_m_bps_read_write: Optional[pulumi.Input[_builtins.float]] = ...,
        disk_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        encryption: Optional[
            pulumi.Input[Union[EncryptionArgs, EncryptionArgsDict]]
        ] = ...,
        encryption_settings_collection: Optional[
            pulumi.Input[
                Union[
                    EncryptionSettingsCollectionArgs,
                    EncryptionSettingsCollectionArgsDict,
                ]
            ]
        ] = ...,
        extended_location: Optional[
            pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]
        ] = ...,
        hyper_v_generation: Optional[
            pulumi.Input[Union[_builtins.str, HyperVGeneration]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_shares: Optional[pulumi.Input[_builtins.int]] = ...,
        network_access_policy: Optional[
            pulumi.Input[Union[_builtins.str, NetworkAccessPolicy]]
        ] = ...,
        optimized_for_frequent_attach: Optional[pulumi.Input[_builtins.bool]] = ...,
        os_type: Optional[pulumi.Input[OperatingSystemTypes]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        purchase_plan: Optional[
            pulumi.Input[Union[DiskPurchasePlanArgs, DiskPurchasePlanArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        security_profile: Optional[
            pulumi.Input[Union[DiskSecurityProfileArgs, DiskSecurityProfileArgsDict]]
        ] = ...,
        sku: Optional[pulumi.Input[Union[DiskSkuArgs, DiskSkuArgsDict]]] = ...,
        supported_capabilities: Optional[
            pulumi.Input[
                Union[SupportedCapabilitiesArgs, SupportedCapabilitiesArgsDict]
            ]
        ] = ...,
        supports_hibernation: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DiskArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Disk: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="burstingEnabled")
    def bursting_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="burstingEnabledTime")
    def bursting_enabled_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="completionPercent")
    def completion_percent(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> pulumi.Output[outputs.CreationDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dataAccessAuthMode")
    def data_access_auth_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="diskAccessId")
    def disk_access_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="diskIOPSReadOnly")
    def disk_iops_read_only(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="diskIOPSReadWrite")
    def disk_iops_read_write(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="diskMBpsReadOnly")
    def disk_m_bps_read_only(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="diskMBpsReadWrite")
    def disk_m_bps_read_write(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeBytes")
    def disk_size_bytes(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="diskState")
    def disk_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional[outputs.EncryptionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionSettingsCollection")
    def encryption_settings_collection(
        self,
    ) -> pulumi.Output[Optional[outputs.EncryptionSettingsCollectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> pulumi.Output[Optional[outputs.ExtendedLocationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastOwnershipUpdateTime")
    def last_ownership_update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedByExtended")
    def managed_by_extended(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxShares")
    def max_shares(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkAccessPolicy")
    def network_access_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="optimizedForFrequentAttach")
    def optimized_for_frequent_attach(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="propertyUpdatesInProgress")
    def property_updates_in_progress(
        self,
    ) -> pulumi.Output[outputs.PropertyUpdatesInProgressResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="purchasePlan")
    def purchase_plan(
        self,
    ) -> pulumi.Output[Optional[outputs.DiskPurchasePlanResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.DiskSecurityProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="shareInfo")
    def share_info(
        self,
    ) -> pulumi.Output[Sequence[outputs.ShareInfoElementResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.DiskSkuResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="supportedCapabilities")
    def supported_capabilities(
        self,
    ) -> pulumi.Output[Optional[outputs.SupportedCapabilitiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="supportsHibernation")
    def supports_hibernation(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
