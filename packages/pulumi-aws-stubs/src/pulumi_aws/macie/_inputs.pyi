import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FindingsFilterFindingCriteriaArgs",
    "FindingsFilterFindingCriteriaArgsDict",
    "FindingsFilterFindingCriteriaCriterionArgs",
    "FindingsFilterFindingCriteriaCriterionArgsDict",
]

class FindingsFilterFindingCriteriaArgsDict(TypedDict):
    criterions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FindingsFilterFindingCriteriaCriterionArgsDict]]
        ]
    ]

@pulumi.input_type
class FindingsFilterFindingCriteriaArgs:
    def __init__(
        __self__,
        *,
        criterions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FindingsFilterFindingCriteriaCriterionArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def criterions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FindingsFilterFindingCriteriaCriterionArgs]]]
    ]: ...
    @criterions.setter
    def criterions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FindingsFilterFindingCriteriaCriterionArgs]]
            ]
        ],
    ): ...

class FindingsFilterFindingCriteriaCriterionArgsDict(TypedDict):
    field: pulumi.Input[_builtins.str]
    eq_exact_matches: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    eqs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    gt: NotRequired[pulumi.Input[_builtins.str]]
    gte: NotRequired[pulumi.Input[_builtins.str]]
    lt: NotRequired[pulumi.Input[_builtins.str]]
    lte: NotRequired[pulumi.Input[_builtins.str]]
    neqs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class FindingsFilterFindingCriteriaCriterionArgs:
    def __init__(
        __self__,
        *,
        field: pulumi.Input[_builtins.str],
        eq_exact_matches: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        eqs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        gt: Optional[pulumi.Input[_builtins.str]] = ...,
        gte: Optional[pulumi.Input[_builtins.str]] = ...,
        lt: Optional[pulumi.Input[_builtins.str]] = ...,
        lte: Optional[pulumi.Input[_builtins.str]] = ...,
        neqs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> pulumi.Input[_builtins.str]: ...
    @field.setter
    def field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="eqExactMatches")
    def eq_exact_matches(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @eq_exact_matches.setter
    def eq_exact_matches(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def eqs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @eqs.setter
    def eqs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def gt(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gt.setter
    def gt(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gte.setter
    def gte(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lt(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lt.setter
    def lt(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lte.setter
    def lte(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def neqs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @neqs.setter
    def neqs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
