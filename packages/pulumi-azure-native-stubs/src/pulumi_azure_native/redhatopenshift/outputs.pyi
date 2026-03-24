

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['APIServerProfileResponse', 'ClusterProfileResponse', 'ConsoleProfileResponse', 'EffectiveOutboundIPResponse', 'IngressProfileResponse', 'LoadBalancerProfileResponse', 'ManagedOutboundIPsResponse', 'MasterProfileResponse', 'NetworkProfileResponse', 'ServicePrincipalProfileResponse', 'SystemDataResponse', 'WorkerProfileResponse']
@pulumi.output_type
class APIServerProfileResponse(dict):
    
    def __init__(__self__, *, ip: _builtins.str, url: _builtins.str, visibility: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain: Optional[_builtins.str] = ..., fips_validated_modules: Optional[_builtins.str] = ..., pull_secret: Optional[_builtins.str] = ..., resource_group_id: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fipsValidatedModules")
    def fips_validated_modules(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pullSecret")
    def pull_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConsoleProfileResponse(dict):
    
    def __init__(__self__, *, url: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EffectiveOutboundIPResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IngressProfileResponse(dict):
    
    def __init__(__self__, *, ip: _builtins.str, name: Optional[_builtins.str] = ..., visibility: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LoadBalancerProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, effective_outbound_ips: Sequence[outputs.EffectiveOutboundIPResponse], managed_outbound_ips: Optional[outputs.ManagedOutboundIPsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveOutboundIps")
    def effective_outbound_ips(self) -> Sequence[outputs.EffectiveOutboundIPResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedOutboundIps")
    def managed_outbound_ips(self) -> Optional[outputs.ManagedOutboundIPsResponse]:
        
        ...
    


@pulumi.output_type
class ManagedOutboundIPsResponse(dict):
    
    def __init__(__self__, *, count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class MasterProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_encryption_set_id: Optional[_builtins.str] = ..., encryption_at_host: Optional[_builtins.str] = ..., subnet_id: Optional[_builtins.str] = ..., vm_size: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, load_balancer_profile: Optional[outputs.LoadBalancerProfileResponse] = ..., outbound_type: Optional[_builtins.str] = ..., pod_cidr: Optional[_builtins.str] = ..., preconfigured_nsg: Optional[_builtins.str] = ..., service_cidr: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerProfile")
    def load_balancer_profile(self) -> Optional[outputs.LoadBalancerProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundType")
    def outbound_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="podCidr")
    def pod_cidr(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preconfiguredNSG")
    def preconfigured_nsg(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceCidr")
    def service_cidr(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServicePrincipalProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., client_secret: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkerProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, count: Optional[_builtins.int] = ..., disk_encryption_set_id: Optional[_builtins.str] = ..., disk_size_gb: Optional[_builtins.int] = ..., encryption_at_host: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., subnet_id: Optional[_builtins.str] = ..., vm_size: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[_builtins.str]:
        
        ...
    


