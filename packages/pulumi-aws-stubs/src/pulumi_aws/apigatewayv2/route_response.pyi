import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RouteResponseArgs", "RouteResponse"]

@pulumi.input_type
class RouteResponseArgs:
    def __init__(
        __self__,
        *,
        api_id: pulumi.Input[_builtins.str],
        route_id: pulumi.Input[_builtins.str],
        route_response_key: pulumi.Input[_builtins.str],
        model_selection_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        response_models: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]: ...
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="routeId")
    def route_id(self) -> pulumi.Input[_builtins.str]: ...
    @route_id.setter
    def route_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="routeResponseKey")
    def route_response_key(self) -> pulumi.Input[_builtins.str]: ...
    @route_response_key.setter
    def route_response_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="modelSelectionExpression")
    def model_selection_expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_selection_expression.setter
    def model_selection_expression(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="responseModels")
    def response_models(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @response_models.setter
    def response_models(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _RouteResponseState:
    def __init__(
        __self__,
        *,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        model_selection_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        response_models: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        route_id: Optional[pulumi.Input[_builtins.str]] = ...,
        route_response_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_id.setter
    def api_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelSelectionExpression")
    def model_selection_expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_selection_expression.setter
    def model_selection_expression(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="responseModels")
    def response_models(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @response_models.setter
    def response_models(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routeId")
    def route_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route_id.setter
    def route_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routeResponseKey")
    def route_response_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route_response_key.setter
    def route_response_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:apigatewayv2/routeResponse:RouteResponse")
class RouteResponse(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        model_selection_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        response_models: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        route_id: Optional[pulumi.Input[_builtins.str]] = ...,
        route_response_key: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RouteResponseArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        model_selection_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        response_models: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        route_id: Optional[pulumi.Input[_builtins.str]] = ...,
        route_response_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> RouteResponse: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelSelectionExpression")
    def model_selection_expression(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="responseModels")
    def response_models(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="routeId")
    def route_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routeResponseKey")
    def route_response_key(self) -> pulumi.Output[_builtins.str]: ...
