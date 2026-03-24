

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConfigurationSetResult', 'AwaitableGetConfigurationSetResult', 'get_configuration_set', 'get_configuration_set_output']
@pulumi.output_type
class GetConfigurationSetResult:
    
    def __init__(__self__, arn=..., configuration_set_name=..., delivery_options=..., id=..., region=..., reputation_options=..., sending_options=..., suppression_options=..., tags=..., tracking_options=..., vdm_options=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryOptions")
    def delivery_options(self) -> Sequence[outputs.GetConfigurationSetDeliveryOptionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reputationOptions")
    def reputation_options(self) -> Sequence[outputs.GetConfigurationSetReputationOptionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendingOptions")
    def sending_options(self) -> Sequence[outputs.GetConfigurationSetSendingOptionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressionOptions")
    def suppression_options(self) -> Sequence[outputs.GetConfigurationSetSuppressionOptionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingOptions")
    def tracking_options(self) -> Sequence[outputs.GetConfigurationSetTrackingOptionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vdmOptions")
    def vdm_options(self) -> Sequence[outputs.GetConfigurationSetVdmOptionResult]:
        
        ...
    


class AwaitableGetConfigurationSetResult(GetConfigurationSetResult):
    def __await__(self): # -> Generator[Never, Any, GetConfigurationSetResult]:
        ...
    


def get_configuration_set(configuration_set_name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConfigurationSetResult:
    
    ...

def get_configuration_set_output(configuration_set_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConfigurationSetResult]:
    
    ...

