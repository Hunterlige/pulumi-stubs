import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetViewsResult", "AwaitableGetViewsResult", "get_views", "get_views_output"]

@pulumi.output_type
class GetViewsResult:
    def __init__(
        __self__, billing_view_types=..., billing_views=..., id=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingViewTypes")
    def billing_view_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="billingViews")
    def billing_views(self) -> Sequence[outputs.GetViewsBillingViewResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

class AwaitableGetViewsResult(GetViewsResult):
    def __await__(self): ...

def get_views(
    billing_view_types: Optional[Sequence[_builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetViewsResult: ...
def get_views_output(
    billing_view_types: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetViewsResult]: ...
