

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AnalyzerConfigurationArgs', 'AnalyzerConfigurationArgsDict', 'AnalyzerConfigurationInternalAccessArgs', 'AnalyzerConfigurationInternalAccessArgsDict', ..., ..., ..., ..., 'AnalyzerConfigurationUnusedAccessArgs', 'AnalyzerConfigurationUnusedAccessArgsDict', 'AnalyzerConfigurationUnusedAccessAnalysisRuleArgs', ..., ..., ..., 'ArchiveRuleFilterArgs', 'ArchiveRuleFilterArgsDict']
class AnalyzerConfigurationArgsDict(TypedDict):
    internal_access: NotRequired[pulumi.Input[AnalyzerConfigurationInternalAccessArgsDict]]
    unused_access: NotRequired[pulumi.Input[AnalyzerConfigurationUnusedAccessArgsDict]]


@pulumi.input_type
class AnalyzerConfigurationArgs:
    def __init__(__self__, *, internal_access: Optional[pulumi.Input[AnalyzerConfigurationInternalAccessArgs]] = ..., unused_access: Optional[pulumi.Input[AnalyzerConfigurationUnusedAccessArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalAccess")
    def internal_access(self) -> Optional[pulumi.Input[AnalyzerConfigurationInternalAccessArgs]]:
        
        ...
    
    @internal_access.setter
    def internal_access(self, value: Optional[pulumi.Input[AnalyzerConfigurationInternalAccessArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unusedAccess")
    def unused_access(self) -> Optional[pulumi.Input[AnalyzerConfigurationUnusedAccessArgs]]:
        
        ...
    
    @unused_access.setter
    def unused_access(self, value: Optional[pulumi.Input[AnalyzerConfigurationUnusedAccessArgs]]): # -> None:
        ...
    


class AnalyzerConfigurationInternalAccessArgsDict(TypedDict):
    analysis_rule: NotRequired[pulumi.Input[AnalyzerConfigurationInternalAccessAnalysisRuleArgsDict]]


@pulumi.input_type
class AnalyzerConfigurationInternalAccessArgs:
    def __init__(__self__, *, analysis_rule: Optional[pulumi.Input[AnalyzerConfigurationInternalAccessAnalysisRuleArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analysisRule")
    def analysis_rule(self) -> Optional[pulumi.Input[AnalyzerConfigurationInternalAccessAnalysisRuleArgs]]:
        
        ...
    
    @analysis_rule.setter
    def analysis_rule(self, value: Optional[pulumi.Input[AnalyzerConfigurationInternalAccessAnalysisRuleArgs]]): # -> None:
        ...
    


class AnalyzerConfigurationInternalAccessAnalysisRuleArgsDict(TypedDict):
    inclusions: NotRequired[pulumi.Input[Sequence[pulumi.Input[AnalyzerConfigurationInternalAccessAnalysisRuleInclusionArgsDict]]]]


@pulumi.input_type
class AnalyzerConfigurationInternalAccessAnalysisRuleArgs:
    def __init__(__self__, *, inclusions: Optional[pulumi.Input[Sequence[pulumi.Input[AnalyzerConfigurationInternalAccessAnalysisRuleInclusionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def inclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AnalyzerConfigurationInternalAccessAnalysisRuleInclusionArgs]]]]:
        
        ...
    
    @inclusions.setter
    def inclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AnalyzerConfigurationInternalAccessAnalysisRuleInclusionArgs]]]]): # -> None:
        ...
    


class AnalyzerConfigurationInternalAccessAnalysisRuleInclusionArgsDict(TypedDict):
    account_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AnalyzerConfigurationInternalAccessAnalysisRuleInclusionArgs:
    def __init__(__self__, *, account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., resource_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountIds")
    def account_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @account_ids.setter
    def account_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArns")
    def resource_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_arns.setter
    def resource_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_types.setter
    def resource_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AnalyzerConfigurationUnusedAccessArgsDict(TypedDict):
    analysis_rule: NotRequired[pulumi.Input[AnalyzerConfigurationUnusedAccessAnalysisRuleArgsDict]]
    unused_access_age: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class AnalyzerConfigurationUnusedAccessArgs:
    def __init__(__self__, *, analysis_rule: Optional[pulumi.Input[AnalyzerConfigurationUnusedAccessAnalysisRuleArgs]] = ..., unused_access_age: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analysisRule")
    def analysis_rule(self) -> Optional[pulumi.Input[AnalyzerConfigurationUnusedAccessAnalysisRuleArgs]]:
        
        ...
    
    @analysis_rule.setter
    def analysis_rule(self, value: Optional[pulumi.Input[AnalyzerConfigurationUnusedAccessAnalysisRuleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unusedAccessAge")
    def unused_access_age(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @unused_access_age.setter
    def unused_access_age(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class AnalyzerConfigurationUnusedAccessAnalysisRuleArgsDict(TypedDict):
    exclusions: NotRequired[pulumi.Input[Sequence[pulumi.Input[AnalyzerConfigurationUnusedAccessAnalysisRuleExclusionArgsDict]]]]


@pulumi.input_type
class AnalyzerConfigurationUnusedAccessAnalysisRuleArgs:
    def __init__(__self__, *, exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[AnalyzerConfigurationUnusedAccessAnalysisRuleExclusionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AnalyzerConfigurationUnusedAccessAnalysisRuleExclusionArgs]]]]:
        
        ...
    
    @exclusions.setter
    def exclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AnalyzerConfigurationUnusedAccessAnalysisRuleExclusionArgs]]]]): # -> None:
        ...
    


class AnalyzerConfigurationUnusedAccessAnalysisRuleExclusionArgsDict(TypedDict):
    account_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]


@pulumi.input_type
class AnalyzerConfigurationUnusedAccessAnalysisRuleExclusionArgs:
    def __init__(__self__, *, account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., resource_tags: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountIds")
    def account_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @account_ids.setter
    def account_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]:
        
        ...
    
    @resource_tags.setter
    def resource_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]): # -> None:
        ...
    


class ArchiveRuleFilterArgsDict(TypedDict):
    criteria: pulumi.Input[_builtins.str]
    contains: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    eqs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    exists: NotRequired[pulumi.Input[_builtins.str]]
    neqs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ArchiveRuleFilterArgs:
    def __init__(__self__, *, criteria: pulumi.Input[_builtins.str], contains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., eqs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., exists: Optional[pulumi.Input[_builtins.str]] = ..., neqs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def criteria(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @criteria.setter
    def criteria(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @contains.setter
    def contains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def eqs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @eqs.setter
    def eqs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exists(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exists.setter
    def exists(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def neqs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @neqs.setter
    def neqs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


