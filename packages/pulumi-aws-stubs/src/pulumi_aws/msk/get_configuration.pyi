import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConfigurationResult",
    "AwaitableGetConfigurationResult",
    "get_configuration",
    "get_configuration_output",
]

@pulumi.output_type
class GetConfigurationResult:
    def __init__(
        __self__,
        arn=...,
        description=...,
        id=...,
        kafka_versions=...,
        latest_revision=...,
        name=...,
        region=...,
        server_properties=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kafkaVersions")
    def kafka_versions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="latestRevision")
    def latest_revision(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serverProperties")
    def server_properties(self) -> _builtins.str: ...

class AwaitableGetConfigurationResult(GetConfigurationResult):
    def __await__(self): ...

def get_configuration(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConfigurationResult: ...
def get_configuration_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConfigurationResult]: ...
