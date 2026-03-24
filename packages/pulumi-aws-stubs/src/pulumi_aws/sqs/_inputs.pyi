import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from .. import iam

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PolicyDocumentArgs", "PolicyDocumentArgsDict"]

class PolicyDocumentArgsDict(TypedDict):
    statement: pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgsDict]]]
    version: pulumi.Input[iam.PolicyDocumentVersion]
    id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyDocumentArgs:
    def __init__(
        __self__,
        *,
        statement: pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgs]]],
        version: pulumi.Input[iam.PolicyDocumentVersion],
        id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="Statement")
    def statement(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgs]]]: ...
    @statement.setter
    def statement(
        self, value: pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="Version")
    def version(self) -> pulumi.Input[iam.PolicyDocumentVersion]: ...
    @version.setter
    def version(self, value: pulumi.Input[iam.PolicyDocumentVersion]): ...
    @_builtins.property
    @pulumi.getter(name="Id")
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
