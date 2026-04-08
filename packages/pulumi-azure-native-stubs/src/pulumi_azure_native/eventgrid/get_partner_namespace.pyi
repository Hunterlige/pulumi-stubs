import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPartnerNamespaceResult",
    "AwaitableGetPartnerNamespaceResult",
    "get_partner_namespace",
    "get_partner_namespace_output",
]

@pulumi.output_type
class GetPartnerNamespaceResult:
    def __init__(
        __self__,
        azure_api_version=...,
        disable_local_auth=...,
        endpoint=...,
        id=...,
        inbound_ip_rules=...,
        location=...,
        minimum_tls_version_allowed=...,
        name=...,
        partner_registration_fully_qualified_id=...,
        partner_topic_routing_mode=...,
        private_endpoint_connections=...,
        provisioning_state=...,
        public_network_access=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inboundIpRules")
    def inbound_ip_rules(self) -> Optional[Sequence[outputs.InboundIpRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minimumTlsVersionAllowed")
    def minimum_tls_version_allowed(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="partnerRegistrationFullyQualifiedId")
    def partner_registration_fully_qualified_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partnerTopicRoutingMode")
    def partner_topic_routing_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Sequence[outputs.PrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetPartnerNamespaceResult(GetPartnerNamespaceResult):
    def __await__(self): ...

def get_partner_namespace(
    partner_namespace_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPartnerNamespaceResult: ...
def get_partner_namespace_output(
    partner_namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPartnerNamespaceResult]: ...
