

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListArtifactStorePrivateEndPointsResult', 'AwaitableListArtifactStorePrivateEndPointsResult', 'list_artifact_store_private_end_points', 'list_artifact_store_private_end_points_output']
@pulumi.output_type
class ListArtifactStorePrivateEndPointsResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.ArtifactStorePrivateEndPointsFormatResponse]]:
        
        ...
    


class AwaitableListArtifactStorePrivateEndPointsResult(ListArtifactStorePrivateEndPointsResult):
    def __await__(self): # -> Generator[Never, Any, ListArtifactStorePrivateEndPointsResult]:
        ...
    


def list_artifact_store_private_end_points(artifact_store_name: Optional[_builtins.str] = ..., publisher_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListArtifactStorePrivateEndPointsResult:
    
    ...

def list_artifact_store_private_end_points_output(artifact_store_name: Optional[pulumi.Input[_builtins.str]] = ..., publisher_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListArtifactStorePrivateEndPointsResult]:
    
    ...

