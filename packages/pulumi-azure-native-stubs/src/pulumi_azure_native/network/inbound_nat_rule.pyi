import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["InboundNatRuleInitArgs", "InboundNatRule"]

@pulumi.input_type
class InboundNatRuleInitArgs:
    def __init__(
        __self__,
        *,
        load_balancer_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        backend_address_pool: Optional[pulumi.Input[SubResourceArgs]] = ...,
        backend_port: Optional[pulumi.Input[_builtins.int]] = ...,
        enable_floating_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_tcp_reset: Optional[pulumi.Input[_builtins.bool]] = ...,
        frontend_ip_configuration: Optional[pulumi.Input[SubResourceArgs]] = ...,
        frontend_port: Optional[pulumi.Input[_builtins.int]] = ...,
        frontend_port_range_end: Optional[pulumi.Input[_builtins.int]] = ...,
        frontend_port_range_start: Optional[pulumi.Input[_builtins.int]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        inbound_nat_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[Union[_builtins.str, TransportProtocol]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerName")
    def load_balancer_name(self) -> pulumi.Input[_builtins.str]: ...
    @load_balancer_name.setter
    def load_balancer_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backendAddressPool")
    def backend_address_pool(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @backend_address_pool.setter
    def backend_address_pool(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @backend_port.setter
    def backend_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="enableFloatingIP")
    def enable_floating_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_floating_ip.setter
    def enable_floating_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableTcpReset")
    def enable_tcp_reset(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_tcp_reset.setter
    def enable_tcp_reset(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="frontendIPConfiguration")
    def frontend_ip_configuration(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @frontend_ip_configuration.setter
    def frontend_ip_configuration(
        self, value: Optional[pulumi.Input[SubResourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @frontend_port.setter
    def frontend_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="frontendPortRangeEnd")
    def frontend_port_range_end(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @frontend_port_range_end.setter
    def frontend_port_range_end(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="frontendPortRangeStart")
    def frontend_port_range_start(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @frontend_port_range_start.setter
    def frontend_port_range_start(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="inboundNatRuleName")
    def inbound_nat_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inbound_nat_rule_name.setter
    def inbound_nat_rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TransportProtocol]]]: ...
    @protocol.setter
    def protocol(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TransportProtocol]]]
    ): ...

@pulumi.type_token("azure-native:network:InboundNatRule")
class InboundNatRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        backend_address_pool: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        backend_port: Optional[pulumi.Input[_builtins.int]] = ...,
        enable_floating_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_tcp_reset: Optional[pulumi.Input[_builtins.bool]] = ...,
        frontend_ip_configuration: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        frontend_port: Optional[pulumi.Input[_builtins.int]] = ...,
        frontend_port_range_end: Optional[pulumi.Input[_builtins.int]] = ...,
        frontend_port_range_start: Optional[pulumi.Input[_builtins.int]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        inbound_nat_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancer_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[Union[_builtins.str, TransportProtocol]]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: InboundNatRuleInitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> InboundNatRule: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backendAddressPool")
    def backend_address_pool(
        self,
    ) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="backendIPConfiguration")
    def backend_ip_configuration(
        self,
    ) -> pulumi.Output[outputs.NetworkInterfaceIPConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="enableFloatingIP")
    def enable_floating_ip(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableTcpReset")
    def enable_tcp_reset(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="frontendIPConfiguration")
    def frontend_ip_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="frontendPortRangeEnd")
    def frontend_port_range_end(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="frontendPortRangeStart")
    def frontend_port_range_start(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
