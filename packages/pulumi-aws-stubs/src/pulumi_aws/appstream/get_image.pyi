

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetImageResult', 'AwaitableGetImageResult', 'get_image', 'get_image_output']
@pulumi.output_type
class GetImageResult:
    
    def __init__(__self__, applications=..., appstream_agent_version=..., arn=..., base_image_arn=..., created_time=..., description=..., display_name=..., id=..., image_builder_name=..., image_builder_supported=..., image_permissions=..., most_recent=..., name=..., name_regex=..., platform=..., public_base_image_released_date=..., region=..., state=..., state_change_reasons=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def applications(self) -> Sequence[outputs.GetImageApplicationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appstreamAgentVersion")
    def appstream_agent_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseImageArn")
    def base_image_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageBuilderName")
    def image_builder_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageBuilderSupported")
    def image_builder_supported(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imagePermissions")
    def image_permissions(self) -> Sequence[outputs.GetImageImagePermissionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def platform(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicBaseImageReleasedDate")
    def public_base_image_released_date(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateChangeReasons")
    def state_change_reasons(self) -> Sequence[outputs.GetImageStateChangeReasonResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetImageResult(GetImageResult):
    def __await__(self): # -> Generator[Never, Any, GetImageResult]:
        ...
    


def get_image(arn: Optional[_builtins.str] = ..., most_recent: Optional[_builtins.bool] = ..., name: Optional[_builtins.str] = ..., name_regex: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetImageResult:
    
    ...

def get_image_output(arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., most_recent: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name_regex: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetImageResult]:
    
    ...

