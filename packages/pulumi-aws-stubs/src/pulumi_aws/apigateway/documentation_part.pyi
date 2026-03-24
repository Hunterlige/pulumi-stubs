import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DocumentationPartArgs", "DocumentationPart"]

@pulumi.input_type
class DocumentationPartArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[DocumentationPartLocationArgs],
        properties: pulumi.Input[_builtins.str],
        rest_api_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[DocumentationPartLocationArgs]: ...
    @location.setter
    def location(self, value: pulumi.Input[DocumentationPartLocationArgs]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[_builtins.str]: ...
    @properties.setter
    def properties(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Input[_builtins.str]: ...
    @rest_api_id.setter
    def rest_api_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _DocumentationPartState:
    def __init__(
        __self__,
        *,
        documentation_part_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[DocumentationPartLocationArgs]] = ...,
        properties: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rest_api_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="documentationPartId")
    def documentation_part_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @documentation_part_id.setter
    def documentation_part_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[DocumentationPartLocationArgs]]: ...
    @location.setter
    def location(
        self, value: Optional[pulumi.Input[DocumentationPartLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rest_api_id.setter
    def rest_api_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:apigateway/documentationPart:DocumentationPart")
class DocumentationPart(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        location: Optional[
            pulumi.Input[
                Union[DocumentationPartLocationArgs, DocumentationPartLocationArgsDict]
            ]
        ] = ...,
        properties: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rest_api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DocumentationPartArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        documentation_part_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[
            pulumi.Input[
                Union[DocumentationPartLocationArgs, DocumentationPartLocationArgsDict]
            ]
        ] = ...,
        properties: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rest_api_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> DocumentationPart: ...
    @_builtins.property
    @pulumi.getter(name="documentationPartId")
    def documentation_part_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[outputs.DocumentationPartLocation]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Output[_builtins.str]: ...
