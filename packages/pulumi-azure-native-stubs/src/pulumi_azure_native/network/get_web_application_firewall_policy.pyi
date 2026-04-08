import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebApplicationFirewallPolicyResult",
    "AwaitableGetWebApplicationFirewallPolicyResult",
    "get_web_application_firewall_policy",
    "get_web_application_firewall_policy_output",
]

@pulumi.output_type
class GetWebApplicationFirewallPolicyResult:
    def __init__(
        __self__,
        application_gateway_for_containers=...,
        application_gateways=...,
        azure_api_version=...,
        custom_rules=...,
        etag=...,
        http_listeners=...,
        id=...,
        location=...,
        managed_rules=...,
        name=...,
        path_based_rules=...,
        policy_settings=...,
        provisioning_state=...,
        resource_state=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationGatewayForContainers")
    def application_gateway_for_containers(
        self,
    ) -> Sequence[
        outputs.ApplicationGatewayForContainersReferenceDefinitionResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="applicationGateways")
    def application_gateways(self) -> Sequence[outputs.ApplicationGatewayResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customRules")
    def custom_rules(
        self,
    ) -> Optional[Sequence[outputs.WebApplicationFirewallCustomRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="httpListeners")
    def http_listeners(self) -> Sequence[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedRules")
    def managed_rules(self) -> outputs.ManagedRulesDefinitionResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pathBasedRules")
    def path_based_rules(self) -> Sequence[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="policySettings")
    def policy_settings(self) -> Optional[outputs.PolicySettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetWebApplicationFirewallPolicyResult(
    GetWebApplicationFirewallPolicyResult
):
    def __await__(self): ...

def get_web_application_firewall_policy(
    policy_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebApplicationFirewallPolicyResult: ...
def get_web_application_firewall_policy_output(
    policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebApplicationFirewallPolicyResult]: ...
