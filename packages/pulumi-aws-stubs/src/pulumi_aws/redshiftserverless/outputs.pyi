

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EndpointAccessVpcEndpoint', 'EndpointAccessVpcEndpointNetworkInterface', 'WorkgroupConfigParameter', 'WorkgroupEndpoint', 'WorkgroupEndpointVpcEndpoint', 'WorkgroupEndpointVpcEndpointNetworkInterface', 'WorkgroupPricePerformanceTarget', 'GetWorkgroupEndpointResult', 'GetWorkgroupEndpointVpcEndpointResult', ...]
@pulumi.output_type
class EndpointAccessVpcEndpoint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_interfaces: Optional[Sequence[outputs.EndpointAccessVpcEndpointNetworkInterface]] = ..., vpc_endpoint_id: Optional[_builtins.str] = ..., vpc_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[Sequence[outputs.EndpointAccessVpcEndpointNetworkInterface]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EndpointAccessVpcEndpointNetworkInterface(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, availability_zone: Optional[_builtins.str] = ..., network_interface_id: Optional[_builtins.str] = ..., private_ip_address: Optional[_builtins.str] = ..., subnet_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkgroupConfigParameter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, parameter_key: _builtins.str, parameter_value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterKey")
    def parameter_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkgroupEndpoint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ..., vpc_endpoints: Optional[Sequence[outputs.WorkgroupEndpointVpcEndpoint]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpoints")
    def vpc_endpoints(self) -> Optional[Sequence[outputs.WorkgroupEndpointVpcEndpoint]]:
        
        ...
    


@pulumi.output_type
class WorkgroupEndpointVpcEndpoint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_interfaces: Optional[Sequence[outputs.WorkgroupEndpointVpcEndpointNetworkInterface]] = ..., vpc_endpoint_id: Optional[_builtins.str] = ..., vpc_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[Sequence[outputs.WorkgroupEndpointVpcEndpointNetworkInterface]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkgroupEndpointVpcEndpointNetworkInterface(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, availability_zone: Optional[_builtins.str] = ..., network_interface_id: Optional[_builtins.str] = ..., private_ip_address: Optional[_builtins.str] = ..., subnet_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkgroupPricePerformanceTarget(dict):
    def __init__(__self__, *, enabled: _builtins.bool, level: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class GetWorkgroupEndpointResult(dict):
    def __init__(__self__, *, address: _builtins.str, port: _builtins.int, vpc_endpoints: Sequence[outputs.GetWorkgroupEndpointVpcEndpointResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpoints")
    def vpc_endpoints(self) -> Sequence[outputs.GetWorkgroupEndpointVpcEndpointResult]:
        
        ...
    


@pulumi.output_type
class GetWorkgroupEndpointVpcEndpointResult(dict):
    def __init__(__self__, *, network_interfaces: Sequence[outputs.GetWorkgroupEndpointVpcEndpointNetworkInterfaceResult], vpc_endpoint_id: _builtins.str, vpc_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence[outputs.GetWorkgroupEndpointVpcEndpointNetworkInterfaceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetWorkgroupEndpointVpcEndpointNetworkInterfaceResult(dict):
    def __init__(__self__, *, availability_zone: _builtins.str, network_interface_id: _builtins.str, private_ip_address: _builtins.str, subnet_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str:
        
        ...
    


