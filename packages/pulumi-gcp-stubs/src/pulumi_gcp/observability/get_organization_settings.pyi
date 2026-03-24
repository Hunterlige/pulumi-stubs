

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOrganizationSettingsResult', 'AwaitableGetOrganizationSettingsResult', 'get_organization_settings', 'get_organization_settings_output']
@pulumi.output_type
class GetOrganizationSettingsResult:
    
    def __init__(__self__, default_storage_location=..., id=..., kms_key_name=..., location=..., name=..., organization=..., service_account_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultStorageLocation")
    def default_storage_location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> _builtins.str:
        ...
    


class AwaitableGetOrganizationSettingsResult(GetOrganizationSettingsResult):
    def __await__(self): # -> Generator[Never, Any, GetOrganizationSettingsResult]:
        ...
    


def get_organization_settings(location: Optional[_builtins.str] = ..., organization: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOrganizationSettingsResult:
    
    ...

def get_organization_settings_output(location: Optional[pulumi.Input[_builtins.str]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOrganizationSettingsResult]:
    
    ...

