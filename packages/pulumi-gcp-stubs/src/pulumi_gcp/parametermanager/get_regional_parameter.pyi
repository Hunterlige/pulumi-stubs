import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRegionalParameterResult",
    "AwaitableGetRegionalParameterResult",
    "get_regional_parameter",
    "get_regional_parameter_output",
]

@pulumi.output_type
class GetRegionalParameterResult:
    def __init__(
        __self__,
        create_time=...,
        effective_labels=...,
        format=...,
        id=...,
        kms_key=...,
        labels=...,
        location=...,
        name=...,
        parameter_id=...,
        policy_members=...,
        project=...,
        pulumi_labels=...,
        update_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterId")
    def parameter_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyMembers")
    def policy_members(
        self,
    ) -> Sequence[outputs.GetRegionalParameterPolicyMemberResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

class AwaitableGetRegionalParameterResult(GetRegionalParameterResult):
    def __await__(self): ...

def get_regional_parameter(
    location: Optional[_builtins.str] = ...,
    parameter_id: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRegionalParameterResult: ...
def get_regional_parameter_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    parameter_id: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRegionalParameterResult]: ...
