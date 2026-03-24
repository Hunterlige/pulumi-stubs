import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkloadIdentityPoolProviderResult",
    "AwaitableGetWorkloadIdentityPoolProviderResult",
    "get_workload_identity_pool_provider",
    "get_workload_identity_pool_provider_output",
]

@pulumi.output_type
class GetWorkloadIdentityPoolProviderResult:
    def __init__(
        __self__,
        attribute_condition=...,
        attribute_mapping=...,
        aws=...,
        description=...,
        disabled=...,
        display_name=...,
        id=...,
        name=...,
        oidcs=...,
        project=...,
        samls=...,
        state=...,
        workload_identity_pool_id=...,
        workload_identity_pool_provider_id=...,
        x509s=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeCondition")
    def attribute_condition(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="attributeMapping")
    def attribute_mapping(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def aws(self) -> Sequence[outputs.GetWorkloadIdentityPoolProviderAwResult]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def oidcs(self) -> Sequence[outputs.GetWorkloadIdentityPoolProviderOidcResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def samls(self) -> Sequence[outputs.GetWorkloadIdentityPoolProviderSamlResult]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolId")
    def workload_identity_pool_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolProviderId")
    def workload_identity_pool_provider_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def x509s(self) -> Sequence[outputs.GetWorkloadIdentityPoolProviderX509Result]: ...

class AwaitableGetWorkloadIdentityPoolProviderResult(
    GetWorkloadIdentityPoolProviderResult
):
    def __await__(self): ...

def get_workload_identity_pool_provider(
    project: Optional[_builtins.str] = ...,
    workload_identity_pool_id: Optional[_builtins.str] = ...,
    workload_identity_pool_provider_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkloadIdentityPoolProviderResult: ...
def get_workload_identity_pool_provider_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    workload_identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    workload_identity_pool_provider_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkloadIdentityPoolProviderResult]: ...
