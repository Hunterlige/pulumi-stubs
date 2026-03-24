

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSamlProviderResult', 'AwaitableGetSamlProviderResult', 'get_saml_provider', 'get_saml_provider_output']
@pulumi.output_type
class GetSamlProviderResult:
    
    def __init__(__self__, arn=..., create_date=..., id=..., name=..., saml_metadata_document=..., saml_provider_uuid=..., tags=..., valid_until=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createDate")
    def create_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="samlMetadataDocument")
    def saml_metadata_document(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="samlProviderUuid")
    def saml_provider_uuid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validUntil")
    def valid_until(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSamlProviderResult(GetSamlProviderResult):
    def __await__(self): # -> Generator[Never, Any, GetSamlProviderResult]:
        ...
    


def get_saml_provider(arn: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSamlProviderResult:
    
    ...

def get_saml_provider_output(arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSamlProviderResult]:
    
    ...

