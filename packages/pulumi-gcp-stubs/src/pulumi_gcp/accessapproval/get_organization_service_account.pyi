import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetOrganizationServiceAccountResult",
    "AwaitableGetOrganizationServiceAccountResult",
    "get_organization_service_account",
    "get_organization_service_account_output",
]

@pulumi.output_type
class GetOrganizationServiceAccountResult:
    def __init__(
        __self__, account_email=..., id=..., name=..., organization_id=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountEmail")
    def account_email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> _builtins.str: ...

class AwaitableGetOrganizationServiceAccountResult(GetOrganizationServiceAccountResult):
    def __await__(self): ...

def get_organization_service_account(
    organization_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetOrganizationServiceAccountResult: ...
def get_organization_service_account_output(
    organization_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOrganizationServiceAccountResult]: ...
