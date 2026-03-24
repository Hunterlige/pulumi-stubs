

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FunctionUrlArgs', 'FunctionUrl']
@pulumi.input_type
class FunctionUrlArgs:
    def __init__(__self__, *, authorization_type: pulumi.Input[_builtins.str], function_name: pulumi.Input[_builtins.str], cors: Optional[pulumi.Input[FunctionUrlCorsArgs]] = ..., invoke_mode: Optional[pulumi.Input[_builtins.str]] = ..., qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authorization_type.setter
    def authorization_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @function_name.setter
    def function_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Optional[pulumi.Input[FunctionUrlCorsArgs]]:
        
        ...
    
    @cors.setter
    def cors(self, value: Optional[pulumi.Input[FunctionUrlCorsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokeMode")
    def invoke_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @invoke_mode.setter
    def invoke_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @qualifier.setter
    def qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _FunctionUrlState:
    def __init__(__self__, *, authorization_type: Optional[pulumi.Input[_builtins.str]] = ..., cors: Optional[pulumi.Input[FunctionUrlCorsArgs]] = ..., function_arn: Optional[pulumi.Input[_builtins.str]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., function_url: Optional[pulumi.Input[_builtins.str]] = ..., invoke_mode: Optional[pulumi.Input[_builtins.str]] = ..., qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., url_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_type.setter
    def authorization_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Optional[pulumi.Input[FunctionUrlCorsArgs]]:
        
        ...
    
    @cors.setter
    def cors(self, value: Optional[pulumi.Input[FunctionUrlCorsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_arn.setter
    def function_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_name.setter
    def function_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionUrl")
    def function_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_url.setter
    def function_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokeMode")
    def invoke_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @invoke_mode.setter
    def invoke_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @qualifier.setter
    def qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlId")
    def url_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @url_id.setter
    def url_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:lambda/functionUrl:FunctionUrl")
class FunctionUrl(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., authorization_type: Optional[pulumi.Input[_builtins.str]] = ..., cors: Optional[pulumi.Input[Union[FunctionUrlCorsArgs, FunctionUrlCorsArgsDict]]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., invoke_mode: Optional[pulumi.Input[_builtins.str]] = ..., qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FunctionUrlArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., authorization_type: Optional[pulumi.Input[_builtins.str]] = ..., cors: Optional[pulumi.Input[Union[FunctionUrlCorsArgs, FunctionUrlCorsArgsDict]]] = ..., function_arn: Optional[pulumi.Input[_builtins.str]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., function_url: Optional[pulumi.Input[_builtins.str]] = ..., invoke_mode: Optional[pulumi.Input[_builtins.str]] = ..., qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., url_id: Optional[pulumi.Input[_builtins.str]] = ...) -> FunctionUrl:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cors(self) -> pulumi.Output[Optional[outputs.FunctionUrlCors]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionUrl")
    def function_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokeMode")
    def invoke_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlId")
    def url_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


