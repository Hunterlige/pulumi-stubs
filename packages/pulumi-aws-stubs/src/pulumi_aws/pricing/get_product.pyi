import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetProductResult",
    "AwaitableGetProductResult",
    "get_product",
    "get_product_output",
]

@pulumi.output_type
class GetProductResult:
    def __init__(
        __self__, filters=..., id=..., result=..., service_code=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Sequence[outputs.GetProductFilterResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def result(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceCode")
    def service_code(self) -> _builtins.str: ...

class AwaitableGetProductResult(GetProductResult):
    def __await__(self): ...

def get_product(
    filters: Optional[
        Sequence[Union[GetProductFilterArgs, GetProductFilterArgsDict]]
    ] = ...,
    service_code: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetProductResult: ...
def get_product_output(
    filters: Optional[
        pulumi.Input[Sequence[Union[GetProductFilterArgs, GetProductFilterArgsDict]]]
    ] = ...,
    service_code: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetProductResult]: ...
