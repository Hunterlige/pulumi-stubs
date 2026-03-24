

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPublicKeyResult', 'AwaitableGetPublicKeyResult', 'get_public_key', 'get_public_key_output']
@pulumi.output_type
class GetPublicKeyResult:
    
    def __init__(__self__, arn=..., customer_master_key_spec=..., encryption_algorithms=..., grant_tokens=..., id=..., key_id=..., key_usage=..., public_key=..., public_key_pem=..., region=..., signing_algorithms=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerMasterKeySpec")
    def customer_master_key_spec(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithms")
    def encryption_algorithms(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grantTokens")
    def grant_tokens(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKeyPem")
    def public_key_pem(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingAlgorithms")
    def signing_algorithms(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetPublicKeyResult(GetPublicKeyResult):
    def __await__(self): # -> Generator[Never, Any, GetPublicKeyResult]:
        ...
    


def get_public_key(grant_tokens: Optional[Sequence[_builtins.str]] = ..., key_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPublicKeyResult:
    
    ...

def get_public_key_output(grant_tokens: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., key_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPublicKeyResult]:
    
    ...

