

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkInterfaceResult', 'AwaitableGetNetworkInterfaceResult', 'get_network_interface', 'get_network_interface_output']
@pulumi.output_type
class GetNetworkInterfaceResult:
    
    def __init__(__self__, auxiliary_mode=..., auxiliary_sku=..., azure_api_version=..., default_outbound_connectivity_enabled=..., disable_tcp_state_tracking=..., dns_settings=..., dscp_configuration=..., enable_accelerated_networking=..., enable_ip_forwarding=..., etag=..., extended_location=..., hosted_workloads=..., id=..., ip_configurations=..., location=..., mac_address=..., migration_phase=..., name=..., network_security_group=..., nic_type=..., primary=..., private_endpoint=..., private_link_service=..., provisioning_state=..., resource_guid=..., tags=..., tap_configurations=..., type=..., virtual_machine=..., vnet_encryption_supported=..., workload_type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="auxiliaryMode")
    def auxiliary_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auxiliarySku")
    def auxiliary_sku(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultOutboundConnectivityEnabled")
    def default_outbound_connectivity_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableTcpStateTracking")
    def disable_tcp_state_tracking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[outputs.NetworkInterfaceDnsSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dscpConfiguration")
    def dscp_configuration(self) -> outputs.SubResourceResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIPForwarding")
    def enable_ip_forwarding(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedWorkloads")
    def hosted_workloads(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Optional[Sequence[outputs.NetworkInterfaceIPConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationPhase")
    def migration_phase(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> Optional[outputs.NetworkSecurityGroupResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nicType")
    def nic_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> outputs.PrivateEndpointResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkService")
    def private_link_service(self) -> Optional[outputs.PrivateLinkServiceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tapConfigurations")
    def tap_configurations(self) -> Sequence[outputs.NetworkInterfaceTapConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(self) -> outputs.SubResourceResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vnetEncryptionSupported")
    def vnet_encryption_supported(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetNetworkInterfaceResult(GetNetworkInterfaceResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkInterfaceResult]:
        ...
    


def get_network_interface(expand: Optional[_builtins.str] = ..., network_interface_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkInterfaceResult:
    
    ...

def get_network_interface_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., network_interface_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkInterfaceResult]:
    
    ...

