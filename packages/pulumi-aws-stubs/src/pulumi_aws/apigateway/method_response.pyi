

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MethodResponseArgs', 'MethodResponse']
@pulumi.input_type
class MethodResponseArgs:
    def __init__(__self__, *, http_method: pulumi.Input[_builtins.str], resource_id: pulumi.Input[_builtins.str], rest_api: pulumi.Input[_builtins.str], status_code: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., response_models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., response_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]] = ...) -> None:
        
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
    @pulumi.getter(name="statusCode")
    def status_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status_code.setter
    def status_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseModels")
    def response_models(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @response_models.setter
    def response_models(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseParameters")
    def response_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]:
        
        ...
    
    @response_parameters.setter
    def response_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]): # -> None:
        ...
    


@pulumi.input_type
class _MethodResponseState:
    def __init__(__self__, *, http_method: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., response_models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., response_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., status_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_method.setter
    def http_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseModels")
    def response_models(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @response_models.setter
    def response_models(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseParameters")
    def response_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]:
        
        ...
    
    @response_parameters.setter
    def response_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rest_api.setter
    def rest_api(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status_code.setter
    def status_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:apigateway/methodResponse:MethodResponse")
class MethodResponse(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., http_method: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., response_models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., response_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., status_code: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MethodResponseArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., http_method: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., response_models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., response_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.bool]]]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., status_code: Optional[pulumi.Input[_builtins.str]] = ...) -> MethodResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseModels")
    def response_models(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseParameters")
    def response_parameters(self) -> pulumi.Output[Optional[Mapping[str, _builtins.bool]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


