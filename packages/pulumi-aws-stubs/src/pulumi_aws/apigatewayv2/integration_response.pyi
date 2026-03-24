import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IntegrationResponseArgs", "IntegrationResponse"]

@pulumi.input_type
class IntegrationResponseArgs:
    def __init__(
        __self__,
        *,
        api_id: pulumi.Input[_builtins.str],
        integration_id: pulumi.Input[_builtins.str],
        integration_response_key: pulumi.Input[_builtins.str],
        content_handling_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        response_templates: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        template_selection_expression: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]: ...
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="integrationId")
    def integration_id(self) -> pulumi.Input[_builtins.str]: ...
    @integration_id.setter
    def integration_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="integrationResponseKey")
    def integration_response_key(self) -> pulumi.Input[_builtins.str]: ...
    @integration_response_key.setter
    def integration_response_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="contentHandlingStrategy")
    def content_handling_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_handling_strategy.setter
    def content_handling_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="responseTemplates")
    def response_templates(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @response_templates.setter
    def response_templates(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="templateSelectionExpression")
    def template_selection_expression(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_selection_expression.setter
    def template_selection_expression(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _IntegrationResponseState:
    def __init__(
        __self__,
        *,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        content_handling_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        integration_id: Optional[pulumi.Input[_builtins.str]] = ...,
        integration_response_key: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        response_templates: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        template_selection_expression: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_id.setter
    def api_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contentHandlingStrategy")
    def content_handling_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_handling_strategy.setter
    def content_handling_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="integrationId")
    def integration_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integration_id.setter
    def integration_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="integrationResponseKey")
    def integration_response_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integration_response_key.setter
    def integration_response_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="responseTemplates")
    def response_templates(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @response_templates.setter
    def response_templates(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="templateSelectionExpression")
    def template_selection_expression(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_selection_expression.setter
    def template_selection_expression(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token(...)
class IntegrationResponse(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        content_handling_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        integration_id: Optional[pulumi.Input[_builtins.str]] = ...,
        integration_response_key: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        response_templates: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        template_selection_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IntegrationResponseArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        content_handling_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        integration_id: Optional[pulumi.Input[_builtins.str]] = ...,
        integration_response_key: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        response_templates: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        template_selection_expression: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> IntegrationResponse: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentHandlingStrategy")
    def content_handling_strategy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="integrationId")
    def integration_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="integrationResponseKey")
    def integration_response_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="responseTemplates")
    def response_templates(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="templateSelectionExpression")
    def template_selection_expression(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
