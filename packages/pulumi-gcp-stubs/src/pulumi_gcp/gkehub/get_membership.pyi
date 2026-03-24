import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMembershipResult",
    "AwaitableGetMembershipResult",
    "get_membership",
    "get_membership_output",
]

@pulumi.output_type
class GetMembershipResult:
    def __init__(
        __self__,
        authorities=...,
        effective_labels=...,
        endpoints=...,
        id=...,
        labels=...,
        location=...,
        membership_id=...,
        name=...,
        project=...,
        pulumi_labels=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def authorities(self) -> Sequence[outputs.GetMembershipAuthorityResult]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Sequence[outputs.GetMembershipEndpointResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="membershipId")
    def membership_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetMembershipResult(GetMembershipResult):
    def __await__(self): ...

def get_membership(
    location: Optional[_builtins.str] = ...,
    membership_id: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMembershipResult: ...
def get_membership_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    membership_id: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMembershipResult]: ...
