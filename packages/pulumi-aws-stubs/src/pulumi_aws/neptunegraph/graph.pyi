import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GraphArgs", "Graph"]

@pulumi.input_type
class GraphArgs:
    def __init__(
        __self__,
        *,
        provisioned_memory: pulumi.Input[_builtins.int],
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        graph_name: Optional[pulumi.Input[_builtins.str]] = ...,
        graph_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        public_connectivity: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[GraphTimeoutsArgs]] = ...,
        vector_search_configuration: Optional[
            pulumi.Input[GraphVectorSearchConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisionedMemory")
    def provisioned_memory(self) -> pulumi.Input[_builtins.int]: ...
    @provisioned_memory.setter
    def provisioned_memory(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="graphName")
    def graph_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @graph_name.setter
    def graph_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="graphNamePrefix")
    def graph_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @graph_name_prefix.setter
    def graph_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_identifier.setter
    def kms_key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicConnectivity")
    def public_connectivity(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @public_connectivity.setter
    def public_connectivity(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[GraphTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[GraphTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="vectorSearchConfiguration")
    def vector_search_configuration(
        self,
    ) -> Optional[pulumi.Input[GraphVectorSearchConfigurationArgs]]: ...
    @vector_search_configuration.setter
    def vector_search_configuration(
        self, value: Optional[pulumi.Input[GraphVectorSearchConfigurationArgs]]
    ): ...

@pulumi.input_type
class _GraphState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        graph_name: Optional[pulumi.Input[_builtins.str]] = ...,
        graph_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_memory: Optional[pulumi.Input[_builtins.int]] = ...,
        public_connectivity: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[GraphTimeoutsArgs]] = ...,
        vector_search_configuration: Optional[
            pulumi.Input[GraphVectorSearchConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="graphName")
    def graph_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @graph_name.setter
    def graph_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="graphNamePrefix")
    def graph_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @graph_name_prefix.setter
    def graph_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_identifier.setter
    def kms_key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedMemory")
    def provisioned_memory(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_memory.setter
    def provisioned_memory(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="publicConnectivity")
    def public_connectivity(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @public_connectivity.setter
    def public_connectivity(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[GraphTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[GraphTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="vectorSearchConfiguration")
    def vector_search_configuration(
        self,
    ) -> Optional[pulumi.Input[GraphVectorSearchConfigurationArgs]]: ...
    @vector_search_configuration.setter
    def vector_search_configuration(
        self, value: Optional[pulumi.Input[GraphVectorSearchConfigurationArgs]]
    ): ...

@pulumi.type_token("aws:neptunegraph/graph:Graph")
class Graph(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        graph_name: Optional[pulumi.Input[_builtins.str]] = ...,
        graph_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_memory: Optional[pulumi.Input[_builtins.int]] = ...,
        public_connectivity: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[GraphTimeoutsArgs, GraphTimeoutsArgsDict]]
        ] = ...,
        vector_search_configuration: Optional[
            pulumi.Input[
                Union[
                    GraphVectorSearchConfigurationArgs,
                    GraphVectorSearchConfigurationArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GraphArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        graph_name: Optional[pulumi.Input[_builtins.str]] = ...,
        graph_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_memory: Optional[pulumi.Input[_builtins.int]] = ...,
        public_connectivity: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[GraphTimeoutsArgs, GraphTimeoutsArgsDict]]
        ] = ...,
        vector_search_configuration: Optional[
            pulumi.Input[
                Union[
                    GraphVectorSearchConfigurationArgs,
                    GraphVectorSearchConfigurationArgsDict,
                ]
            ]
        ] = ...,
    ) -> Graph: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="graphName")
    def graph_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="graphNamePrefix")
    def graph_name_prefix(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedMemory")
    def provisioned_memory(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="publicConnectivity")
    def public_connectivity(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.GraphTimeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="vectorSearchConfiguration")
    def vector_search_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.GraphVectorSearchConfiguration]]: ...
