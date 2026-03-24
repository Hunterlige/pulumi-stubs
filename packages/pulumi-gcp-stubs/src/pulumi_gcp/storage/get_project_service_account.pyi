import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetProjectServiceAccountResult",
    "AwaitableGetProjectServiceAccountResult",
    "get_project_service_account",
    "get_project_service_account_output",
]

@pulumi.output_type
class GetProjectServiceAccountResult:
    def __init__(
        __self__, email_address=..., id=..., member=..., project=..., user_project=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def member(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userProject")
    def user_project(self) -> Optional[_builtins.str]: ...

class AwaitableGetProjectServiceAccountResult(GetProjectServiceAccountResult):
    def __await__(self): ...

def get_project_service_account(
    project: Optional[_builtins.str] = ...,
    user_project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetProjectServiceAccountResult: ...
def get_project_service_account_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    user_project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetProjectServiceAccountResult]: ...
