import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GroupExternalIdArgs",
    "GroupExternalIdArgsDict",
    "UserAddressesArgs",
    "UserAddressesArgsDict",
    "UserEmailsArgs",
    "UserEmailsArgsDict",
    "UserExternalIdArgs",
    "UserExternalIdArgsDict",
    "UserNameArgs",
    "UserNameArgsDict",
    "UserPhoneNumbersArgs",
    "UserPhoneNumbersArgsDict",
    "GetGroupAlternateIdentifierArgs",
    "GetGroupAlternateIdentifierArgsDict",
    "GetGroupAlternateIdentifierExternalIdArgs",
    "GetGroupAlternateIdentifierExternalIdArgsDict",
    "GetGroupAlternateIdentifierUniqueAttributeArgs",
    "GetGroupAlternateIdentifierUniqueAttributeArgsDict",
    "GetUserAlternateIdentifierArgs",
    "GetUserAlternateIdentifierArgsDict",
    "GetUserAlternateIdentifierExternalIdArgs",
    "GetUserAlternateIdentifierExternalIdArgsDict",
    "GetUserAlternateIdentifierUniqueAttributeArgs",
    "GetUserAlternateIdentifierUniqueAttributeArgsDict",
]

class GroupExternalIdArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    issuer: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupExternalIdArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        issuer: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserAddressesArgsDict(TypedDict):
    country: NotRequired[pulumi.Input[_builtins.str]]
    formatted: NotRequired[pulumi.Input[_builtins.str]]
    locality: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    primary: NotRequired[pulumi.Input[_builtins.bool]]
    region: NotRequired[pulumi.Input[_builtins.str]]
    street_address: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserAddressesArgs:
    def __init__(
        __self__,
        *,
        country: Optional[pulumi.Input[_builtins.str]] = ...,
        formatted: Optional[pulumi.Input[_builtins.str]] = ...,
        locality: Optional[pulumi.Input[_builtins.str]] = ...,
        postal_code: Optional[pulumi.Input[_builtins.str]] = ...,
        primary: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        street_address: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @country.setter
    def country(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def formatted(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @formatted.setter
    def formatted(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @locality.setter
    def locality(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary.setter
    def primary(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @street_address.setter
    def street_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserEmailsArgsDict(TypedDict):
    primary: NotRequired[pulumi.Input[_builtins.bool]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserEmailsArgs:
    def __init__(
        __self__,
        *,
        primary: Optional[pulumi.Input[_builtins.bool]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary.setter
    def primary(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserExternalIdArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    issuer: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserExternalIdArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        issuer: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserNameArgsDict(TypedDict):
    family_name: pulumi.Input[_builtins.str]
    given_name: pulumi.Input[_builtins.str]
    formatted: NotRequired[pulumi.Input[_builtins.str]]
    honorific_prefix: NotRequired[pulumi.Input[_builtins.str]]
    honorific_suffix: NotRequired[pulumi.Input[_builtins.str]]
    middle_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserNameArgs:
    def __init__(
        __self__,
        *,
        family_name: pulumi.Input[_builtins.str],
        given_name: pulumi.Input[_builtins.str],
        formatted: Optional[pulumi.Input[_builtins.str]] = ...,
        honorific_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        honorific_suffix: Optional[pulumi.Input[_builtins.str]] = ...,
        middle_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="familyName")
    def family_name(self) -> pulumi.Input[_builtins.str]: ...
    @family_name.setter
    def family_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="givenName")
    def given_name(self) -> pulumi.Input[_builtins.str]: ...
    @given_name.setter
    def given_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def formatted(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @formatted.setter
    def formatted(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="honorificPrefix")
    def honorific_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @honorific_prefix.setter
    def honorific_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="honorificSuffix")
    def honorific_suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @honorific_suffix.setter
    def honorific_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="middleName")
    def middle_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @middle_name.setter
    def middle_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserPhoneNumbersArgsDict(TypedDict):
    primary: NotRequired[pulumi.Input[_builtins.bool]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserPhoneNumbersArgs:
    def __init__(
        __self__,
        *,
        primary: Optional[pulumi.Input[_builtins.bool]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary.setter
    def primary(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GetGroupAlternateIdentifierArgsDict(TypedDict):
    external_id: NotRequired[GetGroupAlternateIdentifierExternalIdArgsDict]
    unique_attribute: NotRequired[GetGroupAlternateIdentifierUniqueAttributeArgsDict]

@pulumi.input_type
class GetGroupAlternateIdentifierArgs:
    def __init__(
        __self__,
        *,
        external_id: Optional[GetGroupAlternateIdentifierExternalIdArgs] = ...,
        unique_attribute: Optional[
            GetGroupAlternateIdentifierUniqueAttributeArgs
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[GetGroupAlternateIdentifierExternalIdArgs]: ...
    @external_id.setter
    def external_id(
        self, value: Optional[GetGroupAlternateIdentifierExternalIdArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="uniqueAttribute")
    def unique_attribute(
        self,
    ) -> Optional[GetGroupAlternateIdentifierUniqueAttributeArgs]: ...
    @unique_attribute.setter
    def unique_attribute(
        self, value: Optional[GetGroupAlternateIdentifierUniqueAttributeArgs]
    ): ...

class GetGroupAlternateIdentifierExternalIdArgsDict(TypedDict):
    id: _builtins.str
    issuer: _builtins.str

@pulumi.input_type
class GetGroupAlternateIdentifierExternalIdArgs:
    def __init__(__self__, *, id: _builtins.str, issuer: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @id.setter
    def id(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @issuer.setter
    def issuer(self, value: _builtins.str): ...

class GetGroupAlternateIdentifierUniqueAttributeArgsDict(TypedDict):
    attribute_path: _builtins.str
    attribute_value: _builtins.str

@pulumi.input_type
class GetGroupAlternateIdentifierUniqueAttributeArgs:
    def __init__(
        __self__, *, attribute_path: _builtins.str, attribute_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributePath")
    def attribute_path(self) -> _builtins.str: ...
    @attribute_path.setter
    def attribute_path(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> _builtins.str: ...
    @attribute_value.setter
    def attribute_value(self, value: _builtins.str): ...

class GetUserAlternateIdentifierArgsDict(TypedDict):
    external_id: NotRequired[GetUserAlternateIdentifierExternalIdArgsDict]
    unique_attribute: NotRequired[GetUserAlternateIdentifierUniqueAttributeArgsDict]

@pulumi.input_type
class GetUserAlternateIdentifierArgs:
    def __init__(
        __self__,
        *,
        external_id: Optional[GetUserAlternateIdentifierExternalIdArgs] = ...,
        unique_attribute: Optional[GetUserAlternateIdentifierUniqueAttributeArgs] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[GetUserAlternateIdentifierExternalIdArgs]: ...
    @external_id.setter
    def external_id(
        self, value: Optional[GetUserAlternateIdentifierExternalIdArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="uniqueAttribute")
    def unique_attribute(
        self,
    ) -> Optional[GetUserAlternateIdentifierUniqueAttributeArgs]: ...
    @unique_attribute.setter
    def unique_attribute(
        self, value: Optional[GetUserAlternateIdentifierUniqueAttributeArgs]
    ): ...

class GetUserAlternateIdentifierExternalIdArgsDict(TypedDict):
    id: _builtins.str
    issuer: _builtins.str

@pulumi.input_type
class GetUserAlternateIdentifierExternalIdArgs:
    def __init__(__self__, *, id: _builtins.str, issuer: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @id.setter
    def id(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @issuer.setter
    def issuer(self, value: _builtins.str): ...

class GetUserAlternateIdentifierUniqueAttributeArgsDict(TypedDict):
    attribute_path: _builtins.str
    attribute_value: _builtins.str

@pulumi.input_type
class GetUserAlternateIdentifierUniqueAttributeArgs:
    def __init__(
        __self__, *, attribute_path: _builtins.str, attribute_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributePath")
    def attribute_path(self) -> _builtins.str: ...
    @attribute_path.setter
    def attribute_path(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> _builtins.str: ...
    @attribute_value.setter
    def attribute_value(self, value: _builtins.str): ...
