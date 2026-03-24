

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['KeyKeyAttribute', 'KeyKeyAttributeKeyModesOfUse', 'KeyTimeouts']
@pulumi.output_type
class KeyKeyAttribute(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_algorithm: _builtins.str, key_class: _builtins.str, key_usage: _builtins.str, key_modes_of_uses: Optional[Sequence[outputs.KeyKeyAttributeKeyModesOfUse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyClass")
    def key_class(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyModesOfUses")
    def key_modes_of_uses(self) -> Optional[Sequence[outputs.KeyKeyAttributeKeyModesOfUse]]:
        
        ...
    


@pulumi.output_type
class KeyKeyAttributeKeyModesOfUse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, decrypt: Optional[_builtins.bool] = ..., derive_key: Optional[_builtins.bool] = ..., encrypt: Optional[_builtins.bool] = ..., generate: Optional[_builtins.bool] = ..., no_restrictions: Optional[_builtins.bool] = ..., sign: Optional[_builtins.bool] = ..., unwrap: Optional[_builtins.bool] = ..., verify: Optional[_builtins.bool] = ..., wrap: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def decrypt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deriveKey")
    def derive_key(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def generate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noRestrictions")
    def no_restrictions(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sign(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unwrap(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def verify(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def wrap(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class KeyTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


