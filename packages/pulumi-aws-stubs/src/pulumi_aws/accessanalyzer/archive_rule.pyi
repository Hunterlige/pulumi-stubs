

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ArchiveRuleArgs', 'ArchiveRule']
@pulumi.input_type
class ArchiveRuleArgs:
    def __init__(__self__, *, analyzer_name: pulumi.Input[_builtins.str], filters: pulumi.Input[Sequence[pulumi.Input[ArchiveRuleFilterArgs]]], rule_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyzerName")
    def analyzer_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @analyzer_name.setter
    def analyzer_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> pulumi.Input[Sequence[pulumi.Input[ArchiveRuleFilterArgs]]]:
        
        ...
    
    @filters.setter
    def filters(self, value: pulumi.Input[Sequence[pulumi.Input[ArchiveRuleFilterArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_name.setter
    def rule_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ArchiveRuleState:
    def __init__(__self__, *, analyzer_name: Optional[pulumi.Input[_builtins.str]] = ..., filters: Optional[pulumi.Input[Sequence[pulumi.Input[ArchiveRuleFilterArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyzerName")
    def analyzer_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @analyzer_name.setter
    def analyzer_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ArchiveRuleFilterArgs]]]]:
        
        ...
    
    @filters.setter
    def filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ArchiveRuleFilterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:accessanalyzer/archiveRule:ArchiveRule")
class ArchiveRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., analyzer_name: Optional[pulumi.Input[_builtins.str]] = ..., filters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ArchiveRuleFilterArgs, ArchiveRuleFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ArchiveRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., analyzer_name: Optional[pulumi.Input[_builtins.str]] = ..., filters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ArchiveRuleFilterArgs, ArchiveRuleFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ...) -> ArchiveRule:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analyzerName")
    def analyzer_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> pulumi.Output[Sequence[outputs.ArchiveRuleFilter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


