

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
__all__ = ['RouterNatArgs', 'RouterNat']
@pulumi.input_type
class RouterNatArgs:
    def __init__(__self__, *, router: pulumi.Input[_builtins.str], source_subnetwork_ip_ranges_to_nat: pulumi.Input[_builtins.str], auto_network_tier: Optional[pulumi.Input[_builtins.str]] = ..., drain_nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enable_dynamic_port_allocation: Optional[pulumi.Input[_builtins.bool]] = ..., enable_endpoint_independent_mapping: Optional[pulumi.Input[_builtins.bool]] = ..., endpoint_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., icmp_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., initial_nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., log_config: Optional[pulumi.Input[RouterNatLogConfigArgs]] = ..., max_ports_per_vm: Optional[pulumi.Input[_builtins.int]] = ..., min_ports_per_vm: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nat64_subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatNat64SubnetworkArgs]]]] = ..., nat_ip_allocate_option: Optional[pulumi.Input[_builtins.str]] = ..., nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatRuleArgs]]]] = ..., source_subnetwork_ip_ranges_to_nat64: Optional[pulumi.Input[_builtins.str]] = ..., subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatSubnetworkArgs]]]] = ..., tcp_established_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., tcp_time_wait_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., tcp_transitory_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., udp_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def router(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @router.setter
    def router(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSubnetworkIpRangesToNat")
    def source_subnetwork_ip_ranges_to_nat(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_subnetwork_ip_ranges_to_nat.setter
    def source_subnetwork_ip_ranges_to_nat(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoNetworkTier")
    def auto_network_tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auto_network_tier.setter
    def auto_network_tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="drainNatIps")
    def drain_nat_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @drain_nat_ips.setter
    def drain_nat_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDynamicPortAllocation")
    def enable_dynamic_port_allocation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_dynamic_port_allocation.setter
    def enable_dynamic_port_allocation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEndpointIndependentMapping")
    def enable_endpoint_independent_mapping(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_endpoint_independent_mapping.setter
    def enable_endpoint_independent_mapping(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointTypes")
    def endpoint_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @endpoint_types.setter
    def endpoint_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpIdleTimeoutSec")
    def icmp_idle_timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @icmp_idle_timeout_sec.setter
    def icmp_idle_timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialNatIps")
    def initial_nat_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @initial_nat_ips.setter
    def initial_nat_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[RouterNatLogConfigArgs]]:
        
        ...
    
    @log_config.setter
    def log_config(self, value: Optional[pulumi.Input[RouterNatLogConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPortsPerVm")
    def max_ports_per_vm(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_ports_per_vm.setter
    def max_ports_per_vm(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minPortsPerVm")
    def min_ports_per_vm(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_ports_per_vm.setter
    def min_ports_per_vm(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nat64Subnetworks")
    def nat64_subnetworks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatNat64SubnetworkArgs]]]]:
        
        ...
    
    @nat64_subnetworks.setter
    def nat64_subnetworks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatNat64SubnetworkArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natIpAllocateOption")
    def nat_ip_allocate_option(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nat_ip_allocate_option.setter
    def nat_ip_allocate_option(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natIps")
    def nat_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @nat_ips.setter
    def nat_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSubnetworkIpRangesToNat64")
    def source_subnetwork_ip_ranges_to_nat64(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_subnetwork_ip_ranges_to_nat64.setter
    def source_subnetwork_ip_ranges_to_nat64(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetworks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatSubnetworkArgs]]]]:
        
        ...
    
    @subnetworks.setter
    def subnetworks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatSubnetworkArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpEstablishedIdleTimeoutSec")
    def tcp_established_idle_timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @tcp_established_idle_timeout_sec.setter
    def tcp_established_idle_timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpTimeWaitTimeoutSec")
    def tcp_time_wait_timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @tcp_time_wait_timeout_sec.setter
    def tcp_time_wait_timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpTransitoryIdleTimeoutSec")
    def tcp_transitory_idle_timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @tcp_transitory_idle_timeout_sec.setter
    def tcp_transitory_idle_timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="udpIdleTimeoutSec")
    def udp_idle_timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @udp_idle_timeout_sec.setter
    def udp_idle_timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.input_type
class _RouterNatState:
    def __init__(__self__, *, auto_network_tier: Optional[pulumi.Input[_builtins.str]] = ..., drain_nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enable_dynamic_port_allocation: Optional[pulumi.Input[_builtins.bool]] = ..., enable_endpoint_independent_mapping: Optional[pulumi.Input[_builtins.bool]] = ..., endpoint_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., icmp_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., initial_nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., log_config: Optional[pulumi.Input[RouterNatLogConfigArgs]] = ..., max_ports_per_vm: Optional[pulumi.Input[_builtins.int]] = ..., min_ports_per_vm: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nat64_subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatNat64SubnetworkArgs]]]] = ..., nat_ip_allocate_option: Optional[pulumi.Input[_builtins.str]] = ..., nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., router: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatRuleArgs]]]] = ..., source_subnetwork_ip_ranges_to_nat: Optional[pulumi.Input[_builtins.str]] = ..., source_subnetwork_ip_ranges_to_nat64: Optional[pulumi.Input[_builtins.str]] = ..., subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatSubnetworkArgs]]]] = ..., tcp_established_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., tcp_time_wait_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., tcp_transitory_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., udp_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoNetworkTier")
    def auto_network_tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auto_network_tier.setter
    def auto_network_tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="drainNatIps")
    def drain_nat_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @drain_nat_ips.setter
    def drain_nat_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDynamicPortAllocation")
    def enable_dynamic_port_allocation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_dynamic_port_allocation.setter
    def enable_dynamic_port_allocation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEndpointIndependentMapping")
    def enable_endpoint_independent_mapping(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_endpoint_independent_mapping.setter
    def enable_endpoint_independent_mapping(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointTypes")
    def endpoint_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @endpoint_types.setter
    def endpoint_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpIdleTimeoutSec")
    def icmp_idle_timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @icmp_idle_timeout_sec.setter
    def icmp_idle_timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialNatIps")
    def initial_nat_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @initial_nat_ips.setter
    def initial_nat_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[RouterNatLogConfigArgs]]:
        
        ...
    
    @log_config.setter
    def log_config(self, value: Optional[pulumi.Input[RouterNatLogConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPortsPerVm")
    def max_ports_per_vm(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_ports_per_vm.setter
    def max_ports_per_vm(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minPortsPerVm")
    def min_ports_per_vm(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_ports_per_vm.setter
    def min_ports_per_vm(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nat64Subnetworks")
    def nat64_subnetworks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatNat64SubnetworkArgs]]]]:
        
        ...
    
    @nat64_subnetworks.setter
    def nat64_subnetworks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatNat64SubnetworkArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natIpAllocateOption")
    def nat_ip_allocate_option(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nat_ip_allocate_option.setter
    def nat_ip_allocate_option(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natIps")
    def nat_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @nat_ips.setter
    def nat_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    def router(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @router.setter
    def router(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSubnetworkIpRangesToNat")
    def source_subnetwork_ip_ranges_to_nat(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_subnetwork_ip_ranges_to_nat.setter
    def source_subnetwork_ip_ranges_to_nat(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSubnetworkIpRangesToNat64")
    def source_subnetwork_ip_ranges_to_nat64(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_subnetwork_ip_ranges_to_nat64.setter
    def source_subnetwork_ip_ranges_to_nat64(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetworks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatSubnetworkArgs]]]]:
        
        ...
    
    @subnetworks.setter
    def subnetworks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RouterNatSubnetworkArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpEstablishedIdleTimeoutSec")
    def tcp_established_idle_timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @tcp_established_idle_timeout_sec.setter
    def tcp_established_idle_timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpTimeWaitTimeoutSec")
    def tcp_time_wait_timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @tcp_time_wait_timeout_sec.setter
    def tcp_time_wait_timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpTransitoryIdleTimeoutSec")
    def tcp_transitory_idle_timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @tcp_transitory_idle_timeout_sec.setter
    def tcp_transitory_idle_timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="udpIdleTimeoutSec")
    def udp_idle_timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @udp_idle_timeout_sec.setter
    def udp_idle_timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/routerNat:RouterNat")
class RouterNat(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auto_network_tier: Optional[pulumi.Input[_builtins.str]] = ..., drain_nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enable_dynamic_port_allocation: Optional[pulumi.Input[_builtins.bool]] = ..., enable_endpoint_independent_mapping: Optional[pulumi.Input[_builtins.bool]] = ..., endpoint_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., icmp_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., initial_nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., log_config: Optional[pulumi.Input[Union[RouterNatLogConfigArgs, RouterNatLogConfigArgsDict]]] = ..., max_ports_per_vm: Optional[pulumi.Input[_builtins.int]] = ..., min_ports_per_vm: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nat64_subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RouterNatNat64SubnetworkArgs, RouterNatNat64SubnetworkArgsDict]]]]] = ..., nat_ip_allocate_option: Optional[pulumi.Input[_builtins.str]] = ..., nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., router: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RouterNatRuleArgs, RouterNatRuleArgsDict]]]]] = ..., source_subnetwork_ip_ranges_to_nat: Optional[pulumi.Input[_builtins.str]] = ..., source_subnetwork_ip_ranges_to_nat64: Optional[pulumi.Input[_builtins.str]] = ..., subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RouterNatSubnetworkArgs, RouterNatSubnetworkArgsDict]]]]] = ..., tcp_established_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., tcp_time_wait_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., tcp_transitory_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., udp_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RouterNatArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., auto_network_tier: Optional[pulumi.Input[_builtins.str]] = ..., drain_nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enable_dynamic_port_allocation: Optional[pulumi.Input[_builtins.bool]] = ..., enable_endpoint_independent_mapping: Optional[pulumi.Input[_builtins.bool]] = ..., endpoint_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., icmp_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., initial_nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., log_config: Optional[pulumi.Input[Union[RouterNatLogConfigArgs, RouterNatLogConfigArgsDict]]] = ..., max_ports_per_vm: Optional[pulumi.Input[_builtins.int]] = ..., min_ports_per_vm: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nat64_subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RouterNatNat64SubnetworkArgs, RouterNatNat64SubnetworkArgsDict]]]]] = ..., nat_ip_allocate_option: Optional[pulumi.Input[_builtins.str]] = ..., nat_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., router: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RouterNatRuleArgs, RouterNatRuleArgsDict]]]]] = ..., source_subnetwork_ip_ranges_to_nat: Optional[pulumi.Input[_builtins.str]] = ..., source_subnetwork_ip_ranges_to_nat64: Optional[pulumi.Input[_builtins.str]] = ..., subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RouterNatSubnetworkArgs, RouterNatSubnetworkArgsDict]]]]] = ..., tcp_established_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., tcp_time_wait_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., tcp_transitory_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., udp_idle_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...) -> RouterNat:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoNetworkTier")
    def auto_network_tier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="drainNatIps")
    def drain_nat_ips(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDynamicPortAllocation")
    def enable_dynamic_port_allocation(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEndpointIndependentMapping")
    def enable_endpoint_independent_mapping(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointTypes")
    def endpoint_types(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpIdleTimeoutSec")
    def icmp_idle_timeout_sec(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialNatIps")
    def initial_nat_ips(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output[Optional[outputs.RouterNatLogConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPortsPerVm")
    def max_ports_per_vm(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minPortsPerVm")
    def min_ports_per_vm(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nat64Subnetworks")
    def nat64_subnetworks(self) -> pulumi.Output[Optional[Sequence[outputs.RouterNatNat64Subnetwork]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="natIpAllocateOption")
    def nat_ip_allocate_option(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="natIps")
    def nat_ips(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
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
    @pulumi.getter
    def router(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence[outputs.RouterNatRule]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSubnetworkIpRangesToNat")
    def source_subnetwork_ip_ranges_to_nat(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSubnetworkIpRangesToNat64")
    def source_subnetwork_ip_ranges_to_nat64(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetworks(self) -> pulumi.Output[Optional[Sequence[outputs.RouterNatSubnetwork]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpEstablishedIdleTimeoutSec")
    def tcp_established_idle_timeout_sec(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpTimeWaitTimeoutSec")
    def tcp_time_wait_timeout_sec(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpTransitoryIdleTimeoutSec")
    def tcp_transitory_idle_timeout_sec(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="udpIdleTimeoutSec")
    def udp_idle_timeout_sec(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    


