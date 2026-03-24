

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SecurityGatewayArgs', 'SecurityGateway']
@pulumi.input_type
class SecurityGatewayArgs:
    def __init__(__self__, *, security_gateway_id: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ..., hubs: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayHubArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging: Optional[pulumi.Input[SecurityGatewayLoggingArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy_protocol_config: Optional[pulumi.Input[SecurityGatewayProxyProtocolConfigArgs]] = ..., service_discovery: Optional[pulumi.Input[SecurityGatewayServiceDiscoveryArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGatewayId")
    def security_gateway_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @security_gateway_id.setter
    def security_gateway_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hubs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayHubArgs]]]]:
        
        ...
    
    @hubs.setter
    def hubs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayHubArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input[SecurityGatewayLoggingArgs]]:
        
        ...
    
    @logging.setter
    def logging(self, value: Optional[pulumi.Input[SecurityGatewayLoggingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyProtocolConfig")
    def proxy_protocol_config(self) -> Optional[pulumi.Input[SecurityGatewayProxyProtocolConfigArgs]]:
        
        ...
    
    @proxy_protocol_config.setter
    def proxy_protocol_config(self, value: Optional[pulumi.Input[SecurityGatewayProxyProtocolConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDiscovery")
    def service_discovery(self) -> Optional[pulumi.Input[SecurityGatewayServiceDiscoveryArgs]]:
        
        ...
    
    @service_discovery.setter
    def service_discovery(self, value: Optional[pulumi.Input[SecurityGatewayServiceDiscoveryArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _SecurityGatewayState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., delegating_service_account: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., external_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., hubs: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayHubArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging: Optional[pulumi.Input[SecurityGatewayLoggingArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy_protocol_config: Optional[pulumi.Input[SecurityGatewayProxyProtocolConfigArgs]] = ..., security_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., service_discovery: Optional[pulumi.Input[SecurityGatewayServiceDiscoveryArgs]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatingServiceAccount")
    def delegating_service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delegating_service_account.setter
    def delegating_service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIps")
    def external_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @external_ips.setter
    def external_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hubs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayHubArgs]]]]:
        
        ...
    
    @hubs.setter
    def hubs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayHubArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input[SecurityGatewayLoggingArgs]]:
        
        ...
    
    @logging.setter
    def logging(self, value: Optional[pulumi.Input[SecurityGatewayLoggingArgs]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyProtocolConfig")
    def proxy_protocol_config(self) -> Optional[pulumi.Input[SecurityGatewayProxyProtocolConfigArgs]]:
        
        ...
    
    @proxy_protocol_config.setter
    def proxy_protocol_config(self, value: Optional[pulumi.Input[SecurityGatewayProxyProtocolConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGatewayId")
    def security_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_gateway_id.setter
    def security_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDiscovery")
    def service_discovery(self) -> Optional[pulumi.Input[SecurityGatewayServiceDiscoveryArgs]]:
        
        ...
    
    @service_discovery.setter
    def service_discovery(self, value: Optional[pulumi.Input[SecurityGatewayServiceDiscoveryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:beyondcorp/securityGateway:SecurityGateway")
class SecurityGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., hubs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SecurityGatewayHubArgs, SecurityGatewayHubArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging: Optional[pulumi.Input[Union[SecurityGatewayLoggingArgs, SecurityGatewayLoggingArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy_protocol_config: Optional[pulumi.Input[Union[SecurityGatewayProxyProtocolConfigArgs, SecurityGatewayProxyProtocolConfigArgsDict]]] = ..., security_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., service_discovery: Optional[pulumi.Input[Union[SecurityGatewayServiceDiscoveryArgs, SecurityGatewayServiceDiscoveryArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SecurityGatewayArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., delegating_service_account: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., external_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., hubs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SecurityGatewayHubArgs, SecurityGatewayHubArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging: Optional[pulumi.Input[Union[SecurityGatewayLoggingArgs, SecurityGatewayLoggingArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy_protocol_config: Optional[pulumi.Input[Union[SecurityGatewayProxyProtocolConfigArgs, SecurityGatewayProxyProtocolConfigArgsDict]]] = ..., security_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., service_discovery: Optional[pulumi.Input[Union[SecurityGatewayServiceDiscoveryArgs, SecurityGatewayServiceDiscoveryArgsDict]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> SecurityGateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatingServiceAccount")
    def delegating_service_account(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIps")
    def external_ips(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hubs(self) -> pulumi.Output[Optional[Sequence[outputs.SecurityGatewayHub]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logging(self) -> pulumi.Output[Optional[outputs.SecurityGatewayLogging]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyProtocolConfig")
    def proxy_protocol_config(self) -> pulumi.Output[Optional[outputs.SecurityGatewayProxyProtocolConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGatewayId")
    def security_gateway_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDiscovery")
    def service_discovery(self) -> pulumi.Output[Optional[outputs.SecurityGatewayServiceDiscovery]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


