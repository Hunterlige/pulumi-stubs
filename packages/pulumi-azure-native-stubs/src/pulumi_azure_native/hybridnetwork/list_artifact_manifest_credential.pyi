

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListArtifactManifestCredentialResult', 'AwaitableListArtifactManifestCredentialResult', 'list_artifact_manifest_credential', 'list_artifact_manifest_credential_output']
@pulumi.output_type
class ListArtifactManifestCredentialResult:
    
    def __init__(__self__, credential_type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialType")
    def credential_type(self) -> _builtins.str:
        
        ...
    


class AwaitableListArtifactManifestCredentialResult(ListArtifactManifestCredentialResult):
    def __await__(self): # -> Generator[Never, Any, ListArtifactManifestCredentialResult]:
        ...
    


def list_artifact_manifest_credential(artifact_manifest_name: Optional[_builtins.str] = ..., artifact_store_name: Optional[_builtins.str] = ..., publisher_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListArtifactManifestCredentialResult:
    
    ...

def list_artifact_manifest_credential_output(artifact_manifest_name: Optional[pulumi.Input[_builtins.str]] = ..., artifact_store_name: Optional[pulumi.Input[_builtins.str]] = ..., publisher_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListArtifactManifestCredentialResult]:
    
    ...

