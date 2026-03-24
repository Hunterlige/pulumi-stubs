import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EntryArgs", "Entry"]

@pulumi.input_type
class EntryArgs:
    def __init__(
        __self__,
        *,
        entry_type: pulumi.Input[_builtins.str],
        aspects: Optional[pulumi.Input[Sequence[pulumi.Input[EntryAspectArgs]]]] = ...,
        entry_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_source: Optional[pulumi.Input[EntryEntrySourceArgs]] = ...,
        fully_qualified_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_entry: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entryType")
    def entry_type(self) -> pulumi.Input[_builtins.str]: ...
    @entry_type.setter
    def entry_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def aspects(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EntryAspectArgs]]]]: ...
    @aspects.setter
    def aspects(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EntryAspectArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="entryGroupId")
    def entry_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entry_group_id.setter
    def entry_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entryId")
    def entry_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entry_id.setter
    def entry_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entrySource")
    def entry_source(self) -> Optional[pulumi.Input[EntryEntrySourceArgs]]: ...
    @entry_source.setter
    def entry_source(self, value: Optional[pulumi.Input[EntryEntrySourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedName")
    def fully_qualified_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fully_qualified_name.setter
    def fully_qualified_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parentEntry")
    def parent_entry(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_entry.setter
    def parent_entry(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _EntryState:
    def __init__(
        __self__,
        *,
        aspects: Optional[pulumi.Input[Sequence[pulumi.Input[EntryAspectArgs]]]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_source: Optional[pulumi.Input[EntryEntrySourceArgs]] = ...,
        entry_type: Optional[pulumi.Input[_builtins.str]] = ...,
        fully_qualified_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_entry: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def aspects(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EntryAspectArgs]]]]: ...
    @aspects.setter
    def aspects(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EntryAspectArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entryGroupId")
    def entry_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entry_group_id.setter
    def entry_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entryId")
    def entry_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entry_id.setter
    def entry_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entrySource")
    def entry_source(self) -> Optional[pulumi.Input[EntryEntrySourceArgs]]: ...
    @entry_source.setter
    def entry_source(self, value: Optional[pulumi.Input[EntryEntrySourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="entryType")
    def entry_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entry_type.setter
    def entry_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedName")
    def fully_qualified_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fully_qualified_name.setter
    def fully_qualified_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parentEntry")
    def parent_entry(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_entry.setter
    def parent_entry(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:dataplex/entry:Entry")
class Entry(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        aspects: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[EntryAspectArgs, EntryAspectArgsDict]]]
            ]
        ] = ...,
        entry_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_source: Optional[
            pulumi.Input[Union[EntryEntrySourceArgs, EntryEntrySourceArgsDict]]
        ] = ...,
        entry_type: Optional[pulumi.Input[_builtins.str]] = ...,
        fully_qualified_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_entry: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EntryArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        aspects: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[EntryAspectArgs, EntryAspectArgsDict]]]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_source: Optional[
            pulumi.Input[Union[EntryEntrySourceArgs, EntryEntrySourceArgsDict]]
        ] = ...,
        entry_type: Optional[pulumi.Input[_builtins.str]] = ...,
        fully_qualified_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_entry: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Entry: ...
    @_builtins.property
    @pulumi.getter
    def aspects(self) -> pulumi.Output[Optional[Sequence[outputs.EntryAspect]]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entryGroupId")
    def entry_group_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="entryId")
    def entry_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="entrySource")
    def entry_source(self) -> pulumi.Output[outputs.EntryEntrySource]: ...
    @_builtins.property
    @pulumi.getter(name="entryType")
    def entry_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedName")
    def fully_qualified_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parentEntry")
    def parent_entry(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
