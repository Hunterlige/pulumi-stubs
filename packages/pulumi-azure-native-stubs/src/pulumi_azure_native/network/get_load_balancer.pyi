import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLoadBalancerResult",
    "AwaitableGetLoadBalancerResult",
    "get_load_balancer",
    "get_load_balancer_output",
]

@pulumi.output_type
class GetLoadBalancerResult:
    def __init__(
        __self__,
        azure_api_version=...,
        backend_address_pools=...,
        etag=...,
        extended_location=...,
        frontend_ip_configurations=...,
        id=...,
        inbound_nat_pools=...,
        inbound_nat_rules=...,
        load_balancing_rules=...,
        location=...,
        name=...,
        outbound_rules=...,
        probes=...,
        provisioning_state=...,
        resource_guid=...,
        sku=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backendAddressPools")
    def backend_address_pools(
        self,
    ) -> Optional[Sequence[outputs.BackendAddressPoolResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="frontendIPConfigurations")
    def frontend_ip_configurations(
        self,
    ) -> Optional[Sequence[outputs.FrontendIPConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inboundNatPools")
    def inbound_nat_pools(
        self,
    ) -> Optional[Sequence[outputs.InboundNatPoolResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="inboundNatRules")
    def inbound_nat_rules(
        self,
    ) -> Optional[Sequence[outputs.InboundNatRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingRules")
    def load_balancing_rules(
        self,
    ) -> Optional[Sequence[outputs.LoadBalancingRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outboundRules")
    def outbound_rules(self) -> Optional[Sequence[outputs.OutboundRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def probes(self) -> Optional[Sequence[outputs.ProbeResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.LoadBalancerSkuResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetLoadBalancerResult(GetLoadBalancerResult):
    def __await__(self): ...

def get_load_balancer(
    expand: Optional[_builtins.str] = ...,
    load_balancer_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLoadBalancerResult: ...
def get_load_balancer_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    load_balancer_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLoadBalancerResult]: ...
