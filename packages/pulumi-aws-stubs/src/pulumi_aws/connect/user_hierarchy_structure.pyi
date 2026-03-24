import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UserHierarchyStructureArgs", "UserHierarchyStructure"]

@pulumi.input_type
class UserHierarchyStructureArgs:
    def __init__(
        __self__,
        *,
        hierarchy_structure: pulumi.Input[UserHierarchyStructureHierarchyStructureArgs],
        instance_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hierarchyStructure")
    def hierarchy_structure(
        self,
    ) -> pulumi.Input[UserHierarchyStructureHierarchyStructureArgs]: ...
    @hierarchy_structure.setter
    def hierarchy_structure(
        self, value: pulumi.Input[UserHierarchyStructureHierarchyStructureArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[_builtins.str]: ...
    @instance_id.setter
    def instance_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _UserHierarchyStructureState:
    def __init__(
        __self__,
        *,
        hierarchy_structure: Optional[
            pulumi.Input[UserHierarchyStructureHierarchyStructureArgs]
        ] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hierarchyStructure")
    def hierarchy_structure(
        self,
    ) -> Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureArgs]]: ...
    @hierarchy_structure.setter
    def hierarchy_structure(
        self,
        value: Optional[pulumi.Input[UserHierarchyStructureHierarchyStructureArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class UserHierarchyStructure(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        hierarchy_structure: Optional[
            pulumi.Input[
                Union[
                    UserHierarchyStructureHierarchyStructureArgs,
                    UserHierarchyStructureHierarchyStructureArgsDict,
                ]
            ]
        ] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: UserHierarchyStructureArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        hierarchy_structure: Optional[
            pulumi.Input[
                Union[
                    UserHierarchyStructureHierarchyStructureArgs,
                    UserHierarchyStructureHierarchyStructureArgsDict,
                ]
            ]
        ] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> UserHierarchyStructure: ...
    @_builtins.property
    @pulumi.getter(name="hierarchyStructure")
    def hierarchy_structure(
        self,
    ) -> pulumi.Output[outputs.UserHierarchyStructureHierarchyStructure]: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
