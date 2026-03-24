

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
__all__ = ['NetworkArgs', 'Network']
@pulumi.input_type
class NetworkArgs:
    def __init__(__self__, *, availability_zone_id: pulumi.Input[_builtins.str], backup_subnet_cidr: pulumi.Input[_builtins.str], client_subnet_cidr: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], s3_access: pulumi.Input[_builtins.str], zero_etl_access: pulumi.Input[_builtins.str], availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., default_dns_prefix: Optional[pulumi.Input[_builtins.str]] = ..., delete_associated_resources: Optional[pulumi.Input[_builtins.bool]] = ..., kms_access: Optional[pulumi.Input[_builtins.str]] = ..., kms_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., sts_access: Optional[pulumi.Input[_builtins.str]] = ..., sts_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[NetworkTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @availability_zone_id.setter
    def availability_zone_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSubnetCidr")
    def backup_subnet_cidr(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @backup_subnet_cidr.setter
    def backup_subnet_cidr(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSubnetCidr")
    def client_subnet_cidr(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_subnet_cidr.setter
    def client_subnet_cidr(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Access")
    def s3_access(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_access.setter
    def s3_access(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zeroEtlAccess")
    def zero_etl_access(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @zero_etl_access.setter
    def zero_etl_access(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_domain_name.setter
    def custom_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDnsPrefix")
    def default_dns_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_dns_prefix.setter
    def default_dns_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAssociatedResources")
    def delete_associated_resources(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_associated_resources.setter
    def delete_associated_resources(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsAccess")
    def kms_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_access.setter
    def kms_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsPolicyDocument")
    def kms_policy_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_policy_document.setter
    def kms_policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3PolicyDocument")
    def s3_policy_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_policy_document.setter
    def s3_policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stsAccess")
    def sts_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sts_access.setter
    def sts_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stsPolicyDocument")
    def sts_policy_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sts_policy_document.setter
    def sts_policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[NetworkTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[NetworkTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _NetworkState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., backup_subnet_cidr: Optional[pulumi.Input[_builtins.str]] = ..., client_subnet_cidr: Optional[pulumi.Input[_builtins.str]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., default_dns_prefix: Optional[pulumi.Input[_builtins.str]] = ..., delete_associated_resources: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., kms_access: Optional[pulumi.Input[_builtins.str]] = ..., kms_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., managed_services: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkManagedServiceArgs]]]] = ..., oci_dns_forwarding_configs: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkOciDnsForwardingConfigArgs]]]] = ..., oci_network_anchor_id: Optional[pulumi.Input[_builtins.str]] = ..., oci_network_anchor_url: Optional[pulumi.Input[_builtins.str]] = ..., oci_resource_anchor_name: Optional[pulumi.Input[_builtins.str]] = ..., oci_vcn_id: Optional[pulumi.Input[_builtins.str]] = ..., oci_vcn_url: Optional[pulumi.Input[_builtins.str]] = ..., peered_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., percent_progress: Optional[pulumi.Input[_builtins.float]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_access: Optional[pulumi.Input[_builtins.str]] = ..., s3_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., status_reason: Optional[pulumi.Input[_builtins.str]] = ..., sts_access: Optional[pulumi.Input[_builtins.str]] = ..., sts_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[NetworkTimeoutsArgs]] = ..., zero_etl_access: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone_id.setter
    def availability_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSubnetCidr")
    def backup_subnet_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_subnet_cidr.setter
    def backup_subnet_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSubnetCidr")
    def client_subnet_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_subnet_cidr.setter
    def client_subnet_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_domain_name.setter
    def custom_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDnsPrefix")
    def default_dns_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_dns_prefix.setter
    def default_dns_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAssociatedResources")
    def delete_associated_resources(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_associated_resources.setter
    def delete_associated_resources(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsAccess")
    def kms_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_access.setter
    def kms_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsPolicyDocument")
    def kms_policy_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_policy_document.setter
    def kms_policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedServices")
    def managed_services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkManagedServiceArgs]]]]:
        
        ...
    
    @managed_services.setter
    def managed_services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkManagedServiceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociDnsForwardingConfigs")
    def oci_dns_forwarding_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkOciDnsForwardingConfigArgs]]]]:
        
        ...
    
    @oci_dns_forwarding_configs.setter
    def oci_dns_forwarding_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkOciDnsForwardingConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociNetworkAnchorId")
    def oci_network_anchor_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oci_network_anchor_id.setter
    def oci_network_anchor_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociNetworkAnchorUrl")
    def oci_network_anchor_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oci_network_anchor_url.setter
    def oci_network_anchor_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oci_resource_anchor_name.setter
    def oci_resource_anchor_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociVcnId")
    def oci_vcn_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oci_vcn_id.setter
    def oci_vcn_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociVcnUrl")
    def oci_vcn_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oci_vcn_url.setter
    def oci_vcn_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeredCidrs")
    def peered_cidrs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @peered_cidrs.setter
    def peered_cidrs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @percent_progress.setter
    def percent_progress(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Access")
    def s3_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_access.setter
    def s3_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3PolicyDocument")
    def s3_policy_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_policy_document.setter
    def s3_policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status_reason.setter
    def status_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stsAccess")
    def sts_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sts_access.setter
    def sts_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stsPolicyDocument")
    def sts_policy_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sts_policy_document.setter
    def sts_policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[NetworkTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[NetworkTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zeroEtlAccess")
    def zero_etl_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zero_etl_access.setter
    def zero_etl_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:odb/network:Network")
class Network(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., backup_subnet_cidr: Optional[pulumi.Input[_builtins.str]] = ..., client_subnet_cidr: Optional[pulumi.Input[_builtins.str]] = ..., custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., default_dns_prefix: Optional[pulumi.Input[_builtins.str]] = ..., delete_associated_resources: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., kms_access: Optional[pulumi.Input[_builtins.str]] = ..., kms_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_access: Optional[pulumi.Input[_builtins.str]] = ..., s3_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., sts_access: Optional[pulumi.Input[_builtins.str]] = ..., sts_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[NetworkTimeoutsArgs, NetworkTimeoutsArgsDict]]] = ..., zero_etl_access: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NetworkArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., backup_subnet_cidr: Optional[pulumi.Input[_builtins.str]] = ..., client_subnet_cidr: Optional[pulumi.Input[_builtins.str]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., default_dns_prefix: Optional[pulumi.Input[_builtins.str]] = ..., delete_associated_resources: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., kms_access: Optional[pulumi.Input[_builtins.str]] = ..., kms_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., managed_services: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NetworkManagedServiceArgs, NetworkManagedServiceArgsDict]]]]] = ..., oci_dns_forwarding_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NetworkOciDnsForwardingConfigArgs, NetworkOciDnsForwardingConfigArgsDict]]]]] = ..., oci_network_anchor_id: Optional[pulumi.Input[_builtins.str]] = ..., oci_network_anchor_url: Optional[pulumi.Input[_builtins.str]] = ..., oci_resource_anchor_name: Optional[pulumi.Input[_builtins.str]] = ..., oci_vcn_id: Optional[pulumi.Input[_builtins.str]] = ..., oci_vcn_url: Optional[pulumi.Input[_builtins.str]] = ..., peered_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., percent_progress: Optional[pulumi.Input[_builtins.float]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_access: Optional[pulumi.Input[_builtins.str]] = ..., s3_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., status_reason: Optional[pulumi.Input[_builtins.str]] = ..., sts_access: Optional[pulumi.Input[_builtins.str]] = ..., sts_policy_document: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[NetworkTimeoutsArgs, NetworkTimeoutsArgsDict]]] = ..., zero_etl_access: Optional[pulumi.Input[_builtins.str]] = ...) -> Network:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupSubnetCidr")
    def backup_subnet_cidr(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSubnetCidr")
    def client_subnet_cidr(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDnsPrefix")
    def default_dns_prefix(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAssociatedResources")
    def delete_associated_resources(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsAccess")
    def kms_access(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsPolicyDocument")
    def kms_policy_document(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedServices")
    def managed_services(self) -> pulumi.Output[Sequence[outputs.NetworkManagedService]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociDnsForwardingConfigs")
    def oci_dns_forwarding_configs(self) -> pulumi.Output[Sequence[outputs.NetworkOciDnsForwardingConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociNetworkAnchorId")
    def oci_network_anchor_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociNetworkAnchorUrl")
    def oci_network_anchor_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociVcnId")
    def oci_vcn_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociVcnUrl")
    def oci_vcn_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeredCidrs")
    def peered_cidrs(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Access")
    def s3_access(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3PolicyDocument")
    def s3_policy_document(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stsAccess")
    def sts_access(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stsPolicyDocument")
    def sts_policy_document(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.NetworkTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zeroEtlAccess")
    def zero_etl_access(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


