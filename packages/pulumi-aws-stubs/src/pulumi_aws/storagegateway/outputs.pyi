

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FileSystemAssociationCacheAttributes', 'GatewayGatewayNetworkInterface', 'GatewayMaintenanceStartTime', 'GatewaySmbActiveDirectorySettings', 'NfsFileShareCacheAttributes', 'NfsFileShareNfsFileShareDefaults', 'SmbFileShareCacheAttributes']
@pulumi.output_type
class FileSystemAssociationCacheAttributes(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cache_stale_timeout_in_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheStaleTimeoutInSeconds")
    def cache_stale_timeout_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class GatewayGatewayNetworkInterface(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ipv4_address: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GatewayMaintenanceStartTime(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hour_of_day: _builtins.int, day_of_month: Optional[_builtins.str] = ..., day_of_week: Optional[_builtins.str] = ..., minute_of_hour: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfMonth")
    def day_of_month(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minuteOfHour")
    def minute_of_hour(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class GatewaySmbActiveDirectorySettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: _builtins.str, password: _builtins.str, username: _builtins.str, active_directory_status: Optional[_builtins.str] = ..., domain_controllers: Optional[Sequence[_builtins.str]] = ..., organizational_unit: Optional[_builtins.str] = ..., timeout_in_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryStatus")
    def active_directory_status(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainControllers")
    def domain_controllers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationalUnit")
    def organizational_unit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class NfsFileShareCacheAttributes(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cache_stale_timeout_in_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheStaleTimeoutInSeconds")
    def cache_stale_timeout_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class NfsFileShareNfsFileShareDefaults(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, directory_mode: Optional[_builtins.str] = ..., file_mode: Optional[_builtins.str] = ..., group_id: Optional[_builtins.str] = ..., owner_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryMode")
    def directory_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileMode")
    def file_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SmbFileShareCacheAttributes(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cache_stale_timeout_in_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheStaleTimeoutInSeconds")
    def cache_stale_timeout_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


