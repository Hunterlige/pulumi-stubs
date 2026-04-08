import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetRuleResult", "AwaitableGetRuleResult", "get_rule", "get_rule_output"]

@pulumi.output_type
class GetRuleResult:
    def __init__(
        __self__,
        actions=...,
        azure_api_version=...,
        conditions=...,
        deployment_status=...,
        id=...,
        match_processing_behavior=...,
        name=...,
        order=...,
        provisioning_state=...,
        rule_set_name=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchProcessingBehavior")
    def match_processing_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ruleSetName")
    def rule_set_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetRuleResult(GetRuleResult):
    def __await__(self): ...

def get_rule(
    profile_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    rule_name: Optional[_builtins.str] = ...,
    rule_set_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRuleResult: ...
def get_rule_output(
    profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    rule_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRuleResult]: ...
