

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BackupScheduleDailyRecurrence', 'BackupScheduleWeeklyRecurrence', 'DatabaseCmekConfig', 'FieldIndexConfig', 'FieldIndexConfigIndex', 'FieldTtlConfig', 'IndexField', 'IndexFieldVectorConfig', 'IndexFieldVectorConfigFlat', 'UserCredsResourceIdentity']
@pulumi.output_type
class BackupScheduleDailyRecurrence(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class BackupScheduleWeeklyRecurrence(dict):
    def __init__(__self__, *, day: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseCmekConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: _builtins.str, active_key_versions: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeKeyVersions")
    def active_key_versions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class FieldIndexConfig(dict):
    def __init__(__self__, *, indexes: Optional[Sequence[outputs.FieldIndexConfigIndex]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def indexes(self) -> Optional[Sequence[outputs.FieldIndexConfigIndex]]:
        
        ...
    


@pulumi.output_type
class FieldIndexConfigIndex(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, array_config: Optional[_builtins.str] = ..., order: Optional[_builtins.str] = ..., query_scope: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arrayConfig")
    def array_config(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryScope")
    def query_scope(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FieldTtlConfig(dict):
    def __init__(__self__, *, state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IndexField(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, array_config: Optional[_builtins.str] = ..., field_path: Optional[_builtins.str] = ..., order: Optional[_builtins.str] = ..., vector_config: Optional[outputs.IndexFieldVectorConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arrayConfig")
    def array_config(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldPath")
    def field_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorConfig")
    def vector_config(self) -> Optional[outputs.IndexFieldVectorConfig]:
        
        ...
    


@pulumi.output_type
class IndexFieldVectorConfig(dict):
    def __init__(__self__, *, dimension: Optional[_builtins.int] = ..., flat: Optional[outputs.IndexFieldVectorConfigFlat] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def flat(self) -> Optional[outputs.IndexFieldVectorConfigFlat]:
        
        ...
    


@pulumi.output_type
class IndexFieldVectorConfigFlat(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class UserCredsResourceIdentity(dict):
    def __init__(__self__, *, principal: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[_builtins.str]:
        
        ...
    


