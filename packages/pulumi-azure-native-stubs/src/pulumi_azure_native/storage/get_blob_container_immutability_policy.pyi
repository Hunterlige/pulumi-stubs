import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBlobContainerImmutabilityPolicyResult",
    "AwaitableGetBlobContainerImmutabilityPolicyResult",
    "get_blob_container_immutability_policy",
    "get_blob_container_immutability_policy_output",
]

@pulumi.output_type
class GetBlobContainerImmutabilityPolicyResult:
    def __init__(
        __self__,
        allow_protected_append_writes=...,
        allow_protected_append_writes_all=...,
        azure_api_version=...,
        etag=...,
        id=...,
        immutability_period_since_creation_in_days=...,
        name=...,
        state=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowProtectedAppendWrites")
    def allow_protected_append_writes(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="allowProtectedAppendWritesAll")
    def allow_protected_append_writes_all(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="immutabilityPeriodSinceCreationInDays")
    def immutability_period_since_creation_in_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetBlobContainerImmutabilityPolicyResult(
    GetBlobContainerImmutabilityPolicyResult
):
    def __await__(self): ...

def get_blob_container_immutability_policy(
    account_name: Optional[_builtins.str] = ...,
    container_name: Optional[_builtins.str] = ...,
    immutability_policy_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBlobContainerImmutabilityPolicyResult: ...
def get_blob_container_immutability_policy_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    container_name: Optional[pulumi.Input[_builtins.str]] = ...,
    immutability_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBlobContainerImmutabilityPolicyResult]: ...
