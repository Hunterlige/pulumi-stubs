import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetManagedZoneIamPolicyResult",
    "AwaitableGetManagedZoneIamPolicyResult",
    "get_managed_zone_iam_policy",
    "get_managed_zone_iam_policy_output",
]

@pulumi.output_type
class GetManagedZoneIamPolicyResult:
    def __init__(
        __self__, etag=..., id=..., managed_zone=..., policy_data=..., project=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedZone")
    def managed_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...

class AwaitableGetManagedZoneIamPolicyResult(GetManagedZoneIamPolicyResult):
    def __await__(self): ...

def get_managed_zone_iam_policy(
    managed_zone: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetManagedZoneIamPolicyResult: ...
def get_managed_zone_iam_policy_output(
    managed_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetManagedZoneIamPolicyResult]: ...
