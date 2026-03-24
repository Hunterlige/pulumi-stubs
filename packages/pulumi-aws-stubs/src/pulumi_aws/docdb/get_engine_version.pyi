import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetEngineVersionResult",
    "AwaitableGetEngineVersionResult",
    "get_engine_version",
    "get_engine_version_output",
]

@pulumi.output_type
class GetEngineVersionResult:
    def __init__(
        __self__,
        engine=...,
        engine_description=...,
        exportable_log_types=...,
        id=...,
        parameter_group_family=...,
        preferred_versions=...,
        region=...,
        supports_log_exports_to_cloudwatch=...,
        valid_upgrade_targets=...,
        version=...,
        version_description=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineDescription")
    def engine_description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exportableLogTypes")
    def exportable_log_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterGroupFamily")
    def parameter_group_family(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="preferredVersions")
    def preferred_versions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportsLogExportsToCloudwatch")
    def supports_log_exports_to_cloudwatch(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="validUpgradeTargets")
    def valid_upgrade_targets(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> _builtins.str: ...

class AwaitableGetEngineVersionResult(GetEngineVersionResult):
    def __await__(self): ...

def get_engine_version(
    engine: Optional[_builtins.str] = ...,
    parameter_group_family: Optional[_builtins.str] = ...,
    preferred_versions: Optional[Sequence[_builtins.str]] = ...,
    region: Optional[_builtins.str] = ...,
    version: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetEngineVersionResult: ...
def get_engine_version_output(
    engine: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    parameter_group_family: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    preferred_versions: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetEngineVersionResult]: ...
