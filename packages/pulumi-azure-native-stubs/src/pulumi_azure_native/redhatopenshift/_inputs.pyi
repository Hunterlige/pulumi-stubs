

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['APIServerProfileArgs', 'APIServerProfileArgsDict', 'ClusterProfileArgs', 'ClusterProfileArgsDict', 'IngressProfileArgs', 'IngressProfileArgsDict', 'LoadBalancerProfileArgs', 'LoadBalancerProfileArgsDict', 'ManagedOutboundIPsArgs', 'ManagedOutboundIPsArgsDict', 'MasterProfileArgs', 'MasterProfileArgsDict', 'NetworkProfileArgs', 'NetworkProfileArgsDict', 'ServicePrincipalProfileArgs', 'ServicePrincipalProfileArgsDict', 'WorkerProfileArgs', 'WorkerProfileArgsDict']
class APIServerProfileArgsDict(TypedDict):
    
    visibility: NotRequired[pulumi.Input[Union[_builtins.str, Visibility]]]


@pulumi.input_type
class APIServerProfileArgs:
    def __init__(__self__, *, visibility: Optional[pulumi.Input[Union[_builtins.str, Visibility]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[Union[_builtins.str, Visibility]]]:
        
        ...
    
    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[Union[_builtins.str, Visibility]]]): # -> None:
        ...
    


class ClusterProfileArgsDict(TypedDict):
    
    domain: NotRequired[pulumi.Input[_builtins.str]]
    fips_validated_modules: NotRequired[pulumi.Input[Union[_builtins.str, FipsValidatedModules]]]
    pull_secret: NotRequired[pulumi.Input[_builtins.str]]
    resource_group_id: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterProfileArgs:
    def __init__(__self__, *, domain: Optional[pulumi.Input[_builtins.str]] = ..., fips_validated_modules: Optional[pulumi.Input[Union[_builtins.str, FipsValidatedModules]]] = ..., pull_secret: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_id: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fipsValidatedModules")
    def fips_validated_modules(self) -> Optional[pulumi.Input[Union[_builtins.str, FipsValidatedModules]]]:
        
        ...
    
    @fips_validated_modules.setter
    def fips_validated_modules(self, value: Optional[pulumi.Input[Union[_builtins.str, FipsValidatedModules]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pullSecret")
    def pull_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pull_secret.setter
    def pull_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_group_id.setter
    def resource_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IngressProfileArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    visibility: NotRequired[pulumi.Input[Union[_builtins.str, Visibility]]]


@pulumi.input_type
class IngressProfileArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., visibility: Optional[pulumi.Input[Union[_builtins.str, Visibility]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[Union[_builtins.str, Visibility]]]:
        
        ...
    
    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[Union[_builtins.str, Visibility]]]): # -> None:
        ...
    


class LoadBalancerProfileArgsDict(TypedDict):
    
    managed_outbound_ips: NotRequired[pulumi.Input[ManagedOutboundIPsArgsDict]]


@pulumi.input_type
class LoadBalancerProfileArgs:
    def __init__(__self__, *, managed_outbound_ips: Optional[pulumi.Input[ManagedOutboundIPsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedOutboundIps")
    def managed_outbound_ips(self) -> Optional[pulumi.Input[ManagedOutboundIPsArgs]]:
        
        ...
    
    @managed_outbound_ips.setter
    def managed_outbound_ips(self, value: Optional[pulumi.Input[ManagedOutboundIPsArgs]]): # -> None:
        ...
    


class ManagedOutboundIPsArgsDict(TypedDict):
    
    count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ManagedOutboundIPsArgs:
    def __init__(__self__, *, count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class MasterProfileArgsDict(TypedDict):
    
    disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    encryption_at_host: NotRequired[pulumi.Input[Union[_builtins.str, EncryptionAtHost]]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    vm_size: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MasterProfileArgs:
    def __init__(__self__, *, disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ..., encryption_at_host: Optional[pulumi.Input[Union[_builtins.str, EncryptionAtHost]]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., vm_size: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[pulumi.Input[Union[_builtins.str, EncryptionAtHost]]]:
        
        ...
    
    @encryption_at_host.setter
    def encryption_at_host(self, value: Optional[pulumi.Input[Union[_builtins.str, EncryptionAtHost]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkProfileArgsDict(TypedDict):
    
    load_balancer_profile: NotRequired[pulumi.Input[LoadBalancerProfileArgsDict]]
    outbound_type: NotRequired[pulumi.Input[Union[_builtins.str, OutboundType]]]
    pod_cidr: NotRequired[pulumi.Input[_builtins.str]]
    preconfigured_nsg: NotRequired[pulumi.Input[Union[_builtins.str, PreconfiguredNSG]]]
    service_cidr: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkProfileArgs:
    def __init__(__self__, *, load_balancer_profile: Optional[pulumi.Input[LoadBalancerProfileArgs]] = ..., outbound_type: Optional[pulumi.Input[Union[_builtins.str, OutboundType]]] = ..., pod_cidr: Optional[pulumi.Input[_builtins.str]] = ..., preconfigured_nsg: Optional[pulumi.Input[Union[_builtins.str, PreconfiguredNSG]]] = ..., service_cidr: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerProfile")
    def load_balancer_profile(self) -> Optional[pulumi.Input[LoadBalancerProfileArgs]]:
        
        ...
    
    @load_balancer_profile.setter
    def load_balancer_profile(self, value: Optional[pulumi.Input[LoadBalancerProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundType")
    def outbound_type(self) -> Optional[pulumi.Input[Union[_builtins.str, OutboundType]]]:
        
        ...
    
    @outbound_type.setter
    def outbound_type(self, value: Optional[pulumi.Input[Union[_builtins.str, OutboundType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="podCidr")
    def pod_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pod_cidr.setter
    def pod_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preconfiguredNSG")
    def preconfigured_nsg(self) -> Optional[pulumi.Input[Union[_builtins.str, PreconfiguredNSG]]]:
        
        ...
    
    @preconfigured_nsg.setter
    def preconfigured_nsg(self, value: Optional[pulumi.Input[Union[_builtins.str, PreconfiguredNSG]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceCidr")
    def service_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_cidr.setter
    def service_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServicePrincipalProfileArgsDict(TypedDict):
    
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServicePrincipalProfileArgs:
    def __init__(__self__, *, client_id: Optional[pulumi.Input[_builtins.str]] = ..., client_secret: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkerProfileArgsDict(TypedDict):
    
    count: NotRequired[pulumi.Input[_builtins.int]]
    disk_encryption_set_id: NotRequired[pulumi.Input[_builtins.str]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    encryption_at_host: NotRequired[pulumi.Input[Union[_builtins.str, EncryptionAtHost]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    vm_size: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkerProfileArgs:
    def __init__(__self__, *, count: Optional[pulumi.Input[_builtins.int]] = ..., disk_encryption_set_id: Optional[pulumi.Input[_builtins.str]] = ..., disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., encryption_at_host: Optional[pulumi.Input[Union[_builtins.str, EncryptionAtHost]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., vm_size: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[pulumi.Input[Union[_builtins.str, EncryptionAtHost]]]:
        
        ...
    
    @encryption_at_host.setter
    def encryption_at_host(self, value: Optional[pulumi.Input[Union[_builtins.str, EncryptionAtHost]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


