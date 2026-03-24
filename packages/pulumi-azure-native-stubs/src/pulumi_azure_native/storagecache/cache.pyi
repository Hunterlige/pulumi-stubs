

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CacheArgs', 'Cache']
@pulumi.input_type
class CacheArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], cache_name: Optional[pulumi.Input[_builtins.str]] = ..., cache_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., directory_services_settings: Optional[pulumi.Input[CacheDirectorySettingsArgs]] = ..., encryption_settings: Optional[pulumi.Input[CacheEncryptionSettingsArgs]] = ..., identity: Optional[pulumi.Input[CacheIdentityArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_settings: Optional[pulumi.Input[CacheNetworkSettingsArgs]] = ..., security_settings: Optional[pulumi.Input[CacheSecuritySettingsArgs]] = ..., sku: Optional[pulumi.Input[CacheSkuArgs]] = ..., subnet: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., upgrade_settings: Optional[pulumi.Input[CacheUpgradeSettingsArgs]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheName")
    def cache_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cache_name.setter
    def cache_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheSizeGB")
    def cache_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cache_size_gb.setter
    def cache_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryServicesSettings")
    def directory_services_settings(self) -> Optional[pulumi.Input[CacheDirectorySettingsArgs]]:
        
        ...
    
    @directory_services_settings.setter
    def directory_services_settings(self, value: Optional[pulumi.Input[CacheDirectorySettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> Optional[pulumi.Input[CacheEncryptionSettingsArgs]]:
        
        ...
    
    @encryption_settings.setter
    def encryption_settings(self, value: Optional[pulumi.Input[CacheEncryptionSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[CacheIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[CacheIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSettings")
    def network_settings(self) -> Optional[pulumi.Input[CacheNetworkSettingsArgs]]:
        
        ...
    
    @network_settings.setter
    def network_settings(self, value: Optional[pulumi.Input[CacheNetworkSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> Optional[pulumi.Input[CacheSecuritySettingsArgs]]:
        
        ...
    
    @security_settings.setter
    def security_settings(self, value: Optional[pulumi.Input[CacheSecuritySettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[CacheSkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[CacheSkuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> Optional[pulumi.Input[CacheUpgradeSettingsArgs]]:
        
        ...
    
    @upgrade_settings.setter
    def upgrade_settings(self, value: Optional[pulumi.Input[CacheUpgradeSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:storagecache:Cache")
class Cache(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cache_name: Optional[pulumi.Input[_builtins.str]] = ..., cache_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., directory_services_settings: Optional[pulumi.Input[Union[CacheDirectorySettingsArgs, CacheDirectorySettingsArgsDict]]] = ..., encryption_settings: Optional[pulumi.Input[Union[CacheEncryptionSettingsArgs, CacheEncryptionSettingsArgsDict]]] = ..., identity: Optional[pulumi.Input[Union[CacheIdentityArgs, CacheIdentityArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_settings: Optional[pulumi.Input[Union[CacheNetworkSettingsArgs, CacheNetworkSettingsArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., security_settings: Optional[pulumi.Input[Union[CacheSecuritySettingsArgs, CacheSecuritySettingsArgsDict]]] = ..., sku: Optional[pulumi.Input[Union[CacheSkuArgs, CacheSkuArgsDict]]] = ..., subnet: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., upgrade_settings: Optional[pulumi.Input[Union[CacheUpgradeSettingsArgs, CacheUpgradeSettingsArgsDict]]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CacheArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Cache:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheSizeGB")
    def cache_size_gb(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryServicesSettings")
    def directory_services_settings(self) -> pulumi.Output[Optional[outputs.CacheDirectorySettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> pulumi.Output[Optional[outputs.CacheEncryptionSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> pulumi.Output[outputs.CacheHealthResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.CacheIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountAddresses")
    def mount_addresses(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSettings")
    def network_settings(self) -> pulumi.Output[Optional[outputs.CacheNetworkSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primingJobs")
    def priming_jobs(self) -> pulumi.Output[Sequence[outputs.PrimingJobResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> pulumi.Output[Optional[outputs.CacheSecuritySettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.CacheResponseSku]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spaceAllocation")
    def space_allocation(self) -> pulumi.Output[Sequence[outputs.StorageTargetSpaceAllocationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> pulumi.Output[Optional[outputs.CacheUpgradeSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeStatus")
    def upgrade_status(self) -> pulumi.Output[outputs.CacheUpgradeStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    


