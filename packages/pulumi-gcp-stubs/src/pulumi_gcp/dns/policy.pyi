

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
__all__ = ['PolicyArgs', 'Policy']
@pulumi.input_type
class PolicyArgs:
    def __init__(__self__, *, alternative_name_server_config: Optional[pulumi.Input[PolicyAlternativeNameServerConfigArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dns64_config: Optional[pulumi.Input[PolicyDns64ConfigArgs]] = ..., enable_inbound_forwarding: Optional[pulumi.Input[_builtins.bool]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyNetworkArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternativeNameServerConfig")
    def alternative_name_server_config(self) -> Optional[pulumi.Input[PolicyAlternativeNameServerConfigArgs]]:
        
        ...
    
    @alternative_name_server_config.setter
    def alternative_name_server_config(self, value: Optional[pulumi.Input[PolicyAlternativeNameServerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dns64Config")
    def dns64_config(self) -> Optional[pulumi.Input[PolicyDns64ConfigArgs]]:
        
        ...
    
    @dns64_config.setter
    def dns64_config(self, value: Optional[pulumi.Input[PolicyDns64ConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInboundForwarding")
    def enable_inbound_forwarding(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_inbound_forwarding.setter
    def enable_inbound_forwarding(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_logging.setter
    def enable_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicyNetworkArgs]]]]:
        
        ...
    
    @networks.setter
    def networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyNetworkArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _PolicyState:
    def __init__(__self__, *, alternative_name_server_config: Optional[pulumi.Input[PolicyAlternativeNameServerConfigArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dns64_config: Optional[pulumi.Input[PolicyDns64ConfigArgs]] = ..., enable_inbound_forwarding: Optional[pulumi.Input[_builtins.bool]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyNetworkArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternativeNameServerConfig")
    def alternative_name_server_config(self) -> Optional[pulumi.Input[PolicyAlternativeNameServerConfigArgs]]:
        
        ...
    
    @alternative_name_server_config.setter
    def alternative_name_server_config(self, value: Optional[pulumi.Input[PolicyAlternativeNameServerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dns64Config")
    def dns64_config(self) -> Optional[pulumi.Input[PolicyDns64ConfigArgs]]:
        
        ...
    
    @dns64_config.setter
    def dns64_config(self, value: Optional[pulumi.Input[PolicyDns64ConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInboundForwarding")
    def enable_inbound_forwarding(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_inbound_forwarding.setter
    def enable_inbound_forwarding(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_logging.setter
    def enable_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicyNetworkArgs]]]]:
        
        ...
    
    @networks.setter
    def networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyNetworkArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:dns/policy:Policy")
class Policy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., alternative_name_server_config: Optional[pulumi.Input[Union[PolicyAlternativeNameServerConfigArgs, PolicyAlternativeNameServerConfigArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dns64_config: Optional[pulumi.Input[Union[PolicyDns64ConfigArgs, PolicyDns64ConfigArgsDict]]] = ..., enable_inbound_forwarding: Optional[pulumi.Input[_builtins.bool]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PolicyNetworkArgs, PolicyNetworkArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[PolicyArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., alternative_name_server_config: Optional[pulumi.Input[Union[PolicyAlternativeNameServerConfigArgs, PolicyAlternativeNameServerConfigArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dns64_config: Optional[pulumi.Input[Union[PolicyDns64ConfigArgs, PolicyDns64ConfigArgsDict]]] = ..., enable_inbound_forwarding: Optional[pulumi.Input[_builtins.bool]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PolicyNetworkArgs, PolicyNetworkArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> Policy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternativeNameServerConfig")
    def alternative_name_server_config(self) -> pulumi.Output[Optional[outputs.PolicyAlternativeNameServerConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dns64Config")
    def dns64_config(self) -> pulumi.Output[outputs.PolicyDns64Config]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInboundForwarding")
    def enable_inbound_forwarding(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def networks(self) -> pulumi.Output[Optional[Sequence[outputs.PolicyNetwork]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


