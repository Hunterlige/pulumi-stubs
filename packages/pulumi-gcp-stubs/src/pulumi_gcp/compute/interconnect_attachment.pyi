

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
__all__ = ['InterconnectAttachmentArgs', 'InterconnectAttachment']
@pulumi.input_type
class InterconnectAttachmentArgs:
    def __init__(__self__, *, admin_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., bandwidth: Optional[pulumi.Input[_builtins.str]] = ..., candidate_cloud_router_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_cloud_router_ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_customer_router_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_customer_router_ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., edge_availability_domain: Optional[pulumi.Input[_builtins.str]] = ..., encryption: Optional[pulumi.Input[_builtins.str]] = ..., interconnect: Optional[pulumi.Input[_builtins.str]] = ..., ipsec_internal_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., l2_forwarding: Optional[pulumi.Input[InterconnectAttachmentL2ForwardingArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., mtu: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[InterconnectAttachmentParamsArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., router: Optional[pulumi.Input[_builtins.str]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ..., subnet_length: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vlan_tag8021q: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminEnabled")
    def admin_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @admin_enabled.setter
    def admin_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bandwidth(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bandwidth.setter
    def bandwidth(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="candidateCloudRouterIpAddress")
    def candidate_cloud_router_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @candidate_cloud_router_ip_address.setter
    def candidate_cloud_router_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="candidateCloudRouterIpv6Address")
    def candidate_cloud_router_ipv6_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @candidate_cloud_router_ipv6_address.setter
    def candidate_cloud_router_ipv6_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="candidateCustomerRouterIpAddress")
    def candidate_customer_router_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @candidate_customer_router_ip_address.setter
    def candidate_customer_router_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="candidateCustomerRouterIpv6Address")
    def candidate_customer_router_ipv6_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @candidate_customer_router_ipv6_address.setter
    def candidate_customer_router_ipv6_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="candidateSubnets")
    def candidate_subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @candidate_subnets.setter
    def candidate_subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgeAvailabilityDomain")
    def edge_availability_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @edge_availability_domain.setter
    def edge_availability_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def interconnect(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interconnect.setter
    def interconnect(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipsecInternalAddresses")
    def ipsec_internal_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipsec_internal_addresses.setter
    def ipsec_internal_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="l2Forwarding")
    def l2_forwarding(self) -> Optional[pulumi.Input[InterconnectAttachmentL2ForwardingArgs]]:
        
        ...
    
    @l2_forwarding.setter
    def l2_forwarding(self, value: Optional[pulumi.Input[InterconnectAttachmentL2ForwardingArgs]]): # -> None:
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
    def mtu(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def params(self) -> Optional[pulumi.Input[InterconnectAttachmentParamsArgs]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[InterconnectAttachmentParamsArgs]]): # -> None:
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
    @pulumi.getter(name="stackType")
    def stack_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_type.setter
    def stack_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetLength")
    def subnet_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @subnet_length.setter
    def subnet_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vlanTag8021q")
    def vlan_tag8021q(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @vlan_tag8021q.setter
    def vlan_tag8021q(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.input_type
class _InterconnectAttachmentState:
    def __init__(__self__, *, admin_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., attachment_group: Optional[pulumi.Input[_builtins.str]] = ..., bandwidth: Optional[pulumi.Input[_builtins.str]] = ..., candidate_cloud_router_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_cloud_router_ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_customer_router_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_customer_router_ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cloud_router_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., cloud_router_ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., customer_router_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., customer_router_ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., edge_availability_domain: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., encryption: Optional[pulumi.Input[_builtins.str]] = ..., google_reference_id: Optional[pulumi.Input[_builtins.str]] = ..., interconnect: Optional[pulumi.Input[_builtins.str]] = ..., ipsec_internal_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., l2_forwarding: Optional[pulumi.Input[InterconnectAttachmentL2ForwardingArgs]] = ..., label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., mtu: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pairing_key: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[InterconnectAttachmentParamsArgs]] = ..., partner_asn: Optional[pulumi.Input[_builtins.str]] = ..., private_interconnect_infos: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectAttachmentPrivateInterconnectInfoArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., router: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., subnet_length: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vlan_tag8021q: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminEnabled")
    def admin_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @admin_enabled.setter
    def admin_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentGroup")
    def attachment_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @attachment_group.setter
    def attachment_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bandwidth(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bandwidth.setter
    def bandwidth(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="candidateCloudRouterIpAddress")
    def candidate_cloud_router_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @candidate_cloud_router_ip_address.setter
    def candidate_cloud_router_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="candidateCloudRouterIpv6Address")
    def candidate_cloud_router_ipv6_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @candidate_cloud_router_ipv6_address.setter
    def candidate_cloud_router_ipv6_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="candidateCustomerRouterIpAddress")
    def candidate_customer_router_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @candidate_customer_router_ip_address.setter
    def candidate_customer_router_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="candidateCustomerRouterIpv6Address")
    def candidate_customer_router_ipv6_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @candidate_customer_router_ipv6_address.setter
    def candidate_customer_router_ipv6_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="candidateSubnets")
    def candidate_subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @candidate_subnets.setter
    def candidate_subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudRouterIpAddress")
    def cloud_router_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloud_router_ip_address.setter
    def cloud_router_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudRouterIpv6Address")
    def cloud_router_ipv6_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloud_router_ipv6_address.setter
    def cloud_router_ipv6_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerRouterIpAddress")
    def customer_router_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_router_ip_address.setter
    def customer_router_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerRouterIpv6Address")
    def customer_router_ipv6_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_router_ipv6_address.setter
    def customer_router_ipv6_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgeAvailabilityDomain")
    def edge_availability_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @edge_availability_domain.setter
    def edge_availability_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleReferenceId")
    def google_reference_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @google_reference_id.setter
    def google_reference_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def interconnect(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interconnect.setter
    def interconnect(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipsecInternalAddresses")
    def ipsec_internal_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipsec_internal_addresses.setter
    def ipsec_internal_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="l2Forwarding")
    def l2_forwarding(self) -> Optional[pulumi.Input[InterconnectAttachmentL2ForwardingArgs]]:
        
        ...
    
    @l2_forwarding.setter
    def l2_forwarding(self, value: Optional[pulumi.Input[InterconnectAttachmentL2ForwardingArgs]]): # -> None:
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
    def mtu(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pairingKey")
    def pairing_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pairing_key.setter
    def pairing_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[InterconnectAttachmentParamsArgs]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[InterconnectAttachmentParamsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerAsn")
    def partner_asn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @partner_asn.setter
    def partner_asn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateInterconnectInfos")
    def private_interconnect_infos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectAttachmentPrivateInterconnectInfoArgs]]]]:
        
        ...
    
    @private_interconnect_infos.setter
    def private_interconnect_infos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectAttachmentPrivateInterconnectInfoArgs]]]]): # -> None:
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
    @pulumi.getter
    def router(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @router.setter
    def router(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetLength")
    def subnet_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @subnet_length.setter
    def subnet_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vlanTag8021q")
    def vlan_tag8021q(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @vlan_tag8021q.setter
    def vlan_tag8021q(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token(...)
class InterconnectAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., admin_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., bandwidth: Optional[pulumi.Input[_builtins.str]] = ..., candidate_cloud_router_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_cloud_router_ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_customer_router_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_customer_router_ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., edge_availability_domain: Optional[pulumi.Input[_builtins.str]] = ..., encryption: Optional[pulumi.Input[_builtins.str]] = ..., interconnect: Optional[pulumi.Input[_builtins.str]] = ..., ipsec_internal_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., l2_forwarding: Optional[pulumi.Input[Union[InterconnectAttachmentL2ForwardingArgs, InterconnectAttachmentL2ForwardingArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., mtu: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Union[InterconnectAttachmentParamsArgs, InterconnectAttachmentParamsArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., router: Optional[pulumi.Input[_builtins.str]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ..., subnet_length: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vlan_tag8021q: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[InterconnectAttachmentArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., admin_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., attachment_group: Optional[pulumi.Input[_builtins.str]] = ..., bandwidth: Optional[pulumi.Input[_builtins.str]] = ..., candidate_cloud_router_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_cloud_router_ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_customer_router_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_customer_router_ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., candidate_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cloud_router_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., cloud_router_ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., customer_router_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., customer_router_ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., edge_availability_domain: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., encryption: Optional[pulumi.Input[_builtins.str]] = ..., google_reference_id: Optional[pulumi.Input[_builtins.str]] = ..., interconnect: Optional[pulumi.Input[_builtins.str]] = ..., ipsec_internal_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., l2_forwarding: Optional[pulumi.Input[Union[InterconnectAttachmentL2ForwardingArgs, InterconnectAttachmentL2ForwardingArgsDict]]] = ..., label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., mtu: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pairing_key: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Union[InterconnectAttachmentParamsArgs, InterconnectAttachmentParamsArgsDict]]] = ..., partner_asn: Optional[pulumi.Input[_builtins.str]] = ..., private_interconnect_infos: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InterconnectAttachmentPrivateInterconnectInfoArgs, InterconnectAttachmentPrivateInterconnectInfoArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., router: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., subnet_length: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vlan_tag8021q: Optional[pulumi.Input[_builtins.int]] = ...) -> InterconnectAttachment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminEnabled")
    def admin_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentGroup")
    def attachment_group(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bandwidth(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="candidateCloudRouterIpAddress")
    def candidate_cloud_router_ip_address(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="candidateCloudRouterIpv6Address")
    def candidate_cloud_router_ipv6_address(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="candidateCustomerRouterIpAddress")
    def candidate_customer_router_ip_address(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="candidateCustomerRouterIpv6Address")
    def candidate_customer_router_ipv6_address(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="candidateSubnets")
    def candidate_subnets(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudRouterIpAddress")
    def cloud_router_ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudRouterIpv6Address")
    def cloud_router_ipv6_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerRouterIpAddress")
    def customer_router_ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerRouterIpv6Address")
    def customer_router_ipv6_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgeAvailabilityDomain")
    def edge_availability_domain(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleReferenceId")
    def google_reference_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interconnect(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipsecInternalAddresses")
    def ipsec_internal_addresses(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="l2Forwarding")
    def l2_forwarding(self) -> pulumi.Output[Optional[outputs.InterconnectAttachmentL2Forwarding]]:
        
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
    def mtu(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pairingKey")
    def pairing_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Output[Optional[outputs.InterconnectAttachmentParams]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerAsn")
    def partner_asn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateInterconnectInfos")
    def private_interconnect_infos(self) -> pulumi.Output[Sequence[outputs.InterconnectAttachmentPrivateInterconnectInfo]]:
        
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
    @pulumi.getter
    def router(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetLength")
    def subnet_length(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vlanTag8021q")
    def vlan_tag8021q(self) -> pulumi.Output[_builtins.int]:
        
        ...
    


