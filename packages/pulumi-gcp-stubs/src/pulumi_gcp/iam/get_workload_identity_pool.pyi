import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkloadIdentityPoolResult",
    "AwaitableGetWorkloadIdentityPoolResult",
    "get_workload_identity_pool",
    "get_workload_identity_pool_output",
]

@pulumi.output_type
class GetWorkloadIdentityPoolResult:
    def __init__(
        __self__,
        description=...,
        disabled=...,
        display_name=...,
        id=...,
        inline_certificate_issuance_configs=...,
        inline_trust_configs=...,
        mode=...,
        name=...,
        project=...,
        state=...,
        workload_identity_pool_id=...,
    ) -> None: ...
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
    @pulumi.getter(name="inlineCertificateIssuanceConfigs")
    def inline_certificate_issuance_configs(
        self,
    ) -> Sequence[
        outputs.GetWorkloadIdentityPoolInlineCertificateIssuanceConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inlineTrustConfigs")
    def inline_trust_configs(
        self,
    ) -> Sequence[outputs.GetWorkloadIdentityPoolInlineTrustConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolId")
    def workload_identity_pool_id(self) -> _builtins.str: ...

class AwaitableGetWorkloadIdentityPoolResult(GetWorkloadIdentityPoolResult):
    def __await__(self): ...

def get_workload_identity_pool(
    project: Optional[_builtins.str] = ...,
    workload_identity_pool_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkloadIdentityPoolResult: ...
def get_workload_identity_pool_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    workload_identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkloadIdentityPoolResult]: ...
