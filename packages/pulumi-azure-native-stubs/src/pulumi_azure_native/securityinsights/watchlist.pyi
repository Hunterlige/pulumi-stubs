

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WatchlistArgs', 'Watchlist']
@pulumi.input_type
class WatchlistArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], items_search_key: pulumi.Input[_builtins.str], provider: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], content_type: Optional[pulumi.Input[_builtins.str]] = ..., created: Optional[pulumi.Input[_builtins.str]] = ..., created_by: Optional[pulumi.Input[WatchlistUserInfoArgs]] = ..., default_duration: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., is_deleted: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., number_of_lines_to_skip: Optional[pulumi.Input[_builtins.int]] = ..., raw_content: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[_builtins.str]] = ..., source_type: Optional[pulumi.Input[Union[_builtins.str, SourceType]]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., updated: Optional[pulumi.Input[_builtins.str]] = ..., updated_by: Optional[pulumi.Input[WatchlistUserInfoArgs]] = ..., upload_status: Optional[pulumi.Input[_builtins.str]] = ..., watchlist_alias: Optional[pulumi.Input[_builtins.str]] = ..., watchlist_id: Optional[pulumi.Input[_builtins.str]] = ..., watchlist_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemsSearchKey")
    def items_search_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @items_search_key.setter
    def items_search_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def provider(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @provider.setter
    def provider(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created.setter
    def created(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[WatchlistUserInfoArgs]]:
        
        ...
    
    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[WatchlistUserInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDuration")
    def default_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_duration.setter
    def default_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeleted")
    def is_deleted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_deleted.setter
    def is_deleted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfLinesToSkip")
    def number_of_lines_to_skip(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @number_of_lines_to_skip.setter
    def number_of_lines_to_skip(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rawContent")
    def raw_content(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @raw_content.setter
    def raw_content(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[pulumi.Input[Union[_builtins.str, SourceType]]]:
        
        ...
    
    @source_type.setter
    def source_type(self, value: Optional[pulumi.Input[Union[_builtins.str, SourceType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def updated(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @updated.setter
    def updated(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> Optional[pulumi.Input[WatchlistUserInfoArgs]]:
        
        ...
    
    @updated_by.setter
    def updated_by(self, value: Optional[pulumi.Input[WatchlistUserInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadStatus")
    def upload_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @upload_status.setter
    def upload_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="watchlistAlias")
    def watchlist_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @watchlist_alias.setter
    def watchlist_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="watchlistId")
    def watchlist_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @watchlist_id.setter
    def watchlist_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="watchlistType")
    def watchlist_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @watchlist_type.setter
    def watchlist_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:securityinsights:Watchlist")
class Watchlist(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., content_type: Optional[pulumi.Input[_builtins.str]] = ..., created: Optional[pulumi.Input[_builtins.str]] = ..., created_by: Optional[pulumi.Input[Union[WatchlistUserInfoArgs, WatchlistUserInfoArgsDict]]] = ..., default_duration: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., is_deleted: Optional[pulumi.Input[_builtins.bool]] = ..., items_search_key: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., number_of_lines_to_skip: Optional[pulumi.Input[_builtins.int]] = ..., provider: Optional[pulumi.Input[_builtins.str]] = ..., raw_content: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[_builtins.str]] = ..., source_type: Optional[pulumi.Input[Union[_builtins.str, SourceType]]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., updated: Optional[pulumi.Input[_builtins.str]] = ..., updated_by: Optional[pulumi.Input[Union[WatchlistUserInfoArgs, WatchlistUserInfoArgsDict]]] = ..., upload_status: Optional[pulumi.Input[_builtins.str]] = ..., watchlist_alias: Optional[pulumi.Input[_builtins.str]] = ..., watchlist_id: Optional[pulumi.Input[_builtins.str]] = ..., watchlist_type: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WatchlistArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Watchlist:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def created(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[Optional[outputs.WatchlistUserInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDuration")
    def default_duration(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeleted")
    def is_deleted(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemsSearchKey")
    def items_search_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfLinesToSkip")
    def number_of_lines_to_skip(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def provider(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rawContent")
    def raw_content(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def updated(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> pulumi.Output[Optional[outputs.WatchlistUserInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadStatus")
    def upload_status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="watchlistAlias")
    def watchlist_alias(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="watchlistId")
    def watchlist_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="watchlistType")
    def watchlist_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


