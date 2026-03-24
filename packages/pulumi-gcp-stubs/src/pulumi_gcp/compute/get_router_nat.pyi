

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRouterNatResult', 'AwaitableGetRouterNatResult', 'get_router_nat', 'get_router_nat_output']
@pulumi.output_type
class GetRouterNatResult:
    
    def __init__(__self__, auto_network_tier=..., drain_nat_ips=..., enable_dynamic_port_allocation=..., enable_endpoint_independent_mapping=..., endpoint_types=..., icmp_idle_timeout_sec=..., id=..., initial_nat_ips=..., log_configs=..., max_ports_per_vm=..., min_ports_per_vm=..., name=..., nat64_subnetworks=..., nat_ip_allocate_option=..., nat_ips=..., project=..., region=..., router=..., rules=..., source_subnetwork_ip_ranges_to_nat=..., source_subnetwork_ip_ranges_to_nat64=..., subnetworks=..., tcp_established_idle_timeout_sec=..., tcp_time_wait_timeout_sec=..., tcp_transitory_idle_timeout_sec=..., type=..., udp_idle_timeout_sec=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoNetworkTier")
    def auto_network_tier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="drainNatIps")
    def drain_nat_ips(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDynamicPortAllocation")
    def enable_dynamic_port_allocation(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEndpointIndependentMapping")
    def enable_endpoint_independent_mapping(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointTypes")
    def endpoint_types(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpIdleTimeoutSec")
    def icmp_idle_timeout_sec(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialNatIps")
    def initial_nat_ips(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfigs")
    def log_configs(self) -> Sequence[outputs.GetRouterNatLogConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPortsPerVm")
    def max_ports_per_vm(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minPortsPerVm")
    def min_ports_per_vm(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nat64Subnetworks")
    def nat64_subnetworks(self) -> Sequence[outputs.GetRouterNatNat64SubnetworkResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natIpAllocateOption")
    def nat_ip_allocate_option(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natIps")
    def nat_ips(self) -> Sequence[_builtins.str]:
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
    @pulumi.getter
    def router(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.GetRouterNatRuleResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSubnetworkIpRangesToNat")
    def source_subnetwork_ip_ranges_to_nat(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSubnetworkIpRangesToNat64")
    def source_subnetwork_ip_ranges_to_nat64(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetworks(self) -> Sequence[outputs.GetRouterNatSubnetworkResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpEstablishedIdleTimeoutSec")
    def tcp_established_idle_timeout_sec(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpTimeWaitTimeoutSec")
    def tcp_time_wait_timeout_sec(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpTransitoryIdleTimeoutSec")
    def tcp_transitory_idle_timeout_sec(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="udpIdleTimeoutSec")
    def udp_idle_timeout_sec(self) -> _builtins.int:
        ...
    


class AwaitableGetRouterNatResult(GetRouterNatResult):
    def __await__(self): # -> Generator[Never, Any, GetRouterNatResult]:
        ...
    


def get_router_nat(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., router: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRouterNatResult:
    
    ...

def get_router_nat_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., router: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRouterNatResult]:
    
    ...

