

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkforcePoolProviderArgs', 'WorkforcePoolProvider']
@pulumi.input_type
class WorkforcePoolProviderArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], provider_id: pulumi.Input[_builtins.str], workforce_pool_id: pulumi.Input[_builtins.str], attribute_condition: Optional[pulumi.Input[_builtins.str]] = ..., attribute_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., extended_attributes_oauth2_client: Optional[pulumi.Input[WorkforcePoolProviderExtendedAttributesOauth2ClientArgs]] = ..., extra_attributes_oauth2_client: Optional[pulumi.Input[WorkforcePoolProviderExtraAttributesOauth2ClientArgs]] = ..., oidc: Optional[pulumi.Input[WorkforcePoolProviderOidcArgs]] = ..., saml: Optional[pulumi.Input[WorkforcePoolProviderSamlArgs]] = ..., scim_usage: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @provider_id.setter
    def provider_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workforce_pool_id.setter
    def workforce_pool_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeCondition")
    def attribute_condition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @attribute_condition.setter
    def attribute_condition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeMapping")
    def attribute_mapping(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @attribute_mapping.setter
    def attribute_mapping(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedAttributesOauth2Client")
    @_utilities.deprecated(...)
    def extended_attributes_oauth2_client(self) -> Optional[pulumi.Input[WorkforcePoolProviderExtendedAttributesOauth2ClientArgs]]:
        
        ...
    
    @extended_attributes_oauth2_client.setter
    def extended_attributes_oauth2_client(self, value: Optional[pulumi.Input[WorkforcePoolProviderExtendedAttributesOauth2ClientArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraAttributesOauth2Client")
    def extra_attributes_oauth2_client(self) -> Optional[pulumi.Input[WorkforcePoolProviderExtraAttributesOauth2ClientArgs]]:
        
        ...
    
    @extra_attributes_oauth2_client.setter
    def extra_attributes_oauth2_client(self, value: Optional[pulumi.Input[WorkforcePoolProviderExtraAttributesOauth2ClientArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def oidc(self) -> Optional[pulumi.Input[WorkforcePoolProviderOidcArgs]]:
        
        ...
    
    @oidc.setter
    def oidc(self, value: Optional[pulumi.Input[WorkforcePoolProviderOidcArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def saml(self) -> Optional[pulumi.Input[WorkforcePoolProviderSamlArgs]]:
        
        ...
    
    @saml.setter
    def saml(self, value: Optional[pulumi.Input[WorkforcePoolProviderSamlArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scimUsage")
    def scim_usage(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scim_usage.setter
    def scim_usage(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _WorkforcePoolProviderState:
    def __init__(__self__, *, attribute_condition: Optional[pulumi.Input[_builtins.str]] = ..., attribute_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., extended_attributes_oauth2_client: Optional[pulumi.Input[WorkforcePoolProviderExtendedAttributesOauth2ClientArgs]] = ..., extra_attributes_oauth2_client: Optional[pulumi.Input[WorkforcePoolProviderExtraAttributesOauth2ClientArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., oidc: Optional[pulumi.Input[WorkforcePoolProviderOidcArgs]] = ..., provider_id: Optional[pulumi.Input[_builtins.str]] = ..., saml: Optional[pulumi.Input[WorkforcePoolProviderSamlArgs]] = ..., scim_usage: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeCondition")
    def attribute_condition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @attribute_condition.setter
    def attribute_condition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeMapping")
    def attribute_mapping(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @attribute_mapping.setter
    def attribute_mapping(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedAttributesOauth2Client")
    @_utilities.deprecated(...)
    def extended_attributes_oauth2_client(self) -> Optional[pulumi.Input[WorkforcePoolProviderExtendedAttributesOauth2ClientArgs]]:
        
        ...
    
    @extended_attributes_oauth2_client.setter
    def extended_attributes_oauth2_client(self, value: Optional[pulumi.Input[WorkforcePoolProviderExtendedAttributesOauth2ClientArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraAttributesOauth2Client")
    def extra_attributes_oauth2_client(self) -> Optional[pulumi.Input[WorkforcePoolProviderExtraAttributesOauth2ClientArgs]]:
        
        ...
    
    @extra_attributes_oauth2_client.setter
    def extra_attributes_oauth2_client(self, value: Optional[pulumi.Input[WorkforcePoolProviderExtraAttributesOauth2ClientArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def oidc(self) -> Optional[pulumi.Input[WorkforcePoolProviderOidcArgs]]:
        
        ...
    
    @oidc.setter
    def oidc(self, value: Optional[pulumi.Input[WorkforcePoolProviderOidcArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @provider_id.setter
    def provider_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def saml(self) -> Optional[pulumi.Input[WorkforcePoolProviderSamlArgs]]:
        
        ...
    
    @saml.setter
    def saml(self, value: Optional[pulumi.Input[WorkforcePoolProviderSamlArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scimUsage")
    def scim_usage(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scim_usage.setter
    def scim_usage(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workforce_pool_id.setter
    def workforce_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class WorkforcePoolProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., attribute_condition: Optional[pulumi.Input[_builtins.str]] = ..., attribute_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., extended_attributes_oauth2_client: Optional[pulumi.Input[Union[WorkforcePoolProviderExtendedAttributesOauth2ClientArgs, WorkforcePoolProviderExtendedAttributesOauth2ClientArgsDict]]] = ..., extra_attributes_oauth2_client: Optional[pulumi.Input[Union[WorkforcePoolProviderExtraAttributesOauth2ClientArgs, WorkforcePoolProviderExtraAttributesOauth2ClientArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., oidc: Optional[pulumi.Input[Union[WorkforcePoolProviderOidcArgs, WorkforcePoolProviderOidcArgsDict]]] = ..., provider_id: Optional[pulumi.Input[_builtins.str]] = ..., saml: Optional[pulumi.Input[Union[WorkforcePoolProviderSamlArgs, WorkforcePoolProviderSamlArgsDict]]] = ..., scim_usage: Optional[pulumi.Input[_builtins.str]] = ..., workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkforcePoolProviderArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., attribute_condition: Optional[pulumi.Input[_builtins.str]] = ..., attribute_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., extended_attributes_oauth2_client: Optional[pulumi.Input[Union[WorkforcePoolProviderExtendedAttributesOauth2ClientArgs, WorkforcePoolProviderExtendedAttributesOauth2ClientArgsDict]]] = ..., extra_attributes_oauth2_client: Optional[pulumi.Input[Union[WorkforcePoolProviderExtraAttributesOauth2ClientArgs, WorkforcePoolProviderExtraAttributesOauth2ClientArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., oidc: Optional[pulumi.Input[Union[WorkforcePoolProviderOidcArgs, WorkforcePoolProviderOidcArgsDict]]] = ..., provider_id: Optional[pulumi.Input[_builtins.str]] = ..., saml: Optional[pulumi.Input[Union[WorkforcePoolProviderSamlArgs, WorkforcePoolProviderSamlArgsDict]]] = ..., scim_usage: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ...) -> WorkforcePoolProvider:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeCondition")
    def attribute_condition(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeMapping")
    def attribute_mapping(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedAttributesOauth2Client")
    @_utilities.deprecated(...)
    def extended_attributes_oauth2_client(self) -> pulumi.Output[Optional[outputs.WorkforcePoolProviderExtendedAttributesOauth2Client]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraAttributesOauth2Client")
    def extra_attributes_oauth2_client(self) -> pulumi.Output[Optional[outputs.WorkforcePoolProviderExtraAttributesOauth2Client]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def oidc(self) -> pulumi.Output[Optional[outputs.WorkforcePoolProviderOidc]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def saml(self) -> pulumi.Output[Optional[outputs.WorkforcePoolProviderSaml]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scimUsage")
    def scim_usage(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


