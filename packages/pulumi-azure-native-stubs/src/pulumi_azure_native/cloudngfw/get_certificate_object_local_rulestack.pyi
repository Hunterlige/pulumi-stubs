

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCertificateObjectLocalRulestackResult', 'AwaitableGetCertificateObjectLocalRulestackResult', 'get_certificate_object_local_rulestack', 'get_certificate_object_local_rulestack_output']
@pulumi.output_type
class GetCertificateObjectLocalRulestackResult:
    
    def __init__(__self__, audit_comment=..., azure_api_version=..., certificate_self_signed=..., certificate_signer_resource_id=..., description=..., etag=..., id=..., name=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateSelfSigned")
    def certificate_self_signed(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateSignerResourceId")
    def certificate_signer_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetCertificateObjectLocalRulestackResult(GetCertificateObjectLocalRulestackResult):
    def __await__(self): # -> Generator[Never, Any, GetCertificateObjectLocalRulestackResult]:
        ...
    


def get_certificate_object_local_rulestack(local_rulestack_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCertificateObjectLocalRulestackResult:
    
    ...

def get_certificate_object_local_rulestack_output(local_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCertificateObjectLocalRulestackResult]:
    
    ...

