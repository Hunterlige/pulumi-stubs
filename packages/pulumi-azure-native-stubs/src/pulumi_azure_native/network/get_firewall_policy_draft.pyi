import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFirewallPolicyDraftResult",
    "AwaitableGetFirewallPolicyDraftResult",
    "get_firewall_policy_draft",
    "get_firewall_policy_draft_output",
]

@pulumi.output_type
class GetFirewallPolicyDraftResult:
    def __init__(
        __self__,
        azure_api_version=...,
        base_policy=...,
        dns_settings=...,
        explicit_proxy=...,
        id=...,
        insights=...,
        intrusion_detection=...,
        location=...,
        name=...,
        snat=...,
        sql=...,
        tags=...,
        threat_intel_mode=...,
        threat_intel_whitelist=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="basePolicy")
    def base_policy(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[outputs.DnsSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="explicitProxy")
    def explicit_proxy(self) -> Optional[outputs.ExplicitProxyResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def insights(self) -> Optional[outputs.FirewallPolicyInsightsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="intrusionDetection")
    def intrusion_detection(
        self,
    ) -> Optional[outputs.FirewallPolicyIntrusionDetectionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def snat(self) -> Optional[outputs.FirewallPolicySNATResponse]: ...
    @_builtins.property
    @pulumi.getter
    def sql(self) -> Optional[outputs.FirewallPolicySQLResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="threatIntelMode")
    def threat_intel_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="threatIntelWhitelist")
    def threat_intel_whitelist(
        self,
    ) -> Optional[outputs.FirewallPolicyThreatIntelWhitelistResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetFirewallPolicyDraftResult(GetFirewallPolicyDraftResult):
    def __await__(self): ...

def get_firewall_policy_draft(
    firewall_policy_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFirewallPolicyDraftResult: ...
def get_firewall_policy_draft_output(
    firewall_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFirewallPolicyDraftResult]: ...
