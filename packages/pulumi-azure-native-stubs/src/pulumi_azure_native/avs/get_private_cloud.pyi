

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPrivateCloudResult', 'AwaitableGetPrivateCloudResult', 'get_private_cloud', 'get_private_cloud_output']
@pulumi.output_type
class GetPrivateCloudResult:
    
    def __init__(__self__, availability=..., azure_api_version=..., circuit=..., dns_zone_type=..., encryption=..., endpoints=..., extended_network_blocks=..., external_cloud_links=..., id=..., identity=..., identity_sources=..., internet=..., location=..., management_cluster=..., management_network=..., name=..., network_block=..., nsx_public_ip_quota_raised=..., nsxt_certificate_thumbprint=..., nsxt_password=..., provisioning_network=..., provisioning_state=..., secondary_circuit=..., sku=..., system_data=..., tags=..., type=..., vcenter_certificate_thumbprint=..., vcenter_password=..., virtual_network_id=..., vmotion_network=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def availability(self) -> Optional[outputs.AvailabilityPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def circuit(self) -> Optional[outputs.CircuitResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsZoneType")
    def dns_zone_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.EncryptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> outputs.EndpointsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedNetworkBlocks")
    def extended_network_blocks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalCloudLinks")
    def external_cloud_links(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.SystemAssignedServiceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identitySources")
    def identity_sources(self) -> Optional[Sequence[outputs.IdentitySourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def internet(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementCluster")
    def management_cluster(self) -> outputs.ManagementClusterResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementNetwork")
    def management_network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBlock")
    def network_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nsxPublicIpQuotaRaised")
    def nsx_public_ip_quota_raised(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nsxtCertificateThumbprint")
    def nsxt_certificate_thumbprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nsxtPassword")
    def nsxt_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningNetwork")
    def provisioning_network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryCircuit")
    def secondary_circuit(self) -> Optional[outputs.CircuitResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcenterCertificateThumbprint")
    def vcenter_certificate_thumbprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcenterPassword")
    def vcenter_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmotionNetwork")
    def vmotion_network(self) -> _builtins.str:
        
        ...
    


class AwaitableGetPrivateCloudResult(GetPrivateCloudResult):
    def __await__(self): # -> Generator[Never, Any, GetPrivateCloudResult]:
        ...
    


def get_private_cloud(private_cloud_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPrivateCloudResult:
    
    ...

def get_private_cloud_output(private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPrivateCloudResult]:
    
    ...

