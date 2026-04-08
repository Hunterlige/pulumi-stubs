import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ActivityCustomEntityQueryArgs", "ActivityCustomEntityQuery"]

@pulumi.input_type
class ActivityCustomEntityQueryArgs:
    def __init__(
        __self__,
        *,
        kind: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        workspace_name: pulumi.Input[_builtins.str],
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        entities_filter: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
        entity_query_id: Optional[pulumi.Input[_builtins.str]] = ...,
        input_entity_type: Optional[
            pulumi.Input[Union[_builtins.str, EntityType]]
        ] = ...,
        query_definitions: Optional[
            pulumi.Input[ActivityEntityQueriesPropertiesQueryDefinitionsArgs]
        ] = ...,
        required_input_fields_sets: Optional[
            pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]
        ] = ...,
        template_name: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="entitiesFilter")
    def entities_filter(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]
    ]: ...
    @entities_filter.setter
    def entities_filter(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="entityQueryId")
    def entity_query_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entity_query_id.setter
    def entity_query_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputEntityType")
    def input_entity_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EntityType]]]: ...
    @input_entity_type.setter
    def input_entity_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EntityType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryDefinitions")
    def query_definitions(
        self,
    ) -> Optional[
        pulumi.Input[ActivityEntityQueriesPropertiesQueryDefinitionsArgs]
    ]: ...
    @query_definitions.setter
    def query_definitions(
        self,
        value: Optional[
            pulumi.Input[ActivityEntityQueriesPropertiesQueryDefinitionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requiredInputFieldsSets")
    def required_input_fields_sets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]
    ]: ...
    @required_input_fields_sets.setter
    def required_input_fields_sets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_name.setter
    def template_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ActivityCustomEntityQuery(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        entities_filter: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
        entity_query_id: Optional[pulumi.Input[_builtins.str]] = ...,
        input_entity_type: Optional[
            pulumi.Input[Union[_builtins.str, EntityType]]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        query_definitions: Optional[
            pulumi.Input[
                Union[
                    ActivityEntityQueriesPropertiesQueryDefinitionsArgs,
                    ActivityEntityQueriesPropertiesQueryDefinitionsArgsDict,
                ]
            ]
        ] = ...,
        required_input_fields_sets: Optional[
            pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        template_name: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ActivityCustomEntityQueryArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ActivityCustomEntityQuery: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="entitiesFilter")
    def entities_filter(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, Sequence[_builtins.str]]]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inputEntityType")
    def input_entity_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTimeUtc")
    def last_modified_time_utc(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryDefinitions")
    def query_definitions(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ActivityEntityQueriesPropertiesResponseQueryDefinitions]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="requiredInputFieldsSets")
    def required_input_fields_sets(
        self,
    ) -> pulumi.Output[Optional[Sequence[Sequence[_builtins.str]]]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="templateName")
    def template_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
