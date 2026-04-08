import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetApplicationGatewayResult",
    "AwaitableGetApplicationGatewayResult",
    "get_application_gateway",
    "get_application_gateway_output",
]

@pulumi.output_type
class GetApplicationGatewayResult:
    def __init__(
        __self__,
        authentication_certificates=...,
        autoscale_configuration=...,
        azure_api_version=...,
        backend_address_pools=...,
        backend_http_settings_collection=...,
        backend_settings_collection=...,
        custom_error_configurations=...,
        default_predefined_ssl_policy=...,
        enable_fips=...,
        enable_http2=...,
        etag=...,
        firewall_policy=...,
        force_firewall_policy_association=...,
        frontend_ip_configurations=...,
        frontend_ports=...,
        gateway_ip_configurations=...,
        global_configuration=...,
        http_listeners=...,
        id=...,
        identity=...,
        listeners=...,
        load_distribution_policies=...,
        location=...,
        name=...,
        operational_state=...,
        private_endpoint_connections=...,
        private_link_configurations=...,
        probes=...,
        provisioning_state=...,
        redirect_configurations=...,
        request_routing_rules=...,
        resource_guid=...,
        rewrite_rule_sets=...,
        routing_rules=...,
        sku=...,
        ssl_certificates=...,
        ssl_policy=...,
        ssl_profiles=...,
        tags=...,
        trusted_client_certificates=...,
        trusted_root_certificates=...,
        type=...,
        url_path_maps=...,
        web_application_firewall_configuration=...,
        zones=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationCertificates")
    def authentication_certificates(
        self,
    ) -> Optional[
        Sequence[outputs.ApplicationGatewayAuthenticationCertificateResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="autoscaleConfiguration")
    def autoscale_configuration(
        self,
    ) -> Optional[outputs.ApplicationGatewayAutoscaleConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backendAddressPools")
    def backend_address_pools(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGatewayBackendAddressPoolResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="backendHttpSettingsCollection")
    def backend_http_settings_collection(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGatewayBackendHttpSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="backendSettingsCollection")
    def backend_settings_collection(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGatewayBackendSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="customErrorConfigurations")
    def custom_error_configurations(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGatewayCustomErrorResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultPredefinedSslPolicy")
    def default_predefined_ssl_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enableFips")
    def enable_fips(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableHttp2")
    def enable_http2(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="forceFirewallPolicyAssociation")
    def force_firewall_policy_association(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="frontendIPConfigurations")
    def frontend_ip_configurations(
        self,
    ) -> Optional[
        Sequence[outputs.ApplicationGatewayFrontendIPConfigurationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="frontendPorts")
    def frontend_ports(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGatewayFrontendPortResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="gatewayIPConfigurations")
    def gateway_ip_configurations(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGatewayIPConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="globalConfiguration")
    def global_configuration(
        self,
    ) -> Optional[outputs.ApplicationGatewayGlobalConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="httpListeners")
    def http_listeners(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGatewayHttpListenerResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def listeners(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGatewayListenerResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="loadDistributionPolicies")
    def load_distribution_policies(
        self,
    ) -> Optional[
        Sequence[outputs.ApplicationGatewayLoadDistributionPolicyResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="operationalState")
    def operational_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Sequence[outputs.ApplicationGatewayPrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkConfigurations")
    def private_link_configurations(
        self,
    ) -> Optional[
        Sequence[outputs.ApplicationGatewayPrivateLinkConfigurationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def probes(self) -> Optional[Sequence[outputs.ApplicationGatewayProbeResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="redirectConfigurations")
    def redirect_configurations(
        self,
    ) -> Optional[
        Sequence[outputs.ApplicationGatewayRedirectConfigurationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="requestRoutingRules")
    def request_routing_rules(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGatewayRequestRoutingRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rewriteRuleSets")
    def rewrite_rule_sets(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGatewayRewriteRuleSetResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="routingRules")
    def routing_rules(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGatewayRoutingRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.ApplicationGatewaySkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGatewaySslCertificateResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> Optional[outputs.ApplicationGatewaySslPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sslProfiles")
    def ssl_profiles(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGatewaySslProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="trustedClientCertificates")
    def trusted_client_certificates(
        self,
    ) -> Optional[
        Sequence[outputs.ApplicationGatewayTrustedClientCertificateResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="trustedRootCertificates")
    def trusted_root_certificates(
        self,
    ) -> Optional[
        Sequence[outputs.ApplicationGatewayTrustedRootCertificateResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="urlPathMaps")
    def url_path_maps(
        self,
    ) -> Optional[Sequence[outputs.ApplicationGatewayUrlPathMapResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="webApplicationFirewallConfiguration")
    def web_application_firewall_configuration(
        self,
    ) -> Optional[
        outputs.ApplicationGatewayWebApplicationFirewallConfigurationResponse
    ]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...

class AwaitableGetApplicationGatewayResult(GetApplicationGatewayResult):
    def __await__(self): ...

def get_application_gateway(
    application_gateway_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetApplicationGatewayResult: ...
def get_application_gateway_output(
    application_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetApplicationGatewayResult]: ...
