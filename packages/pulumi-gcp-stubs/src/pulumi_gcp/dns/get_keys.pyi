import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetKeysResult", "AwaitableGetKeysResult", "get_keys", "get_keys_output"]

@pulumi.output_type
class GetKeysResult:
    def __init__(
        __self__,
        id=...,
        key_signing_keys=...,
        managed_zone=...,
        project=...,
        zone_signing_keys=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keySigningKeys")
    def key_signing_keys(self) -> Sequence[outputs.GetKeysKeySigningKeyResult]: ...
    @_builtins.property
    @pulumi.getter(name="managedZone")
    def managed_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="zoneSigningKeys")
    def zone_signing_keys(self) -> Sequence[outputs.GetKeysZoneSigningKeyResult]: ...

class AwaitableGetKeysResult(GetKeysResult):
    def __await__(self): ...

def get_keys(
    managed_zone: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKeysResult: ...
def get_keys_output(
    managed_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKeysResult]: ...
