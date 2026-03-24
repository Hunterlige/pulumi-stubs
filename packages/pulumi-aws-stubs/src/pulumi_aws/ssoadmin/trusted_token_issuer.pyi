

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
__all__ = ['TrustedTokenIssuerArgs', 'TrustedTokenIssuer']
@pulumi.input_type
class TrustedTokenIssuerArgs:
    def __init__(__self__, *, instance_arn: pulumi.Input[_builtins.str], trusted_token_issuer_configuration: pulumi.Input[TrustedTokenIssuerTrustedTokenIssuerConfigurationArgs], trusted_token_issuer_type: pulumi.Input[_builtins.str], client_token: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_arn.setter
    def instance_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedTokenIssuerConfiguration")
    def trusted_token_issuer_configuration(self) -> pulumi.Input[TrustedTokenIssuerTrustedTokenIssuerConfigurationArgs]:
        
        ...
    
    @trusted_token_issuer_configuration.setter
    def trusted_token_issuer_configuration(self, value: pulumi.Input[TrustedTokenIssuerTrustedTokenIssuerConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedTokenIssuerType")
    def trusted_token_issuer_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @trusted_token_issuer_type.setter
    def trusted_token_issuer_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_token.setter
    def client_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.input_type
class _TrustedTokenIssuerState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., client_token: Optional[pulumi.Input[_builtins.str]] = ..., instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., trusted_token_issuer_configuration: Optional[pulumi.Input[TrustedTokenIssuerTrustedTokenIssuerConfigurationArgs]] = ..., trusted_token_issuer_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_token.setter
    def client_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_arn.setter
    def instance_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="trustedTokenIssuerConfiguration")
    def trusted_token_issuer_configuration(self) -> Optional[pulumi.Input[TrustedTokenIssuerTrustedTokenIssuerConfigurationArgs]]:
        
        ...
    
    @trusted_token_issuer_configuration.setter
    def trusted_token_issuer_configuration(self, value: Optional[pulumi.Input[TrustedTokenIssuerTrustedTokenIssuerConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedTokenIssuerType")
    def trusted_token_issuer_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trusted_token_issuer_type.setter
    def trusted_token_issuer_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ssoadmin/trustedTokenIssuer:TrustedTokenIssuer")
class TrustedTokenIssuer(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., client_token: Optional[pulumi.Input[_builtins.str]] = ..., instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., trusted_token_issuer_configuration: Optional[pulumi.Input[Union[TrustedTokenIssuerTrustedTokenIssuerConfigurationArgs, TrustedTokenIssuerTrustedTokenIssuerConfigurationArgsDict]]] = ..., trusted_token_issuer_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TrustedTokenIssuerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., client_token: Optional[pulumi.Input[_builtins.str]] = ..., instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., trusted_token_issuer_configuration: Optional[pulumi.Input[Union[TrustedTokenIssuerTrustedTokenIssuerConfigurationArgs, TrustedTokenIssuerTrustedTokenIssuerConfigurationArgsDict]]] = ..., trusted_token_issuer_type: Optional[pulumi.Input[_builtins.str]] = ...) -> TrustedTokenIssuer:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="trustedTokenIssuerConfiguration")
    def trusted_token_issuer_configuration(self) -> pulumi.Output[outputs.TrustedTokenIssuerTrustedTokenIssuerConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedTokenIssuerType")
    def trusted_token_issuer_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


