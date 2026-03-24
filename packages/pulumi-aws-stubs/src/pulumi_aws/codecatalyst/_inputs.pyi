

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DevEnvironmentIdesArgs', 'DevEnvironmentIdesArgsDict', 'DevEnvironmentPersistentStorageArgs', 'DevEnvironmentPersistentStorageArgsDict', 'DevEnvironmentRepositoryArgs', 'DevEnvironmentRepositoryArgsDict', 'GetDevEnvironmentRepositoryArgs', 'GetDevEnvironmentRepositoryArgsDict']
class DevEnvironmentIdesArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    runtime: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DevEnvironmentIdesArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., runtime: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def runtime(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime.setter
    def runtime(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DevEnvironmentPersistentStorageArgsDict(TypedDict):
    size: pulumi.Input[_builtins.int]


@pulumi.input_type
class DevEnvironmentPersistentStorageArgs:
    def __init__(__self__, *, size: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @size.setter
    def size(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class DevEnvironmentRepositoryArgsDict(TypedDict):
    repository_name: pulumi.Input[_builtins.str]
    branch_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DevEnvironmentRepositoryArgs:
    def __init__(__self__, *, repository_name: pulumi.Input[_builtins.str], branch_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_name.setter
    def repository_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @branch_name.setter
    def branch_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GetDevEnvironmentRepositoryArgsDict(TypedDict):
    branch_name: _builtins.str
    repository_name: _builtins.str


@pulumi.input_type
class GetDevEnvironmentRepositoryArgs:
    def __init__(__self__, *, branch_name: _builtins.str, repository_name: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> _builtins.str:
        ...
    
    @branch_name.setter
    def branch_name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> _builtins.str:
        ...
    
    @repository_name.setter
    def repository_name(self, value: _builtins.str): # -> None:
        ...
    


