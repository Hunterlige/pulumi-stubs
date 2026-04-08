import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListTenantAccessSecretsResult",
    "AwaitableListTenantAccessSecretsResult",
    "list_tenant_access_secrets",
    "list_tenant_access_secrets_output",
]

@pulumi.output_type
class ListTenantAccessSecretsResult:
    def __init__(
        __self__,
        enabled=...,
        id=...,
        primary_key=...,
        principal_id=...,
        secondary_key=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[_builtins.str]: ...

class AwaitableListTenantAccessSecretsResult(ListTenantAccessSecretsResult):
    def __await__(self): ...

def list_tenant_access_secrets(
    access_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListTenantAccessSecretsResult: ...
def list_tenant_access_secrets_output(
    access_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListTenantAccessSecretsResult]: ...
