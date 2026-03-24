

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
__all__ = ['OriginRequestPolicyArgs', 'OriginRequestPolicy']
@pulumi.input_type
class OriginRequestPolicyArgs:
    def __init__(__self__, *, cookies_config: pulumi.Input[OriginRequestPolicyCookiesConfigArgs], headers_config: pulumi.Input[OriginRequestPolicyHeadersConfigArgs], query_strings_config: pulumi.Input[OriginRequestPolicyQueryStringsConfigArgs], comment: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cookiesConfig")
    def cookies_config(self) -> pulumi.Input[OriginRequestPolicyCookiesConfigArgs]:
        
        ...
    
    @cookies_config.setter
    def cookies_config(self, value: pulumi.Input[OriginRequestPolicyCookiesConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="headersConfig")
    def headers_config(self) -> pulumi.Input[OriginRequestPolicyHeadersConfigArgs]:
        
        ...
    
    @headers_config.setter
    def headers_config(self, value: pulumi.Input[OriginRequestPolicyHeadersConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringsConfig")
    def query_strings_config(self) -> pulumi.Input[OriginRequestPolicyQueryStringsConfigArgs]:
        
        ...
    
    @query_strings_config.setter
    def query_strings_config(self, value: pulumi.Input[OriginRequestPolicyQueryStringsConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _OriginRequestPolicyState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., cookies_config: Optional[pulumi.Input[OriginRequestPolicyCookiesConfigArgs]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., headers_config: Optional[pulumi.Input[OriginRequestPolicyHeadersConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., query_strings_config: Optional[pulumi.Input[OriginRequestPolicyQueryStringsConfigArgs]] = ...) -> None:
        
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
    @pulumi.getter(name="cookiesConfig")
    def cookies_config(self) -> Optional[pulumi.Input[OriginRequestPolicyCookiesConfigArgs]]:
        
        ...
    
    @cookies_config.setter
    def cookies_config(self, value: Optional[pulumi.Input[OriginRequestPolicyCookiesConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="headersConfig")
    def headers_config(self) -> Optional[pulumi.Input[OriginRequestPolicyHeadersConfigArgs]]:
        
        ...
    
    @headers_config.setter
    def headers_config(self, value: Optional[pulumi.Input[OriginRequestPolicyHeadersConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringsConfig")
    def query_strings_config(self) -> Optional[pulumi.Input[OriginRequestPolicyQueryStringsConfigArgs]]:
        
        ...
    
    @query_strings_config.setter
    def query_strings_config(self, value: Optional[pulumi.Input[OriginRequestPolicyQueryStringsConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class OriginRequestPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., cookies_config: Optional[pulumi.Input[Union[OriginRequestPolicyCookiesConfigArgs, OriginRequestPolicyCookiesConfigArgsDict]]] = ..., headers_config: Optional[pulumi.Input[Union[OriginRequestPolicyHeadersConfigArgs, OriginRequestPolicyHeadersConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., query_strings_config: Optional[pulumi.Input[Union[OriginRequestPolicyQueryStringsConfigArgs, OriginRequestPolicyQueryStringsConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: OriginRequestPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., cookies_config: Optional[pulumi.Input[Union[OriginRequestPolicyCookiesConfigArgs, OriginRequestPolicyCookiesConfigArgsDict]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., headers_config: Optional[pulumi.Input[Union[OriginRequestPolicyHeadersConfigArgs, OriginRequestPolicyHeadersConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., query_strings_config: Optional[pulumi.Input[Union[OriginRequestPolicyQueryStringsConfigArgs, OriginRequestPolicyQueryStringsConfigArgsDict]]] = ...) -> OriginRequestPolicy:
        
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
    @pulumi.getter(name="cookiesConfig")
    def cookies_config(self) -> pulumi.Output[outputs.OriginRequestPolicyCookiesConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headersConfig")
    def headers_config(self) -> pulumi.Output[outputs.OriginRequestPolicyHeadersConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringsConfig")
    def query_strings_config(self) -> pulumi.Output[outputs.OriginRequestPolicyQueryStringsConfig]:
        
        ...
    


