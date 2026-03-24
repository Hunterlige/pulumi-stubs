import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkerConfigurationResult",
    "AwaitableGetWorkerConfigurationResult",
    "get_worker_configuration",
    "get_worker_configuration_output",
]

@pulumi.output_type
class GetWorkerConfigurationResult:
    def __init__(
        __self__,
        arn=...,
        description=...,
        id=...,
        latest_revision=...,
        name=...,
        properties_file_content=...,
        region=...,
        tags=...,
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
    @pulumi.getter(name="latestRevision")
    def latest_revision(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="propertiesFileContent")
    def properties_file_content(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetWorkerConfigurationResult(GetWorkerConfigurationResult):
    def __await__(self): ...

def get_worker_configuration(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkerConfigurationResult: ...
def get_worker_configuration_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkerConfigurationResult]: ...
