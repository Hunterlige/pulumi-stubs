import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListListTenantConfigurationViolationResult",
    ...,
    "list_list_tenant_configuration_violation",
    "list_list_tenant_configuration_violation_output",
]

@pulumi.output_type
class ListListTenantConfigurationViolationResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.ViolationResponse]: ...

class AwaitableListListTenantConfigurationViolationResult(
    ListListTenantConfigurationViolationResult
):
    def __await__(self): ...

def list_list_tenant_configuration_violation(
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListListTenantConfigurationViolationResult: ...
def list_list_tenant_configuration_violation_output(
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListListTenantConfigurationViolationResult]: ...
