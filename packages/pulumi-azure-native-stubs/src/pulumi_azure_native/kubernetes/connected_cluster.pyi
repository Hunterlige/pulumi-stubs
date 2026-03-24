

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectedClusterArgs', 'ConnectedCluster']
@pulumi.input_type
class ConnectedClusterArgs:
    def __init__(__self__, *, agent_public_key_certificate: pulumi.Input[_builtins.str], identity: pulumi.Input[ConnectedClusterIdentityArgs], resource_group_name: pulumi.Input[_builtins.str], aad_profile: Optional[pulumi.Input[AadProfileArgs]] = ..., arc_agent_profile: Optional[pulumi.Input[ArcAgentProfileArgs]] = ..., azure_hybrid_benefit: Optional[pulumi.Input[Union[_builtins.str, AzureHybridBenefit]]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., distribution: Optional[pulumi.Input[_builtins.str]] = ..., distribution_version: Optional[pulumi.Input[_builtins.str]] = ..., infrastructure: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[Union[_builtins.str, ConnectedClusterKind]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., private_link_scope_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., private_link_state: Optional[pulumi.Input[Union[_builtins.str, PrivateLinkState]]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentPublicKeyCertificate")
    def agent_public_key_certificate(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @agent_public_key_certificate.setter
    def agent_public_key_certificate(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Input[ConnectedClusterIdentityArgs]:
        
        ...
    
    @identity.setter
    def identity(self, value: pulumi.Input[ConnectedClusterIdentityArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadProfile")
    def aad_profile(self) -> Optional[pulumi.Input[AadProfileArgs]]:
        
        ...
    
    @aad_profile.setter
    def aad_profile(self, value: Optional[pulumi.Input[AadProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="arcAgentProfile")
    def arc_agent_profile(self) -> Optional[pulumi.Input[ArcAgentProfileArgs]]:
        
        ...
    
    @arc_agent_profile.setter
    def arc_agent_profile(self, value: Optional[pulumi.Input[ArcAgentProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureHybridBenefit")
    def azure_hybrid_benefit(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureHybridBenefit]]]:
        
        ...
    
    @azure_hybrid_benefit.setter
    def azure_hybrid_benefit(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureHybridBenefit]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @distribution.setter
    def distribution(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionVersion")
    def distribution_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @distribution_version.setter
    def distribution_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def infrastructure(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @infrastructure.setter
    def infrastructure(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, ConnectedClusterKind]]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectedClusterKind]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkScopeResourceId")
    def private_link_scope_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_link_scope_resource_id.setter
    def private_link_scope_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkState")
    def private_link_state(self) -> Optional[pulumi.Input[Union[_builtins.str, PrivateLinkState]]]:
        
        ...
    
    @private_link_state.setter
    def private_link_state(self, value: Optional[pulumi.Input[Union[_builtins.str, PrivateLinkState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:kubernetes:ConnectedCluster")
class ConnectedCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aad_profile: Optional[pulumi.Input[Union[AadProfileArgs, AadProfileArgsDict]]] = ..., agent_public_key_certificate: Optional[pulumi.Input[_builtins.str]] = ..., arc_agent_profile: Optional[pulumi.Input[Union[ArcAgentProfileArgs, ArcAgentProfileArgsDict]]] = ..., azure_hybrid_benefit: Optional[pulumi.Input[Union[_builtins.str, AzureHybridBenefit]]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., distribution: Optional[pulumi.Input[_builtins.str]] = ..., distribution_version: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[Union[ConnectedClusterIdentityArgs, ConnectedClusterIdentityArgsDict]]] = ..., infrastructure: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[Union[_builtins.str, ConnectedClusterKind]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., private_link_scope_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., private_link_state: Optional[pulumi.Input[Union[_builtins.str, PrivateLinkState]]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConnectedClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ConnectedCluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadProfile")
    def aad_profile(self) -> pulumi.Output[Optional[outputs.AadProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentPublicKeyCertificate")
    def agent_public_key_certificate(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arcAgentProfile")
    def arc_agent_profile(self) -> pulumi.Output[Optional[outputs.ArcAgentProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureHybridBenefit")
    def azure_hybrid_benefit(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectivityStatus")
    def connectivity_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def distribution(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionVersion")
    def distribution_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[outputs.ConnectedClusterIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def infrastructure(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastConnectivityTime")
    def last_connectivity_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentityCertificateExpirationTime")
    def managed_identity_certificate_expiration_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="miscellaneousProperties")
    def miscellaneous_properties(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def offering(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkScopeResourceId")
    def private_link_scope_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkState")
    def private_link_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="totalCoreCount")
    def total_core_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalNodeCount")
    def total_node_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


