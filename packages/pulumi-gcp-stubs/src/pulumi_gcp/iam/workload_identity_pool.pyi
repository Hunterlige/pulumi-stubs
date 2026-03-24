

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkloadIdentityPoolArgs', 'WorkloadIdentityPool']
@pulumi.input_type
class WorkloadIdentityPoolArgs:
    def __init__(__self__, *, workload_identity_pool_id: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., inline_certificate_issuance_config: Optional[pulumi.Input[WorkloadIdentityPoolInlineCertificateIssuanceConfigArgs]] = ..., inline_trust_config: Optional[pulumi.Input[WorkloadIdentityPoolInlineTrustConfigArgs]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolId")
    def workload_identity_pool_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workload_identity_pool_id.setter
    def workload_identity_pool_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inlineCertificateIssuanceConfig")
    def inline_certificate_issuance_config(self) -> Optional[pulumi.Input[WorkloadIdentityPoolInlineCertificateIssuanceConfigArgs]]:
        
        ...
    
    @inline_certificate_issuance_config.setter
    def inline_certificate_issuance_config(self, value: Optional[pulumi.Input[WorkloadIdentityPoolInlineCertificateIssuanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inlineTrustConfig")
    def inline_trust_config(self) -> Optional[pulumi.Input[WorkloadIdentityPoolInlineTrustConfigArgs]]:
        
        ...
    
    @inline_trust_config.setter
    def inline_trust_config(self, value: Optional[pulumi.Input[WorkloadIdentityPoolInlineTrustConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _WorkloadIdentityPoolState:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., inline_certificate_issuance_config: Optional[pulumi.Input[WorkloadIdentityPoolInlineCertificateIssuanceConfigArgs]] = ..., inline_trust_config: Optional[pulumi.Input[WorkloadIdentityPoolInlineTrustConfigArgs]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., workload_identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inlineCertificateIssuanceConfig")
    def inline_certificate_issuance_config(self) -> Optional[pulumi.Input[WorkloadIdentityPoolInlineCertificateIssuanceConfigArgs]]:
        
        ...
    
    @inline_certificate_issuance_config.setter
    def inline_certificate_issuance_config(self, value: Optional[pulumi.Input[WorkloadIdentityPoolInlineCertificateIssuanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inlineTrustConfig")
    def inline_trust_config(self) -> Optional[pulumi.Input[WorkloadIdentityPoolInlineTrustConfigArgs]]:
        
        ...
    
    @inline_trust_config.setter
    def inline_trust_config(self, value: Optional[pulumi.Input[WorkloadIdentityPoolInlineTrustConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolId")
    def workload_identity_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workload_identity_pool_id.setter
    def workload_identity_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:iam/workloadIdentityPool:WorkloadIdentityPool")
class WorkloadIdentityPool(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., inline_certificate_issuance_config: Optional[pulumi.Input[Union[WorkloadIdentityPoolInlineCertificateIssuanceConfigArgs, WorkloadIdentityPoolInlineCertificateIssuanceConfigArgsDict]]] = ..., inline_trust_config: Optional[pulumi.Input[Union[WorkloadIdentityPoolInlineTrustConfigArgs, WorkloadIdentityPoolInlineTrustConfigArgsDict]]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., workload_identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkloadIdentityPoolArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., inline_certificate_issuance_config: Optional[pulumi.Input[Union[WorkloadIdentityPoolInlineCertificateIssuanceConfigArgs, WorkloadIdentityPoolInlineCertificateIssuanceConfigArgsDict]]] = ..., inline_trust_config: Optional[pulumi.Input[Union[WorkloadIdentityPoolInlineTrustConfigArgs, WorkloadIdentityPoolInlineTrustConfigArgsDict]]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., workload_identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ...) -> WorkloadIdentityPool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inlineCertificateIssuanceConfig")
    def inline_certificate_issuance_config(self) -> pulumi.Output[Optional[outputs.WorkloadIdentityPoolInlineCertificateIssuanceConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inlineTrustConfig")
    def inline_trust_config(self) -> pulumi.Output[Optional[outputs.WorkloadIdentityPoolInlineTrustConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolId")
    def workload_identity_pool_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


