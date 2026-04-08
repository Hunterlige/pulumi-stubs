import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetApiManagementServiceSsoTokenResult",
    "AwaitableGetApiManagementServiceSsoTokenResult",
    "get_api_management_service_sso_token",
    "get_api_management_service_sso_token_output",
]

@pulumi.output_type
class GetApiManagementServiceSsoTokenResult:
    def __init__(__self__, redirect_uri=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[_builtins.str]: ...

class AwaitableGetApiManagementServiceSsoTokenResult(
    GetApiManagementServiceSsoTokenResult
):
    def __await__(self): ...

def get_api_management_service_sso_token(
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetApiManagementServiceSsoTokenResult: ...
def get_api_management_service_sso_token_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetApiManagementServiceSsoTokenResult]: ...
