

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetKMSCryptoKeyResult', 'AwaitableGetKMSCryptoKeyResult', 'get_kms_crypto_key', 'get_kms_crypto_key_output']
@pulumi.output_type
class GetKMSCryptoKeyResult:
    
    def __init__(__self__, crypto_key_backend=..., destroy_scheduled_duration=..., effective_labels=..., id=..., import_only=..., key_access_justifications_policies=..., key_ring=..., labels=..., name=..., primaries=..., pulumi_labels=..., purpose=..., rotation_period=..., skip_initial_version_creation=..., version_templates=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyBackend")
    def crypto_key_backend(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destroyScheduledDuration")
    def destroy_scheduled_duration(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importOnly")
    def import_only(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAccessJustificationsPolicies")
    def key_access_justifications_policies(self) -> Sequence[outputs.GetKMSCryptoKeyKeyAccessJustificationsPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyRing")
    def key_ring(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def primaries(self) -> Sequence[outputs.GetKMSCryptoKeyPrimaryResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def purpose(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipInitialVersionCreation")
    def skip_initial_version_creation(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionTemplates")
    def version_templates(self) -> Sequence[outputs.GetKMSCryptoKeyVersionTemplateResult]:
        ...
    


class AwaitableGetKMSCryptoKeyResult(GetKMSCryptoKeyResult):
    def __await__(self): # -> Generator[Never, Any, GetKMSCryptoKeyResult]:
        ...
    


def get_kms_crypto_key(key_ring: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetKMSCryptoKeyResult:
    
    ...

def get_kms_crypto_key_output(key_ring: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetKMSCryptoKeyResult]:
    
    ...

