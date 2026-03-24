import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGlossaryIamPolicyResult",
    "AwaitableGetGlossaryIamPolicyResult",
    "get_glossary_iam_policy",
    "get_glossary_iam_policy_output",
]

@pulumi.output_type
class GetGlossaryIamPolicyResult:
    def __init__(
        __self__,
        etag=...,
        glossary_id=...,
        id=...,
        location=...,
        policy_data=...,
        project=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="glossaryId")
    def glossary_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...

class AwaitableGetGlossaryIamPolicyResult(GetGlossaryIamPolicyResult):
    def __await__(self): ...

def get_glossary_iam_policy(
    glossary_id: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGlossaryIamPolicyResult: ...
def get_glossary_iam_policy_output(
    glossary_id: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGlossaryIamPolicyResult]: ...
