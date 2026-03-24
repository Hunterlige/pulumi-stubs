import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetApiKeysResult",
    "AwaitableGetApiKeysResult",
    "get_api_keys",
    "get_api_keys_output",
]

@pulumi.output_type
class GetApiKeysResult:
    def __init__(
        __self__, customer_id=..., id=..., include_values=..., items=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includeValues")
    def include_values(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[outputs.GetApiKeysItemResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetApiKeysResult(GetApiKeysResult):
    def __await__(self): ...

def get_api_keys(
    customer_id: Optional[_builtins.str] = ...,
    include_values: Optional[_builtins.bool] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetApiKeysResult: ...
def get_api_keys_output(
    customer_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    include_values: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetApiKeysResult]: ...
