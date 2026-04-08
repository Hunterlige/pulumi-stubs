import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BookmarkArgs", "Bookmark"]

@pulumi.input_type
class BookmarkArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        query: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        workspace_name: pulumi.Input[_builtins.str],
        bookmark_id: Optional[pulumi.Input[_builtins.str]] = ...,
        created: Optional[pulumi.Input[_builtins.str]] = ...,
        created_by: Optional[pulumi.Input[UserInfoArgs]] = ...,
        event_time: Optional[pulumi.Input[_builtins.str]] = ...,
        incident_info: Optional[pulumi.Input[IncidentInfoArgs]] = ...,
        labels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        notes: Optional[pulumi.Input[_builtins.str]] = ...,
        query_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        query_result: Optional[pulumi.Input[_builtins.str]] = ...,
        query_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        updated: Optional[pulumi.Input[_builtins.str]] = ...,
        updated_by: Optional[pulumi.Input[UserInfoArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> pulumi.Input[_builtins.str]: ...
    @query.setter
    def query(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="bookmarkId")
    def bookmark_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bookmark_id.setter
    def bookmark_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created.setter
    def created(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[UserInfoArgs]]: ...
    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[UserInfoArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="eventTime")
    def event_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_time.setter
    def event_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="incidentInfo")
    def incident_info(self) -> Optional[pulumi.Input[IncidentInfoArgs]]: ...
    @incident_info.setter
    def incident_info(self, value: Optional[pulumi.Input[IncidentInfoArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notes.setter
    def notes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryEndTime")
    def query_end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_end_time.setter
    def query_end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryResult")
    def query_result(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_result.setter
    def query_result(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryStartTime")
    def query_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_start_time.setter
    def query_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def updated(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @updated.setter
    def updated(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> Optional[pulumi.Input[UserInfoArgs]]: ...
    @updated_by.setter
    def updated_by(self, value: Optional[pulumi.Input[UserInfoArgs]]): ...

@pulumi.type_token("azure-native:securityinsights:Bookmark")
class Bookmark(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bookmark_id: Optional[pulumi.Input[_builtins.str]] = ...,
        created: Optional[pulumi.Input[_builtins.str]] = ...,
        created_by: Optional[pulumi.Input[Union[UserInfoArgs, UserInfoArgsDict]]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        event_time: Optional[pulumi.Input[_builtins.str]] = ...,
        incident_info: Optional[
            pulumi.Input[Union[IncidentInfoArgs, IncidentInfoArgsDict]]
        ] = ...,
        labels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        notes: Optional[pulumi.Input[_builtins.str]] = ...,
        query: Optional[pulumi.Input[_builtins.str]] = ...,
        query_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        query_result: Optional[pulumi.Input[_builtins.str]] = ...,
        query_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        updated: Optional[pulumi.Input[_builtins.str]] = ...,
        updated_by: Optional[pulumi.Input[Union[UserInfoArgs, UserInfoArgsDict]]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BookmarkArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Bookmark: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[Optional[outputs.UserInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="eventTime")
    def event_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="incidentInfo")
    def incident_info(
        self,
    ) -> pulumi.Output[Optional[outputs.IncidentInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryEndTime")
    def query_end_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="queryResult")
    def query_result(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="queryStartTime")
    def query_start_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def updated(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> pulumi.Output[Optional[outputs.UserInfoResponse]]: ...
