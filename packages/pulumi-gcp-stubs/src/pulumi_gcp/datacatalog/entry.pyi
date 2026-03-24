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
        entry_group: pulumi.Input[_builtins.str],
        entry_id: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gcs_fileset_spec: Optional[pulumi.Input[EntryGcsFilesetSpecArgs]] = ...,
        linked_resource: Optional[pulumi.Input[_builtins.str]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        user_specified_system: Optional[pulumi.Input[_builtins.str]] = ...,
        user_specified_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entryGroup")
    def entry_group(self) -> pulumi.Input[_builtins.str]: ...
    @entry_group.setter
    def entry_group(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="entryId")
    def entry_id(self) -> pulumi.Input[_builtins.str]: ...
    @entry_id.setter
    def entry_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gcsFilesetSpec")
    def gcs_fileset_spec(self) -> Optional[pulumi.Input[EntryGcsFilesetSpecArgs]]: ...
    @gcs_fileset_spec.setter
    def gcs_fileset_spec(
        self, value: Optional[pulumi.Input[EntryGcsFilesetSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedResource")
    def linked_resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_resource.setter
    def linked_resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userSpecifiedSystem")
    def user_specified_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_specified_system.setter
    def user_specified_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userSpecifiedType")
    def user_specified_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_specified_type.setter
    def user_specified_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _EntryState:
    def __init__(
        __self__,
        *,
        bigquery_date_sharded_specs: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntryBigqueryDateShardedSpecArgs]]]
        ] = ...,
        bigquery_table_specs: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntryBigqueryTableSpecArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_group: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        gcs_fileset_spec: Optional[pulumi.Input[EntryGcsFilesetSpecArgs]] = ...,
        integrated_system: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_resource: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        user_specified_system: Optional[pulumi.Input[_builtins.str]] = ...,
        user_specified_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryDateShardedSpecs")
    def bigquery_date_sharded_specs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EntryBigqueryDateShardedSpecArgs]]]
    ]: ...
    @bigquery_date_sharded_specs.setter
    def bigquery_date_sharded_specs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntryBigqueryDateShardedSpecArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bigqueryTableSpecs")
    def bigquery_table_specs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EntryBigqueryTableSpecArgs]]]]: ...
    @bigquery_table_specs.setter
    def bigquery_table_specs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntryBigqueryTableSpecArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entryGroup")
    def entry_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entry_group.setter
    def entry_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entryId")
    def entry_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entry_id.setter
    def entry_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gcsFilesetSpec")
    def gcs_fileset_spec(self) -> Optional[pulumi.Input[EntryGcsFilesetSpecArgs]]: ...
    @gcs_fileset_spec.setter
    def gcs_fileset_spec(
        self, value: Optional[pulumi.Input[EntryGcsFilesetSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="integratedSystem")
    def integrated_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integrated_system.setter
    def integrated_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkedResource")
    def linked_resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_resource.setter
    def linked_resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userSpecifiedSystem")
    def user_specified_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_specified_system.setter
    def user_specified_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userSpecifiedType")
    def user_specified_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_specified_type.setter
    def user_specified_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:datacatalog/entry:Entry")
class Entry(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_group: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        gcs_fileset_spec: Optional[
            pulumi.Input[Union[EntryGcsFilesetSpecArgs, EntryGcsFilesetSpecArgsDict]]
        ] = ...,
        linked_resource: Optional[pulumi.Input[_builtins.str]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        user_specified_system: Optional[pulumi.Input[_builtins.str]] = ...,
        user_specified_type: Optional[pulumi.Input[_builtins.str]] = ...,
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
        bigquery_date_sharded_specs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EntryBigqueryDateShardedSpecArgs,
                            EntryBigqueryDateShardedSpecArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        bigquery_table_specs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EntryBigqueryTableSpecArgs, EntryBigqueryTableSpecArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_group: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        gcs_fileset_spec: Optional[
            pulumi.Input[Union[EntryGcsFilesetSpecArgs, EntryGcsFilesetSpecArgsDict]]
        ] = ...,
        integrated_system: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_resource: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        user_specified_system: Optional[pulumi.Input[_builtins.str]] = ...,
        user_specified_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Entry: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryDateShardedSpecs")
    def bigquery_date_sharded_specs(
        self,
    ) -> pulumi.Output[Sequence[outputs.EntryBigqueryDateShardedSpec]]: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryTableSpecs")
    def bigquery_table_specs(
        self,
    ) -> pulumi.Output[Sequence[outputs.EntryBigqueryTableSpec]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="entryGroup")
    def entry_group(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entryId")
    def entry_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gcsFilesetSpec")
    def gcs_fileset_spec(
        self,
    ) -> pulumi.Output[Optional[outputs.EntryGcsFilesetSpec]]: ...
    @_builtins.property
    @pulumi.getter(name="integratedSystem")
    def integrated_system(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linkedResource")
    def linked_resource(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userSpecifiedSystem")
    def user_specified_system(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userSpecifiedType")
    def user_specified_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
