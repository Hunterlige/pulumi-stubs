import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetOpenIdConnectProviderResult",
    "AwaitableGetOpenIdConnectProviderResult",
    "get_open_id_connect_provider",
    "get_open_id_connect_provider_output",
]

@pulumi.output_type
class GetOpenIdConnectProviderResult:
    def __init__(
        __self__,
        arn=...,
        client_id_lists=...,
        id=...,
        tags=...,
        thumbprint_lists=...,
        url=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientIdLists")
    def client_id_lists(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="thumbprintLists")
    def thumbprint_lists(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...

class AwaitableGetOpenIdConnectProviderResult(GetOpenIdConnectProviderResult):
    def __await__(self): ...

def get_open_id_connect_provider(
    arn: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    url: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetOpenIdConnectProviderResult: ...
def get_open_id_connect_provider_output(
    arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    url: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOpenIdConnectProviderResult]: ...
