

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
__all__ = ['DeveloperAppArgs', 'DeveloperApp']
@pulumi.input_type
class DeveloperAppArgs:
    def __init__(__self__, *, callback_url: pulumi.Input[_builtins.str], developer_email: pulumi.Input[_builtins.str], org_id: pulumi.Input[_builtins.str], api_products: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., app_family: Optional[pulumi.Input[_builtins.str]] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAppAttributeArgs]]]] = ..., key_expires_in: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callbackUrl")
    def callback_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @callback_url.setter
    def callback_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerEmail")
    def developer_email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @developer_email.setter
    def developer_email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiProducts")
    def api_products(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @api_products.setter
    def api_products(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appFamily")
    def app_family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_family.setter
    def app_family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAppAttributeArgs]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAppAttributeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyExpiresIn")
    def key_expires_in(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_expires_in.setter
    def key_expires_in(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DeveloperAppState:
    def __init__(__self__, *, api_products: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., app_family: Optional[pulumi.Input[_builtins.str]] = ..., app_id: Optional[pulumi.Input[_builtins.str]] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAppAttributeArgs]]]] = ..., callback_url: Optional[pulumi.Input[_builtins.str]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., credentials: Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAppCredentialArgs]]]] = ..., developer_email: Optional[pulumi.Input[_builtins.str]] = ..., developer_id: Optional[pulumi.Input[_builtins.str]] = ..., key_expires_in: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_at: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiProducts")
    def api_products(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @api_products.setter
    def api_products(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appFamily")
    def app_family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_family.setter
    def app_family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAppAttributeArgs]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAppAttributeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="callbackUrl")
    def callback_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @callback_url.setter
    def callback_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAppCredentialArgs]]]]:
        
        ...
    
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAppCredentialArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerEmail")
    def developer_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @developer_email.setter
    def developer_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerId")
    def developer_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @developer_id.setter
    def developer_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyExpiresIn")
    def key_expires_in(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_expires_in.setter
    def key_expires_in(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified_at.setter
    def last_modified_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:apigee/developerApp:DeveloperApp")
class DeveloperApp(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api_products: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., app_family: Optional[pulumi.Input[_builtins.str]] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeveloperAppAttributeArgs, DeveloperAppAttributeArgsDict]]]]] = ..., callback_url: Optional[pulumi.Input[_builtins.str]] = ..., developer_email: Optional[pulumi.Input[_builtins.str]] = ..., key_expires_in: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DeveloperAppArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., api_products: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., app_family: Optional[pulumi.Input[_builtins.str]] = ..., app_id: Optional[pulumi.Input[_builtins.str]] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeveloperAppAttributeArgs, DeveloperAppAttributeArgsDict]]]]] = ..., callback_url: Optional[pulumi.Input[_builtins.str]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., credentials: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeveloperAppCredentialArgs, DeveloperAppCredentialArgsDict]]]]] = ..., developer_email: Optional[pulumi.Input[_builtins.str]] = ..., developer_id: Optional[pulumi.Input[_builtins.str]] = ..., key_expires_in: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_at: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> DeveloperApp:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiProducts")
    def api_products(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appFamily")
    def app_family(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Optional[Sequence[outputs.DeveloperAppAttribute]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callbackUrl")
    def callback_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Sequence[outputs.DeveloperAppCredential]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerEmail")
    def developer_email(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerId")
    def developer_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyExpiresIn")
    def key_expires_in(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


