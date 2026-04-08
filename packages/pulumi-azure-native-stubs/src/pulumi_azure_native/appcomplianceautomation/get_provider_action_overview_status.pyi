import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetProviderActionOverviewStatusResult",
    "AwaitableGetProviderActionOverviewStatusResult",
    "get_provider_action_overview_status",
    "get_provider_action_overview_status_output",
]

@pulumi.output_type
class GetProviderActionOverviewStatusResult:
    def __init__(__self__, status_list=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="statusList")
    def status_list(self) -> Optional[Sequence[outputs.StatusItemResponse]]: ...

class AwaitableGetProviderActionOverviewStatusResult(
    GetProviderActionOverviewStatusResult
):
    def __await__(self): ...

def get_provider_action_overview_status(
    type: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetProviderActionOverviewStatusResult: ...
def get_provider_action_overview_status_output(
    type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetProviderActionOverviewStatusResult]: ...
