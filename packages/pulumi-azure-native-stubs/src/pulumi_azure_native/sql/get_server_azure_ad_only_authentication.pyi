import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServerAzureADOnlyAuthenticationResult",
    "AwaitableGetServerAzureADOnlyAuthenticationResult",
    "get_server_azure_ad_only_authentication",
    "get_server_azure_ad_only_authentication_output",
]

@pulumi.output_type
class GetServerAzureADOnlyAuthenticationResult:
    def __init__(
        __self__,
        azure_ad_only_authentication=...,
        azure_api_version=...,
        id=...,
        name=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureADOnlyAuthentication")
    def azure_ad_only_authentication(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetServerAzureADOnlyAuthenticationResult(
    GetServerAzureADOnlyAuthenticationResult
):
    def __await__(self): ...

def get_server_azure_ad_only_authentication(
    authentication_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServerAzureADOnlyAuthenticationResult: ...
def get_server_azure_ad_only_authentication_output(
    authentication_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServerAzureADOnlyAuthenticationResult]: ...
