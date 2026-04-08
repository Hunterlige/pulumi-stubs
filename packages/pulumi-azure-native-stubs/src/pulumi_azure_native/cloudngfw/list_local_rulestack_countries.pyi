import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListLocalRulestackCountriesResult",
    "AwaitableListLocalRulestackCountriesResult",
    "list_local_rulestack_countries",
    "list_local_rulestack_countries_output",
]

@pulumi.output_type
class ListLocalRulestackCountriesResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.CountryResponse]: ...

class AwaitableListLocalRulestackCountriesResult(ListLocalRulestackCountriesResult):
    def __await__(self): ...

def list_local_rulestack_countries(
    local_rulestack_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    skip: Optional[_builtins.str] = ...,
    top: Optional[_builtins.int] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListLocalRulestackCountriesResult: ...
def list_local_rulestack_countries_output(
    local_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    skip: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    top: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListLocalRulestackCountriesResult]: ...
