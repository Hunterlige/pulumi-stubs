import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAttachedInstallManifestResult",
    "AwaitableGetAttachedInstallManifestResult",
    "get_attached_install_manifest",
    "get_attached_install_manifest_output",
]

@pulumi.output_type
class GetAttachedInstallManifestResult:
    def __init__(
        __self__,
        cluster_id=...,
        id=...,
        location=...,
        manifest=...,
        platform_version=...,
        project=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def manifest(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...

class AwaitableGetAttachedInstallManifestResult(GetAttachedInstallManifestResult):
    def __await__(self): ...

def get_attached_install_manifest(
    cluster_id: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    platform_version: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAttachedInstallManifestResult: ...
def get_attached_install_manifest_output(
    cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    platform_version: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAttachedInstallManifestResult]: ...
