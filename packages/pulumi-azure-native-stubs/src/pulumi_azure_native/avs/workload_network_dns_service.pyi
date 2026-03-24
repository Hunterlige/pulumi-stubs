

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkloadNetworkDnsServiceArgs', 'WorkloadNetworkDnsService']
@pulumi.input_type
class WorkloadNetworkDnsServiceArgs:
    def __init__(__self__, *, private_cloud_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], default_dns_zone: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., dns_service_id: Optional[pulumi.Input[_builtins.str]] = ..., dns_service_ip: Optional[pulumi.Input[_builtins.str]] = ..., fqdn_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., log_level: Optional[pulumi.Input[Union[_builtins.str, DnsServiceLogLevelEnum]]] = ..., revision: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @private_cloud_name.setter
    def private_cloud_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDnsZone")
    def default_dns_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_dns_zone.setter
    def default_dns_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsServiceId")
    def dns_service_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_service_id.setter
    def dns_service_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsServiceIp")
    def dns_service_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_service_ip.setter
    def dns_service_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fqdnZones")
    def fqdn_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @fqdn_zones.setter
    def fqdn_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[Union[_builtins.str, DnsServiceLogLevelEnum]]]:
        
        ...
    
    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[Union[_builtins.str, DnsServiceLogLevelEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:avs:WorkloadNetworkDnsService")
class WorkloadNetworkDnsService(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., default_dns_zone: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., dns_service_id: Optional[pulumi.Input[_builtins.str]] = ..., dns_service_ip: Optional[pulumi.Input[_builtins.str]] = ..., fqdn_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., log_level: Optional[pulumi.Input[Union[_builtins.str, DnsServiceLogLevelEnum]]] = ..., private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., revision: Optional[pulumi.Input[_builtins.float]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkloadNetworkDnsServiceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> WorkloadNetworkDnsService:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDnsZone")
    def default_dns_zone(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsServiceIp")
    def dns_service_ip(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fqdnZones")
    def fqdn_zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


