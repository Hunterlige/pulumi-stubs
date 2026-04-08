import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLoadBalancerBackendAddressPoolResult",
    "AwaitableGetLoadBalancerBackendAddressPoolResult",
    "get_load_balancer_backend_address_pool",
    "get_load_balancer_backend_address_pool_output",
]

@pulumi.output_type
class GetLoadBalancerBackendAddressPoolResult:
    def __init__(
        __self__,
        azure_api_version=...,
        backend_ip_configurations=...,
        drain_period_in_seconds=...,
        etag=...,
        id=...,
        inbound_nat_rules=...,
        load_balancer_backend_addresses=...,
        load_balancing_rules=...,
        location=...,
        name=...,
        outbound_rule=...,
        outbound_rules=...,
        provisioning_state=...,
        sync_mode=...,
        tunnel_interfaces=...,
        type=...,
        virtual_network=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backendIPConfigurations")
    def backend_ip_configurations(
        self,
    ) -> Sequence[outputs.NetworkInterfaceIPConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="drainPeriodInSeconds")
    def drain_period_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inboundNatRules")
    def inbound_nat_rules(self) -> Sequence[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerBackendAddresses")
    def load_balancer_backend_addresses(
        self,
    ) -> Optional[Sequence[outputs.LoadBalancerBackendAddressResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingRules")
    def load_balancing_rules(self) -> Sequence[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outboundRule")
    def outbound_rule(self) -> outputs.SubResourceResponse: ...
    @_builtins.property
    @pulumi.getter(name="outboundRules")
    def outbound_rules(self) -> Sequence[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="syncMode")
    def sync_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tunnelInterfaces")
    def tunnel_interfaces(
        self,
    ) -> Optional[Sequence[outputs.GatewayLoadBalancerTunnelInterfaceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetwork")
    def virtual_network(self) -> Optional[outputs.SubResourceResponse]: ...

class AwaitableGetLoadBalancerBackendAddressPoolResult(
    GetLoadBalancerBackendAddressPoolResult
):
    def __await__(self): ...

def get_load_balancer_backend_address_pool(
    backend_address_pool_name: Optional[_builtins.str] = ...,
    load_balancer_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLoadBalancerBackendAddressPoolResult: ...
def get_load_balancer_backend_address_pool_output(
    backend_address_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    load_balancer_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLoadBalancerBackendAddressPoolResult]: ...
