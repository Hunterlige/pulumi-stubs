

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
__all__ = ['NetworkVirtualApplianceArgs', 'NetworkVirtualAppliance']
@pulumi.input_type
class NetworkVirtualApplianceArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], additional_nics: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualApplianceAdditionalNicPropertiesArgs]]]] = ..., boot_strap_configuration_blobs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cloud_init_configuration: Optional[pulumi.Input[_builtins.str]] = ..., cloud_init_configuration_blobs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., delegation: Optional[pulumi.Input[DelegationPropertiesArgs]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ..., internet_ingress_public_ips: Optional[pulumi.Input[Sequence[pulumi.Input[InternetIngressPublicIpsPropertiesArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_profile: Optional[pulumi.Input[NetworkVirtualAppliancePropertiesFormatNetworkProfileArgs]] = ..., network_virtual_appliance_name: Optional[pulumi.Input[_builtins.str]] = ..., nva_sku: Optional[pulumi.Input[VirtualApplianceSkuPropertiesArgs]] = ..., ssh_public_key: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_appliance_asn: Optional[pulumi.Input[_builtins.float]] = ..., virtual_hub: Optional[pulumi.Input[SubResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalNics")
    def additional_nics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualApplianceAdditionalNicPropertiesArgs]]]]:
        
        ...
    
    @additional_nics.setter
    def additional_nics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualApplianceAdditionalNicPropertiesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootStrapConfigurationBlobs")
    def boot_strap_configuration_blobs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @boot_strap_configuration_blobs.setter
    def boot_strap_configuration_blobs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudInitConfiguration")
    def cloud_init_configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloud_init_configuration.setter
    def cloud_init_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudInitConfigurationBlobs")
    def cloud_init_configuration_blobs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @cloud_init_configuration_blobs.setter
    def cloud_init_configuration_blobs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delegation(self) -> Optional[pulumi.Input[DelegationPropertiesArgs]]:
        
        ...
    
    @delegation.setter
    def delegation(self, value: Optional[pulumi.Input[DelegationPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetIngressPublicIps")
    def internet_ingress_public_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InternetIngressPublicIpsPropertiesArgs]]]]:
        
        ...
    
    @internet_ingress_public_ips.setter
    def internet_ingress_public_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InternetIngressPublicIpsPropertiesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input[NetworkVirtualAppliancePropertiesFormatNetworkProfileArgs]]:
        
        ...
    
    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input[NetworkVirtualAppliancePropertiesFormatNetworkProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkVirtualApplianceName")
    def network_virtual_appliance_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_virtual_appliance_name.setter
    def network_virtual_appliance_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nvaSku")
    def nva_sku(self) -> Optional[pulumi.Input[VirtualApplianceSkuPropertiesArgs]]:
        
        ...
    
    @nva_sku.setter
    def nva_sku(self, value: Optional[pulumi.Input[VirtualApplianceSkuPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssh_public_key.setter
    def ssh_public_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualApplianceAsn")
    def virtual_appliance_asn(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @virtual_appliance_asn.setter
    def virtual_appliance_asn(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @virtual_hub.setter
    def virtual_hub(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:NetworkVirtualAppliance")
class NetworkVirtualAppliance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., additional_nics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VirtualApplianceAdditionalNicPropertiesArgs, VirtualApplianceAdditionalNicPropertiesArgsDict]]]]] = ..., boot_strap_configuration_blobs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cloud_init_configuration: Optional[pulumi.Input[_builtins.str]] = ..., cloud_init_configuration_blobs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., delegation: Optional[pulumi.Input[Union[DelegationPropertiesArgs, DelegationPropertiesArgsDict]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]]] = ..., internet_ingress_public_ips: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InternetIngressPublicIpsPropertiesArgs, InternetIngressPublicIpsPropertiesArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_profile: Optional[pulumi.Input[Union[NetworkVirtualAppliancePropertiesFormatNetworkProfileArgs, NetworkVirtualAppliancePropertiesFormatNetworkProfileArgsDict]]] = ..., network_virtual_appliance_name: Optional[pulumi.Input[_builtins.str]] = ..., nva_sku: Optional[pulumi.Input[Union[VirtualApplianceSkuPropertiesArgs, VirtualApplianceSkuPropertiesArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., ssh_public_key: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_appliance_asn: Optional[pulumi.Input[_builtins.float]] = ..., virtual_hub: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NetworkVirtualApplianceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> NetworkVirtualAppliance:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalNics")
    def additional_nics(self) -> pulumi.Output[Optional[Sequence[outputs.VirtualApplianceAdditionalNicPropertiesResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootStrapConfigurationBlobs")
    def boot_strap_configuration_blobs(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudInitConfiguration")
    def cloud_init_configuration(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudInitConfigurationBlobs")
    def cloud_init_configuration_blobs(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delegation(self) -> pulumi.Output[Optional[outputs.DelegationPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundSecurityRules")
    def inbound_security_rules(self) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetIngressPublicIps")
    def internet_ingress_public_ips(self) -> pulumi.Output[Optional[Sequence[outputs.InternetIngressPublicIpsPropertiesResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[Optional[outputs.NetworkVirtualAppliancePropertiesFormatResponseNetworkProfile]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nvaSku")
    def nva_sku(self) -> pulumi.Output[Optional[outputs.VirtualApplianceSkuPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerManagedResource")
    def partner_managed_resource(self) -> pulumi.Output[Optional[outputs.PartnerManagedResourcePropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualApplianceAsn")
    def virtual_appliance_asn(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualApplianceConnections")
    def virtual_appliance_connections(self) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualApplianceNics")
    def virtual_appliance_nics(self) -> pulumi.Output[Sequence[outputs.VirtualApplianceNicPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualApplianceSites")
    def virtual_appliance_sites(self) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    


