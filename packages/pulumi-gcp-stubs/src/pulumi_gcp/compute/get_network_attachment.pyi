

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkAttachmentResult', 'AwaitableGetNetworkAttachmentResult', 'get_network_attachment', 'get_network_attachment_output']
@pulumi.output_type
class GetNetworkAttachmentResult:
    
    def __init__(__self__, connection_endpoints=..., connection_preference=..., creation_timestamp=..., description=..., fingerprint=..., id=..., kind=..., name=..., network=..., producer_accept_lists=..., producer_reject_lists=..., project=..., region=..., self_link=..., self_link_with_id=..., subnetworks=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionEndpoints")
    def connection_endpoints(self) -> Sequence[outputs.GetNetworkAttachmentConnectionEndpointResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPreference")
    def connection_preference(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="producerAcceptLists")
    def producer_accept_lists(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="producerRejectLists")
    def producer_reject_lists(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetworks(self) -> Sequence[_builtins.str]:
        ...
    


class AwaitableGetNetworkAttachmentResult(GetNetworkAttachmentResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkAttachmentResult]:
        ...
    


def get_network_attachment(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkAttachmentResult:
    
    ...

def get_network_attachment_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkAttachmentResult]:
    
    ...

