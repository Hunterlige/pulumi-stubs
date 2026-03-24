

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BasePathMappingArgs', 'BasePathMapping']
@pulumi.input_type
class BasePathMappingArgs:
    def __init__(__self__, *, domain_name: pulumi.Input[_builtins.str], rest_api: pulumi.Input[_builtins.str], base_path: Optional[pulumi.Input[_builtins.str]] = ..., domain_name_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., stage_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rest_api.setter
    def rest_api(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="basePath")
    def base_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @base_path.setter
    def base_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNameId")
    def domain_name_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name_id.setter
    def domain_name_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stage_name.setter
    def stage_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _BasePathMappingState:
    def __init__(__self__, *, base_path: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_name_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., stage_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basePath")
    def base_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @base_path.setter
    def base_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNameId")
    def domain_name_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name_id.setter
    def domain_name_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="stageName")
    def stage_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stage_name.setter
    def stage_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:apigateway/basePathMapping:BasePathMapping")
class BasePathMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., base_path: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_name_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., stage_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BasePathMappingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., base_path: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_name_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rest_api: Optional[pulumi.Input[_builtins.str]] = ..., stage_name: Optional[pulumi.Input[_builtins.str]] = ...) -> BasePathMapping:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basePath")
    def base_path(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNameId")
    def domain_name_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="stageName")
    def stage_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


