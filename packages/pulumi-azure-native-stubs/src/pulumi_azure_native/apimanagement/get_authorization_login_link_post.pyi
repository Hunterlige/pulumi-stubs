import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAuthorizationLoginLinkPostResult",
    "AwaitableGetAuthorizationLoginLinkPostResult",
    "get_authorization_login_link_post",
    "get_authorization_login_link_post_output",
]

@pulumi.output_type
class GetAuthorizationLoginLinkPostResult:
    def __init__(__self__, login_link=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loginLink")
    def login_link(self) -> Optional[_builtins.str]: ...

class AwaitableGetAuthorizationLoginLinkPostResult(GetAuthorizationLoginLinkPostResult):
    def __await__(self): ...

def get_authorization_login_link_post(
    authorization_id: Optional[_builtins.str] = ...,
    authorization_provider_id: Optional[_builtins.str] = ...,
    post_login_redirect_url: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAuthorizationLoginLinkPostResult: ...
def get_authorization_login_link_post_output(
    authorization_id: Optional[pulumi.Input[_builtins.str]] = ...,
    authorization_provider_id: Optional[pulumi.Input[_builtins.str]] = ...,
    post_login_redirect_url: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAuthorizationLoginLinkPostResult]: ...
