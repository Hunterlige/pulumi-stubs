import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTransferProjectServieAccountResult",
    "AwaitableGetTransferProjectServieAccountResult",
    "get_transfer_project_servie_account",
    "get_transfer_project_servie_account_output",
]

@pulumi.output_type
class GetTransferProjectServieAccountResult:
    def __init__(
        __self__, email=..., id=..., member=..., project=..., subject_id=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
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
    @pulumi.getter(name="subjectId")
    def subject_id(self) -> _builtins.str: ...

class AwaitableGetTransferProjectServieAccountResult(
    GetTransferProjectServieAccountResult
):
    def __await__(self): ...

def get_transfer_project_servie_account(
    project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetTransferProjectServieAccountResult: ...
def get_transfer_project_servie_account_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTransferProjectServieAccountResult]: ...
