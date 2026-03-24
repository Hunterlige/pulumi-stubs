

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
__all__ = ['ImageRecipeArgs', 'ImageRecipe']
@pulumi.input_type
class ImageRecipeArgs:
    def __init__(__self__, *, components: pulumi.Input[Sequence[pulumi.Input[ImageRecipeComponentArgs]]], parent_image: pulumi.Input[_builtins.str], version: pulumi.Input[_builtins.str], ami_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., block_device_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[ImageRecipeBlockDeviceMappingArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., systems_manager_agent: Optional[pulumi.Input[ImageRecipeSystemsManagerAgentArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_data_base64: Optional[pulumi.Input[_builtins.str]] = ..., working_directory: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> pulumi.Input[Sequence[pulumi.Input[ImageRecipeComponentArgs]]]:
        
        ...
    
    @components.setter
    def components(self, value: pulumi.Input[Sequence[pulumi.Input[ImageRecipeComponentArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentImage")
    def parent_image(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent_image.setter
    def parent_image(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amiTags")
    def ami_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ami_tags.setter
    def ami_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockDeviceMappings")
    def block_device_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImageRecipeBlockDeviceMappingArgs]]]]:
        
        ...
    
    @block_device_mappings.setter
    def block_device_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ImageRecipeBlockDeviceMappingArgs]]]]): # -> None:
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
    @pulumi.getter(name="systemsManagerAgent")
    def systems_manager_agent(self) -> Optional[pulumi.Input[ImageRecipeSystemsManagerAgentArgs]]:
        
        ...
    
    @systems_manager_agent.setter
    def systems_manager_agent(self, value: Optional[pulumi.Input[ImageRecipeSystemsManagerAgentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDataBase64")
    def user_data_base64(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data_base64.setter
    def user_data_base64(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workingDirectory")
    def working_directory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @working_directory.setter
    def working_directory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ImageRecipeState:
    def __init__(__self__, *, ami_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., block_device_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[ImageRecipeBlockDeviceMappingArgs]]]] = ..., components: Optional[pulumi.Input[Sequence[pulumi.Input[ImageRecipeComponentArgs]]]] = ..., date_created: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., owner: Optional[pulumi.Input[_builtins.str]] = ..., parent_image: Optional[pulumi.Input[_builtins.str]] = ..., platform: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., systems_manager_agent: Optional[pulumi.Input[ImageRecipeSystemsManagerAgentArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_data_base64: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., working_directory: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amiTags")
    def ami_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ami_tags.setter
    def ami_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockDeviceMappings")
    def block_device_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImageRecipeBlockDeviceMappingArgs]]]]:
        
        ...
    
    @block_device_mappings.setter
    def block_device_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ImageRecipeBlockDeviceMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImageRecipeComponentArgs]]]]:
        
        ...
    
    @components.setter
    def components(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ImageRecipeComponentArgs]]]]): # -> None:
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemsManagerAgent")
    def systems_manager_agent(self) -> Optional[pulumi.Input[ImageRecipeSystemsManagerAgentArgs]]:
        
        ...
    
    @systems_manager_agent.setter
    def systems_manager_agent(self, value: Optional[pulumi.Input[ImageRecipeSystemsManagerAgentArgs]]): # -> None:
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
    @pulumi.getter(name="userDataBase64")
    def user_data_base64(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data_base64.setter
    def user_data_base64(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("aws:imagebuilder/imageRecipe:ImageRecipe")
class ImageRecipe(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., ami_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., block_device_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ImageRecipeBlockDeviceMappingArgs, ImageRecipeBlockDeviceMappingArgsDict]]]]] = ..., components: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ImageRecipeComponentArgs, ImageRecipeComponentArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent_image: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., systems_manager_agent: Optional[pulumi.Input[Union[ImageRecipeSystemsManagerAgentArgs, ImageRecipeSystemsManagerAgentArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_data_base64: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., working_directory: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ImageRecipeArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., ami_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., block_device_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ImageRecipeBlockDeviceMappingArgs, ImageRecipeBlockDeviceMappingArgsDict]]]]] = ..., components: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ImageRecipeComponentArgs, ImageRecipeComponentArgsDict]]]]] = ..., date_created: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., owner: Optional[pulumi.Input[_builtins.str]] = ..., parent_image: Optional[pulumi.Input[_builtins.str]] = ..., platform: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., systems_manager_agent: Optional[pulumi.Input[Union[ImageRecipeSystemsManagerAgentArgs, ImageRecipeSystemsManagerAgentArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_data_base64: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., working_directory: Optional[pulumi.Input[_builtins.str]] = ...) -> ImageRecipe:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amiTags")
    def ami_tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockDeviceMappings")
    def block_device_mappings(self) -> pulumi.Output[Optional[Sequence[outputs.ImageRecipeBlockDeviceMapping]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> pulumi.Output[Sequence[outputs.ImageRecipeComponent]]:
        
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
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemsManagerAgent")
    def systems_manager_agent(self) -> pulumi.Output[outputs.ImageRecipeSystemsManagerAgent]:
        
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
    @pulumi.getter(name="userDataBase64")
    def user_data_base64(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workingDirectory")
    def working_directory(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


