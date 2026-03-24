import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DevEnvironmentArgs", "DevEnvironment"]

@pulumi.input_type
class DevEnvironmentArgs:
    def __init__(
        __self__,
        *,
        ides: pulumi.Input[DevEnvironmentIdesArgs],
        instance_type: pulumi.Input[_builtins.str],
        persistent_storage: pulumi.Input[DevEnvironmentPersistentStorageArgs],
        project_name: pulumi.Input[_builtins.str],
        space_name: pulumi.Input[_builtins.str],
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        inactivity_timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repositories: Optional[
            pulumi.Input[Sequence[pulumi.Input[DevEnvironmentRepositoryArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ides(self) -> pulumi.Input[DevEnvironmentIdesArgs]: ...
    @ides.setter
    def ides(self, value: pulumi.Input[DevEnvironmentIdesArgs]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="persistentStorage")
    def persistent_storage(
        self,
    ) -> pulumi.Input[DevEnvironmentPersistentStorageArgs]: ...
    @persistent_storage.setter
    def persistent_storage(
        self, value: pulumi.Input[DevEnvironmentPersistentStorageArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[_builtins.str]: ...
    @project_name.setter
    def project_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="spaceName")
    def space_name(self) -> pulumi.Input[_builtins.str]: ...
    @space_name.setter
    def space_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alias.setter
    def alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inactivityTimeoutMinutes")
    def inactivity_timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @inactivity_timeout_minutes.setter
    def inactivity_timeout_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def repositories(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DevEnvironmentRepositoryArgs]]]
    ]: ...
    @repositories.setter
    def repositories(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DevEnvironmentRepositoryArgs]]]
        ],
    ): ...

@pulumi.input_type
class _DevEnvironmentState:
    def __init__(
        __self__,
        *,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        ides: Optional[pulumi.Input[DevEnvironmentIdesArgs]] = ...,
        inactivity_timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        persistent_storage: Optional[
            pulumi.Input[DevEnvironmentPersistentStorageArgs]
        ] = ...,
        project_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repositories: Optional[
            pulumi.Input[Sequence[pulumi.Input[DevEnvironmentRepositoryArgs]]]
        ] = ...,
        space_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alias.setter
    def alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ides(self) -> Optional[pulumi.Input[DevEnvironmentIdesArgs]]: ...
    @ides.setter
    def ides(self, value: Optional[pulumi.Input[DevEnvironmentIdesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="inactivityTimeoutMinutes")
    def inactivity_timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @inactivity_timeout_minutes.setter
    def inactivity_timeout_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="persistentStorage")
    def persistent_storage(
        self,
    ) -> Optional[pulumi.Input[DevEnvironmentPersistentStorageArgs]]: ...
    @persistent_storage.setter
    def persistent_storage(
        self, value: Optional[pulumi.Input[DevEnvironmentPersistentStorageArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_name.setter
    def project_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def repositories(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DevEnvironmentRepositoryArgs]]]
    ]: ...
    @repositories.setter
    def repositories(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DevEnvironmentRepositoryArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="spaceName")
    def space_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @space_name.setter
    def space_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:codecatalyst/devEnvironment:DevEnvironment")
class DevEnvironment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        ides: Optional[
            pulumi.Input[Union[DevEnvironmentIdesArgs, DevEnvironmentIdesArgsDict]]
        ] = ...,
        inactivity_timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        persistent_storage: Optional[
            pulumi.Input[
                Union[
                    DevEnvironmentPersistentStorageArgs,
                    DevEnvironmentPersistentStorageArgsDict,
                ]
            ]
        ] = ...,
        project_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repositories: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DevEnvironmentRepositoryArgs,
                            DevEnvironmentRepositoryArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        space_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DevEnvironmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        ides: Optional[
            pulumi.Input[Union[DevEnvironmentIdesArgs, DevEnvironmentIdesArgsDict]]
        ] = ...,
        inactivity_timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        persistent_storage: Optional[
            pulumi.Input[
                Union[
                    DevEnvironmentPersistentStorageArgs,
                    DevEnvironmentPersistentStorageArgsDict,
                ]
            ]
        ] = ...,
        project_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repositories: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DevEnvironmentRepositoryArgs,
                            DevEnvironmentRepositoryArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        space_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> DevEnvironment: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def ides(self) -> pulumi.Output[outputs.DevEnvironmentIdes]: ...
    @_builtins.property
    @pulumi.getter(name="inactivityTimeoutMinutes")
    def inactivity_timeout_minutes(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="persistentStorage")
    def persistent_storage(
        self,
    ) -> pulumi.Output[outputs.DevEnvironmentPersistentStorage]: ...
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def repositories(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.DevEnvironmentRepository]]]: ...
    @_builtins.property
    @pulumi.getter(name="spaceName")
    def space_name(self) -> pulumi.Output[_builtins.str]: ...
