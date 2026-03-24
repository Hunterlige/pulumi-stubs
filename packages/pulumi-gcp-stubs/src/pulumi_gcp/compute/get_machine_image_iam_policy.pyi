import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMachineImageIamPolicyResult",
    "AwaitableGetMachineImageIamPolicyResult",
    "get_machine_image_iam_policy",
    "get_machine_image_iam_policy_output",
]

@pulumi.output_type
class GetMachineImageIamPolicyResult:
    def __init__(
        __self__, etag=..., id=..., machine_image=..., policy_data=..., project=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="machineImage")
    def machine_image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...

class AwaitableGetMachineImageIamPolicyResult(GetMachineImageIamPolicyResult):
    def __await__(self): ...

def get_machine_image_iam_policy(
    machine_image: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMachineImageIamPolicyResult: ...
def get_machine_image_iam_policy_output(
    machine_image: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMachineImageIamPolicyResult]: ...
