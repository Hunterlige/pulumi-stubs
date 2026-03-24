

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CxTestCaseArgs', 'CxTestCase']
@pulumi.input_type
class CxTestCaseArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], notes: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., test_case_conversation_turns: Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseTestCaseConversationTurnArgs]]]] = ..., test_config: Optional[pulumi.Input[CxTestCaseTestConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notes.setter
    def notes(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testCaseConversationTurns")
    def test_case_conversation_turns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseTestCaseConversationTurnArgs]]]]:
        
        ...
    
    @test_case_conversation_turns.setter
    def test_case_conversation_turns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseTestCaseConversationTurnArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testConfig")
    def test_config(self) -> Optional[pulumi.Input[CxTestCaseTestConfigArgs]]:
        
        ...
    
    @test_config.setter
    def test_config(self, value: Optional[pulumi.Input[CxTestCaseTestConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _CxTestCaseState:
    def __init__(__self__, *, creation_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., last_test_results: Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseLastTestResultArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notes: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., test_case_conversation_turns: Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseTestCaseConversationTurnArgs]]]] = ..., test_config: Optional[pulumi.Input[CxTestCaseTestConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTestResults")
    def last_test_results(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseLastTestResultArgs]]]]:
        
        ...
    
    @last_test_results.setter
    def last_test_results(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseLastTestResultArgs]]]]): # -> None:
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
    def notes(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notes.setter
    def notes(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testCaseConversationTurns")
    def test_case_conversation_turns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseTestCaseConversationTurnArgs]]]]:
        
        ...
    
    @test_case_conversation_turns.setter
    def test_case_conversation_turns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseTestCaseConversationTurnArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testConfig")
    def test_config(self) -> Optional[pulumi.Input[CxTestCaseTestConfigArgs]]:
        
        ...
    
    @test_config.setter
    def test_config(self, value: Optional[pulumi.Input[CxTestCaseTestConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:diagflow/cxTestCase:CxTestCase")
class CxTestCase(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., notes: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., test_case_conversation_turns: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CxTestCaseTestCaseConversationTurnArgs, CxTestCaseTestCaseConversationTurnArgsDict]]]]] = ..., test_config: Optional[pulumi.Input[Union[CxTestCaseTestConfigArgs, CxTestCaseTestConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CxTestCaseArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., creation_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., last_test_results: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CxTestCaseLastTestResultArgs, CxTestCaseLastTestResultArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notes: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., test_case_conversation_turns: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CxTestCaseTestCaseConversationTurnArgs, CxTestCaseTestCaseConversationTurnArgsDict]]]]] = ..., test_config: Optional[pulumi.Input[Union[CxTestCaseTestConfigArgs, CxTestCaseTestConfigArgsDict]]] = ...) -> CxTestCase:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTestResults")
    def last_test_results(self) -> pulumi.Output[Sequence[outputs.CxTestCaseLastTestResult]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testCaseConversationTurns")
    def test_case_conversation_turns(self) -> pulumi.Output[Optional[Sequence[outputs.CxTestCaseTestCaseConversationTurn]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testConfig")
    def test_config(self) -> pulumi.Output[Optional[outputs.CxTestCaseTestConfig]]:
        
        ...
    


