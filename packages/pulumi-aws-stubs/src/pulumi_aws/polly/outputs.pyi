

import builtins as _builtins
import sys
import pulumi
from typing import Sequence

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVoicesVoiceResult']
@pulumi.output_type
class GetVoicesVoiceResult(dict):
    def __init__(__self__, *, additional_language_codes: Sequence[_builtins.str], gender: _builtins.str, id: _builtins.str, language_code: _builtins.str, language_name: _builtins.str, name: _builtins.str, supported_engines: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalLanguageCodes")
    def additional_language_codes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gender(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageName")
    def language_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedEngines")
    def supported_engines(self) -> Sequence[_builtins.str]:
        
        ...
    


