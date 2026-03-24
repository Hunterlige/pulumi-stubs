import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetKeyRingIamPolicyResult",
    "AwaitableGetKeyRingIamPolicyResult",
    "get_key_ring_iam_policy",
    "get_key_ring_iam_policy_output",
]

@pulumi.output_type
class GetKeyRingIamPolicyResult:
    def __init__(
        __self__, etag=..., id=..., key_ring_id=..., policy_data=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyRingId")
    def key_ring_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...

class AwaitableGetKeyRingIamPolicyResult(GetKeyRingIamPolicyResult):
    def __await__(self): ...

def get_key_ring_iam_policy(
    key_ring_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKeyRingIamPolicyResult: ...
def get_key_ring_iam_policy_output(
    key_ring_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKeyRingIamPolicyResult]: ...
