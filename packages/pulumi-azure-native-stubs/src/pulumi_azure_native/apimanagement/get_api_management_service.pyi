

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetApiManagementServiceResult', 'AwaitableGetApiManagementServiceResult', 'get_api_management_service', 'get_api_management_service_output']
@pulumi.output_type
class GetApiManagementServiceResult:
    
    def __init__(__self__, additional_locations=..., api_version_constraint=..., azure_api_version=..., certificates=..., configuration_api=..., created_at_utc=..., custom_properties=..., developer_portal_status=..., developer_portal_url=..., disable_gateway=..., enable_client_certificate=..., etag=..., gateway_regional_url=..., gateway_url=..., hostname_configurations=..., id=..., identity=..., legacy_portal_status=..., location=..., management_api_url=..., name=..., nat_gateway_state=..., notification_sender_email=..., outbound_public_ip_addresses=..., platform_version=..., portal_url=..., private_endpoint_connections=..., private_ip_addresses=..., provisioning_state=..., public_ip_addresses=..., public_ip_address_id=..., public_network_access=..., publisher_email=..., publisher_name=..., restore=..., scm_url=..., sku=..., system_data=..., tags=..., target_provisioning_state=..., type=..., virtual_network_configuration=..., virtual_network_type=..., zones=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalLocations")
    def additional_locations(self) -> Optional[Sequence[outputs.AdditionalLocationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiVersionConstraint")
    def api_version_constraint(self) -> Optional[outputs.ApiVersionConstraintResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Optional[Sequence[outputs.CertificateConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationApi")
    def configuration_api(self) -> Optional[outputs.ConfigurationApiResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAtUtc")
    def created_at_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerPortalStatus")
    def developer_portal_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerPortalUrl")
    def developer_portal_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableGateway")
    def disable_gateway(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableClientCertificate")
    def enable_client_certificate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayRegionalUrl")
    def gateway_regional_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayUrl")
    def gateway_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostnameConfigurations")
    def hostname_configurations(self) -> Optional[Sequence[outputs.HostnameConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ApiManagementServiceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="legacyPortalStatus")
    def legacy_portal_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementApiUrl")
    def management_api_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayState")
    def nat_gateway_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationSenderEmail")
    def notification_sender_email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundPublicIPAddresses")
    def outbound_public_ip_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalUrl")
    def portal_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[Sequence[outputs.RemotePrivateEndpointConnectionWrapperResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIPAddresses")
    def private_ip_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPAddresses")
    def public_ip_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpAddressId")
    def public_ip_address_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherEmail")
    def publisher_email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherName")
    def publisher_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def restore(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scmUrl")
    def scm_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.ApiManagementServiceSkuPropertiesResponse:
        
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
    @pulumi.getter(name="targetProvisioningState")
    def target_provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkConfiguration")
    def virtual_network_configuration(self) -> Optional[outputs.VirtualNetworkConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkType")
    def virtual_network_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableGetApiManagementServiceResult(GetApiManagementServiceResult):
    def __await__(self): # -> Generator[Never, Any, GetApiManagementServiceResult]:
        ...
    


def get_api_management_service(resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetApiManagementServiceResult:
    
    ...

def get_api_management_service_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetApiManagementServiceResult]:
    
    ...

