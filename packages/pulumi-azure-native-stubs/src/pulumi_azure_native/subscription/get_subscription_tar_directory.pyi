import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSubscriptionTarDirectoryResult",
    "AwaitableGetSubscriptionTarDirectoryResult",
    "get_subscription_tar_directory",
    "get_subscription_tar_directory_output",
]

@pulumi.output_type
class GetSubscriptionTarDirectoryResult:
    def __init__(
        __self__, azure_api_version=..., id=..., name=..., properties=..., type=...
    ) -> None: ...
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
    def properties(self) -> outputs.TargetDirectoryResultPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSubscriptionTarDirectoryResult(GetSubscriptionTarDirectoryResult):
    def __await__(self): ...

def get_subscription_tar_directory(
    subscription_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSubscriptionTarDirectoryResult: ...
def get_subscription_tar_directory_output(
    subscription_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSubscriptionTarDirectoryResult]: ...
