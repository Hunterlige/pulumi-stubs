

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterArgs', 'Cluster']
@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]], aad_application_object_id: Optional[pulumi.Input[_builtins.str]] = ..., aad_client_id: Optional[pulumi.Input[_builtins.str]] = ..., aad_service_principal_object_id: Optional[pulumi.Input[_builtins.str]] = ..., aad_tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., cloud_management_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., desired_properties: Optional[pulumi.Input[ClusterDesiredPropertiesArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., software_assurance_properties: Optional[pulumi.Input[SoftwareAssurancePropertiesArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadApplicationObjectId")
    def aad_application_object_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aad_application_object_id.setter
    def aad_application_object_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadClientId")
    def aad_client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aad_client_id.setter
    def aad_client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadServicePrincipalObjectId")
    def aad_service_principal_object_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aad_service_principal_object_id.setter
    def aad_service_principal_object_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadTenantId")
    def aad_tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aad_tenant_id.setter
    def aad_tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudManagementEndpoint")
    def cloud_management_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloud_management_endpoint.setter
    def cloud_management_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredProperties")
    def desired_properties(self) -> Optional[pulumi.Input[ClusterDesiredPropertiesArgs]]:
        
        ...
    
    @desired_properties.setter
    def desired_properties(self, value: Optional[pulumi.Input[ClusterDesiredPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="softwareAssuranceProperties")
    def software_assurance_properties(self) -> Optional[pulumi.Input[SoftwareAssurancePropertiesArgs]]:
        
        ...
    
    @software_assurance_properties.setter
    def software_assurance_properties(self, value: Optional[pulumi.Input[SoftwareAssurancePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:azurestackhci:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aad_application_object_id: Optional[pulumi.Input[_builtins.str]] = ..., aad_client_id: Optional[pulumi.Input[_builtins.str]] = ..., aad_service_principal_object_id: Optional[pulumi.Input[_builtins.str]] = ..., aad_tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., cloud_management_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., desired_properties: Optional[pulumi.Input[Union[ClusterDesiredPropertiesArgs, ClusterDesiredPropertiesArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., software_assurance_properties: Optional[pulumi.Input[Union[SoftwareAssurancePropertiesArgs, SoftwareAssurancePropertiesArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]] = ..., user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Cluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadApplicationObjectId")
    def aad_application_object_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadClientId")
    def aad_client_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadServicePrincipalObjectId")
    def aad_service_principal_object_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadTenantId")
    def aad_tenant_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingModel")
    def billing_model(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudId")
    def cloud_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudManagementEndpoint")
    def cloud_management_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectivityStatus")
    def connectivity_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredProperties")
    def desired_properties(self) -> pulumi.Output[Optional[outputs.ClusterDesiredPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isolatedVmAttestationConfiguration")
    def isolated_vm_attestation_configuration(self) -> pulumi.Output[outputs.IsolatedVmAttestationConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBillingTimestamp")
    def last_billing_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSyncTimestamp")
    def last_sync_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logCollectionProperties")
    def log_collection_properties(self) -> pulumi.Output[Optional[outputs.LogCollectionPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationTimestamp")
    def registration_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteSupportProperties")
    def remote_support_properties(self) -> pulumi.Output[Optional[outputs.RemoteSupportPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportedProperties")
    def reported_properties(self) -> pulumi.Output[outputs.ClusterReportedPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceProviderObjectId")
    def resource_provider_object_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softwareAssuranceProperties")
    def software_assurance_properties(self) -> pulumi.Output[Optional[outputs.SoftwareAssurancePropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trialDaysRemaining")
    def trial_days_remaining(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> pulumi.Output[Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]]:
        
        ...
    


