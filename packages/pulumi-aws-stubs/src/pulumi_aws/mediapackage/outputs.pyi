

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ChannelHlsIngest', 'ChannelHlsIngestIngestEndpoint']
@pulumi.output_type
class ChannelHlsIngest(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ingest_endpoints: Optional[Sequence[outputs.ChannelHlsIngestIngestEndpoint]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestEndpoints")
    def ingest_endpoints(self) -> Optional[Sequence[outputs.ChannelHlsIngestIngestEndpoint]]:
        
        ...
    


@pulumi.output_type
class ChannelHlsIngestIngestEndpoint(dict):
    def __init__(__self__, *, password: Optional[_builtins.str] = ..., url: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


