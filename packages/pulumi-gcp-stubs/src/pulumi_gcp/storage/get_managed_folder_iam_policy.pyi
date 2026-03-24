import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetManagedFolderIamPolicyResult",
    "AwaitableGetManagedFolderIamPolicyResult",
    "get_managed_folder_iam_policy",
    "get_managed_folder_iam_policy_output",
]

@pulumi.output_type
class GetManagedFolderIamPolicyResult:
    def __init__(
        __self__, bucket=..., etag=..., id=..., managed_folder=..., policy_data=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedFolder")
    def managed_folder(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...

class AwaitableGetManagedFolderIamPolicyResult(GetManagedFolderIamPolicyResult):
    def __await__(self): ...

def get_managed_folder_iam_policy(
    bucket: Optional[_builtins.str] = ...,
    managed_folder: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetManagedFolderIamPolicyResult: ...
def get_managed_folder_iam_policy_output(
    bucket: Optional[pulumi.Input[_builtins.str]] = ...,
    managed_folder: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetManagedFolderIamPolicyResult]: ...
