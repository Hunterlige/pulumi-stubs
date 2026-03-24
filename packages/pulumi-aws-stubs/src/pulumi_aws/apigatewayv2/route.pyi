

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RouteArgs', 'Route']
@pulumi.input_type
class RouteArgs:
    def __init__(__self__, *, api_id: pulumi.Input[_builtins.str], route_key: pulumi.Input[_builtins.str], api_key_required: Optional[pulumi.Input[_builtins.bool]] = ..., authorization_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., authorization_type: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_id: Optional[pulumi.Input[_builtins.str]] = ..., model_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., operation_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., request_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[RouteRequestParameterArgs]]]] = ..., route_response_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeKey")
    def route_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @route_key.setter
    def route_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyRequired")
    def api_key_required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @api_key_required.setter
    def api_key_required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationScopes")
    def authorization_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @authorization_scopes.setter
    def authorization_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_type.setter
    def authorization_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerId")
    def authorizer_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorizer_id.setter
    def authorizer_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSelectionExpression")
    def model_selection_expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_selection_expression.setter
    def model_selection_expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationName")
    def operation_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @operation_name.setter
    def operation_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestModels")
    def request_models(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @request_models.setter
    def request_models(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestParameters")
    def request_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RouteRequestParameterArgs]]]]:
        
        ...
    
    @request_parameters.setter
    def request_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RouteRequestParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeResponseSelectionExpression")
    def route_response_selection_expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_response_selection_expression.setter
    def route_response_selection_expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RouteState:
    def __init__(__self__, *, api_id: Optional[pulumi.Input[_builtins.str]] = ..., api_key_required: Optional[pulumi.Input[_builtins.bool]] = ..., authorization_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., authorization_type: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_id: Optional[pulumi.Input[_builtins.str]] = ..., model_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., operation_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., request_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[RouteRequestParameterArgs]]]] = ..., route_key: Optional[pulumi.Input[_builtins.str]] = ..., route_response_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_id.setter
    def api_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyRequired")
    def api_key_required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @api_key_required.setter
    def api_key_required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationScopes")
    def authorization_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @authorization_scopes.setter
    def authorization_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_type.setter
    def authorization_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerId")
    def authorizer_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorizer_id.setter
    def authorizer_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSelectionExpression")
    def model_selection_expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_selection_expression.setter
    def model_selection_expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationName")
    def operation_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @operation_name.setter
    def operation_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestModels")
    def request_models(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @request_models.setter
    def request_models(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestParameters")
    def request_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RouteRequestParameterArgs]]]]:
        
        ...
    
    @request_parameters.setter
    def request_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RouteRequestParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeKey")
    def route_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_key.setter
    def route_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeResponseSelectionExpression")
    def route_response_selection_expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_response_selection_expression.setter
    def route_response_selection_expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:apigatewayv2/route:Route")
class Route(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., api_key_required: Optional[pulumi.Input[_builtins.bool]] = ..., authorization_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., authorization_type: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_id: Optional[pulumi.Input[_builtins.str]] = ..., model_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., operation_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., request_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RouteRequestParameterArgs, RouteRequestParameterArgsDict]]]]] = ..., route_key: Optional[pulumi.Input[_builtins.str]] = ..., route_response_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RouteArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., api_key_required: Optional[pulumi.Input[_builtins.bool]] = ..., authorization_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., authorization_type: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_id: Optional[pulumi.Input[_builtins.str]] = ..., model_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., operation_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., request_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RouteRequestParameterArgs, RouteRequestParameterArgsDict]]]]] = ..., route_key: Optional[pulumi.Input[_builtins.str]] = ..., route_response_selection_expression: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[_builtins.str]] = ...) -> Route:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyRequired")
    def api_key_required(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationScopes")
    def authorization_scopes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerId")
    def authorizer_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSelectionExpression")
    def model_selection_expression(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationName")
    def operation_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestModels")
    def request_models(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestParameters")
    def request_parameters(self) -> pulumi.Output[Optional[Sequence[outputs.RouteRequestParameter]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeKey")
    def route_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeResponseSelectionExpression")
    def route_response_selection_expression(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


