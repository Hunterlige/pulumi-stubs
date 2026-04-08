import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListGitHubOwnerAvailableResult",
    "AwaitableListGitHubOwnerAvailableResult",
    "list_git_hub_owner_available",
    "list_git_hub_owner_available_output",
]

@pulumi.output_type
class ListGitHubOwnerAvailableResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.GitHubOwnerResponse]]: ...

class AwaitableListGitHubOwnerAvailableResult(ListGitHubOwnerAvailableResult):
    def __await__(self): ...

def list_git_hub_owner_available(
    resource_group_name: Optional[_builtins.str] = ...,
    security_connector_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListGitHubOwnerAvailableResult: ...
def list_git_hub_owner_available_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    security_connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListGitHubOwnerAvailableResult]: ...
