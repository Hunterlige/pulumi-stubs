

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DirectoryConnectSettings', 'DirectoryVpcSettings', 'ServiceRegionVpcSettings', 'SharedDirectoryTarget', 'GetDirectoryConnectSettingResult', 'GetDirectoryRadiusSettingResult', 'GetDirectoryVpcSettingResult']
@pulumi.output_type
class DirectoryConnectSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, customer_dns_ips: Sequence[_builtins.str], customer_username: _builtins.str, subnet_ids: Sequence[_builtins.str], vpc_id: _builtins.str, availability_zones: Optional[Sequence[_builtins.str]] = ..., connect_ips: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerDnsIps")
    def customer_dns_ips(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerUsername")
    def customer_username(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectIps")
    def connect_ips(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class DirectoryVpcSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnet_ids: Sequence[_builtins.str], vpc_id: _builtins.str, availability_zones: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class ServiceRegionVpcSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnet_ids: Sequence[_builtins.str], vpc_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SharedDirectoryTarget(dict):
    def __init__(__self__, *, id: _builtins.str, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetDirectoryConnectSettingResult(dict):
    def __init__(__self__, *, availability_zones: Sequence[_builtins.str], connect_ips: Sequence[_builtins.str], customer_dns_ips: Sequence[_builtins.str], customer_username: _builtins.str, subnet_ids: Sequence[_builtins.str], vpc_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectIps")
    def connect_ips(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerDnsIps")
    def customer_dns_ips(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerUsername")
    def customer_username(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDirectoryRadiusSettingResult(dict):
    def __init__(__self__, *, authentication_protocol: _builtins.str, display_label: _builtins.str, radius_port: _builtins.int, radius_retries: _builtins.int, radius_servers: Sequence[_builtins.str], radius_timeout: _builtins.int, use_same_username: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationProtocol")
    def authentication_protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayLabel")
    def display_label(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusPort")
    def radius_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusRetries")
    def radius_retries(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusServers")
    def radius_servers(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="radiusTimeout")
    def radius_timeout(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useSameUsername")
    def use_same_username(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetDirectoryVpcSettingResult(dict):
    def __init__(__self__, *, availability_zones: Sequence[_builtins.str], subnet_ids: Sequence[_builtins.str], vpc_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
        ...
    


