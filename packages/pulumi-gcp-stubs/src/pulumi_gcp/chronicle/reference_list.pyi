

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
__all__ = ['ReferenceListArgs', 'ReferenceList']
@pulumi.input_type
class ReferenceListArgs:
    def __init__(__self__, *, description: pulumi.Input[_builtins.str], entries: pulumi.Input[Sequence[pulumi.Input[ReferenceListEntryArgs]]], instance: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], reference_list_id: pulumi.Input[_builtins.str], syntax_type: pulumi.Input[_builtins.str], project: Optional[pulumi.Input[_builtins.str]] = ..., scope_infos: Optional[pulumi.Input[Sequence[pulumi.Input[ReferenceListScopeInfoArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def entries(self) -> pulumi.Input[Sequence[pulumi.Input[ReferenceListEntryArgs]]]:
        
        ...
    
    @entries.setter
    def entries(self, value: pulumi.Input[Sequence[pulumi.Input[ReferenceListEntryArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance.setter
    def instance(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="referenceListId")
    def reference_list_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @reference_list_id.setter
    def reference_list_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syntaxType")
    def syntax_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @syntax_type.setter
    def syntax_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeInfos")
    def scope_infos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReferenceListScopeInfoArgs]]]]:
        
        ...
    
    @scope_infos.setter
    def scope_infos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ReferenceListScopeInfoArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ReferenceListState:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., entries: Optional[pulumi.Input[Sequence[pulumi.Input[ReferenceListEntryArgs]]]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., reference_list_id: Optional[pulumi.Input[_builtins.str]] = ..., revision_create_time: Optional[pulumi.Input[_builtins.str]] = ..., rule_associations_count: Optional[pulumi.Input[_builtins.int]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., scope_infos: Optional[pulumi.Input[Sequence[pulumi.Input[ReferenceListScopeInfoArgs]]]] = ..., syntax_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReferenceListEntryArgs]]]]:
        
        ...
    
    @entries.setter
    def entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ReferenceListEntryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="referenceListId")
    def reference_list_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @reference_list_id.setter
    def reference_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionCreateTime")
    def revision_create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @revision_create_time.setter
    def revision_create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAssociationsCount")
    def rule_associations_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @rule_associations_count.setter
    def rule_associations_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeInfos")
    def scope_infos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReferenceListScopeInfoArgs]]]]:
        
        ...
    
    @scope_infos.setter
    def scope_infos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ReferenceListScopeInfoArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syntaxType")
    def syntax_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @syntax_type.setter
    def syntax_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:chronicle/referenceList:ReferenceList")
class ReferenceList(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., entries: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ReferenceListEntryArgs, ReferenceListEntryArgsDict]]]]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., reference_list_id: Optional[pulumi.Input[_builtins.str]] = ..., scope_infos: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ReferenceListScopeInfoArgs, ReferenceListScopeInfoArgsDict]]]]] = ..., syntax_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ReferenceListArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., entries: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ReferenceListEntryArgs, ReferenceListEntryArgsDict]]]]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., reference_list_id: Optional[pulumi.Input[_builtins.str]] = ..., revision_create_time: Optional[pulumi.Input[_builtins.str]] = ..., rule_associations_count: Optional[pulumi.Input[_builtins.int]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., scope_infos: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ReferenceListScopeInfoArgs, ReferenceListScopeInfoArgsDict]]]]] = ..., syntax_type: Optional[pulumi.Input[_builtins.str]] = ...) -> ReferenceList:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def entries(self) -> pulumi.Output[Sequence[outputs.ReferenceListEntry]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="referenceListId")
    def reference_list_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionCreateTime")
    def revision_create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAssociationsCount")
    def rule_associations_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeInfos")
    def scope_infos(self) -> pulumi.Output[Optional[Sequence[outputs.ReferenceListScopeInfo]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syntaxType")
    def syntax_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


