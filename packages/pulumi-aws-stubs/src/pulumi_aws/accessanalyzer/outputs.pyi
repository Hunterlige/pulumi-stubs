

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AnalyzerConfiguration', 'AnalyzerConfigurationInternalAccess', 'AnalyzerConfigurationInternalAccessAnalysisRule', ..., 'AnalyzerConfigurationUnusedAccess', 'AnalyzerConfigurationUnusedAccessAnalysisRule', ..., 'ArchiveRuleFilter']
@pulumi.output_type
class AnalyzerConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, internal_access: Optional[outputs.AnalyzerConfigurationInternalAccess] = ..., unused_access: Optional[outputs.AnalyzerConfigurationUnusedAccess] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalAccess")
    def internal_access(self) -> Optional[outputs.AnalyzerConfigurationInternalAccess]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unusedAccess")
    def unused_access(self) -> Optional[outputs.AnalyzerConfigurationUnusedAccess]:
        
        ...
    


@pulumi.output_type
class AnalyzerConfigurationInternalAccess(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, analysis_rule: Optional[outputs.AnalyzerConfigurationInternalAccessAnalysisRule] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analysisRule")
    def analysis_rule(self) -> Optional[outputs.AnalyzerConfigurationInternalAccessAnalysisRule]:
        
        ...
    


@pulumi.output_type
class AnalyzerConfigurationInternalAccessAnalysisRule(dict):
    def __init__(__self__, *, inclusions: Optional[Sequence[outputs.AnalyzerConfigurationInternalAccessAnalysisRuleInclusion]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def inclusions(self) -> Optional[Sequence[outputs.AnalyzerConfigurationInternalAccessAnalysisRuleInclusion]]:
        
        ...
    


@pulumi.output_type
class AnalyzerConfigurationInternalAccessAnalysisRuleInclusion(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_ids: Optional[Sequence[_builtins.str]] = ..., resource_arns: Optional[Sequence[_builtins.str]] = ..., resource_types: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountIds")
    def account_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArns")
    def resource_arns(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class AnalyzerConfigurationUnusedAccess(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, analysis_rule: Optional[outputs.AnalyzerConfigurationUnusedAccessAnalysisRule] = ..., unused_access_age: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analysisRule")
    def analysis_rule(self) -> Optional[outputs.AnalyzerConfigurationUnusedAccessAnalysisRule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unusedAccessAge")
    def unused_access_age(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AnalyzerConfigurationUnusedAccessAnalysisRule(dict):
    def __init__(__self__, *, exclusions: Optional[Sequence[outputs.AnalyzerConfigurationUnusedAccessAnalysisRuleExclusion]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> Optional[Sequence[outputs.AnalyzerConfigurationUnusedAccessAnalysisRuleExclusion]]:
        
        ...
    


@pulumi.output_type
class AnalyzerConfigurationUnusedAccessAnalysisRuleExclusion(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_ids: Optional[Sequence[_builtins.str]] = ..., resource_tags: Optional[Sequence[Mapping[str, _builtins.str]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountIds")
    def account_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Optional[Sequence[Mapping[str, _builtins.str]]]:
        
        ...
    


@pulumi.output_type
class ArchiveRuleFilter(dict):
    def __init__(__self__, *, criteria: _builtins.str, contains: Optional[Sequence[_builtins.str]] = ..., eqs: Optional[Sequence[_builtins.str]] = ..., exists: Optional[_builtins.str] = ..., neqs: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def criteria(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def eqs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exists(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def neqs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


