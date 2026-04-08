import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNamespaceNetworkRuleSetResult",
    "AwaitableGetNamespaceNetworkRuleSetResult",
    "get_namespace_network_rule_set",
    "get_namespace_network_rule_set_output",
]

@pulumi.output_type
class GetNamespaceNetworkRuleSetResult:
    def __init__(
        __self__,
        azure_api_version=...,
        default_action=...,
        id=...,
        ip_rules=...,
        location=...,
        name=...,
        public_network_access=...,
        system_data=...,
        trusted_service_access_enabled=...,
        type=...,
        virtual_network_rules=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[Sequence[outputs.NWRuleSetIpRulesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="trustedServiceAccessEnabled")
    def trusted_service_access_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(
        self,
    ) -> Optional[Sequence[outputs.NWRuleSetVirtualNetworkRulesResponse]]: ...

class AwaitableGetNamespaceNetworkRuleSetResult(GetNamespaceNetworkRuleSetResult):
    def __await__(self): ...

def get_namespace_network_rule_set(
    namespace_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNamespaceNetworkRuleSetResult: ...
def get_namespace_network_rule_set_output(
    namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNamespaceNetworkRuleSetResult]: ...
