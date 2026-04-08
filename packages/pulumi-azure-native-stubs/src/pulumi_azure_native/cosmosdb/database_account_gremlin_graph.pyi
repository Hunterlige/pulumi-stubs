import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DatabaseAccountGremlinGraphArgs", "DatabaseAccountGremlinGraph"]

@pulumi.input_type
class DatabaseAccountGremlinGraphArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        database_name: pulumi.Input[_builtins.str],
        options: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        resource: pulumi.Input[GremlinGraphResourceArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        graph_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @options.setter
    def options(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Input[GremlinGraphResourceArgs]: ...
    @resource.setter
    def resource(self, value: pulumi.Input[GremlinGraphResourceArgs]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="graphName")
    def graph_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @graph_name.setter
    def graph_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:cosmosdb:DatabaseAccountGremlinGraph")
class DatabaseAccountGremlinGraph(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        graph_name: Optional[pulumi.Input[_builtins.str]] = ...,
        options: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource: Optional[
            pulumi.Input[Union[GremlinGraphResourceArgs, GremlinGraphResourceArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DatabaseAccountGremlinGraphArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> DatabaseAccountGremlinGraph: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="conflictResolutionPolicy")
    def conflict_resolution_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.ConflictResolutionPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="indexingPolicy")
    def indexing_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.IndexingPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(
        self,
    ) -> pulumi.Output[Optional[outputs.ContainerPartitionKeyResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def rid(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def ts(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="uniqueKeyPolicy")
    def unique_key_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.UniqueKeyPolicyResponse]]: ...
