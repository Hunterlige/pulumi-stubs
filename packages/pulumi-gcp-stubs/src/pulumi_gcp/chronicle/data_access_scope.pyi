

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
__all__ = ['DataAccessScopeArgs', 'DataAccessScope']
@pulumi.input_type
class DataAccessScopeArgs:
    def __init__(__self__, *, data_access_scope_id: pulumi.Input[_builtins.str], instance: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], allow_all: Optional[pulumi.Input[_builtins.bool]] = ..., allowed_data_access_labels: Optional[pulumi.Input[Sequence[pulumi.Input[DataAccessScopeAllowedDataAccessLabelArgs]]]] = ..., denied_data_access_labels: Optional[pulumi.Input[Sequence[pulumi.Input[DataAccessScopeDeniedDataAccessLabelArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccessScopeId")
    def data_access_scope_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_access_scope_id.setter
    def data_access_scope_id(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    @pulumi.getter(name="allowAll")
    def allow_all(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_all.setter
    def allow_all(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedDataAccessLabels")
    def allowed_data_access_labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataAccessScopeAllowedDataAccessLabelArgs]]]]:
        
        ...
    
    @allowed_data_access_labels.setter
    def allowed_data_access_labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataAccessScopeAllowedDataAccessLabelArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deniedDataAccessLabels")
    def denied_data_access_labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataAccessScopeDeniedDataAccessLabelArgs]]]]:
        
        ...
    
    @denied_data_access_labels.setter
    def denied_data_access_labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataAccessScopeDeniedDataAccessLabelArgs]]]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DataAccessScopeState:
    def __init__(__self__, *, allow_all: Optional[pulumi.Input[_builtins.bool]] = ..., allowed_data_access_labels: Optional[pulumi.Input[Sequence[pulumi.Input[DataAccessScopeAllowedDataAccessLabelArgs]]]] = ..., author: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_access_scope_id: Optional[pulumi.Input[_builtins.str]] = ..., denied_data_access_labels: Optional[pulumi.Input[Sequence[pulumi.Input[DataAccessScopeDeniedDataAccessLabelArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., last_editor: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAll")
    def allow_all(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_all.setter
    def allow_all(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedDataAccessLabels")
    def allowed_data_access_labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataAccessScopeAllowedDataAccessLabelArgs]]]]:
        
        ...
    
    @allowed_data_access_labels.setter
    def allowed_data_access_labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataAccessScopeAllowedDataAccessLabelArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def author(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @author.setter
    def author(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccessScopeId")
    def data_access_scope_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_access_scope_id.setter
    def data_access_scope_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deniedDataAccessLabels")
    def denied_data_access_labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataAccessScopeDeniedDataAccessLabelArgs]]]]:
        
        ...
    
    @denied_data_access_labels.setter
    def denied_data_access_labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataAccessScopeDeniedDataAccessLabelArgs]]]]): # -> None:
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
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastEditor")
    def last_editor(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_editor.setter
    def last_editor(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:chronicle/dataAccessScope:DataAccessScope")
class DataAccessScope(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allow_all: Optional[pulumi.Input[_builtins.bool]] = ..., allowed_data_access_labels: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataAccessScopeAllowedDataAccessLabelArgs, DataAccessScopeAllowedDataAccessLabelArgsDict]]]]] = ..., data_access_scope_id: Optional[pulumi.Input[_builtins.str]] = ..., denied_data_access_labels: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataAccessScopeDeniedDataAccessLabelArgs, DataAccessScopeDeniedDataAccessLabelArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DataAccessScopeArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., allow_all: Optional[pulumi.Input[_builtins.bool]] = ..., allowed_data_access_labels: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataAccessScopeAllowedDataAccessLabelArgs, DataAccessScopeAllowedDataAccessLabelArgsDict]]]]] = ..., author: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_access_scope_id: Optional[pulumi.Input[_builtins.str]] = ..., denied_data_access_labels: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataAccessScopeDeniedDataAccessLabelArgs, DataAccessScopeDeniedDataAccessLabelArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., last_editor: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> DataAccessScope:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAll")
    def allow_all(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedDataAccessLabels")
    def allowed_data_access_labels(self) -> pulumi.Output[Optional[Sequence[outputs.DataAccessScopeAllowedDataAccessLabel]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def author(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccessScopeId")
    def data_access_scope_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deniedDataAccessLabels")
    def denied_data_access_labels(self) -> pulumi.Output[Optional[Sequence[outputs.DataAccessScopeDeniedDataAccessLabel]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastEditor")
    def last_editor(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


