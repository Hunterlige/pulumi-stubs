

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListContainerAppCustomHostNameAnalysisResult', ..., 'list_container_app_custom_host_name_analysis', ...]
@pulumi.output_type
class ListContainerAppCustomHostNameAnalysisResult:
    
    def __init__(__self__, a_records=..., alternate_c_name_records=..., alternate_txt_records=..., c_name_records=..., conflict_with_environment_custom_domain=..., conflicting_container_app_resource_id=..., custom_domain_verification_failure_info=..., custom_domain_verification_test=..., has_conflict_on_managed_environment=..., host_name=..., is_hostname_already_verified=..., txt_records=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aRecords")
    def a_records(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternateCNameRecords")
    def alternate_c_name_records(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternateTxtRecords")
    def alternate_txt_records(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cNameRecords")
    def c_name_records(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictWithEnvironmentCustomDomain")
    def conflict_with_environment_custom_domain(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictingContainerAppResourceId")
    def conflicting_container_app_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainVerificationFailureInfo")
    def custom_domain_verification_failure_info(self) -> outputs.CustomHostnameAnalysisResultResponseCustomDomainVerificationFailureInfo:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainVerificationTest")
    def custom_domain_verification_test(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasConflictOnManagedEnvironment")
    def has_conflict_on_managed_environment(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isHostnameAlreadyVerified")
    def is_hostname_already_verified(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="txtRecords")
    def txt_records(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableListContainerAppCustomHostNameAnalysisResult(ListContainerAppCustomHostNameAnalysisResult):
    def __await__(self): # -> Generator[Never, Any, ListContainerAppCustomHostNameAnalysisResult]:
        ...
    


def list_container_app_custom_host_name_analysis(container_app_name: Optional[_builtins.str] = ..., custom_hostname: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListContainerAppCustomHostNameAnalysisResult:
    
    ...

def list_container_app_custom_host_name_analysis_output(container_app_name: Optional[pulumi.Input[_builtins.str]] = ..., custom_hostname: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListContainerAppCustomHostNameAnalysisResult]:
    
    ...

