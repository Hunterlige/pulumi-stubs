import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetProducerDataSharesResult",
    "AwaitableGetProducerDataSharesResult",
    "get_producer_data_shares",
    "get_producer_data_shares_output",
]

@pulumi.output_type
class GetProducerDataSharesResult:
    def __init__(
        __self__, data_shares=..., id=..., producer_arn=..., region=..., status=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataShares")
    def data_shares(self) -> Sequence[outputs.GetProducerDataSharesDataShareResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="producerArn")
    def producer_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

class AwaitableGetProducerDataSharesResult(GetProducerDataSharesResult):
    def __await__(self): ...

def get_producer_data_shares(
    producer_arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    status: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetProducerDataSharesResult: ...
def get_producer_data_shares_output(
    producer_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    status: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetProducerDataSharesResult]: ...
