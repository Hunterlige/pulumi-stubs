

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['KeyKeyAttributeArgs', 'KeyKeyAttributeArgsDict', 'KeyKeyAttributeKeyModesOfUseArgs', 'KeyKeyAttributeKeyModesOfUseArgsDict', 'KeyTimeoutsArgs', 'KeyTimeoutsArgsDict']
class KeyKeyAttributeArgsDict(TypedDict):
    key_algorithm: pulumi.Input[_builtins.str]
    key_class: pulumi.Input[_builtins.str]
    key_usage: pulumi.Input[_builtins.str]
    key_modes_of_uses: NotRequired[pulumi.Input[Sequence[pulumi.Input[KeyKeyAttributeKeyModesOfUseArgsDict]]]]


@pulumi.input_type
class KeyKeyAttributeArgs:
    def __init__(__self__, *, key_algorithm: pulumi.Input[_builtins.str], key_class: pulumi.Input[_builtins.str], key_usage: pulumi.Input[_builtins.str], key_modes_of_uses: Optional[pulumi.Input[Sequence[pulumi.Input[KeyKeyAttributeKeyModesOfUseArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_algorithm.setter
    def key_algorithm(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyClass")
    def key_class(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_class.setter
    def key_class(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_usage.setter
    def key_usage(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyModesOfUses")
    def key_modes_of_uses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[KeyKeyAttributeKeyModesOfUseArgs]]]]:
        
        ...
    
    @key_modes_of_uses.setter
    def key_modes_of_uses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[KeyKeyAttributeKeyModesOfUseArgs]]]]): # -> None:
        ...
    


class KeyKeyAttributeKeyModesOfUseArgsDict(TypedDict):
    decrypt: NotRequired[pulumi.Input[_builtins.bool]]
    derive_key: NotRequired[pulumi.Input[_builtins.bool]]
    encrypt: NotRequired[pulumi.Input[_builtins.bool]]
    generate: NotRequired[pulumi.Input[_builtins.bool]]
    no_restrictions: NotRequired[pulumi.Input[_builtins.bool]]
    sign: NotRequired[pulumi.Input[_builtins.bool]]
    unwrap: NotRequired[pulumi.Input[_builtins.bool]]
    verify: NotRequired[pulumi.Input[_builtins.bool]]
    wrap: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class KeyKeyAttributeKeyModesOfUseArgs:
    def __init__(__self__, *, decrypt: Optional[pulumi.Input[_builtins.bool]] = ..., derive_key: Optional[pulumi.Input[_builtins.bool]] = ..., encrypt: Optional[pulumi.Input[_builtins.bool]] = ..., generate: Optional[pulumi.Input[_builtins.bool]] = ..., no_restrictions: Optional[pulumi.Input[_builtins.bool]] = ..., sign: Optional[pulumi.Input[_builtins.bool]] = ..., unwrap: Optional[pulumi.Input[_builtins.bool]] = ..., verify: Optional[pulumi.Input[_builtins.bool]] = ..., wrap: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def decrypt(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @decrypt.setter
    def decrypt(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deriveKey")
    def derive_key(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @derive_key.setter
    def derive_key(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypt(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypt.setter
    def encrypt(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def generate(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @generate.setter
    def generate(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noRestrictions")
    def no_restrictions(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @no_restrictions.setter
    def no_restrictions(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sign(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @sign.setter
    def sign(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def unwrap(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @unwrap.setter
    def unwrap(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def verify(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @verify.setter
    def verify(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def wrap(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wrap.setter
    def wrap(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class KeyTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeyTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


