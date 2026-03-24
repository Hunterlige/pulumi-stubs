import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetEventCategoriesResult",
    "AwaitableGetEventCategoriesResult",
    "get_event_categories",
    "get_event_categories_output",
]

@pulumi.output_type
class GetEventCategoriesResult:
    def __init__(
        __self__, event_categories=..., id=..., region=..., source_type=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventCategories")
    def event_categories(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[_builtins.str]: ...

class AwaitableGetEventCategoriesResult(GetEventCategoriesResult):
    def __await__(self): ...

def get_event_categories(
    region: Optional[_builtins.str] = ...,
    source_type: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetEventCategoriesResult: ...
def get_event_categories_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    source_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetEventCategoriesResult]: ...
