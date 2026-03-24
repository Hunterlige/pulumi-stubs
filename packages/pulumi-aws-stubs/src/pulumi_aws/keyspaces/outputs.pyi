

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['KeyspaceReplicationSpecification', 'TableCapacitySpecification', 'TableClientSideTimestamps', 'TableComment', 'TableEncryptionSpecification', 'TablePointInTimeRecovery', 'TableSchemaDefinition', 'TableSchemaDefinitionClusteringKey', 'TableSchemaDefinitionColumn', 'TableSchemaDefinitionPartitionKey', 'TableSchemaDefinitionStaticColumn', 'TableTtl']
@pulumi.output_type
class KeyspaceReplicationSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, region_lists: Optional[Sequence[_builtins.str]] = ..., replication_strategy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionLists")
    def region_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationStrategy")
    def replication_strategy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TableCapacitySpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, read_capacity_units: Optional[_builtins.int] = ..., throughput_mode: Optional[_builtins.str] = ..., write_capacity_units: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readCapacityUnits")
    def read_capacity_units(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputMode")
    def throughput_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeCapacityUnits")
    def write_capacity_units(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class TableClientSideTimestamps(dict):
    def __init__(__self__, *, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TableComment(dict):
    def __init__(__self__, *, message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TableEncryptionSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_identifier: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TablePointInTimeRecovery(dict):
    def __init__(__self__, *, status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TableSchemaDefinition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, columns: Sequence[outputs.TableSchemaDefinitionColumn], partition_keys: Sequence[outputs.TableSchemaDefinitionPartitionKey], clustering_keys: Optional[Sequence[outputs.TableSchemaDefinitionClusteringKey]] = ..., static_columns: Optional[Sequence[outputs.TableSchemaDefinitionStaticColumn]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Sequence[outputs.TableSchemaDefinitionColumn]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKeys")
    def partition_keys(self) -> Sequence[outputs.TableSchemaDefinitionPartitionKey]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusteringKeys")
    def clustering_keys(self) -> Optional[Sequence[outputs.TableSchemaDefinitionClusteringKey]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticColumns")
    def static_columns(self) -> Optional[Sequence[outputs.TableSchemaDefinitionStaticColumn]]:
        
        ...
    


@pulumi.output_type
class TableSchemaDefinitionClusteringKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, order_by: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orderBy")
    def order_by(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TableSchemaDefinitionColumn(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TableSchemaDefinitionPartitionKey(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TableSchemaDefinitionStaticColumn(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TableTtl(dict):
    def __init__(__self__, *, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


