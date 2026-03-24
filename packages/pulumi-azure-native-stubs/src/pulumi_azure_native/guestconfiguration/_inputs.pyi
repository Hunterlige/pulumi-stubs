

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConfigurationParameterArgs', 'ConfigurationParameterArgsDict', 'GuestConfigurationAssignmentPropertiesArgs', 'GuestConfigurationAssignmentPropertiesArgsDict', 'GuestConfigurationNavigationArgs', 'GuestConfigurationNavigationArgsDict']
class ConfigurationParameterArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConfigurationParameterArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GuestConfigurationAssignmentPropertiesArgsDict(TypedDict):
    
    context: NotRequired[pulumi.Input[_builtins.str]]
    guest_configuration: NotRequired[pulumi.Input[GuestConfigurationNavigationArgsDict]]


@pulumi.input_type
class GuestConfigurationAssignmentPropertiesArgs:
    def __init__(__self__, *, context: Optional[pulumi.Input[_builtins.str]] = ..., guest_configuration: Optional[pulumi.Input[GuestConfigurationNavigationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @context.setter
    def context(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestConfiguration")
    def guest_configuration(self) -> Optional[pulumi.Input[GuestConfigurationNavigationArgs]]:
        
        ...
    
    @guest_configuration.setter
    def guest_configuration(self, value: Optional[pulumi.Input[GuestConfigurationNavigationArgs]]): # -> None:
        ...
    


class GuestConfigurationNavigationArgsDict(TypedDict):
    
    assignment_type: NotRequired[pulumi.Input[Union[_builtins.str, AssignmentType]]]
    configuration_parameter: NotRequired[pulumi.Input[Sequence[pulumi.Input[ConfigurationParameterArgsDict]]]]
    configuration_protected_parameter: NotRequired[pulumi.Input[Sequence[pulumi.Input[ConfigurationParameterArgsDict]]]]
    content_hash: NotRequired[pulumi.Input[_builtins.str]]
    content_managed_identity: NotRequired[pulumi.Input[_builtins.str]]
    content_uri: NotRequired[pulumi.Input[_builtins.str]]
    kind: NotRequired[pulumi.Input[Union[_builtins.str, Kind]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GuestConfigurationNavigationArgs:
    def __init__(__self__, *, assignment_type: Optional[pulumi.Input[Union[_builtins.str, AssignmentType]]] = ..., configuration_parameter: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationParameterArgs]]]] = ..., configuration_protected_parameter: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationParameterArgs]]]] = ..., content_hash: Optional[pulumi.Input[_builtins.str]] = ..., content_managed_identity: Optional[pulumi.Input[_builtins.str]] = ..., content_uri: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[Union[_builtins.str, Kind]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignmentType")
    def assignment_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AssignmentType]]]:
        
        ...
    
    @assignment_type.setter
    def assignment_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AssignmentType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationParameter")
    def configuration_parameter(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationParameterArgs]]]]:
        
        ...
    
    @configuration_parameter.setter
    def configuration_parameter(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationProtectedParameter")
    def configuration_protected_parameter(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationParameterArgs]]]]:
        
        ...
    
    @configuration_protected_parameter.setter
    def configuration_protected_parameter(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigurationParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentHash")
    def content_hash(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_hash.setter
    def content_hash(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentManagedIdentity")
    def content_managed_identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_managed_identity.setter
    def content_managed_identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentUri")
    def content_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_uri.setter
    def content_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, Kind]]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[_builtins.str, Kind]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


