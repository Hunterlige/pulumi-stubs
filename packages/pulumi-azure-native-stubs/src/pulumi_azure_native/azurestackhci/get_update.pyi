

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetUpdateResult', 'AwaitableGetUpdateResult', 'get_update', 'get_update_output']
@pulumi.output_type
class GetUpdateResult:
    
    def __init__(__self__, additional_properties=..., availability_type=..., azure_api_version=..., description=..., display_name=..., health_check_date=..., id=..., installed_date=..., location=..., min_sbe_version_required=..., name=..., notify_message=..., package_path=..., package_size_in_mb=..., package_type=..., prerequisites=..., progress_percentage=..., provisioning_state=..., publisher=..., release_link=..., state=..., system_data=..., type=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityType")
    def availability_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckDate")
    def health_check_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="installedDate")
    def installed_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSbeVersionRequired")
    def min_sbe_version_required(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notifyMessage")
    def notify_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packagePath")
    def package_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageSizeInMb")
    def package_size_in_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageType")
    def package_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prerequisites(self) -> Optional[Sequence[outputs.UpdatePrerequisiteResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="progressPercentage")
    def progress_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseLink")
    def release_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetUpdateResult(GetUpdateResult):
    def __await__(self): # -> Generator[Never, Any, GetUpdateResult]:
        ...
    


def get_update(cluster_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., update_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetUpdateResult:
    
    ...

def get_update_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., update_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetUpdateResult]:
    
    ...

