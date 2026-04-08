import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ClusterClusterCertificateArgs", "ClusterClusterCertificateArgsDict"]

class ClusterClusterCertificateArgsDict(TypedDict):
    aws_hardware_certificate: NotRequired[pulumi.Input[_builtins.str]]
    cluster_certificate: NotRequired[pulumi.Input[_builtins.str]]
    cluster_csr: NotRequired[pulumi.Input[_builtins.str]]
    hsm_certificate: NotRequired[pulumi.Input[_builtins.str]]
    manufacturer_hardware_certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterClusterCertificateArgs:
    def __init__(
        __self__,
        *,
        aws_hardware_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_csr: Optional[pulumi.Input[_builtins.str]] = ...,
        hsm_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        manufacturer_hardware_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsHardwareCertificate")
    def aws_hardware_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_hardware_certificate.setter
    def aws_hardware_certificate(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterCertificate")
    def cluster_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_certificate.setter
    def cluster_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterCsr")
    def cluster_csr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_csr.setter
    def cluster_csr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hsmCertificate")
    def hsm_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hsm_certificate.setter
    def hsm_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manufacturerHardwareCertificate")
    def manufacturer_hardware_certificate(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @manufacturer_hardware_certificate.setter
    def manufacturer_hardware_certificate(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
