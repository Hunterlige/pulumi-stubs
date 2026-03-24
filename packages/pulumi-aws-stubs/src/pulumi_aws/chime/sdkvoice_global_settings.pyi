

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SdkvoiceGlobalSettingsArgs', 'SdkvoiceGlobalSettings']
@pulumi.input_type
class SdkvoiceGlobalSettingsArgs:
    def __init__(__self__, *, voice_connector: pulumi.Input[SdkvoiceGlobalSettingsVoiceConnectorArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceConnector")
    def voice_connector(self) -> pulumi.Input[SdkvoiceGlobalSettingsVoiceConnectorArgs]:
        
        ...
    
    @voice_connector.setter
    def voice_connector(self, value: pulumi.Input[SdkvoiceGlobalSettingsVoiceConnectorArgs]): # -> None:
        ...
    


@pulumi.input_type
class _SdkvoiceGlobalSettingsState:
    def __init__(__self__, *, voice_connector: Optional[pulumi.Input[SdkvoiceGlobalSettingsVoiceConnectorArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceConnector")
    def voice_connector(self) -> Optional[pulumi.Input[SdkvoiceGlobalSettingsVoiceConnectorArgs]]:
        
        ...
    
    @voice_connector.setter
    def voice_connector(self, value: Optional[pulumi.Input[SdkvoiceGlobalSettingsVoiceConnectorArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class SdkvoiceGlobalSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., voice_connector: Optional[pulumi.Input[Union[SdkvoiceGlobalSettingsVoiceConnectorArgs, SdkvoiceGlobalSettingsVoiceConnectorArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SdkvoiceGlobalSettingsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., voice_connector: Optional[pulumi.Input[Union[SdkvoiceGlobalSettingsVoiceConnectorArgs, SdkvoiceGlobalSettingsVoiceConnectorArgsDict]]] = ...) -> SdkvoiceGlobalSettings:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceConnector")
    def voice_connector(self) -> pulumi.Output[outputs.SdkvoiceGlobalSettingsVoiceConnector]:
        
        ...
    


