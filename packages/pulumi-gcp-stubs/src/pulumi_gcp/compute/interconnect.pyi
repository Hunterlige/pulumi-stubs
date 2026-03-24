

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
__all__ = ['InterconnectArgs', 'Interconnect']
@pulumi.input_type
class InterconnectArgs:
    def __init__(__self__, *, interconnect_type: pulumi.Input[_builtins.str], link_type: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], requested_link_count: pulumi.Input[_builtins.int], aai_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., admin_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., application_aware_interconnect: Optional[pulumi.Input[InterconnectApplicationAwareInterconnectArgs]] = ..., customer_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., macsec: Optional[pulumi.Input[InterconnectMacsecArgs]] = ..., macsec_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., noc_contact_email: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[InterconnectParamsArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., remote_location: Optional[pulumi.Input[_builtins.str]] = ..., requested_features: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interconnectType")
    def interconnect_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @interconnect_type.setter
    def interconnect_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkType")
    def link_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @link_type.setter
    def link_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedLinkCount")
    def requested_link_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @requested_link_count.setter
    def requested_link_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aaiEnabled")
    def aai_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @aai_enabled.setter
    def aai_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminEnabled")
    def admin_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @admin_enabled.setter
    def admin_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationAwareInterconnect")
    def application_aware_interconnect(self) -> Optional[pulumi.Input[InterconnectApplicationAwareInterconnectArgs]]:
        
        ...
    
    @application_aware_interconnect.setter
    def application_aware_interconnect(self, value: Optional[pulumi.Input[InterconnectApplicationAwareInterconnectArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerName")
    def customer_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_name.setter
    def customer_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def macsec(self) -> Optional[pulumi.Input[InterconnectMacsecArgs]]:
        
        ...
    
    @macsec.setter
    def macsec(self, value: Optional[pulumi.Input[InterconnectMacsecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="macsecEnabled")
    def macsec_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @macsec_enabled.setter
    def macsec_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nocContactEmail")
    def noc_contact_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @noc_contact_email.setter
    def noc_contact_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[InterconnectParamsArgs]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[InterconnectParamsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteLocation")
    def remote_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @remote_location.setter
    def remote_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedFeatures")
    def requested_features(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @requested_features.setter
    def requested_features(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _InterconnectState:
    def __init__(__self__, *, aai_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., admin_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., application_aware_interconnect: Optional[pulumi.Input[InterconnectApplicationAwareInterconnectArgs]] = ..., available_features: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., circuit_infos: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectCircuitInfoArgs]]]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., customer_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., expected_outages: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectExpectedOutageArgs]]]] = ..., google_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., google_reference_id: Optional[pulumi.Input[_builtins.str]] = ..., interconnect_attachments: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., interconnect_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., interconnect_type: Optional[pulumi.Input[_builtins.str]] = ..., label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., link_type: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., macsec: Optional[pulumi.Input[InterconnectMacsecArgs]] = ..., macsec_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., noc_contact_email: Optional[pulumi.Input[_builtins.str]] = ..., operational_status: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[InterconnectParamsArgs]] = ..., peer_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., provisioned_link_count: Optional[pulumi.Input[_builtins.int]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., remote_location: Optional[pulumi.Input[_builtins.str]] = ..., requested_features: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., requested_link_count: Optional[pulumi.Input[_builtins.int]] = ..., satisfies_pzs: Optional[pulumi.Input[_builtins.bool]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., wire_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aaiEnabled")
    def aai_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @aai_enabled.setter
    def aai_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminEnabled")
    def admin_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @admin_enabled.setter
    def admin_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationAwareInterconnect")
    def application_aware_interconnect(self) -> Optional[pulumi.Input[InterconnectApplicationAwareInterconnectArgs]]:
        
        ...
    
    @application_aware_interconnect.setter
    def application_aware_interconnect(self, value: Optional[pulumi.Input[InterconnectApplicationAwareInterconnectArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableFeatures")
    def available_features(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @available_features.setter
    def available_features(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="circuitInfos")
    def circuit_infos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectCircuitInfoArgs]]]]:
        
        ...
    
    @circuit_infos.setter
    def circuit_infos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectCircuitInfoArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerName")
    def customer_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_name.setter
    def customer_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="expectedOutages")
    def expected_outages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectExpectedOutageArgs]]]]:
        
        ...
    
    @expected_outages.setter
    def expected_outages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InterconnectExpectedOutageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleIpAddress")
    def google_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @google_ip_address.setter
    def google_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleReferenceId")
    def google_reference_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @google_reference_id.setter
    def google_reference_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interconnectAttachments")
    def interconnect_attachments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @interconnect_attachments.setter
    def interconnect_attachments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interconnectGroups")
    def interconnect_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @interconnect_groups.setter
    def interconnect_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interconnectType")
    def interconnect_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interconnect_type.setter
    def interconnect_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="linkType")
    def link_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @link_type.setter
    def link_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def macsec(self) -> Optional[pulumi.Input[InterconnectMacsecArgs]]:
        
        ...
    
    @macsec.setter
    def macsec(self, value: Optional[pulumi.Input[InterconnectMacsecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="macsecEnabled")
    def macsec_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @macsec_enabled.setter
    def macsec_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nocContactEmail")
    def noc_contact_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @noc_contact_email.setter
    def noc_contact_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationalStatus")
    def operational_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @operational_status.setter
    def operational_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[InterconnectParamsArgs]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[InterconnectParamsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpAddress")
    def peer_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_ip_address.setter
    def peer_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedLinkCount")
    def provisioned_link_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @provisioned_link_count.setter
    def provisioned_link_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteLocation")
    def remote_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @remote_location.setter
    def remote_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedFeatures")
    def requested_features(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @requested_features.setter
    def requested_features(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedLinkCount")
    def requested_link_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @requested_link_count.setter
    def requested_link_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="satisfiesPzs")
    def satisfies_pzs(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @satisfies_pzs.setter
    def satisfies_pzs(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="wireGroups")
    def wire_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @wire_groups.setter
    def wire_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/interconnect:Interconnect")
class Interconnect(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aai_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., admin_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., application_aware_interconnect: Optional[pulumi.Input[Union[InterconnectApplicationAwareInterconnectArgs, InterconnectApplicationAwareInterconnectArgsDict]]] = ..., customer_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., interconnect_type: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., link_type: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., macsec: Optional[pulumi.Input[Union[InterconnectMacsecArgs, InterconnectMacsecArgsDict]]] = ..., macsec_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., noc_contact_email: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Union[InterconnectParamsArgs, InterconnectParamsArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., remote_location: Optional[pulumi.Input[_builtins.str]] = ..., requested_features: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., requested_link_count: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InterconnectArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., aai_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., admin_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., application_aware_interconnect: Optional[pulumi.Input[Union[InterconnectApplicationAwareInterconnectArgs, InterconnectApplicationAwareInterconnectArgsDict]]] = ..., available_features: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., circuit_infos: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InterconnectCircuitInfoArgs, InterconnectCircuitInfoArgsDict]]]]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., customer_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., expected_outages: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InterconnectExpectedOutageArgs, InterconnectExpectedOutageArgsDict]]]]] = ..., google_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., google_reference_id: Optional[pulumi.Input[_builtins.str]] = ..., interconnect_attachments: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., interconnect_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., interconnect_type: Optional[pulumi.Input[_builtins.str]] = ..., label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., link_type: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., macsec: Optional[pulumi.Input[Union[InterconnectMacsecArgs, InterconnectMacsecArgsDict]]] = ..., macsec_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., noc_contact_email: Optional[pulumi.Input[_builtins.str]] = ..., operational_status: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Union[InterconnectParamsArgs, InterconnectParamsArgsDict]]] = ..., peer_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., provisioned_link_count: Optional[pulumi.Input[_builtins.int]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., remote_location: Optional[pulumi.Input[_builtins.str]] = ..., requested_features: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., requested_link_count: Optional[pulumi.Input[_builtins.int]] = ..., satisfies_pzs: Optional[pulumi.Input[_builtins.bool]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., wire_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> Interconnect:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aaiEnabled")
    def aai_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminEnabled")
    def admin_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationAwareInterconnect")
    def application_aware_interconnect(self) -> pulumi.Output[Optional[outputs.InterconnectApplicationAwareInterconnect]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableFeatures")
    def available_features(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="circuitInfos")
    def circuit_infos(self) -> pulumi.Output[Sequence[outputs.InterconnectCircuitInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerName")
    def customer_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="expectedOutages")
    def expected_outages(self) -> pulumi.Output[Sequence[outputs.InterconnectExpectedOutage]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleIpAddress")
    def google_ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleReferenceId")
    def google_reference_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interconnectAttachments")
    def interconnect_attachments(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interconnectGroups")
    def interconnect_groups(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interconnectType")
    def interconnect_type(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="linkType")
    def link_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def macsec(self) -> pulumi.Output[Optional[outputs.InterconnectMacsec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="macsecEnabled")
    def macsec_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nocContactEmail")
    def noc_contact_email(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationalStatus")
    def operational_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Output[Optional[outputs.InterconnectParams]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpAddress")
    def peer_ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedLinkCount")
    def provisioned_link_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteLocation")
    def remote_location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedFeatures")
    def requested_features(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedLinkCount")
    def requested_link_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="satisfiesPzs")
    def satisfies_pzs(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wireGroups")
    def wire_groups(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    


