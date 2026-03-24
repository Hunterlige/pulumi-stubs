

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
__all__ = ['FolderSinkArgs', 'FolderSink']
@pulumi.input_type
class FolderSinkArgs:
    def __init__(__self__, *, destination: pulumi.Input[_builtins.str], folder: pulumi.Input[_builtins.str], bigquery_options: Optional[pulumi.Input[FolderSinkBigqueryOptionsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[FolderSinkExclusionArgs]]]] = ..., filter: Optional[pulumi.Input[_builtins.str]] = ..., include_children: Optional[pulumi.Input[_builtins.bool]] = ..., intercept_children: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @folder.setter
    def folder(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(self) -> Optional[pulumi.Input[FolderSinkBigqueryOptionsArgs]]:
        
        ...
    
    @bigquery_options.setter
    def bigquery_options(self, value: Optional[pulumi.Input[FolderSinkBigqueryOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FolderSinkExclusionArgs]]]]:
        
        ...
    
    @exclusions.setter
    def exclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FolderSinkExclusionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeChildren")
    def include_children(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_children.setter
    def include_children(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interceptChildren")
    def intercept_children(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @intercept_children.setter
    def intercept_children(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _FolderSinkState:
    def __init__(__self__, *, bigquery_options: Optional[pulumi.Input[FolderSinkBigqueryOptionsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[FolderSinkExclusionArgs]]]] = ..., filter: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., include_children: Optional[pulumi.Input[_builtins.bool]] = ..., intercept_children: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., writer_identity: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(self) -> Optional[pulumi.Input[FolderSinkBigqueryOptionsArgs]]:
        
        ...
    
    @bigquery_options.setter
    def bigquery_options(self, value: Optional[pulumi.Input[FolderSinkBigqueryOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FolderSinkExclusionArgs]]]]:
        
        ...
    
    @exclusions.setter
    def exclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FolderSinkExclusionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @folder.setter
    def folder(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeChildren")
    def include_children(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_children.setter
    def include_children(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interceptChildren")
    def intercept_children(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @intercept_children.setter
    def intercept_children(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writerIdentity")
    def writer_identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @writer_identity.setter
    def writer_identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:logging/folderSink:FolderSink")
class FolderSink(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bigquery_options: Optional[pulumi.Input[Union[FolderSinkBigqueryOptionsArgs, FolderSinkBigqueryOptionsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FolderSinkExclusionArgs, FolderSinkExclusionArgsDict]]]]] = ..., filter: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., include_children: Optional[pulumi.Input[_builtins.bool]] = ..., intercept_children: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FolderSinkArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bigquery_options: Optional[pulumi.Input[Union[FolderSinkBigqueryOptionsArgs, FolderSinkBigqueryOptionsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FolderSinkExclusionArgs, FolderSinkExclusionArgsDict]]]]] = ..., filter: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., include_children: Optional[pulumi.Input[_builtins.bool]] = ..., intercept_children: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., writer_identity: Optional[pulumi.Input[_builtins.str]] = ...) -> FolderSink:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(self) -> pulumi.Output[outputs.FolderSinkBigqueryOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> pulumi.Output[Optional[Sequence[outputs.FolderSinkExclusion]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeChildren")
    def include_children(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interceptChildren")
    def intercept_children(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="writerIdentity")
    def writer_identity(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


