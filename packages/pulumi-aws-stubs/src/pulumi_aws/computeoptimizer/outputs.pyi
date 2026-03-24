

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EnrollmentStatusTimeouts', 'RecommendationPreferencesExternalMetricsPreference', 'RecommendationPreferencesPreferredResource', 'RecommendationPreferencesScope', 'RecommendationPreferencesUtilizationPreference', ...]
@pulumi.output_type
class EnrollmentStatusTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RecommendationPreferencesExternalMetricsPreference(dict):
    def __init__(__self__, *, source: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RecommendationPreferencesPreferredResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, exclude_lists: Optional[Sequence[_builtins.str]] = ..., include_lists: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeLists")
    def exclude_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeLists")
    def include_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RecommendationPreferencesScope(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RecommendationPreferencesUtilizationPreference(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metric_name: _builtins.str, metric_parameters: outputs.RecommendationPreferencesUtilizationPreferenceMetricParameters) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricParameters")
    def metric_parameters(self) -> outputs.RecommendationPreferencesUtilizationPreferenceMetricParameters:
        
        ...
    


@pulumi.output_type
class RecommendationPreferencesUtilizationPreferenceMetricParameters(dict):
    def __init__(__self__, *, headroom: _builtins.str, threshold: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headroom(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[_builtins.str]:
        
        ...
    


