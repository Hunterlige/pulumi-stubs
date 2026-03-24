import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DirectoryConfigArgs", "DirectoryConfig"]

@pulumi.input_type
class DirectoryConfigArgs:
    def __init__(
        __self__,
        *,
        directory_name: pulumi.Input[_builtins.str],
        organizational_unit_distinguished_names: pulumi.Input[
            Sequence[pulumi.Input[_builtins.str]]
        ],
        service_account_credentials: pulumi.Input[
            DirectoryConfigServiceAccountCredentialsArgs
        ],
        certificate_based_auth_properties: Optional[
            pulumi.Input[DirectoryConfigCertificateBasedAuthPropertiesArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> pulumi.Input[_builtins.str]: ...
    @directory_name.setter
    def directory_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitDistinguishedNames")
    def organizational_unit_distinguished_names(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @organizational_unit_distinguished_names.setter
    def organizational_unit_distinguished_names(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountCredentials")
    def service_account_credentials(
        self,
    ) -> pulumi.Input[DirectoryConfigServiceAccountCredentialsArgs]: ...
    @service_account_credentials.setter
    def service_account_credentials(
        self, value: pulumi.Input[DirectoryConfigServiceAccountCredentialsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="certificateBasedAuthProperties")
    def certificate_based_auth_properties(
        self,
    ) -> Optional[pulumi.Input[DirectoryConfigCertificateBasedAuthPropertiesArgs]]: ...
    @certificate_based_auth_properties.setter
    def certificate_based_auth_properties(
        self,
        value: Optional[
            pulumi.Input[DirectoryConfigCertificateBasedAuthPropertiesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _DirectoryConfigState:
    def __init__(
        __self__,
        *,
        certificate_based_auth_properties: Optional[
            pulumi.Input[DirectoryConfigCertificateBasedAuthPropertiesArgs]
        ] = ...,
        created_time: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        organizational_unit_distinguished_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_credentials: Optional[
            pulumi.Input[DirectoryConfigServiceAccountCredentialsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateBasedAuthProperties")
    def certificate_based_auth_properties(
        self,
    ) -> Optional[pulumi.Input[DirectoryConfigCertificateBasedAuthPropertiesArgs]]: ...
    @certificate_based_auth_properties.setter
    def certificate_based_auth_properties(
        self,
        value: Optional[
            pulumi.Input[DirectoryConfigCertificateBasedAuthPropertiesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_name.setter
    def directory_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitDistinguishedNames")
    def organizational_unit_distinguished_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @organizational_unit_distinguished_names.setter
    def organizational_unit_distinguished_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountCredentials")
    def service_account_credentials(
        self,
    ) -> Optional[pulumi.Input[DirectoryConfigServiceAccountCredentialsArgs]]: ...
    @service_account_credentials.setter
    def service_account_credentials(
        self,
        value: Optional[pulumi.Input[DirectoryConfigServiceAccountCredentialsArgs]],
    ): ...

@pulumi.type_token("aws:appstream/directoryConfig:DirectoryConfig")
class DirectoryConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        certificate_based_auth_properties: Optional[
            pulumi.Input[
                Union[
                    DirectoryConfigCertificateBasedAuthPropertiesArgs,
                    DirectoryConfigCertificateBasedAuthPropertiesArgsDict,
                ]
            ]
        ] = ...,
        directory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        organizational_unit_distinguished_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_credentials: Optional[
            pulumi.Input[
                Union[
                    DirectoryConfigServiceAccountCredentialsArgs,
                    DirectoryConfigServiceAccountCredentialsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DirectoryConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        certificate_based_auth_properties: Optional[
            pulumi.Input[
                Union[
                    DirectoryConfigCertificateBasedAuthPropertiesArgs,
                    DirectoryConfigCertificateBasedAuthPropertiesArgsDict,
                ]
            ]
        ] = ...,
        created_time: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        organizational_unit_distinguished_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_credentials: Optional[
            pulumi.Input[
                Union[
                    DirectoryConfigServiceAccountCredentialsArgs,
                    DirectoryConfigServiceAccountCredentialsArgsDict,
                ]
            ]
        ] = ...,
    ) -> DirectoryConfig: ...
    @_builtins.property
    @pulumi.getter(name="certificateBasedAuthProperties")
    def certificate_based_auth_properties(
        self,
    ) -> pulumi.Output[
        Optional[outputs.DirectoryConfigCertificateBasedAuthProperties]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitDistinguishedNames")
    def organizational_unit_distinguished_names(
        self,
    ) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountCredentials")
    def service_account_credentials(
        self,
    ) -> pulumi.Output[outputs.DirectoryConfigServiceAccountCredentials]: ...
