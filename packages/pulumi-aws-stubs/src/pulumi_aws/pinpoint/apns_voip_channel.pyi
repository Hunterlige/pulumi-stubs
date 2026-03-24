

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApnsVoipChannelArgs', 'ApnsVoipChannel']
@pulumi.input_type
class ApnsVoipChannelArgs:
    def __init__(__self__, *, application_id: pulumi.Input[_builtins.str], bundle_id: Optional[pulumi.Input[_builtins.str]] = ..., certificate: Optional[pulumi.Input[_builtins.str]] = ..., default_authentication_method: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., private_key: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., team_id: Optional[pulumi.Input[_builtins.str]] = ..., token_key: Optional[pulumi.Input[_builtins.str]] = ..., token_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @application_id.setter
    def application_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bundle_id.setter
    def bundle_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAuthenticationMethod")
    def default_authentication_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_authentication_method.setter
    def default_authentication_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenKey")
    def token_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @token_key.setter
    def token_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenKeyId")
    def token_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @token_key_id.setter
    def token_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ApnsVoipChannelState:
    def __init__(__self__, *, application_id: Optional[pulumi.Input[_builtins.str]] = ..., bundle_id: Optional[pulumi.Input[_builtins.str]] = ..., certificate: Optional[pulumi.Input[_builtins.str]] = ..., default_authentication_method: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., private_key: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., team_id: Optional[pulumi.Input[_builtins.str]] = ..., token_key: Optional[pulumi.Input[_builtins.str]] = ..., token_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bundle_id.setter
    def bundle_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAuthenticationMethod")
    def default_authentication_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_authentication_method.setter
    def default_authentication_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenKey")
    def token_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @token_key.setter
    def token_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenKeyId")
    def token_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @token_key_id.setter
    def token_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:pinpoint/apnsVoipChannel:ApnsVoipChannel")
class ApnsVoipChannel(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., application_id: Optional[pulumi.Input[_builtins.str]] = ..., bundle_id: Optional[pulumi.Input[_builtins.str]] = ..., certificate: Optional[pulumi.Input[_builtins.str]] = ..., default_authentication_method: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., private_key: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., team_id: Optional[pulumi.Input[_builtins.str]] = ..., token_key: Optional[pulumi.Input[_builtins.str]] = ..., token_key_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ApnsVoipChannelArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., application_id: Optional[pulumi.Input[_builtins.str]] = ..., bundle_id: Optional[pulumi.Input[_builtins.str]] = ..., certificate: Optional[pulumi.Input[_builtins.str]] = ..., default_authentication_method: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., private_key: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., team_id: Optional[pulumi.Input[_builtins.str]] = ..., token_key: Optional[pulumi.Input[_builtins.str]] = ..., token_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> ApnsVoipChannel:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAuthenticationMethod")
    def default_authentication_method(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenKey")
    def token_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenKeyId")
    def token_key_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


