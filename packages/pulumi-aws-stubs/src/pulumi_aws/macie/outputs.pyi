import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FindingsFilterFindingCriteria", "FindingsFilterFindingCriteriaCriterion"]

@pulumi.output_type
class FindingsFilterFindingCriteria(dict):
    def __init__(
        __self__,
        *,
        criterions: Optional[
            Sequence[outputs.FindingsFilterFindingCriteriaCriterion]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def criterions(
        self,
    ) -> Optional[Sequence[outputs.FindingsFilterFindingCriteriaCriterion]]: ...

@pulumi.output_type
class FindingsFilterFindingCriteriaCriterion(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        field: _builtins.str,
        eq_exact_matches: Optional[Sequence[_builtins.str]] = ...,
        eqs: Optional[Sequence[_builtins.str]] = ...,
        gt: Optional[_builtins.str] = ...,
        gte: Optional[_builtins.str] = ...,
        lt: Optional[_builtins.str] = ...,
        lte: Optional[_builtins.str] = ...,
        neqs: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eqExactMatches")
    def eq_exact_matches(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def eqs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def gt(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def lt(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def neqs(self) -> Optional[Sequence[_builtins.str]]: ...
