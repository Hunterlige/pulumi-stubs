

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
__all__ = ['AdvSecurityObjectModelResponse', 'AppSeenDataResponse', 'AppSeenInfoResponse', 'ApplicationInsightsResponse', ..., 'AzureResourceManagerUserAssignedIdentityResponse', 'CategoryResponse', 'CountryResponse', 'DNSSettingsResponse', 'DestinationAddrResponse', 'EndpointConfigurationResponse', 'EventHubResponse', 'FrontendSettingResponse', 'IPAddressResponse', 'IPAddressSpaceResponse', 'LogDestinationResponse', 'MarketplaceDetailsResponse', 'MonitorLogResponse', 'NameDescriptionObjectResponse', 'NetworkProfileResponse', 'PanoramaConfigResponse', 'PlanDataResponse', 'PredefinedUrlCategoryResponse', 'RulestackDetailsResponse', 'SecurityServicesResponse', 'SecurityServicesTypeListResponse', 'SourceAddrResponse', 'StorageAccountResponse', 'StrataCloudManagerConfigResponse', 'SystemDataResponse', 'TagInfoResponse', 'VnetConfigurationResponse', 'VwanConfigurationResponse']
@pulumi.output_type
class AdvSecurityObjectModelResponse(dict):
    
    def __init__(__self__, *, entry: Sequence[outputs.NameDescriptionObjectResponse], type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def entry(self) -> Sequence[outputs.NameDescriptionObjectResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppSeenDataResponse(dict):
    
    def __init__(__self__, *, app_seen_list: Sequence[outputs.AppSeenInfoResponse], count: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appSeenList")
    def app_seen_list(self) -> Sequence[outputs.AppSeenInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class AppSeenInfoResponse(dict):
    
    def __init__(__self__, *, category: _builtins.str, risk: _builtins.str, standard_ports: _builtins.str, sub_category: _builtins.str, tag: _builtins.str, technology: _builtins.str, title: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def risk(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standardPorts")
    def standard_ports(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subCategory")
    def sub_category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def technology(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ApplicationInsightsResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureResourceManagerManagedIdentityPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: _builtins.str, user_assigned_identities: Optional[Mapping[str, outputs.AzureResourceManagerUserAssignedIdentityResponse]] = ...) -> None:
        
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
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.AzureResourceManagerUserAssignedIdentityResponse]]:
        
        ...
    


@pulumi.output_type
class AzureResourceManagerUserAssignedIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., principal_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CategoryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, feeds: Sequence[_builtins.str], url_custom: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def feeds(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlCustom")
    def url_custom(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CountryResponse(dict):
    
    def __init__(__self__, *, code: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DNSSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dns_servers: Optional[Sequence[outputs.IPAddressResponse]] = ..., enable_dns_proxy: Optional[_builtins.str] = ..., enabled_dns_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[Sequence[outputs.IPAddressResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDnsProxy")
    def enable_dns_proxy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledDnsType")
    def enabled_dns_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DestinationAddrResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cidrs: Optional[Sequence[_builtins.str]] = ..., countries: Optional[Sequence[_builtins.str]] = ..., feeds: Optional[Sequence[_builtins.str]] = ..., fqdn_lists: Optional[Sequence[_builtins.str]] = ..., prefix_lists: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidrs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def countries(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def feeds(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fqdnLists")
    def fqdn_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixLists")
    def prefix_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class EndpointConfigurationResponse(dict):
    
    def __init__(__self__, *, address: outputs.IPAddressResponse, port: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> outputs.IPAddressResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EventHubResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., name_space: Optional[_builtins.str] = ..., policy_name: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameSpace")
    def name_space(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FrontendSettingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backend_configuration: outputs.EndpointConfigurationResponse, frontend_configuration: outputs.EndpointConfigurationResponse, name: _builtins.str, protocol: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendConfiguration")
    def backend_configuration(self) -> outputs.EndpointConfigurationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontendConfiguration")
    def frontend_configuration(self) -> outputs.EndpointConfigurationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class IPAddressResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IPAddressSpaceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address_space: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressSpace")
    def address_space(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LogDestinationResponse(dict):
    
    def __init__(__self__, *, event_hub_configurations: Optional[outputs.EventHubResponse] = ..., monitor_configurations: Optional[outputs.MonitorLogResponse] = ..., storage_configurations: Optional[outputs.StorageAccountResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubConfigurations")
    def event_hub_configurations(self) -> Optional[outputs.EventHubResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitorConfigurations")
    def monitor_configurations(self) -> Optional[outputs.MonitorLogResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConfigurations")
    def storage_configurations(self) -> Optional[outputs.StorageAccountResponse]:
        
        ...
    


@pulumi.output_type
class MarketplaceDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, marketplace_subscription_id: _builtins.str, offer_id: _builtins.str, publisher_id: _builtins.str, marketplace_subscription_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketplaceSubscriptionId")
    def marketplace_subscription_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offerId")
    def offer_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketplaceSubscriptionStatus")
    def marketplace_subscription_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MonitorLogResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., primary_key: Optional[_builtins.str] = ..., secondary_key: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ..., workspace: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def workspace(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NameDescriptionObjectResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_egress_nat: _builtins.str, network_type: _builtins.str, public_ips: Sequence[outputs.IPAddressResponse], egress_nat_ip: Optional[Sequence[outputs.IPAddressResponse]] = ..., private_source_nat_rules_destination: Optional[Sequence[_builtins.str]] = ..., trusted_ranges: Optional[Sequence[_builtins.str]] = ..., vnet_configuration: Optional[outputs.VnetConfigurationResponse] = ..., vwan_configuration: Optional[outputs.VwanConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEgressNat")
    def enable_egress_nat(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIps")
    def public_ips(self) -> Sequence[outputs.IPAddressResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressNatIp")
    def egress_nat_ip(self) -> Optional[Sequence[outputs.IPAddressResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateSourceNatRulesDestination")
    def private_source_nat_rules_destination(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedRanges")
    def trusted_ranges(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vnetConfiguration")
    def vnet_configuration(self) -> Optional[outputs.VnetConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vwanConfiguration")
    def vwan_configuration(self) -> Optional[outputs.VwanConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class PanoramaConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cg_name: _builtins.str, config_string: _builtins.str, dg_name: _builtins.str, host_name: _builtins.str, panorama_server: _builtins.str, panorama_server2: _builtins.str, tpl_name: _builtins.str, vm_auth_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cgName")
    def cg_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configString")
    def config_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dgName")
    def dg_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="panoramaServer")
    def panorama_server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="panoramaServer2")
    def panorama_server2(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tplName")
    def tpl_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmAuthKey")
    def vm_auth_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PlanDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, billing_cycle: _builtins.str, effective_date: _builtins.str, plan_id: _builtins.str, usage_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingCycle")
    def billing_cycle(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveDate")
    def effective_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usageType")
    def usage_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PredefinedUrlCategoryResponse(dict):
    
    def __init__(__self__, *, action: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class RulestackDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, location: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ..., rulestack_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rulestackId")
    def rulestack_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityServicesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, anti_spyware_profile: Optional[_builtins.str] = ..., anti_virus_profile: Optional[_builtins.str] = ..., dns_subscription: Optional[_builtins.str] = ..., file_blocking_profile: Optional[_builtins.str] = ..., outbound_trust_certificate: Optional[_builtins.str] = ..., outbound_un_trust_certificate: Optional[_builtins.str] = ..., url_filtering_profile: Optional[_builtins.str] = ..., vulnerability_profile: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="antiSpywareProfile")
    def anti_spyware_profile(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="antiVirusProfile")
    def anti_virus_profile(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSubscription")
    def dns_subscription(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileBlockingProfile")
    def file_blocking_profile(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundTrustCertificate")
    def outbound_trust_certificate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundUnTrustCertificate")
    def outbound_un_trust_certificate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlFilteringProfile")
    def url_filtering_profile(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vulnerabilityProfile")
    def vulnerability_profile(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityServicesTypeListResponse(dict):
    
    def __init__(__self__, *, entry: Sequence[outputs.NameDescriptionObjectResponse], type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def entry(self) -> Sequence[outputs.NameDescriptionObjectResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SourceAddrResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cidrs: Optional[Sequence[_builtins.str]] = ..., countries: Optional[Sequence[_builtins.str]] = ..., feeds: Optional[Sequence[_builtins.str]] = ..., prefix_lists: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidrs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def countries(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def feeds(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixLists")
    def prefix_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class StorageAccountResponse(dict):
    
    def __init__(__self__, *, account_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StrataCloudManagerConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_manager_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudManagerName")
    def cloud_manager_name(self) -> _builtins.str:
        
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
class TagInfoResponse(dict):
    
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VnetConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, trust_subnet: outputs.IPAddressSpaceResponse, un_trust_subnet: outputs.IPAddressSpaceResponse, vnet: outputs.IPAddressSpaceResponse, ip_of_trust_subnet_for_udr: Optional[outputs.IPAddressResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustSubnet")
    def trust_subnet(self) -> outputs.IPAddressSpaceResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unTrustSubnet")
    def un_trust_subnet(self) -> outputs.IPAddressSpaceResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vnet(self) -> outputs.IPAddressSpaceResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipOfTrustSubnetForUdr")
    def ip_of_trust_subnet_for_udr(self) -> Optional[outputs.IPAddressResponse]:
        
        ...
    


@pulumi.output_type
class VwanConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, v_hub: outputs.IPAddressSpaceResponse, ip_of_trust_subnet_for_udr: Optional[outputs.IPAddressResponse] = ..., network_virtual_appliance_id: Optional[_builtins.str] = ..., trust_subnet: Optional[outputs.IPAddressSpaceResponse] = ..., un_trust_subnet: Optional[outputs.IPAddressSpaceResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vHub")
    def v_hub(self) -> outputs.IPAddressSpaceResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipOfTrustSubnetForUdr")
    def ip_of_trust_subnet_for_udr(self) -> Optional[outputs.IPAddressResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkVirtualApplianceId")
    def network_virtual_appliance_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustSubnet")
    def trust_subnet(self) -> Optional[outputs.IPAddressSpaceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unTrustSubnet")
    def un_trust_subnet(self) -> Optional[outputs.IPAddressSpaceResponse]:
        
        ...
    


