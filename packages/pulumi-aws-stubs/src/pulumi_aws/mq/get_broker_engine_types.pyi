import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBrokerEngineTypesResult",
    "AwaitableGetBrokerEngineTypesResult",
    "get_broker_engine_types",
    "get_broker_engine_types_output",
]

@pulumi.output_type
class GetBrokerEngineTypesResult:
    def __init__(
        __self__, broker_engine_types=..., engine_type=..., id=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="brokerEngineTypes")
    def broker_engine_types(
        self,
    ) -> Sequence[outputs.GetBrokerEngineTypesBrokerEngineTypeResult]: ...
    @_builtins.property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetBrokerEngineTypesResult(GetBrokerEngineTypesResult):
    def __await__(self): ...

def get_broker_engine_types(
    engine_type: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBrokerEngineTypesResult: ...
def get_broker_engine_types_output(
    engine_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBrokerEngineTypesResult]: ...
