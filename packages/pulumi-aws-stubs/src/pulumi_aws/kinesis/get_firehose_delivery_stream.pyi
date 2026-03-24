import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFirehoseDeliveryStreamResult",
    "AwaitableGetFirehoseDeliveryStreamResult",
    "get_firehose_delivery_stream",
    "get_firehose_delivery_stream_output",
]

@pulumi.output_type
class GetFirehoseDeliveryStreamResult:
    def __init__(__self__, arn=..., id=..., name=..., region=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetFirehoseDeliveryStreamResult(GetFirehoseDeliveryStreamResult):
    def __await__(self): ...

def get_firehose_delivery_stream(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFirehoseDeliveryStreamResult: ...
def get_firehose_delivery_stream_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFirehoseDeliveryStreamResult]: ...
