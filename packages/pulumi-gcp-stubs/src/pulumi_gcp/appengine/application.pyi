

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
__all__ = ['ApplicationArgs', 'Application']
@pulumi.input_type
class ApplicationArgs:
    def __init__(__self__, *, location_id: pulumi.Input[_builtins.str], auth_domain: Optional[pulumi.Input[_builtins.str]] = ..., database_type: Optional[pulumi.Input[_builtins.str]] = ..., feature_settings: Optional[pulumi.Input[ApplicationFeatureSettingsArgs]] = ..., iap: Optional[pulumi.Input[ApplicationIapArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., serving_status: Optional[pulumi.Input[_builtins.str]] = ..., ssl_policy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationId")
    def location_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location_id.setter
    def location_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authDomain")
    def auth_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_domain.setter
    def auth_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_type.setter
    def database_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureSettings")
    def feature_settings(self) -> Optional[pulumi.Input[ApplicationFeatureSettingsArgs]]:
        
        ...
    
    @feature_settings.setter
    def feature_settings(self, value: Optional[pulumi.Input[ApplicationFeatureSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iap(self) -> Optional[pulumi.Input[ApplicationIapArgs]]:
        
        ...
    
    @iap.setter
    def iap(self, value: Optional[pulumi.Input[ApplicationIapArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="servingStatus")
    def serving_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @serving_status.setter
    def serving_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssl_policy.setter
    def ssl_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ApplicationState:
    def __init__(__self__, *, app_id: Optional[pulumi.Input[_builtins.str]] = ..., auth_domain: Optional[pulumi.Input[_builtins.str]] = ..., code_bucket: Optional[pulumi.Input[_builtins.str]] = ..., database_type: Optional[pulumi.Input[_builtins.str]] = ..., default_bucket: Optional[pulumi.Input[_builtins.str]] = ..., default_hostname: Optional[pulumi.Input[_builtins.str]] = ..., feature_settings: Optional[pulumi.Input[ApplicationFeatureSettingsArgs]] = ..., gcr_domain: Optional[pulumi.Input[_builtins.str]] = ..., iap: Optional[pulumi.Input[ApplicationIapArgs]] = ..., location_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., serving_status: Optional[pulumi.Input[_builtins.str]] = ..., ssl_policy: Optional[pulumi.Input[_builtins.str]] = ..., url_dispatch_rules: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationUrlDispatchRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authDomain")
    def auth_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_domain.setter
    def auth_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeBucket")
    def code_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @code_bucket.setter
    def code_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_type.setter
    def database_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBucket")
    def default_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_bucket.setter
    def default_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultHostname")
    def default_hostname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_hostname.setter
    def default_hostname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureSettings")
    def feature_settings(self) -> Optional[pulumi.Input[ApplicationFeatureSettingsArgs]]:
        
        ...
    
    @feature_settings.setter
    def feature_settings(self, value: Optional[pulumi.Input[ApplicationFeatureSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcrDomain")
    def gcr_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gcr_domain.setter
    def gcr_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iap(self) -> Optional[pulumi.Input[ApplicationIapArgs]]:
        
        ...
    
    @iap.setter
    def iap(self, value: Optional[pulumi.Input[ApplicationIapArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationId")
    def location_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location_id.setter
    def location_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="servingStatus")
    def serving_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @serving_status.setter
    def serving_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssl_policy.setter
    def ssl_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlDispatchRules")
    def url_dispatch_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationUrlDispatchRuleArgs]]]]:
        
        ...
    
    @url_dispatch_rules.setter
    def url_dispatch_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationUrlDispatchRuleArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:appengine/application:Application")
class Application(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auth_domain: Optional[pulumi.Input[_builtins.str]] = ..., database_type: Optional[pulumi.Input[_builtins.str]] = ..., feature_settings: Optional[pulumi.Input[Union[ApplicationFeatureSettingsArgs, ApplicationFeatureSettingsArgsDict]]] = ..., iap: Optional[pulumi.Input[Union[ApplicationIapArgs, ApplicationIapArgsDict]]] = ..., location_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., serving_status: Optional[pulumi.Input[_builtins.str]] = ..., ssl_policy: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ApplicationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., app_id: Optional[pulumi.Input[_builtins.str]] = ..., auth_domain: Optional[pulumi.Input[_builtins.str]] = ..., code_bucket: Optional[pulumi.Input[_builtins.str]] = ..., database_type: Optional[pulumi.Input[_builtins.str]] = ..., default_bucket: Optional[pulumi.Input[_builtins.str]] = ..., default_hostname: Optional[pulumi.Input[_builtins.str]] = ..., feature_settings: Optional[pulumi.Input[Union[ApplicationFeatureSettingsArgs, ApplicationFeatureSettingsArgsDict]]] = ..., gcr_domain: Optional[pulumi.Input[_builtins.str]] = ..., iap: Optional[pulumi.Input[Union[ApplicationIapArgs, ApplicationIapArgsDict]]] = ..., location_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., serving_status: Optional[pulumi.Input[_builtins.str]] = ..., ssl_policy: Optional[pulumi.Input[_builtins.str]] = ..., url_dispatch_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ApplicationUrlDispatchRuleArgs, ApplicationUrlDispatchRuleArgsDict]]]]] = ...) -> Application:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authDomain")
    def auth_domain(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeBucket")
    def code_bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBucket")
    def default_bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultHostname")
    def default_hostname(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureSettings")
    def feature_settings(self) -> pulumi.Output[outputs.ApplicationFeatureSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcrDomain")
    def gcr_domain(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iap(self) -> pulumi.Output[outputs.ApplicationIap]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationId")
    def location_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servingStatus")
    def serving_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlDispatchRules")
    def url_dispatch_rules(self) -> pulumi.Output[Sequence[outputs.ApplicationUrlDispatchRule]]:
        
        ...
    


