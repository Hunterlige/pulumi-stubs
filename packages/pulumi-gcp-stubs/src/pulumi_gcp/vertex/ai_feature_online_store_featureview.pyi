import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AiFeatureOnlineStoreFeatureviewArgs", "AiFeatureOnlineStoreFeatureview"]

@pulumi.input_type
class AiFeatureOnlineStoreFeatureviewArgs:
    def __init__(
        __self__,
        *,
        feature_online_store: pulumi.Input[_builtins.str],
        big_query_source: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewBigQuerySourceArgs]
        ] = ...,
        feature_registry_source: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sync_config: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewSyncConfigArgs]
        ] = ...,
        vector_search_config: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewVectorSearchConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="featureOnlineStore")
    def feature_online_store(self) -> pulumi.Input[_builtins.str]: ...
    @feature_online_store.setter
    def feature_online_store(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bigQuerySource")
    def big_query_source(
        self,
    ) -> Optional[pulumi.Input[AiFeatureOnlineStoreFeatureviewBigQuerySourceArgs]]: ...
    @big_query_source.setter
    def big_query_source(
        self,
        value: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewBigQuerySourceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="featureRegistrySource")
    def feature_registry_source(
        self,
    ) -> Optional[
        pulumi.Input[AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceArgs]
    ]: ...
    @feature_registry_source.setter
    def feature_registry_source(
        self,
        value: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="syncConfig")
    def sync_config(
        self,
    ) -> Optional[pulumi.Input[AiFeatureOnlineStoreFeatureviewSyncConfigArgs]]: ...
    @sync_config.setter
    def sync_config(
        self,
        value: Optional[pulumi.Input[AiFeatureOnlineStoreFeatureviewSyncConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vectorSearchConfig")
    def vector_search_config(
        self,
    ) -> Optional[
        pulumi.Input[AiFeatureOnlineStoreFeatureviewVectorSearchConfigArgs]
    ]: ...
    @vector_search_config.setter
    def vector_search_config(
        self,
        value: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewVectorSearchConfigArgs]
        ],
    ): ...

@pulumi.input_type
class _AiFeatureOnlineStoreFeatureviewState:
    def __init__(
        __self__,
        *,
        big_query_source: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewBigQuerySourceArgs]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        feature_online_store: Optional[pulumi.Input[_builtins.str]] = ...,
        feature_registry_source: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sync_config: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewSyncConfigArgs]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        vector_search_config: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewVectorSearchConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigQuerySource")
    def big_query_source(
        self,
    ) -> Optional[pulumi.Input[AiFeatureOnlineStoreFeatureviewBigQuerySourceArgs]]: ...
    @big_query_source.setter
    def big_query_source(
        self,
        value: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewBigQuerySourceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="featureOnlineStore")
    def feature_online_store(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @feature_online_store.setter
    def feature_online_store(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="featureRegistrySource")
    def feature_registry_source(
        self,
    ) -> Optional[
        pulumi.Input[AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceArgs]
    ]: ...
    @feature_registry_source.setter
    def feature_registry_source(
        self,
        value: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
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
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="syncConfig")
    def sync_config(
        self,
    ) -> Optional[pulumi.Input[AiFeatureOnlineStoreFeatureviewSyncConfigArgs]]: ...
    @sync_config.setter
    def sync_config(
        self,
        value: Optional[pulumi.Input[AiFeatureOnlineStoreFeatureviewSyncConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vectorSearchConfig")
    def vector_search_config(
        self,
    ) -> Optional[
        pulumi.Input[AiFeatureOnlineStoreFeatureviewVectorSearchConfigArgs]
    ]: ...
    @vector_search_config.setter
    def vector_search_config(
        self,
        value: Optional[
            pulumi.Input[AiFeatureOnlineStoreFeatureviewVectorSearchConfigArgs]
        ],
    ): ...

@pulumi.type_token(...)
class AiFeatureOnlineStoreFeatureview(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        big_query_source: Optional[
            pulumi.Input[
                Union[
                    AiFeatureOnlineStoreFeatureviewBigQuerySourceArgs,
                    AiFeatureOnlineStoreFeatureviewBigQuerySourceArgsDict,
                ]
            ]
        ] = ...,
        feature_online_store: Optional[pulumi.Input[_builtins.str]] = ...,
        feature_registry_source: Optional[
            pulumi.Input[
                Union[
                    AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceArgs,
                    AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceArgsDict,
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sync_config: Optional[
            pulumi.Input[
                Union[
                    AiFeatureOnlineStoreFeatureviewSyncConfigArgs,
                    AiFeatureOnlineStoreFeatureviewSyncConfigArgsDict,
                ]
            ]
        ] = ...,
        vector_search_config: Optional[
            pulumi.Input[
                Union[
                    AiFeatureOnlineStoreFeatureviewVectorSearchConfigArgs,
                    AiFeatureOnlineStoreFeatureviewVectorSearchConfigArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AiFeatureOnlineStoreFeatureviewArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        big_query_source: Optional[
            pulumi.Input[
                Union[
                    AiFeatureOnlineStoreFeatureviewBigQuerySourceArgs,
                    AiFeatureOnlineStoreFeatureviewBigQuerySourceArgsDict,
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        feature_online_store: Optional[pulumi.Input[_builtins.str]] = ...,
        feature_registry_source: Optional[
            pulumi.Input[
                Union[
                    AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceArgs,
                    AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceArgsDict,
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sync_config: Optional[
            pulumi.Input[
                Union[
                    AiFeatureOnlineStoreFeatureviewSyncConfigArgs,
                    AiFeatureOnlineStoreFeatureviewSyncConfigArgsDict,
                ]
            ]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        vector_search_config: Optional[
            pulumi.Input[
                Union[
                    AiFeatureOnlineStoreFeatureviewVectorSearchConfigArgs,
                    AiFeatureOnlineStoreFeatureviewVectorSearchConfigArgsDict,
                ]
            ]
        ] = ...,
    ) -> AiFeatureOnlineStoreFeatureview: ...
    @_builtins.property
    @pulumi.getter(name="bigQuerySource")
    def big_query_source(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AiFeatureOnlineStoreFeatureviewBigQuerySource]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="featureOnlineStore")
    def feature_online_store(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="featureRegistrySource")
    def feature_registry_source(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AiFeatureOnlineStoreFeatureviewFeatureRegistrySource]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncConfig")
    def sync_config(
        self,
    ) -> pulumi.Output[Optional[outputs.AiFeatureOnlineStoreFeatureviewSyncConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vectorSearchConfig")
    def vector_search_config(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AiFeatureOnlineStoreFeatureviewVectorSearchConfig]
    ]: ...
