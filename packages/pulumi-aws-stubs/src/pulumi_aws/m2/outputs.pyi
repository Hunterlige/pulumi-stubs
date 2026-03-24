import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApplicationDefinition",
    "ApplicationTimeouts",
    "DeploymentTimeouts",
    "EnvironmentHighAvailabilityConfig",
    "EnvironmentStorageConfiguration",
    "EnvironmentStorageConfigurationEfs",
    "EnvironmentStorageConfigurationFsx",
    "EnvironmentTimeouts",
]

@pulumi.output_type
class ApplicationDefinition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        content: Optional[_builtins.str] = ...,
        s3_location: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3Location")
    def s3_location(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeploymentTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnvironmentHighAvailabilityConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, desired_capacity: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> _builtins.int: ...

@pulumi.output_type
class EnvironmentStorageConfiguration(dict):
    def __init__(
        __self__,
        *,
        efs: Optional[outputs.EnvironmentStorageConfigurationEfs] = ...,
        fsx: Optional[outputs.EnvironmentStorageConfigurationFsx] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def efs(self) -> Optional[outputs.EnvironmentStorageConfigurationEfs]: ...
    @_builtins.property
    @pulumi.getter
    def fsx(self) -> Optional[outputs.EnvironmentStorageConfigurationFsx]: ...

@pulumi.output_type
class EnvironmentStorageConfigurationEfs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, file_system_id: _builtins.str, mount_point: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mountPoint")
    def mount_point(self) -> _builtins.str: ...

@pulumi.output_type
class EnvironmentStorageConfigurationFsx(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, file_system_id: _builtins.str, mount_point: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mountPoint")
    def mount_point(self) -> _builtins.str: ...

@pulumi.output_type
class EnvironmentTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...
