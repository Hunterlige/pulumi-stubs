import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CollaborationArgs", "Collaboration"]

@pulumi.input_type
class CollaborationArgs:
    def __init__(
        __self__,
        *,
        creator_display_name: pulumi.Input[_builtins.str],
        creator_member_abilities: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        description: pulumi.Input[_builtins.str],
        query_log_status: pulumi.Input[_builtins.str],
        analytics_engine: Optional[pulumi.Input[_builtins.str]] = ...,
        data_encryption_metadata: Optional[
            pulumi.Input[CollaborationDataEncryptionMetadataArgs]
        ] = ...,
        members: Optional[
            pulumi.Input[Sequence[pulumi.Input[CollaborationMemberArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creatorDisplayName")
    def creator_display_name(self) -> pulumi.Input[_builtins.str]: ...
    @creator_display_name.setter
    def creator_display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="creatorMemberAbilities")
    def creator_member_abilities(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @creator_member_abilities.setter
    def creator_member_abilities(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]: ...
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="queryLogStatus")
    def query_log_status(self) -> pulumi.Input[_builtins.str]: ...
    @query_log_status.setter
    def query_log_status(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="analyticsEngine")
    def analytics_engine(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @analytics_engine.setter
    def analytics_engine(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataEncryptionMetadata")
    def data_encryption_metadata(
        self,
    ) -> Optional[pulumi.Input[CollaborationDataEncryptionMetadataArgs]]: ...
    @data_encryption_metadata.setter
    def data_encryption_metadata(
        self, value: Optional[pulumi.Input[CollaborationDataEncryptionMetadataArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def members(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CollaborationMemberArgs]]]]: ...
    @members.setter
    def members(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[CollaborationMemberArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _CollaborationState:
    def __init__(
        __self__,
        *,
        analytics_engine: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        creator_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        creator_member_abilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        data_encryption_metadata: Optional[
            pulumi.Input[CollaborationDataEncryptionMetadataArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        members: Optional[
            pulumi.Input[Sequence[pulumi.Input[CollaborationMemberArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        query_log_status: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="analyticsEngine")
    def analytics_engine(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @analytics_engine.setter
    def analytics_engine(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="creatorDisplayName")
    def creator_display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creator_display_name.setter
    def creator_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="creatorMemberAbilities")
    def creator_member_abilities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @creator_member_abilities.setter
    def creator_member_abilities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataEncryptionMetadata")
    def data_encryption_metadata(
        self,
    ) -> Optional[pulumi.Input[CollaborationDataEncryptionMetadataArgs]]: ...
    @data_encryption_metadata.setter
    def data_encryption_metadata(
        self, value: Optional[pulumi.Input[CollaborationDataEncryptionMetadataArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def members(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CollaborationMemberArgs]]]]: ...
    @members.setter
    def members(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[CollaborationMemberArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryLogStatus")
    def query_log_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_log_status.setter
    def query_log_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:cleanrooms/collaboration:Collaboration")
class Collaboration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        analytics_engine: Optional[pulumi.Input[_builtins.str]] = ...,
        creator_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        creator_member_abilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        data_encryption_metadata: Optional[
            pulumi.Input[
                Union[
                    CollaborationDataEncryptionMetadataArgs,
                    CollaborationDataEncryptionMetadataArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        members: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CollaborationMemberArgs, CollaborationMemberArgsDict]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        query_log_status: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CollaborationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        analytics_engine: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        creator_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        creator_member_abilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        data_encryption_metadata: Optional[
            pulumi.Input[
                Union[
                    CollaborationDataEncryptionMetadataArgs,
                    CollaborationDataEncryptionMetadataArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        members: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CollaborationMemberArgs, CollaborationMemberArgsDict]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        query_log_status: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Collaboration: ...
    @_builtins.property
    @pulumi.getter(name="analyticsEngine")
    def analytics_engine(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creatorDisplayName")
    def creator_display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creatorMemberAbilities")
    def creator_member_abilities(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dataEncryptionMetadata")
    def data_encryption_metadata(
        self,
    ) -> pulumi.Output[Optional[outputs.CollaborationDataEncryptionMetadata]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def members(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.CollaborationMember]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryLogStatus")
    def query_log_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
