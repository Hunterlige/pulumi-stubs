

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetStorageAccountCredentialResult', 'AwaitableGetStorageAccountCredentialResult', 'get_storage_account_credential', 'get_storage_account_credential_output']
@pulumi.output_type
class GetStorageAccountCredentialResult:
    
    def __init__(__self__, account_key=..., account_type=..., alias=..., azure_api_version=..., blob_domain_name=..., connection_string=..., id=..., name=..., ssl_status=..., storage_account_id=..., system_data=..., type=..., user_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[outputs.AsymmetricEncryptedSecretResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountType")
    def account_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobDomainName")
    def blob_domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="sslStatus")
    def ssl_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetStorageAccountCredentialResult(GetStorageAccountCredentialResult):
    def __await__(self): # -> Generator[Never, Any, GetStorageAccountCredentialResult]:
        ...
    


def get_storage_account_credential(device_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetStorageAccountCredentialResult:
    
    ...

def get_storage_account_credential_output(device_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetStorageAccountCredentialResult]:
    
    ...

