

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
__all__ = ['DocumentClassifierArgs', 'DocumentClassifier']
@pulumi.input_type
class DocumentClassifierArgs:
    def __init__(__self__, *, data_access_role_arn: pulumi.Input[_builtins.str], input_data_config: pulumi.Input[DocumentClassifierInputDataConfigArgs], language_code: pulumi.Input[_builtins.str], mode: Optional[pulumi.Input[_builtins.str]] = ..., model_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., output_data_config: Optional[pulumi.Input[DocumentClassifierOutputDataConfigArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., version_name: Optional[pulumi.Input[_builtins.str]] = ..., version_name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., volume_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_config: Optional[pulumi.Input[DocumentClassifierVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccessRoleArn")
    def data_access_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_access_role_arn.setter
    def data_access_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputDataConfig")
    def input_data_config(self) -> pulumi.Input[DocumentClassifierInputDataConfigArgs]:
        
        ...
    
    @input_data_config.setter
    def input_data_config(self, value: pulumi.Input[DocumentClassifierInputDataConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @language_code.setter
    def language_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelKmsKeyId")
    def model_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_kms_key_id.setter
    def model_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputDataConfig")
    def output_data_config(self) -> Optional[pulumi.Input[DocumentClassifierOutputDataConfigArgs]]:
        
        ...
    
    @output_data_config.setter
    def output_data_config(self, value: Optional[pulumi.Input[DocumentClassifierOutputDataConfigArgs]]): # -> None:
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
    @pulumi.getter(name="versionName")
    def version_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version_name.setter
    def version_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionNamePrefix")
    def version_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version_name_prefix.setter
    def version_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeKmsKeyId")
    def volume_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_kms_key_id.setter
    def volume_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[DocumentClassifierVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[DocumentClassifierVpcConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _DocumentClassifierState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., data_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., input_data_config: Optional[pulumi.Input[DocumentClassifierInputDataConfigArgs]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., model_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., output_data_config: Optional[pulumi.Input[DocumentClassifierOutputDataConfigArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., version_name: Optional[pulumi.Input[_builtins.str]] = ..., version_name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., volume_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_config: Optional[pulumi.Input[DocumentClassifierVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccessRoleArn")
    def data_access_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_access_role_arn.setter
    def data_access_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputDataConfig")
    def input_data_config(self) -> Optional[pulumi.Input[DocumentClassifierInputDataConfigArgs]]:
        
        ...
    
    @input_data_config.setter
    def input_data_config(self, value: Optional[pulumi.Input[DocumentClassifierInputDataConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelKmsKeyId")
    def model_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_kms_key_id.setter
    def model_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputDataConfig")
    def output_data_config(self) -> Optional[pulumi.Input[DocumentClassifierOutputDataConfigArgs]]:
        
        ...
    
    @output_data_config.setter
    def output_data_config(self, value: Optional[pulumi.Input[DocumentClassifierOutputDataConfigArgs]]): # -> None:
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
    @pulumi.getter(name="versionName")
    def version_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version_name.setter
    def version_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionNamePrefix")
    def version_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version_name_prefix.setter
    def version_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeKmsKeyId")
    def volume_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_kms_key_id.setter
    def volume_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[DocumentClassifierVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[DocumentClassifierVpcConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DocumentClassifier(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., data_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., input_data_config: Optional[pulumi.Input[Union[DocumentClassifierInputDataConfigArgs, DocumentClassifierInputDataConfigArgsDict]]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., model_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., output_data_config: Optional[pulumi.Input[Union[DocumentClassifierOutputDataConfigArgs, DocumentClassifierOutputDataConfigArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., version_name: Optional[pulumi.Input[_builtins.str]] = ..., version_name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., volume_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_config: Optional[pulumi.Input[Union[DocumentClassifierVpcConfigArgs, DocumentClassifierVpcConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DocumentClassifierArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., data_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., input_data_config: Optional[pulumi.Input[Union[DocumentClassifierInputDataConfigArgs, DocumentClassifierInputDataConfigArgsDict]]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., model_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., output_data_config: Optional[pulumi.Input[Union[DocumentClassifierOutputDataConfigArgs, DocumentClassifierOutputDataConfigArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., version_name: Optional[pulumi.Input[_builtins.str]] = ..., version_name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., volume_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_config: Optional[pulumi.Input[Union[DocumentClassifierVpcConfigArgs, DocumentClassifierVpcConfigArgsDict]]] = ...) -> DocumentClassifier:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccessRoleArn")
    def data_access_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputDataConfig")
    def input_data_config(self) -> pulumi.Output[outputs.DocumentClassifierInputDataConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelKmsKeyId")
    def model_kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputDataConfig")
    def output_data_config(self) -> pulumi.Output[outputs.DocumentClassifierOutputDataConfig]:
        
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
    @pulumi.getter(name="versionName")
    def version_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionNamePrefix")
    def version_name_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeKmsKeyId")
    def volume_kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Output[Optional[outputs.DocumentClassifierVpcConfig]]:
        
        ...
    


