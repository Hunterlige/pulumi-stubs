

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEngineVersionResult', 'AwaitableGetEngineVersionResult', 'get_engine_version', 'get_engine_version_output']
@pulumi.output_type
class GetEngineVersionResult:
    
    def __init__(__self__, default_character_set=..., default_only=..., engine=..., engine_description=..., exportable_log_types=..., filters=..., has_major_target=..., has_minor_target=..., id=..., include_all=..., latest=..., parameter_group_family=..., preferred_major_targets=..., preferred_upgrade_targets=..., preferred_versions=..., region=..., status=..., supported_character_sets=..., supported_feature_names=..., supported_modes=..., supported_timezones=..., supports_certificate_rotation_without_restart=..., supports_global_databases=..., supports_integrations=..., supports_limitless_database=..., supports_local_write_forwarding=..., supports_log_exports_to_cloudwatch=..., supports_parallel_query=..., supports_read_replica=..., valid_major_targets=..., valid_minor_targets=..., valid_upgrade_targets=..., version=..., version_actual=..., version_description=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCharacterSet")
    def default_character_set(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultOnly")
    def default_only(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineDescription")
    def engine_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportableLogTypes")
    def exportable_log_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetEngineVersionFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasMajorTarget")
    def has_major_target(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasMinorTarget")
    def has_minor_target(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeAll")
    def include_all(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def latest(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterGroupFamily")
    def parameter_group_family(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredMajorTargets")
    def preferred_major_targets(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredUpgradeTargets")
    def preferred_upgrade_targets(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredVersions")
    def preferred_versions(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedCharacterSets")
    def supported_character_sets(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedFeatureNames")
    def supported_feature_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedModes")
    def supported_modes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedTimezones")
    def supported_timezones(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportsCertificateRotationWithoutRestart")
    def supports_certificate_rotation_without_restart(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportsGlobalDatabases")
    def supports_global_databases(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportsIntegrations")
    def supports_integrations(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportsLimitlessDatabase")
    def supports_limitless_database(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportsLocalWriteForwarding")
    def supports_local_write_forwarding(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportsLogExportsToCloudwatch")
    def supports_log_exports_to_cloudwatch(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportsParallelQuery")
    def supports_parallel_query(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportsReadReplica")
    def supports_read_replica(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validMajorTargets")
    def valid_major_targets(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validMinorTargets")
    def valid_minor_targets(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validUpgradeTargets")
    def valid_upgrade_targets(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionActual")
    def version_actual(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> _builtins.str:
        
        ...
    


class AwaitableGetEngineVersionResult(GetEngineVersionResult):
    def __await__(self): # -> Generator[Never, Any, GetEngineVersionResult]:
        ...
    


def get_engine_version(default_only: Optional[_builtins.bool] = ..., engine: Optional[_builtins.str] = ..., filters: Optional[Sequence[Union[GetEngineVersionFilterArgs, GetEngineVersionFilterArgsDict]]] = ..., has_major_target: Optional[_builtins.bool] = ..., has_minor_target: Optional[_builtins.bool] = ..., include_all: Optional[_builtins.bool] = ..., latest: Optional[_builtins.bool] = ..., parameter_group_family: Optional[_builtins.str] = ..., preferred_major_targets: Optional[Sequence[_builtins.str]] = ..., preferred_upgrade_targets: Optional[Sequence[_builtins.str]] = ..., preferred_versions: Optional[Sequence[_builtins.str]] = ..., region: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEngineVersionResult:
    
    ...

def get_engine_version_output(default_only: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., filters: Optional[pulumi.Input[Optional[Sequence[Union[GetEngineVersionFilterArgs, GetEngineVersionFilterArgsDict]]]]] = ..., has_major_target: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., has_minor_target: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., include_all: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., latest: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., parameter_group_family: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., preferred_major_targets: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., preferred_upgrade_targets: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., preferred_versions: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., version: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEngineVersionResult]:
    
    ...

