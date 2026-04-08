import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListServiceGloballyEnabledApmsResult",
    "AwaitableListServiceGloballyEnabledApmsResult",
    "list_service_globally_enabled_apms",
    "list_service_globally_enabled_apms_output",
]

@pulumi.output_type
class ListServiceGloballyEnabledApmsResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[_builtins.str]]: ...

class AwaitableListServiceGloballyEnabledApmsResult(
    ListServiceGloballyEnabledApmsResult
):
    def __await__(self): ...

def list_service_globally_enabled_apms(
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListServiceGloballyEnabledApmsResult: ...
def list_service_globally_enabled_apms_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListServiceGloballyEnabledApmsResult]: ...
