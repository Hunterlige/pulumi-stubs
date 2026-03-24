

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRegionalSecretResult', 'AwaitableGetRegionalSecretResult', 'get_regional_secret', 'get_regional_secret_output']
@pulumi.output_type
class GetRegionalSecretResult:
    
    def __init__(__self__, annotations=..., create_time=..., customer_managed_encryptions=..., deletion_protection=..., effective_annotations=..., effective_labels=..., expire_time=..., id=..., labels=..., location=..., name=..., project=..., pulumi_labels=..., rotations=..., secret_id=..., tags=..., topics=..., ttl=..., version_aliases=..., version_destroy_ttl=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedEncryptions")
    def customer_managed_encryptions(self) -> Sequence[outputs.GetRegionalSecretCustomerManagedEncryptionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
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
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rotations(self) -> Sequence[outputs.GetRegionalSecretRotationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def topics(self) -> Sequence[outputs.GetRegionalSecretTopicResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionAliases")
    def version_aliases(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionDestroyTtl")
    def version_destroy_ttl(self) -> _builtins.str:
        ...
    


class AwaitableGetRegionalSecretResult(GetRegionalSecretResult):
    def __await__(self): # -> Generator[Never, Any, GetRegionalSecretResult]:
        ...
    


def get_regional_secret(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., secret_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRegionalSecretResult:
    
    ...

def get_regional_secret_output(location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., secret_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRegionalSecretResult]:
    
    ...

