

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DevEnvironmentIdes', 'DevEnvironmentPersistentStorage', 'DevEnvironmentRepository', 'GetDevEnvironmentIdeResult', 'GetDevEnvironmentPersistentStorageResult', 'GetDevEnvironmentRepositoryResult']
@pulumi.output_type
class DevEnvironmentIdes(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., runtime: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DevEnvironmentPersistentStorage(dict):
    def __init__(__self__, *, size: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class DevEnvironmentRepository(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, repository_name: _builtins.str, branch_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetDevEnvironmentIdeResult(dict):
    def __init__(__self__, *, name: _builtins.str, runtime: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetDevEnvironmentPersistentStorageResult(dict):
    def __init__(__self__, *, size: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetDevEnvironmentRepositoryResult(dict):
    def __init__(__self__, *, branch_name: _builtins.str, repository_name: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> _builtins.str:
        ...
    


