

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebAppDeploymentSlotResult', 'AwaitableGetWebAppDeploymentSlotResult', 'get_web_app_deployment_slot', 'get_web_app_deployment_slot_output']
@pulumi.output_type
class GetWebAppDeploymentSlotResult:
    
    def __init__(__self__, active=..., author=..., author_email=..., azure_api_version=..., deployer=..., details=..., end_time=..., id=..., kind=..., message=..., name=..., start_time=..., status=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def author(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorEmail")
    def author_email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deployer(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWebAppDeploymentSlotResult(GetWebAppDeploymentSlotResult):
    def __await__(self): # -> Generator[Never, Any, GetWebAppDeploymentSlotResult]:
        ...
    


def get_web_app_deployment_slot(id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., slot: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebAppDeploymentSlotResult:
    
    ...

def get_web_app_deployment_slot_output(id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., slot: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebAppDeploymentSlotResult]:
    
    ...

