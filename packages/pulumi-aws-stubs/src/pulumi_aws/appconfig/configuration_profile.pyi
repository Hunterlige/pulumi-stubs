

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
__all__ = ['ConfigurationProfileArgs', 'ConfigurationProfile']
@pulumi.input_type
class ConfigurationProfileArgs:
    def __init__(__self__, *, application_id: pulumi.Input[_builtins.str], location_uri: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retrieval_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., validators: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationProfileValidatorArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @application_id.setter
    def application_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location_uri.setter
    def location_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_identifier.setter
    def kms_key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="retrievalRoleArn")
    def retrieval_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @retrieval_role_arn.setter
    def retrieval_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def validators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationProfileValidatorArgs]]]]:
        
        ...
    
    @validators.setter
    def validators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationProfileValidatorArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ConfigurationProfileState:
    def __init__(__self__, *, application_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., configuration_profile_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ..., location_uri: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retrieval_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., validators: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationProfileValidatorArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationProfileId")
    def configuration_profile_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configuration_profile_id.setter
    def configuration_profile_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_identifier.setter
    def kms_key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location_uri.setter
    def location_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="retrievalRoleArn")
    def retrieval_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @retrieval_role_arn.setter
    def retrieval_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def validators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationProfileValidatorArgs]]]]:
        
        ...
    
    @validators.setter
    def validators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationProfileValidatorArgs]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ConfigurationProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., application_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ..., location_uri: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retrieval_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., validators: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ConfigurationProfileValidatorArgs, ConfigurationProfileValidatorArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConfigurationProfileArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., application_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., configuration_profile_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ..., location_uri: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retrieval_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., validators: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ConfigurationProfileValidatorArgs, ConfigurationProfileValidatorArgsDict]]]]] = ...) -> ConfigurationProfile:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationProfileId")
    def configuration_profile_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="retrievalRoleArn")
    def retrieval_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def validators(self) -> pulumi.Output[Optional[Sequence[outputs.ConfigurationProfileValidator]]]:
        
        ...
    


