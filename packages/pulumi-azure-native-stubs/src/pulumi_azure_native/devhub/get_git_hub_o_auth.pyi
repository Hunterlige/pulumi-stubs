import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGitHubOAuthResult",
    "AwaitableGetGitHubOAuthResult",
    "get_git_hub_o_auth",
    "get_git_hub_o_auth_output",
]

@pulumi.output_type
class GetGitHubOAuthResult:
    def __init__(__self__, auth_url=..., token=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authURL")
    def auth_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[_builtins.str]: ...

class AwaitableGetGitHubOAuthResult(GetGitHubOAuthResult):
    def __await__(self): ...

def get_git_hub_o_auth(
    location: Optional[_builtins.str] = ...,
    redirect_url: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGitHubOAuthResult: ...
def get_git_hub_o_auth_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    redirect_url: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGitHubOAuthResult]: ...
