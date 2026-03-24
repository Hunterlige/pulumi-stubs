

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['KeyvaluestoreKeyArgs', 'KeyvaluestoreKey']
@pulumi.input_type
class KeyvaluestoreKeyArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], key_value_store_arn: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyValueStoreArn")
    def key_value_store_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_value_store_arn.setter
    def key_value_store_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _KeyvaluestoreKeyState:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., key_value_store_arn: Optional[pulumi.Input[_builtins.str]] = ..., total_size_in_bytes: Optional[pulumi.Input[_builtins.int]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyValueStoreArn")
    def key_value_store_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_value_store_arn.setter
    def key_value_store_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalSizeInBytes")
    def total_size_in_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @total_size_in_bytes.setter
    def total_size_in_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:cloudfront/keyvaluestoreKey:KeyvaluestoreKey")
class KeyvaluestoreKey(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., key_value_store_arn: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: KeyvaluestoreKeyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., key_value_store_arn: Optional[pulumi.Input[_builtins.str]] = ..., total_size_in_bytes: Optional[pulumi.Input[_builtins.int]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> KeyvaluestoreKey:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyValueStoreArn")
    def key_value_store_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalSizeInBytes")
    def total_size_in_bytes(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


