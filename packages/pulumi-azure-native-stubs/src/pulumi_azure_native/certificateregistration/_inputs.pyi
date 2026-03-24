

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AppServiceCertificateArgs', 'AppServiceCertificateArgsDict']
class AppServiceCertificateArgsDict(TypedDict):
    
    key_vault_id: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_secret_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppServiceCertificateArgs:
    def __init__(__self__, *, key_vault_id: Optional[pulumi.Input[_builtins.str]] = ..., key_vault_secret_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_vault_id.setter
    def key_vault_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultSecretName")
    def key_vault_secret_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_vault_secret_name.setter
    def key_vault_secret_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


