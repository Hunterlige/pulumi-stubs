import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetKafkaVersionResult",
    "AwaitableGetKafkaVersionResult",
    "get_kafka_version",
    "get_kafka_version_output",
]

@pulumi.output_type
class GetKafkaVersionResult:
    def __init__(
        __self__, id=..., preferred_versions=..., region=..., status=..., version=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="preferredVersions")
    def preferred_versions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

class AwaitableGetKafkaVersionResult(GetKafkaVersionResult):
    def __await__(self): ...

def get_kafka_version(
    preferred_versions: Optional[Sequence[_builtins.str]] = ...,
    region: Optional[_builtins.str] = ...,
    version: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKafkaVersionResult: ...
def get_kafka_version_output(
    preferred_versions: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKafkaVersionResult]: ...
