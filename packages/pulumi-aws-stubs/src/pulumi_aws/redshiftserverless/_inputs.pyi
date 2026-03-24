

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EndpointAccessVpcEndpointArgs', 'EndpointAccessVpcEndpointArgsDict', 'EndpointAccessVpcEndpointNetworkInterfaceArgs', 'EndpointAccessVpcEndpointNetworkInterfaceArgsDict', 'WorkgroupConfigParameterArgs', 'WorkgroupConfigParameterArgsDict', 'WorkgroupEndpointArgs', 'WorkgroupEndpointArgsDict', 'WorkgroupEndpointVpcEndpointArgs', 'WorkgroupEndpointVpcEndpointArgsDict', 'WorkgroupEndpointVpcEndpointNetworkInterfaceArgs', ..., 'WorkgroupPricePerformanceTargetArgs', 'WorkgroupPricePerformanceTargetArgsDict']
class EndpointAccessVpcEndpointArgsDict(TypedDict):
    network_interfaces: NotRequired[pulumi.Input[Sequence[pulumi.Input[EndpointAccessVpcEndpointNetworkInterfaceArgsDict]]]]
    vpc_endpoint_id: NotRequired[pulumi.Input[_builtins.str]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EndpointAccessVpcEndpointArgs:
    def __init__(__self__, *, network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointAccessVpcEndpointNetworkInterfaceArgs]]]] = ..., vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointAccessVpcEndpointNetworkInterfaceArgs]]]]:
        
        ...
    
    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointAccessVpcEndpointNetworkInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EndpointAccessVpcEndpointNetworkInterfaceArgsDict(TypedDict):
    availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    network_interface_id: NotRequired[pulumi.Input[_builtins.str]]
    private_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EndpointAccessVpcEndpointNetworkInterfaceArgs:
    def __init__(__self__, *, availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., private_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkgroupConfigParameterArgsDict(TypedDict):
    parameter_key: pulumi.Input[_builtins.str]
    parameter_value: pulumi.Input[_builtins.str]


@pulumi.input_type
class WorkgroupConfigParameterArgs:
    def __init__(__self__, *, parameter_key: pulumi.Input[_builtins.str], parameter_value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterKey")
    def parameter_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_key.setter
    def parameter_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class WorkgroupEndpointArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    vpc_endpoints: NotRequired[pulumi.Input[Sequence[pulumi.Input[WorkgroupEndpointVpcEndpointArgsDict]]]]


@pulumi.input_type
class WorkgroupEndpointArgs:
    def __init__(__self__, *, address: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., vpc_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[WorkgroupEndpointVpcEndpointArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpoints")
    def vpc_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkgroupEndpointVpcEndpointArgs]]]]:
        
        ...
    
    @vpc_endpoints.setter
    def vpc_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkgroupEndpointVpcEndpointArgs]]]]): # -> None:
        ...
    


class WorkgroupEndpointVpcEndpointArgsDict(TypedDict):
    network_interfaces: NotRequired[pulumi.Input[Sequence[pulumi.Input[WorkgroupEndpointVpcEndpointNetworkInterfaceArgsDict]]]]
    vpc_endpoint_id: NotRequired[pulumi.Input[_builtins.str]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkgroupEndpointVpcEndpointArgs:
    def __init__(__self__, *, network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[WorkgroupEndpointVpcEndpointNetworkInterfaceArgs]]]] = ..., vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkgroupEndpointVpcEndpointNetworkInterfaceArgs]]]]:
        
        ...
    
    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkgroupEndpointVpcEndpointNetworkInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkgroupEndpointVpcEndpointNetworkInterfaceArgsDict(TypedDict):
    availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    network_interface_id: NotRequired[pulumi.Input[_builtins.str]]
    private_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkgroupEndpointVpcEndpointNetworkInterfaceArgs:
    def __init__(__self__, *, availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., private_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkgroupPricePerformanceTargetArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    level: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class WorkgroupPricePerformanceTargetArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], level: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @level.setter
    def level(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


