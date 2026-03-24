import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetResourcePolicyResult",
    "AwaitableGetResourcePolicyResult",
    "get_resource_policy",
    "get_resource_policy_output",
]

@pulumi.output_type
class GetResourcePolicyResult:
    def __init__(
        __self__, id=..., policy=..., region=..., resource_arn=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...

class AwaitableGetResourcePolicyResult(GetResourcePolicyResult):
    def __await__(self): ...

def get_resource_policy(
    region: Optional[_builtins.str] = ...,
    resource_arn: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetResourcePolicyResult: ...
def get_resource_policy_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetResourcePolicyResult]: ...
