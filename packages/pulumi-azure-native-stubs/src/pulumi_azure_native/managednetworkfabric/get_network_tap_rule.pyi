import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNetworkTapRuleResult",
    "AwaitableGetNetworkTapRuleResult",
    "get_network_tap_rule",
    "get_network_tap_rule_output",
]

@pulumi.output_type
class GetNetworkTapRuleResult:
    def __init__(
        __self__,
        administrative_state=...,
        annotation=...,
        azure_api_version=...,
        configuration_state=...,
        configuration_type=...,
        dynamic_match_configurations=...,
        id=...,
        last_synced_time=...,
        location=...,
        match_configurations=...,
        name=...,
        network_tap_id=...,
        polling_interval_in_seconds=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        tap_rules_url=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dynamicMatchConfigurations")
    def dynamic_match_configurations(
        self,
    ) -> Optional[Sequence[outputs.CommonDynamicMatchConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastSyncedTime")
    def last_synced_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchConfigurations")
    def match_configurations(
        self,
    ) -> Optional[Sequence[outputs.NetworkTapRuleMatchConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkTapId")
    def network_tap_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pollingIntervalInSeconds")
    def polling_interval_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tapRulesUrl")
    def tap_rules_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetNetworkTapRuleResult(GetNetworkTapRuleResult):
    def __await__(self): ...

def get_network_tap_rule(
    network_tap_rule_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNetworkTapRuleResult: ...
def get_network_tap_rule_output(
    network_tap_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNetworkTapRuleResult]: ...
