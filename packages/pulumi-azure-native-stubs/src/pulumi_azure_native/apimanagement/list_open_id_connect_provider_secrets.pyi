import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListOpenIdConnectProviderSecretsResult",
    "AwaitableListOpenIdConnectProviderSecretsResult",
    "list_open_id_connect_provider_secrets",
    "list_open_id_connect_provider_secrets_output",
]

@pulumi.output_type
class ListOpenIdConnectProviderSecretsResult:
    def __init__(__self__, client_secret=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...

class AwaitableListOpenIdConnectProviderSecretsResult(
    ListOpenIdConnectProviderSecretsResult
):
    def __await__(self): ...

def list_open_id_connect_provider_secrets(
    opid: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListOpenIdConnectProviderSecretsResult: ...
def list_open_id_connect_provider_secrets_output(
    opid: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListOpenIdConnectProviderSecretsResult]: ...
