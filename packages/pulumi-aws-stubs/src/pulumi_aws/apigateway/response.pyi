

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ResponseArgs', 'Response']
@pulumi.input_type
class ResponseArgs:
    def __init__(__self__, *, response_type: pulumi.Input[_builtins.str], rest_api_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., response_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., response_templates: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., status_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseType")
    def response_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @response_type.setter
    def response_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rest_api_id.setter
    def rest_api_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseParameters")
    def response_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @response_parameters.setter
    def response_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseTemplates")
    def response_templates(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @response_templates.setter
    def response_templates(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status_code.setter
    def status_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ResponseState:
    def __init__(__self__, *, region: Optional[pulumi.Input[_builtins.str]] = ..., response_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., response_templates: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., response_type: Optional[pulumi.Input[_builtins.str]] = ..., rest_api_id: Optional[pulumi.Input[_builtins.str]] = ..., status_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseParameters")
    def response_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @response_parameters.setter
    def response_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseTemplates")
    def response_templates(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @response_templates.setter
    def response_templates(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseType")
    def response_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @response_type.setter
    def response_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rest_api_id.setter
    def rest_api_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status_code.setter
    def status_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:apigateway/response:Response")
class Response(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., response_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., response_templates: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., response_type: Optional[pulumi.Input[_builtins.str]] = ..., rest_api_id: Optional[pulumi.Input[_builtins.str]] = ..., status_code: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ResponseArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., response_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., response_templates: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., response_type: Optional[pulumi.Input[_builtins.str]] = ..., rest_api_id: Optional[pulumi.Input[_builtins.str]] = ..., status_code: Optional[pulumi.Input[_builtins.str]] = ...) -> Response:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseParameters")
    def response_parameters(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseTemplates")
    def response_templates(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseType")
    def response_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


