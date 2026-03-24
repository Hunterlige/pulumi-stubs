

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
__all__ = ['ServiceAttachmentArgs', 'ServiceAttachment']
@pulumi.input_type
class ServiceAttachmentArgs:
    def __init__(__self__, *, connection_preference: pulumi.Input[_builtins.str], enable_proxy_protocol: pulumi.Input[_builtins.bool], nat_subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], target_service: pulumi.Input[_builtins.str], consumer_accept_lists: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttachmentConsumerAcceptListArgs]]]] = ..., consumer_reject_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., propagated_connection_limit: Optional[pulumi.Input[_builtins.int]] = ..., reconcile_connections: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., send_propagated_connection_limit_if_zero: Optional[pulumi.Input[_builtins.bool]] = ..., show_nat_ips: Optional[pulumi.Input[_builtins.bool]] = ..., tunneling_config: Optional[pulumi.Input[ServiceAttachmentTunnelingConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPreference")
    def connection_preference(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connection_preference.setter
    def connection_preference(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableProxyProtocol")
    def enable_proxy_protocol(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_proxy_protocol.setter
    def enable_proxy_protocol(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natSubnets")
    def nat_subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @nat_subnets.setter
    def nat_subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetService")
    def target_service(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_service.setter
    def target_service(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerAcceptLists")
    def consumer_accept_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttachmentConsumerAcceptListArgs]]]]:
        
        ...
    
    @consumer_accept_lists.setter
    def consumer_accept_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttachmentConsumerAcceptListArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerRejectLists")
    def consumer_reject_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @consumer_reject_lists.setter
    def consumer_reject_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNames")
    def domain_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @domain_names.setter
    def domain_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="propagatedConnectionLimit")
    def propagated_connection_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @propagated_connection_limit.setter
    def propagated_connection_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reconcileConnections")
    def reconcile_connections(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @reconcile_connections.setter
    def reconcile_connections(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendPropagatedConnectionLimitIfZero")
    def send_propagated_connection_limit_if_zero(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @send_propagated_connection_limit_if_zero.setter
    def send_propagated_connection_limit_if_zero(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="showNatIps")
    def show_nat_ips(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @show_nat_ips.setter
    def show_nat_ips(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tunnelingConfig")
    def tunneling_config(self) -> Optional[pulumi.Input[ServiceAttachmentTunnelingConfigArgs]]:
        
        ...
    
    @tunneling_config.setter
    def tunneling_config(self, value: Optional[pulumi.Input[ServiceAttachmentTunnelingConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ServiceAttachmentState:
    def __init__(__self__, *, connected_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttachmentConnectedEndpointArgs]]]] = ..., connection_preference: Optional[pulumi.Input[_builtins.str]] = ..., consumer_accept_lists: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttachmentConsumerAcceptListArgs]]]] = ..., consumer_reject_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enable_proxy_protocol: Optional[pulumi.Input[_builtins.bool]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nat_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., propagated_connection_limit: Optional[pulumi.Input[_builtins.int]] = ..., psc_service_attachment_ids: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttachmentPscServiceAttachmentIdArgs]]]] = ..., reconcile_connections: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., send_propagated_connection_limit_if_zero: Optional[pulumi.Input[_builtins.bool]] = ..., show_nat_ips: Optional[pulumi.Input[_builtins.bool]] = ..., target_service: Optional[pulumi.Input[_builtins.str]] = ..., tunneling_config: Optional[pulumi.Input[ServiceAttachmentTunnelingConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedEndpoints")
    def connected_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttachmentConnectedEndpointArgs]]]]:
        
        ...
    
    @connected_endpoints.setter
    def connected_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttachmentConnectedEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPreference")
    def connection_preference(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_preference.setter
    def connection_preference(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerAcceptLists")
    def consumer_accept_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttachmentConsumerAcceptListArgs]]]]:
        
        ...
    
    @consumer_accept_lists.setter
    def consumer_accept_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttachmentConsumerAcceptListArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerRejectLists")
    def consumer_reject_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @consumer_reject_lists.setter
    def consumer_reject_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNames")
    def domain_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @domain_names.setter
    def domain_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableProxyProtocol")
    def enable_proxy_protocol(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_proxy_protocol.setter
    def enable_proxy_protocol(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natSubnets")
    def nat_subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @nat_subnets.setter
    def nat_subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagatedConnectionLimit")
    def propagated_connection_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @propagated_connection_limit.setter
    def propagated_connection_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscServiceAttachmentIds")
    def psc_service_attachment_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttachmentPscServiceAttachmentIdArgs]]]]:
        
        ...
    
    @psc_service_attachment_ids.setter
    def psc_service_attachment_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttachmentPscServiceAttachmentIdArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reconcileConnections")
    def reconcile_connections(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @reconcile_connections.setter
    def reconcile_connections(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter(name="sendPropagatedConnectionLimitIfZero")
    def send_propagated_connection_limit_if_zero(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @send_propagated_connection_limit_if_zero.setter
    def send_propagated_connection_limit_if_zero(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="showNatIps")
    def show_nat_ips(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @show_nat_ips.setter
    def show_nat_ips(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetService")
    def target_service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_service.setter
    def target_service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tunnelingConfig")
    def tunneling_config(self) -> Optional[pulumi.Input[ServiceAttachmentTunnelingConfigArgs]]:
        
        ...
    
    @tunneling_config.setter
    def tunneling_config(self, value: Optional[pulumi.Input[ServiceAttachmentTunnelingConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/serviceAttachment:ServiceAttachment")
class ServiceAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., connection_preference: Optional[pulumi.Input[_builtins.str]] = ..., consumer_accept_lists: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceAttachmentConsumerAcceptListArgs, ServiceAttachmentConsumerAcceptListArgsDict]]]]] = ..., consumer_reject_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enable_proxy_protocol: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nat_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., propagated_connection_limit: Optional[pulumi.Input[_builtins.int]] = ..., reconcile_connections: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., send_propagated_connection_limit_if_zero: Optional[pulumi.Input[_builtins.bool]] = ..., show_nat_ips: Optional[pulumi.Input[_builtins.bool]] = ..., target_service: Optional[pulumi.Input[_builtins.str]] = ..., tunneling_config: Optional[pulumi.Input[Union[ServiceAttachmentTunnelingConfigArgs, ServiceAttachmentTunnelingConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ServiceAttachmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., connected_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceAttachmentConnectedEndpointArgs, ServiceAttachmentConnectedEndpointArgsDict]]]]] = ..., connection_preference: Optional[pulumi.Input[_builtins.str]] = ..., consumer_accept_lists: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceAttachmentConsumerAcceptListArgs, ServiceAttachmentConsumerAcceptListArgsDict]]]]] = ..., consumer_reject_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enable_proxy_protocol: Optional[pulumi.Input[_builtins.bool]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nat_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., propagated_connection_limit: Optional[pulumi.Input[_builtins.int]] = ..., psc_service_attachment_ids: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceAttachmentPscServiceAttachmentIdArgs, ServiceAttachmentPscServiceAttachmentIdArgsDict]]]]] = ..., reconcile_connections: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., send_propagated_connection_limit_if_zero: Optional[pulumi.Input[_builtins.bool]] = ..., show_nat_ips: Optional[pulumi.Input[_builtins.bool]] = ..., target_service: Optional[pulumi.Input[_builtins.str]] = ..., tunneling_config: Optional[pulumi.Input[Union[ServiceAttachmentTunnelingConfigArgs, ServiceAttachmentTunnelingConfigArgsDict]]] = ...) -> ServiceAttachment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedEndpoints")
    def connected_endpoints(self) -> pulumi.Output[Sequence[outputs.ServiceAttachmentConnectedEndpoint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPreference")
    def connection_preference(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerAcceptLists")
    def consumer_accept_lists(self) -> pulumi.Output[Optional[Sequence[outputs.ServiceAttachmentConsumerAcceptList]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerRejectLists")
    def consumer_reject_lists(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNames")
    def domain_names(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableProxyProtocol")
    def enable_proxy_protocol(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="natSubnets")
    def nat_subnets(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagatedConnectionLimit")
    def propagated_connection_limit(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscServiceAttachmentIds")
    def psc_service_attachment_ids(self) -> pulumi.Output[Sequence[outputs.ServiceAttachmentPscServiceAttachmentId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reconcileConnections")
    def reconcile_connections(self) -> pulumi.Output[_builtins.bool]:
        
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
    @pulumi.getter(name="sendPropagatedConnectionLimitIfZero")
    def send_propagated_connection_limit_if_zero(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="showNatIps")
    def show_nat_ips(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetService")
    def target_service(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tunnelingConfig")
    def tunneling_config(self) -> pulumi.Output[Optional[outputs.ServiceAttachmentTunnelingConfig]]:
        
        ...
    


