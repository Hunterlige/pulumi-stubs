

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DetectorFeatureArgs', 'DetectorFeature']
@pulumi.input_type
class DetectorFeatureArgs:
    def __init__(__self__, *, detector_id: pulumi.Input[_builtins.str], status: pulumi.Input[_builtins.str], additional_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[DetectorFeatureAdditionalConfigurationArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @detector_id.setter
    def detector_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalConfigurations")
    def additional_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DetectorFeatureAdditionalConfigurationArgs]]]]:
        
        ...
    
    @additional_configurations.setter
    def additional_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DetectorFeatureAdditionalConfigurationArgs]]]]): # -> None:
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
    


@pulumi.input_type
class _DetectorFeatureState:
    def __init__(__self__, *, additional_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[DetectorFeatureAdditionalConfigurationArgs]]]] = ..., detector_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalConfigurations")
    def additional_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DetectorFeatureAdditionalConfigurationArgs]]]]:
        
        ...
    
    @additional_configurations.setter
    def additional_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DetectorFeatureAdditionalConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @detector_id.setter
    def detector_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:guardduty/detectorFeature:DetectorFeature")
class DetectorFeature(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., additional_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DetectorFeatureAdditionalConfigurationArgs, DetectorFeatureAdditionalConfigurationArgsDict]]]]] = ..., detector_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DetectorFeatureArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., additional_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DetectorFeatureAdditionalConfigurationArgs, DetectorFeatureAdditionalConfigurationArgsDict]]]]] = ..., detector_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> DetectorFeature:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalConfigurations")
    def additional_configurations(self) -> pulumi.Output[Optional[Sequence[outputs.DetectorFeatureAdditionalConfiguration]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


