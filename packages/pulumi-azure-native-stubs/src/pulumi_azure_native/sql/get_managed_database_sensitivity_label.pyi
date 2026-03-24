

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetManagedDatabaseSensitivityLabelResult', 'AwaitableGetManagedDatabaseSensitivityLabelResult', 'get_managed_database_sensitivity_label', 'get_managed_database_sensitivity_label_output']
@pulumi.output_type
class GetManagedDatabaseSensitivityLabelResult:
    
    def __init__(__self__, azure_api_version=..., client_classification_source=..., column_name=..., id=..., information_type=..., information_type_id=..., is_disabled=..., label_id=..., label_name=..., managed_by=..., name=..., rank=..., schema_name=..., table_name=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientClassificationSource")
    def client_classification_source(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="informationType")
    def information_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="informationTypeId")
    def information_type_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelId")
    def label_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelName")
    def label_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rank(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetManagedDatabaseSensitivityLabelResult(GetManagedDatabaseSensitivityLabelResult):
    def __await__(self): # -> Generator[Never, Any, GetManagedDatabaseSensitivityLabelResult]:
        ...
    


def get_managed_database_sensitivity_label(column_name: Optional[_builtins.str] = ..., database_name: Optional[_builtins.str] = ..., managed_instance_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., schema_name: Optional[_builtins.str] = ..., sensitivity_label_source: Optional[_builtins.str] = ..., table_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetManagedDatabaseSensitivityLabelResult:
    
    ...

def get_managed_database_sensitivity_label_output(column_name: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., schema_name: Optional[pulumi.Input[_builtins.str]] = ..., sensitivity_label_source: Optional[pulumi.Input[_builtins.str]] = ..., table_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetManagedDatabaseSensitivityLabelResult]:
    
    ...

