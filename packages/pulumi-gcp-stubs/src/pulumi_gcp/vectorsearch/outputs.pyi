

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CollectionVectorSchema', 'CollectionVectorSchemaDenseVector', ..., 'CollectionVectorSchemaSparseVector']
@pulumi.output_type
class CollectionVectorSchema(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, field_name: _builtins.str, dense_vector: Optional[outputs.CollectionVectorSchemaDenseVector] = ..., sparse_vector: Optional[outputs.CollectionVectorSchemaSparseVector] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="denseVector")
    def dense_vector(self) -> Optional[outputs.CollectionVectorSchemaDenseVector]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparseVector")
    def sparse_vector(self) -> Optional[outputs.CollectionVectorSchemaSparseVector]:
        
        ...
    


@pulumi.output_type
class CollectionVectorSchemaDenseVector(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dimensions: Optional[_builtins.int] = ..., vertex_embedding_config: Optional[outputs.CollectionVectorSchemaDenseVectorVertexEmbeddingConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vertexEmbeddingConfig")
    def vertex_embedding_config(self) -> Optional[outputs.CollectionVectorSchemaDenseVectorVertexEmbeddingConfig]:
        
        ...
    


@pulumi.output_type
class CollectionVectorSchemaDenseVectorVertexEmbeddingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, model_id: _builtins.str, task_type: _builtins.str, text_template: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTemplate")
    def text_template(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CollectionVectorSchemaSparseVector(dict):
    def __init__(__self__) -> None:
        ...
    


