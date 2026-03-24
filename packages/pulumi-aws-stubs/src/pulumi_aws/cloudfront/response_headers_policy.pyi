

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
__all__ = ['ResponseHeadersPolicyArgs', 'ResponseHeadersPolicy']
@pulumi.input_type
class ResponseHeadersPolicyArgs:
    def __init__(__self__, *, comment: Optional[pulumi.Input[_builtins.str]] = ..., cors_config: Optional[pulumi.Input[ResponseHeadersPolicyCorsConfigArgs]] = ..., custom_headers_config: Optional[pulumi.Input[ResponseHeadersPolicyCustomHeadersConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., remove_headers_config: Optional[pulumi.Input[ResponseHeadersPolicyRemoveHeadersConfigArgs]] = ..., security_headers_config: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigArgs]] = ..., server_timing_headers_config: Optional[pulumi.Input[ResponseHeadersPolicyServerTimingHeadersConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsConfig")
    def cors_config(self) -> Optional[pulumi.Input[ResponseHeadersPolicyCorsConfigArgs]]:
        
        ...
    
    @cors_config.setter
    def cors_config(self, value: Optional[pulumi.Input[ResponseHeadersPolicyCorsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHeadersConfig")
    def custom_headers_config(self) -> Optional[pulumi.Input[ResponseHeadersPolicyCustomHeadersConfigArgs]]:
        
        ...
    
    @custom_headers_config.setter
    def custom_headers_config(self, value: Optional[pulumi.Input[ResponseHeadersPolicyCustomHeadersConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="removeHeadersConfig")
    def remove_headers_config(self) -> Optional[pulumi.Input[ResponseHeadersPolicyRemoveHeadersConfigArgs]]:
        
        ...
    
    @remove_headers_config.setter
    def remove_headers_config(self, value: Optional[pulumi.Input[ResponseHeadersPolicyRemoveHeadersConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityHeadersConfig")
    def security_headers_config(self) -> Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigArgs]]:
        
        ...
    
    @security_headers_config.setter
    def security_headers_config(self, value: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverTimingHeadersConfig")
    def server_timing_headers_config(self) -> Optional[pulumi.Input[ResponseHeadersPolicyServerTimingHeadersConfigArgs]]:
        
        ...
    
    @server_timing_headers_config.setter
    def server_timing_headers_config(self, value: Optional[pulumi.Input[ResponseHeadersPolicyServerTimingHeadersConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ResponseHeadersPolicyState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., cors_config: Optional[pulumi.Input[ResponseHeadersPolicyCorsConfigArgs]] = ..., custom_headers_config: Optional[pulumi.Input[ResponseHeadersPolicyCustomHeadersConfigArgs]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., remove_headers_config: Optional[pulumi.Input[ResponseHeadersPolicyRemoveHeadersConfigArgs]] = ..., security_headers_config: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigArgs]] = ..., server_timing_headers_config: Optional[pulumi.Input[ResponseHeadersPolicyServerTimingHeadersConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsConfig")
    def cors_config(self) -> Optional[pulumi.Input[ResponseHeadersPolicyCorsConfigArgs]]:
        
        ...
    
    @cors_config.setter
    def cors_config(self, value: Optional[pulumi.Input[ResponseHeadersPolicyCorsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHeadersConfig")
    def custom_headers_config(self) -> Optional[pulumi.Input[ResponseHeadersPolicyCustomHeadersConfigArgs]]:
        
        ...
    
    @custom_headers_config.setter
    def custom_headers_config(self, value: Optional[pulumi.Input[ResponseHeadersPolicyCustomHeadersConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="removeHeadersConfig")
    def remove_headers_config(self) -> Optional[pulumi.Input[ResponseHeadersPolicyRemoveHeadersConfigArgs]]:
        
        ...
    
    @remove_headers_config.setter
    def remove_headers_config(self, value: Optional[pulumi.Input[ResponseHeadersPolicyRemoveHeadersConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityHeadersConfig")
    def security_headers_config(self) -> Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigArgs]]:
        
        ...
    
    @security_headers_config.setter
    def security_headers_config(self, value: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverTimingHeadersConfig")
    def server_timing_headers_config(self) -> Optional[pulumi.Input[ResponseHeadersPolicyServerTimingHeadersConfigArgs]]:
        
        ...
    
    @server_timing_headers_config.setter
    def server_timing_headers_config(self, value: Optional[pulumi.Input[ResponseHeadersPolicyServerTimingHeadersConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ResponseHeadersPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., cors_config: Optional[pulumi.Input[Union[ResponseHeadersPolicyCorsConfigArgs, ResponseHeadersPolicyCorsConfigArgsDict]]] = ..., custom_headers_config: Optional[pulumi.Input[Union[ResponseHeadersPolicyCustomHeadersConfigArgs, ResponseHeadersPolicyCustomHeadersConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., remove_headers_config: Optional[pulumi.Input[Union[ResponseHeadersPolicyRemoveHeadersConfigArgs, ResponseHeadersPolicyRemoveHeadersConfigArgsDict]]] = ..., security_headers_config: Optional[pulumi.Input[Union[ResponseHeadersPolicySecurityHeadersConfigArgs, ResponseHeadersPolicySecurityHeadersConfigArgsDict]]] = ..., server_timing_headers_config: Optional[pulumi.Input[Union[ResponseHeadersPolicyServerTimingHeadersConfigArgs, ResponseHeadersPolicyServerTimingHeadersConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ResponseHeadersPolicyArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., cors_config: Optional[pulumi.Input[Union[ResponseHeadersPolicyCorsConfigArgs, ResponseHeadersPolicyCorsConfigArgsDict]]] = ..., custom_headers_config: Optional[pulumi.Input[Union[ResponseHeadersPolicyCustomHeadersConfigArgs, ResponseHeadersPolicyCustomHeadersConfigArgsDict]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., remove_headers_config: Optional[pulumi.Input[Union[ResponseHeadersPolicyRemoveHeadersConfigArgs, ResponseHeadersPolicyRemoveHeadersConfigArgsDict]]] = ..., security_headers_config: Optional[pulumi.Input[Union[ResponseHeadersPolicySecurityHeadersConfigArgs, ResponseHeadersPolicySecurityHeadersConfigArgsDict]]] = ..., server_timing_headers_config: Optional[pulumi.Input[Union[ResponseHeadersPolicyServerTimingHeadersConfigArgs, ResponseHeadersPolicyServerTimingHeadersConfigArgsDict]]] = ...) -> ResponseHeadersPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsConfig")
    def cors_config(self) -> pulumi.Output[Optional[outputs.ResponseHeadersPolicyCorsConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHeadersConfig")
    def custom_headers_config(self) -> pulumi.Output[Optional[outputs.ResponseHeadersPolicyCustomHeadersConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="removeHeadersConfig")
    def remove_headers_config(self) -> pulumi.Output[Optional[outputs.ResponseHeadersPolicyRemoveHeadersConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityHeadersConfig")
    def security_headers_config(self) -> pulumi.Output[Optional[outputs.ResponseHeadersPolicySecurityHeadersConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverTimingHeadersConfig")
    def server_timing_headers_config(self) -> pulumi.Output[Optional[outputs.ResponseHeadersPolicyServerTimingHeadersConfig]]:
        
        ...
    


