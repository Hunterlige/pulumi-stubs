

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ImageVersionArgs', 'ImageVersion']
@pulumi.input_type
class ImageVersionArgs:
    def __init__(__self__, *, base_image: pulumi.Input[_builtins.str], image_name: pulumi.Input[_builtins.str], aliases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., horovod: Optional[pulumi.Input[_builtins.bool]] = ..., job_type: Optional[pulumi.Input[_builtins.str]] = ..., ml_framework: Optional[pulumi.Input[_builtins.str]] = ..., processor: Optional[pulumi.Input[_builtins.str]] = ..., programming_lang: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., release_notes: Optional[pulumi.Input[_builtins.str]] = ..., vendor_guidance: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @base_image.setter
    def base_image(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def aliases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @aliases.setter
    def aliases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def horovod(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @horovod.setter
    def horovod(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @job_type.setter
    def job_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mlFramework")
    def ml_framework(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ml_framework.setter
    def ml_framework(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def processor(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @processor.setter
    def processor(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="programmingLang")
    def programming_lang(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @programming_lang.setter
    def programming_lang(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseNotes")
    def release_notes(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @release_notes.setter
    def release_notes(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vendorGuidance")
    def vendor_guidance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vendor_guidance.setter
    def vendor_guidance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ImageVersionState:
    def __init__(__self__, *, aliases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., base_image: Optional[pulumi.Input[_builtins.str]] = ..., container_image: Optional[pulumi.Input[_builtins.str]] = ..., horovod: Optional[pulumi.Input[_builtins.bool]] = ..., image_arn: Optional[pulumi.Input[_builtins.str]] = ..., image_name: Optional[pulumi.Input[_builtins.str]] = ..., job_type: Optional[pulumi.Input[_builtins.str]] = ..., ml_framework: Optional[pulumi.Input[_builtins.str]] = ..., processor: Optional[pulumi.Input[_builtins.str]] = ..., programming_lang: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., release_notes: Optional[pulumi.Input[_builtins.str]] = ..., vendor_guidance: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def aliases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @aliases.setter
    def aliases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @base_image.setter
    def base_image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container_image.setter
    def container_image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def horovod(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @horovod.setter
    def horovod(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageArn")
    def image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @image_arn.setter
    def image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @job_type.setter
    def job_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mlFramework")
    def ml_framework(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ml_framework.setter
    def ml_framework(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def processor(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @processor.setter
    def processor(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="programmingLang")
    def programming_lang(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @programming_lang.setter
    def programming_lang(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseNotes")
    def release_notes(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @release_notes.setter
    def release_notes(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vendorGuidance")
    def vendor_guidance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vendor_guidance.setter
    def vendor_guidance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("aws:sagemaker/imageVersion:ImageVersion")
class ImageVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aliases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., base_image: Optional[pulumi.Input[_builtins.str]] = ..., horovod: Optional[pulumi.Input[_builtins.bool]] = ..., image_name: Optional[pulumi.Input[_builtins.str]] = ..., job_type: Optional[pulumi.Input[_builtins.str]] = ..., ml_framework: Optional[pulumi.Input[_builtins.str]] = ..., processor: Optional[pulumi.Input[_builtins.str]] = ..., programming_lang: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., release_notes: Optional[pulumi.Input[_builtins.str]] = ..., vendor_guidance: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ImageVersionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., aliases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., base_image: Optional[pulumi.Input[_builtins.str]] = ..., container_image: Optional[pulumi.Input[_builtins.str]] = ..., horovod: Optional[pulumi.Input[_builtins.bool]] = ..., image_arn: Optional[pulumi.Input[_builtins.str]] = ..., image_name: Optional[pulumi.Input[_builtins.str]] = ..., job_type: Optional[pulumi.Input[_builtins.str]] = ..., ml_framework: Optional[pulumi.Input[_builtins.str]] = ..., processor: Optional[pulumi.Input[_builtins.str]] = ..., programming_lang: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., release_notes: Optional[pulumi.Input[_builtins.str]] = ..., vendor_guidance: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> ImageVersion:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def aliases(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def horovod(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageArn")
    def image_arn(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mlFramework")
    def ml_framework(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def processor(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="programmingLang")
    def programming_lang(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseNotes")
    def release_notes(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vendorGuidance")
    def vendor_guidance(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.int]:
        
        ...
    


