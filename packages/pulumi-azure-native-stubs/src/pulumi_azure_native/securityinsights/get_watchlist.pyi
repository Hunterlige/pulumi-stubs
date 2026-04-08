import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWatchlistResult",
    "AwaitableGetWatchlistResult",
    "get_watchlist",
    "get_watchlist_output",
]

@pulumi.output_type
class GetWatchlistResult:
    def __init__(
        __self__,
        azure_api_version=...,
        content_type=...,
        created=...,
        created_by=...,
        default_duration=...,
        description=...,
        display_name=...,
        etag=...,
        id=...,
        is_deleted=...,
        items_search_key=...,
        labels=...,
        name=...,
        number_of_lines_to_skip=...,
        provider=...,
        provisioning_state=...,
        raw_content=...,
        source=...,
        source_type=...,
        system_data=...,
        tenant_id=...,
        type=...,
        updated=...,
        updated_by=...,
        upload_status=...,
        watchlist_alias=...,
        watchlist_id=...,
        watchlist_type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[outputs.WatchlistUserInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="defaultDuration")
    def default_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isDeleted")
    def is_deleted(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="itemsSearchKey")
    def items_search_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="numberOfLinesToSkip")
    def number_of_lines_to_skip(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rawContent")
    def raw_content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def updated(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> Optional[outputs.WatchlistUserInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="uploadStatus")
    def upload_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="watchlistAlias")
    def watchlist_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="watchlistId")
    def watchlist_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="watchlistType")
    def watchlist_type(self) -> Optional[_builtins.str]: ...

class AwaitableGetWatchlistResult(GetWatchlistResult):
    def __await__(self): ...

def get_watchlist(
    resource_group_name: Optional[_builtins.str] = ...,
    watchlist_alias: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWatchlistResult: ...
def get_watchlist_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    watchlist_alias: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWatchlistResult]: ...
