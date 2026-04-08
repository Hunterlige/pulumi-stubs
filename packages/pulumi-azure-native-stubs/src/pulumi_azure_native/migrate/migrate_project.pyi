import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MigrateProjectArgs", "MigrateProject"]

@pulumi.input_type
class MigrateProjectArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        e_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        migrate_project_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[MigrateProjectPropertiesArgs]] = ...,
        tags: Optional[pulumi.Input[MigrateProjectTagsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="migrateProjectName")
    def migrate_project_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @migrate_project_name.setter
    def migrate_project_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[MigrateProjectPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[MigrateProjectPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[MigrateProjectTagsArgs]]: ...
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[MigrateProjectTagsArgs]]): ...

@pulumi.type_token("azure-native:migrate:MigrateProject")
class MigrateProject(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        e_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        migrate_project_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[MigrateProjectPropertiesArgs, MigrateProjectPropertiesArgsDict]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[
            pulumi.Input[Union[MigrateProjectTagsArgs, MigrateProjectTagsArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MigrateProjectArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> MigrateProject: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.MigrateProjectPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[outputs.MigrateProjectResponseTags]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
