

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetInboundNatRuleResult', 'AwaitableGetInboundNatRuleResult', 'get_inbound_nat_rule', 'get_inbound_nat_rule_output']
@pulumi.output_type
class GetInboundNatRuleResult:
    
    def __init__(__self__, azure_api_version=..., backend_address_pool=..., backend_ip_configuration=..., backend_port=..., enable_floating_ip=..., enable_tcp_reset=..., etag=..., frontend_ip_configuration=..., frontend_port=..., frontend_port_range_end=..., frontend_port_range_start=..., id=..., idle_timeout_in_minutes=..., name=..., protocol=..., provisioning_state=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendAddressPool")
    def backend_address_pool(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendIPConfiguration")
    def backend_ip_configuration(self) -> outputs.NetworkInterfaceIPConfigurationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableFloatingIP")
    def enable_floating_ip(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableTcpReset")
    def enable_tcp_reset(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontendIPConfiguration")
    def frontend_ip_configuration(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontendPortRangeEnd")
    def frontend_port_range_end(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontendPortRangeStart")
    def frontend_port_range_start(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetInboundNatRuleResult(GetInboundNatRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetInboundNatRuleResult]:
        ...
    


def get_inbound_nat_rule(expand: Optional[_builtins.str] = ..., inbound_nat_rule_name: Optional[_builtins.str] = ..., load_balancer_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInboundNatRuleResult:
    
    ...

def get_inbound_nat_rule_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., inbound_nat_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., load_balancer_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInboundNatRuleResult]:
    
    ...

