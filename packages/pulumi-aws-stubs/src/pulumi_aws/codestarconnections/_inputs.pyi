import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["HostVpcConfigurationArgs", "HostVpcConfigurationArgsDict"]

class HostVpcConfigurationArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    vpc_id: pulumi.Input[_builtins.str]
    tls_certificate: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HostVpcConfigurationArgs:
    def __init__(
        __self__,
        *,
        security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        vpc_id: pulumi.Input[_builtins.str],
        tls_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tlsCertificate")
    def tls_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tls_certificate.setter
    def tls_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
