

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConnectorResult', 'AwaitableGetConnectorResult', 'get_connector', 'get_connector_output']
@pulumi.output_type
class GetConnectorResult:
    
    def __init__(__self__, connected_projects=..., id=..., ip_cidr_range=..., machine_type=..., max_instances=..., max_throughput=..., min_instances=..., min_throughput=..., name=..., network=..., project=..., region=..., self_link=..., state=..., subnets=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedProjects")
    def connected_projects(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minThroughput")
    def min_throughput(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[outputs.GetConnectorSubnetResult]:
        ...
    


class AwaitableGetConnectorResult(GetConnectorResult):
    def __await__(self): # -> Generator[Never, Any, GetConnectorResult]:
        ...
    


def get_connector(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConnectorResult:
    
    ...

def get_connector_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConnectorResult]:
    
    ...

