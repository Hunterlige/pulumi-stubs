

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AgentConfigurationResponse', 'AgentUpgradeResponse', 'CloudMetadataResponse', 'ConfigurationExtensionResponse', 'ErrorAdditionalInfoResponse', 'ErrorDetailResponse', 'EsuKeyResponse', 'ExtensionsResourceStatusResponse', 'HybridComputePrivateLinkScopePropertiesResponse', 'IdentityResponse', 'IpAddressResponse', 'LicenseDetailsResponse', ..., 'LicenseProfileMachineInstanceViewResponse', 'LicenseResponse', 'LocationDataResponse', 'MachineExtensionInstanceViewResponse', 'MachineExtensionInstanceViewResponseStatus', 'MachineExtensionPropertiesResponse', 'MachineExtensionResponse', 'MachineRunCommandInstanceViewResponse', 'MachineRunCommandScriptSourceResponse', 'NetworkInterfaceResponse', 'NetworkProfileResponse', 'OSProfileResponse', 'OSProfileResponseLinuxConfiguration', 'OSProfileResponseWindowsConfiguration', 'PatchSettingsResponseStatus', 'PrivateEndpointConnectionDataModelResponse', 'PrivateEndpointConnectionPropertiesResponse', 'PrivateEndpointPropertyResponse', 'PrivateLinkServiceConnectionStatePropertyResponse', 'ProductFeatureResponse', 'RunCommandInputParameterResponse', 'RunCommandManagedIdentityResponse', 'ServiceStatusResponse', 'ServiceStatusesResponse', 'SubnetResponse', 'SystemDataResponse', 'VolumeLicenseDetailsResponse']
@pulumi.output_type
class AgentConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, config_mode: _builtins.str, extensions_allow_list: Sequence[outputs.ConfigurationExtensionResponse], extensions_block_list: Sequence[outputs.ConfigurationExtensionResponse], extensions_enabled: _builtins.str, guest_configuration_enabled: _builtins.str, incoming_connections_ports: Sequence[_builtins.str], proxy_bypass: Sequence[_builtins.str], proxy_url: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configMode")
    def config_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionsAllowList")
    def extensions_allow_list(self) -> Sequence[outputs.ConfigurationExtensionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionsBlockList")
    def extensions_block_list(self) -> Sequence[outputs.ConfigurationExtensionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionsEnabled")
    def extensions_enabled(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestConfigurationEnabled")
    def guest_configuration_enabled(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incomingConnectionsPorts")
    def incoming_connections_ports(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyBypass")
    def proxy_bypass(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyUrl")
    def proxy_url(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AgentUpgradeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_attempt_desired_version: _builtins.str, last_attempt_message: _builtins.str, last_attempt_status: _builtins.str, last_attempt_timestamp: _builtins.str, correlation_id: Optional[_builtins.str] = ..., desired_version: Optional[_builtins.str] = ..., enable_automatic_upgrade: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAttemptDesiredVersion")
    def last_attempt_desired_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAttemptMessage")
    def last_attempt_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAttemptStatus")
    def last_attempt_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAttemptTimestamp")
    def last_attempt_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredVersion")
    def desired_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class CloudMetadataResponse(dict):
    
    def __init__(__self__, *, provider: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def provider(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ConfigurationExtensionResponse(dict):
    
    def __init__(__self__, *, publisher: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ErrorAdditionalInfoResponse(dict):
    
    def __init__(__self__, *, info: Any, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def info(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ErrorDetailResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_info: Sequence[outputs.ErrorAdditionalInfoResponse], code: _builtins.str, details: Sequence[outputs.ErrorDetailResponse], message: _builtins.str, target: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence[outputs.ErrorAdditionalInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EsuKeyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, license_status: Optional[_builtins.int] = ..., sku: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseStatus")
    def license_status(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExtensionsResourceStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, code: Optional[_builtins.str] = ..., display_status: Optional[_builtins.str] = ..., level: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayStatus")
    def display_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HybridComputePrivateLinkScopePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, private_endpoint_connections: Sequence[outputs.PrivateEndpointConnectionDataModelResponse], private_link_scope_id: _builtins.str, provisioning_state: _builtins.str, public_network_access: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionDataModelResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkScopeId")
    def private_link_scope_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IpAddressResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnet: outputs.SubnetResponse, address: Optional[_builtins.str] = ..., ip_address_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> outputs.SubnetResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressVersion")
    def ip_address_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LicenseDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assigned_licenses: _builtins.int, immutable_id: _builtins.str, edition: Optional[_builtins.str] = ..., processors: Optional[_builtins.int] = ..., state: Optional[_builtins.str] = ..., target: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., volume_license_details: Optional[Sequence[outputs.VolumeLicenseDetailsResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedLicenses")
    def assigned_licenses(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immutableId")
    def immutable_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def processors(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeLicenseDetails")
    def volume_license_details(self) -> Optional[Sequence[outputs.VolumeLicenseDetailsResponse]]:
        
        ...
    


@pulumi.output_type
class LicenseProfileMachineInstanceViewEsuPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assigned_license_immutable_id: _builtins.str, esu_eligibility: _builtins.str, esu_key_state: _builtins.str, esu_keys: Sequence[outputs.EsuKeyResponse], server_type: _builtins.str, assigned_license: Optional[outputs.LicenseResponse] = ..., license_assignment_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedLicenseImmutableId")
    def assigned_license_immutable_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="esuEligibility")
    def esu_eligibility(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="esuKeyState")
    def esu_key_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="esuKeys")
    def esu_keys(self) -> Sequence[outputs.EsuKeyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverType")
    def server_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedLicense")
    def assigned_license(self) -> Optional[outputs.LicenseResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseAssignmentState")
    def license_assignment_state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LicenseProfileMachineInstanceViewResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, billing_end_date: _builtins.str, billing_start_date: _builtins.str, disenrollment_date: _builtins.str, enrollment_date: _builtins.str, error: outputs.ErrorDetailResponse, license_channel: _builtins.str, license_status: _builtins.str, esu_profile: Optional[outputs.LicenseProfileMachineInstanceViewEsuPropertiesResponse] = ..., product_features: Optional[Sequence[outputs.ProductFeatureResponse]] = ..., product_type: Optional[_builtins.str] = ..., software_assurance_customer: Optional[_builtins.bool] = ..., subscription_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingEndDate")
    def billing_end_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingStartDate")
    def billing_start_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disenrollmentDate")
    def disenrollment_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enrollmentDate")
    def enrollment_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ErrorDetailResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseChannel")
    def license_channel(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseStatus")
    def license_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="esuProfile")
    def esu_profile(self) -> Optional[outputs.LicenseProfileMachineInstanceViewEsuPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productFeatures")
    def product_features(self) -> Optional[Sequence[outputs.ProductFeatureResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productType")
    def product_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softwareAssuranceCustomer")
    def software_assurance_customer(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionStatus")
    def subscription_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LicenseResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, location: _builtins.str, name: _builtins.str, provisioning_state: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, license_details: Optional[outputs.LicenseDetailsResponse] = ..., license_type: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseDetails")
    def license_details(self) -> Optional[outputs.LicenseDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LocationDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, city: Optional[_builtins.str] = ..., country_or_region: Optional[_builtins.str] = ..., district: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryOrRegion")
    def country_or_region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def district(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MachineExtensionInstanceViewResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., status: Optional[outputs.MachineExtensionInstanceViewResponseStatus] = ..., type: Optional[_builtins.str] = ..., type_handler_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[outputs.MachineExtensionInstanceViewResponseStatus]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MachineExtensionInstanceViewResponseStatus(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, code: Optional[_builtins.str] = ..., display_status: Optional[_builtins.str] = ..., level: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayStatus")
    def display_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MachineExtensionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, auto_upgrade_minor_version: Optional[_builtins.bool] = ..., enable_automatic_upgrade: Optional[_builtins.bool] = ..., force_update_tag: Optional[_builtins.str] = ..., instance_view: Optional[outputs.MachineExtensionInstanceViewResponse] = ..., protected_settings: Optional[Any] = ..., publisher: Optional[_builtins.str] = ..., settings: Optional[Any] = ..., type: Optional[_builtins.str] = ..., type_handler_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> Optional[outputs.MachineExtensionInstanceViewResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MachineExtensionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, location: _builtins.str, name: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, properties: Optional[outputs.MachineExtensionPropertiesResponse] = ..., tags: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.MachineExtensionPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class MachineRunCommandInstanceViewResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_time: Optional[_builtins.str] = ..., error: Optional[_builtins.str] = ..., execution_message: Optional[_builtins.str] = ..., execution_state: Optional[_builtins.str] = ..., exit_code: Optional[_builtins.int] = ..., output: Optional[_builtins.str] = ..., start_time: Optional[_builtins.str] = ..., statuses: Optional[Sequence[outputs.ExtensionsResourceStatusResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionMessage")
    def execution_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionState")
    def execution_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exitCode")
    def exit_code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Optional[Sequence[outputs.ExtensionsResourceStatusResponse]]:
        
        ...
    


@pulumi.output_type
class MachineRunCommandScriptSourceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, command_id: Optional[_builtins.str] = ..., script: Optional[_builtins.str] = ..., script_uri: Optional[_builtins.str] = ..., script_uri_managed_identity: Optional[outputs.RunCommandManagedIdentityResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commandId")
    def command_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptUri")
    def script_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptUriManagedIdentity")
    def script_uri_managed_identity(self) -> Optional[outputs.RunCommandManagedIdentityResponse]:
        
        ...
    


@pulumi.output_type
class NetworkInterfaceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_addresses: Optional[Sequence[outputs.IpAddressResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[outputs.IpAddressResponse]]:
        
        ...
    


@pulumi.output_type
class NetworkProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_interfaces: Optional[Sequence[outputs.NetworkInterfaceResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[Sequence[outputs.NetworkInterfaceResponse]]:
        
        ...
    


@pulumi.output_type
class OSProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, computer_name: _builtins.str, linux_configuration: Optional[outputs.OSProfileResponseLinuxConfiguration] = ..., windows_configuration: Optional[outputs.OSProfileResponseWindowsConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxConfiguration")
    def linux_configuration(self) -> Optional[outputs.OSProfileResponseLinuxConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsConfiguration")
    def windows_configuration(self) -> Optional[outputs.OSProfileResponseWindowsConfiguration]:
        
        ...
    


@pulumi.output_type
class OSProfileResponseLinuxConfiguration(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, status: outputs.PatchSettingsResponseStatus, assessment_mode: Optional[_builtins.str] = ..., enable_hotpatching: Optional[_builtins.bool] = ..., patch_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.PatchSettingsResponseStatus:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHotpatching")
    def enable_hotpatching(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OSProfileResponseWindowsConfiguration(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, status: outputs.PatchSettingsResponseStatus, assessment_mode: Optional[_builtins.str] = ..., enable_hotpatching: Optional[_builtins.bool] = ..., patch_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.PatchSettingsResponseStatus:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHotpatching")
    def enable_hotpatching(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PatchSettingsResponseStatus(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error: outputs.ErrorDetailResponse, hotpatch_enablement_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ErrorDetailResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotpatchEnablementStatus")
    def hotpatch_enablement_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionDataModelResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, type: _builtins.str, properties: Optional[outputs.PrivateEndpointConnectionPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.PrivateEndpointConnectionPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_ids: Sequence[_builtins.str], provisioning_state: _builtins.str, private_endpoint: Optional[outputs.PrivateEndpointPropertyResponse] = ..., private_link_service_connection_state: Optional[outputs.PrivateLinkServiceConnectionStatePropertyResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointPropertyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[outputs.PrivateLinkServiceConnectionStatePropertyResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointPropertyResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateLinkServiceConnectionStatePropertyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions_required: _builtins.str, description: _builtins.str, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ProductFeatureResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, billing_end_date: _builtins.str, billing_start_date: _builtins.str, disenrollment_date: _builtins.str, enrollment_date: _builtins.str, error: outputs.ErrorDetailResponse, name: Optional[_builtins.str] = ..., subscription_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingEndDate")
    def billing_end_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingStartDate")
    def billing_start_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disenrollmentDate")
    def disenrollment_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enrollmentDate")
    def enrollment_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ErrorDetailResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionStatus")
    def subscription_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RunCommandInputParameterResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RunCommandManagedIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., object_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, startup_type: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startupType")
    def startup_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceStatusesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, extension_service: Optional[outputs.ServiceStatusResponse] = ..., guest_configuration_service: Optional[outputs.ServiceStatusResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionService")
    def extension_service(self) -> Optional[outputs.ServiceStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestConfigurationService")
    def guest_configuration_service(self) -> Optional[outputs.ServiceStatusResponse]:
        
        ...
    


@pulumi.output_type
class SubnetResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VolumeLicenseDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, invoice_id: Optional[_builtins.str] = ..., program_year: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invoiceId")
    def invoice_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="programYear")
    def program_year(self) -> Optional[_builtins.str]:
        
        ...
    


