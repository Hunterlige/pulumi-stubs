

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCacheResult', 'AwaitableGetCacheResult', 'get_cache', 'get_cache_output']
@pulumi.output_type
class GetCacheResult:
    
    def __init__(__self__, azure_api_version=..., cache_size_gb=..., directory_services_settings=..., encryption_settings=..., health=..., id=..., identity=..., location=..., mount_addresses=..., name=..., network_settings=..., priming_jobs=..., provisioning_state=..., security_settings=..., sku=..., space_allocation=..., subnet=..., system_data=..., tags=..., type=..., upgrade_settings=..., upgrade_status=..., zones=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheSizeGB")
    def cache_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryServicesSettings")
    def directory_services_settings(self) -> Optional[outputs.CacheDirectorySettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> Optional[outputs.CacheEncryptionSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> outputs.CacheHealthResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.CacheIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountAddresses")
    def mount_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSettings")
    def network_settings(self) -> Optional[outputs.CacheNetworkSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primingJobs")
    def priming_jobs(self) -> Sequence[outputs.PrimingJobResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> Optional[outputs.CacheSecuritySettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.CacheResponseSku]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spaceAllocation")
    def space_allocation(self) -> Sequence[outputs.StorageTargetSpaceAllocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> Optional[outputs.CacheUpgradeSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeStatus")
    def upgrade_status(self) -> outputs.CacheUpgradeStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableGetCacheResult(GetCacheResult):
    def __await__(self): # -> Generator[Never, Any, GetCacheResult]:
        ...
    


def get_cache(cache_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCacheResult:
    
    ...

def get_cache_output(cache_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCacheResult]:
    
    ...

