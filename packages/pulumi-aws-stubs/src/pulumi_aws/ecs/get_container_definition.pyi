import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetContainerDefinitionResult",
    "AwaitableGetContainerDefinitionResult",
    "get_container_definition",
    "get_container_definition_output",
]

@pulumi.output_type
class GetContainerDefinitionResult:
    def __init__(
        __self__,
        container_name=...,
        cpu=...,
        disable_networking=...,
        docker_labels=...,
        environment=...,
        id=...,
        image=...,
        image_digest=...,
        memory=...,
        memory_reservation=...,
        region=...,
        task_definition=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="disableNetworking")
    def disable_networking(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="dockerLabels")
    def docker_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageDigest")
    def image_digest(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memoryReservation")
    def memory_reservation(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="taskDefinition")
    def task_definition(self) -> _builtins.str: ...

class AwaitableGetContainerDefinitionResult(GetContainerDefinitionResult):
    def __await__(self): ...

def get_container_definition(
    container_name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    task_definition: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetContainerDefinitionResult: ...
def get_container_definition_output(
    container_name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    task_definition: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetContainerDefinitionResult]: ...
