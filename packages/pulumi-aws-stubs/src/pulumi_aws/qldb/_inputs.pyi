import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["StreamKinesisConfigurationArgs", "StreamKinesisConfigurationArgsDict"]

class StreamKinesisConfigurationArgsDict(TypedDict):
    stream_arn: pulumi.Input[_builtins.str]
    aggregation_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class StreamKinesisConfigurationArgs:
    def __init__(
        __self__,
        *,
        stream_arn: pulumi.Input[_builtins.str],
        aggregation_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> pulumi.Input[_builtins.str]: ...
    @stream_arn.setter
    def stream_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="aggregationEnabled")
    def aggregation_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @aggregation_enabled.setter
    def aggregation_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
