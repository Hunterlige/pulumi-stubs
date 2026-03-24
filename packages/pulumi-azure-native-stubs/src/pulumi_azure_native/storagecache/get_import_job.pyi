

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetImportJobResult', 'AwaitableGetImportJobResult', 'get_import_job', 'get_import_job_output']
@pulumi.output_type
class GetImportJobResult:
    
    def __init__(__self__, azure_api_version=..., blobs_imported_per_second=..., blobs_walked_per_second=..., conflict_resolution_mode=..., id=..., import_prefixes=..., last_completion_time=..., last_started_time=..., location=..., maximum_errors=..., name=..., provisioning_state=..., state=..., status_message=..., system_data=..., tags=..., total_blobs_imported=..., total_blobs_walked=..., total_conflicts=..., total_errors=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobsImportedPerSecond")
    def blobs_imported_per_second(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobsWalkedPerSecond")
    def blobs_walked_per_second(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictResolutionMode")
    def conflict_resolution_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importPrefixes")
    def import_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastCompletionTime")
    def last_completion_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStartedTime")
    def last_started_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumErrors")
    def maximum_errors(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalBlobsImported")
    def total_blobs_imported(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalBlobsWalked")
    def total_blobs_walked(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalConflicts")
    def total_conflicts(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalErrors")
    def total_errors(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetImportJobResult(GetImportJobResult):
    def __await__(self): # -> Generator[Never, Any, GetImportJobResult]:
        ...
    


def get_import_job(aml_filesystem_name: Optional[_builtins.str] = ..., import_job_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetImportJobResult:
    
    ...

def get_import_job_output(aml_filesystem_name: Optional[pulumi.Input[_builtins.str]] = ..., import_job_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetImportJobResult]:
    
    ...

