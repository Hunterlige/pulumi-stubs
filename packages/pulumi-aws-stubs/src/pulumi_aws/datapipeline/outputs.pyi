import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PipelineDefinitionParameterObject",
    "PipelineDefinitionParameterObjectAttribute",
    "PipelineDefinitionParameterValue",
    "PipelineDefinitionPipelineObject",
    "PipelineDefinitionPipelineObjectField",
    "GetPipelineDefinitionParameterObjectResult",
    ...,
    "GetPipelineDefinitionParameterValueResult",
    "GetPipelineDefinitionPipelineObjectResult",
    "GetPipelineDefinitionPipelineObjectFieldResult",
]

@pulumi.output_type
class PipelineDefinitionParameterObject(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        attributes: Optional[
            Sequence[outputs.PipelineDefinitionParameterObjectAttribute]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> Optional[Sequence[outputs.PipelineDefinitionParameterObjectAttribute]]: ...

@pulumi.output_type
class PipelineDefinitionParameterObjectAttribute(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, key: _builtins.str, string_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> _builtins.str: ...

@pulumi.output_type
class PipelineDefinitionParameterValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, id: _builtins.str, string_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> _builtins.str: ...

@pulumi.output_type
class PipelineDefinitionPipelineObject(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        fields: Optional[Sequence[outputs.PipelineDefinitionPipelineObjectField]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[Sequence[outputs.PipelineDefinitionPipelineObjectField]]: ...

@pulumi.output_type
class PipelineDefinitionPipelineObjectField(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        ref_value: Optional[_builtins.str] = ...,
        string_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="refValue")
    def ref_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetPipelineDefinitionParameterObjectResult(dict):
    def __init__(
        __self__,
        *,
        attributes: Sequence[
            outputs.GetPipelineDefinitionParameterObjectAttributeResult
        ],
        id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> Sequence[outputs.GetPipelineDefinitionParameterObjectAttributeResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class GetPipelineDefinitionParameterObjectAttributeResult(dict):
    def __init__(
        __self__, *, key: _builtins.str, string_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> _builtins.str: ...

@pulumi.output_type
class GetPipelineDefinitionParameterValueResult(dict):
    def __init__(
        __self__, *, id: _builtins.str, string_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> _builtins.str: ...

@pulumi.output_type
class GetPipelineDefinitionPipelineObjectResult(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        fields: Optional[
            Sequence[outputs.GetPipelineDefinitionPipelineObjectFieldResult]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[Sequence[outputs.GetPipelineDefinitionPipelineObjectFieldResult]]: ...

@pulumi.output_type
class GetPipelineDefinitionPipelineObjectFieldResult(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        ref_value: _builtins.str,
        string_value: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="refValue")
    def ref_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> _builtins.str: ...
