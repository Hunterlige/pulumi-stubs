import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DocumentAiWarehouseDocumentSchemaArgs", "DocumentAiWarehouseDocumentSchema"]

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        project_number: pulumi.Input[_builtins.str],
        property_definitions: pulumi.Input[
            Sequence[
                pulumi.Input[DocumentAiWarehouseDocumentSchemaPropertyDefinitionArgs]
            ]
        ],
        document_is_folder: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> pulumi.Input[_builtins.str]: ...
    @project_number.setter
    def project_number(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="propertyDefinitions")
    def property_definitions(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[DocumentAiWarehouseDocumentSchemaPropertyDefinitionArgs]]
    ]: ...
    @property_definitions.setter
    def property_definitions(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[DocumentAiWarehouseDocumentSchemaPropertyDefinitionArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="documentIsFolder")
    def document_is_folder(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @document_is_folder.setter
    def document_is_folder(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _DocumentAiWarehouseDocumentSchemaState:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        document_is_folder: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project_number: Optional[pulumi.Input[_builtins.str]] = ...,
        property_definitions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DocumentAiWarehouseDocumentSchemaPropertyDefinitionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="documentIsFolder")
    def document_is_folder(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @document_is_folder.setter
    def document_is_folder(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_number.setter
    def project_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="propertyDefinitions")
    def property_definitions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[DocumentAiWarehouseDocumentSchemaPropertyDefinitionArgs]
            ]
        ]
    ]: ...
    @property_definitions.setter
    def property_definitions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DocumentAiWarehouseDocumentSchemaPropertyDefinitionArgs
                    ]
                ]
            ]
        ],
    ): ...

@pulumi.type_token(...)
class DocumentAiWarehouseDocumentSchema(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        document_is_folder: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project_number: Optional[pulumi.Input[_builtins.str]] = ...,
        property_definitions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DocumentAiWarehouseDocumentSchemaPropertyDefinitionArgs,
                            DocumentAiWarehouseDocumentSchemaPropertyDefinitionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DocumentAiWarehouseDocumentSchemaArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        document_is_folder: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project_number: Optional[pulumi.Input[_builtins.str]] = ...,
        property_definitions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DocumentAiWarehouseDocumentSchemaPropertyDefinitionArgs,
                            DocumentAiWarehouseDocumentSchemaPropertyDefinitionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> DocumentAiWarehouseDocumentSchema: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentIsFolder")
    def document_is_folder(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertyDefinitions")
    def property_definitions(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinition]
    ]: ...
