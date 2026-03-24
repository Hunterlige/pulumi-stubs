

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRandomPasswordResult', 'AwaitableGetRandomPasswordResult', 'get_random_password', 'get_random_password_output']
@pulumi.output_type
class GetRandomPasswordResult:
    
    def __init__(__self__, exclude_characters=..., exclude_lowercase=..., exclude_numbers=..., exclude_punctuation=..., exclude_uppercase=..., id=..., include_space=..., password_length=..., random_password=..., region=..., require_each_included_type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeCharacters")
    def exclude_characters(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeLowercase")
    def exclude_lowercase(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeNumbers")
    def exclude_numbers(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludePunctuation")
    def exclude_punctuation(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeUppercase")
    def exclude_uppercase(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeSpace")
    def include_space(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordLength")
    def password_length(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="randomPassword")
    def random_password(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireEachIncludedType")
    def require_each_included_type(self) -> Optional[_builtins.bool]:
        ...
    


class AwaitableGetRandomPasswordResult(GetRandomPasswordResult):
    def __await__(self): # -> Generator[Never, Any, GetRandomPasswordResult]:
        ...
    


def get_random_password(exclude_characters: Optional[_builtins.str] = ..., exclude_lowercase: Optional[_builtins.bool] = ..., exclude_numbers: Optional[_builtins.bool] = ..., exclude_punctuation: Optional[_builtins.bool] = ..., exclude_uppercase: Optional[_builtins.bool] = ..., include_space: Optional[_builtins.bool] = ..., password_length: Optional[_builtins.int] = ..., region: Optional[_builtins.str] = ..., require_each_included_type: Optional[_builtins.bool] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRandomPasswordResult:
    
    ...

def get_random_password_output(exclude_characters: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., exclude_lowercase: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., exclude_numbers: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., exclude_punctuation: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., exclude_uppercase: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., include_space: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., password_length: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., require_each_included_type: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRandomPasswordResult]:
    
    ...

