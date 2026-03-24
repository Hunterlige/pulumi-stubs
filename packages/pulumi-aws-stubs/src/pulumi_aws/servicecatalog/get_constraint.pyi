import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConstraintResult",
    "AwaitableGetConstraintResult",
    "get_constraint",
    "get_constraint_output",
]

@pulumi.output_type
class GetConstraintResult:
    def __init__(
        __self__,
        accept_language=...,
        description=...,
        id=...,
        owner=...,
        parameters=...,
        portfolio_id=...,
        product_id=...,
        region=...,
        status=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetConstraintResult(GetConstraintResult):
    def __await__(self): ...

def get_constraint(
    accept_language: Optional[_builtins.str] = ...,
    description: Optional[_builtins.str] = ...,
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConstraintResult: ...
def get_constraint_output(
    accept_language: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    description: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConstraintResult]: ...
