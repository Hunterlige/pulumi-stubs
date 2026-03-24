import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EntryLinkArgs", "EntryLink"]

@pulumi.input_type
class EntryLinkArgs:
    def __init__(
        __self__,
        *,
        entry_group_id: pulumi.Input[_builtins.str],
        entry_link_id: pulumi.Input[_builtins.str],
        entry_link_type: pulumi.Input[_builtins.str],
        entry_references: pulumi.Input[
            Sequence[pulumi.Input[EntryLinkEntryReferenceArgs]]
        ],
        location: pulumi.Input[_builtins.str],
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entryGroupId")
    def entry_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @entry_group_id.setter
    def entry_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="entryLinkId")
    def entry_link_id(self) -> pulumi.Input[_builtins.str]: ...
    @entry_link_id.setter
    def entry_link_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="entryLinkType")
    def entry_link_type(self) -> pulumi.Input[_builtins.str]: ...
    @entry_link_type.setter
    def entry_link_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="entryReferences")
    def entry_references(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[EntryLinkEntryReferenceArgs]]]: ...
    @entry_references.setter
    def entry_references(
        self, value: pulumi.Input[Sequence[pulumi.Input[EntryLinkEntryReferenceArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _EntryLinkState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_link_id: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_link_type: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_references: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntryLinkEntryReferenceArgs]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="entryLinkId")
    def entry_link_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entry_link_id.setter
    def entry_link_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entryLinkType")
    def entry_link_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entry_link_type.setter
    def entry_link_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entryReferences")
    def entry_references(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EntryLinkEntryReferenceArgs]]]
    ]: ...
    @entry_references.setter
    def entry_references(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntryLinkEntryReferenceArgs]]]
        ],
    ): ...
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
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:dataplex/entryLink:EntryLink")
class EntryLink(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        entry_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_link_id: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_link_type: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_references: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EntryLinkEntryReferenceArgs, EntryLinkEntryReferenceArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EntryLinkArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_link_id: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_link_type: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_references: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EntryLinkEntryReferenceArgs, EntryLinkEntryReferenceArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> EntryLink: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entryGroupId")
    def entry_group_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entryLinkId")
    def entry_link_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entryLinkType")
    def entry_link_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entryReferences")
    def entry_references(
        self,
    ) -> pulumi.Output[Sequence[outputs.EntryLinkEntryReference]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
