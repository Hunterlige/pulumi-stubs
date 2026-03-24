

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
__all__ = ['ContainerRecipeArgs', 'ContainerRecipe']
@pulumi.input_type
class ContainerRecipeArgs:
    def __init__(__self__, *, components: pulumi.Input[Sequence[pulumi.Input[ContainerRecipeComponentArgs]]], container_type: pulumi.Input[_builtins.str], parent_image: pulumi.Input[_builtins.str], target_repository: pulumi.Input[ContainerRecipeTargetRepositoryArgs], version: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., dockerfile_template_data: Optional[pulumi.Input[_builtins.str]] = ..., dockerfile_template_uri: Optional[pulumi.Input[_builtins.str]] = ..., instance_configuration: Optional[pulumi.Input[ContainerRecipeInstanceConfigurationArgs]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., platform_override: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., working_directory: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> pulumi.Input[Sequence[pulumi.Input[ContainerRecipeComponentArgs]]]:
        
        ...
    
    @components.setter
    def components(self, value: pulumi.Input[Sequence[pulumi.Input[ContainerRecipeComponentArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @container_type.setter
    def container_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentImage")
    def parent_image(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent_image.setter
    def parent_image(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetRepository")
    def target_repository(self) -> pulumi.Input[ContainerRecipeTargetRepositoryArgs]:
        
        ...
    
    @target_repository.setter
    def target_repository(self, value: pulumi.Input[ContainerRecipeTargetRepositoryArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerfileTemplateData")
    def dockerfile_template_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dockerfile_template_data.setter
    def dockerfile_template_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerfileTemplateUri")
    def dockerfile_template_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dockerfile_template_uri.setter
    def dockerfile_template_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceConfiguration")
    def instance_configuration(self) -> Optional[pulumi.Input[ContainerRecipeInstanceConfigurationArgs]]:
        
        ...
    
    @instance_configuration.setter
    def instance_configuration(self, value: Optional[pulumi.Input[ContainerRecipeInstanceConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformOverride")
    def platform_override(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform_override.setter
    def platform_override(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="workingDirectory")
    def working_directory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @working_directory.setter
    def working_directory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ContainerRecipeState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., components: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerRecipeComponentArgs]]]] = ..., container_type: Optional[pulumi.Input[_builtins.str]] = ..., date_created: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dockerfile_template_data: Optional[pulumi.Input[_builtins.str]] = ..., dockerfile_template_uri: Optional[pulumi.Input[_builtins.str]] = ..., encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., instance_configuration: Optional[pulumi.Input[ContainerRecipeInstanceConfigurationArgs]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., owner: Optional[pulumi.Input[_builtins.str]] = ..., parent_image: Optional[pulumi.Input[_builtins.str]] = ..., platform: Optional[pulumi.Input[_builtins.str]] = ..., platform_override: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_repository: Optional[pulumi.Input[ContainerRecipeTargetRepositoryArgs]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., working_directory: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ContainerRecipeComponentArgs]]]]:
        
        ...
    
    @components.setter
    def components(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerRecipeComponentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container_type.setter
    def container_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @date_created.setter
    def date_created(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerfileTemplateData")
    def dockerfile_template_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dockerfile_template_data.setter
    def dockerfile_template_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerfileTemplateUri")
    def dockerfile_template_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dockerfile_template_uri.setter
    def dockerfile_template_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceConfiguration")
    def instance_configuration(self) -> Optional[pulumi.Input[ContainerRecipeInstanceConfigurationArgs]]:
        
        ...
    
    @instance_configuration.setter
    def instance_configuration(self, value: Optional[pulumi.Input[ContainerRecipeInstanceConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentImage")
    def parent_image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent_image.setter
    def parent_image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform.setter
    def platform(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformOverride")
    def platform_override(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform_override.setter
    def platform_override(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="targetRepository")
    def target_repository(self) -> Optional[pulumi.Input[ContainerRecipeTargetRepositoryArgs]]:
        
        ...
    
    @target_repository.setter
    def target_repository(self, value: Optional[pulumi.Input[ContainerRecipeTargetRepositoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workingDirectory")
    def working_directory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @working_directory.setter
    def working_directory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:imagebuilder/containerRecipe:ContainerRecipe")
class ContainerRecipe(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., components: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ContainerRecipeComponentArgs, ContainerRecipeComponentArgsDict]]]]] = ..., container_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dockerfile_template_data: Optional[pulumi.Input[_builtins.str]] = ..., dockerfile_template_uri: Optional[pulumi.Input[_builtins.str]] = ..., instance_configuration: Optional[pulumi.Input[Union[ContainerRecipeInstanceConfigurationArgs, ContainerRecipeInstanceConfigurationArgsDict]]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent_image: Optional[pulumi.Input[_builtins.str]] = ..., platform_override: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_repository: Optional[pulumi.Input[Union[ContainerRecipeTargetRepositoryArgs, ContainerRecipeTargetRepositoryArgsDict]]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., working_directory: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ContainerRecipeArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., components: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ContainerRecipeComponentArgs, ContainerRecipeComponentArgsDict]]]]] = ..., container_type: Optional[pulumi.Input[_builtins.str]] = ..., date_created: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., dockerfile_template_data: Optional[pulumi.Input[_builtins.str]] = ..., dockerfile_template_uri: Optional[pulumi.Input[_builtins.str]] = ..., encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., instance_configuration: Optional[pulumi.Input[Union[ContainerRecipeInstanceConfigurationArgs, ContainerRecipeInstanceConfigurationArgsDict]]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., owner: Optional[pulumi.Input[_builtins.str]] = ..., parent_image: Optional[pulumi.Input[_builtins.str]] = ..., platform: Optional[pulumi.Input[_builtins.str]] = ..., platform_override: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_repository: Optional[pulumi.Input[Union[ContainerRecipeTargetRepositoryArgs, ContainerRecipeTargetRepositoryArgsDict]]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., working_directory: Optional[pulumi.Input[_builtins.str]] = ...) -> ContainerRecipe:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> pulumi.Output[Sequence[outputs.ContainerRecipeComponent]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerfileTemplateData")
    def dockerfile_template_data(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerfileTemplateUri")
    def dockerfile_template_uri(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceConfiguration")
    def instance_configuration(self) -> pulumi.Output[Optional[outputs.ContainerRecipeInstanceConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentImage")
    def parent_image(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def platform(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformOverride")
    def platform_override(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="targetRepository")
    def target_repository(self) -> pulumi.Output[outputs.ContainerRecipeTargetRepository]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workingDirectory")
    def working_directory(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


