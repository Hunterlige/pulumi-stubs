

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AiFeatureOnlineStoreArgs', 'AiFeatureOnlineStore']
@pulumi.input_type
class AiFeatureOnlineStoreArgs:
    def __init__(__self__, *, bigtable: Optional[pulumi.Input[AiFeatureOnlineStoreBigtableArgs]] = ..., dedicated_serving_endpoint: Optional[pulumi.Input[AiFeatureOnlineStoreDedicatedServingEndpointArgs]] = ..., embedding_management: Optional[pulumi.Input[AiFeatureOnlineStoreEmbeddingManagementArgs]] = ..., encryption_spec: Optional[pulumi.Input[AiFeatureOnlineStoreEncryptionSpecArgs]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., optimized: Optional[pulumi.Input[AiFeatureOnlineStoreOptimizedArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bigtable(self) -> Optional[pulumi.Input[AiFeatureOnlineStoreBigtableArgs]]:
        
        ...
    
    @bigtable.setter
    def bigtable(self, value: Optional[pulumi.Input[AiFeatureOnlineStoreBigtableArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedicatedServingEndpoint")
    def dedicated_serving_endpoint(self) -> Optional[pulumi.Input[AiFeatureOnlineStoreDedicatedServingEndpointArgs]]:
        
        ...
    
    @dedicated_serving_endpoint.setter
    def dedicated_serving_endpoint(self, value: Optional[pulumi.Input[AiFeatureOnlineStoreDedicatedServingEndpointArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="embeddingManagement")
    @_utilities.deprecated(...)
    def embedding_management(self) -> Optional[pulumi.Input[AiFeatureOnlineStoreEmbeddingManagementArgs]]:
        
        ...
    
    @embedding_management.setter
    def embedding_management(self, value: Optional[pulumi.Input[AiFeatureOnlineStoreEmbeddingManagementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(self) -> Optional[pulumi.Input[AiFeatureOnlineStoreEncryptionSpecArgs]]:
        
        ...
    
    @encryption_spec.setter
    def encryption_spec(self, value: Optional[pulumi.Input[AiFeatureOnlineStoreEncryptionSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def optimized(self) -> Optional[pulumi.Input[AiFeatureOnlineStoreOptimizedArgs]]:
        
        ...
    
    @optimized.setter
    def optimized(self, value: Optional[pulumi.Input[AiFeatureOnlineStoreOptimizedArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AiFeatureOnlineStoreState:
    def __init__(__self__, *, bigtable: Optional[pulumi.Input[AiFeatureOnlineStoreBigtableArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., dedicated_serving_endpoint: Optional[pulumi.Input[AiFeatureOnlineStoreDedicatedServingEndpointArgs]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., embedding_management: Optional[pulumi.Input[AiFeatureOnlineStoreEmbeddingManagementArgs]] = ..., encryption_spec: Optional[pulumi.Input[AiFeatureOnlineStoreEncryptionSpecArgs]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., optimized: Optional[pulumi.Input[AiFeatureOnlineStoreOptimizedArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bigtable(self) -> Optional[pulumi.Input[AiFeatureOnlineStoreBigtableArgs]]:
        
        ...
    
    @bigtable.setter
    def bigtable(self, value: Optional[pulumi.Input[AiFeatureOnlineStoreBigtableArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedicatedServingEndpoint")
    def dedicated_serving_endpoint(self) -> Optional[pulumi.Input[AiFeatureOnlineStoreDedicatedServingEndpointArgs]]:
        
        ...
    
    @dedicated_serving_endpoint.setter
    def dedicated_serving_endpoint(self, value: Optional[pulumi.Input[AiFeatureOnlineStoreDedicatedServingEndpointArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="embeddingManagement")
    @_utilities.deprecated(...)
    def embedding_management(self) -> Optional[pulumi.Input[AiFeatureOnlineStoreEmbeddingManagementArgs]]:
        
        ...
    
    @embedding_management.setter
    def embedding_management(self, value: Optional[pulumi.Input[AiFeatureOnlineStoreEmbeddingManagementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(self) -> Optional[pulumi.Input[AiFeatureOnlineStoreEncryptionSpecArgs]]:
        
        ...
    
    @encryption_spec.setter
    def encryption_spec(self, value: Optional[pulumi.Input[AiFeatureOnlineStoreEncryptionSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def optimized(self) -> Optional[pulumi.Input[AiFeatureOnlineStoreOptimizedArgs]]:
        
        ...
    
    @optimized.setter
    def optimized(self, value: Optional[pulumi.Input[AiFeatureOnlineStoreOptimizedArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AiFeatureOnlineStore(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bigtable: Optional[pulumi.Input[Union[AiFeatureOnlineStoreBigtableArgs, AiFeatureOnlineStoreBigtableArgsDict]]] = ..., dedicated_serving_endpoint: Optional[pulumi.Input[Union[AiFeatureOnlineStoreDedicatedServingEndpointArgs, AiFeatureOnlineStoreDedicatedServingEndpointArgsDict]]] = ..., embedding_management: Optional[pulumi.Input[Union[AiFeatureOnlineStoreEmbeddingManagementArgs, AiFeatureOnlineStoreEmbeddingManagementArgsDict]]] = ..., encryption_spec: Optional[pulumi.Input[Union[AiFeatureOnlineStoreEncryptionSpecArgs, AiFeatureOnlineStoreEncryptionSpecArgsDict]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., optimized: Optional[pulumi.Input[Union[AiFeatureOnlineStoreOptimizedArgs, AiFeatureOnlineStoreOptimizedArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[AiFeatureOnlineStoreArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bigtable: Optional[pulumi.Input[Union[AiFeatureOnlineStoreBigtableArgs, AiFeatureOnlineStoreBigtableArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., dedicated_serving_endpoint: Optional[pulumi.Input[Union[AiFeatureOnlineStoreDedicatedServingEndpointArgs, AiFeatureOnlineStoreDedicatedServingEndpointArgsDict]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., embedding_management: Optional[pulumi.Input[Union[AiFeatureOnlineStoreEmbeddingManagementArgs, AiFeatureOnlineStoreEmbeddingManagementArgsDict]]] = ..., encryption_spec: Optional[pulumi.Input[Union[AiFeatureOnlineStoreEncryptionSpecArgs, AiFeatureOnlineStoreEncryptionSpecArgsDict]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., optimized: Optional[pulumi.Input[Union[AiFeatureOnlineStoreOptimizedArgs, AiFeatureOnlineStoreOptimizedArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> AiFeatureOnlineStore:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bigtable(self) -> pulumi.Output[Optional[outputs.AiFeatureOnlineStoreBigtable]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedicatedServingEndpoint")
    def dedicated_serving_endpoint(self) -> pulumi.Output[outputs.AiFeatureOnlineStoreDedicatedServingEndpoint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="embeddingManagement")
    @_utilities.deprecated(...)
    def embedding_management(self) -> pulumi.Output[outputs.AiFeatureOnlineStoreEmbeddingManagement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(self) -> pulumi.Output[Optional[outputs.AiFeatureOnlineStoreEncryptionSpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def optimized(self) -> pulumi.Output[Optional[outputs.AiFeatureOnlineStoreOptimized]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


