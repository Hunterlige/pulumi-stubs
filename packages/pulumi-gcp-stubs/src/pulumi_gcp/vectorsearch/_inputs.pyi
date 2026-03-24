import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CollectionVectorSchemaArgs",
    "CollectionVectorSchemaArgsDict",
    "CollectionVectorSchemaDenseVectorArgs",
    "CollectionVectorSchemaDenseVectorArgsDict",
    ...,
    ...,
    "CollectionVectorSchemaSparseVectorArgs",
    "CollectionVectorSchemaSparseVectorArgsDict",
]

class CollectionVectorSchemaArgsDict(TypedDict):
    field_name: pulumi.Input[_builtins.str]
    dense_vector: NotRequired[pulumi.Input[CollectionVectorSchemaDenseVectorArgsDict]]
    sparse_vector: NotRequired[pulumi.Input[CollectionVectorSchemaSparseVectorArgsDict]]
    ...

@pulumi.input_type
class CollectionVectorSchemaArgs:
    def __init__(
        __self__,
        *,
        field_name: pulumi.Input[_builtins.str],
        dense_vector: Optional[
            pulumi.Input[CollectionVectorSchemaDenseVectorArgs]
        ] = ...,
        sparse_vector: Optional[
            pulumi.Input[CollectionVectorSchemaSparseVectorArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> pulumi.Input[_builtins.str]: ...
    @field_name.setter
    def field_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="denseVector")
    def dense_vector(
        self,
    ) -> Optional[pulumi.Input[CollectionVectorSchemaDenseVectorArgs]]: ...
    @dense_vector.setter
    def dense_vector(
        self, value: Optional[pulumi.Input[CollectionVectorSchemaDenseVectorArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparseVector")
    def sparse_vector(
        self,
    ) -> Optional[pulumi.Input[CollectionVectorSchemaSparseVectorArgs]]: ...
    @sparse_vector.setter
    def sparse_vector(
        self, value: Optional[pulumi.Input[CollectionVectorSchemaSparseVectorArgs]]
    ): ...

class CollectionVectorSchemaDenseVectorArgsDict(TypedDict):
    dimensions: NotRequired[pulumi.Input[_builtins.int]]
    vertex_embedding_config: NotRequired[
        pulumi.Input[CollectionVectorSchemaDenseVectorVertexEmbeddingConfigArgsDict]
    ]
    ...

@pulumi.input_type
class CollectionVectorSchemaDenseVectorArgs:
    def __init__(
        __self__,
        *,
        dimensions: Optional[pulumi.Input[_builtins.int]] = ...,
        vertex_embedding_config: Optional[
            pulumi.Input[CollectionVectorSchemaDenseVectorVertexEmbeddingConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="vertexEmbeddingConfig")
    def vertex_embedding_config(
        self,
    ) -> Optional[
        pulumi.Input[CollectionVectorSchemaDenseVectorVertexEmbeddingConfigArgs]
    ]: ...
    @vertex_embedding_config.setter
    def vertex_embedding_config(
        self,
        value: Optional[
            pulumi.Input[CollectionVectorSchemaDenseVectorVertexEmbeddingConfigArgs]
        ],
    ): ...

class CollectionVectorSchemaDenseVectorVertexEmbeddingConfigArgsDict(TypedDict):
    model_id: pulumi.Input[_builtins.str]
    task_type: pulumi.Input[_builtins.str]
    text_template: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class CollectionVectorSchemaDenseVectorVertexEmbeddingConfigArgs:
    def __init__(
        __self__,
        *,
        model_id: pulumi.Input[_builtins.str],
        task_type: pulumi.Input[_builtins.str],
        text_template: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> pulumi.Input[_builtins.str]: ...
    @model_id.setter
    def model_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]: ...
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="textTemplate")
    def text_template(self) -> pulumi.Input[_builtins.str]: ...
    @text_template.setter
    def text_template(self, value: pulumi.Input[_builtins.str]): ...

class CollectionVectorSchemaSparseVectorArgsDict(TypedDict): ...

@pulumi.input_type
class CollectionVectorSchemaSparseVectorArgs:
    def __init__(__self__) -> None: ...
