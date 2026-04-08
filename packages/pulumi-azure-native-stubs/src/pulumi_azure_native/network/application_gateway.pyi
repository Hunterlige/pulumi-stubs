import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApplicationGatewayArgs", "ApplicationGateway"]

@pulumi.input_type
class ApplicationGatewayArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        application_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_certificates: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayAuthenticationCertificateArgs]]
            ]
        ] = ...,
        autoscale_configuration: Optional[
            pulumi.Input[ApplicationGatewayAutoscaleConfigurationArgs]
        ] = ...,
        backend_address_pools: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayBackendAddressPoolArgs]]
            ]
        ] = ...,
        backend_http_settings_collection: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayBackendHttpSettingsArgs]]
            ]
        ] = ...,
        backend_settings_collection: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayBackendSettingsArgs]]]
        ] = ...,
        custom_error_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayCustomErrorArgs]]]
        ] = ...,
        enable_fips: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_http2: Optional[pulumi.Input[_builtins.bool]] = ...,
        firewall_policy: Optional[pulumi.Input[SubResourceArgs]] = ...,
        force_firewall_policy_association: Optional[pulumi.Input[_builtins.bool]] = ...,
        frontend_ip_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayFrontendIPConfigurationArgs]]
            ]
        ] = ...,
        frontend_ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayFrontendPortArgs]]]
        ] = ...,
        gateway_ip_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayIPConfigurationArgs]]]
        ] = ...,
        global_configuration: Optional[
            pulumi.Input[ApplicationGatewayGlobalConfigurationArgs]
        ] = ...,
        http_listeners: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayHttpListenerArgs]]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        listeners: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayListenerArgs]]]
        ] = ...,
        load_distribution_policies: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayLoadDistributionPolicyArgs]]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayPrivateLinkConfigurationArgs]]
            ]
        ] = ...,
        probes: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayProbeArgs]]]
        ] = ...,
        redirect_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayRedirectConfigurationArgs]]
            ]
        ] = ...,
        request_routing_rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayRequestRoutingRuleArgs]]
            ]
        ] = ...,
        rewrite_rule_sets: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayRewriteRuleSetArgs]]]
        ] = ...,
        routing_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayRoutingRuleArgs]]]
        ] = ...,
        sku: Optional[pulumi.Input[ApplicationGatewaySkuArgs]] = ...,
        ssl_certificates: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewaySslCertificateArgs]]]
        ] = ...,
        ssl_policy: Optional[pulumi.Input[ApplicationGatewaySslPolicyArgs]] = ...,
        ssl_profiles: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewaySslProfileArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        trusted_client_certificates: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayTrustedClientCertificateArgs]]
            ]
        ] = ...,
        trusted_root_certificates: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayTrustedRootCertificateArgs]]
            ]
        ] = ...,
        url_path_maps: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayUrlPathMapArgs]]]
        ] = ...,
        web_application_firewall_configuration: Optional[
            pulumi.Input[ApplicationGatewayWebApplicationFirewallConfigurationArgs]
        ] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applicationGatewayName")
    def application_gateway_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_gateway_name.setter
    def application_gateway_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="authenticationCertificates")
    def authentication_certificates(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ApplicationGatewayAuthenticationCertificateArgs]]
        ]
    ]: ...
    @authentication_certificates.setter
    def authentication_certificates(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayAuthenticationCertificateArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoscaleConfiguration")
    def autoscale_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationGatewayAutoscaleConfigurationArgs]]: ...
    @autoscale_configuration.setter
    def autoscale_configuration(
        self,
        value: Optional[pulumi.Input[ApplicationGatewayAutoscaleConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="backendAddressPools")
    def backend_address_pools(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayBackendAddressPoolArgs]]]
    ]: ...
    @backend_address_pools.setter
    def backend_address_pools(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayBackendAddressPoolArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="backendHttpSettingsCollection")
    def backend_http_settings_collection(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayBackendHttpSettingsArgs]]]
    ]: ...
    @backend_http_settings_collection.setter
    def backend_http_settings_collection(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayBackendHttpSettingsArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="backendSettingsCollection")
    def backend_settings_collection(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayBackendSettingsArgs]]]
    ]: ...
    @backend_settings_collection.setter
    def backend_settings_collection(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayBackendSettingsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customErrorConfigurations")
    def custom_error_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayCustomErrorArgs]]]
    ]: ...
    @custom_error_configurations.setter
    def custom_error_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayCustomErrorArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableFips")
    def enable_fips(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_fips.setter
    def enable_fips(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableHttp2")
    def enable_http2(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_http2.setter
    def enable_http2(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @firewall_policy.setter
    def firewall_policy(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="forceFirewallPolicyAssociation")
    def force_firewall_policy_association(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_firewall_policy_association.setter
    def force_firewall_policy_association(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="frontendIPConfigurations")
    def frontend_ip_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ApplicationGatewayFrontendIPConfigurationArgs]]
        ]
    ]: ...
    @frontend_ip_configurations.setter
    def frontend_ip_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayFrontendIPConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="frontendPorts")
    def frontend_ports(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayFrontendPortArgs]]]
    ]: ...
    @frontend_ports.setter
    def frontend_ports(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayFrontendPortArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gatewayIPConfigurations")
    def gateway_ip_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayIPConfigurationArgs]]]
    ]: ...
    @gateway_ip_configurations.setter
    def gateway_ip_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayIPConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalConfiguration")
    def global_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationGatewayGlobalConfigurationArgs]]: ...
    @global_configuration.setter
    def global_configuration(
        self, value: Optional[pulumi.Input[ApplicationGatewayGlobalConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpListeners")
    def http_listeners(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayHttpListenerArgs]]]
    ]: ...
    @http_listeners.setter
    def http_listeners(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayHttpListenerArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def listeners(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayListenerArgs]]]
    ]: ...
    @listeners.setter
    def listeners(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayListenerArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadDistributionPolicies")
    def load_distribution_policies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ApplicationGatewayLoadDistributionPolicyArgs]]
        ]
    ]: ...
    @load_distribution_policies.setter
    def load_distribution_policies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayLoadDistributionPolicyArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkConfigurations")
    def private_link_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ApplicationGatewayPrivateLinkConfigurationArgs]]
        ]
    ]: ...
    @private_link_configurations.setter
    def private_link_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayPrivateLinkConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def probes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayProbeArgs]]]
    ]: ...
    @probes.setter
    def probes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayProbeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="redirectConfigurations")
    def redirect_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ApplicationGatewayRedirectConfigurationArgs]]
        ]
    ]: ...
    @redirect_configurations.setter
    def redirect_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayRedirectConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requestRoutingRules")
    def request_routing_rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayRequestRoutingRuleArgs]]]
    ]: ...
    @request_routing_rules.setter
    def request_routing_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayRequestRoutingRuleArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rewriteRuleSets")
    def rewrite_rule_sets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayRewriteRuleSetArgs]]]
    ]: ...
    @rewrite_rule_sets.setter
    def rewrite_rule_sets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayRewriteRuleSetArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingRules")
    def routing_rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayRoutingRuleArgs]]]
    ]: ...
    @routing_rules.setter
    def routing_rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayRoutingRuleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[ApplicationGatewaySkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[ApplicationGatewaySkuArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewaySslCertificateArgs]]]
    ]: ...
    @ssl_certificates.setter
    def ssl_certificates(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewaySslCertificateArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> Optional[pulumi.Input[ApplicationGatewaySslPolicyArgs]]: ...
    @ssl_policy.setter
    def ssl_policy(
        self, value: Optional[pulumi.Input[ApplicationGatewaySslPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslProfiles")
    def ssl_profiles(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewaySslProfileArgs]]]
    ]: ...
    @ssl_profiles.setter
    def ssl_profiles(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewaySslProfileArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trustedClientCertificates")
    def trusted_client_certificates(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ApplicationGatewayTrustedClientCertificateArgs]]
        ]
    ]: ...
    @trusted_client_certificates.setter
    def trusted_client_certificates(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayTrustedClientCertificateArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="trustedRootCertificates")
    def trusted_root_certificates(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ApplicationGatewayTrustedRootCertificateArgs]]
        ]
    ]: ...
    @trusted_root_certificates.setter
    def trusted_root_certificates(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayTrustedRootCertificateArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="urlPathMaps")
    def url_path_maps(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayUrlPathMapArgs]]]
    ]: ...
    @url_path_maps.setter
    def url_path_maps(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayUrlPathMapArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="webApplicationFirewallConfiguration")
    def web_application_firewall_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ApplicationGatewayWebApplicationFirewallConfigurationArgs]
    ]: ...
    @web_application_firewall_configuration.setter
    def web_application_firewall_configuration(
        self,
        value: Optional[
            pulumi.Input[ApplicationGatewayWebApplicationFirewallConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:network:ApplicationGateway")
class ApplicationGateway(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_certificates: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayAuthenticationCertificateArgs,
                            ApplicationGatewayAuthenticationCertificateArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        autoscale_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationGatewayAutoscaleConfigurationArgs,
                    ApplicationGatewayAutoscaleConfigurationArgsDict,
                ]
            ]
        ] = ...,
        backend_address_pools: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayBackendAddressPoolArgs,
                            ApplicationGatewayBackendAddressPoolArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        backend_http_settings_collection: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayBackendHttpSettingsArgs,
                            ApplicationGatewayBackendHttpSettingsArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        backend_settings_collection: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayBackendSettingsArgs,
                            ApplicationGatewayBackendSettingsArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        custom_error_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayCustomErrorArgs,
                            ApplicationGatewayCustomErrorArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        enable_fips: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_http2: Optional[pulumi.Input[_builtins.bool]] = ...,
        firewall_policy: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        force_firewall_policy_association: Optional[pulumi.Input[_builtins.bool]] = ...,
        frontend_ip_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayFrontendIPConfigurationArgs,
                            ApplicationGatewayFrontendIPConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        frontend_ports: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayFrontendPortArgs,
                            ApplicationGatewayFrontendPortArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        gateway_ip_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayIPConfigurationArgs,
                            ApplicationGatewayIPConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        global_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationGatewayGlobalConfigurationArgs,
                    ApplicationGatewayGlobalConfigurationArgsDict,
                ]
            ]
        ] = ...,
        http_listeners: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayHttpListenerArgs,
                            ApplicationGatewayHttpListenerArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        listeners: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayListenerArgs,
                            ApplicationGatewayListenerArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        load_distribution_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayLoadDistributionPolicyArgs,
                            ApplicationGatewayLoadDistributionPolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayPrivateLinkConfigurationArgs,
                            ApplicationGatewayPrivateLinkConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        probes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayProbeArgs, ApplicationGatewayProbeArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        redirect_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayRedirectConfigurationArgs,
                            ApplicationGatewayRedirectConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        request_routing_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayRequestRoutingRuleArgs,
                            ApplicationGatewayRequestRoutingRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rewrite_rule_sets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayRewriteRuleSetArgs,
                            ApplicationGatewayRewriteRuleSetArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        routing_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayRoutingRuleArgs,
                            ApplicationGatewayRoutingRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        sku: Optional[
            pulumi.Input[
                Union[ApplicationGatewaySkuArgs, ApplicationGatewaySkuArgsDict]
            ]
        ] = ...,
        ssl_certificates: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewaySslCertificateArgs,
                            ApplicationGatewaySslCertificateArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        ssl_policy: Optional[
            pulumi.Input[
                Union[
                    ApplicationGatewaySslPolicyArgs, ApplicationGatewaySslPolicyArgsDict
                ]
            ]
        ] = ...,
        ssl_profiles: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewaySslProfileArgs,
                            ApplicationGatewaySslProfileArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        trusted_client_certificates: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayTrustedClientCertificateArgs,
                            ApplicationGatewayTrustedClientCertificateArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        trusted_root_certificates: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayTrustedRootCertificateArgs,
                            ApplicationGatewayTrustedRootCertificateArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        url_path_maps: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationGatewayUrlPathMapArgs,
                            ApplicationGatewayUrlPathMapArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        web_application_firewall_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationGatewayWebApplicationFirewallConfigurationArgs,
                    ApplicationGatewayWebApplicationFirewallConfigurationArgsDict,
                ]
            ]
        ] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApplicationGatewayArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ApplicationGateway: ...
    @_builtins.property
    @pulumi.getter(name="authenticationCertificates")
    def authentication_certificates(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayAuthenticationCertificateResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="autoscaleConfiguration")
    def autoscale_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ApplicationGatewayAutoscaleConfigurationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backendAddressPools")
    def backend_address_pools(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayBackendAddressPoolResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="backendHttpSettingsCollection")
    def backend_http_settings_collection(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayBackendHttpSettingsResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="backendSettingsCollection")
    def backend_settings_collection(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayBackendSettingsResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="customErrorConfigurations")
    def custom_error_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayCustomErrorResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultPredefinedSslPolicy")
    def default_predefined_ssl_policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableFips")
    def enable_fips(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableHttp2")
    def enable_http2(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="forceFirewallPolicyAssociation")
    def force_firewall_policy_association(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="frontendIPConfigurations")
    def frontend_ip_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayFrontendIPConfigurationResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="frontendPorts")
    def frontend_ports(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayFrontendPortResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="gatewayIPConfigurations")
    def gateway_ip_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayIPConfigurationResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="globalConfiguration")
    def global_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ApplicationGatewayGlobalConfigurationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="httpListeners")
    def http_listeners(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayHttpListenerResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def listeners(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayListenerResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="loadDistributionPolicies")
    def load_distribution_policies(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayLoadDistributionPolicyResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operationalState")
    def operational_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.ApplicationGatewayPrivateEndpointConnectionResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkConfigurations")
    def private_link_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayPrivateLinkConfigurationResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def probes(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ApplicationGatewayProbeResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectConfigurations")
    def redirect_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayRedirectConfigurationResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="requestRoutingRules")
    def request_routing_rules(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayRequestRoutingRuleResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rewriteRuleSets")
    def rewrite_rule_sets(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayRewriteRuleSetResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="routingRules")
    def routing_rules(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayRoutingRuleResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.ApplicationGatewaySkuResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewaySslCertificateResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.ApplicationGatewaySslPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="sslProfiles")
    def ssl_profiles(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewaySslProfileResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="trustedClientCertificates")
    def trusted_client_certificates(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayTrustedClientCertificateResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="trustedRootCertificates")
    def trusted_root_certificates(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayTrustedRootCertificateResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="urlPathMaps")
    def url_path_maps(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationGatewayUrlPathMapResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="webApplicationFirewallConfiguration")
    def web_application_firewall_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ApplicationGatewayWebApplicationFirewallConfigurationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
