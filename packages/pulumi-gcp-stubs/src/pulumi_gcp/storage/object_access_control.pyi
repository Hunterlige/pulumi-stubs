import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ObjectAccessControlArgs", "ObjectAccessControl"]

@pulumi.input_type
class ObjectAccessControlArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        entity: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        role: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def entity(self) -> pulumi.Input[_builtins.str]: ...
    @entity.setter
    def entity(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]: ...
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _ObjectAccessControlState:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        entity: Optional[pulumi.Input[_builtins.str]] = ...,
        entity_id: Optional[pulumi.Input[_builtins.str]] = ...,
        generation: Optional[pulumi.Input[_builtins.int]] = ...,
        object: Optional[pulumi.Input[_builtins.str]] = ...,
        project_teams: Optional[
            pulumi.Input[Sequence[pulumi.Input[ObjectAccessControlProjectTeamArgs]]]
        ] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def entity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entity.setter
    def entity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entity_id.setter
    def entity_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object.setter
    def object(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectTeams")
    def project_teams(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ObjectAccessControlProjectTeamArgs]]]
    ]: ...
    @project_teams.setter
    def project_teams(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ObjectAccessControlProjectTeamArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ObjectAccessControl(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        entity: Optional[pulumi.Input[_builtins.str]] = ...,
        object: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ObjectAccessControlArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        entity: Optional[pulumi.Input[_builtins.str]] = ...,
        entity_id: Optional[pulumi.Input[_builtins.str]] = ...,
        generation: Optional[pulumi.Input[_builtins.int]] = ...,
        object: Optional[pulumi.Input[_builtins.str]] = ...,
        project_teams: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ObjectAccessControlProjectTeamArgs,
                            ObjectAccessControlProjectTeamArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ObjectAccessControl: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def entity(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectTeams")
    def project_teams(
        self,
    ) -> pulumi.Output[Sequence[outputs.ObjectAccessControlProjectTeam]]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]: ...
