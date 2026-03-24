

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MethodArgs', 'Method']
@pulumi.input_type
class MethodArgs:
    def __init__(__self__, *, authorization: pulumi.Input[_builtins.str], http_method: pulumi.Input[_builtins.str], resource_id: pulumi.Input[_builtins.str], rest_api: pulumi.Input[_builtins.str], api_key_required: Optional[pulumi.Input[_builtins.bool]] = ..., authorization_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., authorizer_id: Optional[pulumi.Input[_builtins.str]] = ..., operation_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., request_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]] = ..., request_validator_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authorization.setter
    def authorization(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @http_method.setter
    def http_method(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rest_api.setter
    def rest_api(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    @pulumi.getter(name="authorizerId")
    def authorizer_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorizer_id.setter
    def authorizer_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def request_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]:
        
        ...
    
    @request_parameters.setter
    def request_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestValidatorId")
    def request_validator_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_validator_id.setter
    def request_validator_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _MethodState:
    def __init__(__self__, *, api_key_required: Optional[pulumi.Input[_builtins.bool]] = ..., authorization: Optional[pulumi.Input[_builtins.str]] = ..., authorization_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., authorizer_id: Optional[pulumi.Input[_builtins.str]] = ..., http_method: Optional[pulumi.Input[_builtins.str]] = ..., operation_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., request_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]] = ..., request_validator_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyRequired")
    def api_key_required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @api_key_required.setter
    def api_key_required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization.setter
    def authorization(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationScopes")
    def authorization_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @authorization_scopes.setter
    def authorization_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerId")
    def authorizer_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorizer_id.setter
    def authorizer_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_method.setter
    def http_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def request_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]:
        
        ...
    
    @request_parameters.setter
    def request_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestValidatorId")
    def request_validator_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_validator_id.setter
    def request_validator_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rest_api.setter
    def rest_api(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:apigateway/method:Method")
class Method(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api_key_required: Optional[pulumi.Input[_builtins.bool]] = ..., authorization: Optional[pulumi.Input[_builtins.str]] = ..., authorization_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., authorizer_id: Optional[pulumi.Input[_builtins.str]] = ..., http_method: Optional[pulumi.Input[_builtins.str]] = ..., operation_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., request_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]] = ..., request_validator_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MethodArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., api_key_required: Optional[pulumi.Input[_builtins.bool]] = ..., authorization: Optional[pulumi.Input[_builtins.str]] = ..., authorization_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., authorizer_id: Optional[pulumi.Input[_builtins.str]] = ..., http_method: Optional[pulumi.Input[_builtins.str]] = ..., operation_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., request_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]] = ..., request_validator_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ...) -> Method:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyRequired")
    def api_key_required(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationScopes")
    def authorization_scopes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerId")
    def authorizer_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> pulumi.Output[_builtins.str]:
        
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
    def request_parameters(self) -> pulumi.Output[Optional[Mapping[str, _builtins.bool]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestValidatorId")
    def request_validator_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


