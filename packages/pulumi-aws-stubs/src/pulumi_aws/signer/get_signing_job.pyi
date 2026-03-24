

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSigningJobResult', 'AwaitableGetSigningJobResult', 'get_signing_job', 'get_signing_job_output']
@pulumi.output_type
class GetSigningJobResult:
    
    def __init__(__self__, completed_at=..., created_at=..., id=..., job_id=..., job_invoker=..., job_owner=..., platform_display_name=..., platform_id=..., profile_name=..., profile_version=..., region=..., requested_by=..., revocation_records=..., signature_expires_at=..., signed_objects=..., sources=..., status=..., status_reason=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="completedAt")
    def completed_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobInvoker")
    def job_invoker(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobOwner")
    def job_owner(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformDisplayName")
    def platform_display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformId")
    def platform_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileVersion")
    def profile_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestedBy")
    def requested_by(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revocationRecords")
    def revocation_records(self) -> Sequence[outputs.GetSigningJobRevocationRecordResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signatureExpiresAt")
    def signature_expires_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signedObjects")
    def signed_objects(self) -> Sequence[outputs.GetSigningJobSignedObjectResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Sequence[outputs.GetSigningJobSourceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSigningJobResult(GetSigningJobResult):
    def __await__(self): # -> Generator[Never, Any, GetSigningJobResult]:
        ...
    


def get_signing_job(job_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSigningJobResult:
    
    ...

def get_signing_job_output(job_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSigningJobResult]:
    
    ...

