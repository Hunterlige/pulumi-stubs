

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConfigurationProfileResult', 'AwaitableGetConfigurationProfileResult', 'get_configuration_profile', 'get_configuration_profile_output']
@pulumi.output_type
class GetConfigurationProfileResult:
    
    def __init__(__self__, application_id=..., arn=..., configuration_profile_id=..., description=..., id=..., kms_key_identifier=..., location_uri=..., name=..., region=..., retrieval_role_arn=..., tags=..., type=..., validators=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationProfileId")
    def configuration_profile_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retrievalRoleArn")
    def retrieval_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def validators(self) -> Sequence[outputs.GetConfigurationProfileValidatorResult]:
        
        ...
    


class AwaitableGetConfigurationProfileResult(GetConfigurationProfileResult):
    def __await__(self): # -> Generator[Never, Any, GetConfigurationProfileResult]:
        ...
    


def get_configuration_profile(application_id: Optional[_builtins.str] = ..., configuration_profile_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConfigurationProfileResult:
    
    ...

def get_configuration_profile_output(application_id: Optional[pulumi.Input[_builtins.str]] = ..., configuration_profile_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConfigurationProfileResult]:
    
    ...

