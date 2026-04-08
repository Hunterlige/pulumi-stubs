import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PipelineDefinitionParameterObjectArgs",
    "PipelineDefinitionParameterObjectArgsDict",
    "PipelineDefinitionParameterObjectAttributeArgs",
    "PipelineDefinitionParameterObjectAttributeArgsDict",
    "PipelineDefinitionParameterValueArgs",
    "PipelineDefinitionParameterValueArgsDict",
    "PipelineDefinitionPipelineObjectArgs",
    "PipelineDefinitionPipelineObjectArgsDict",
    "PipelineDefinitionPipelineObjectFieldArgs",
    "PipelineDefinitionPipelineObjectFieldArgsDict",
    "GetPipelineDefinitionParameterValueArgs",
    "GetPipelineDefinitionParameterValueArgsDict",
]

class PipelineDefinitionParameterObjectArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    attributes: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PipelineDefinitionParameterObjectAttributeArgsDict]]
        ]
    ]

@pulumi.input_type
class PipelineDefinitionParameterObjectArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        attributes: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipelineDefinitionParameterObjectAttributeArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PipelineDefinitionParameterObjectAttributeArgs]]
        ]
    ]: ...
    @attributes.setter
    def attributes(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipelineDefinitionParameterObjectAttributeArgs]]
            ]
        ],
    ): ...

class PipelineDefinitionParameterObjectAttributeArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    string_value: pulumi.Input[_builtins.str]

@pulumi.input_type
class PipelineDefinitionParameterObjectAttributeArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        string_value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> pulumi.Input[_builtins.str]: ...
    @string_value.setter
    def string_value(self, value: pulumi.Input[_builtins.str]): ...

class PipelineDefinitionParameterValueArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    string_value: pulumi.Input[_builtins.str]

@pulumi.input_type
class PipelineDefinitionParameterValueArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        string_value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> pulumi.Input[_builtins.str]: ...
    @string_value.setter
    def string_value(self, value: pulumi.Input[_builtins.str]): ...

class PipelineDefinitionPipelineObjectArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    fields: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PipelineDefinitionPipelineObjectFieldArgsDict]]
        ]
    ]

@pulumi.input_type
class PipelineDefinitionPipelineObjectArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        fields: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipelineDefinitionPipelineObjectFieldArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PipelineDefinitionPipelineObjectFieldArgs]]]
    ]: ...
    @fields.setter
    def fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PipelineDefinitionPipelineObjectFieldArgs]]
            ]
        ],
    ): ...

class PipelineDefinitionPipelineObjectFieldArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    ref_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PipelineDefinitionPipelineObjectFieldArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        ref_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="refValue")
    def ref_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ref_value.setter
    def ref_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GetPipelineDefinitionParameterValueArgsDict(TypedDict):
    id: _builtins.str
    string_value: _builtins.str

@pulumi.input_type
class GetPipelineDefinitionParameterValueArgs:
    def __init__(
        __self__, *, id: _builtins.str, string_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @id.setter
    def id(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> _builtins.str: ...
    @string_value.setter
    def string_value(self, value: _builtins.str): ...
