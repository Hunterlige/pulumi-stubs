

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectorArgs', 'Connector']
@pulumi.input_type
class ConnectorArgs:
    def __init__(__self__, *, ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., machine_type: Optional[pulumi.Input[_builtins.str]] = ..., max_instances: Optional[pulumi.Input[_builtins.int]] = ..., max_throughput: Optional[pulumi.Input[_builtins.int]] = ..., min_instances: Optional[pulumi.Input[_builtins.int]] = ..., min_throughput: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet: Optional[pulumi.Input[ConnectorSubnetArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_cidr_range.setter
    def ip_cidr_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_instances.setter
    def max_instances(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_throughput.setter
    def max_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_instances.setter
    def min_instances(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minThroughput")
    def min_throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_throughput.setter
    def min_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[ConnectorSubnetArgs]]:
        
        ...
    
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[ConnectorSubnetArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ConnectorState:
    def __init__(__self__, *, connected_projects: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., machine_type: Optional[pulumi.Input[_builtins.str]] = ..., max_instances: Optional[pulumi.Input[_builtins.int]] = ..., max_throughput: Optional[pulumi.Input[_builtins.int]] = ..., min_instances: Optional[pulumi.Input[_builtins.int]] = ..., min_throughput: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., subnet: Optional[pulumi.Input[ConnectorSubnetArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedProjects")
    def connected_projects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @connected_projects.setter
    def connected_projects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_cidr_range.setter
    def ip_cidr_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_instances.setter
    def max_instances(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_throughput.setter
    def max_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_instances.setter
    def min_instances(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minThroughput")
    def min_throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_throughput.setter
    def min_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[ConnectorSubnetArgs]]:
        
        ...
    
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[ConnectorSubnetArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:vpcaccess/connector:Connector")
class Connector(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., machine_type: Optional[pulumi.Input[_builtins.str]] = ..., max_instances: Optional[pulumi.Input[_builtins.int]] = ..., max_throughput: Optional[pulumi.Input[_builtins.int]] = ..., min_instances: Optional[pulumi.Input[_builtins.int]] = ..., min_throughput: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet: Optional[pulumi.Input[Union[ConnectorSubnetArgs, ConnectorSubnetArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ConnectorArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., connected_projects: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., machine_type: Optional[pulumi.Input[_builtins.str]] = ..., max_instances: Optional[pulumi.Input[_builtins.int]] = ..., max_throughput: Optional[pulumi.Input[_builtins.int]] = ..., min_instances: Optional[pulumi.Input[_builtins.int]] = ..., min_throughput: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., subnet: Optional[pulumi.Input[Union[ConnectorSubnetArgs, ConnectorSubnetArgsDict]]] = ...) -> Connector:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedProjects")
    def connected_projects(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minThroughput")
    def min_throughput(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> pulumi.Output[Optional[outputs.ConnectorSubnet]]:
        
        ...
    


