

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBlobFolderDataSetResult', 'AwaitableGetBlobFolderDataSetResult', 'get_blob_folder_data_set', 'get_blob_folder_data_set_output']
@pulumi.output_type
class GetBlobFolderDataSetResult:
    
    def __init__(__self__, azure_api_version=..., container_name=..., data_set_id=..., id=..., kind=..., name=..., prefix=..., resource_group=..., storage_account_name=..., subscription_id=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetBlobFolderDataSetResult(GetBlobFolderDataSetResult):
    def __await__(self): # -> Generator[Never, Any, GetBlobFolderDataSetResult]:
        ...
    


def get_blob_folder_data_set(account_name: Optional[_builtins.str] = ..., data_set_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., share_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBlobFolderDataSetResult:
    
    ...

def get_blob_folder_data_set_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., data_set_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., share_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBlobFolderDataSetResult]:
    
    ...

