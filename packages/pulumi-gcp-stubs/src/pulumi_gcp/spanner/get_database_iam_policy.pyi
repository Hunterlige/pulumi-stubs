import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDatabaseIamPolicyResult",
    "AwaitableGetDatabaseIamPolicyResult",
    "get_database_iam_policy",
    "get_database_iam_policy_output",
]

@pulumi.output_type
class GetDatabaseIamPolicyResult:
    def __init__(
        __self__,
        database=...,
        etag=...,
        id=...,
        instance=...,
        policy_data=...,
        project=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...

class AwaitableGetDatabaseIamPolicyResult(GetDatabaseIamPolicyResult):
    def __await__(self): ...

def get_database_iam_policy(
    database: Optional[_builtins.str] = ...,
    instance: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDatabaseIamPolicyResult: ...
def get_database_iam_policy_output(
    database: Optional[pulumi.Input[_builtins.str]] = ...,
    instance: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDatabaseIamPolicyResult]: ...
