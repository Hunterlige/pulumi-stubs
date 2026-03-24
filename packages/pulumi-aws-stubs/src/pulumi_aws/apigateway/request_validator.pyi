

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RequestValidatorArgs', 'RequestValidator']
@pulumi.input_type
class RequestValidatorArgs:
    def __init__(__self__, *, rest_api: pulumi.Input[_builtins.str], name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., validate_request_body: Optional[pulumi.Input[_builtins.bool]] = ..., validate_request_parameters: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rest_api.setter
    def rest_api(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateRequestBody")
    def validate_request_body(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @validate_request_body.setter
    def validate_request_body(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateRequestParameters")
    def validate_request_parameters(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @validate_request_parameters.setter
    def validate_request_parameters(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _RequestValidatorState:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., validate_request_body: Optional[pulumi.Input[_builtins.bool]] = ..., validate_request_parameters: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rest_api.setter
    def rest_api(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateRequestBody")
    def validate_request_body(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @validate_request_body.setter
    def validate_request_body(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateRequestParameters")
    def validate_request_parameters(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @validate_request_parameters.setter
    def validate_request_parameters(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("aws:apigateway/requestValidator:RequestValidator")
class RequestValidator(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., validate_request_body: Optional[pulumi.Input[_builtins.bool]] = ..., validate_request_parameters: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RequestValidatorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., validate_request_body: Optional[pulumi.Input[_builtins.bool]] = ..., validate_request_parameters: Optional[pulumi.Input[_builtins.bool]] = ...) -> RequestValidator:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateRequestBody")
    def validate_request_body(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateRequestParameters")
    def validate_request_parameters(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


