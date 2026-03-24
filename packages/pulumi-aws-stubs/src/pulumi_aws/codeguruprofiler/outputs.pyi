

import builtins as _builtins
import sys
import pulumi
from typing import Any, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ProfilingGroupAgentOrchestrationConfig', 'GetProfilingGroupAgentOrchestrationConfigResult', 'GetProfilingGroupProfilingStatusResult', ...]
@pulumi.output_type
class ProfilingGroupAgentOrchestrationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, profiling_enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profilingEnabled")
    def profiling_enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetProfilingGroupAgentOrchestrationConfigResult(dict):
    def __init__(__self__, *, profiling_enabled: _builtins.bool) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="profilingEnabled")
    def profiling_enabled(self) -> _builtins.bool:
        ...
    


@pulumi.output_type
class GetProfilingGroupProfilingStatusResult(dict):
    def __init__(__self__, *, latest_agent_orchestrated_at: _builtins.str, latest_agent_profile_reported_at: _builtins.str, latest_aggregated_profiles: Sequence[outputs.GetProfilingGroupProfilingStatusLatestAggregatedProfileResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestAgentOrchestratedAt")
    def latest_agent_orchestrated_at(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestAgentProfileReportedAt")
    def latest_agent_profile_reported_at(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestAggregatedProfiles")
    def latest_aggregated_profiles(self) -> Sequence[outputs.GetProfilingGroupProfilingStatusLatestAggregatedProfileResult]:
        ...
    


@pulumi.output_type
class GetProfilingGroupProfilingStatusLatestAggregatedProfileResult(dict):
    def __init__(__self__, *, period: _builtins.str, start: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def period(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.str:
        ...
    


