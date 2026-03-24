

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterClusterCertificate', 'GetClusterClusterCertificateResult']
@pulumi.output_type
class ClusterClusterCertificate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_hardware_certificate: Optional[_builtins.str] = ..., cluster_certificate: Optional[_builtins.str] = ..., cluster_csr: Optional[_builtins.str] = ..., hsm_certificate: Optional[_builtins.str] = ..., manufacturer_hardware_certificate: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsHardwareCertificate")
    def aws_hardware_certificate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterCertificate")
    def cluster_certificate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterCsr")
    def cluster_csr(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmCertificate")
    def hsm_certificate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manufacturerHardwareCertificate")
    def manufacturer_hardware_certificate(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetClusterClusterCertificateResult(dict):
    def __init__(__self__, *, aws_hardware_certificate: _builtins.str, cluster_certificate: _builtins.str, cluster_csr: _builtins.str, hsm_certificate: _builtins.str, manufacturer_hardware_certificate: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsHardwareCertificate")
    def aws_hardware_certificate(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterCertificate")
    def cluster_certificate(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterCsr")
    def cluster_csr(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmCertificate")
    def hsm_certificate(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manufacturerHardwareCertificate")
    def manufacturer_hardware_certificate(self) -> _builtins.str:
        
        ...
    


