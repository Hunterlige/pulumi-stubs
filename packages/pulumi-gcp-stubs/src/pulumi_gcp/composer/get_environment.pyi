import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetEnvironmentResult",
    "AwaitableGetEnvironmentResult",
    "get_environment",
    "get_environment_output",
]

@pulumi.output_type
class GetEnvironmentResult:
    def __init__(
        __self__,
        configs=...,
        effective_labels=...,
        id=...,
        labels=...,
        name=...,
        project=...,
        pulumi_labels=...,
        region=...,
        storage_configs=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configs(self) -> Sequence[outputs.GetEnvironmentConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageConfigs")
    def storage_configs(
        self,
    ) -> Sequence[outputs.GetEnvironmentStorageConfigResult]: ...

class AwaitableGetEnvironmentResult(GetEnvironmentResult):
    def __await__(self): ...

def get_environment(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetEnvironmentResult: ...
def get_environment_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetEnvironmentResult]: ...
