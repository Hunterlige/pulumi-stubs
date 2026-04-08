import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListGlobalRulestackPredefinedUrlCategoriesResult",
    ...,
    "list_global_rulestack_predefined_url_categories",
    ...,
]

@pulumi.output_type
class ListGlobalRulestackPredefinedUrlCategoriesResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.PredefinedUrlCategoryResponse]: ...

class AwaitableListGlobalRulestackPredefinedUrlCategoriesResult(
    ListGlobalRulestackPredefinedUrlCategoriesResult
):
    def __await__(self): ...

def list_global_rulestack_predefined_url_categories(
    global_rulestack_name: Optional[_builtins.str] = ...,
    skip: Optional[_builtins.str] = ...,
    top: Optional[_builtins.int] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListGlobalRulestackPredefinedUrlCategoriesResult: ...
def list_global_rulestack_predefined_url_categories_output(
    global_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ...,
    skip: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    top: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListGlobalRulestackPredefinedUrlCategoriesResult]: ...
