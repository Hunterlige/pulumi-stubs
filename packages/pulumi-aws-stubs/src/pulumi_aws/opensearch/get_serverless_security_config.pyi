

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServerlessSecurityConfigResult', 'AwaitableGetServerlessSecurityConfigResult', 'get_serverless_security_config', 'get_serverless_security_config_output']
@pulumi.output_type
class GetServerlessSecurityConfigResult:
    
    def __init__(__self__, config_version=..., created_date=..., description=..., id=..., last_modified_date=..., region=..., saml_options=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configVersion")
    def config_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str:
        
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
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="samlOptions")
    def saml_options(self) -> Optional[Sequence[outputs.GetServerlessSecurityConfigSamlOptionResult]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetServerlessSecurityConfigResult(GetServerlessSecurityConfigResult):
    def __await__(self): # -> Generator[Never, Any, GetServerlessSecurityConfigResult]:
        ...
    


def get_serverless_security_config(id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., saml_options: Optional[Sequence[Union[GetServerlessSecurityConfigSamlOptionArgs, GetServerlessSecurityConfigSamlOptionArgsDict]]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServerlessSecurityConfigResult:
    
    ...

def get_serverless_security_config_output(id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., saml_options: Optional[pulumi.Input[Optional[Sequence[Union[GetServerlessSecurityConfigSamlOptionArgs, GetServerlessSecurityConfigSamlOptionArgsDict]]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServerlessSecurityConfigResult]:
    
    ...

