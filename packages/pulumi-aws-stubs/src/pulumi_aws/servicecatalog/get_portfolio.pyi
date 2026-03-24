import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPortfolioResult",
    "AwaitableGetPortfolioResult",
    "get_portfolio",
    "get_portfolio_output",
]

@pulumi.output_type
class GetPortfolioResult:
    def __init__(
        __self__,
        accept_language=...,
        arn=...,
        created_time=...,
        description=...,
        id=...,
        name=...,
        provider_name=...,
        region=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetPortfolioResult(GetPortfolioResult):
    def __await__(self): ...

def get_portfolio(
    accept_language: Optional[_builtins.str] = ...,
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPortfolioResult: ...
def get_portfolio_output(
    accept_language: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPortfolioResult]: ...
