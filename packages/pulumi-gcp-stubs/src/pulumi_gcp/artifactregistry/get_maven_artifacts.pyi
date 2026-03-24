import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMavenArtifactsResult",
    "AwaitableGetMavenArtifactsResult",
    "get_maven_artifacts",
    "get_maven_artifacts_output",
]

@pulumi.output_type
class GetMavenArtifactsResult:
    def __init__(
        __self__,
        id=...,
        location=...,
        maven_artifacts=...,
        project=...,
        repository_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mavenArtifacts")
    def maven_artifacts(
        self,
    ) -> Sequence[outputs.GetMavenArtifactsMavenArtifactResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> _builtins.str: ...

class AwaitableGetMavenArtifactsResult(GetMavenArtifactsResult):
    def __await__(self): ...

def get_maven_artifacts(
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    repository_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMavenArtifactsResult: ...
def get_maven_artifacts_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    repository_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMavenArtifactsResult]: ...
