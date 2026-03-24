import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SslCertArgs", "SslCert"]

@pulumi.input_type
class SslCertArgs:
    def __init__(
        __self__,
        *,
        common_name: pulumi.Input[_builtins.str],
        instance: pulumi.Input[_builtins.str],
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> pulumi.Input[_builtins.str]: ...
    @common_name.setter
    def common_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Input[_builtins.str]: ...
    @instance.setter
    def instance(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _SslCertState:
    def __init__(
        __self__,
        *,
        cert: Optional[pulumi.Input[_builtins.str]] = ...,
        cert_serial_number: Optional[pulumi.Input[_builtins.str]] = ...,
        common_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        expiration_time: Optional[pulumi.Input[_builtins.str]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        private_key: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        server_ca_cert: Optional[pulumi.Input[_builtins.str]] = ...,
        sha1_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cert.setter
    def cert(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certSerialNumber")
    def cert_serial_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cert_serial_number.setter
    def cert_serial_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @common_name.setter
    def common_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiration_time.setter
    def expiration_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverCaCert")
    def server_ca_cert(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_ca_cert.setter
    def server_ca_cert(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sha1Fingerprint")
    def sha1_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha1_fingerprint.setter
    def sha1_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:sql/sslCert:SslCert")
class SslCert(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        common_name: Optional[pulumi.Input[_builtins.str]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SslCertArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        cert: Optional[pulumi.Input[_builtins.str]] = ...,
        cert_serial_number: Optional[pulumi.Input[_builtins.str]] = ...,
        common_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        expiration_time: Optional[pulumi.Input[_builtins.str]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        private_key: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        server_ca_cert: Optional[pulumi.Input[_builtins.str]] = ...,
        sha1_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SslCert: ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certSerialNumber")
    def cert_serial_number(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serverCaCert")
    def server_ca_cert(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sha1Fingerprint")
    def sha1_fingerprint(self) -> pulumi.Output[_builtins.str]: ...
