

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
__all__ = ['WebAppArgs', 'WebApp']
@pulumi.input_type
class WebAppArgs:
    def __init__(__self__, *, identity_provider_details: pulumi.Input[WebAppIdentityProviderDetailsArgs], access_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_details: Optional[pulumi.Input[WebAppEndpointDetailsArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., web_app_endpoint_policy: Optional[pulumi.Input[_builtins.str]] = ..., web_app_units: Optional[pulumi.Input[Sequence[pulumi.Input[WebAppWebAppUnitArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityProviderDetails")
    def identity_provider_details(self) -> pulumi.Input[WebAppIdentityProviderDetailsArgs]:
        
        ...
    
    @identity_provider_details.setter
    def identity_provider_details(self, value: pulumi.Input[WebAppIdentityProviderDetailsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessEndpoint")
    def access_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_endpoint.setter
    def access_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointDetails")
    def endpoint_details(self) -> Optional[pulumi.Input[WebAppEndpointDetailsArgs]]:
        
        ...
    
    @endpoint_details.setter
    def endpoint_details(self, value: Optional[pulumi.Input[WebAppEndpointDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAppEndpointPolicy")
    def web_app_endpoint_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @web_app_endpoint_policy.setter
    def web_app_endpoint_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAppUnits")
    def web_app_units(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WebAppWebAppUnitArgs]]]]:
        
        ...
    
    @web_app_units.setter
    def web_app_units(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WebAppWebAppUnitArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _WebAppState:
    def __init__(__self__, *, access_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_details: Optional[pulumi.Input[WebAppEndpointDetailsArgs]] = ..., identity_provider_details: Optional[pulumi.Input[WebAppIdentityProviderDetailsArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., web_app_endpoint_policy: Optional[pulumi.Input[_builtins.str]] = ..., web_app_id: Optional[pulumi.Input[_builtins.str]] = ..., web_app_units: Optional[pulumi.Input[Sequence[pulumi.Input[WebAppWebAppUnitArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessEndpoint")
    def access_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_endpoint.setter
    def access_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointDetails")
    def endpoint_details(self) -> Optional[pulumi.Input[WebAppEndpointDetailsArgs]]:
        
        ...
    
    @endpoint_details.setter
    def endpoint_details(self, value: Optional[pulumi.Input[WebAppEndpointDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityProviderDetails")
    def identity_provider_details(self) -> Optional[pulumi.Input[WebAppIdentityProviderDetailsArgs]]:
        
        ...
    
    @identity_provider_details.setter
    def identity_provider_details(self, value: Optional[pulumi.Input[WebAppIdentityProviderDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAppEndpointPolicy")
    def web_app_endpoint_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @web_app_endpoint_policy.setter
    def web_app_endpoint_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAppId")
    def web_app_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @web_app_id.setter
    def web_app_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAppUnits")
    def web_app_units(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WebAppWebAppUnitArgs]]]]:
        
        ...
    
    @web_app_units.setter
    def web_app_units(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WebAppWebAppUnitArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:transfer/webApp:WebApp")
class WebApp(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_details: Optional[pulumi.Input[Union[WebAppEndpointDetailsArgs, WebAppEndpointDetailsArgsDict]]] = ..., identity_provider_details: Optional[pulumi.Input[Union[WebAppIdentityProviderDetailsArgs, WebAppIdentityProviderDetailsArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., web_app_endpoint_policy: Optional[pulumi.Input[_builtins.str]] = ..., web_app_units: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WebAppWebAppUnitArgs, WebAppWebAppUnitArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WebAppArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_details: Optional[pulumi.Input[Union[WebAppEndpointDetailsArgs, WebAppEndpointDetailsArgsDict]]] = ..., identity_provider_details: Optional[pulumi.Input[Union[WebAppIdentityProviderDetailsArgs, WebAppIdentityProviderDetailsArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., web_app_endpoint_policy: Optional[pulumi.Input[_builtins.str]] = ..., web_app_id: Optional[pulumi.Input[_builtins.str]] = ..., web_app_units: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WebAppWebAppUnitArgs, WebAppWebAppUnitArgsDict]]]]] = ...) -> WebApp:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessEndpoint")
    def access_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointDetails")
    def endpoint_details(self) -> pulumi.Output[Optional[outputs.WebAppEndpointDetails]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityProviderDetails")
    def identity_provider_details(self) -> pulumi.Output[outputs.WebAppIdentityProviderDetails]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAppEndpointPolicy")
    def web_app_endpoint_policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAppId")
    def web_app_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAppUnits")
    def web_app_units(self) -> pulumi.Output[Sequence[outputs.WebAppWebAppUnit]]:
        
        ...
    


