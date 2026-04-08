import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListApplicationAllowedUpgradePlansResult",
    "AwaitableListApplicationAllowedUpgradePlansResult",
    "list_application_allowed_upgrade_plans",
    "list_application_allowed_upgrade_plans_output",
]

@pulumi.output_type
class ListApplicationAllowedUpgradePlansResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.PlanResponse]]: ...

class AwaitableListApplicationAllowedUpgradePlansResult(
    ListApplicationAllowedUpgradePlansResult
):
    def __await__(self): ...

def list_application_allowed_upgrade_plans(
    application_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListApplicationAllowedUpgradePlansResult: ...
def list_application_allowed_upgrade_plans_output(
    application_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListApplicationAllowedUpgradePlansResult]: ...
