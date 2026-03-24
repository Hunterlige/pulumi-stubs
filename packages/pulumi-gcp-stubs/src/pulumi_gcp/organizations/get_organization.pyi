import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetOrganizationResult",
    "AwaitableGetOrganizationResult",
    "get_organization",
    "get_organization_output",
]

@pulumi.output_type
class GetOrganizationResult:
    def __init__(
        __self__,
        create_time=...,
        directory_customer_id=...,
        domain=...,
        id=...,
        lifecycle_state=...,
        name=...,
        org_id=...,
        organization=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="directoryCustomerId")
    def directory_customer_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[_builtins.str]: ...

class AwaitableGetOrganizationResult(GetOrganizationResult):
    def __await__(self): ...

def get_organization(
    domain: Optional[_builtins.str] = ...,
    organization: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetOrganizationResult: ...
def get_organization_output(
    domain: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    organization: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOrganizationResult]: ...
