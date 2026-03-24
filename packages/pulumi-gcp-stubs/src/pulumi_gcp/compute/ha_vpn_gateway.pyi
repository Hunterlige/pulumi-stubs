

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['HaVpnGatewayArgs', 'HaVpnGateway']
@pulumi.input_type
class HaVpnGatewayArgs:
    def __init__(__self__, *, network: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., gateway_ip_version: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[HaVpnGatewayParamsArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ..., vpn_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[HaVpnGatewayVpnInterfaceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayIpVersion")
    def gateway_ip_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_ip_version.setter
    def gateway_ip_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    def params(self) -> Optional[pulumi.Input[HaVpnGatewayParamsArgs]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[HaVpnGatewayParamsArgs]]): # -> None:
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
    @pulumi.getter(name="stackType")
    def stack_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_type.setter
    def stack_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnInterfaces")
    def vpn_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[HaVpnGatewayVpnInterfaceArgs]]]]:
        
        ...
    
    @vpn_interfaces.setter
    def vpn_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HaVpnGatewayVpnInterfaceArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _HaVpnGatewayState:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., gateway_ip_version: Optional[pulumi.Input[_builtins.str]] = ..., label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[HaVpnGatewayParamsArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ..., vpn_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[HaVpnGatewayVpnInterfaceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayIpVersion")
    def gateway_ip_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_ip_version.setter
    def gateway_ip_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @label_fingerprint.setter
    def label_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    def params(self) -> Optional[pulumi.Input[HaVpnGatewayParamsArgs]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[HaVpnGatewayParamsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="stackType")
    def stack_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_type.setter
    def stack_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnInterfaces")
    def vpn_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[HaVpnGatewayVpnInterfaceArgs]]]]:
        
        ...
    
    @vpn_interfaces.setter
    def vpn_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HaVpnGatewayVpnInterfaceArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/haVpnGateway:HaVpnGateway")
class HaVpnGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., gateway_ip_version: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Union[HaVpnGatewayParamsArgs, HaVpnGatewayParamsArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ..., vpn_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union[HaVpnGatewayVpnInterfaceArgs, HaVpnGatewayVpnInterfaceArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: HaVpnGatewayArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., gateway_ip_version: Optional[pulumi.Input[_builtins.str]] = ..., label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Union[HaVpnGatewayParamsArgs, HaVpnGatewayParamsArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ..., vpn_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union[HaVpnGatewayVpnInterfaceArgs, HaVpnGatewayVpnInterfaceArgsDict]]]]] = ...) -> HaVpnGateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayIpVersion")
    def gateway_ip_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
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
    def params(self) -> pulumi.Output[Optional[outputs.HaVpnGatewayParams]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
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
    @pulumi.getter(name="stackType")
    def stack_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnInterfaces")
    def vpn_interfaces(self) -> pulumi.Output[Sequence[outputs.HaVpnGatewayVpnInterface]]:
        
        ...
    


