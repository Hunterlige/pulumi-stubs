import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPrefixListGlobalRulestackResult",
    "AwaitableGetPrefixListGlobalRulestackResult",
    "get_prefix_list_global_rulestack",
    "get_prefix_list_global_rulestack_output",
]

@pulumi.output_type
class GetPrefixListGlobalRulestackResult:
    def __init__(
        __self__,
        audit_comment=...,
        azure_api_version=...,
        description=...,
        etag=...,
        id=...,
        name=...,
        prefix_list=...,
        provisioning_state=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="prefixList")
    def prefix_list(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetPrefixListGlobalRulestackResult(GetPrefixListGlobalRulestackResult):
    def __await__(self): ...

def get_prefix_list_global_rulestack(
    global_rulestack_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPrefixListGlobalRulestackResult: ...
def get_prefix_list_global_rulestack_output(
    global_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPrefixListGlobalRulestackResult]: ...
