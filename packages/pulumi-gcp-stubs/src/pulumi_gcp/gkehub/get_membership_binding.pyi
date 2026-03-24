import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMembershipBindingResult",
    "AwaitableGetMembershipBindingResult",
    "get_membership_binding",
    "get_membership_binding_output",
]

@pulumi.output_type
class GetMembershipBindingResult:
    def __init__(
        __self__,
        create_time=...,
        delete_time=...,
        effective_labels=...,
        id=...,
        labels=...,
        location=...,
        membership_binding_id=...,
        membership_id=...,
        name=...,
        project=...,
        pulumi_labels=...,
        scope=...,
        states=...,
        uid=...,
        update_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
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
    @pulumi.getter(name="membershipBindingId")
    def membership_binding_id(self) -> _builtins.str: ...
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
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def states(self) -> Sequence[outputs.GetMembershipBindingStateResult]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

class AwaitableGetMembershipBindingResult(GetMembershipBindingResult):
    def __await__(self): ...

def get_membership_binding(
    location: Optional[_builtins.str] = ...,
    membership_binding_id: Optional[_builtins.str] = ...,
    membership_id: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMembershipBindingResult: ...
def get_membership_binding_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    membership_binding_id: Optional[pulumi.Input[_builtins.str]] = ...,
    membership_id: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMembershipBindingResult]: ...
