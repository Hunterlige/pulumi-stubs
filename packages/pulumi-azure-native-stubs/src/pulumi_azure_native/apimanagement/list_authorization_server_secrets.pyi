import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListAuthorizationServerSecretsResult",
    "AwaitableListAuthorizationServerSecretsResult",
    "list_authorization_server_secrets",
    "list_authorization_server_secrets_output",
]

@pulumi.output_type
class ListAuthorizationServerSecretsResult:
    def __init__(
        __self__,
        client_secret=...,
        resource_owner_password=...,
        resource_owner_username=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceOwnerPassword")
    def resource_owner_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceOwnerUsername")
    def resource_owner_username(self) -> Optional[_builtins.str]: ...

class AwaitableListAuthorizationServerSecretsResult(
    ListAuthorizationServerSecretsResult
):
    def __await__(self): ...

def list_authorization_server_secrets(
    authsid: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListAuthorizationServerSecretsResult: ...
def list_authorization_server_secrets_output(
    authsid: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListAuthorizationServerSecretsResult]: ...
