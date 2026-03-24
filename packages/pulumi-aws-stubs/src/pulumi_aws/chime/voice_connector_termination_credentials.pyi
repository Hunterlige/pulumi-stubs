

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
__all__ = ['VoiceConnectorTerminationCredentialsArgs', 'VoiceConnectorTerminationCredentials']
@pulumi.input_type
class VoiceConnectorTerminationCredentialsArgs:
    def __init__(__self__, *, credentials: pulumi.Input[Sequence[pulumi.Input[VoiceConnectorTerminationCredentialsCredentialArgs]]], voice_connector_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> pulumi.Input[Sequence[pulumi.Input[VoiceConnectorTerminationCredentialsCredentialArgs]]]:
        
        ...
    
    @credentials.setter
    def credentials(self, value: pulumi.Input[Sequence[pulumi.Input[VoiceConnectorTerminationCredentialsCredentialArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceConnectorId")
    def voice_connector_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @voice_connector_id.setter
    def voice_connector_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _VoiceConnectorTerminationCredentialsState:
    def __init__(__self__, *, credentials: Optional[pulumi.Input[Sequence[pulumi.Input[VoiceConnectorTerminationCredentialsCredentialArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., voice_connector_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VoiceConnectorTerminationCredentialsCredentialArgs]]]]:
        
        ...
    
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VoiceConnectorTerminationCredentialsCredentialArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceConnectorId")
    def voice_connector_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @voice_connector_id.setter
    def voice_connector_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class VoiceConnectorTerminationCredentials(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., credentials: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VoiceConnectorTerminationCredentialsCredentialArgs, VoiceConnectorTerminationCredentialsCredentialArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., voice_connector_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VoiceConnectorTerminationCredentialsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., credentials: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VoiceConnectorTerminationCredentialsCredentialArgs, VoiceConnectorTerminationCredentialsCredentialArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., voice_connector_id: Optional[pulumi.Input[_builtins.str]] = ...) -> VoiceConnectorTerminationCredentials:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Sequence[outputs.VoiceConnectorTerminationCredentialsCredential]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceConnectorId")
    def voice_connector_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


