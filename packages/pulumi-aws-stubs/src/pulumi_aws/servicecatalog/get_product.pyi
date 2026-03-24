import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

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
        __self__,
        accept_language=...,
        arn=...,
        created_time=...,
        description=...,
        distributor=...,
        has_default_path=...,
        id=...,
        name=...,
        owner=...,
        region=...,
        status=...,
        support_description=...,
        support_email=...,
        support_url=...,
        tags=...,
        type=...,
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
    def distributor(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hasDefaultPath")
    def has_default_path(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportDescription")
    def support_description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportEmail")
    def support_email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportUrl")
    def support_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetProductResult(GetProductResult):
    def __await__(self): ...

def get_product(
    accept_language: Optional[_builtins.str] = ...,
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetProductResult: ...
def get_product_output(
    accept_language: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetProductResult]: ...
