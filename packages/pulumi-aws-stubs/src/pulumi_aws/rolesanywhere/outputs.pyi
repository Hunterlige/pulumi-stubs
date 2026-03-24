

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TrustAnchorNotificationSetting', 'TrustAnchorSource', 'TrustAnchorSourceSourceData']
@pulumi.output_type
class TrustAnchorNotificationSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel: Optional[_builtins.str] = ..., configured_by: Optional[_builtins.str] = ..., enabled: Optional[_builtins.bool] = ..., event: Optional[_builtins.str] = ..., threshold: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configuredBy")
    def configured_by(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def event(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class TrustAnchorSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_data: outputs.TrustAnchorSourceSourceData, source_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceData")
    def source_data(self) -> outputs.TrustAnchorSourceSourceData:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TrustAnchorSourceSourceData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, acm_pca_arn: Optional[_builtins.str] = ..., x509_certificate_data: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acmPcaArn")
    def acm_pca_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="x509CertificateData")
    def x509_certificate_data(self) -> Optional[_builtins.str]:
        ...
    


