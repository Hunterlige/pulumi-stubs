import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSecretResult",
    "AwaitableGetSecretResult",
    "get_secret",
    "get_secret_output",
]

@pulumi.output_type
class GetSecretResult:
    def __init__(
        __self__,
        annotations=...,
        create_time=...,
        deletion_protection=...,
        effective_annotations=...,
        effective_labels=...,
        expire_time=...,
        id=...,
        labels=...,
        name=...,
        project=...,
        pulumi_labels=...,
        replications=...,
        rotations=...,
        secret_id=...,
        tags=...,
        topics=...,
        ttl=...,
        version_aliases=...,
        version_destroy_ttl=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> _builtins.str: ...
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
    def replications(self) -> Sequence[outputs.GetSecretReplicationResult]: ...
    @_builtins.property
    @pulumi.getter
    def rotations(self) -> Sequence[outputs.GetSecretRotationResult]: ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def topics(self) -> Sequence[outputs.GetSecretTopicResult]: ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="versionAliases")
    def version_aliases(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="versionDestroyTtl")
    def version_destroy_ttl(self) -> _builtins.str: ...

class AwaitableGetSecretResult(GetSecretResult):
    def __await__(self): ...

def get_secret(
    project: Optional[_builtins.str] = ...,
    secret_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecretResult: ...
def get_secret_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    secret_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecretResult]: ...
