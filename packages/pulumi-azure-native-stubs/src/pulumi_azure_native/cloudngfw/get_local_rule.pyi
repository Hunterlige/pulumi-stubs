import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLocalRuleResult",
    "AwaitableGetLocalRuleResult",
    "get_local_rule",
    "get_local_rule_output",
]

@pulumi.output_type
class GetLocalRuleResult:
    def __init__(
        __self__,
        action_type=...,
        applications=...,
        audit_comment=...,
        azure_api_version=...,
        category=...,
        decryption_rule_type=...,
        description=...,
        destination=...,
        enable_logging=...,
        etag=...,
        id=...,
        inbound_inspection_certificate=...,
        name=...,
        negate_destination=...,
        negate_source=...,
        priority=...,
        protocol=...,
        protocol_port_list=...,
        provisioning_state=...,
        rule_name=...,
        rule_state=...,
        source=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def applications(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[outputs.CategoryResponse]: ...
    @_builtins.property
    @pulumi.getter(name="decryptionRuleType")
    def decryption_rule_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[outputs.DestinationAddrResponse]: ...
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inboundInspectionCertificate")
    def inbound_inspection_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="negateDestination")
    def negate_destination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="negateSource")
    def negate_source(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="protocolPortList")
    def protocol_port_list(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ruleState")
    def rule_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[outputs.SourceAddrResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[outputs.TagInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetLocalRuleResult(GetLocalRuleResult):
    def __await__(self): ...

def get_local_rule(
    local_rulestack_name: Optional[_builtins.str] = ...,
    priority: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLocalRuleResult: ...
def get_local_rule_output(
    local_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ...,
    priority: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLocalRuleResult]: ...
