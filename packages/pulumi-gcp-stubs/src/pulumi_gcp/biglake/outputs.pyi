

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DatabaseHiveOptions', 'IcebergCatalogIamBindingCondition', 'IcebergCatalogIamMemberCondition', 'IcebergCatalogReplica', 'IcebergNamespaceIamBindingCondition', 'IcebergNamespaceIamMemberCondition', 'IcebergTableIamBindingCondition', 'IcebergTableIamMemberCondition', 'IcebergTablePartitionSpec', 'IcebergTablePartitionSpecField', 'IcebergTableSchema', 'IcebergTableSchemaField', 'TableHiveOptions', 'TableHiveOptionsStorageDescriptor']
@pulumi.output_type
class DatabaseHiveOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, location_uri: Optional[_builtins.str] = ..., parameters: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class IcebergCatalogIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class IcebergCatalogIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class IcebergCatalogReplica(dict):
    def __init__(__self__, *, region: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IcebergNamespaceIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class IcebergNamespaceIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class IcebergTableIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class IcebergTableIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class IcebergTablePartitionSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fields: Sequence[outputs.IcebergTablePartitionSpecField], spec_id: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> Sequence[outputs.IcebergTablePartitionSpecField]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="specId")
    def spec_id(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class IcebergTablePartitionSpecField(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, source_id: _builtins.int, transform: _builtins.str, field_id: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transform(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldId")
    def field_id(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class IcebergTableSchema(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fields: Sequence[outputs.IcebergTableSchemaField], identifier_field_ids: Optional[Sequence[_builtins.int]] = ..., schema_id: Optional[_builtins.int] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> Sequence[outputs.IcebergTableSchemaField]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identifierFieldIds")
    def identifier_field_ids(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaId")
    def schema_id(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IcebergTableSchemaField(dict):
    def __init__(__self__, *, id: _builtins.int, name: _builtins.str, required: _builtins.bool, type: _builtins.str, doc: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def required(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def doc(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TableHiveOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, parameters: Optional[Mapping[str, _builtins.str]] = ..., storage_descriptor: Optional[outputs.TableHiveOptionsStorageDescriptor] = ..., table_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageDescriptor")
    def storage_descriptor(self) -> Optional[outputs.TableHiveOptionsStorageDescriptor]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableType")
    def table_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TableHiveOptionsStorageDescriptor(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, input_format: Optional[_builtins.str] = ..., location_uri: Optional[_builtins.str] = ..., output_format: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[_builtins.str]:
        
        ...
    


