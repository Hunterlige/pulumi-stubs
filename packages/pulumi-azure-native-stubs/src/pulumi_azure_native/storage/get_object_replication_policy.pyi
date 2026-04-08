import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetObjectReplicationPolicyResult",
    "AwaitableGetObjectReplicationPolicyResult",
    "get_object_replication_policy",
    "get_object_replication_policy_output",
]

@pulumi.output_type
class GetObjectReplicationPolicyResult:
    def __init__(
        __self__,
        azure_api_version=...,
        destination_account=...,
        enabled_time=...,
        id=...,
        metrics=...,
        name=...,
        policy_id=...,
        rules=...,
        source_account=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationAccount")
    def destination_account(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enabledTime")
    def enabled_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def metrics(
        self,
    ) -> Optional[outputs.ObjectReplicationPolicyPropertiesResponseMetrics]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[Sequence[outputs.ObjectReplicationPolicyRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceAccount")
    def source_account(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetObjectReplicationPolicyResult(GetObjectReplicationPolicyResult):
    def __await__(self): ...

def get_object_replication_policy(
    account_name: Optional[_builtins.str] = ...,
    object_replication_policy_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetObjectReplicationPolicyResult: ...
def get_object_replication_policy_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    object_replication_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetObjectReplicationPolicyResult]: ...
