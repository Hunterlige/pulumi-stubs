import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AzureResourceManagerManagedIdentityPropertiesArgs",
    ...,
    "AzureResourceManagerUserAssignedIdentityArgs",
    "AzureResourceManagerUserAssignedIdentityArgsDict",
    "CategoryArgs",
    "CategoryArgsDict",
    "DNSSettingsArgs",
    "DNSSettingsArgsDict",
    "DestinationAddrArgs",
    "DestinationAddrArgsDict",
    "EndpointConfigurationArgs",
    "EndpointConfigurationArgsDict",
    "FrontendSettingArgs",
    "FrontendSettingArgsDict",
    "IPAddressSpaceArgs",
    "IPAddressSpaceArgsDict",
    "IPAddressArgs",
    "IPAddressArgsDict",
    "MarketplaceDetailsArgs",
    "MarketplaceDetailsArgsDict",
    "NetworkProfileArgs",
    "NetworkProfileArgsDict",
    "PanoramaConfigArgs",
    "PanoramaConfigArgsDict",
    "PlanDataArgs",
    "PlanDataArgsDict",
    "RulestackDetailsArgs",
    "RulestackDetailsArgsDict",
    "SecurityServicesArgs",
    "SecurityServicesArgsDict",
    "SourceAddrArgs",
    "SourceAddrArgsDict",
    "StrataCloudManagerConfigArgs",
    "StrataCloudManagerConfigArgsDict",
    "TagInfoArgs",
    "TagInfoArgsDict",
    "VnetConfigurationArgs",
    "VnetConfigurationArgsDict",
    "VwanConfigurationArgs",
    "VwanConfigurationArgsDict",
]

class AzureResourceManagerManagedIdentityPropertiesArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ManagedIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[
            Mapping[str, pulumi.Input[AzureResourceManagerUserAssignedIdentityArgsDict]]
        ]
    ]

@pulumi.input_type
class AzureResourceManagerManagedIdentityPropertiesArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ManagedIdentityType]],
        user_assigned_identities: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[AzureResourceManagerUserAssignedIdentityArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ManagedIdentityType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ManagedIdentityType]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[str, pulumi.Input[AzureResourceManagerUserAssignedIdentityArgs]]
        ]
    ]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[AzureResourceManagerUserAssignedIdentityArgs]]
            ]
        ],
    ): ...

class AzureResourceManagerUserAssignedIdentityArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureResourceManagerUserAssignedIdentityArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CategoryArgsDict(TypedDict):
    feeds: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    url_custom: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class CategoryArgs:
    def __init__(
        __self__,
        *,
        feeds: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        url_custom: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def feeds(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @feeds.setter
    def feeds(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="urlCustom")
    def url_custom(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @url_custom.setter
    def url_custom(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class DNSSettingsArgsDict(TypedDict):
    dns_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[IPAddressArgsDict]]]]
    enable_dns_proxy: NotRequired[pulumi.Input[Union[_builtins.str, DNSProxy]]]
    enabled_dns_type: NotRequired[pulumi.Input[Union[_builtins.str, EnabledDNSType]]]

@pulumi.input_type
class DNSSettingsArgs:
    def __init__(
        __self__,
        *,
        dns_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[IPAddressArgs]]]
        ] = ...,
        enable_dns_proxy: Optional[pulumi.Input[Union[_builtins.str, DNSProxy]]] = ...,
        enabled_dns_type: Optional[
            pulumi.Input[Union[_builtins.str, EnabledDNSType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IPAddressArgs]]]]: ...
    @dns_servers.setter
    def dns_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IPAddressArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableDnsProxy")
    def enable_dns_proxy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DNSProxy]]]: ...
    @enable_dns_proxy.setter
    def enable_dns_proxy(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DNSProxy]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enabledDnsType")
    def enabled_dns_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EnabledDNSType]]]: ...
    @enabled_dns_type.setter
    def enabled_dns_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EnabledDNSType]]]
    ): ...

class DestinationAddrArgsDict(TypedDict):
    cidrs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    countries: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    feeds: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    fqdn_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    prefix_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DestinationAddrArgs:
    def __init__(
        __self__,
        *,
        cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        countries: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        feeds: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        fqdn_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        prefix_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidrs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cidrs.setter
    def cidrs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def countries(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @countries.setter
    def countries(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def feeds(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @feeds.setter
    def feeds(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fqdnLists")
    def fqdn_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @fqdn_lists.setter
    def fqdn_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="prefixLists")
    def prefix_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @prefix_lists.setter
    def prefix_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class EndpointConfigurationArgsDict(TypedDict):
    address: pulumi.Input[IPAddressArgsDict]
    port: pulumi.Input[_builtins.str]

@pulumi.input_type
class EndpointConfigurationArgs:
    def __init__(
        __self__,
        *,
        address: pulumi.Input[IPAddressArgs],
        port: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> pulumi.Input[IPAddressArgs]: ...
    @address.setter
    def address(self, value: pulumi.Input[IPAddressArgs]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.str]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.str]): ...

class FrontendSettingArgsDict(TypedDict):
    backend_configuration: pulumi.Input[EndpointConfigurationArgsDict]
    frontend_configuration: pulumi.Input[EndpointConfigurationArgsDict]
    name: pulumi.Input[_builtins.str]
    protocol: pulumi.Input[Union[_builtins.str, ProtocolType]]

@pulumi.input_type
class FrontendSettingArgs:
    def __init__(
        __self__,
        *,
        backend_configuration: pulumi.Input[EndpointConfigurationArgs],
        frontend_configuration: pulumi.Input[EndpointConfigurationArgs],
        name: pulumi.Input[_builtins.str],
        protocol: pulumi.Input[Union[_builtins.str, ProtocolType]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendConfiguration")
    def backend_configuration(self) -> pulumi.Input[EndpointConfigurationArgs]: ...
    @backend_configuration.setter
    def backend_configuration(self, value: pulumi.Input[EndpointConfigurationArgs]): ...
    @_builtins.property
    @pulumi.getter(name="frontendConfiguration")
    def frontend_configuration(self) -> pulumi.Input[EndpointConfigurationArgs]: ...
    @frontend_configuration.setter
    def frontend_configuration(
        self, value: pulumi.Input[EndpointConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[Union[_builtins.str, ProtocolType]]: ...
    @protocol.setter
    def protocol(self, value: pulumi.Input[Union[_builtins.str, ProtocolType]]): ...

class IPAddressSpaceArgsDict(TypedDict):
    address_space: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IPAddressSpaceArgs:
    def __init__(
        __self__,
        *,
        address_space: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressSpace")
    def address_space(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_space.setter
    def address_space(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IPAddressArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IPAddressArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MarketplaceDetailsArgsDict(TypedDict):
    offer_id: pulumi.Input[_builtins.str]
    publisher_id: pulumi.Input[_builtins.str]
    marketplace_subscription_status: NotRequired[
        pulumi.Input[Union[_builtins.str, MarketplaceSubscriptionStatus]]
    ]

@pulumi.input_type
class MarketplaceDetailsArgs:
    def __init__(
        __self__,
        *,
        offer_id: pulumi.Input[_builtins.str],
        publisher_id: pulumi.Input[_builtins.str],
        marketplace_subscription_status: Optional[
            pulumi.Input[Union[_builtins.str, MarketplaceSubscriptionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="offerId")
    def offer_id(self) -> pulumi.Input[_builtins.str]: ...
    @offer_id.setter
    def offer_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> pulumi.Input[_builtins.str]: ...
    @publisher_id.setter
    def publisher_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="marketplaceSubscriptionStatus")
    def marketplace_subscription_status(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, MarketplaceSubscriptionStatus]]
    ]: ...
    @marketplace_subscription_status.setter
    def marketplace_subscription_status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, MarketplaceSubscriptionStatus]]
        ],
    ): ...

class NetworkProfileArgsDict(TypedDict):
    enable_egress_nat: pulumi.Input[Union[_builtins.str, EgressNat]]
    network_type: pulumi.Input[Union[_builtins.str, NetworkType]]
    public_ips: pulumi.Input[Sequence[pulumi.Input[IPAddressArgsDict]]]
    egress_nat_ip: NotRequired[pulumi.Input[Sequence[pulumi.Input[IPAddressArgsDict]]]]
    private_source_nat_rules_destination: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    trusted_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vnet_configuration: NotRequired[pulumi.Input[VnetConfigurationArgsDict]]
    vwan_configuration: NotRequired[pulumi.Input[VwanConfigurationArgsDict]]

@pulumi.input_type
class NetworkProfileArgs:
    def __init__(
        __self__,
        *,
        enable_egress_nat: pulumi.Input[Union[_builtins.str, EgressNat]],
        network_type: pulumi.Input[Union[_builtins.str, NetworkType]],
        public_ips: pulumi.Input[Sequence[pulumi.Input[IPAddressArgs]]],
        egress_nat_ip: Optional[
            pulumi.Input[Sequence[pulumi.Input[IPAddressArgs]]]
        ] = ...,
        private_source_nat_rules_destination: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        trusted_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vnet_configuration: Optional[pulumi.Input[VnetConfigurationArgs]] = ...,
        vwan_configuration: Optional[pulumi.Input[VwanConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableEgressNat")
    def enable_egress_nat(self) -> pulumi.Input[Union[_builtins.str, EgressNat]]: ...
    @enable_egress_nat.setter
    def enable_egress_nat(
        self, value: pulumi.Input[Union[_builtins.str, EgressNat]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Input[Union[_builtins.str, NetworkType]]: ...
    @network_type.setter
    def network_type(self, value: pulumi.Input[Union[_builtins.str, NetworkType]]): ...
    @_builtins.property
    @pulumi.getter(name="publicIps")
    def public_ips(self) -> pulumi.Input[Sequence[pulumi.Input[IPAddressArgs]]]: ...
    @public_ips.setter
    def public_ips(
        self, value: pulumi.Input[Sequence[pulumi.Input[IPAddressArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressNatIp")
    def egress_nat_ip(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IPAddressArgs]]]]: ...
    @egress_nat_ip.setter
    def egress_nat_ip(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IPAddressArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateSourceNatRulesDestination")
    def private_source_nat_rules_destination(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @private_source_nat_rules_destination.setter
    def private_source_nat_rules_destination(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trustedRanges")
    def trusted_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @trusted_ranges.setter
    def trusted_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vnetConfiguration")
    def vnet_configuration(self) -> Optional[pulumi.Input[VnetConfigurationArgs]]: ...
    @vnet_configuration.setter
    def vnet_configuration(
        self, value: Optional[pulumi.Input[VnetConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vwanConfiguration")
    def vwan_configuration(self) -> Optional[pulumi.Input[VwanConfigurationArgs]]: ...
    @vwan_configuration.setter
    def vwan_configuration(
        self, value: Optional[pulumi.Input[VwanConfigurationArgs]]
    ): ...

class PanoramaConfigArgsDict(TypedDict):
    config_string: pulumi.Input[_builtins.str]

@pulumi.input_type
class PanoramaConfigArgs:
    def __init__(__self__, *, config_string: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configString")
    def config_string(self) -> pulumi.Input[_builtins.str]: ...
    @config_string.setter
    def config_string(self, value: pulumi.Input[_builtins.str]): ...

class PlanDataArgsDict(TypedDict):
    billing_cycle: pulumi.Input[Union[_builtins.str, BillingCycle]]
    plan_id: pulumi.Input[_builtins.str]
    usage_type: NotRequired[pulumi.Input[Union[_builtins.str, UsageType]]]

@pulumi.input_type
class PlanDataArgs:
    def __init__(
        __self__,
        *,
        billing_cycle: pulumi.Input[Union[_builtins.str, BillingCycle]],
        plan_id: pulumi.Input[_builtins.str],
        usage_type: Optional[pulumi.Input[Union[_builtins.str, UsageType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingCycle")
    def billing_cycle(self) -> pulumi.Input[Union[_builtins.str, BillingCycle]]: ...
    @billing_cycle.setter
    def billing_cycle(
        self, value: pulumi.Input[Union[_builtins.str, BillingCycle]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> pulumi.Input[_builtins.str]: ...
    @plan_id.setter
    def plan_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="usageType")
    def usage_type(self) -> Optional[pulumi.Input[Union[_builtins.str, UsageType]]]: ...
    @usage_type.setter
    def usage_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, UsageType]]]
    ): ...

class RulestackDetailsArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]
    rulestack_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RulestackDetailsArgs:
    def __init__(
        __self__,
        *,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        rulestack_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rulestackId")
    def rulestack_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rulestack_id.setter
    def rulestack_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecurityServicesArgsDict(TypedDict):
    anti_spyware_profile: NotRequired[pulumi.Input[_builtins.str]]
    anti_virus_profile: NotRequired[pulumi.Input[_builtins.str]]
    dns_subscription: NotRequired[pulumi.Input[_builtins.str]]
    file_blocking_profile: NotRequired[pulumi.Input[_builtins.str]]
    outbound_trust_certificate: NotRequired[pulumi.Input[_builtins.str]]
    outbound_un_trust_certificate: NotRequired[pulumi.Input[_builtins.str]]
    url_filtering_profile: NotRequired[pulumi.Input[_builtins.str]]
    vulnerability_profile: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecurityServicesArgs:
    def __init__(
        __self__,
        *,
        anti_spyware_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        anti_virus_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_subscription: Optional[pulumi.Input[_builtins.str]] = ...,
        file_blocking_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        outbound_trust_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        outbound_un_trust_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        url_filtering_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        vulnerability_profile: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="antiSpywareProfile")
    def anti_spyware_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @anti_spyware_profile.setter
    def anti_spyware_profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="antiVirusProfile")
    def anti_virus_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @anti_virus_profile.setter
    def anti_virus_profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsSubscription")
    def dns_subscription(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_subscription.setter
    def dns_subscription(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileBlockingProfile")
    def file_blocking_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_blocking_profile.setter
    def file_blocking_profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outboundTrustCertificate")
    def outbound_trust_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @outbound_trust_certificate.setter
    def outbound_trust_certificate(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outboundUnTrustCertificate")
    def outbound_un_trust_certificate(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @outbound_un_trust_certificate.setter
    def outbound_un_trust_certificate(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="urlFilteringProfile")
    def url_filtering_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url_filtering_profile.setter
    def url_filtering_profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vulnerabilityProfile")
    def vulnerability_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vulnerability_profile.setter
    def vulnerability_profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SourceAddrArgsDict(TypedDict):
    cidrs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    countries: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    feeds: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    prefix_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class SourceAddrArgs:
    def __init__(
        __self__,
        *,
        cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        countries: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        feeds: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        prefix_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidrs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cidrs.setter
    def cidrs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def countries(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @countries.setter
    def countries(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def feeds(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @feeds.setter
    def feeds(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="prefixLists")
    def prefix_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @prefix_lists.setter
    def prefix_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class StrataCloudManagerConfigArgsDict(TypedDict):
    cloud_manager_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class StrataCloudManagerConfigArgs:
    def __init__(
        __self__, *, cloud_manager_name: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudManagerName")
    def cloud_manager_name(self) -> pulumi.Input[_builtins.str]: ...
    @cloud_manager_name.setter
    def cloud_manager_name(self, value: pulumi.Input[_builtins.str]): ...

class TagInfoArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class TagInfoArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class VnetConfigurationArgsDict(TypedDict):
    trust_subnet: pulumi.Input[IPAddressSpaceArgsDict]
    un_trust_subnet: pulumi.Input[IPAddressSpaceArgsDict]
    vnet: pulumi.Input[IPAddressSpaceArgsDict]
    ip_of_trust_subnet_for_udr: NotRequired[pulumi.Input[IPAddressArgsDict]]

@pulumi.input_type
class VnetConfigurationArgs:
    def __init__(
        __self__,
        *,
        trust_subnet: pulumi.Input[IPAddressSpaceArgs],
        un_trust_subnet: pulumi.Input[IPAddressSpaceArgs],
        vnet: pulumi.Input[IPAddressSpaceArgs],
        ip_of_trust_subnet_for_udr: Optional[pulumi.Input[IPAddressArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="trustSubnet")
    def trust_subnet(self) -> pulumi.Input[IPAddressSpaceArgs]: ...
    @trust_subnet.setter
    def trust_subnet(self, value: pulumi.Input[IPAddressSpaceArgs]): ...
    @_builtins.property
    @pulumi.getter(name="unTrustSubnet")
    def un_trust_subnet(self) -> pulumi.Input[IPAddressSpaceArgs]: ...
    @un_trust_subnet.setter
    def un_trust_subnet(self, value: pulumi.Input[IPAddressSpaceArgs]): ...
    @_builtins.property
    @pulumi.getter
    def vnet(self) -> pulumi.Input[IPAddressSpaceArgs]: ...
    @vnet.setter
    def vnet(self, value: pulumi.Input[IPAddressSpaceArgs]): ...
    @_builtins.property
    @pulumi.getter(name="ipOfTrustSubnetForUdr")
    def ip_of_trust_subnet_for_udr(self) -> Optional[pulumi.Input[IPAddressArgs]]: ...
    @ip_of_trust_subnet_for_udr.setter
    def ip_of_trust_subnet_for_udr(
        self, value: Optional[pulumi.Input[IPAddressArgs]]
    ): ...

class VwanConfigurationArgsDict(TypedDict):
    v_hub: pulumi.Input[IPAddressSpaceArgsDict]
    ip_of_trust_subnet_for_udr: NotRequired[pulumi.Input[IPAddressArgsDict]]
    network_virtual_appliance_id: NotRequired[pulumi.Input[_builtins.str]]
    trust_subnet: NotRequired[pulumi.Input[IPAddressSpaceArgsDict]]
    un_trust_subnet: NotRequired[pulumi.Input[IPAddressSpaceArgsDict]]

@pulumi.input_type
class VwanConfigurationArgs:
    def __init__(
        __self__,
        *,
        v_hub: pulumi.Input[IPAddressSpaceArgs],
        ip_of_trust_subnet_for_udr: Optional[pulumi.Input[IPAddressArgs]] = ...,
        network_virtual_appliance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_subnet: Optional[pulumi.Input[IPAddressSpaceArgs]] = ...,
        un_trust_subnet: Optional[pulumi.Input[IPAddressSpaceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vHub")
    def v_hub(self) -> pulumi.Input[IPAddressSpaceArgs]: ...
    @v_hub.setter
    def v_hub(self, value: pulumi.Input[IPAddressSpaceArgs]): ...
    @_builtins.property
    @pulumi.getter(name="ipOfTrustSubnetForUdr")
    def ip_of_trust_subnet_for_udr(self) -> Optional[pulumi.Input[IPAddressArgs]]: ...
    @ip_of_trust_subnet_for_udr.setter
    def ip_of_trust_subnet_for_udr(
        self, value: Optional[pulumi.Input[IPAddressArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkVirtualApplianceId")
    def network_virtual_appliance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_virtual_appliance_id.setter
    def network_virtual_appliance_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trustSubnet")
    def trust_subnet(self) -> Optional[pulumi.Input[IPAddressSpaceArgs]]: ...
    @trust_subnet.setter
    def trust_subnet(self, value: Optional[pulumi.Input[IPAddressSpaceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="unTrustSubnet")
    def un_trust_subnet(self) -> Optional[pulumi.Input[IPAddressSpaceArgs]]: ...
    @un_trust_subnet.setter
    def un_trust_subnet(self, value: Optional[pulumi.Input[IPAddressSpaceArgs]]): ...
