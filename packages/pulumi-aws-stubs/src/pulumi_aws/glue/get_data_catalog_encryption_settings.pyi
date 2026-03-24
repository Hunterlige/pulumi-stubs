

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDataCatalogEncryptionSettingsResult', 'AwaitableGetDataCatalogEncryptionSettingsResult', 'get_data_catalog_encryption_settings', 'get_data_catalog_encryption_settings_output']
@pulumi.output_type
class GetDataCatalogEncryptionSettingsResult:
    
    def __init__(__self__, catalog_id=..., data_catalog_encryption_settings=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCatalogEncryptionSettings")
    def data_catalog_encryption_settings(self) -> Sequence[outputs.GetDataCatalogEncryptionSettingsDataCatalogEncryptionSettingResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetDataCatalogEncryptionSettingsResult(GetDataCatalogEncryptionSettingsResult):
    def __await__(self): # -> Generator[Never, Any, GetDataCatalogEncryptionSettingsResult]:
        ...
    


def get_data_catalog_encryption_settings(catalog_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDataCatalogEncryptionSettingsResult:
    
    ...

def get_data_catalog_encryption_settings_output(catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDataCatalogEncryptionSettingsResult]:
    
    ...

