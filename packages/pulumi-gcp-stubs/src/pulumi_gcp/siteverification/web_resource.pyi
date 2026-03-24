

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WebResourceArgs', 'WebResource']
@pulumi.input_type
class WebResourceArgs:
    def __init__(__self__, *, site: pulumi.Input[WebResourceSiteArgs], verification_method: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def site(self) -> pulumi.Input[WebResourceSiteArgs]:
        
        ...
    
    @site.setter
    def site(self, value: pulumi.Input[WebResourceSiteArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verificationMethod")
    def verification_method(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @verification_method.setter
    def verification_method(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _WebResourceState:
    def __init__(__self__, *, owners: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., site: Optional[pulumi.Input[WebResourceSiteArgs]] = ..., verification_method: Optional[pulumi.Input[_builtins.str]] = ..., web_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @owners.setter
    def owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def site(self) -> Optional[pulumi.Input[WebResourceSiteArgs]]:
        
        ...
    
    @site.setter
    def site(self, value: Optional[pulumi.Input[WebResourceSiteArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verificationMethod")
    def verification_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @verification_method.setter
    def verification_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webResourceId")
    def web_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @web_resource_id.setter
    def web_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:siteverification/webResource:WebResource")
class WebResource(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., site: Optional[pulumi.Input[Union[WebResourceSiteArgs, WebResourceSiteArgsDict]]] = ..., verification_method: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WebResourceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., owners: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., site: Optional[pulumi.Input[Union[WebResourceSiteArgs, WebResourceSiteArgsDict]]] = ..., verification_method: Optional[pulumi.Input[_builtins.str]] = ..., web_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> WebResource:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owners(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def site(self) -> pulumi.Output[outputs.WebResourceSite]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verificationMethod")
    def verification_method(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webResourceId")
    def web_resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


