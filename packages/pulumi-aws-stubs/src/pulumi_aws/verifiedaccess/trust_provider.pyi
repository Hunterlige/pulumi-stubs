

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TrustProviderArgs', 'TrustProvider']
@pulumi.input_type
class TrustProviderArgs:
    def __init__(__self__, *, policy_reference_name: pulumi.Input[_builtins.str], trust_provider_type: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., device_options: Optional[pulumi.Input[TrustProviderDeviceOptionsArgs]] = ..., device_trust_provider_type: Optional[pulumi.Input[_builtins.str]] = ..., native_application_oidc_options: Optional[pulumi.Input[TrustProviderNativeApplicationOidcOptionsArgs]] = ..., oidc_options: Optional[pulumi.Input[TrustProviderOidcOptionsArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sse_specification: Optional[pulumi.Input[TrustProviderSseSpecificationArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_trust_provider_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyReferenceName")
    def policy_reference_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_reference_name.setter
    def policy_reference_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustProviderType")
    def trust_provider_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @trust_provider_type.setter
    def trust_provider_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceOptions")
    def device_options(self) -> Optional[pulumi.Input[TrustProviderDeviceOptionsArgs]]:
        
        ...
    
    @device_options.setter
    def device_options(self, value: Optional[pulumi.Input[TrustProviderDeviceOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceTrustProviderType")
    def device_trust_provider_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_trust_provider_type.setter
    def device_trust_provider_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nativeApplicationOidcOptions")
    def native_application_oidc_options(self) -> Optional[pulumi.Input[TrustProviderNativeApplicationOidcOptionsArgs]]:
        
        ...
    
    @native_application_oidc_options.setter
    def native_application_oidc_options(self, value: Optional[pulumi.Input[TrustProviderNativeApplicationOidcOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcOptions")
    def oidc_options(self) -> Optional[pulumi.Input[TrustProviderOidcOptionsArgs]]:
        
        ...
    
    @oidc_options.setter
    def oidc_options(self, value: Optional[pulumi.Input[TrustProviderOidcOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseSpecification")
    def sse_specification(self) -> Optional[pulumi.Input[TrustProviderSseSpecificationArgs]]:
        ...
    
    @sse_specification.setter
    def sse_specification(self, value: Optional[pulumi.Input[TrustProviderSseSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userTrustProviderType")
    def user_trust_provider_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_trust_provider_type.setter
    def user_trust_provider_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TrustProviderState:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., device_options: Optional[pulumi.Input[TrustProviderDeviceOptionsArgs]] = ..., device_trust_provider_type: Optional[pulumi.Input[_builtins.str]] = ..., native_application_oidc_options: Optional[pulumi.Input[TrustProviderNativeApplicationOidcOptionsArgs]] = ..., oidc_options: Optional[pulumi.Input[TrustProviderOidcOptionsArgs]] = ..., policy_reference_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sse_specification: Optional[pulumi.Input[TrustProviderSseSpecificationArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., trust_provider_type: Optional[pulumi.Input[_builtins.str]] = ..., user_trust_provider_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceOptions")
    def device_options(self) -> Optional[pulumi.Input[TrustProviderDeviceOptionsArgs]]:
        
        ...
    
    @device_options.setter
    def device_options(self, value: Optional[pulumi.Input[TrustProviderDeviceOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceTrustProviderType")
    def device_trust_provider_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_trust_provider_type.setter
    def device_trust_provider_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nativeApplicationOidcOptions")
    def native_application_oidc_options(self) -> Optional[pulumi.Input[TrustProviderNativeApplicationOidcOptionsArgs]]:
        
        ...
    
    @native_application_oidc_options.setter
    def native_application_oidc_options(self, value: Optional[pulumi.Input[TrustProviderNativeApplicationOidcOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcOptions")
    def oidc_options(self) -> Optional[pulumi.Input[TrustProviderOidcOptionsArgs]]:
        
        ...
    
    @oidc_options.setter
    def oidc_options(self, value: Optional[pulumi.Input[TrustProviderOidcOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyReferenceName")
    def policy_reference_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_reference_name.setter
    def policy_reference_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseSpecification")
    def sse_specification(self) -> Optional[pulumi.Input[TrustProviderSseSpecificationArgs]]:
        ...
    
    @sse_specification.setter
    def sse_specification(self, value: Optional[pulumi.Input[TrustProviderSseSpecificationArgs]]): # -> None:
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
    @pulumi.getter(name="trustProviderType")
    def trust_provider_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trust_provider_type.setter
    def trust_provider_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userTrustProviderType")
    def user_trust_provider_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_trust_provider_type.setter
    def user_trust_provider_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:verifiedaccess/trustProvider:TrustProvider")
class TrustProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., device_options: Optional[pulumi.Input[Union[TrustProviderDeviceOptionsArgs, TrustProviderDeviceOptionsArgsDict]]] = ..., device_trust_provider_type: Optional[pulumi.Input[_builtins.str]] = ..., native_application_oidc_options: Optional[pulumi.Input[Union[TrustProviderNativeApplicationOidcOptionsArgs, TrustProviderNativeApplicationOidcOptionsArgsDict]]] = ..., oidc_options: Optional[pulumi.Input[Union[TrustProviderOidcOptionsArgs, TrustProviderOidcOptionsArgsDict]]] = ..., policy_reference_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sse_specification: Optional[pulumi.Input[Union[TrustProviderSseSpecificationArgs, TrustProviderSseSpecificationArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., trust_provider_type: Optional[pulumi.Input[_builtins.str]] = ..., user_trust_provider_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TrustProviderArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., device_options: Optional[pulumi.Input[Union[TrustProviderDeviceOptionsArgs, TrustProviderDeviceOptionsArgsDict]]] = ..., device_trust_provider_type: Optional[pulumi.Input[_builtins.str]] = ..., native_application_oidc_options: Optional[pulumi.Input[Union[TrustProviderNativeApplicationOidcOptionsArgs, TrustProviderNativeApplicationOidcOptionsArgsDict]]] = ..., oidc_options: Optional[pulumi.Input[Union[TrustProviderOidcOptionsArgs, TrustProviderOidcOptionsArgsDict]]] = ..., policy_reference_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sse_specification: Optional[pulumi.Input[Union[TrustProviderSseSpecificationArgs, TrustProviderSseSpecificationArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., trust_provider_type: Optional[pulumi.Input[_builtins.str]] = ..., user_trust_provider_type: Optional[pulumi.Input[_builtins.str]] = ...) -> TrustProvider:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceOptions")
    def device_options(self) -> pulumi.Output[Optional[outputs.TrustProviderDeviceOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceTrustProviderType")
    def device_trust_provider_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nativeApplicationOidcOptions")
    def native_application_oidc_options(self) -> pulumi.Output[Optional[outputs.TrustProviderNativeApplicationOidcOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcOptions")
    def oidc_options(self) -> pulumi.Output[Optional[outputs.TrustProviderOidcOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyReferenceName")
    def policy_reference_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseSpecification")
    def sse_specification(self) -> pulumi.Output[outputs.TrustProviderSseSpecification]:
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
    @pulumi.getter(name="trustProviderType")
    def trust_provider_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userTrustProviderType")
    def user_trust_provider_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


