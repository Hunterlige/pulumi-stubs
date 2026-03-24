

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWorkflowResult', 'AwaitableGetWorkflowResult', 'get_workflow', 'get_workflow_output']
@pulumi.output_type
class GetWorkflowResult:
    
    def __init__(__self__, app_name=..., azure_api_version=..., builder_version=..., dockerfile_generation_mode=..., dockerfile_output_directory=..., generation_language=..., github_workflow_profile=..., id=..., image_name=..., image_tag=..., language_version=..., location=..., manifest_generation_mode=..., manifest_output_directory=..., manifest_type=..., name=..., namespace=..., port=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appName")
    def app_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="builderVersion")
    def builder_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerfileGenerationMode")
    def dockerfile_generation_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerfileOutputDirectory")
    def dockerfile_output_directory(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generationLanguage")
    def generation_language(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="githubWorkflowProfile")
    def github_workflow_profile(self) -> Optional[outputs.GitHubWorkflowProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageTag")
    def image_tag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageVersion")
    def language_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestGenerationMode")
    def manifest_generation_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestOutputDirectory")
    def manifest_output_directory(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestType")
    def manifest_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWorkflowResult(GetWorkflowResult):
    def __await__(self): # -> Generator[Never, Any, GetWorkflowResult]:
        ...
    


def get_workflow(resource_group_name: Optional[_builtins.str] = ..., workflow_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWorkflowResult:
    
    ...

def get_workflow_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workflow_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWorkflowResult]:
    
    ...

