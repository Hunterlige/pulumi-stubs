

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEvidenceResult', 'AwaitableGetEvidenceResult', 'get_evidence', 'get_evidence_output']
@pulumi.output_type
class GetEvidenceResult:
    
    def __init__(__self__, azure_api_version=..., control_id=..., evidence_type=..., extra_data=..., file_path=..., id=..., name=..., provisioning_state=..., responsibility_id=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlId")
    def control_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evidenceType")
    def evidence_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraData")
    def extra_data(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> _builtins.str:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responsibilityId")
    def responsibility_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetEvidenceResult(GetEvidenceResult):
    def __await__(self): # -> Generator[Never, Any, GetEvidenceResult]:
        ...
    


def get_evidence(evidence_name: Optional[_builtins.str] = ..., report_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEvidenceResult:
    
    ...

def get_evidence_output(evidence_name: Optional[pulumi.Input[_builtins.str]] = ..., report_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEvidenceResult]:
    
    ...

