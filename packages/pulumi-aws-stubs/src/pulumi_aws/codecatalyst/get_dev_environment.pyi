import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDevEnvironmentResult",
    "AwaitableGetDevEnvironmentResult",
    "get_dev_environment",
    "get_dev_environment_output",
]

@pulumi.output_type
class GetDevEnvironmentResult:
    def __init__(
        __self__,
        alias=...,
        creator_id=...,
        env_id=...,
        id=...,
        ides=...,
        inactivity_timeout_minutes=...,
        instance_type=...,
        last_updated_time=...,
        persistent_storages=...,
        project_name=...,
        region=...,
        repositories=...,
        space_name=...,
        status=...,
        status_reason=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creatorId")
    def creator_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="envId")
    def env_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ides(self) -> Sequence[outputs.GetDevEnvironmentIdeResult]: ...
    @_builtins.property
    @pulumi.getter(name="inactivityTimeoutMinutes")
    def inactivity_timeout_minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="persistentStorages")
    def persistent_storages(
        self,
    ) -> Sequence[outputs.GetDevEnvironmentPersistentStorageResult]: ...
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def repositories(
        self,
    ) -> Optional[Sequence[outputs.GetDevEnvironmentRepositoryResult]]: ...
    @_builtins.property
    @pulumi.getter(name="spaceName")
    def space_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetDevEnvironmentResult(GetDevEnvironmentResult):
    def __await__(self): ...

def get_dev_environment(
    alias: Optional[_builtins.str] = ...,
    creator_id: Optional[_builtins.str] = ...,
    env_id: Optional[_builtins.str] = ...,
    project_name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    repositories: Optional[
        Sequence[
            Union[GetDevEnvironmentRepositoryArgs, GetDevEnvironmentRepositoryArgsDict]
        ]
    ] = ...,
    space_name: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDevEnvironmentResult: ...
def get_dev_environment_output(
    alias: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    creator_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    env_id: Optional[pulumi.Input[_builtins.str]] = ...,
    project_name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    repositories: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetDevEnvironmentRepositoryArgs,
                        GetDevEnvironmentRepositoryArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    space_name: Optional[pulumi.Input[_builtins.str]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDevEnvironmentResult]: ...
