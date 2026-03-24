

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApplicationDefinitionArgs', 'ApplicationDefinitionArgsDict', 'ApplicationTimeoutsArgs', 'ApplicationTimeoutsArgsDict', 'DeploymentTimeoutsArgs', 'DeploymentTimeoutsArgsDict', 'EnvironmentHighAvailabilityConfigArgs', 'EnvironmentHighAvailabilityConfigArgsDict', 'EnvironmentStorageConfigurationArgs', 'EnvironmentStorageConfigurationArgsDict', 'EnvironmentStorageConfigurationEfsArgs', 'EnvironmentStorageConfigurationEfsArgsDict', 'EnvironmentStorageConfigurationFsxArgs', 'EnvironmentStorageConfigurationFsxArgsDict', 'EnvironmentTimeoutsArgs', 'EnvironmentTimeoutsArgsDict']
class ApplicationDefinitionArgsDict(TypedDict):
    content: NotRequired[pulumi.Input[_builtins.str]]
    s3_location: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationDefinitionArgs:
    def __init__(__self__, *, content: Optional[pulumi.Input[_builtins.str]] = ..., s3_location: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Location")
    def s3_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_location.setter
    def s3_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DeploymentTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeploymentTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EnvironmentHighAvailabilityConfigArgsDict(TypedDict):
    desired_capacity: pulumi.Input[_builtins.int]


@pulumi.input_type
class EnvironmentHighAvailabilityConfigArgs:
    def __init__(__self__, *, desired_capacity: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @desired_capacity.setter
    def desired_capacity(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class EnvironmentStorageConfigurationArgsDict(TypedDict):
    efs: NotRequired[pulumi.Input[EnvironmentStorageConfigurationEfsArgsDict]]
    fsx: NotRequired[pulumi.Input[EnvironmentStorageConfigurationFsxArgsDict]]


@pulumi.input_type
class EnvironmentStorageConfigurationArgs:
    def __init__(__self__, *, efs: Optional[pulumi.Input[EnvironmentStorageConfigurationEfsArgs]] = ..., fsx: Optional[pulumi.Input[EnvironmentStorageConfigurationFsxArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def efs(self) -> Optional[pulumi.Input[EnvironmentStorageConfigurationEfsArgs]]:
        ...
    
    @efs.setter
    def efs(self, value: Optional[pulumi.Input[EnvironmentStorageConfigurationEfsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fsx(self) -> Optional[pulumi.Input[EnvironmentStorageConfigurationFsxArgs]]:
        ...
    
    @fsx.setter
    def fsx(self, value: Optional[pulumi.Input[EnvironmentStorageConfigurationFsxArgs]]): # -> None:
        ...
    


class EnvironmentStorageConfigurationEfsArgsDict(TypedDict):
    file_system_id: pulumi.Input[_builtins.str]
    mount_point: pulumi.Input[_builtins.str]


@pulumi.input_type
class EnvironmentStorageConfigurationEfsArgs:
    def __init__(__self__, *, file_system_id: pulumi.Input[_builtins.str], mount_point: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_system_id.setter
    def file_system_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPoint")
    def mount_point(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @mount_point.setter
    def mount_point(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EnvironmentStorageConfigurationFsxArgsDict(TypedDict):
    file_system_id: pulumi.Input[_builtins.str]
    mount_point: pulumi.Input[_builtins.str]


@pulumi.input_type
class EnvironmentStorageConfigurationFsxArgs:
    def __init__(__self__, *, file_system_id: pulumi.Input[_builtins.str], mount_point: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_system_id.setter
    def file_system_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPoint")
    def mount_point(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @mount_point.setter
    def mount_point(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EnvironmentTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


