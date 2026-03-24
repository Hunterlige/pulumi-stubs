

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AutoScalingConfigurationVersionArgs', 'AutoScalingConfigurationVersion']
@pulumi.input_type
class AutoScalingConfigurationVersionArgs:
    def __init__(__self__, *, auto_scaling_configuration_name: pulumi.Input[_builtins.str], max_concurrency: Optional[pulumi.Input[_builtins.int]] = ..., max_size: Optional[pulumi.Input[_builtins.int]] = ..., min_size: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingConfigurationName")
    def auto_scaling_configuration_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @auto_scaling_configuration_name.setter
    def auto_scaling_configuration_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrency")
    def max_concurrency(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_concurrency.setter
    def max_concurrency(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_size.setter
    def max_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_size.setter
    def min_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
class _AutoScalingConfigurationVersionState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_scaling_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., auto_scaling_configuration_revision: Optional[pulumi.Input[_builtins.int]] = ..., has_associated_service: Optional[pulumi.Input[_builtins.bool]] = ..., is_default: Optional[pulumi.Input[_builtins.bool]] = ..., latest: Optional[pulumi.Input[_builtins.bool]] = ..., max_concurrency: Optional[pulumi.Input[_builtins.int]] = ..., max_size: Optional[pulumi.Input[_builtins.int]] = ..., min_size: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingConfigurationName")
    def auto_scaling_configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auto_scaling_configuration_name.setter
    def auto_scaling_configuration_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingConfigurationRevision")
    def auto_scaling_configuration_revision(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @auto_scaling_configuration_revision.setter
    def auto_scaling_configuration_revision(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasAssociatedService")
    def has_associated_service(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @has_associated_service.setter
    def has_associated_service(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @is_default.setter
    def is_default(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def latest(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @latest.setter
    def latest(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrency")
    def max_concurrency(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_concurrency.setter
    def max_concurrency(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_size.setter
    def max_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_size.setter
    def min_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token(...)
class AutoScalingConfigurationVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auto_scaling_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., max_concurrency: Optional[pulumi.Input[_builtins.int]] = ..., max_size: Optional[pulumi.Input[_builtins.int]] = ..., min_size: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AutoScalingConfigurationVersionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_scaling_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., auto_scaling_configuration_revision: Optional[pulumi.Input[_builtins.int]] = ..., has_associated_service: Optional[pulumi.Input[_builtins.bool]] = ..., is_default: Optional[pulumi.Input[_builtins.bool]] = ..., latest: Optional[pulumi.Input[_builtins.bool]] = ..., max_concurrency: Optional[pulumi.Input[_builtins.int]] = ..., max_size: Optional[pulumi.Input[_builtins.int]] = ..., min_size: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> AutoScalingConfigurationVersion:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingConfigurationName")
    def auto_scaling_configuration_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingConfigurationRevision")
    def auto_scaling_configuration_revision(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasAssociatedService")
    def has_associated_service(self) -> pulumi.Output[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> pulumi.Output[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def latest(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrency")
    def max_concurrency(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


