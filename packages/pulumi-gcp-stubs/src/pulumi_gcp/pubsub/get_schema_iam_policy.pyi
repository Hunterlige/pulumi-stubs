import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSchemaIamPolicyResult",
    "AwaitableGetSchemaIamPolicyResult",
    "get_schema_iam_policy",
    "get_schema_iam_policy_output",
]

@pulumi.output_type
class GetSchemaIamPolicyResult:
    def __init__(
        __self__, etag=..., id=..., policy_data=..., project=..., schema=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...

class AwaitableGetSchemaIamPolicyResult(GetSchemaIamPolicyResult):
    def __await__(self): ...

def get_schema_iam_policy(
    project: Optional[_builtins.str] = ...,
    schema: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSchemaIamPolicyResult: ...
def get_schema_iam_policy_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    schema: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSchemaIamPolicyResult]: ...
