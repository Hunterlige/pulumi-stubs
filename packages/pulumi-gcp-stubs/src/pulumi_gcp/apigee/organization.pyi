

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['OrganizationArgs', 'Organization']
@pulumi.input_type
class OrganizationArgs:
    def __init__(__self__, *, project_id: pulumi.Input[_builtins.str], analytics_region: Optional[pulumi.Input[_builtins.str]] = ..., api_consumer_data_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., api_consumer_data_location: Optional[pulumi.Input[_builtins.str]] = ..., authorized_network: Optional[pulumi.Input[_builtins.str]] = ..., billing_type: Optional[pulumi.Input[_builtins.str]] = ..., control_plane_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_vpc_peering: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[OrganizationPropertiesArgs]] = ..., retention: Optional[pulumi.Input[_builtins.str]] = ..., runtime_database_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., runtime_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticsRegion")
    def analytics_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @analytics_region.setter
    def analytics_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConsumerDataEncryptionKeyName")
    def api_consumer_data_encryption_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_consumer_data_encryption_key_name.setter
    def api_consumer_data_encryption_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConsumerDataLocation")
    def api_consumer_data_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_consumer_data_location.setter
    def api_consumer_data_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedNetwork")
    def authorized_network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorized_network.setter
    def authorized_network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingType")
    def billing_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @billing_type.setter
    def billing_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneEncryptionKeyName")
    def control_plane_encryption_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @control_plane_encryption_key_name.setter
    def control_plane_encryption_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableVpcPeering")
    def disable_vpc_peering(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_vpc_peering.setter
    def disable_vpc_peering(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def properties(self) -> Optional[pulumi.Input[OrganizationPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[OrganizationPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def retention(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @retention.setter
    def retention(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeDatabaseEncryptionKeyName")
    def runtime_database_encryption_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_database_encryption_key_name.setter
    def runtime_database_encryption_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeType")
    def runtime_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_type.setter
    def runtime_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _OrganizationState:
    def __init__(__self__, *, analytics_region: Optional[pulumi.Input[_builtins.str]] = ..., api_consumer_data_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., api_consumer_data_location: Optional[pulumi.Input[_builtins.str]] = ..., apigee_project_id: Optional[pulumi.Input[_builtins.str]] = ..., authorized_network: Optional[pulumi.Input[_builtins.str]] = ..., billing_type: Optional[pulumi.Input[_builtins.str]] = ..., ca_certificate: Optional[pulumi.Input[_builtins.str]] = ..., control_plane_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_vpc_peering: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project_id: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[OrganizationPropertiesArgs]] = ..., retention: Optional[pulumi.Input[_builtins.str]] = ..., runtime_database_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., runtime_type: Optional[pulumi.Input[_builtins.str]] = ..., subscription_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticsRegion")
    def analytics_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @analytics_region.setter
    def analytics_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConsumerDataEncryptionKeyName")
    def api_consumer_data_encryption_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_consumer_data_encryption_key_name.setter
    def api_consumer_data_encryption_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConsumerDataLocation")
    def api_consumer_data_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_consumer_data_location.setter
    def api_consumer_data_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apigeeProjectId")
    def apigee_project_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @apigee_project_id.setter
    def apigee_project_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedNetwork")
    def authorized_network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorized_network.setter
    def authorized_network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingType")
    def billing_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @billing_type.setter
    def billing_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ca_certificate.setter
    def ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneEncryptionKeyName")
    def control_plane_encryption_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @control_plane_encryption_key_name.setter
    def control_plane_encryption_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableVpcPeering")
    def disable_vpc_peering(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_vpc_peering.setter
    def disable_vpc_peering(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[OrganizationPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[OrganizationPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def retention(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @retention.setter
    def retention(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeDatabaseEncryptionKeyName")
    def runtime_database_encryption_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_database_encryption_key_name.setter
    def runtime_database_encryption_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeType")
    def runtime_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_type.setter
    def runtime_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionType")
    def subscription_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscription_type.setter
    def subscription_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:apigee/organization:Organization")
class Organization(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., analytics_region: Optional[pulumi.Input[_builtins.str]] = ..., api_consumer_data_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., api_consumer_data_location: Optional[pulumi.Input[_builtins.str]] = ..., authorized_network: Optional[pulumi.Input[_builtins.str]] = ..., billing_type: Optional[pulumi.Input[_builtins.str]] = ..., control_plane_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_vpc_peering: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., project_id: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[OrganizationPropertiesArgs, OrganizationPropertiesArgsDict]]] = ..., retention: Optional[pulumi.Input[_builtins.str]] = ..., runtime_database_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., runtime_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: OrganizationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., analytics_region: Optional[pulumi.Input[_builtins.str]] = ..., api_consumer_data_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., api_consumer_data_location: Optional[pulumi.Input[_builtins.str]] = ..., apigee_project_id: Optional[pulumi.Input[_builtins.str]] = ..., authorized_network: Optional[pulumi.Input[_builtins.str]] = ..., billing_type: Optional[pulumi.Input[_builtins.str]] = ..., ca_certificate: Optional[pulumi.Input[_builtins.str]] = ..., control_plane_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_vpc_peering: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project_id: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[OrganizationPropertiesArgs, OrganizationPropertiesArgsDict]]] = ..., retention: Optional[pulumi.Input[_builtins.str]] = ..., runtime_database_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., runtime_type: Optional[pulumi.Input[_builtins.str]] = ..., subscription_type: Optional[pulumi.Input[_builtins.str]] = ...) -> Organization:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyticsRegion")
    def analytics_region(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConsumerDataEncryptionKeyName")
    def api_consumer_data_encryption_key_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConsumerDataLocation")
    def api_consumer_data_location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apigeeProjectId")
    def apigee_project_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedNetwork")
    def authorized_network(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingType")
    def billing_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneEncryptionKeyName")
    def control_plane_encryption_key_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableVpcPeering")
    def disable_vpc_peering(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.OrganizationProperties]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def retention(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeDatabaseEncryptionKeyName")
    def runtime_database_encryption_key_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeType")
    def runtime_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionType")
    def subscription_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


